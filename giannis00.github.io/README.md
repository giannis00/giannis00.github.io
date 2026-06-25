# giannis00.github.io

Personal academic website of **Ioannis Tsioulis** — built on the [al-folio](https://github.com/alshedivat/al-folio) Jekyll theme.

## Deploy (one-time)

This theme's `deploy.yml` workflow builds the site and publishes it to a **`gh-pages`** branch.

1. Create a **public** repository named exactly **`giannis00.github.io`**.
2. Push these files to the **`main`** branch (the files must be at the repo root — `_config.yml`, `assets/`, `.github/` directly at top level, NOT inside a sub-folder).
3. Repo **Settings → Actions → General → Workflow permissions → Read and write permissions** (safety; lets the workflow push the built site).
4. The **"Deploy site"** workflow runs automatically on push. If not, go to **Actions → Deploy site → Run workflow**. It builds and pushes to the `gh-pages` branch.
5. **Settings → Pages →** Source: **Deploy from a branch** · Branch: **`gh-pages`** · Folder: **`/ (root)`**.
6. Site is live at **https://giannis00.github.io**.

## Editing
- Home / bio: `_pages/about.md`
- Courses: `_teachings/*.md`  ·  Teaching page: `_pages/teaching.md`
- Course materials (PDFs): drop into `assets/courses/<CODE>/`, then link them per week in the course file
- Supervised theses: `_pages/supervision.md`  ·  thesis PDFs into `assets/theses/`
- Research projects: `_projects/*.md`
- Publications: `_bibliography/papers.bib`
- News (homepage): `_news/*.md`
- CV: `_data/cv.yml` (the download button uses `assets/pdf/cv.pdf`, already included)
- Profile photo: replace `assets/img/prof_pic.jpg`
- Global settings: `_config.yml`
