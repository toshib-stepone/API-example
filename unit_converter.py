def convert(value, from_unit, to_unit):
    conversions = {
        # length (base: meters)
        "m_to_km": lambda v: v / 1000,
        "km_to_m": lambda v: v * 1000,
        "m_to_ft": lambda v: v * 3.28084,
        "ft_to_m": lambda v: v / 3.28084,

        # weight (base: kg)
        "kg_to_lb": lambda v: v * 2.20462,
        "lb_to_kg": lambda v: v / 2.20462,

        # temperature
        "c_to_f": lambda v: (v * 9 / 5) + 32,
        "f_to_c": lambda v: (v - 32) * 5 / 9,
    }

    key = f"{from_unit}_to_{to_unit}"
    if key not in conversions:
        return None

    return conversions[key](value)


def main():
    print("Available conversions:")
    print("  m <-> km, m <-> ft")
    print("  kg <-> lb")
    print("  c <-> f  (temperature)\n")

    from_unit = input("Convert from (e.g. m, km, ft, kg, lb, c, f): ").strip().lower()
    to_unit = input("Convert to: ").strip().lower()

    try:
        value = float(input(f"Enter value in {from_unit}: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    result = convert(value, from_unit, to_unit)

    if result is None:
        print(f"Conversion from '{from_unit}' to '{to_unit}' is not supported.")
    else:
        print(f"{value} {from_unit} = {result:.4f} {to_unit}")


if __name__ == "__main__":
    main()