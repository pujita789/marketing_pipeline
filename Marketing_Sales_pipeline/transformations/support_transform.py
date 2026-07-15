from transformations.base_transformer import BaseTransformer


class SupportTransformer(BaseTransformer):

    def transform(self, df):

        self.validate_required_columns(

            df,

            [

                "ticket_id",

                "priority",

                "status",

                "created_date"

            ]

        )

        df = self.remove_duplicates(df)

        df = self.remove_null_rows(df)

        df = self.convert_numeric(

            df,

            [

                "resolution_time_hours"

            ]

        )

        df = self.convert_dates(

            df,

            [

                "created_date"

            ]

        )

        df = self.remove_negative_values(

            df,

            [

                "resolution_time_hours"

            ]

        )

        return df