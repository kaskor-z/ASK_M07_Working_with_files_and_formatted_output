#
#           Использование %:
#
# Переменные: количество участников первой команды (team1_num).
team1_num = 5; team2_num = 6
print('В команде "Мастера кода" участников: %d ! ' % team1_num)
# Пример итоговой строки: "В команде Мастера кода участников: 5 ! "
#
# Переменные: количество участников в обеих командах (team1_num, team2_num).
team_num = {'team1_num': 5, 'team2_num': 6}
print('Итого сегодня в командах участников: %(team1_num)s и %(team2_num)s !' % team_num)
# Пример итоговой строки: "Итого сегодня в командах участников: 5 и 6 !"
#
#           Использование format():
#
# Переменные: количество задач решённых командой 42 (score_2).
score_2 = 42
print('Команда Волшебники данных решила задач: {} !'.format(score_2))
# Пример итоговой строки: "Команда Волшебники данных решила задач: 42 !"
#
# Переменные: время за которое команда 2 решила задачи (team1_time).
team1_time = 18015.2
print('Волшебники данных решили задачи за {} с !'.format(team1_time))
# Пример итоговой строки: " Волшебники данных решили задачи за 18015.2 с !"
#
#           Использование f-строк:
#
# Переменные: количество решённых задач по командам: score_1, score_2
score_1 = 40
score_2 = 42
print(f'Команды решили {score_1} и {score_2} задач.')
# Пример итоговой строки: "Команды решили 40 и 42 задач.”
#
# Переменные: исход соревнования (challenge_result).
challenge_result = 'победа команды Мастера кода!'
print(f'Результат битвы: {challenge_result}')
# Пример итоговой строки: "Результат битвы: победа команды Мастера кода!"
#
# Переменные: количество задач (tasks_total) и среднее время решения (time_avg).
tasks_total = 82
time_avg = 350.4
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.')
# Пример итоговой строки: "Сегодня было решено 82 задач, в среднем по 350.4 секунды на задачу!."
#
# Переменные challenge_result, tasks_total, time_avg можно задать вручную или рассчитать.
# Например, для challenge_result:

team1_time = 1552.512; team2_time = 2153.31451

def challenge_result(score_1, score_2, team1_time, team2_time):
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        result = 'Победа команды Мастера кода!'
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        result = 'Победа команды Волшебники данных!'
    else:
        result = 'Ничья!'
    return result

print(f'\n\t\tВходных данных:\n\nteam1_num = {team1_num} team2_num = {team2_num}\n'
      f'score1 = {score_1}\nscore2 = {score_2}\n'
      f'team1_time = {team1_time} team2_time = {team2_time} tasks_total = {score_1 + score_2}\n'
      f'time_avg = {round(((team1_time + team2_time) / (score_1 + score_2)), 1)}\n'
      f'challenge_result = "{challenge_result(score_1, score_2, team1_time, team2_time)}"')
