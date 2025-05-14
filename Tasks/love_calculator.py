# def calculate_love_score(name1, name2):
    # true_counter = 0
    # love_counter = 0
    # for char in name1.lower():
    #     if char == "t":
    #         true_counter += 1
    #     if char == "r":
    #         true_counter += 1
    #     if char == "u":
    #         true_counter += 1
    #     if char == "e":
    #         true_counter += 1
    # for char in name2.lower():
    #     if char == "t":
    #         true_counter += 1
    #     if char == "r":
    #         true_counter += 1
    #     if char == "u":
    #         true_counter += 1
    #     if char == "e":
    #         true_counter += 1
    # for char in name1.lower():
    #     if char == "l":
    #         love_counter += 1
    #     if char == "o":
    #         love_counter += 1
    #     if char == "v":
    #         love_counter += 1
    #     if char == "e":
    #         love_counter += 1
    # for char in name2.lower():
    #     if char == "l":
    #         love_counter += 1
    #     if char == "o":
    #         love_counter += 1
    #     if char == "v":
    #         love_counter += 1
    #     if char == "e":
    #         love_counter += 1
    # sum = str(true_counter) + str(love_counter)
    # return print(sum)

def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()
    true_counter = sum(combined_names.count(c) for c in "true")
    love_counter = sum(combined_names.count(c) for c in "love")
    love_score = str(true_counter) + str(love_counter)
    print(love_score)

calculate_love_score("Kanye West", "Kim Kardashian")