def grocery_budget(grocery_list, budget):    # TC: O(2^n)
    if budget < 0:                           # SC: O(2^n), where n = len(grocery_list)
        return []

    if not grocery_list:
        return [ [] ]

    all_lists = []

    current_name, current_price = grocery_list[0]
    for list_with_current in grocery_budget(grocery_list[1:], budget - current_price):
        list_with_current.append(current_name)
        all_lists.append(list_with_current)

    all_lists += grocery_budget(grocery_list[1:], budget)
    return all_lists