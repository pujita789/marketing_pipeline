from transformations.base_transformer import BaseTransformer


class GoogleTransformer(BaseTransformer):

    def transform(self, df):

        self.validate_required_columns(

            df,

            [

                "campaign_id",

                "campaign_name",

                "clicks",

                "impressions",

                "spend",

                "date"

            ]

        )

        df = self.remove_duplicates(df)

        df = self.remove_null_rows(df)

        df = self.convert_numeric(

            df,

            [

                "clicks",

                "impressions",

                "spend"

            ]

        )

        df = self.convert_dates(

            df,

            [

                "date"

            ]

        )

        df = self.remove_negative_values(

            df,

            [

                "clicks",

                "impressions",

                "spend"

            ]

        )

        return df