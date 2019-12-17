"""Script de précorrection pour l'évaluation à mi-semestre du S1 2019.

TOUS LES RENDUS ONT SUBI UNE CORRECTION MANUELLE, CE SCRIPT N'EST QU'UNE AIDE, NE PAS S'EN SERVIR
SEUL POUR ESTIMER UNE NOTE.
"""

import ast
import math
import os
import pathlib
import shutil
import subprocess
import tempfile
import typing as ty

import tqdm

data_source = pathlib.Path("AI08.txt")


def extract_answers(answer_script: os.PathLike):
    with tempfile.TemporaryDirectory() as tempdir:
        temp_answer = shutil.copy(answer_script, tempdir)
        shutil.copy(data_source, tempdir)
        answers_proc: ty.Union[subprocess.TimeoutExpired, subprocess.CompletedProcess]
        try:
            answers_proc = subprocess.run(
                ["python", temp_answer],
                capture_output=True,
                text=True,
                cwd=tempdir,
                timeout=10,
            )
            run_returned = not answers_proc.returncode
        except subprocess.TimeoutExpired as e:
            answers_proc = e
            run_returned = False
    if answers_proc.stdout is None:
        answers = [""]
    else:
        answers = [l.strip() for l in answers_proc.stdout.splitlines()]
    return run_returned, answers, answers_proc


class AnswerValidation(ty.NamedTuple):
    validable: bool
    correct: ty.Optional[float]
    answer: ty.Optional[str]
    canonical: str


def validate_answer1(answer):
    """Quantité d'ammoniac (en t/an) émise en Alsace en 2004"""
    canonical = "180.13"
    if answer is None:
        return AnswerValidation(
            validable=False, correct=0.0, answer=None, canonical=canonical
        )
    if answer.isspace():
        return AnswerValidation(
            validable=True, correct=0.0, answer=None, canonical=canonical
        )
    try:
        val = ast.literal_eval(answer)
        validable = isinstance(val, float)
    except SyntaxError:
        validable = False
    if validable:
        correct = 1.0 if math.isclose(val, 180.13) else 0.0
    else:
        correct = None
    return AnswerValidation(
        validable=validable, correct=correct, answer=answer, canonical=canonical
    )


def validate_answer2(answer):
    """Combien de noms de régions mentionnées dans ce fichier comportent un nombre de
    lettres supérieur ou égal à 10 (espaces et tirets non compris) ?"""
    canonical = "13"
    if answer is None:
        return AnswerValidation(
            validable=False, correct=0.0, answer=None, canonical=canonical
        )
    if answer.isspace():
        return AnswerValidation(
            validable=True, correct=0.0, answer=None, canonical=canonical
        )
    try:
        val = ast.literal_eval(answer)
        validable = isinstance(val, int)
    except SyntaxError:
        validable = False
    if validable:
        correct = 1.0 if val == 13 else 0.0
    else:
        correct = None
    return AnswerValidation(
        validable=validable, correct=correct, answer=answer, canonical=canonical
    )


def validate_answer3(answer):
    """Quelle est la région pour laquelle les émissions de monoxyde de carbone on été
    maximales en 2008 ?"""
    canonical = "LORRAINE"
    if answer is None:
        return AnswerValidation(
            validable=False, correct=0.0, answer=None, canonical=canonical
        )
    return AnswerValidation(
        validable=True,
        correct=1.0 if answer.lower() == canonical.lower() else 0.0,
        answer=answer,
        canonical=canonical,
    )


def validate_answer4(answer):
    """Même question que 3., mais pour le total des émissions de monoxyde de carbone
    sur l'ensemble de la période 1999 — 2009"""
    canonical = "AQUITAINE"
    if answer is None:
        return AnswerValidation(
            validable=False, correct=0.0, answer=None, canonical=canonical
        )
    return AnswerValidation(
        validable=True,
        correct=1.0 if answer.lower() == canonical.lower() else 0.0,
        answer=answer,
        canonical=canonical,
    )


def validate_answer5(answer):
    """Donner le contenu de la précision donnée entre parenthèses la plus longue du
    fichier."""
    canonical = "et ses composants"
    if answer is None:
        return AnswerValidation(
            validable=False, correct=0.0, answer=None, canonical=canonical
        )
    accepted = ("et ses composants", "NOX y compris NO2")
    if answer in accepted:
        correct = 1.0
    elif answer[1:-1] in accepted:
        correct = 0.9
    else:
        correct = 0.0
    return AnswerValidation(
        validable=True, correct=correct, answer=answer, canonical=canonical
    )


