import pandas as pd


class SupportAnalytics:

    def transform(
        self,
        support_df: pd.DataFrame,
        customers_df: pd.DataFrame
    ):

        support = (

            support_df

            .groupby("customer_id", as_index=False)

            .agg(

                total_tickets=("ticket_id", "count"),

                avg_resolution_time=("resolution_time_hours", "mean")

            )

        )

        df = customers_df.merge(

            support,

            on="customer_id",

            how="left"

        )

        df.fillna(

            {

                "total_tickets": 0,

                "avg_resolution_time": 0

            },

            inplace=True

        )

        return df