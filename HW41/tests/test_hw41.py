import pytest

from FixedPixel import Pixel


def test_if_rgb_in_range():
    assert Pixel(0, 100, 255)


@pytest.mark.xfail(reason="parameter not in range")
def test_if_rgb_not_in_range():
    assert Pixel(-1, 256, 300)


# adding cases
def test_adding_2_int_objects():
    pixel1 = Pixel(3, 3, 3)
    pixel2 = Pixel(1, 2, 3)
    result = pixel1 + pixel2

    assert result.r == 4 and result.g == 5 and result.b == 6


def test_adding_to_reach_out_of_range():
    pixel1 = Pixel(255, 3, 255)
    pixel2 = Pixel(10, 255, 3)
    result = pixel1 + pixel2

    assert result.r == 255 and result.g == 255 and result.b == 255


@pytest.mark.xfail(reason="adding int with str")
def test_adding_str_objects():
    pixel1 = Pixel("3", 3, 3)
    pixel2 = Pixel(1, "2", 3)
    result = pixel1 + pixel2

    assert result.r == 4 and result.g == 5 and result.b == 6


# difference cases
def test_difference_2_objects():
    pixel1 = Pixel(3, 3, 3)
    pixel2 = Pixel(1, 2, 3)
    result = pixel1 - pixel2

    assert result.r == 2 and result.g == 1 and result.b == 0


def test_difference_to_reach_out_of_range():
    pixel1 = Pixel(255, 3, 1)
    pixel2 = Pixel(1, 255, 255)
    result = pixel1 - pixel2

    assert result.r == 254 and result.g == 0 and result.b == 0


@pytest.mark.xfail(reason="difference int with str")
def test_difference_with_str_objects():
    pixel1 = Pixel(3, "3", 3)
    pixel2 = Pixel("1", 2, 3)
    result = pixel1 - pixel2

    assert result.r == 2 and result.g == 1 and result.b == 0


# multiplication cases
def test_multiply_int():
    pixel1 = Pixel(3, 3, 3)
    pixel2 = Pixel(1, 2, 3)
    result = pixel1 * pixel2

    assert result.r == 3 and result.g == 6 and result.b == 9


def test_multiply_float():
    pixel1 = Pixel(3.0, 3.0, 3.0)
    pixel2 = Pixel(1.0, 2.0, 3.0)
    result = pixel1 * pixel2

    assert result.r == 3 and result.g == 6 and result.b == 9


def test_multiply_to_reach_out_of_range():
    pixel1 = Pixel(255.0, 255.0, 255.0)
    pixel2 = Pixel(1, 2, 3)
    result = pixel1 * pixel2

    assert result.r == 255 and result.g == 255 and result.b == 255


@pytest.mark.xfail(reason="multiply with 0")
def test_multiply_with_0():
    pixel1 = Pixel(3, 3, 3)
    pixel2 = Pixel(0, 2, 3)
    result = pixel1 * pixel2

    assert result.r == -3 and result.g == 6 and result.b == 9


@pytest.mark.xfail(reason="multiplying str with int")
def test_multiply_bad_type():
    pixel1 = Pixel("3.0", 3.0, 3.0)
    pixel2 = Pixel("1.0", 2.0, 3.0)
    result = pixel1 * pixel2

    assert result.r == 3 and result.g == 6 and result.b == 9


# division cases
def test_div_int():
    pixel1 = Pixel(3, 5, 3)
    pixel2 = Pixel(1, 2, 3)
    result = pixel1 / pixel2

    assert result.r == 3 and result.g == 2 and result.b == 1


def test_div_float():
    pixel1 = Pixel(3.0, 5.0, 3.0)
    pixel2 = Pixel(1.0, 2.0, 3.0)
    result = pixel1 / pixel2

    assert result.r == 3 and result.g == 2 and result.b == 1


@pytest.mark.xfail(reason="div with 0")
def test_div_with_0():
    pixel1 = Pixel(3, 3, 3)
    pixel2 = Pixel(0, 2, 3)
    result = pixel1 / pixel2

    assert result.r == 3 and result.g == 1 and result.b == 1


@pytest.mark.xfail(reason="multiplying str with int")
def test_div_bad_type():
    pixel1 = Pixel("3.0", 3.0, 3.0)
    pixel2 = Pixel("1.0", 2.0, 3.0)
    result = pixel1 / pixel2

    assert result.r == 3 and result.g == 6 and result.b == 9


def test_random_pixel():
    pixel = Pixel(10.0, 10, 10)

    assert 8.0 <= pixel.r <= 12.0 and 8 <= pixel.g <= 12 and 8 <= pixel.b <= 12
