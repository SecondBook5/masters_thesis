"""Apply deterministic JHU ETD production fixes to the thesis source.

This helper is intentionally narrow and temporary. It changes only defects identified
in the final PDF audit: the clipped Figure 3.12 caption, unbreakable falsification-ladder
identifiers, and stale/malformed bibliography metadata. It does not alter scientific
results, numerical values, or the August 2026 title-page date.

The script fails loudly if an expected source pattern cannot be found. That behavior is
intentional: silent partial edits are more dangerous than a failed finalization build.
"""

# Import regular-expression support for tightly scoped source substitutions.
import re
# Import sys so fatal validation errors can return a non-zero workflow status.
import sys
# Import Path for explicit repository-relative file handling.
from pathlib import Path

# Define the repository root relative to this temporary helper.
REPO_ROOT: Path = Path(__file__).resolve().parents[1]


def read_text(relative_path: str) -> str:
    """Read one UTF-8 repository text file with explicit validation.

    The finalization workflow operates only on text sources. Centralizing reads here
    gives every edit the same existence, file-type, encoding, and error behavior rather
    than allowing an accidental missing file to become an empty replacement.

    Args:
        relative_path: Repository-relative path to the UTF-8 text file.

    Returns:
        The complete file contents.

    Raises:
        FileNotFoundError: If the requested path does not exist.
        IsADirectoryError: If the requested path resolves to a directory.
        UnicodeError: If the file cannot be decoded as UTF-8.
        OSError: If the file cannot otherwise be read.
    """
    # Resolve the repository-relative source path.
    path: Path = REPO_ROOT / relative_path
    # Reject missing inputs rather than creating partial replacement files.
    if not path.exists():
        # Raise a path-specific error that is useful in CI logs.
        raise FileNotFoundError(f"Required thesis source does not exist: {path}")
    # Reject directories because this helper only edits individual text files.
    if not path.is_file():
        # Raise a precise type error for an unexpected repository layout.
        raise IsADirectoryError(f"Expected a file but found a non-file path: {path}")
    # Read the complete file as UTF-8.
    return path.read_text(encoding="utf-8")


def write_text(relative_path: str, content: str) -> None:
    """Write a validated UTF-8 replacement for one repository text file.

    The function refuses to write an empty file. The thesis sources are large enough
    that a zero-length replacement would almost certainly indicate a failed patching
    step rather than an intentional edit.

    Args:
        relative_path: Repository-relative destination path.
        content: Complete replacement text.

    Raises:
        ValueError: If the replacement content is empty.
        OSError: If the destination cannot be written.
    """
    # Refuse an empty replacement because that would be catastrophic here.
    if not content:
        # Raise an explicit error rather than truncating a thesis source file.
        raise ValueError(f"Refusing to write empty content to {relative_path}")
    # Resolve the destination path inside the repository.
    path: Path = REPO_ROOT / relative_path
    # Write the complete replacement as UTF-8.
    path.write_text(content, encoding="utf-8")


def replace_exact(text: str, old: str, new: str, label: str, expected_count: int = 1) -> str:
    """Replace an exact source block only when its occurrence count is as expected.

    Exact-count validation prevents the finalization pass from silently changing the
    wrong location after upstream edits. If the source has drifted, the workflow stops
    and requires manual inspection instead of guessing.

    Args:
        text: Complete source text.
        old: Exact source block expected in the file.
        new: Exact replacement block.
        label: Human-readable edit name for error messages.
        expected_count: Required number of occurrences of ``old``.

    Returns:
        The patched source text.

    Raises:
        RuntimeError: If the source block occurs a different number of times.
    """
    # Count exact occurrences before modifying the source.
    count: int = text.count(old)
    # Stop if the source no longer matches the audited version.
    if count != expected_count:
        # Report the exact mismatch so the problem is diagnosable from CI logs.
        raise RuntimeError(
            f"{label}: expected {expected_count} exact occurrence(s), found {count}. "
            "Source drift requires manual review."
        )
    # Apply only the validated number of replacements.
    return text.replace(old, new, expected_count)


