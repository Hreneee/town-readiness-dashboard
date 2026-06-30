# Town Readiness Assessment Dashboard

Static dashboard for the Long Island Clean Energy Hub Town Readiness Assessment.

The published dashboard entry point is:

`outputs/liceh_dashboard_prototype/looker_studio_dashboard_prototype.html`

This repository is currently a static HTML/CSS/JavaScript dashboard generated from editable CSV and copy files. It is not a React/Vite app at this time.

## How to Update the Dashboard

### Update the main dashboard data

The main dashboard data is located at:

`data/master-dashboard-data.csv`

Staff can edit this CSV directly in GitHub or upload a replacement CSV with the same filename. Keep the existing column names. Do not rename columns or delete required fields unless a technical maintainer is also updating the dashboard code.

Blank cells are allowed where information is unavailable. Use the existing missing-value style already present in the file, such as blank cells, `Unavailable`, or `Not available`.

After committing changes to the production branch, Vercel will redeploy automatically. If the generated dashboard HTML is not rebuilt by the deployment workflow, a technical maintainer should run `npm run build` and commit the updated files.

### Update source documentation

Source documentation is located at:

`data/source-documentation.csv`

Use this file for source names, source links, and source categories used to document municipal assessment responses. Each row should include the municipality, category, source name, and URL. The dashboard Sources page displays the source name as a clickable link.

### Update dashboard wording or tooltips

Dashboard wording and tooltip text are located at:

`data/dashboard-copy.js`

Staff should edit text inside quotation marks. Avoid renaming object keys, deleting commas, or changing the object structure unless a technical maintainer is also updating the code.

### How changes go live

1. Edit the relevant file in GitHub.
2. Commit the change to the production branch.
3. Vercel automatically rebuilds or redeploys the site.
4. Wait a few moments for Vercel to finish.
5. Check the live dashboard to confirm the update appears correctly.

### Local development for technical users

Install dependencies:

```bash
npm install
```

Run the dashboard locally:

```bash
npm run dev
```

Rebuild the generated dashboard files:

```bash
npm run build
```

Rebuild the NationBuilder-ready files:

```bash
npm run build:nationbuilder
```

## Project Structure

- `data/master-dashboard-data.csv` - editable master dashboard data.
- `data/source-documentation.csv` - editable source documentation for the Sources page.
- `data/dashboard-copy.js` - editable public copy and tooltip text.
- `work/refine_liceh_dashboard.py` - generator that rebuilds the static dashboard from the editable files.
- `nationbuilder/town-readiness-dashboard-snippet.html` - self-contained NationBuilder paste snippet.
- `nationbuilder/town-readiness-dashboard.css` - optional separated CSS for NationBuilder.
- `nationbuilder/town-readiness-dashboard.js` - optional separated JavaScript for NationBuilder.
- `docs/nationbuilder-hosting-guide.md` - NationBuilder hosting and fallback instructions.
- `outputs/liceh_dashboard_prototype/looker_studio_dashboard_prototype.html` - generated dashboard page.
- `outputs/liceh_dashboard_prototype/dashboard_data.json` - generated structured data export.
- `outputs/liceh_dashboard_prototype/liceh_looker_studio_data_source.csv` - generated tabular data export.

## Vercel

`vercel.json` rewrites the site root to the generated dashboard HTML file so stakeholder reviewers can open the deployment URL directly.
