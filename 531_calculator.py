
# Plates available for use
plates = [20.0, 10.0, 5.0, 2.5, 2.0, 1.5, 1.0, 0.5]

# Percentages and reps for each week of the program (weeks 1, 2, 3 and 4)
percntg_data = {
    1: {
        "main": [0.65, 0.75, 0.85, 5, 5, 5],
        "assistance": [0.5, 0.6, 0.7, 10, 10, 10]
    },
    2: {
        "main": [0.7, 0.8, 0.9, 3, 3, 3],
        "assistance": [0.6, 0.7, 0.8, 8, 8, 6],
    },
    3: {
        "main": [0.75, 0.85, 0.95, 5, 3, 1],
        "assistance": [0.65, 0.75, 0.85, 5, 5, 5],
    },
    4: {
        "main": [0.1, 0.4, 0.6, 5, 5, 5],
        "assistance": [0.4, 0.5, 0.6, 5, 5, 5],
    }
}


def plate_calculator(weight):
    # Determines weight on each side of the barbell
    weight -= 17
    side_weight = weight / 2
    # Initializes empty list
    plate_distribution = []

    # Keeps adding weight until below the threshold for the lightest plate.
    for plate in plates:
        while side_weight >= plate:
            side_weight -= plate
            plate_distribution.append(plate)

    return plate_distribution


def lift_calculator(training_max, first_set_perct, second_set_perct,
                    third_set_perct, first_set_reps, second_set_reps,
                    third_set_reps):
    first_set_calc = int(training_max * first_set_perct)
    second_set_calc = int(training_max * second_set_perct)
    third_set_calc = int(training_max * third_set_perct)

    print(
        f"1 x {first_set_calc} x {first_set_reps} reps",
        f"{plate_calculator(first_set_calc)}")
    print(
        f"1 x {second_set_calc} x {second_set_reps} reps",
        f"{plate_calculator(second_set_calc)}")
    print(
        f"1 x {third_set_calc} x {third_set_reps} or more reps",
        f"{plate_calculator(third_set_calc)}")


def main():
    gym_data = input(
        "Input the week, lift TMax: ").split(".")
    week, lift_tmax = int(gym_data[0]), int(gym_data[1])

    if week in [1, 2, 3, 4]:
        assistance_lift = input(
            "Will you perform an assistance lift? [1 (yes) / 2 (no)]: ")

        if assistance_lift == "1":
            assistance_lift_tmax = int(input("Input assistance lift TMax: "))

        # Prints main calcs regardless of assistance lift
        print("\nMain lift:")
        week_lifts = percntg_data[week]
        lift_calculator(lift_tmax, *week_lifts["main"])

        # If assistance lift is checked, prints calcs
        if assistance_lift == "1":
            print("\nAssistance lift:")
            lift_calculator(assistance_lift_tmax, *week_lifts["assistance"])

    else:
        print("For the week, input 1, 2, 3 or 4.")
        print()
        main()


if __name__ == '__main__':
    main()
