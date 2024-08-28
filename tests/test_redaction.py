import pickle

import pytest

from discression.redaction import RedactedValue


class TestRedactedValue:

    def test_subst(self):
        rv = RedactedValue('real value', '[redacted]')
        assert rv.subst == '[redacted]'

    def test__str__(self):
        rv = RedactedValue('real value', '[redacted]')
        assert str(rv) == '[redacted]'

    def test_sensitive_val(self):
        rv = RedactedValue('real value', '[redacted]')
        assert rv.sensitive_val == 'real value'

    def test__repr__(self):
        rv = RedactedValue('real value', '[redacted]')
        assert repr(rv) == (
            "discression.redaction.RedactedValue"
            "(<str object...>, '[redacted]')")

    @pytest.mark.parametrize(
        'sval', ('real value', 54321))
    def test_does_not_expose_sensitive_val_in__dict__(self, sval):
        rv = RedactedValue(sval)
        assert str(sval) not in str(rv.__dict__)
        assert repr(sval) not in str(rv.__dict__)

    def test_is_not_pickleable(self):
        rv = RedactedValue('real value', '[redacted]')
        with pytest.raises(AttributeError):
            pickle.dumps(rv)
