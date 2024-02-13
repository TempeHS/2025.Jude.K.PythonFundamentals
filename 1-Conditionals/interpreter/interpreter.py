def main():

    expression = input("Expression: ").strip()
    # Convert this into varibles
    x, y, z = expression.split(" ")

    x_f = float(x)
    z_f = float(z)
    # Calculate the results
    if y == "+":
        results = x_f + z_f
    elif y == "-":
        results = x_f - z_f
    elif y == "*":
        results = x_f * z_f
    elif y == "/":
        results = x_f / z_f
    print(round(results, 1))


main()
