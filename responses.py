
def get_response(user_message: str) -> str:
    lowered: str = user_message.lower()

    if lowered == 'halo':
        return "Haiii \(> v <)/"
    elif lowered == 'hai':
        return "Halooo \(^ o ^)/"
    else:
        return "Ga ngerti 😔"