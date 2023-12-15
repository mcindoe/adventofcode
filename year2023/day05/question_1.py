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
            (
                int(destination_range_start),
                int(source_range_start),
                int(range_length),
            )
            for entry in range_descriptions
            for destination_range_start, source_range_start, range_length in entry.strip().split(
                " "
            )
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


def get_seeds(puzzle_line: str) -> tuple[int]:
    assert puzzle_line.startswith("seeds:")
    return tuple(int(x) for x in puzzle_line.lstrip("sedes:").strip().split(" "))


def get_maps(puzzle_input) -> list[SourceToDestinationMap]:
    map_description_line_numbers = tuple(
        line_number for line_number, line in enumerate(puzzle_input) if "map:" in line
    )
    for idx, line_number in enumerate(map_description_indices):
        pass

    pass


if __name__ == "__main__":
    with open(YEAR_2023_DIR / "day05/data.txt", "r", encoding="utf-8") as fp:
        question_input = fp.readlines()
