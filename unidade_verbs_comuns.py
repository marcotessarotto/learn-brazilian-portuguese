from utilities import WordType, WordNote, PronNote, BookPage, Level, Item, process_dictionary, find_random_answers, \
    start_tests, WebLink

verbs_comuns = {}

verbs_comuns["fazer (fare)"] = (
    ("fazer", "fare", WordType.VERB),
    ("eu faço", "io faccio", WordType.VERB),
    ("você faz", "tu fai", WordType.VERB),
    ("ele faz", "lui fa", WordType.VERB),
    ("ela faz", "lei fa", WordType.VERB),
    ("nós fazemos", "noi facciamo", WordType.VERB),
    ("vocês fazem", "voi fate", WordType.VERB),
    ("eles fazem", "essi fanno", WordType.VERB),
    ("elas fazem", "esse fanno", WordType.VERB),
    ("não faço", "non faccio"),
    ("não faz", "non fai/non fa"),
    ("não fazemos", "non facciamo"),
    ("não fazem", "non fate/non fanno"),
)

verbs_comuns["poder (potere)"] = (
    ("poder", "potere", WordType.VERB),
    ("eu posso", "io posso", WordType.VERB),
    ("você pode", "tu puoi", WordType.VERB),
    ("ele pode", "lui può", WordType.VERB),
    ("ela pode", "lei può", WordType.VERB),
    ("nós podemos", "noi possiamo", WordType.VERB),
    ("vocês podem", "voi potete", WordType.VERB),
    ("eles podem", "essi possono", WordType.VERB),
    ("elas podem", "esse possono", WordType.VERB),
    ("posso", "posso"),
    ("pode", "puoi/può"),
    ("podemos", "possiamo"),
    ("podem", "potete/possono"),
)

verbs_comuns["saber (sapere)"] = (
    ("saber", "sapere", WordType.VERB),
    ("eu sei", "io so", WordType.VERB),
    ("você sabe", "tu sai", WordType.VERB),
    ("ele sabe", "lui sa", WordType.VERB),
    ("ela sabe", "lei sa", WordType.VERB),
    ("nós sabemos", "noi sappiamo", WordType.VERB),
    ("vocês sabem", "voi sapete", WordType.VERB),
    ("eles sabem", "essi sanno", WordType.VERB),
    ("elas sabem", "esse sanno", WordType.VERB),
    ("sei", "so"),
    ("sabe", "sai/sa"),
    ("sabemos", "sappiamo"),
    ("sabem", "sapete/sanno"),
)

verbs_comuns["gostar (piacere)"] = (
    ("gostar", "piacere", WordType.VERB),
    ("eu gosto", "mi piace (io gusto)", WordType.VERB),
    ("você gosta", "ti piace", WordType.VERB),
    ("ele gosta", "gli piace", WordType.VERB),
    ("ela gosta", "le piace", WordType.VERB),
    ("nós gostamos", "ci piace", WordType.VERB),
    ("vocês gostam", "vi piace", WordType.VERB),
    ("eles gostam", "a loro piace", WordType.VERB),
    ("elas gostam", "a loro piace (f)", WordType.VERB),
    ("gosto de...", "mi piace..."),
    ("você gosta de...", "ti piace..."),
)

verbs_comuns["comprar (comprare)"] = (
    ("comprar", "comprare", WordType.VERB),
    ("eu compro", "io compro", WordType.VERB),
    ("você compra", "tu compri", WordType.VERB),
    ("ele compra", "lui compra", WordType.VERB),
    ("ela compra", "lei compra", WordType.VERB),
    ("nós compramos", "noi compriamo", WordType.VERB),
    ("vocês compram", "voi comprate", WordType.VERB),
    ("eles compram", "essi comprano", WordType.VERB),
    ("elas compram", "esse comprano", WordType.VERB),
)

verbs_comuns["dizer (dire)"] = (
    ("dizer", "dire", WordType.VERB),
    ("eu digo", "io dico", WordType.VERB),
    ("você diz", "tu dici", WordType.VERB),
    ("ele diz", "lui dice", WordType.VERB),
    ("ela diz", "lei dice", WordType.VERB),
    ("nós dizemos", "noi diciamo", WordType.VERB),
    ("vocês dizem", "voi dite", WordType.VERB),
    ("eles dizem", "essi dicono", WordType.VERB),
    ("elas dizem", "esse dicono", WordType.VERB),
)

verbs_comuns["viajar (viaggiare)"] = (
    ("viajar", "viaggiare", WordType.VERB),
    ("eu viajo", "io viaggio", WordType.VERB),
    ("você viaja", "tu viaggi", WordType.VERB),
    ("ele viaja", "lui viaggia", WordType.VERB),
    ("ela viaja", "lei viaggia", WordType.VERB),
    ("nós viajamos", "noi viaggiamo", WordType.VERB),
    ("vocês viajam", "voi viaggiate", WordType.VERB),
    ("eles viajam", "essi viaggiano", WordType.VERB),
    ("elas viajam", "esse viaggiano", WordType.VERB),
)

verbs_comuns["exemplos práticos"] = (
    ("o que você faz?", "cosa fai?"),
    ("eu faço um programa em Python", "io faccio un programma in Python"),
    ("você pode me ajudar?", "puoi aiutarmi?"),
    ("posso pagar com cartão?", "posso pagare con la carta?"),
    ("eu não sei", "io non lo so"),
    ("eu sei programar", "io so programmare"),
    ("você sabe onde é o banheiro?", "sai dov'è il bagno?"),
    ("eu gosto de viajar para o Brasil em janeiro", "mi piace viaggiare in Brasile a gennaio"),
    ("eu gosto de tocar violão", "mi piace suonare la chitarra"),
    ("nós gostamos de comer pizza", "ci piace mangiare la pizza"),
    ("eu compro uma casa nova", "io compro una casa nuova"),
    ("você compra pão?", "compri il pane?"),
    ("como se diz isso?", "come si dice questo?"),
    ("ela diz que sim", "lei dice di sì"),
    ("eu uso Linux", "io uso Linux"),
)

def run_me():
    dict_pt, dict_ita = process_dictionary(verbs_comuns)

    print("1 - test da portoghese a italiano")
    print("2 - test da italiano a portoghese")
    data = input("risposta (q per uscire): ")
    if data is None or data == "q":
        return
    elif data == "1":
        start_tests(dict_pt)
    elif data == "2":
        start_tests(dict_ita, pt2ita=False)
    else:
        print("risposta non valida")

if __name__ == "__main__":
    run_me()