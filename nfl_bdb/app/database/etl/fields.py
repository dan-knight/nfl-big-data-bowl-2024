from typing import Any, Mapping
from marshmallow.fields import Field, String, Integer, Float, Date


DATE_FORMAT: str = "%d/%m/%Y"
TIME_FORMAT: str = "%H:%M:%S"


class _NAField(Field):
    def _deserialize(
        self,
        value: Any,
        attr: str | None = None,
        data: Mapping[str, Any] | None = None,
        **kwargs: Mapping[str, Any],
    ):
        if value == "NA":
            value = None
        
        return super()._deserialize(value, attr, data, **kwargs)  # pyright: ignore[reportUnknownMemberType]
           


class NAString(_NAField, String):
    pass


class NAInteger(_NAField, Integer):
    pass
 

class NAFloat(_NAField, Float):
    pass


class NADate(_NAField, Date):
    pass