def patch_results_caption() -> None:
    """Shorten the Figure 3.12 caption so it remains inside the printable page area.

    The rendered audit found the Figure 3.12 caption clipped below the physical page.
    The figure content is left unchanged; only redundant caption prose is compressed.
    This is preferable to shrinking the already information-dense embedded labels.
    """
    # Identify the Results chapter source file.
    relative_path: str = "08-chapter-3.tex"
    # Read the complete audited source.
    text: str = read_text(relative_path)
    # Store the exact caption block that produced the clipped PDF.
    old: str = """  \\caption[Spatial organization of the AAH and AIS microenvironment]{Microenvironment across the AAH
  and AIS Visium sections (tissue coordinates; one sub-panel per section). \\textbf{(a)}~Local malignant
  fraction is concentrated in focal, contiguous foci, more pronounced in several AIS sections.
  \\textbf{(b)}~BANKSY domains partition each section into spatially coherent microenvironments,
  confirming the composition features are spatially structured. These descriptive maps illustrate the
  spatial structure quantified in the text (the monotonic rise in malignant Moran's~$I$ and positive
  within-section autocorrelation); they are not themselves a statistical test.}
"""
    # Define a shorter caption that preserves the same interpretation and caveat.
    new: str = """  \\caption[Spatial organization of the AAH and AIS microenvironment]{AAH and AIS Visium
  microenvironments. \\textbf{(a)}~Malignant-cell fraction forms focal contiguous regions, often more
  pronounced in AIS. \\textbf{(b)}~BANKSY partitions each section into spatially coherent domains.
  These descriptive maps illustrate the spatial structure quantified in the text and are not themselves
  a statistical test.}
"""
    # Replace only the audited Figure 3.12 caption block.
    text = replace_exact(text, old, new, "Figure 3.12 caption")
    # Persist the complete Results source after the validated patch.
    write_text(relative_path, text)


def patch_ladder_identifiers() -> None:
    """Make long Appendix C falsification-ladder identifiers legally line-breakable.

    The PDF audit found identifiers such as ``neural_residuals_only`` and
    ``donor_stage_average_context`` extending beyond the right page boundary. Hyperref's
    ``\\nolinkurl`` provides safe break points at underscores without changing the literal
    identifier, numerical table content, or scientific meaning.
    """
    # Identify the Appendix C source file.
    relative_path: str = "13-appendix-C.tex"
    # Read the complete appendix source.
    text: str = read_text(relative_path)
    # Define the two complete ladder-table regions by their stable labels.
    table_labels: tuple[str, ...] = ("tab:app-c-ladder-aah", "tab:app-c-ladder-inv")
    # Process each audited table independently to avoid touching unrelated identifiers.
    for table_label in table_labels:
        # Locate the table label that uniquely identifies this ladder table.
        label_index: int = text.find(f"\\label{{{table_label}}}")
        # Stop if the audited table cannot be found.
        if label_index < 0:
            # Raise a table-specific source-drift error.
            raise RuntimeError(f"Could not locate Appendix C table label: {table_label}")
        # Find the start of the enclosing table environment.
        table_start: int = text.rfind("\\begin{table}", 0, label_index)
        # Find the end of the enclosing table environment.
        table_end_marker: int = text.find("\\end{table}", label_index)
        # Reject malformed or unexpectedly reorganized source.
        if table_start < 0 or table_end_marker < 0:
            # Report the table whose boundaries could not be resolved.
            raise RuntimeError(f"Could not resolve table boundaries for {table_label}")
        # Include the complete end marker in the extracted region.
        table_end: int = table_end_marker + len("\\end{table}")
        # Extract only this audited table.
        table_text: str = text[table_start:table_end]
        # Define a row matcher whose first field is an underscore-delimited ladder identifier.
        row_pattern: re.Pattern[str] = re.compile(r"^(\s*)([A-Za-z0-9]+(?:\\_[A-Za-z0-9]+)+)(\s*&)", re.MULTILINE)

        # Define the row-level conversion from escaped TeX underscores to a breakable literal URL token.
        def wrap_identifier(match: re.Match[str]) -> str:
            """Wrap one ladder identifier in ``\\nolinkurl`` while preserving row alignment.

            Args:
                match: Regular-expression match for the first table field.

            Returns:
                The replacement first field and original ampersand separator.
            """
            # Preserve the original row indentation.
            indent: str = match.group(1)
            # Convert TeX-escaped underscores back to literal underscores for ``\\nolinkurl``.
            identifier: str = match.group(2).replace("\\_", "_")
            # Preserve the original spacing and column separator.
            separator: str = match.group(3)
            # Return a line-breakable rendering of the exact identifier.
            return f"{indent}\\nolinkurl{{{identifier}}}{separator}"

        # Apply the conversion to every long identifier in this table only.
        patched_table, replacement_count = row_pattern.subn(wrap_identifier, table_text)
        # Require multiple affected rows so a no-op cannot masquerade as a successful fix.
        if replacement_count < 5:
            # Raise a precise count mismatch for diagnostic review.
            raise RuntimeError(
                f"{table_label}: expected multiple ladder identifiers, wrapped only {replacement_count}."
            )
        # Replace the original table region with its breakable-identifier version.
        text = text[:table_start] + patched_table + text[table_end:]
    # Persist the complete Appendix C source after both table fixes.
    write_text(relative_path, text)


