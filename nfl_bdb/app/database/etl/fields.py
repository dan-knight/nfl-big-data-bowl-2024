import datetime
from typing import Any, List, Mapping, Optional
from marshmallow import ValidationError

from marshmallow.fields import Date, DateTime, Field, Float, Integer, String

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

        return super()._deserialize(  # pyright: ignore[reportUnknownMemberType]
            value, attr, data, **kwargs
        )  

class NAString(NAField, String):
    pass


class NAInteger(NAField, Integer):
    pass


class NAFloat(NAField, Float):
    pass


class NADate(NAField, Date):  # pyright: ignore[reportIncompatibleMethodOverride]
    pass


class MultiFormatDateTime(DateTime):
    def __init__(self, formats: Optional[List[str]], **kwargs: Any) -> None:
        super().__init__(  # pyright: ignore[reportUnknownMemberType]
            format=None, **kwargs
        )
        self.formats: List[str] = formats if formats is not None else []

    def _deserialize(
        self,
        value: Any,
        attr: str | None = None,
        data: Mapping[str, Any] | None = None,
        **kwargs: Mapping[str, Any],
    ) -> datetime.datetime:
        exception: Optional[ValidationError] = None

        for format in self.formats:
            try:
                return self._try_date_format(value, format)
            except ValidationError as e:
                exception = e

        if exception is None:
            exception = self.make_error(  # pyright: ignore[reportUnknownMemberType]
                "invalid", input=value, obj_type=self.OBJ_TYPE
            )
        raise exception
        

    def _try_date_format(self, value: Any, date_format: str) -> datetime.datetime:
        if not value:
            raise self.make_error(  # pyright: ignore[reportUnknownMemberType]
                "invalid", input=value, obj_type=self.OBJ_TYPE
            )
        
        func = self.DESERIALIZATION_FUNCS.get(date_format)
        try:
            if func:
                return func(value)
            return self._make_object_from_format(  # pyright: ignore[reportUnknownMemberType]
                value, date_format
            )
        except (TypeError, AttributeError, ValueError) as error:
            raise self.make_error(  # pyright: ignore[reportUnknownMemberType]
                "invalid", input=value, obj_type=self.OBJ_TYPE
            ) from error
    
    
class MultiFormatDate(MultiFormatDateTime):
    def _deserialize(  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        value: Any,
        attr: str | None = None,
        data: Mapping[str, Any] | None = None,
        **kwargs: Mapping[str, Any]
    ) -> datetime.date:
        date_time: datetime.datetime = super()._deserialize(value, attr, data, **kwargs)
        return date_time.date()


class NAMultiFormatDateTime(NAField, MultiFormatDateTime):  # pyright: ignore[reportIncompatibleMethodOverride]
    pass        


class NAMultiFormatDate(NAField, MultiFormatDate):  # pyright: ignore[reportIncompatibleMethodOverride]
    pass
