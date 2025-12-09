def merge_guest_lists(*lists):
    result = []
    for lst in lists:
        for el in lst:
            result.append(el)
    return sorted(set(result))


Instagram = merge_guest_lists(["maria", "petro"], ["semen","semen"])
Facebook = merge_guest_lists(["Ahmed", "sasha"], ["krystyna", "kek"])
Onlyfriends = merge_guest_lists(["Yevhenii", "kotak"], ["Arina", "Maria"])
print(Instagram, Facebook, Onlyfriends)