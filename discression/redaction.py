from ._utils import fq_typename

__all__ = ['RedactedValue']


class RedactedValue:
    """
    Wraps and allows easy access to a sensitive value while blocking many
    of the ways that the value might be accidentally exposed.

    - Only returns its sensitive value via its 'sensitive_val' property
      getter.
    - Returns its given 'subst' value as its string value.
    - Does not expose its sensitive content its 'repr' value.
    - Does not expose its sensitive content its `.__dict__` contents.
    - Is not picklable.
    """

    def __init__(self, sensitive_val, subst='[...]'):
        def getter_fn():
            return sensitive_val

        self._getter_fn = getter_fn
        self._subst = subst

    @property
    def subst(self):
        return self._subst

    def __str__(self):
        return self._subst

    def __repr__(self):
        sv_repr = f'<{fq_typename(self.sensitive_val)} object...>'
        return f'{fq_typename(self)}({sv_repr}, {self._subst!r})'

    @property
    def sensitive_val(self):
        return self._getter_fn()
