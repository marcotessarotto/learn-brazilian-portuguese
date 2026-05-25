"""
Portuguese-Italian Language Learning Utilities

This module provides a comprehensive framework for creating and managing
Brazilian Portuguese-Italian vocabulary learning applications with quiz functionality.

The module supports:
- Vocabulary item management with metadata (difficulty, word types, etc.)
- Dictionary processing from structured data
- Interactive quiz generation with multiple choice answers
- Support for complex language features (gender, pronunciation, etc.)
"""

from __future__ import annotations
from enum import Enum
from typing import Optional, List, Dict, Tuple, Union
from dataclasses import dataclass, field
import random


# =============================================================================
# ENUMERATIONS AND METADATA CLASSES
# =============================================================================

class WordType(Enum):
    NOP = 0
    VERB = 1
    SENTENCE = 2
    ADVERB = 3
    PRONOUN = 4
    CONJUNCTION = 5
    NUMBER = 6
    NOUN = 7
    ADJECTIVE = 8

class SentenceCategory(Enum):
    NOP = 0,
    INTERROGATIVE = 1,
    SENTENCE = 2,

class Level(Enum):
    NOP = 0
    EASY = 1
    MEDIUM = 2
    DIFFICULT = 3

class Gender(Enum):
    NEUTRAL = 0
    MALE = 1
    FEMALE = 2


# =============================================================================
# METADATA AND REFERENCE CLASSES
# =============================================================================

@dataclass
class QuestionGroup:
    id: str

@dataclass
class WordNote:
    text: str

@dataclass
class PronNote:
    text: str

@dataclass
class ImageUrl:
    url: str

@dataclass
class BookPage:
    page: int

@dataclass
class WebLink:
    url: str
    def __str__(self) -> str:
        return f"url={self.url}"

@dataclass
class AudioLink:
    url: str
    def __str__(self) -> str:
        return f"url={self.url}"


# =============================================================================
# CORE VOCABULARY ITEM CLASS
# =============================================================================

@dataclass
class Item:
    _next_id = 1
    _all_instances = []
    _all_question_groups = {}

    id: int = field(init=False)

    portoghese: Optional[str] = None
    italiano: Optional[str] = None

    category: Optional[str] = None
    bookpage: Optional[int] = None

    wordtype: Optional[WordType] = None
    sentence_category: Optional[SentenceCategory] = None
    level: Optional[Level] = None
    gender: Optional[Gender] = None

    weblink: Optional[WebLink] = None

    pt_multiple_words: bool = field(init=False, default=False)
    ita_multiple_words: bool = field(init=False, default=False)
    is_question: bool = field(init=False, default=False)
    portoghese_num_words: int = field(init=False, default=0)
    italiano_num_words: int = field(init=False, default=0)
    ends_with_r: bool = field(init=False, default=False)

    question_groups: Optional[list] = field(init=True, default_factory=list)

    def __post_init__(self):
        self.id = Item._next_id
        Item._next_id += 1

        if self.portoghese:
            self.portoghese = self.portoghese.lower()
            self.portoghese_num_words = len(self.portoghese.split())
            self.pt_multiple_words = self.portoghese_num_words > 1
            self.is_question = self.portoghese.endswith("?")
            self.ends_with_r = True if self.portoghese.endswith("r") else False

        if self.italiano:
            self.italiano = self.italiano.lower()
            self.italiano_num_words = len(self.italiano.split())
            self.ita_multiple_words = self.italiano_num_words > 1

        if self.is_question and self.sentence_category is None:
            self.sentence_category = SentenceCategory.INTERROGATIVE

        Item._all_instances.append(self)

        for gp in self.question_groups:
            if gp.id not in Item._all_question_groups:
                Item._all_question_groups[gp.id] = []
            Item._all_question_groups[gp.id].append(self)

    @classmethod
    def get_all_questions(cls) -> List['Item']:
        return [item for item in cls._all_instances if item.is_question]

    @classmethod
    def from_row(cls, row: Tuple, category: str) -> 'Item':
        kwargs = {'category': category, 'question_groups': []}

        for count, val in enumerate(row):
            if count == 0:
                kwargs['portoghese'] = val
            elif count == 1:
                kwargs['italiano'] = val
            elif isinstance(val, BookPage):
                kwargs['bookpage'] = val.page
            elif isinstance(val, WordType):
                kwargs['wordtype'] = val
            elif isinstance(val, SentenceCategory):
                kwargs['sentence_category'] = val
            elif isinstance(val, Level):
                kwargs['level'] = val
            elif isinstance(val, Gender):
                kwargs['gender'] = val
            elif isinstance(val, WebLink):
                kwargs['weblink'] = val
            elif isinstance(val, QuestionGroup):
                kwargs['question_groups'].append(val)

        return cls(**kwargs)

    def __str__(self) -> str:
        result = f"portoghese='{self.portoghese}' italiano='{self.italiano}'"
        optional_attrs = ['bookpage', 'wordtype', 'sentence_category', 'level', 'gender', 'weblink']
        for attr in optional_attrs:
            value = getattr(self, attr, None)
            if value is not None:
                result += f" {attr}={value}"
        return result


