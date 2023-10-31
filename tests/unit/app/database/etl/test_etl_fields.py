import datetime
import unittest
from typing import Any, cast, Dict

from marshmallow import Schema

from nfl_bdb.app.database.etl.fields import DATE_FORMAT, NADate, NAInteger


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
