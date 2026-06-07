# CreateQuizzesOnline

**Live site:** https://brightlane.github.io/createquizesonline/

Independent affiliate review and guide site for online quiz creation. Built with a single Python static site generator — zero dependencies, zero npm, zero pip installs.

---

## What This Is

A global SEO affiliate site targeting quiz creator keywords across 10 languages. One `build.py` script generates every page and deploys automatically to GitHub Pages via GitHub Actions.

**Affiliate product:** Quiz Creator by Wondershare
**Affiliate link:** `https://www.linkconnector.com/ta.php?lc=007949038162004532&atid=quizcreatorweb`

---

## Stats

| Metric | Value |
|---|---|
| Page types | 47 |
| Languages | 10 |
| Total HTML pages | 470+ |
| Dependencies | 0 |
| Build time | ~30 seconds |
| Python required | 3.6+ |

---

## Languages

English, Espanol, Francais, Deutsch, Portugues, Japanese, Korean, Chinese, Arabic, Hindi

Every page has full hreflang alternate tags, a canonical URL, Open Graph tags, Twitter card tags and a JSON-LD WebPage schema. The FAQ page has FAQPage schema. The sitemap covers all 470+ URLs with priority and changefreq.

---

## Page Types

**Quiz Types (10)**
- Multiple Choice Quiz
- Personality Quiz
- Trivia Quiz
- Online Assessment
- Survey
- Knowledge Test
- Online Exam
- Feedback Form
- Lead Generation Quiz
- Scored Quiz

**Industry Pages (8)**
- Healthcare
- Education
- Corporate Training
- Retail
- Fitness and Wellness
- Non-Profits
- Real Estate
- E-Commerce

**How-To Guides (7)**
- How to Create a Quiz Online
- How to Make a Quiz Go Viral
- How to Create a Quiz with AI
- How to Grade Quizzes Automatically
- How to Share Your Quiz
- How to Create a Quiz Certificate
- How to Make a Quiz Mobile-Friendly

**Feature Pages (6)**
- AI Quiz Maker
- Quiz Analytics Dashboard
- Online Quiz Certificates
- Embed Quiz on Website
- Live Quiz Software
- Quiz Maker with Timer

**Comparison Pages (5)**
- Best Online Quiz Maker (10-tool roundup)
- Quiz Creator vs Typeform
- Quiz Creator vs Google Forms
- Quiz Creator vs Kahoot
- Quiz Creator vs SurveyMonkey

**Use Case Pages (4)**
- Make a Quiz for Students
- Make a Quiz for Employees
- Make a Marketing Quiz
- Make a Quiz for Free

**Other Pages**
- Free Quiz Templates
- Quiz Creator Review 2025
- Quiz Maker Pricing
- Quiz Creation FAQ (25 questions, FAQPage schema)
- About (affiliate disclosure)
- 404

---

## File Structure

```
createquizesonline/
├── build.py                        # The entire site generator
├── README.md                       # This file
├── .github/
│   └── workflows/
│       └── deploy.yml              # GitHub Actions deploy workflow
└── dist/                           # Generated -- do not edit manually
    ├── index.html
    ├── assets/
    │   ├── style.css
    │   └── favicon.svg
    ├── robots.txt
    ├── sitemap.xml
    ├── llms.txt
    ├── humans.txt
    ├── 404.html
    ├── create-multiple-choice-quiz.html
    ├── ... (all EN pages)
    ├── es/
    │   └── ... (all ES pages)
    ├── fr/
    ├── de/
    ├── pt/
    ├── ja/
    ├── ko/
    ├── zh/
    ├── ar/
    └── hi/
```

---

## How to Build Locally

```bash
python3 build.py
```

Output goes to `./dist/`. Open `dist/index.html` in a browser to preview.

No pip installs. No npm. No virtual environment. Pure Python stdlib only.

---

## How to Deploy

### Automatic (GitHub Actions)

Every push to `main` triggers a build and deploy automatically. The workflow runs `python3 build.py`, uploads `./dist/` as a Pages artifact, and deploys.

To trigger manually: **Actions -> Build and Deploy -> Run workflow**

### First-Time Setup

1. Go to **Settings -> Pages**
2. Set Source to **GitHub Actions**
3. Push `build.py` and `.github/workflows/deploy.yml` to `main`
4. The first deploy runs automatically

### GitHub Actions Workflow

Create `.github/workflows/deploy.yml`:

