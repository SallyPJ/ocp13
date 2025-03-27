import pytest

def test_custom_500():
    """
    Test if the custom 500 error page is triggered correctly.

    Returns:
        None
    """
    with pytest.raises(ValueError, match="Test error for 500 page"):
        raise ValueError("Test error for 500 page")