import datetime
import unittest
from typing import Any, Dict, cast

from marshmallow import Schema

from nfl_bdb.app.database.etl.fields import (
    DATE_FORMAT,
    DATETIME_FORMAT,
    MultiFormatDate,
    MultiFormatDateTime,
    NADate,
    NAInteger,
    NAMultiFormatDate,
    NAMultiFormatDateTime,
)


class TestETLFields(unittest.TestCase):
    def test__na_field__allows_valid_value(self):
        class TestSchema(Schema):
            test_value = NAInteger(required=True)

        value: int = 10
        key: str = "test_value"

        schema = TestSchema()
        result = cast(Dict[str, Any], schema.load({key: value}))

        assert result[key] == value

    def test__na_field__allows_required_na(self):
        class TestSchema(Schema):
            test_value = NAInteger(required=True)

        key: str = "test_value"
        schema = TestSchema()
        result = cast(Dict[str, Any], schema.load({key: "NA"}))

        assert result.get(key) is None

    def test__na_date_field__allows_valid_date(self):
        date_format: str = DATE_FORMAT

        class TestSchema(Schema):
            test_value = NADate(format=date_format, required=True)

        value = datetime.date(2021, 9, 15)
        key: str = "test_value"
        schema = TestSchema()
        result = cast(Dict[str, Any], schema.load({key: value.strftime(DATE_FORMAT)}))

        assert result[key] == value

    def test__na_date_field__allows_required_na_date(self):
        date_format: str = DATE_FORMAT

        class TestSchema(Schema):
            test_value = NADate(format=date_format)

        key: str = "test_value"
        schema = TestSchema()
        result = cast(Dict[str, Any], schema.load({key: "NA"}))

        assert result[key] is None

    def test__multi_format_datetime_field__allows_valid_date(self):
        date_format: str = DATETIME_FORMAT

        class TestSchema(Schema):
            test_value = MultiFormatDateTime(formats=[date_format])

        value = datetime.datetime(2022, 8, 11, 8, 15)
        key: str = "test_value"
        schema = TestSchema()
        result = cast(Dict[str, Any], schema.load({key: value.strftime(date_format)}))

        assert result[key] == value

    def test__multi_format_datetime_field__allows_valid_second_format(self):
        date_format: str = "%m/%d/%Y %H:%M"

        class TestSchema(Schema):
            test_value = MultiFormatDateTime(formats=[DATETIME_FORMAT, date_format])

        value = datetime.datetime(2022, 8, 11, 4, 30)
        key: str = "test_value"
        schema = TestSchema()
        result = cast(Dict[str, Any], schema.load({key: value.strftime(date_format)}))

        assert result[key] == value

    def test__na_multi_format_datetime_field__allows_required_na_datetime(self):
        date_format: str = "%m/%d/%Y %H:%M"

        class TestSchema(Schema):
            test_value = NAMultiFormatDateTime(
                formats=[DATETIME_FORMAT, date_format], required=True
            )

        key: str = "test_value"
        schema = TestSchema()
        result = cast(Dict[str, Any], schema.load({key: "NA"}))

        assert result[key] is None

    def test__multi_format_date_field__allows_valid_date(self):
        date_format: str = DATE_FORMAT

        class TestSchema(Schema):
            test_value = MultiFormatDate(formats=[date_format])

        value = datetime.date(2020, 3, 9)
        key: str = "test_value"
        schema = TestSchema()
        result = cast(Dict[str, Any], schema.load({key: value.strftime(date_format)}))

        assert result[key] == value

    def test__multi_format_date_field__allows_valid_second_format(self):
        date_format: str = "%m/%d/%Y"

        class TestSchema(Schema):
            test_value = MultiFormatDate(formats=[DATE_FORMAT, date_format])

        value = datetime.date(2022, 8, 11)
        key: str = "test_value"
        schema = TestSchema()
        result = cast(Dict[str, Any], schema.load({key: value.strftime(date_format)}))

        assert result[key] == value

    def test__na_multi_format_date_field__allows_required_na_date(self):
        date_format: str = "%m/%d/%Y"

        class TestSchema(Schema):
            test_value = NAMultiFormatDate(
                formats=[DATE_FORMAT, date_format], required=True
            )

        key: str = "test_value"
        schema = TestSchema()
        result = cast(Dict[str, Any], schema.load({key: "NA"}))

        assert result[key] is None
