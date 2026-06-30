# NationBuilder Hosting Guide

This dashboard is a static generated dashboard. It does not require React, Vite, Node, or Vercel to render in a browser after the HTML is generated.

## Runtime File Inventory

The current dashboard can run from one generated HTML file:

- `outputs/liceh_dashboard_prototype/looker_studio_dashboard_prototype.html`

That file contains:

- HTML markup
- CSS inside a `<style>` block
- JavaScript inside a `<script>` block
- Embedded dashboard data as a JavaScript object
- Inline SVG icons used in the side navigation

Generated supporting files:

- `outputs/liceh_dashboard_prototype/dashboard_data.json`
- `outputs/liceh_dashboard_prototype/liceh_looker_studio_data_source.csv`
- `outputs/liceh_dashboard_prototype/backlog.md`
- `outputs/liceh_dashboard_prototype/calculated_fields_created.md`
- `outputs/liceh_dashboard_prototype/visualizations_created.md`
- `outputs/liceh_dashboard_prototype/public_dashboard_field_review.md`

Editable source files for future updates:

- `data/master-dashboard-data.csv`
- `data/source-documentation.csv`
- `data/dashboard-copy.js`

NationBuilder package files:

- `nationbuilder/town-readiness-dashboard-snippet.html`
- `nationbuilder/town-readiness-dashboard-full.html`
- `nationbuilder/town-readiness-dashboard.css`
- `nationbuilder/town-readiness-dashboard.js`

## External Dependencies

The dashboard has no required local image, font, CSS, JavaScript, or charting-library files.

External runtime dependencies:

- Google Maps iframe embeds are loaded from `https://www.google.com/maps`
- Source links open to their original public URLs
- The LEED description links to `https://www.usgbc.org/leed`

If Google Maps iframes are blocked by NationBuilder or by a visitor's browser, the rest of the dashboard should still render.

## Relative Paths That May Break Inside NationBuilder

The generated dashboard HTML does not currently depend on relative paths for CSS, JavaScript, images, icons, fonts, CSV, or JSON.

The NationBuilder package includes separate CSS and JS files for convenience, but the safest paste option is:

- `nationbuilder/town-readiness-dashboard-snippet.html`

That snippet includes the CSS and JavaScript inline, so there are no `style.css`, `assets/file.js`, `./data/file.csv`, or local image paths to fix.

## Can This Run Directly Inside NationBuilder?

Yes, the generated dashboard can run as a fully static page if NationBuilder allows:

- Custom HTML
- `<style>` tags
- `<script>` tags
- Inline JavaScript
- Google Maps iframe embeds

The most compatible version is the self-contained snippet:

- `nationbuilder/town-readiness-dashboard-snippet.html`

Because the data is embedded in the snippet, it does not need to fetch CSV files at runtime. This avoids common NationBuilder problems with file paths, CORS, and blocked script loading.

## Recommended NationBuilder Setup

### Option A: Paste one self-contained snippet

1. Open `nationbuilder/town-readiness-dashboard-snippet.html`.
2. Copy the full contents.
3. In NationBuilder, open the page template or content area where the dashboard should appear.
4. Paste the snippet into the HTML/source editor.
5. Save and preview the page.

This is the simplest option because no separate CSS, JS, or CSV file paths are required.

### Option B: Upload CSS and JS separately

Use this only if NationBuilder limits large inline HTML snippets.

1. Upload `nationbuilder/town-readiness-dashboard.css` to NationBuilder files.
2. Upload `nationbuilder/town-readiness-dashboard.js` to NationBuilder files.
3. Paste the dashboard HTML markup from `nationbuilder/town-readiness-dashboard-snippet.html`, but remove the inline `<style>` and `<script>` blocks.
4. Add a stylesheet link that points to the uploaded CSS file.
5. Add a script tag that points to the uploaded JS file.

Example:

```html
<link rel="stylesheet" href="REPLACE_WITH_NATIONBUILDER_CSS_FILE_URL">
<!-- Paste the dashboard <main>...</main> markup here. -->
<script src="REPLACE_WITH_NATIONBUILDER_JS_FILE_URL"></script>
```

## CSV and Copy File Uploads

The maintainable source files are:

- `data/master-dashboard-data.csv`
- `data/source-documentation.csv`
- `data/dashboard-copy.js`

For the current self-contained NationBuilder snippet, these files are source files used before the snippet is generated. Uploading them to NationBuilder is useful for recordkeeping, but the pasted dashboard snippet will not automatically reload them.

The JavaScript package includes these placeholder constants for a future live-CSV-loading version:

```js
const DATA_URL = "REPLACE_WITH_NATIONBUILDER_MASTER_DASHBOARD_DATA_CSV_URL";
const SOURCES_URL = "REPLACE_WITH_NATIONBUILDER_SOURCE_DOCUMENTATION_CSV_URL";
const DASHBOARD_COPY_URL = "REPLACE_WITH_NATIONBUILDER_DASHBOARD_COPY_JS_URL";
```

At this stage, those constants are documented placeholders. The current dashboard embeds generated data for maximum NationBuilder compatibility.

## How to Update the Dashboard Later

1. Edit `data/master-dashboard-data.csv`, `data/source-documentation.csv`, or `data/dashboard-copy.js`.
2. Run the generator:

```bash
npm run build
```

3. Recreate the NationBuilder package if needed:

```bash
python3 scripts/create_nationbuilder_package.py
```

If the script is not available, copy the latest generated HTML from `outputs/liceh_dashboard_prototype/looker_studio_dashboard_prototype.html` and ask a technical maintainer to extract the updated snippet.

4. Replace the old snippet in NationBuilder with the new snippet.
5. Save and preview the NationBuilder page.

## How to Test in NationBuilder

After pasting the snippet:

1. Confirm the Overview page renders.
2. Open the Municipality Explorer.
3. Change the municipality selector.
4. Confirm charts and scorecards update.
5. Open the Sources page.
6. Use the Municipality and Category filters.
7. Click a source link and confirm it opens in a new tab.
8. Confirm Google Maps appears or fails gracefully.
9. Test on a mobile-sized screen.

## Fallback: Host on Vercel and Embed With an Iframe

If NationBuilder blocks inline scripts, strips style tags, blocks iframes, or cannot handle the snippet size, use Vercel as the dashboard host and embed it in NationBuilder.

1. Keep the dashboard deployed on Vercel.
2. In NationBuilder, add an iframe:

```html
<iframe
  src="REPLACE_WITH_VERCEL_DASHBOARD_URL"
  title="Town Readiness Assessment Dashboard"
  style="width:100%; min-height:900px; border:0;"
  loading="lazy">
</iframe>
```

3. Save and preview the page.
4. If the iframe feels too short, increase `min-height`.

This fallback is usually the easiest long-term option if non-technical staff will update CSV files in GitHub and rely on automatic redeployment.
