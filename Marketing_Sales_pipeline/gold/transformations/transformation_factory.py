from gold.transformations.campaign_performance import CampaignPerformance
from gold.transformations.customer_analytics import CustomerAnalytics
from gold.transformations.support_analytics import SupportAnalytics
from gold.transformations.executive_dashboard import ExecutiveDashboard


class GoldTransformationFactory:

    _transformations = {

        "campaign_performance": CampaignPerformance(),

        "customer_analytics": CustomerAnalytics(),

        "support_analytics": SupportAnalytics(),

        "executive_dashboard": ExecutiveDashboard()

    }

    @classmethod
    def get_transformation(cls, dataset_name):

        if dataset_name not in cls._transformations:

            raise ValueError(
                f"No Gold Transformation found for {dataset_name}"
            )

        return cls._transformations[dataset_name]