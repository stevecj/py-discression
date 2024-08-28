__all__ = ['fq_typename']


def fq_typename(obj):
    typ = obj if isinstance(obj, type) else type(obj)
    if typ.__module__ == 'builtins':
        return typ.__qualname__
    else:
        return f'{typ.__module__}.{typ.__qualname__}'
