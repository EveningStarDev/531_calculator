
# Plates available for use
plates = [20.0, 10.0, 5.0, 2.5, 2.0, 1.5, 1.0, 0.5]

# Percentages and reps for each week of the program (weeks 1, 2, 3 and 4)
percntg_data = {
    1: {
        "main": [0.65, 0.75, 0.85, 5, 5, 5, True],
        "assistance": [0.5, 0.6, 0.7, 10, 10, 10, False]
    },
    2: {
        "main": [0.7, 0.8, 0.9, 3, 3, 3, True],
        "assistance": [0.6, 0.7, 0.8, 8, 8, 6, False],
    },
    3: {
        "main": [0.75, 0.85, 0.95, 5, 3, 1, True],
        "assistance": [0.65, 0.75, 0.85, 5, 5, 5, False],
    },
    4: {
        "main": [0.1, 0.4, 0.6, 5, 5, 5, True],
        "assistance": [0.4, 0.5, 0.6, 5, 5, 5, False],
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


def rep_max(weight, reps):
    # Estimates a theoretical 1RM based on reps
    one_rep_max = (weight * reps * 0.0333) + weight

    return one_rep_max


def reps_to_one_rep_max(one_rep_max, current_weight):
    # Estimates the necessary reps to match a theoretical 1RM
    max_reps = (one_rep_max - current_weight) / (current_weight * 0.0333)
    return max_reps


def lift_calculator(training_max, last_weight, last_reps,
                    first_set_perct, second_set_perct,
                    third_set_perct, first_set_reps, second_set_reps,
                    third_set_reps, is_main):
    first_set_calc = int(training_max * first_set_perct)
    second_set_calc = int(training_max * second_set_perct)
    third_set_calc = int(training_max * third_set_perct)

    print(
        f"1 x {first_set_calc} x {first_set_reps} reps",
        f"{plate_calculator(first_set_calc)}")
    print(
        f"1 x {second_set_calc} x {second_set_reps} reps",
        f"{plate_calculator(second_set_calc)}")

    if is_main:
        last_cycle_one_rep_max = rep_max(last_weight, last_reps)

        print(
            f"1 x {third_set_calc} x {third_set_reps} or more reps",
            f"{plate_calculator(third_set_calc)}")
        print(
            f"\nEstimated 1RM for last cycle's 3rd week top set: {last_cycle_one_rep_max:.0f}")
        print(
            f"Estimated 1RM for this week's top set: {rep_max(third_set_calc, third_set_reps):.0f}")
        print(
            f"Estimated reps to match last cycle's 1RM for the 3rd week top set: {reps_to_one_rep_max(last_cycle_one_rep_max, third_set_calc):.2f}")
    else:
        print(
            f"1 x {third_set_calc} x {third_set_reps} reps",
            f"{plate_calculator(third_set_calc)}")


def main():
    # Asks for the week and current training max
    gym_data = input(
        "Input the week, lift TMax: ").split(".")
    week, lift_tmax = int(gym_data[0]), int(gym_data[1])

    past_cycle_data = input(
        "Input your last cycle's third week's weight, reps: ").split(".")
    last_weight, last_reps = int(past_cycle_data[0]), int(past_cycle_data[1])

    if week in [1, 2, 3, 4]:
        # Asks whether there are assistance lifts
        assistance_lift = input(
            "Will you perform an assistance lift? [1 (yes) / 2 (no)]: ")

        if assistance_lift == "1":
            # Asks for assistance lift weight
            assistance_lift_tmax = int(input("Input assistance lift TMax: "))

        # Prints main calcs regardless of assistance lift
        print("\nMain lift:")
        week_lifts = percntg_data[week]
        lift_calculator(lift_tmax, last_weight, last_reps, *week_lifts["main"])

        # If assistance lift is checked, prints respective calcs
        if assistance_lift == "1":
            print("\nAssistance lift:")
            lift_calculator(assistance_lift_tmax, last_weight, last_reps,
                            *week_lifts["assistance"])

    else:
        print("For the week, input 1, 2, 3 or 4.")
        print()
        main()


if __name__ == '__main__':
    main()
