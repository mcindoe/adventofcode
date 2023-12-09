from collections.abc import Generator
from enum import Enum
import math

from adventofcode.location import YEAR_2023_DIR


class Colour(Enum):
    blue = "blue"
    red = "red"
    green = "green"


TEST_CASES = {
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green": 48,
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue": 12,
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red": 1560,
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red": 630,
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green": 36,
}


def parse_game_entry_str(game_entry_str: str) -> dict[Colour, int]:
    specified_cubes = {}
    for cube_number_description in game_entry_str.split(","):
        cube_number_description = cube_number_description.strip()
        number, colour = cube_number_description.split(" ")
        specified_cubes[Colour[colour]] = int(number)

    return specified_cubes


def get_all_game_entries(game_description: str) -> Generator[dict[Colour, int]]:
    return (parse_game_entry_str(x) for x in game_description.split(";"))


def get_minimum_required_cubes(game_description: str) -> dict[Colour, int]:
    minimum_required_cubes = {colour: 0 for colour in Colour}
    for game_entry in get_all_game_entries(game_description):
        for colour, required_number in game_entry.items():
            minimum_required_cubes[colour] = max(
                minimum_required_cubes[colour], required_number
            )

    return minimum_required_cubes


def get_power_of_required_cubes(game_description: str) -> int:
    minimum_required_cubes = get_minimum_required_cubes(game_description)
    return math.prod(minimum_required_cubes.values())


def run_tests():
    for test_input, expected_test_output in TEST_CASES.items():
        observed_test_output = get_power_of_required_cubes(test_input.split(":")[1])
        assert expected_test_output == observed_test_output


if __name__ == "__main__":
    run_tests()

    DATA_FILE_PATH = YEAR_2023_DIR / "day02/data.txt"

    with open(DATA_FILE_PATH, "r", encoding="utf-8") as fp:
        sum_of_powers = sum(
            get_power_of_required_cubes(line.split(":")[1]) for line in fp
        )

    print(f"Sum of powers: {sum_of_powers}")
