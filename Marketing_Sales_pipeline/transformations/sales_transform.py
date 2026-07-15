from transformations.base_transformer import BaseTransformer


class SalesTransformer(BaseTransformer):

    def transform(self, df):

        self.validate_required_columns(

            df,

            [

                "order_id",

                "customer_id",

                "amount",

                "quantity",

                "order_date"

            ]

        )

        df = self.remove_duplicates(df)

        df = self.remove_null_rows(df)

        df = self.convert_numeric(

            df,

            [

                "amount",

                "quantity"

            ]

        )

        df = self.convert_dates(

            df,

            [

                "order_date"

            ]

        )

        df = self.remove_negative_values(

            df,

            [

                "amount",

                "quantity"

            ]

        )

        return df