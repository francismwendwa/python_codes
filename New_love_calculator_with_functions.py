def calculate_love_score(name_1, name_2):
    combined_name = name_1 + name_2
    new_combined_name = combined_name.lower()

    t = new_combined_name.count("t")
    r = new_combined_name.count("r")
    u = new_combined_name.count("u")
    e = new_combined_name.count("e")

    true = (t + r + u + e)

    l = new_combined_name.count("l")
    o = new_combined_name.count("o")
    v = new_combined_name.count("v")
    e = new_combined_name.count("e")

    love = (l + o + v + e)

    cal_name = int(str(true) + str(love))
    print(cal_name)


calculate_love_score("francis", "mildred nafula")