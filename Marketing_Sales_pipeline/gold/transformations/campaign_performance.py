import pandas as pd


class CampaignPerformance:

    def transform(
        self,
        google_df: pd.DataFrame,
        meta_df: pd.DataFrame,
        sales_df: pd.DataFrame,
        crm_df: pd.DataFrame
    ) -> pd.DataFrame:

        # -----------------------------
        # Google Ads Aggregation
        # -----------------------------
        google = (
            google_df
            .groupby(
                ["campaign_name", "platform"],
                as_index=False
            )
            .agg(
                impressions=("impressions", "sum"),
                clicks=("clicks", "sum"),
                spend=("spend", "sum")
            )
        )

        # -----------------------------
        # Meta Ads Aggregation
        # -----------------------------
        meta = (
            meta_df
            .groupby(
                ["campaign_name", "platform"],
                as_index=False
            )
            .agg(
                impressions=("impressions", "sum"),
                clicks=("clicks", "sum"),
                spend=("spend", "sum")
            )
        )

        # -----------------------------
        # Combine Advertising Platforms
        # -----------------------------
        ads = pd.concat(
            [google, meta],
            ignore_index=True
        )

        # -----------------------------
        # Sales Aggregation
        # -----------------------------
        sales = (
            sales_df
            .groupby(
                "campaign_name",
                as_index=False
            )
            .agg(
                revenue=("amount", "sum"),
                orders=("order_id", "count")
            )
        )

        # -----------------------------
        # CRM Aggregation
        # -----------------------------
        crm = (
            crm_df
            .groupby(
                "campaign_name",
                as_index=False
            )
            .agg(
                conversions=("lead_status",
                             lambda x: (x == "Converted").sum())
            )
        )

        # -----------------------------
        # Merge Everything
        # -----------------------------
        df = ads.merge(
            sales,
            on="campaign_name",
            how="left"
        )

        df = df.merge(
            crm,
            on="campaign_name",
            how="left"
        )

        # -----------------------------
        # Fill Missing Values
        # -----------------------------
        df.fillna(
            {
                "revenue": 0,
                "orders": 0,
                "conversions": 0
            },
            inplace=True
        )

        # -----------------------------
        # Calculate KPIs
        # -----------------------------
        df["ctr"] = (
            df["clicks"] /
            df["impressions"]
        ) * 100

        df["cpc"] = (
            df["spend"] /
            df["clicks"]
        )

        df["roas"] = (
            df["revenue"] /
            df["spend"]
        )

        df["conversion_rate"] = (
            df["conversions"] /
            df["clicks"]
        ) * 100

        # -----------------------------
        # Clean Numeric Columns
        # -----------------------------
        numeric_cols = [
            "ctr",
            "cpc",
            "roas",
            "conversion_rate"
        ]

        df[numeric_cols] = (
            df[numeric_cols]
            .fillna(0)
            .round(2)
        )

        return df