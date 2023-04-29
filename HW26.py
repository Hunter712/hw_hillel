def skip(condition, reason=''):
    def inner(function):
        def wrapper():
            if condition:
                result = reason
            else:
                result = function()
            return result
        return wrapper

    return inner


@skip(condition=True, reason='Skipped because of JIRA-123 bug')
def test_two_plus_two():
    assert 2 + 2 == 5


print(test_two_plus_two())
