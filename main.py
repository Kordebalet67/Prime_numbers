import prime_numbers as pn


def main():
    try:
        user_input = int(input("Input the end of number row(it must be a NATURAL number): "))
        x, y = pn.natural_generation(user_input)
        x_prime, y_prime = pn.is_prime(x, y)
        x_simple, y_simple = pn.is_simple(x, y)
        pn.build_graphic(x, y, x_prime, y_prime, x_simple, y_simple)


    except ValueError:
        print("You input not a naturall number. Try again")
        main()
    except:
        print("Smth goes wrong. Rebooting the app")
        main()


if __name__ == '__main__':
    main()