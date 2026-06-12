# Town Readiness Assessment Dashboard

Static dashboard prototype for the Long Island Clean Energy Hub Town Readiness Assessment.

## Published dashboard

The dashboard entry point is:

`outputs/liceh_dashboard_prototype/looker_studio_dashboard_prototype.html`

The page is a static HTML/CSS/JavaScript file with embedded data. No build step is required to view or deploy the dashboard.

## Supporting files

- `outputs/liceh_dashboard_prototype/dashboard_data.json` - structured dashboard data export.
- `outputs/liceh_dashboard_prototype/liceh_looker_studio_data_source.csv` - tabular data source export.
- `outputs/liceh_dashboard_prototype/visualizations_created.md` - list of created dashboard visualizations.
- `outputs/liceh_dashboard_prototype/calculated_fields_created.md` - calculated fields documentation.
- `outputs/liceh_dashboard_prototype/backlog.md` - dashboard backlog and future enhancement notes.
- `outputs/liceh_dashboard_prototype/public_dashboard_field_review.md` - public-facing field review notes.

## Vercel

`vercel.json` rewrites the site root to the dashboard HTML file so stakeholder reviewers can open the deployment URL directly.

