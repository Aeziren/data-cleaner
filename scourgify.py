import sys
import csv

def main():
    # Argument handling
    if len(sys.argv) != 3:
        sys.exit(r"Usage: python scourgify.py path/to/input.csv path/to/output.csv'")
    if not sys.argv[1].endswith(".csv") and not sys.argv[2].endswith(".csv"):
        sys.exit("Input and Output must be .csv files")

    # Open csv file and save first, last and house name of student in students list of dicts
    try:
        with open(sys.argv[1]) as file:
            students = []
            reader = csv.DictReader(file)

            for row in reader:
                last, first = row["name"].split(",")
                house = row["house"]

                students.append({"first": first.strip(), "last": last, "house": house})
    except FileNotFoundError:
        sys.exit("Input file not found")

    # Write each student into new csv file
    with open(sys.argv[2], "w") as output:
        writer = csv.DictWriter(output, fieldnames=students[0].keys())

        writer.writeheader()
        for student in students:
            writer.writerow(student)

if __name__ == "__main__":
    main()