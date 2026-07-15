from transformations.base_transformer import BaseTransformer


class WebsiteTransformer(BaseTransformer):

    def transform(self, df):

        self.validate_required_columns(

            df,

            [

                "session_id",

                "page_views",

                "session_duration_seconds",

                "visit_date"

            ]

        )

        df = self.remove_duplicates(df)

        df = self.remove_null_rows(df)

        df = self.convert_numeric(

            df,

            [

                "page_views",

                "session_duration_seconds"

            ]

        )

        df = self.convert_dates(

            df,

            [

                "visit_date"

            ]

        )

        df = self.remove_negative_values(

            df,

            [

                "page_views",

                "session_duration_seconds"

            ]

        )

        return df