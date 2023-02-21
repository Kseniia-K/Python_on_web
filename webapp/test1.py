todos = open('todos.txt', 'a')

print('Привет!', file=todos)
print('Как дела?', file=todos)
print('Пока!', file=todos)

todos.close()