def find_bib_entry(text: str, title_fragment: str) -> tuple[int, int, str]:
    """Locate one BibTeX/BibLaTeX entry by a unique title fragment using brace balancing.

    A brace-balanced scan is used instead of a naive regular expression because bibliography
    fields can themselves contain nested braces. The helper requires a unique title fragment
    and returns the complete entry boundaries for safe field-level replacement.

    Args:
        text: Complete bibliography text.
        title_fragment: Unique literal fragment from the target title.

    Returns:
        ``(start, end, entry_text)`` where ``end`` is exclusive.

    Raises:
        RuntimeError: If the title is absent, duplicated, or the entry braces are malformed.
    """
    # Count the title fragment before locating its entry.
    fragment_count: int = text.count(title_fragment)
    # Require one unique matching bibliography record.
    if fragment_count != 1:
        # Stop instead of guessing between missing or duplicated records.
        raise RuntimeError(
            f"Bibliography title fragment {title_fragment!r} occurs {fragment_count} times; expected exactly 1."
        )
    # Locate the title fragment in the bibliography.
    title_index: int = text.index(title_fragment)
    # Find the entry's opening ``@`` before the title.
    entry_start: int = text.rfind("@", 0, title_index)
    # Reject malformed content with no entry opener.
    if entry_start < 0:
        # Raise a title-specific parsing error.
        raise RuntimeError(f"Could not locate BibTeX entry start for {title_fragment!r}")
    # Find the first opening brace of the entry header.
    brace_start: int = text.find("{", entry_start)
    # Reject malformed content with no opening entry brace.
    if brace_start < 0 or brace_start > title_index:
        # Raise a precise structural parsing error.
        raise RuntimeError(f"Could not locate BibTeX opening brace for {title_fragment!r}")
    # Initialize nested-brace depth at the entry opening brace.
    depth: int = 0
    # Walk forward until the matching entry-closing brace is found.
    for index in range(brace_start, len(text)):
        # Read the current character once for clear brace logic.
        char: str = text[index]
        # Increase nesting depth on an opening brace.
        if char == "{":
            # Track nested field braces as part of the entry.
            depth += 1
        # Decrease nesting depth on a closing brace.
        elif char == "}":
            # Account for the closing brace.
            depth -= 1
            # Stop when the entry's outermost brace has closed.
            if depth == 0:
                # Define an exclusive end position immediately after the closing brace.
                entry_end: int = index + 1
                # Return the complete balanced entry.
                return entry_start, entry_end, text[entry_start:entry_end]
        # Detect impossible negative nesting as malformed BibTeX.
        if depth < 0:
            # Raise rather than editing corrupted entry boundaries.
            raise RuntimeError(f"Malformed brace structure while parsing {title_fragment!r}")
    # Reaching EOF without closing the outer brace means the entry is malformed.
    raise RuntimeError(f"Unterminated BibTeX entry for {title_fragment!r}")


