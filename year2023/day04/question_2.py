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


def get_n_winning_numbers(card_description: str) -> int:
    winning_numbers, player_numbers = get_winning_and_player_numbers(card_description)
    return sum(n in winning_numbers for n in player_numbers)


def get_n_total_scratchcards(card_descriptions: list[str]) -> int:
    card_counts = [1] * len(card_descriptions)

    for card_idx, card_description in enumerate(card_descriptions):
        n_winning_numbers = get_n_winning_numbers(card_description)
        n_copies_of_this_card = card_counts[card_idx]

        for i in range(card_idx + 1, card_idx + 1 + n_winning_numbers):
            card_counts[i] += n_copies_of_this_card

    return sum(card_counts)


if __name__ == "__main__":
    with open(YEAR_2023_DIR / "day04/data.txt", encoding="utf-8") as fp:
        question_input = fp.readlines()

    print("Example total: ", get_n_total_scratchcards(EXAMPLE))
    print("Question total: ", get_n_total_scratchcards(question_input))
