def sequence(start, next, matches, top_sequence):
    if next >= len(matches):
        return
    if matches[next] >= matches[start]:
        top_sequence.append(matches[next])

    else:
        return sequence(start, next + 1, matches, top_sequence)

    return sequence(next, next + 1, matches, top_sequence)


goals = []
for game_goals in input().split(', '):
    goals.append(game_goals)

options = []

for i in range(len(goals)):
    seq = [goals[i]]

    sequence(i, i + 1, goals, seq)

    options.append(seq)

max_streak = len(options[0])
best_streak = 0

for i in range(1, len(options)):
    if len(options[i]) > max_streak:
        max_streak = len(options[i])
        best_streak = i

print(*options[best_streak], sep=' ')
