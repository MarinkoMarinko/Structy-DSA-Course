def lining_up(people, capacity):    # TC: O(n! / (n - k)!)
    if capacity == 0:               # SC: O(n! / (n - k)!), where n = len(people) and c = capacity
        return [ [] ]

    if len(people) < capacity:
        return []

    all_lines = []

    first_person = people[0]
    for line in lining_up(people[1:], capacity - 1):
        for i in range(0, len(line) + 1):
            line_with_current = [*line[:i], first_person, *line[i:]]
            all_lines.append(line_with_current)

    all_lines += lining_up(people[1:], capacity)
    return all_lines