def validate_answer6(answer):
    """Donner, sous forme de liste séparée par des barres `|` et triée par ordre
    alphabétique l'ensemble des noms de composés chimiques ou de catégories de
    composés mentionnés dans ce fichier."""
    canonical = "1,2-dichloroéthane|acide cyanhydrique|ammoniac|arsenic|benzène|cadmium|chloroforme|chlorure d'hydrogène|chlorure de vinyle monomère|composés organiques volatils non méthaniques|dichlorométhane|dioxyde de carbone|fluorure d'hydrogène|mercure|monoxyde de carbone|oxyde d'azote|oxydes de soufre|perchloroéthylène|plomb|poussières|protoxyde d'azote|sulfure d'hydrogène|trichloroéthylène"
    if answer is None:
        return AnswerValidation(
            validable=False, correct=0.0, answer=None, canonical=canonical
        )
    if answer.isspace():
        return AnswerValidation(
            validable=True, correct=0.0, answer=None, canonical=canonical
        )
    parsed = answer.split("|")
    validable = len(parsed) > 1 and parsed == sorted(parsed)
    if validable:
        if answer == canonical:
            correct = 1.0
        # Facile à louper et pas important: virer les parenthèses peut laisser des double espaces
        elif answer.replace("  ", " ") == canonical:
            correct = 1.0
        else:
            correct = 0.0
    else:
        correct = None
    return AnswerValidation(
        validable=validable, correct=correct, answer=answer, canonical=canonical
    )


def validate_answer7(answer):
    """Donner, sous forme de liste séparée par des barres `|` et triée par ordre
    alphabétique l'ensemble des noms de régions présents dans ce fichier en
    capitalisant les débuts de mots"""
    canonical = "Alsace|Aquitaine|Auvergne|Basse Normandie|Bourgogne|Bretagne|Centre-Val De Loire|Champagne-Ardenne|Corse|D.O.M.|Franche Comte|Haute Normandie|Ile De France|Languedoc-Roussillon|Limousin|Lorraine|Midi-Pyrenees|Nord-Pas-De-Calais|Pays De La Loire|Picardie|Poitou-Charentes|Provence-Alpes-Cote D Azur|Rhone-Alpes"
    if answer is None:
        return AnswerValidation(
            validable=False, correct=0.0, answer=None, canonical=canonical
        )

    if answer.isspace():
        return AnswerValidation(
            validable=True, correct=0.0, answer=None, canonical=canonical
        )
    parsed = answer.split("|")
    validable = len(parsed) > 1 and parsed == sorted(parsed)
    if validable:
        correct = 1.0 if answer == canonical else 0.0
    else:
        correct = None
    return AnswerValidation(
        validable=validable, correct=correct, answer=answer, canonical=canonical
    )


def validate_answer8(answer):
    """Quelle est le composé dont pour lequel la moyenne annuelle des émissions en
    région Basse Normandie a été la plus élevée sur la période 1999–2009 ?"""
    canonical = "Dioxyde de carbone (CO2)"
    if answer is None:
        return AnswerValidation(
            validable=False, correct=0.0, answer=None, canonical=canonical
        )
    return AnswerValidation(
        validable=True,
        correct=1.0 if answer == canonical else 0.0,
        answer=answer,
        canonical=canonical,
    )


def autocorrect(
    answers: ty.Sequence[ty.Optional[str]]
) -> ty.Generator[AnswerValidation, None, None]:
    yield validate_answer1(answers[0])
    yield validate_answer2(answers[1])
    yield validate_answer3(answers[2])
    yield validate_answer4(answers[3])
    yield validate_answer5(answers[4])
    yield validate_answer6(answers[5])
    yield validate_answer7(answers[6])
    yield validate_answer8(answers[7])


results_file = pathlib.Path("results.tsv")
answers_dir = pathlib.Path("answers")
debugged_answers_dir = pathlib.Path("answers_dbug")
outputs_dir = pathlib.Path("outputs")
outputs_dir.mkdir(exist_ok=True)

with open(results_file, "w") as out_stream:
    # Header
    out_stream.write("name\treturned\tfull\t")
    out_stream.write("\t".join(f"q{i}\t" for i in range(1, 9)))
    out_stream.write("\n")
    pbar = tqdm.tqdm(list(answers_dir.glob("*.py")), unit="file")
    for answer_script in pbar:
        pbar.set_description(f"validating {answer_script.name}")
        full = True
        run_returned, answers, proc = extract_answers(answer_script)
        if not run_returned:
            _, answers, proc = extract_answers(
                debugged_answers_dir / answer_script.name
            )
            answers = [None if a == "DEBUGGED" else a for a in answers]
        if len(answers) < 8:
            answers = [*answers, *("" for _ in range(8 - len(answers)))]
            full = False
        elif len(answers) > 8:
            answers = answers[:8]
            full = False
        out_stream.write(f"{answer_script.stem}\t{int(run_returned)}\t{int(full)}\t")
        for validation in autocorrect(answers):
            out_stream.write(f"{int(validation.validable)}\t{validation.correct}\t")
        out_stream.write("\n")
        with open(
            outputs_dir / f"{answer_script.stem}.txt", "w"
        ) as script_output_stream:
            script_output_stream.write("========== stderr ===========\n")
            script_output_stream.write(proc.stderr if proc.stderr is not None else "")
            script_output_stream.write("\n========= stdout ===========\n")
            script_output_stream.write(proc.stdout if proc.stdout is not None else "")
