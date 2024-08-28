from datetime import datetime
from decimal import Decimal

import pytest

from discression._utils import fq_typename


class TestFQTypename:

    @pytest.mark.parametrize(
        'typ,expected_repr', (
            (str, 'str'),
            (int, 'int'),
            ))
    def test_gives_correct_repr_of_builtin_type(self, typ, expected_repr):
        assert fq_typename(typ) == expected_repr

    @pytest.mark.parametrize(
        'obj,expected_repr', (
            ('some str', 'str'),
            (54321, 'int'),
            ))
    def test_gives_correct_repr_of_builtin_type_of_obj(
            self, obj, expected_repr):
        assert fq_typename(obj) == expected_repr

    @pytest.mark.parametrize(
        'typ,expected_repr', (
            (datetime, 'datetime.datetime'),
            (Decimal, 'decimal.Decimal'),
            ))
    def test_gives_correct_repr_of_misc_type(self, typ, expected_repr):
        assert fq_typename(typ) == expected_repr

    @pytest.mark.parametrize(
        'obj,expected_repr', (
            (datetime.now(), 'datetime.datetime'),
            (Decimal(54321), 'decimal.Decimal'),
            ))
    def test_gives_correct_repr_of_misc_type_of_obj(
            self, obj, expected_repr):
        assert fq_typename(obj) == expected_repr