```yaml
name: Build and Deploy CreateQuizzesOnline
on:
  push:
    branches:
      - main
  workflow_dispatch:
    inputs:
      reason:
        description: 'Reason for manual run'
        required: false
        default: 'Manual deploy'
permissions:
  contents: read
  pages: write
  id-token: write
concurrency:
  group: pages
  cancel-in-progress: false
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
      - name: Set up Python 3.11
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Run build.py
        run: python3 build.py
      - name: Upload Pages artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: ./dist
  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deploy.outputs.page_url }}
    permissions:
      pages: write
      id-token: write
    steps:
      - name: Deploy to GitHub Pages
        id: deploy
        uses: actions/deploy-pages@v4
```

---

## How the Code Works

`build.py` is one self-contained file with no imports beyond the Python stdlib.

**Key variables at the top:**

```python
BASE_URL  = "https://brightlane.github.io/createquizesonline"
BASE_PATH = "/createquizesonline"
AFF       = "https://www.linkconnector.com/ta.php?lc=007949038162004532&atid=quizcreatorweb"
```

**Flow:**

1. `LANGS` -- 10 tuples, one per language, containing all localised strings
2. `T` -- translation dictionary for shared UI strings
3. `PAGES` -- list of all 47 page slugs, titles, descriptions and template types
4. `CSS` -- full design system as a single string, written to `assets/style.css`
5. HTML helpers -- `ticker_html()`, `navbar()`, `trustbar()`, `langbar()`, `footer_html()`, `wrap()`
6. Page builders -- one function per template type (14 total)
7. `BUILDERS` -- dict mapping template type to builder function
8. `build()` -- loops all languages x all pages, calls the right builder, writes HTML

**Adding a new page:**

1. Add a tuple to `PAGES`: `("slug", "Title", "Description", "template_type")`
2. If it needs a new template type, add a builder function and register it in `BUILDERS`
3. Run `python3 build.py` and push

**Adding a new language:**

1. Add a tuple to `LANGS` with all required strings
2. Add the language code to every dict in `T`
3. Run `python3 build.py` -- all pages generate automatically for the new language

---

## Design System

| Token | Value | Use |
|---|---|---|
| `--a` | `#6D28D9` | Primary purple -- buttons, links, accents |
| `--a2` | `#8B5CF6` | Lighter purple -- hover states, gradients |
| `--a3` | `#C4B5FD` | Very light purple -- hero text highlights |
| `--green` | `#10B981` | Success, checkmarks, feature tags |
| `--p` | `#09090F` | Near-black -- hero background, footer |
| `--s3` | `#EDE9FE` | Lightest purple -- card backgrounds, highlights |

**Fonts:** Outfit (headings, 900 weight) + Plus Jakarta Sans (body)

**Key components:** Dark hero with CSS grid overlay and radial glow, animated ticker bar, before/after comparison section, sticky navbar, auto-responsive stat grid, feature rows, industry cards, quiz type cards, testimonial grid, FAQ accordions, comparison tables, pricing cards, full-width CTA block.

---

## SEO

Every page includes:
- `<title>` and `<meta name="description">`
- `<link rel="canonical">`
- `hreflang` alternate tags for all 10 languages plus `x-default`
- Open Graph tags (`og:title`, `og:description`, `og:url`, `og:type`, `og:site_name`)
- Twitter Card tags
- JSON-LD `WebPage` schema with `publisher`, `url`, `inLanguage`, `dateModified`
- FAQ page also has `FAQPage` schema with all 25 questions

Sitemap at `/sitemap.xml` covers all 470+ URLs with `lastmod`, `changefreq: monthly`, priority scores and `xhtml:link` alternate tags for multilingual pages.

`/robots.txt`, `/llms.txt` and `/humans.txt` are also generated.

---

## Affiliate Disclosure

This site earns a commission via the Quiz Creator affiliate programme (LinkConnector, ID: quizcreatorweb). The disclosure appears in the footer of every page and in full on the About page.

---

## Related Sites

| Site | Repo | Status |
|---|---|---|
| Quiz Creator v1 | brightlane/quizcreator | Live |
| Android Recovery v1 | brightlane/datarecoveryandroid | Live |
| Android Recovery v2 | brightlane/androiddatarecovery | Live |
| DrFone | brightlane/drfoneonline | Live |
| WonderShare v1 | brightlane/WonderShare | Live |
| WonderShare v2 | brightlane/wondershare.com | Live |
| **CreateQuizzesOnline** | brightlane/createquizesonline | **This repo** |
