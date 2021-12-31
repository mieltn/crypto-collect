# crypto currency data collection
App provides functionality to automatically collect and update data about selected crypto currency rates and its market capitalization.

Project purpose is to start working with **postgres** and get familiar with **airflow**.

It automates the proccess of:
1. Scraping data from [web](https://coinmarketcap.com/)
2. Adding to postgres database
3. Setting up autoupdate with airflow

To reproduce on local machine:
1. Install python and run `pip install -r requirements.txt`
2. Install airflow [locally](https://airflow.apache.org/docs/apache-airflow/stable/start/local.html) and put `crypto_update.py` in airflow/dags
3. Create postgres database and execute `schema.sql` to create table
4. Update `config.py` with your database cridentioals
5. Run `airflow standalone`
