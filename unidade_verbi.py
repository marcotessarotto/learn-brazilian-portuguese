from utilities import WordType, WordNote, PronNote, BookPage, Level, Item, process_dictionary, find_random_answers, \
    start_tests, WebLink, generic_run_me

verbs = {}

verbs["pronomes"] = (
    ("eu", "io"),
    ("você", "tu"),
    ("ele", "lui"),
    ("ela", "lei"),
    ("nós", "noi"),
    ("vocês", "voi"),
    ("eles", "essi"),
    ("elas", "esse"),
)

verbs["extra"] = (
    ("presente", "presente"),
    ("qual", "quale"),
    ("quais", "quali"),
)

verbs["ser/estar"] = (
    ("eu sou", "io sono", WordType.VERB),
    ("você é", "tu sei", WordType.VERB),
    ("ele é", "lui è", WordType.VERB),
    ("ela é", "lei è", WordType.VERB),
    ("nós somos", "noi siamo", WordType.VERB),
    ("vocês são", "voi siete", WordType.VERB),
    ("eles são", "essi sono", WordType.VERB),
    ("elas são", "esse sono", WordType.VERB),
    ("eu não sou", "io non sono", WordType.VERB),
    ("você não é", "tu non sei", WordType.VERB),
    ("ele não é", "lui non è", WordType.VERB),
    ("ela não é", "lei non è", WordType.VERB),
    ("nós não somos", "noi non siamo", WordType.VERB),
    ("vocês não são", "voi non siete", WordType.VERB),
    ("eles não são", "essi non sono", WordType.VERB),
    ("elas não são", "esse non sono", WordType.VERB),
    ("sou", "sono"),
    ("é", "sei/è"),
    ("somos", "siamo"),
    ("são", "siete/sono"),
    ("não sou", "non sono"),
    ("não é", "non sei/non è"),
    ("não somos", "non siamo"),
    ("não são", "non siete/non sono"),
)

verbs["exemplos ser/estar"] = (
    ("eu estou muito bem", "io sto molto bene"),
    ("Anton tem 46 anos", "Anton ha 46 anni"),
    ("ele tem 46 anos", "lui ha 46 anni"),
    ("ela tem 46 anos", "lei ha 46 anni"),
    ("Nataša é médica", "Nataša è medico"),
    ("eles têm 46 anos", "essi hanno 46 anni"),
    ("vocês são da Argentina", "voi venite dall'Argentina"),
    ("vocês não são de São Paulo", "voi non siete di São Paulo"),
    ("Eva não está muito bem", "Eva non sta molto bene"),
    ("eu não tenho 46 anos", "io non ho 46 anni"),
    ("você não é médica", "tu non sei un medico"),
    ("vocês não têm 46 anos", "voi non avete 46 anni"),
    ("Mark não é da Argentina", "Mark non viene dall'Argentina"),
    ("Ana, Boštjan e Matej são de São Paulo", "Ana, Boštjan e Matej sono di São Paulo"),
    ("qual é o seu nome?", "quale è il tuo nome?"),
    ("qual é o seu sobrenome?", "quale è il tuo cognome? ('come ti cognomi')"),
    ("quantos anos você tem?", "quanti anni hai?"),
    ("quantos anos o senhor tem?", "(formale) quanti anni ha?"),
    ("de onde você é?", "di dove sei/da dove vieni?"),
    ("qual é a sua profissão?", "cosa sei di mestiere/che lavoro fai?"),
    ("quais línguas você fala?", "quali lingue parli?"),
    ("quais línguas vocês falam?", "quali lingue parlate?"),
    ("me dá o número de telefone, por favor?", "mi dai il numero di telefono, per favore?"),
    ("me dá o endereço, por favor?", "mi dai l'indirizzo, per favore?"),
    ("me dá o e-mail, por favor?", "mi dai l'email, per favore?"),
    ("quanto custa a pizza?", "quanto costa la pizza?"),
    ("como se diz ...?", "come si dice ...?"),
    ("o que é ...?", "cosa è ...?"),
)

verbs["ler"] = (
    ("ler", "leggere"),
    ("eu leio", "io leggo", WordType.VERB),
    ("você lê", "tu leggi"),
    ("ele lê", "lui legge"),
    ("ela lê", "lei legge"),
    ("nós lemos", "noi leggiamo"),
    ("vocês leem", "voi leggete"),
    ("eles leem", "essi leggono"),
    ("elas leem", "esse leggono"),
    ("você lê um livro", "tu leggi un libro"),
    ("ele lê um livro", "lui legge un libro"),
)

verbs["chegar"] = (
    ("chegar", "arrivare"),
    ("chego", "arrivo"),
    ("chega", "arrivi/arriva"),
    ("chegamos", "arriviamo"),
    ("chegam", "arrivate/arrivano"),
)

verbs["trabalhar"] = (
    ("trabalhar", "lavorare"),
    ("eu trabalho", "io lavoro"),
    ("você trabalha", "tu lavori"),
    ("ele trabalha", "lui lavora"),
    ("ela trabalha", "lei lavora"),
    ("nós trabalhamos", "noi lavoriamo"),
    ("vocês trabalham", "voi lavorate"),
    ("eles trabalham", "essi lavorano"),
    ("elas trabalham", "esse lavorano"),
)

verbs["causar"] = (
    ("causar", ("causare", "provocare")),
    ("eu causo", "io causo"),
    ("você causa", "causi"),
    ("ele causa", "causa"),
    ("nós causamos", "causiamo"),
    ("vocês causam", "causate"),
    ("eles causam", "causano"),
)

