from collections.abc import Iterable
from pathlib import Path


numbers = (
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
)


def get_first_number(str_iterable: Iterable[str], number_strings: Iterable[str]) -> str:
    """
    Get the first numeric digit, or number spelled out as
    a string, in a string iterable
    """

    str_iterable = str(str_iterable)
    number_strings = tuple(str(x) for x in number_strings)

    for char_idx, char in enumerate(str_iterable):
        if char.isnumeric():
            return char

        for number_idx, number in enumerate(number_strings):
            if char_idx + len(number) >= len(str_iterable):
                continue

            if str_iterable[char_idx:].startswith(number):
                return number_idx + 1

    raise ValueError(f"Unable to find any digits in {str_iterable}")


def get_calibration_value(text: str) -> int:
    """
    Get the first and last numbers from a string,
    concatenate together and parse as an integer
    """

    first_number = get_first_number(text, numbers)
    last_number = get_first_number(text[::-1], (n[::-1] for n in numbers))
    return int(f"{first_number}{last_number}")


def run_tests():
    expected_results = {
        "two1nine": 29,
        "eightwothree": 83,
        "abcone2threexyz": 13,
        "xtwone3four": 24,
        "4nineeightseven2": 42,
        "zoneight234": 14,
        "7pqrstsixteen": 76,
    }
    for text, expected_result in expected_results.items():
        assert get_calibration_value(text) == expected_result


if __name__ == "__main__":
    input_file = Path(__file__).parents[1] / "data.txt"

    with open(input_file, "r") as fp:
        sum_of_calibrations = sum(get_calibration_value(text) for text in fp)

    print(f"Sum of calibrations: {sum_of_calibrations}")
