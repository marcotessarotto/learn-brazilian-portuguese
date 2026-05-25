from utilities import WordType, WordNote, PronNote, BookPage, Level, Item, process_dictionary, find_random_answers, \
    start_tests, WebLink

verbs_irregulares = {}

verbs_irregulares["trazer (portare)"] = (
    ("trazer", "portare", WordType.VERB),
    ("eu trago", "io porto", WordType.VERB),
    ("você traz", "tu porti", WordType.VERB),
    ("ele traz", "lui porta", WordType.VERB),
    ("ela traz", "lei porta", WordType.VERB),
    ("nós trazemos", "noi portiamo", WordType.VERB),
    ("vocês trazem", "voi portate", WordType.VERB),
    ("eles trazem", "essi portano", WordType.VERB),
    ("elas trazem", "esse portano", WordType.VERB),
    ("não trago", "non porto"),
    ("não traz", "non porti/non porta"),
)

verbs_irregulares["sair (uscire)"] = (
    ("sair", "uscire", WordType.VERB),
    ("eu saio", "io esco", WordType.VERB),
    ("você sai", "tu esci", WordType.VERB),
    ("ele sai", "lui esce", WordType.VERB),
    ("ela sai", "lei esce", WordType.VERB),
    ("nós saímos", "noi usciamo", WordType.VERB),
    ("vocês saem", "voi uscite", WordType.VERB),
    ("eles saem", "essi escono", WordType.VERB),
    ("elas saem", "esse escono", WordType.VERB),
)

verbs_irregulares["ouvir (sentire/ascoltare)"] = (
    ("ouvir", ("sentire", "ascoltare"), WordType.VERB),
    ("eu ouço", "io sento", WordType.VERB),
    ("você ouve", "tu senti", WordType.VERB),
    ("ele ouve", "lui sente", WordType.VERB),
    ("ela ouve", "lei sente", WordType.VERB),
    ("nós ouvimos", "noi sentiamo", WordType.VERB),
    ("vocês ouvem", "voi sentite", WordType.VERB),
    ("eles ouvem", "essi sentono", WordType.VERB),
    ("elas ouvem", "esse sentono", WordType.VERB),
)

verbs_irregulares["pedir (chiedere/ordinare)"] = (
    ("pedir", ("chiedere", "ordinare"), WordType.VERB),
    ("eu peço", "io chiedo", WordType.VERB),
    ("você pede", "tu chiedi", WordType.VERB),
    ("ele pede", "lui chiede", WordType.VERB),
    ("ela pede", "lei chiede", WordType.VERB),
    ("nós pedimos", "noi chiediamo", WordType.VERB),
    ("vocês pedem", "voi chiedete", WordType.VERB),
    ("eles pedem", "essi chiedono", WordType.VERB),
    ("elas pedem", "esse chiedono", WordType.VERB),
)

verbs_irregulares["dormir (dormire)"] = (
    ("dormir", "dormire", WordType.VERB),
    ("eu durmo", "io dormo", WordType.VERB),
    ("você dorme", "tu dormi", WordType.VERB),
    ("ele dorme", "lui dorme", WordType.VERB),
    ("ela dorme", "lei dorme", WordType.VERB),
    ("nós dormimos", "noi dormiamo", WordType.VERB),
    ("vocês dormem", "voi dormite", WordType.VERB),
    ("eles dormem", "essi dormono", WordType.VERB),
    ("elas dormem", "esse dormono", WordType.VERB),
)

verbs_irregulares["pôr (mettere)"] = (
    ("pôr", "mettere", WordType.VERB),
    ("eu ponho", "io metto", WordType.VERB),
    ("você põe", "tu metti", WordType.VERB),
    ("ele põe", "lui mette", WordType.VERB),
    ("ela põe", "lei mette", WordType.VERB),
    ("nós pomos", "noi mettiamo", WordType.VERB),
    ("vocês põem", "voi mettete", WordType.VERB),
    ("eles põem", "essi mettono", WordType.VERB),
    ("elas põem", "esse mettono", WordType.VERB),
)

verbs_irregulares["vir (venire)"] = (
    ("vir", "venire", WordType.VERB),
    ("eu venho", "io vengo", WordType.VERB),
    ("você vem", "tu vieni", WordType.VERB),
    ("ele vem", "lui viene", WordType.VERB),
    ("ela vem", "lei viene", WordType.VERB),
    ("nós vimos", "noi veniamo", WordType.VERB),
    ("vocês vêm", "voi venite", WordType.VERB),
    ("eles vêm", "essi vengono", WordType.VERB),
    ("elas vêm", "esse vengono", WordType.VERB),
)

verbs_irregulares["exemplos práticos"] = (
    ("eu trago o vinho e você traz a cerveja", "io porto il vino e tu porti la birra"),
    ("a que horas você sai do trabalho?", "a che ora esci dal lavoro?"),
    ("eu saio às seis da tarde", "esco alle sei di sera"),
    ("você ouve música brasileira?", "ascolti musica brasiliana?"),
    ("eu não ouço nada", "non sento niente"),
    ("no restaurante, eu peço uma pizza", "al ristorante, io ordino una pizza"),
    ("posso pedir um favor?", "posso chiedere un favore?"),
    ("eu durmo oito horas por noite", "io dormo otto ore a notte"),
    ("o menino dorme muito", "il bambino dorme molto"),
    ("onde você põe as chaves?", "dove metti le chiavi?"),
    ("eu ponho o livro na mesa", "io metto il libro sul tavolo"),
    ("de onde você vem?", "da dove vieni?"),
    ("eu venho da Itália", "io vengo dall'Italia"),
    ("eles vêm para a festa", "loro vengono alla festa"),
)

def run_me():
    dict_pt, dict_ita = process_dictionary(verbs_irregulares)

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