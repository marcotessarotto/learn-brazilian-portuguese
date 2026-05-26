from utilities import WordType, WordNote, PronNote, BookPage, Level, Item, process_dictionary, find_random_answers, \
    start_tests, Gender, generic_run_me

enota_pre_a1 = {}

enota_pre_a1["elementos principais (pre-A1)"] = (
    # Palavras interrogativas (Parole interrogative)
    ("o que?", "cosa?", WordType.PRONOUN),
    ("quem?", "chi?", WordType.PRONOUN),
    ("onde?", "dove?", WordType.PRONOUN),
    ("quando?", "quando?", WordType.PRONOUN),
    ("como?", "come?", WordType.PRONOUN),
    ("por que?", "perché? (domanda)", WordType.PRONOUN),
    ("porque", "perché (risposta)", WordType.CONJUNCTION),
    ("quanto?", "quanto?", WordType.PRONOUN),
    ("qual?", "quale?", WordType.PRONOUN),

    # Conectores e preposições (Connettivi e preposizioni)
    ("com", "con", WordType.CONJUNCTION),
    ("sem", "senza", WordType.CONJUNCTION),
    ("para", "per", WordType.CONJUNCTION),
    ("de", "di / da", WordType.CONJUNCTION),
    ("em", "in", WordType.CONJUNCTION),
    ("mas", "ma", WordType.CONJUNCTION),
    ("e", "e", WordType.CONJUNCTION),
    ("ou", "o / oppure", WordType.CONJUNCTION),

    # Espaço e direções (Spazio e direzioni)
    ("aqui", "qui", WordType.ADVERB),
    ("ali", "lì", WordType.ADVERB),
    ("perto", "vicino", WordType.ADVERB),
    ("longe", "lontano", WordType.ADVERB),
    ("à direita", "a destra"),
    ("à esquerda", "a sinistra"),
    ("em frente", "dritto / di fronte"),
    ("rua", "strada / via", Gender.FEMALE),
    ("praça", "piazza", Gender.FEMALE),

    # Adjetivos básicos (Aggettivi di base)
    ("bom", "buono", WordType.ADJECTIVE),
    ("ruim", "cattivo / brutto (di qualità)", WordType.ADJECTIVE),
    ("quente", "caldo", WordType.ADJECTIVE),
    ("frio", "freddo", WordType.ADJECTIVE),
    ("novo", "nuovo", WordType.ADJECTIVE),
    ("velho", "vecchio", WordType.ADJECTIVE),
    ("aberto", "aperto", WordType.ADJECTIVE),
    ("fechado", "chiuso", WordType.ADJECTIVE),
    ("caro", "costoso", WordType.ADJECTIVE),
    ("barato", "economico", WordType.ADJECTIVE),

    # Logística e viagem (Logistica e viaggio)
    ("aeroporto", "aeroporto", Gender.MALE),
    ("táxi", "taxi", Gender.MALE),
    ("hotel", "hotel", Gender.MALE),
    ("restaurante", "ristorante", Gender.MALE),
    ("farmácia", "farmacia", Gender.FEMALE),
    ("hospital", "ospedale", Gender.MALE),
    ("polícia", "polizia", Gender.FEMALE),
    ("caixa eletrônico", "bancomat", Gender.MALE),
    ("dinheiro", "soldi / contanti", Gender.MALE),
    ("cartão", "carta (di credito/debito)", Gender.MALE),

    # Frases de sobrevivência e emergência (Frasi di sopravvivenza ed emergenza)
    ("não falo português", "non parlo portoghese", WordType.SENTENCE),
    ("fale mais devagar, por favor", "parli più piano, per favore", WordType.SENTENCE),
    ("eu não entendo", "io non capisco", WordType.SENTENCE),
    ("pode repetir, por favor?", "può ripetere, per favore?", WordType.SENTENCE),
    ("socorro! / ajuda!", "aiuto!", WordType.SENTENCE),
    ("preciso de ajuda", "ho bisogno di aiuto", WordType.SENTENCE),
    ("onde fica o banheiro?", "dov'è il bagno?", WordType.SENTENCE),
    ("onde fica o hotel?", "dov'è l'hotel?", WordType.SENTENCE),
    ("onde tem um caixa eletrônico?", "dove c'è un bancomat?", WordType.SENTENCE),
    ("quanto custa isso?", "quanto costa questo?", WordType.SENTENCE),
    ("estou perdido", "mi sono perso (m)", WordType.SENTENCE),
    ("estou perdida", "mi sono persa (f)", WordType.SENTENCE),
    ("perdi meu telefone", "ho perso il mio telefono", WordType.SENTENCE),
    ("perdi minha carteira", "ho perso il mio portafoglio", WordType.SENTENCE),
    ("eu queria...", "vorrei...", WordType.SENTENCE),
    ("a conta, por favor", "il conto, per favore", WordType.SENTENCE),
)

def run_me():
    dict_pt, dict_ita = process_dictionary(enota_pre_a1)

    print("1 - test da portoghese a italiano")
    print("2 - test da italiano a portoghese")
    data = input("risposta (q per uscire): ")
    if data is None or data == "q":
        return
    elif data == "1":
        start_tests(dict_pt, pt2ita=True)
    elif data == "2":
        start_tests(dict_ita, pt2ita=False)
    else:
        print("risposta non valida")

if __name__ == "__main__":
    run_me()