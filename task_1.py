time_values = '1h 45m,360s,25m,30m 120s,2h 60s'
values = time_values.split(',')

total_minutes = 0

for val in values:
    val = val.strip().replace(' ', '')
    minutes = 0
    number = ''
    for char in val:
        if char.isdigit():
            number += char
        else:
            if char == 'h':
                total_minutes += int(number) * 60
            elif char == 'm':
                total_minutes += int(number)
            elif char == 's':
                total_minutes += int(number) // 60
            number = ''

print("Общее количество минут:", total_minutes)
