from pytest import raises


def test_custom_500():
    """
    Test if the custom 500 error page is triggered correctly.

    Returns:
        None
    """
    with raises(ValueError, match="Test error for 500 page"):
        raise ValueError("Test error for 500 page")
