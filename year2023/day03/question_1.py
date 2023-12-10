from adventofcode.location import YEAR_2023_DIR

EXAMPLE_SCHEMATIC = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
]


def get_number_locations_in_line(schematic_line: str) -> list[tuple[int, int]]:
    """
    Return the first (inclusive) and last index (exclusive) of all numbers
    in the schematic
    """

    number_locations = []

    in_number = False
    number_start = None

    for char_idx, char in enumerate(schematic_line):
        if char.isnumeric():
            if not in_number:
                number_start = char_idx
                in_number = True
            if char_idx == len(schematic_line) - 1:
                number_locations.append((number_start, char_idx + 1))

        elif in_number:
            number_end = char_idx
            in_number = False
            number_locations.append((number_start, number_end))

    return number_locations


def is_symbol(char: str) -> bool:
    return (not char.isnumeric()) and (char != ".") and (char != "\n")


def location_is_part_number(
    schematic: list[str], number_row: int, number_start: int, number_end: int
) -> bool:
    for row in range(number_row - 1, number_row + 2):
        for col in range(number_start - 1, number_end + 1):
            if (not 0 <= row < len(schematic)) or (not 0 <= col < len(schematic[0])):
                continue

            try:
                if is_symbol(schematic[row][col]):
                    return True
            except IndexError:
                continue

    return False


def get_schematic_part_numbers(schematic: list[str], line_number: int) -> tuple[int]:
    number_locations = get_number_locations_in_line(schematic[line_number])
    schematic_part_numbers = tuple(
        int(schematic[line_number][number_start:number_end])
        for number_start, number_end in number_locations
        if location_is_part_number(schematic, line_number, number_start, number_end)
    )

    return schematic_part_numbers


def get_sum_of_schematic_part_numbers(schematic: list[str]) -> int:
    return sum(
        sum(get_schematic_part_numbers(schematic, line_number))
        for line_number in range(len(schematic))
    )


def run_tests():
    assert get_number_locations_in_line(EXAMPLE_SCHEMATIC[0]) == [(0, 3), (5, 8)]
    assert location_is_part_number(EXAMPLE_SCHEMATIC, 0, 0, 3)
    assert not location_is_part_number(EXAMPLE_SCHEMATIC, 0, 5, 8)


if __name__ == "__main__":
    run_tests()

    with open(YEAR_2023_DIR / "day03/data.txt", "r", encoding="utf-8") as fp:
        question_schematic = fp.readlines()

    print("Example:", get_sum_of_schematic_part_numbers(EXAMPLE_SCHEMATIC))
    print("Question Answer:", get_sum_of_schematic_part_numbers(question_schematic))
