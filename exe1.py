logs = [("10:00", 200), ("10:01", 404), ("10:02", 200), ("10:03", 500), ("10:04", 404)]

frequencia = {}

for hora, codigo in logs:
    # 3. Verificação e contagem
    if codigo in frequencia:
        frequencia[codigo] += 1
    else:
        frequencia[codigo] = 1

print(frequencia)