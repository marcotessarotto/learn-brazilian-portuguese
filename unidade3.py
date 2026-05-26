from utilities import WordType, WordNote, PronNote, BookPage, Level, Item, process_dictionary, find_random_answers, \
    start_tests, Gender, generic_run_me

enota = {}

enota["unidade 3"] = (
    # Dias da semana e tempo (Giorni della settimana e tempo)
    ("segunda-feira", "lunedì"),
    ("terça-feira", "martedì"),
    ("quarta-feira", "mercoledì"),
    ("quinta-feira", "giovedì"),
    ("sexta-feira", "venerdì"),
    ("sábado", "sabato"),
    ("domingo", "domenica"),
    ("hoje", "oggi"),
    ("amanhã", "domani"),
    ("ontem", "ieri"),
    ("fim de semana", "fine settimana"),

    # Cores (Colori)
    ("branco", "bianco"),
    ("preto", "nero"),
    ("vermelho", "rosso"),
    ("azul", "blu"),
    ("verde", "verde"),
    ("amarelo", "giallo"),

    # Interesses, profissões e cotidiano (Interessi, professioni e quotidianità)
    ("computador", "computer", Gender.MALE),
    ("teclado", "tastiera", Gender.MALE),
    ("tela", "schermo", Gender.FEMALE),
    ("banco de dados", "database", Gender.MALE),
    ("engenharia de software", "ingegneria del software", Gender.FEMALE),
    ("criptografia", "crittografia", Gender.FEMALE),
    ("violão", "chitarra acustica", Gender.MALE),
    ("guitarra", "chitarra elettrica", Gender.FEMALE),
    ("música", "musica", Gender.FEMALE),
    ("futebol", "calcio", Gender.MALE),
    ("futsal", "calcio a 5", Gender.MALE),
    ("psicoterapia", "psicoterapia", Gender.FEMALE),
    ("clínica", "studio (medico)", Gender.FEMALE),
    ("investimento", "investimento", Gender.MALE),
    ("imóvel", "immobile", Gender.MALE),

    # Frases práticas (Frasi pratiche)
    ("que dia é hoje?", "che giorno è oggi?"),
    ("hoje é segunda-feira", "oggi è lunedì"),
    ("eu jogo futsal na quinta-feira", "io gioco a calcio a 5 il giovedì"),
    ("eu toco guitarra no fim de semana", "io suono la chitarra elettrica nel fine settimana"),
    ("ela trabalha na clínica", "lei lavora nello studio"),
    ("eu programo em Python", "io programmo in Python"),
    ("o banco de dados está pronto", "il database è pronto"),
    ("vou comprar um imóvel novo", "voglio comprare un immobile nuovo"),
    ("a tela do meu computador é grande", "lo schermo del mio computer è grande"),
)

if __name__ == "__main__":
    generic_run_me(enota)