verbs["ver"] = (
    ("ver", ("vedere", "guardare")),
    ("vejo", "vedo"),
    ("vê", "vedi/vede"),
    ("vemos", "vediamo"),
    ("veem", "vedete/vedono"),
    ("não vejo", "non vedo"),
    ("não vê", "non vedi/non vede"),
    ("não vemos", "non vediamo"),
    ("não veem", "non vedete/non vedono"),
    ("eu vejo?", "vedo?"),
    ("você vê?", "vedi?"),
    ("ele vê?", "vede?"),
    ("nós vemos?", "vediamo?"),
    ("vocês veem?", "vedete?"),
    ("eles veem?", "vedono?"),
)

verbs["querer"] = (
    ("quero", "voglio"),
    ("quer", "vuoi/vuole"),
    ("queremos", "vogliamo"),
    ("querem", "volete/vogliono"),
    ("não quero", "non voglio"),
    ("não quer", "non vuoi/non vuole"),
    ("não queremos", "non vogliamo"),
    ("não querem", "non volete/non vogliono"),
)

verbs["ter"] = (
    ("ter", "avere"),
    ("eu tenho", "io ho"),
    ("você tem", "tu hai"),
    ("ele tem", "lui ha"),
    ("ela tem", "lei ha"),
    ("nós temos", "noi abbiamo"),
    ("vocês têm", "voi avete"),
    ("eles têm", "essi hanno"),
    ("elas têm", "esse hanno"),
    ("tenho", "ho"),
    ("tem", "hai/ha"),
    ("temos", "abbiamo"),
    ("têm", "avete/hanno"),
    ("não tenho", "non ho"),
    ("não tem", "non hai/non ha"),
    ("não temos", "non abbiamo"),
    ("não têm", "non avete/non hanno"),
    ("eu tenho?", "ho?"),
    ("você tem?", "hai?"),
    ("ele tem?", "ha?"),
    ("nós temos?", "abbiamo?"),
    ("vocês têm?", "avete?"),
    ("eles têm?", "hanno?"),
)

verbs["ir"] = (
    ("ir", "andare"),
    ("vou", "vado"),
    ("vai", "vai/va"),
    ("vamos", "andiamo"),
    ("vão", "andate/vanno"),
    ("não vou", "non vado"),
    ("não vai", "non vai/non va"),
    ("não vamos", "non andiamo"),
    ("não vão", "non andate/non vanno"),
    ("eu vou?", "vado?"),
    ("você vai?", "vai?"),
    ("ele vai?", "va?"),
    ("nós vamos?", "andiamo?"),
    ("vocês vão?", "andate?"),
    ("eles vão?", "vanno?"),
)

verbs["beber"] = (
    ("beber", "bere"),
    ("eu bebo", "io bevo", WordType.VERB),
    ("você bebe", "tu bevi", WordType.VERB),
    ("ele bebe", "egli/lei beve", WordType.VERB),
    ("ela bebe", "lei beve", WordType.VERB),
    ("nós bebemos", "noi beviamo", WordType.VERB),
    ("vocês bebem", "voi bevete", WordType.VERB),
    ("eles bebem", "essi bevono", WordType.VERB),
    ("elas bebem", "esse bevono", WordType.VERB),
    ("eu não bebo", "io non bevo", WordType.VERB),
    ("você não bebe", "tu non bevi", WordType.VERB),
    ("ele não bebe", "egli/lei non beve", WordType.VERB),
    ("nós não bebemos", "noi non beviamo", WordType.VERB),
    ("vocês não bebem", "voi non bevete", WordType.VERB),
    ("eles não bebem", "essi/esse non bevono", WordType.VERB),
)

verbs["escrever"] = (
    ("escrever", "scrivere"),
    ("eu escrevo", "io scrivo"),
    ("você escreve", "tu scrivi"),
    ("ele escreve", "lui scrive"),
    ("ela escreve", "lei scrive"),
    ("nós escrevemos", "noi scriviamo"),
    ("vocês escrevem", "voi scrivete"),
    ("eles escrevem", "essi scrivono"),
    ("elas escrevem", "esse scrivono"),
)

verbs["falar"] = (
    ("eu falo", "io parlo", WordType.VERB),
    ("você fala", "tu parli", WordType.VERB),
    ("ele fala", "lui parla", WordType.VERB),
    ("ela fala", "lei parla", WordType.VERB),
    ("nós falamos", "noi parliamo", WordType.VERB),
    ("vocês falam", "voi parlate", WordType.VERB),
    ("eles falam", "essi parlano", WordType.VERB),
    ("elas falam", "esse parlano", WordType.VERB),
    ("eu não falo alemão", "io non parlo tedesco", WordType.VERB),
    ("ela fala inglês", "lei parla inglese"),
    ("eu falo um pouco de português", "io parlo un po' di portoghese"),
    ("você fala espanhol?", "parli spagnolo?"),
    ("nós falamos alemão", "noi parliamo il tedesco"),
    ("Sara fala francês", "Sara parla francese"),
    ("eles falam árabe", "essi parlano arabo"),
    ("você não fala alemão", "tu non parli tedesco"),
    ("ele não fala alemão", "lui non parla tedesco"),
    ("nós não falamos alemão", "noi non parliamo tedesco"),
    ("vocês não falam alemão", "voi non parlate tedesco"),
    ("eles não falam alemão", "loro non parlano tedesco"),
)

def run_me():
    # Ho aggiornato le variabili interne al portoghese (pt) come fatto in utilities.py
    dict_pt, dict_ita = process_dictionary(verbs)

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