def remove_field(entry: str, field_name: str) -> str:
    """Remove one simple BibLaTeX field if it exists.

    Args:
        entry: Complete single BibTeX/BibLaTeX entry.
        field_name: Case-insensitive field name to remove.

    Returns:
        The entry with all matching simple field assignments removed.
    """
    # Match conventional one-line Zotero/BibLaTeX scalar fields.
    pattern: re.Pattern[str] = re.compile(
        rf"(?mi)^\s*{re.escape(field_name)}\s*=\s*(?:\{{[^\n]*\}}|\"[^\n]*\"|[^,\n]+),?\s*\n?"
    )
    # Remove every matching assignment from the entry.
    return pattern.sub("", entry)


def set_field(entry: str, field_name: str, value: str) -> str:
    """Replace or add one simple braced BibLaTeX field.

    Args:
        entry: Complete single BibTeX/BibLaTeX entry.
        field_name: Field name to set.
        value: Unbraced field value.

    Returns:
        The updated entry.

    Raises:
        RuntimeError: If the entry has no closing brace for appending a new field.
    """
    # Define the canonical braced field assignment used by this repository.
    replacement: str = f"  {field_name} = {{{value}}},\n"
    # Match an existing one-line assignment to the same field.
    pattern: re.Pattern[str] = re.compile(
        rf"(?mi)^\s*{re.escape(field_name)}\s*=\s*(?:\{{[^\n]*\}}|\"[^\n]*\"|[^,\n]+),?\s*$"
    )
    # Replace the existing field if one is present.
    if pattern.search(entry):
        # Substitute exactly one canonical field line.
        return pattern.sub(replacement.rstrip("\n"), entry, count=1)
    # Find the final brace of the balanced entry for a missing field.
    closing_index: int = entry.rfind("}")
    # Reject malformed entries rather than appending outside the record.
    if closing_index < 0:
        # Raise a field-specific structural error.
        raise RuntimeError(f"Cannot add {field_name!r}: bibliography entry has no closing brace")
    # Ensure the preceding field has a newline before appending the new field.
    prefix: str = entry[:closing_index].rstrip()
    # Add a trailing comma to the preceding field if necessary.
    if not prefix.endswith(","):
        # Preserve valid BibTeX separation before the appended field.
        prefix += ","
    # Reconstruct the entry with the canonical new field before its closing brace.
    return prefix + "\n" + replacement + entry[closing_index:]


def update_entry_fields(text: str, title_fragment: str, fields: dict[str, str], remove: tuple[str, ...] = ()) -> str:
    """Update fields in one uniquely identified bibliography record.

    Args:
        text: Complete bibliography text.
        title_fragment: Unique literal title fragment identifying the record.
        fields: Field/value pairs to set after removals.
        remove: Field names to remove before setting replacements.

    Returns:
        Complete bibliography text containing the updated record.
    """
    # Locate the complete balanced entry by title.
    start, end, entry = find_bib_entry(text, title_fragment)
    # Remove each obsolete field explicitly.
    for field_name in remove:
        # Apply one field removal to the isolated entry.
        entry = remove_field(entry, field_name)
    # Set each authoritative replacement field.
    for field_name, value in fields.items():
        # Apply the field replacement or insertion.
        entry = set_field(entry, field_name, value)
    # Reinsert the corrected entry into the complete bibliography.
    return text[:start] + entry + text[end:]


