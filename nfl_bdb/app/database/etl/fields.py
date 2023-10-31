from typing import Any, Mapping

from marshmallow.fields import Date, Field, Float, Integer, String

DATE_FORMAT: str = "%Y-%m-%d"
TIME_FORMAT: str = "%H:%M:%S"
DATETIME_FORMAT: str = f"{DATE_FORMAT} {TIME_FORMAT}.%f"


class NAField(Field):
    def _deserialize(
        self,
        value: Any,
        attr: str | None = None,
        data: Mapping[str, Any] | None = None,
        **kwargs: Mapping[str, Any],
    ):
        if value == "NA":
            return None

        return super()._deserialize(
            value, attr, data, **kwargs
        )  # pyright: ignore[reportUnknownMemberType]


class NAString(NAField, String):
    pass


class NAInteger(NAField, Integer):
    pass


class NAFloat(NAField, Float):
    pass


class NADate(NAField, Date):  # pyright: ignore[reportIncompatibleMethodOverride]
    pass
