import pandas as pd


class CustomerAnalytics:

    def transform(
        self,
        customers_df: pd.DataFrame,
        sales_df: pd.DataFrame,
        crm_df: pd.DataFrame
    ):

        sales = (

            sales_df

            .groupby("customer_id", as_index=False)

            .agg(

                total_orders=("order_id", "count"),

                total_spent=("amount", "sum")

            )

        )

        crm = (

            crm_df

            .groupby("customer_id", as_index=False)

            .agg(

                lead_status=("lead_status", "last"),

                conversion_value=("conversion_value", "sum")

            )

        )

        df = customers_df.merge(

            sales,

            on="customer_id",

            how="left"

        )

        df = df.merge(

            crm,

            on="customer_id",

            how="left"

        )

        df.fillna({
          "total_orders": 0,
          "total_spent": 0,
          "conversion_value": 0,
          "lead_status": "Unknown"
        }, inplace=True)

        return df