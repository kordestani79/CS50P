def main():

    time_input = input("What time is it? ")

    time_hours = convert(time_input)

    if 7.0 <= time_hours <= 8.0:
        print("breakfast time")
    elif 12.0 <= time_hours <= 13.0:
        print("lunch time")
    elif 18.0 <= time_hours <= 19.0:
        print("dinner time")


def convert(time):
    hours, minutes = map(int, time.split(":"))
    total_hours = hours + minutes / 60
    return total_hours


if __name__ == "__main__":
    main()
