LEVELS = [
    (0, "Level 1 - Intern"),
    (100, "Level 2 - Analyst"),
    (250, "Level 3 - Security Engineer"),
    (450, "Level 4 - Pen Tester"),
    (700, "Level 5 - SOC Lead"),
]


def get_level_name(xp):
    current_level = LEVELS[0][1]

    for needed_xp, level_name in LEVELS:
        if xp >= needed_xp:
            current_level = level_name

    return current_level


def get_level_number(xp):
    level_number = 1

    for index, level in enumerate(LEVELS):
        needed_xp = level[0]
        if xp >= needed_xp:
            level_number = index + 1

    return level_number


def add_reward(student, mission):
    if mission.title not in student.completed_missions:
        student.xp = student.xp + mission.xp_reward
        student.level = get_level_number(student.xp)
        student.completed_missions.append(mission.title)

        if mission.badge not in student.badges:
            student.badges.append(mission.badge)


def record_answer(student, was_correct):
    student.total_answers = student.total_answers + 1

    if was_correct:
        student.correct_answers = student.correct_answers + 1


def get_success_rate(student):
    if student.total_answers == 0:
        return 0

    return int((student.correct_answers / student.total_answers) * 100)
