import pytest

from home_work_41.tests.pixel.FixedPixel import Pixel


def test_if_rgb_in_range():
    pixel = Pixel(0, 100, 255)
    assert pixel.r == 0
    assert pixel.g == 100
    assert pixel.b == 255


# negative test case, expected ValueError exception
@pytest.mark.xfail(reason="negative test case, expected ValueError exception")
def test_if_rgb_not_in_range():
    pixel = Pixel(-1, 255, 300)
    assert pixel.r == 0
    assert pixel.g == 255
    assert pixel.b == 255


def test_if_2_objects_is_equal():
    pixel1 = Pixel(1, 255, 30)
    pixel2 = Pixel(1, 255, 30)
    assert pixel1 == pixel2


# negative test case, expected fail
@pytest.mark.xfail(reason="negative test case, expected fail")
def test_if_2_objects_is_not_equal():
    pixel1 = Pixel(1, 255, 30)
    pixel2 = Pixel(12, 255, 30)
    assert pixel1 == pixel2, f"expected fail, pixel1.r != pixel2.r"


# adding cases
def test_adding_objects():
    pixel1 = Pixel(3, 3, 3)
    pixel2 = Pixel(1, 2, 3)
    result = pixel1 + pixel2

    assert result.r == 4
    assert result.g == 5
    assert result.b == 6


def test_adding_to_reach_out_of_range():
    pixel1 = Pixel(255, 3, 255)
    pixel2 = Pixel(10, 255, 3)
    result = pixel1 + pixel2

    assert result.r == 255
    assert result.g == 255
    assert result.b == 255


# negative test case, expected TypeError exception
@pytest.mark.xfail(reason="negative test case, expected TypeError exception")
def test_add_wrong_types():
    pixel1 = Pixel("3", 3, 3)
    pixel2 = Pixel(1, "2", 3)
    result = pixel1 + pixel2

    assert result.r == 4
    assert result.g == 5
    assert result.b == 6


# difference cases
def test_difference_between_2_objects():
    pixel1 = Pixel(3, 3, 3)
    pixel2 = Pixel(1, 2, 3)
    result = pixel1 - pixel2

    assert result.r == 2
    assert result.g == 1
    assert result.b == 0


def test_difference_to_reach_out_of_range():
    pixel1 = Pixel(1, 3, 1)
    pixel2 = Pixel(4, 255, 255)
    result = pixel1 - pixel2
    assert result.r == 0
    assert result.g == 0
    assert result.b == 0


# negative test case, expected TypeError exception
@pytest.mark.xfail(reason="negative test case, expected TypeError exception")
def test_difference_with_wrong_types():
    pixel1 = Pixel(3, "3", 3)
    pixel2 = Pixel("1", 2, 3)
    result = pixel1 - pixel2

    assert result.r == 2
    assert result.g == 1
    assert result.b == 0


# multiplication cases
def test_multiply_with_int():
    pixel1 = Pixel(1, 2, 3)
    result = pixel1 * 2

    assert result.r == 2
    assert result.g == 4
    assert result.b == 6


def test_multiply_with_float():
    pixel1 = Pixel(1.0, 2.0, 3.0)
    result = 3.0 * pixel1

    assert result.r == 3
    assert result.g == 6
    assert result.b == 9


def test_multiply_to_reach_out_of_range():
    pixel1 = Pixel(255, 255.0, 255)
    result = pixel1 * 5

    assert result.r == 255
    assert result.g == 255
    assert result.b == 255


# negative test case, expected ValueError exception
@pytest.mark.xfail(reason="negative test case, expected ValueError exception")
def test_multiply_with_0():
    pixel1 = Pixel(1, 2, 3)
    result = pixel1 * 0

    assert result.r == 0
    assert result.g == 0
    assert result.b == 0


# negative test case, expected TypeError exception
@pytest.mark.xfail(reason="negative test case, expected TypeError exception")
def test_multiply_with_wrong_type():
    pixel1 = Pixel(1, 3, 32.0)
    result = pixel1 * "1"

    assert result.r == 1
    assert result.g == 3
    assert result.b == 32


# division cases
def test_div_with_int():
    pixel1 = Pixel(6, 9, 12)
    result = pixel1 / 2

    assert result.r == 3
    assert result.g == 4
    assert result.b == 6


def test_div_with_float():
    pixel1 = Pixel(3, 6.0, 3.0)
    result = pixel1 / 3.0

    assert result.r == 1
    assert result.g == 2
    assert result.b == 1


# negative test case, expected ValueError exception
@pytest.mark.xfail(reason="negative test case, expected ValueError exception")
def test_div_with_0():
    pixel1 = Pixel(3, 3, 3)
    result = pixel1 / 0

    assert result.r == 0
    assert result.g == 0
    assert result.b == 0


# negative test case, expected TypeError exception
@pytest.mark.xfail(reason="negative test case, expected TypeError exception")
def test_div_with_wrong_type():
    pixel1 = Pixel(3, 3, 6)
    result = pixel1 / "3"

    assert result.r == 1
    assert result.g == 1
    assert result.b == 2


def test_random_pixel():
    pixel = Pixel(10.0, 10, 10)
    result = pixel.get_pixel_near(2)
    assert 8.0 <= result.r <= 12.0
    assert 8 <= result.g <= 12
    assert 8 <= result.b <= 12


def test_random_pixel_near_0():
    pixel = Pixel(10.0, 10, 10)
    result = pixel.get_pixel_near(0)
    print(result)
    assert 8.0 <= result.r <= 12.0
    assert 8 <= result.g <= 12
    assert 8 <= result.b <= 12


# negative test case, expected ValueError exception
@pytest.mark.xfail(reason="negative test case, expected ValueError exception")
def test_random_pixel_near_out_of_range_number():
    pixel = Pixel(0, 255, 2)
    result = pixel.get_pixel_near(2)
    assert -2 <= result.r <= 2
    assert 253 <= result.g <= 257
    assert 0 <= result.b <= 4