# =============================================================================
# DICTIONARY PROCESSING FUNCTIONS
# =============================================================================

def process_dictionary(
        my_dict: Dict[str, List[Tuple]],
        dict_pt: Optional[Dict[str, List[Item]]] = None,
        dict_ita: Optional[Dict[str, List[Item]]] = None
) -> Tuple[Dict[str, List[Item]], Dict[str, List[Item]]]:

    if dict_pt is None:
        dict_pt = {}
    if dict_ita is None:
        dict_ita = {}

    def append_to_dict(d: Dict[str, List[Item]], key: str, item: Item) -> None:
        if key not in d:
            d[key] = [item]
        else:
            d[key].append(item)

    def process_row_variants(row: Tuple, category: str) -> List[Item]:
        items = []
        if (isinstance(row[0], (tuple, list)) and isinstance(row[1], (tuple, list))):
            raise ValueError(f"Both portoghese and italiano cannot be collections in row: {row}")

        if isinstance(row[0], (tuple, list)):
            for pt_variant in row[0]:
                if pt_variant:
                    new_row = list(row)
                    new_row[0] = pt_variant
                    items.append(Item.from_row(tuple(new_row), category))

        elif isinstance(row[1], (tuple, list)):
            for ita_variant in row[1]:
                if ita_variant:
                    new_row = list(row)
                    new_row[1] = ita_variant
                    items.append(Item.from_row(tuple(new_row), category))
        else:
            if row[0]:
                items.append(Item.from_row(row, category))

        return items

    for category, rows in my_dict.items():
        print(f"Processing category: {category}")
        for row in rows:
            try:
                items = process_row_variants(row, category)
                for item in items:
                    append_to_dict(dict_pt, item.portoghese, item)
                    append_to_dict(dict_ita, item.italiano, item)
            except Exception as e:
                print(f"Error processing row {row} in category {category}: {e}")
                continue

    return dict_pt, dict_ita


# =============================================================================
# QUIZ GENERATION FUNCTIONS
# =============================================================================

def find_random_answers(
        dict_lang: Dict[str, List[Item]],
        current_question: str,
        current_answer: Item,
        number_of_answers: int = 5,
        pt2ita: bool = True,
        max_attempts: int = 1000
) -> List[Item]:
    answers = [current_answer]
    available_keys = [key for key in dict_lang.keys() if key != current_question]
    attempts = 0

    while len(answers) < number_of_answers and attempts < max_attempts:
        attempts += 1
        random_answer = None

        try:
            if current_answer.question_groups and attempts*2 < max_attempts:
                qg = random.choice(current_answer.question_groups)
                question_group = qg.id
                random_answer = random.choice(Item._all_question_groups[question_group])
                if random_answer.id == current_answer.id:
                    continue
            else:
                random_key = random.choice(available_keys)
                random_answer = random.choice(dict_lang[random_key])

                if current_answer.is_question:
                    if not random_answer.is_question and attempts < max_attempts/5:
                        continue

                if current_answer.ends_with_r:
                    if not random_answer.ends_with_r and attempts < max_attempts/3:
                        continue

                if not current_answer.is_question:
                    if random_answer.is_question and attempts < max_attempts/5:
                        continue

                if not current_answer.is_question:
                    if not pt2ita:
                        if random_answer.pt_multiple_words != current_answer.pt_multiple_words and attempts < max_attempts/5:
                            continue
                    else:
                        if random_answer.ita_multiple_words != current_answer.ita_multiple_words and attempts < max_attempts/5:
                            continue

            if random_answer in answers:
                continue

            if pt2ita:
                if any(item.italiano == random_answer.italiano for item in answers):
                    continue
            else:
                if any(item.portoghese == random_answer.portoghese for item in answers):
                    continue

            answers.append(random_answer)
        except (IndexError, ValueError):
            continue

    if len(answers) < number_of_answers:
        print(f"Warning: Could only find {len(answers)} answers out of "
              f"{number_of_answers} requested for question '{current_question}'")
    return answers


# =============================================================================
# QUIZ INTERFACE CLASS
# =============================================================================

