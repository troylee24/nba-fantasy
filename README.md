# nba-fantasy
Flask App displaying jQuery datatable of fantasy basketball projections

API for data-scraping: https://www.fantasybasketballnerd.com/fantasy-basketball-api 

## Process data from API
1. Retrieve in XML
    ```bash
    python3 retrieve_data.py
    ```
2. Parse data from XML to JSON
    ```bash
    python3 parse_data.py
    ```

## Run Flask App
```bash
python3 app.py
```