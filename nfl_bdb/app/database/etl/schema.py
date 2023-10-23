from typing import Generic, Iterable, Mapping, Any, Optional, TypeVar, TYPE_CHECKING
from marshmallow import Schema, types


T = TypeVar("T")


class GenericSchema(Schema, Generic[T]):
    if TYPE_CHECKING:
        def load(
            self,
            data: Mapping[str, Any] | Iterable[Mapping[str, Any]],
            *,
            many: Optional[bool] = None,
            partial: types.StrSequenceOrSet | bool | None = None,
            unknown: Optional[str] = None
        ) -> T:
            return super().load(  # pyright: ignore[reportGeneralTypeIssues, reportUnknownVariableType]
                data, many=many, partial=partial, unknown=unknown
            )
