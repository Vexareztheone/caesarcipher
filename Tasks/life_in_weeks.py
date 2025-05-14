def life_in_weeks(age):
    LIFE_EXPECTANCY_WEEKS = 4680
    weeks_left = LIFE_EXPECTANCY_WEEKS - (age * 52)
    return print(f"You have {weeks_left} weeks left.")

life_in_weeks(12)