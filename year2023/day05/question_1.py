from adventofcode.location import YEAR_2023_DIR


EXAMPLE = [
    "seeds: 79 14 55 13",
    "",
    "seed-to-soil map:",
    "50 98 2",
    "52 50 48",
    "",
    "soil-to-fertilizer map:",
    "0 15 37",
    "37 52 2",
    "39 0 15",
    "",
    "fertilizer-to-water map:",
    "49 53 8",
    "0 11 42",
    "42 0 7",
    "57 7 4",
    "",
    "water-to-light map:",
    "88 18 7",
    "18 25 70",
    "",
    "light-to-temperature map:",
    "45 77 23",
    "81 45 19",
    "68 64 13",
    "",
    "temperature-to-humidity map:",
    "0 69 1",
    "1 0 69",
    "",
    "humidity-to-location map:",
    "60 56 37",
    "56 93 4",
]


class SourceToDestinationMap:
    def __init__(self, range_descriptions: list[str]):
        self.__range_descriptions = tuple(
            tuple(int(x) for x in entry.strip().split(" "))
            for entry in range_descriptions
        )

    def __call__(self, x: int) -> int:
        for (
            destination_range_start,
            source_range_start,
            range_length,
        ) in self.__range_descriptions:
            if x in range(source_range_start, source_range_start + range_length):
                return destination_range_start + x - source_range_start

        return x


def get_seeds(puzzle_input: list[str]) -> tuple[int]:
    first_line = puzzle_input[0]
    assert first_line.startswith("seeds:")
    return tuple(int(x) for x in first_line.lstrip("seeds:").strip().split(" "))


def get_maps(puzzle_input: list[str]) -> tuple[SourceToDestinationMap]:
    map_description_line_numbers = tuple(
        line_number for line_number, line in enumerate(puzzle_input) if "map:" in line
    )

    map_range_description_bounds = tuple(
        (
            map_description_line_numbers[idx] + 1,
            map_description_line_numbers[idx + 1] - 1,
        )
        for idx in range(len(map_description_line_numbers) - 1)
    ) + ((map_description_line_numbers[-1] + 1, len(puzzle_input)),)

    return tuple(
        SourceToDestinationMap(
            puzzle_input[range_description_start:range_description_stop]
        )
        for range_description_start, range_description_stop in map_range_description_bounds
    )


def get_seed_locations(puzzle_input: list[str]) -> dict[int, int]:
    seeds = get_seeds(puzzle_input)
    source_to_destination_maps = get_maps(puzzle_input)

    seed_destinations = {}
    for seed in seeds:
        location = seed
        for source_to_destination_map in source_to_destination_maps:
            location = source_to_destination_map(location)

        seed_destinations[seed] = location

    return seed_destinations


def get_lowest_seed_location(puzzle_input: list[str]) -> int:
    seed_locations = get_seed_locations(puzzle_input)
    return min(seed_locations.values())


def run_tests():
    example_seed_locations = get_seed_locations(EXAMPLE)
    expected_seed_locations = {79: 82, 14: 43, 55: 86, 13: 35}
    assert example_seed_locations == expected_seed_locations


if __name__ == "__main__":
    run_tests()

    with open(YEAR_2023_DIR / "day05/data.txt", "r", encoding="utf-8") as fp:
        question_input = fp.readlines()

    lowest_seed_location = get_lowest_seed_location(question_input)
    print(f"Lowest seed location: {lowest_seed_location}")
