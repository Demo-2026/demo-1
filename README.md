# demo-1

Beginner-friendly Applied Analytics mini-project showing ETL, SQLite, and Secure SQL practices.

## Folder Structure

- `data/raw`: Contains source CSV files.
- `data/db`: Contains the generated SQLite database.
- `src`: Python source code for ETL and Analysis.
- `tests`: Pytest unit tests.

## Setup

1. **Create Virtual Environment:**
   ```bash
   python -m venv myenv
   ```
2. **Activate Environment:**
   - Windows: `myenv\Scripts\activate`
   - Mac/Linux: `source myenv/bin/activate`
3. **Install Requirements:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Project

1. **Run ETL (Load Data):**
   ```bash
   python src/etl_load_sqlite.py
   ```
2. **Run KPI Script:**
   ```bash
   python src/kpi_city.py
   ```
   *Note: Observe how the injection attempt returns (0, None) instead of leaking data.*

## Testing

Run the automated tests:
```bash
pytest
```
