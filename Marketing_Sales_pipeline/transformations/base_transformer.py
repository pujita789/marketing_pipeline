import pandas as pd


class BaseTransformer:

    def remove_duplicates(self, df: pd.DataFrame):

        return df.drop_duplicates()


    def remove_null_rows(self, df: pd.DataFrame):

        return df.dropna()


    def convert_dates(self, df: pd.DataFrame, columns: list):

        for column in columns:

            if column in df.columns:

                df[column] = pd.to_datetime(
                    df[column],
                    errors="coerce"
                )

        return df


    def convert_numeric(self, df: pd.DataFrame, columns: list):

        for column in columns:

            if column in df.columns:

                df[column] = pd.to_numeric(
                    df[column],
                    errors="coerce"
                )

        return df


    def remove_negative_values(
        self,
        df: pd.DataFrame,
        columns: list
    ):

        for column in columns:

            if column in df.columns:

                df = df[df[column] >= 0]

        return df


    def validate_required_columns(
        self,
        df: pd.DataFrame,
        required_columns: list
    ):

        missing = set(required_columns) - set(df.columns)

        if missing:

            raise Exception(
                f"Missing columns: {missing}"
            )

        return df