import pandas.api.types as pdt
import pandas as pd

from tenzing.core.mixins import optionMixin
from tenzing.core.model_implementations.types.tenzing_generic import tenzing_generic


class tenzing_timedelta(optionMixin, tenzing_generic):
    """**Timedelta** implementation of :class:`tenzing.core.models.tenzing_model`.

    >>> x = pd.Series([pd.Timedelta(days=i) for i in range(3)])
    >>> x in tenzing_timedelta
    True
    """

    @classmethod
    def contains_op(cls, series):
        return pdt.is_timedelta64_dtype(series)

    @classmethod
    def cast_op(cls, series, operation=None):
        return pd.to_timedelta(series)

    @classmethod
    def summarization_op(cls, series):
        summary = super().summarization_op(series)
        # TODO: statistics
        return summary