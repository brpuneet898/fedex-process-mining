```
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python generate_synthetic_log.py --seed 42 --cases 200 --out data
python -m pytest tests -v
python run_pm4py_smoke_test.py --input data/synthetic_events.csv --out outputs
```