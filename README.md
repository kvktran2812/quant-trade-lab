# 📈 Quant-Trade-Lab – Local Financial Data Analysis Web App

A personal web application for downloading, storing, analyzing, and visualizing financial market data. Built for **local use only** (not SaaS), so you can clone the repo, run it on your laptop, and keep all your data private.

---

## 🚀 Project Overview

The app provides:

* **Historical data ingestion** (tickers, equities, ETFs, etc.)
* **Data storage** in efficient local formats
* **Query & analytics layer** (SQL + Python APIs)
* **Visualization** (candlesticks, volume, indicators, overlays)
* **Technical analysis & screening**
* **Backtesting** for strategies (planned)
* **Machine learning / predictive models** (optional future feature)

Designed for **individual users**: no accounts, no servers, no paid subscriptions required (beyond optional data providers).

---

## 🛠️ Tech Stack

### Backend

* **FastAPI** – REST API for data, analytics, backtesting, ML
* **DuckDB** – fast, embedded analytical database
* **Parquet files** – local data lake for historical OHLCV
* **SQLite** – optional metadata store (sync state, jobs, settings)

### Frontend (UI Options)

We decided to go with a simpler, more developer-friendly alternative than React:

* **FastAPI + HTMX + TailwindCSS** → server-driven UI with partial updates

  * Jinja2 templates for pages
  * HTMX for dynamic tables, forms, filters, dashboards
  * Plotly/ECharts/TradingView for charts

(Other possible frontends: NiceGUI \[all-Python], SvelteKit, Vue—but **HTMX** is the current pick.)

### Data / Analysis Libraries

* **pandas** or **polars** – DataFrames
* **yfinance**, **investpy**, **fredapi**, or paid APIs (Alpha Vantage, Tiingo, Polygon.io)
* **plotly** – interactive visualization
* **pandas-ta** or **ta** – indicators
* **vectorbt** or **backtrader** – backtesting (later)
* **scikit-learn**, **prophet**, **statsmodels** – ML/forecasting (later)

### Developer Experience

* **uv** / **poetry** – dependency + venv management
* **pytest** – testing
* **ruff**, **black**, **mypy** – linting, formatting, typing
* **Makefile** – simple task runner (setup, run, test)

---

## 📂 Project Structure

### Monorepo layout

```
To be updated soon
```

---

## 🗄️ Database & Storage

* **Primary:** DuckDB + Parquet files

  * Partition by `provider / interval / symbol / date`
  * Store raw OHLCV + derived data (indicators, features, results)
  * Fast analytical queries (SQL + window functions)
* **Secondary:** SQLite (optional)

  * App metadata, sync logs, saved queries, job states

**Why this choice?**

* Lightweight, portable, and fast enough for local use
* No server needed, no setup headaches
* Parquet is easy to back up, share, or re-ingest

---

## 🔑 Key Design Choices

1. **Local-first**: everything runs on your machine, no cloud required
2. **Data lake pattern**: append-only Parquet files for raw downloads
3. **Thin adapters** for each provider (yfinance, Tiingo, etc.)
4. **Deterministic caching**: avoid re-downloading data unnecessarily
5. **Stateless analytics functions**: pure in/out for testing & reproducibility
6. **Plot builders**: centralized logic for consistent chart styles
7. **Background-friendly jobs**: long tasks (bulk fetch, backtests) write to `/data/results/`
8. **ML isolation**: models and preprocessing saved separately, optional add-on

---

## 🏃 Quick Start

**Setup environment:**

```bash
uv venv
uv pip install -e backend
cp .env.example .env
```

**Run backend (FastAPI):**

```bash
uv run fastapi dev backend/app/main.py
```

**Run frontend (HTMX):**

* Open `http://localhost:8000` (served by FastAPI)

---

## 📌 Roadmap

* [x] Local data lake (Parquet + DuckDB)
* [x] FastAPI backend + HTMX UI
* [ ] Visualization: candlesticks + volume + indicators
* [ ] TA screeners & filters
* [ ] Backtesting (vectorbt/backtrader)
* [ ] Export (CSV/Parquet)
* [ ] ML models (forecasting, classification)
* [ ] Notebook integration (optional)

---

## 🤝 Contributions

This is a personal-use project, but contributions/PRs are welcome for:

* Adding new data providers
* Expanding TA/backtesting modules
* Improving visualization & UI components
* Packaging / installer support

---

## 📜 License

MIT License – free to use, modify, and share.
