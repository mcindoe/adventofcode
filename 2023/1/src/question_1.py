from collections.abc import Iterable
from pathlib import Path


def get_first_digit(str_iterable: Iterable[str]) -> str:
    """
    Get the first numberic character in a string iterable,
    raising an exception if not found
    """

    for char in str_iterable:
        if char.isnumeric():
            return char

    raise ValueError(f"Unable to find any digits in {str_iterable}")


def get_calibration_value(text: str) -> int:
    """
    Get the first and last digits from a string,
    concatenate together and parse as an integer
    """

    first_digit = get_first_digit(text)
    last_digit = get_first_digit(reversed(text))
    return int(f"{first_digit}{last_digit}")


if __name__ == "__main__":
    input_file = Path(__file__).parents[1] / "data/question_1_input.txt"

    with open(input_file, "r") as fp:
        sum_of_calibrations = sum(get_calibration_value(text) for text in fp)

    print(f"Sum of calibrations: {sum_of_calibrations}")
