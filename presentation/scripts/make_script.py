r"""Extract the spoken script from defense.tex into a standalone readable doc.

Pairs every \begin{frame}{title} (and \actcard) with the \note{...} that follows it,
strips LaTeX to plain readable prose, and writes presentation/defense-script.md.
Stage directions (\cue{...}) are kept, marked as [CUE: ...].

Regenerate after editing the deck:
    python presentation/scripts/make_script.py
"""
import re, os

SRC = "/home/booka/masters_thesis/presentation/defense.tex"
OUT = "/home/booka/masters_thesis/presentation/defense-script.md"

txt = open(SRC).read()
# work only from \begin{document} onward
txt = txt[txt.index(r"\begin{document}"):]

def clean(s):
    """LaTeX -> readable plain text."""
    # drop the leading line-continuation % that follows \note{
    s = re.sub(r"^\s*%\s*\n", "", s)
    # pull \cue{...} out first, mark them
    s = re.sub(r"\\cue\{(.*?)\}", r"\n\n[CUE: \1]\n", s, flags=re.S)
    # common wrappers -> inner text
    for cmd in ["emph", "textbf", "textit", "hl", "text", "mathrm", "color"]:
        # \color{key} takes an arg that is NOT text to keep; drop it
        if cmd == "color":
            s = re.sub(r"\\color\{[^}]*\}", "", s)
            continue
        s = re.sub(r"\\%s\{(.*?)\}" % cmd, r"\1", s, flags=re.S)
    # math: strip $...$ delimiters, keep inner symbol text lightly cleaned
    def mathrepl(m):
        inner = m.group(1)
        inner = inner.replace(r"\tau", "tau").replace(r"\odot", " (elementwise x) ")
        inner = re.sub(r"\\mathrm\{(.*?)\}", r"\1", inner)
        inner = re.sub(r"\\text\{(.*?)\}", r"\1", inner)
        inner = inner.replace(r"\rightarrow", "->").replace(r"\uparrow", "up").replace(r"\downarrow", "down")
        inner = re.sub(r"[{}]", "", inner)
        return inner
    s = re.sub(r"\$(.*?)\$", mathrepl, s, flags=re.S)
    # residual escapes / spacing macros
    s = s.replace(r"\%", "%").replace(r"---", "\u2014").replace(r"--", "\u2013")
    s = s.replace("``", "\u201c").replace("''", "\u201d")   # TeX quotes -> curly
    s = s.replace(r"\emph", "").replace(r"~", " ")
    s = re.sub(r"\\[a-zA-Z]+", "", s)          # drop any leftover control seqs
    s = re.sub(r"[{}]", "", s)
    # tidy whitespace but keep paragraph breaks
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n[ \t]+", "\n", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()

def grab_braced(s, i):
    """Return (content, index-after) for a brace group starting at s[i]=='{'."""
    assert s[i] == "{"
    depth = 0; j = i
    while j < len(s):
        if s[j] == "{": depth += 1
        elif s[j] == "}":
            depth -= 1
            if depth == 0: return s[i+1:j], j+1
        j += 1
    return s[i+1:], len(s)

def title_clean(t):
    for cmd in ["emph", "textbf", "textit", "hl", "text"]:
        t = re.sub(r"\\%s\{(.*?)\}" % cmd, r"\1", t, flags=re.S)
    t = re.sub(r"\$(.*?)\$", lambda m: re.sub(r"[\\{}]", "", m.group(1)), t)
    t = t.replace(r"---", "\u2014").replace(r"--", "\u2013").replace(r"\%", "%")
    t = re.sub(r"\\[a-zA-Z]+", "", t).replace("{", "").replace("}", "").strip()
    return t

# tokenize into ordered (kind, title) markers and note blocks
frames = []
# frame titles (brace-balanced so nested \emph{} in a title is captured whole)
for m in re.finditer(r"\\begin\{frame\}(?:\[[^\]]*\])?\s*\{", txt):
    body, _ = grab_braced(txt, m.end() - 1)
    frames.append((m.start(), "frame", title_clean(body)))
# plain frames with no title (e.g. the "Backup" divider) -- capture so their
# note does not bleed onto the previous titled slide
for m in re.finditer(r"\\begin\{frame\}\[plain\]", txt):
    tail = txt[m.end():m.end()+120]
    lab = "Backup" if "Backup" in tail else ("Title" if "titlepage" in tail else "(section)")
    frames.append((m.start(), "frame" if lab != "(section)" else "act", lab))
for m in re.finditer(r"\\actcard\{", txt):
    a, j = grab_braced(txt, m.end() - 1)
    b, _ = grab_braced(txt, j)
    frames.append((m.start(), "act", f"{title_clean(a)} \u2014 {title_clean(b)}"))
# note blocks: match \note{ ... } with brace balancing
notes = []
for m in re.finditer(r"\\note\{", txt):
    i = m.end(); depth = 1
    while i < len(txt) and depth:
        if txt[i] == "{": depth += 1
        elif txt[i] == "}": depth -= 1
        i += 1
    notes.append((m.start(), txt[m.end():i-1]))

frames.sort()
# attach each note to the most recent frame/act before it
def owner(pos):
    o = None
    for p, kind, title in frames:
        if p < pos: o = (kind, title)
        else: break
    return o

paired = {}   # index in frames order -> note text
note_for = {}
for npos, ntext in notes:
    # find frame index whose position is the largest < npos
    idx = None
    for k, (p, kind, title) in enumerate(frames):
        if p < npos: idx = k
        else: break
    if idx is not None:
        note_for.setdefault(idx, []).append(clean(ntext))

# build markdown
ACT_RE = re.compile(r"^(Act [0IVX]+)")
lines = []
lines.append("# Defense speaker script")
lines.append("")
lines.append("*Niche-Conditioned Regulatory Transport in Premalignant Epithelial Progression* \u2014 "
             "Abraham J. Book. Mentor: Chris Bradburne, PhD.")
lines.append("")
lines.append("Generated from `defense.tex` presenter notes (`make_script.py`). "
             "One section per slide, in order. **[CUE: ...]** lines are stage directions / "
             "anticipated-question prompts, not spoken verbatim. Target ~150 words per slide, "
             "~68 s each across ~40 main slides = 45 min.")
lines.append("")
lines.append("---")
lines.append("")

slide_no = 0
for k, (p, kind, title) in enumerate(frames):
    body = "\n\n".join(note_for.get(k, [])).strip()
    if kind == "act":
        lines.append(f"## {title}")
        lines.append("")
        lines.append("*(section divider slide \u2014 no script; pause, then advance)*")
        lines.append("")
        continue
    slide_no += 1
    lines.append(f"## Slide {slide_no}. {title}")
    lines.append("")
    if body:
        lines.append(body)
    else:
        lines.append("*(no script \u2014 visual/table slide, or backup)*")
    lines.append("")

open(OUT, "w").write("\n".join(lines) + "\n")
nslides = slide_no
nscripted = sum(1 for k in range(len(frames)) if note_for.get(k) and frames[k][1] == "frame")
print(f"wrote {OUT}: {nslides} slides, {nscripted} with script")
