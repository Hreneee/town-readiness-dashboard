from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HTML_PATH = ROOT / "outputs/liceh_dashboard_prototype/looker_studio_dashboard_prototype.html"
OUT = ROOT / "nationbuilder"


CONFIG_COMMENT = """/*
NationBuilder update pointers
- Main dashboard data CSV: data/master-dashboard-data.csv
- Source documentation CSV: data/source-documentation.csv
- Dashboard copy/tooltips: data/dashboard-copy.js

This generated NationBuilder bundle currently embeds dashboard data for maximum compatibility.
If a technical maintainer later ports the dashboard to live CSV loading, replace these placeholders
with the NationBuilder-hosted file URLs and update the CSV loading logic accordingly.
*/
const DATA_URL = "REPLACE_WITH_NATIONBUILDER_MASTER_DASHBOARD_DATA_CSV_URL";
const SOURCES_URL = "REPLACE_WITH_NATIONBUILDER_SOURCE_DOCUMENTATION_CSV_URL";
const DASHBOARD_COPY_URL = "REPLACE_WITH_NATIONBUILDER_DASHBOARD_COPY_JS_URL";
"""


def between(text: str, start: str, end: str, *, last_end: bool = False) -> str:
    start_index = text.index(start) + len(start)
    end_index = text.rindex(end) if last_end else text.index(end, start_index)
    return text[start_index:end_index].strip()


def split_selectors(selector_text: str) -> list[str]:
    selectors: list[str] = []
    current: list[str] = []
    depth = 0
    for char in selector_text:
        if char == "(":
            depth += 1
        elif char == ")" and depth:
            depth -= 1
        if char == "," and depth == 0:
            selectors.append("".join(current).strip())
            current = []
        else:
            current.append(char)
    if current:
        selectors.append("".join(current).strip())
    return selectors


def scope_selector(selector: str) -> str:
    wrapper = "#town-readiness-dashboard-section"
    selector = selector.strip()
    if not selector:
        return selector
    if selector.startswith(".dashboard-tooltip") or selector.startswith(".tooltip-"):
        return selector
    if selector == ":root":
        return wrapper
    if selector == "body":
        return wrapper
    if selector == "html":
        return wrapper
    if selector == "header":
        return f"{wrapper} header"
    if selector == "main":
        return f"{wrapper} .town-readiness-dashboard-main"
    if selector.startswith("body.nav-collapsed main"):
        return selector.replace("body.nav-collapsed main", f"body.nav-collapsed {wrapper} .town-readiness-dashboard-main", 1)
    if selector.startswith("body.nav-collapsed "):
        return selector.replace("body.nav-collapsed ", f"body.nav-collapsed {wrapper} ", 1)
    if selector.startswith(wrapper):
        return selector
    return f"{wrapper} {selector}"


def scope_css(style: str) -> str:
    scoped_lines: list[str] = [
        "/*",
        "NationBuilder-safe dashboard CSS.",
        "All dashboard styles are scoped to #town-readiness-dashboard-section so the normal reLI layout stays visible.",
        "*/",
    ]
    for line in style.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("@") or stripped == "}":
            scoped_lines.append(line)
            continue
        if "{" not in line:
            scoped_lines.append(line)
            continue
        before, after = line.split("{", 1)
        indentation = before[: len(before) - len(before.lstrip())]
        selector_text = before.strip()
        if not selector_text:
            scoped_lines.append(line)
            continue
        scoped_selectors = [scope_selector(selector) for selector in split_selectors(selector_text)]
        scoped_lines.append(f"{indentation}{', '.join(scoped_selectors)} {{{after}")
    return "\n".join(scoped_lines).strip() + "\n"


def nationbuilder_markup(html: str) -> str:
    main_markup = html[html.index("<main>") : html.index("</main>") + len("</main>")].strip()
    inner = main_markup.removeprefix("<main>").removesuffix("</main>").strip()
    return f"""<section id="town-readiness-dashboard-section" class="town-readiness-dashboard-section">
  <div class="town-readiness-dashboard-main" role="region" aria-label="Town Readiness Assessment dashboard">
{inner}
  </div>
</section>"""


def scope_script(script: str) -> str:
    return (
        script.replace(
            "document.querySelectorAll('.section-nav button[data-view]')",
            "document.querySelectorAll('#town-readiness-dashboard-section .section-nav button[data-view]')",
        )
        .replace(
            "document.querySelectorAll('.page')",
            "document.querySelectorAll('#town-readiness-dashboard-section .page')",
        )
        .replace(
            "document.querySelector(`.section-nav button[data-view=\"${target}\"]`)",
            "document.querySelector(`#town-readiness-dashboard-section .section-nav button[data-view=\"${target}\"]`)",
        )
    )


def main() -> None:
    html = HTML_PATH.read_text(encoding="utf-8")
    style = scope_css(between(html, "<style>", "</style>"))
    dashboard_markup = nationbuilder_markup(html)
    script = scope_script(between(html, "<script>", "</script>", last_end=True))
    script_with_comment = f"{CONFIG_COMMENT}\n{script}"

    OUT.mkdir(exist_ok=True)
    (OUT / "town-readiness-dashboard.css").write_text(f"{style}\n", encoding="utf-8")
    (OUT / "town-readiness-dashboard.js").write_text(f"{script_with_comment}\n", encoding="utf-8")
    (OUT / "town_readiness_dashboard.liquid").write_text(f"{dashboard_markup}\n", encoding="utf-8")
    (OUT / "town-readiness-dashboard-snippet.html").write_text(
        f"<style>\n{style}\n</style>\n\n{dashboard_markup}\n\n<script>\n{script_with_comment}\n</script>\n",
        encoding="utf-8",
    )
    (OUT / "town-readiness-dashboard-full.html").write_text(html, encoding="utf-8")


if __name__ == "__main__":
    main()
