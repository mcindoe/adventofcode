from adventofcode.location import YEAR_2023_DIR

EXAMPLE = [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
]


def get_winning_and_player_numbers(
    card_description: str,
) -> tuple[set[int], tuple[int]]:
    card_description = card_description.split(":")[1].replace("  ", " ")
    winning_numbers, player_numbers = card_description.split("|")
    winning_numbers = set(int(x.strip()) for x in winning_numbers.strip().split(" "))
    player_numbers = tuple(int(x.strip()) for x in player_numbers.strip().split(" "))

    return winning_numbers, player_numbers


def get_card_value(card_description: str) -> int:
    winning_numbers, player_numbers = get_winning_and_player_numbers(card_description)
    n_winning_numbers = sum(n in winning_numbers for n in player_numbers)

    if n_winning_numbers == 0:
        return 0

    return 2 ** (n_winning_numbers - 1)


def get_sum_of_card_values(card_descriptions: list[str]) -> int:
    return sum(
        get_card_value(card_description) for card_description in card_descriptions
    )


def run_tests():
    for card_index, card_description in enumerate(EXAMPLE, start=1):
        print(f"{card_index}: {get_card_value(card_description)}")


if __name__ == "__main__":
    run_tests()

    with open(YEAR_2023_DIR / "day04/data.txt", encoding="utf-8") as fp:
        question_input = fp.readlines()

    print("Example total: ", get_sum_of_card_values(EXAMPLE))
    print("Question total: ", get_sum_of_card_values(question_input))
