import pandas as pd


class ExecutiveDashboard:

    def transform(

        self,

        campaign_df: pd.DataFrame,

        customer_df: pd.DataFrame,

        support_df: pd.DataFrame,

        website_df: pd.DataFrame

    ):

        dashboard = {

            "total_revenue":

                campaign_df["revenue"].sum(),

            "marketing_spend":

                campaign_df["spend"].sum(),

            "total_clicks":

                campaign_df["clicks"].sum(),

            "total_impressions":

                campaign_df["impressions"].sum(),

            "total_conversions":

                campaign_df["conversions"].sum(),

            "customers":

                len(customer_df),

            "support_tickets":

                support_df["total_tickets"].sum(),

            "website_sessions":

                len(website_df)

        }

        dashboard["roas"] = (

            dashboard["total_revenue"]

            /

            dashboard["marketing_spend"]

            if dashboard["marketing_spend"] > 0

            else 0

        )

        return pd.DataFrame([dashboard])