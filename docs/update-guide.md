# Dashboard Update Guide

This guide is for staff who need to update the dashboard without changing code.

## Update a CSV in GitHub

1. Open the repository on GitHub.
2. Go to `data/`.
3. Choose the file you need:
   - `master-dashboard-data.csv` for dashboard values.
   - `source-documentation.csv` for source links and references.
4. Click the edit pencil, or upload a replacement file with the same filename.
5. Keep the same column names.
6. Commit the change.

## Update copy or tooltips

1. Open `data/dashboard-copy.js`.
2. Edit only the text inside quotation marks.
3. Do not rename keys such as `intro`, `sections`, `labels`, or `tooltips`.
4. Commit the change.

## What not to change

- Do not rename CSV columns.
- Do not delete required columns.
- Do not change file names or folder paths.
- Do not remove quotation marks, commas, or braces in `dashboard-copy.js`.
- Do not edit generated dashboard files unless a technical maintainer asks you to.

## Confirm the live site updated

1. After committing, wait a few moments for Vercel to redeploy.
2. Open the live dashboard.
3. Check the page, chart, table, or tooltip you updated.
4. If the change does not appear after a few minutes, ask a technical maintainer to run the dashboard build and check Vercel.
