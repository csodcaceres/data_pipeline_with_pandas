from data_utils import (
    load_data,
    validate_columns,
    average_salary,
    people_of_30,
    save_to_csv
)

INPUT_FILE = "data/data.csv"
OUTPUT_FILE = "data/output/people_over_30.csv"

def main():
    df = load_data(INPUT_FILE)
        
    validate_columns(df)

    avg = average_salary(df)
    print(f"Salario promedio: {avg}")

    filtered = people_of_30(df)
    print("Peaple over 30:")
    print(filtered)

    save_to_csv(filtered, OUTPUT_FILE)

if __name__ == "__main__":
    main()