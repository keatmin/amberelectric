import os

import pandas as pd
import psycopg2 as pg
from psycopg2.extensions import connection
from queries import SQL


def connect_db(
    user: str = None,
    host: str = "localhost",
    port: int = 5432,
    dbname: str = "amber",
) -> connection:
    user = os.environ.get("USER") if not user else user
    return pg.connect(host=host, port=port, dbname=dbname, user=user)


def get_data(SQL: str, conn: connection) -> pd.DataFrame:
    return pd.read_sql(SQL, conn)


def clean_data(data: pd.DataFrame) -> None:
    basedir = os.path.dirname(__file__)
    df = data.pivot(
        index=["cohort", "cohort_size"],
        columns=["churned_month"],
        values=["churned_users"],
    ).fillna(0)
    return df.to_csv(
        f"{os.path.join(basedir, '..')}/data/processed/dataset.csv"
    )


def main():
    conn = connect_db()
    data = get_data(SQL, conn)
    clean_data(data)


if __name__ == "__main__":
    main()
