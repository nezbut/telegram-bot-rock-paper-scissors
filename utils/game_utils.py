def user_winner(bot_answer: str, user_answer: str) -> bool | None:
    bot_answer = ''.join(filter(lambda a: a.isalpha(), bot_answer)).lower().strip()
    user_answer = ''.join(filter(lambda a: a.isalpha(), user_answer)).lower().strip()

    if bot_answer == user_answer:
        return

    return any(
        [
            user_answer == 'камень' and bot_answer == 'ножницы',
            user_answer == 'ножницы' and bot_answer == 'бумага',
            user_answer == 'бумага' and bot_answer == 'камень'
        ]
    )

__all__ = (
    'user_winner',
)
