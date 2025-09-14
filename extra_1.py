types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}


def remove_duplicates(ticket_dict):
    seen = set()
    result = {}

    for priority in sorted(ticket_dict):
        unique_tickets = []
        for ticket in ticket_dict[priority]:
            if ticket not in seen:
                unique_tickets.append(ticket)
                seen.add(ticket)
        result[priority] = unique_tickets

    return result


def group_tickets_by_type(types_dict, tickets_dict):
    unique_tickets = remove_duplicates(tickets_dict)
    result = {}

    for priority, name in types_dict.items():
        result[name] = unique_tickets.get(priority, [])

    return result


tickets_by_type = group_tickets_by_type(types, tickets)

print(tickets_by_type)
