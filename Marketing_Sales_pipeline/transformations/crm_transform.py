from transformations.base_transformer import BaseTransformer


class CRMTransformer(BaseTransformer):

    def transform(self, df):

        self.validate_required_columns(

            df,

            [

                "lead_id",

                "lead_status",

                "lead_source",

                "created_date"

            ]

        )

        df = self.remove_duplicates(df)

        df = self.remove_null_rows(df)

        df = self.convert_numeric(

            df,

            [

                "conversion_value"

            ]

        )

        df = self.convert_dates(

            df,

            [

                "created_date",

                "conversion_date"

            ]

        )

        df = self.remove_negative_values(

            df,

            [

                "conversion_value"

            ]

        )

        return df