from transformations.base_transformer import BaseTransformer


class CustomerTransformer(BaseTransformer):

    def transform(self, df):

        self.validate_required_columns(

            df,

            [

                "customer_id",

                "customer_name",

                "customer_since"

            ]

        )

        df = self.remove_duplicates(df)

        df = self.remove_null_rows(df)

        df = self.convert_dates(

            df,

            [

                "customer_since"

            ]

        )

        return df