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


def get_part_number_locations_on_line(
    schematic: list[str], line_number: int
) -> tuple[int]:
    number_locations = get_number_locations_in_line(schematic[line_number])
    return tuple(
        (number_start, number_end)
        for number_start, number_end in number_locations
        if location_is_part_number(schematic, line_number, number_start, number_end)
    )


def get_adjacent_part_numbers(
    schematic: list[str], line_number: int, char_idx: int
) -> list[int]:
    adjacent_part_numbers = []

    for row in range(line_number - 1, line_number + 2):
        if not 0 <= row < len(schematic):
            continue

        row_part_number_locations = get_part_number_locations_on_line(schematic, row)

        for number_start, number_end in row_part_number_locations:
            is_adjacent = char_idx in range(number_start - 1, number_end + 1)
            if is_adjacent:
                adjacent_part_numbers.append(
                    int(schematic[row][number_start:number_end])
                )

    return adjacent_part_numbers


def get_sum_of_gear_ratios(schematic: list[str]) -> int:
    gear_ratio_sum = 0

    for line_idx, line in enumerate(schematic):
        for char_idx, char in enumerate(line):
            if char != "*":
                continue

            adjacent_part_numbers = get_adjacent_part_numbers(
                schematic, line_idx, char_idx
            )
            is_gear = len(adjacent_part_numbers) == 2
            if is_gear:
                gear_ratio = adjacent_part_numbers[0] * adjacent_part_numbers[1]
                gear_ratio_sum += gear_ratio

    return gear_ratio_sum


if __name__ == "__main__":
    with open(YEAR_2023_DIR / "day03/data.txt", "r", encoding="utf-8") as fp:
        question_schematic = fp.readlines()

    print("Example gear ratio:", get_sum_of_gear_ratios(EXAMPLE_SCHEMATIC))
    print("Question Answer:", get_sum_of_gear_ratios(question_schematic))