class LanguageQuiz:
    def __init__(self, dict_lang: Dict[str, List[Item]], seed: int = 0):
        self.dict_lang = dict_lang
        self.seed = seed
        self.reset_stats()
        if seed != 0:
            random.seed(seed)
        else:
            random.seed()

    def reset_stats(self) -> None:
        self.wrong_answers = []
        self.number_of_questions = 0
        self.correct_answers = 0

    def prepare_questions(
            self,
            pt2ita: bool = True,
            max_questions: int = 0,
            number_of_answers: int = 5
    ) -> List[Tuple[str, Item, List[Item]]]:
        if max_questions == 0:
            max_questions = len(self.dict_lang)

        dict_keys = list(self.dict_lang.keys())
        questions_and_answers = []

        while dict_keys and len(questions_and_answers) < max_questions:
            current_question = random.choice(dict_keys)
            dict_keys.remove(current_question)
            correct_answer = random.choice(self.dict_lang[current_question])
            possible_answers = find_random_answers(
                self.dict_lang, current_question, correct_answer, number_of_answers, pt2ita
            )
            random.shuffle(possible_answers)
            questions_and_answers.append((current_question, correct_answer, possible_answers))

        return questions_and_answers

    def run_quiz(
            self,
            pt2ita: bool = True,
            max_questions: int = 0,
            number_of_answers: int = 5
    ) -> Dict[str, Union[int, float]]:
        questions_and_answers = self.prepare_questions(pt2ita, max_questions, number_of_answers)
        self.reset_stats()

        for current_pos, (current_question, correct_answer, possible_answers) in enumerate(questions_and_answers, 1):
            print(f"\nQuiz #{current_pos} / {len(questions_and_answers)}")
            if pt2ita:
                print(f"Cosa significa '{current_question}' ?")
            else:
                print(f"Come traduci '{current_question}' ?")

            for counter, answer in enumerate(possible_answers):
                display_text = answer.italiano if pt2ita else answer.portoghese
                print(f"{chr(ord('a') + counter)}: {display_text}")

            user_answer = self._get_user_input(possible_answers)
            if user_answer is None:
                break

            self.number_of_questions += 1
            if correct_answer == user_answer:
                print("✓ Corretto!")
                self.correct_answers += 1
                print(f"Risposta: {correct_answer}")
            else:
                print("✗ Sbagliato")
                print(f"Risposta corretta: {correct_answer}")
                self.wrong_answers.append(correct_answer)

        return self._display_results()

    def _get_user_input(self, possible_answers: List[Item]) -> Optional[Item]:
        while True:
            try:
                data = input("Risposta (q per uscire): ").strip().lower()
                if not data:
                    continue
                if data == "q":
                    return None
                if len(data) == 1 and 'a' <= data <= chr(ord('a') + len(possible_answers) - 1):
                    answer_pos = ord(data) - ord('a')
                    return possible_answers[answer_pos]
                else:
                    print("Input non valido. Per favore scegli un input valido (a, b, c, etc.).")
            except (EOFError, KeyboardInterrupt):
                print("\nQuiz interrotto dall'utente.")
                return None

    def _display_results(self) -> Dict[str, Union[int, float]]:
        print("\n" + "=" * 50)
        print("QUIZ COMPLETATO!")
        print("=" * 50)

        if self.number_of_questions > 0:
            ratio = (self.correct_answers / self.number_of_questions) * 100
            print(f"Numero di quiz: {self.number_of_questions}")
            print(f"Risposte corrette: {self.correct_answers}")
            print(f"Punteggio: {ratio:.1f}%")
            if self.wrong_answers:
                print(f"\nRisposte sbagliate ({len(self.wrong_answers)}):")
                for answer in self.wrong_answers:
                    print(f"  • {answer}")
        else:
            ratio = 0
            print("Nessuna risposta è stata data.")

        return {
            "total_questions": self.number_of_questions,
            "correct_answers": self.correct_answers,
            "score_percentage": ratio
        }


# =============================================================================
# LEGACY COMPATIBILITY FUNCTIONS
# =============================================================================

def start_tests(
        dict_lang: Dict[str, List[Item]],
        int_seed: int = 0,
        pt2ita: bool = True,
        max_questions: int = 0,
        number_of_answers: int = 5
) -> Dict[str, Union[int, float]]:
    quiz = LanguageQuiz(dict_lang, int_seed)
    return quiz.run_quiz(pt2ita, max_questions, number_of_answers)

def prepare_list_of_questions_and_answers(
        dict_lang: Dict[str, List[Item]],
        pt2ita: bool = True,
        max_questions: int = 0,
        number_of_answers: int = 5
) -> List[Tuple[str, Item, List[Item]]]:
    quiz = LanguageQuiz(dict_lang, 0)
    return quiz.prepare_questions(pt2ita, max_questions, number_of_answers)

def generic_run_me(enota_dict):
    dict_pt, dict_ita = process_dictionary(enota_dict)

    if Item._all_question_groups:
        print(f"\nGruppi di domande (numero totale quiz: {len(Item._all_instances)}):")
        for k,v in Item._all_question_groups.items():
            print(f"'{k}': {len(v)} quiz")

    print(f"\npt items: {len(dict_pt)}")
    print(f"ita items: {len(dict_ita)}\n")

    print("1 - test da portoghese a italiano")
    print("2 - test da italiano a portoghese")
    data = input("risposta (q per uscire, s per statistiche): ")
    if data is None or data == "q":
        return
    elif data == "1":
        start_tests(dict_pt)
    elif data == "2":
        start_tests(dict_ita, pt2ita=False)
    elif data == "s":
        print(f"numero di istanze di Item: {len(Item._all_instances)}")
        questions = Item.get_all_questions()
        print(f"numero di domande: {len(questions)}")
    else:
        print("risposta non valida")