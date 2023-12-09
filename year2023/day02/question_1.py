from enum import Enum

from adventofcode.location import YEAR_2023_DIR


class Colour(Enum):
    blue = "blue"
    red = "red"
    green = "green"


MAX_CUBES = {Colour.blue: 14, Colour.red: 12, Colour.green: 13}


TEST_CASES = {
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green": 1,
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue": 2,
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red": 0,
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red": 0,
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green": 5,
}


def parse_game_entry_str(game_entry_str: str) -> dict[Colour, int]:
    specified_cubes = {}
    for cube_number_description in game_entry_str.split(","):
        cube_number_description = cube_number_description.strip()
        number, colour = cube_number_description.split(" ")
        specified_cubes[Colour[colour]] = int(number)

    return specified_cubes


def game_entry_is_possible(game_entry: dict[Colour, int]) -> bool:
    for colour, game_entry_colour_number in game_entry.items():
        max_allowed = MAX_CUBES[colour]
        if game_entry_colour_number > max_allowed:
            return False

    return True


def game_is_possible(game_description: str) -> bool:
    return all(
        game_entry_is_possible(parse_game_entry_str(game_entry_str))
        for game_entry_str in game_description.split(";")
    )


def get_index_if_possible_else_zero(game_line: str) -> int:
    game_index_str, game_description = game_line.split(":")
    game_index = int(game_index_str.removeprefix("Game "))

    if game_is_possible(game_description):
        return game_index

    return 0


def run_tests():
    for test_input, expected_test_output in TEST_CASES.items():
        assert get_index_if_possible_else_zero(test_input) == expected_test_output


if __name__ == "__main__":
    run_tests()

    DATA_FILE_PATH = YEAR_2023_DIR / "day02/data.txt"

    with open(DATA_FILE_PATH, "r", encoding="utf-8") as fp:
        sum_of_possible_indices = sum(
            get_index_if_possible_else_zero(line) for line in fp
        )

    print(f"Sum of possible game indices: {sum_of_possible_indices}")
