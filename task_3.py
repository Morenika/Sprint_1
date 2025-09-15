world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}

# 1. Добавляем 2022 год
world_champions[2022] = 'Аргентина'

# 2. Выводим всех чемпионов в формате "год - страна"
for year, country_name in world_champions.items():
    print(f"{year} - {country_name}")

# 3. Проверка на Италию
country = 'Италия'

if country in world_champions.values():
    print(f'{country} становилась чемпионом мира по футболу в 21 веке!')
else:
    print(f'{country} не выигрывала чемпионат мира по футболу в 21 веке.')
