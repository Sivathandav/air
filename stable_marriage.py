def stable_marriage(n, men_preferences, women_preferences):
    matches = [-1] * n
    women_engaged = [-1] * n
    men_proposals = [0] * n

    while -1 in matches:
        free_man = matches.index(-1)
        preferences = men_preferences[free_man]

        for woman in preferences[men_proposals[free_man]:]:
            men_proposals[free_man] += 1

            if women_engaged[woman] == -1:
                women_engaged[woman] = free_man
                matches[free_man] = woman
                break

            current_partner = women_engaged[woman]
            woman_preferences = women_preferences[woman]

            if woman_preferences.index(current_partner) > woman_preferences.index(free_man):
                women_engaged[woman] = free_man
                matches[free_man] = woman
                matches[current_partner] = -1
                break

    return matches


# Demonstration of solving the Stable Marriage problem
if __name__ == "__main__":
    n = int(input("Enter the number of men/women: "))

    men_preferences = []
    women_preferences = []

    print("Enter the preferences for men:")
    for _ in range(n):
        preferences = list(map(int, input().split()))
        men_preferences.append(preferences)

    print("Enter the preferences for women:")
    for _ in range(n):
        preferences = list(map(int, input().split()))
        women_preferences.append(preferences)

    matches = stable_marriage(n, men_preferences, women_preferences)

    print("Matches:")
    for man, woman in enumerate(matches):
        print(f"Man {man} matches Woman {woman}")
