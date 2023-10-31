from typing import (Any, Generic, Iterable, Mapping, Optional, TYPE_CHECKING,
                    TypeVar)

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