def patch_bibliography() -> None:
    """Correct audited bibliography defects without changing citation identities.

    The audit found one objectively malformed final citation (Cancer Cell 0 (0 2025)),
    one newly paginated Nature paper, and three Nature issue numbers rendered as if they
    were part of the year. This function updates final publication metadata and removes
    only the problematic issue-number fields. It also removes redundant English-language
    markers that render as repeated ``en.`` prefixes.
    """
    # Identify the master bibliography.
    relative_path: str = "thesis.bib"
    # Read the complete bibliography text.
    text: str = read_text(relative_path)
    # Update the final Cancer Cell metadata for the Peng spatial-omics paper.
    text = update_entry_fields(
        text,
        "Multimodal spatial-omics reveal co-evolution of alveolar",
        {
            "journaltitle": "Cancer Cell",
            "volume": "44",
            "pages": "321--339.e13",
            "date": "2026",
            "doi": "10.1016/j.ccell.2025.10.004",
        },
        remove=("journal", "year", "number", "issue"),
    )
    # Update the final Nature pagination for the Cardoso fibrotic-niche paper.
    text = update_entry_fields(
        text,
        "Early fibrotic niches establish tumour-permissive microenvironments",
        {
            "journaltitle": "Nature",
            "volume": "653",
            "pages": "254--264",
            "date": "2026",
            "doi": "10.1038/s41586-026-10399-6",
        },
        remove=("journal", "year", "number", "issue"),
    )
    # Define Nature titles whose issue numbers render incorrectly in the current style.
    issue_cleanup_titles: tuple[str, ...] = (
        "Critical role for a high-plasticity cell state in lung cancer",
        "3D genomic mapping reveals multifocality of human pancreatic precancers",
        "Temporal tissue dynamics from a spatial snapshot",
    )
    # Remove only issue/number fields from those otherwise correct records.
    for title_fragment in issue_cleanup_titles:
        # Locate the complete target entry.
        start, end, entry = find_bib_entry(text, title_fragment)
        # Remove the issue-number field if exported as ``number``.
        entry = remove_field(entry, "number")
        # Remove the issue-number field if exported as ``issue``.
        entry = remove_field(entry, "issue")
        # Reinsert the cleaned record.
        text = text[:start] + entry + text[end:]
    # Remove redundant English-only language tags that produce repeated ``en.`` output.
    text, _ = re.subn(r"(?mi)^\s*(?:langid|language)\s*=\s*\{(?:english|en)\},?\s*\n?", "", text)
    # Persist the complete corrected bibliography.
    write_text(relative_path, text)


def main() -> int:
    """Run all ETD production fixes and return an explicit process status.

    The edits are deliberately sequential. Any validation failure aborts the workflow before
    a commit is created, leaving Git history untouched by partial finalization output.

    Returns:
        ``0`` when all validated edits complete successfully; ``1`` on any failure.
    """
    # Wrap the finalization pass so CI receives a clear non-zero status on any exception.
    try:
        # Fix the clipped main-text figure caption without shrinking the embedded figure labels.
        patch_results_caption()
        # Make the Appendix C ladder identifiers breakable at page margins.
        patch_ladder_identifiers()
        # Correct final publication metadata and bibliography rendering defects.
        patch_bibliography()
    # Catch all ordinary exceptions so the workflow log contains a concise failure message.
    except Exception as exc:
        # Emit the exception type and message to standard error for CI diagnostics.
        print(f"ETD finalization failed: {type(exc).__name__}: {exc}", file=sys.stderr)
        # Return a non-zero status so no downstream commit step runs.
        return 1
    # Report successful completion after every validated edit has been written.
    print("ETD finalization patches applied successfully.")
    # Return success to the workflow.
    return 0


# Execute the validated finalization pass only when this file is run as a script.
if __name__ == "__main__":
    # Propagate the explicit status code to the calling workflow.
    raise SystemExit(main())
