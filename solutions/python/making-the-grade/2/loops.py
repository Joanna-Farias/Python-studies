"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores: list[float]) -> list[int]:
    """Round all provided student scores.

    Parameters:
        student_scores: Student exam scores.

    Returns:
        list: Student scores *rounded* to the nearest integer value.
    """
    return [round(score) for score in student_scores]

def count_failed_students(student_scores: list[int]) -> int:
    """Count the number of failing students out of the group provided.

    Parameters:
        student_scores: Student scores as ints.

    Returns:
        The count of student scores at or below 40.
    """

    return len([score for score in student_scores if score <= 40])

def above_threshold(student_scores: list[int], threshold: int) -> list[int]:
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    Parameters:
        student_scores: Integer scores.
        threshold: The threshold to cross to be the "best" score.

    Returns:
        list: Integer scores that are at or above the "best" threshold.
    """

    return [score for score in student_scores if score >= threshold]


def letter_grades(highest: int) -> list[int]:
    """Create a list of grade thresholds based on the provided highest grade.

    Parameters:
        highest: The value of the highest exam score.

    Returns:
        list: Lower threshold scores for each D-A letter grade interval.

        For example, where the highest score is 100, and failing is <= 40,
        The result would be [41, 56, 71, 86]:
            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    passo = (highest - 40) // 4
    return list(range(41, highest, passo))


def student_ranking(student_scores: list[int], student_names: list[str]) -> list[str]:
    """Organize the student's rank, name, and grade information in descending order.

    Parameters:
        student_scores: Scores in descending order.
        student_names: Student names by exam score in descending order.

    Returns:
        Strings in format ["<rank>. <student name>: <score>"].
    """
    return [f"{rank}. {nome}: {nota}" for rank, (nome, nota) in enumerate(zip(student_names, student_scores), start=1)]


def perfect_score(student_info: list[list]) -> list:
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    Parameters:
        student_info: List of [<student name>, <score>] lists.

    Returns:
        First `[<student name>, 100]` found OR `[]` if no student score of 100 is found.
    """
    for student in student_info:
        if student[1] == 100:
            return student
    return []