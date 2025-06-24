import csv


def printing_csv(filename):
    try:
        with open(filename, 'r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            for info in reader:
                print(f"This is {info['Title']} {info['GivenName']}. "
                      f"{'He' if info['Gender'] == 'male' else 'She'} works as {info['Occupation']}"
                      f" in the city of {info['City']}")
    except IOError as ex:
        print(f"Error performing I/O operations on the file {filename}: ", ex)


def add_record_to_csv(filename):
    print("Please enter the new record details:")

    given_name = input("Given name: ").strip()
    gender = input("Gender (male/female): ").strip().lower()
    title = input("Title (Mr./Ms./Dr./etc.): ").strip()
    occupation = input("Occupation: ").strip()
    city = input("City: ").strip()

    # Validation
    if not given_name:
        print("Given name is required.")
        return
    if gender not in ('male', 'female'):
        print("Gender must be 'male' or 'female'.")
        return
    if not title:
        print("Title is required.")
        return
    if not occupation:
        print("Occupation is required.")
        return
    if not city:
        print("City is required.")
        return

    # Append the new record
    try:
        with open(filename, 'a', newline='', encoding='utf-8-sig') as file:
            fieldnames = ['GivenName', 'Gender', 'Title', 'Occupation', 'City']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writerow({
                'GivenName': given_name,
                'Gender': gender,
                'Title': title,
                'Occupation': occupation,
                'City': city
            })
        print("Record added successfully.")
    except IOError as e:
        print(f"Failed to write to file: {e}")


def summarize_city_titles(input_filename, output_filename="city_summary.csv"):
    city_dict = {}

    # Read the input file
    try:
        with open(input_filename, 'r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)

            for row in reader:
                city = row.get('City', '').strip()
                title = row.get('Title', '').strip()
                if city and title:
                    city_dict.setdefault(city, {}).setdefault(title, 0)
                    city_dict[city][title] += 1

    except IOError as e:
        print(f"Error reading file: {e}")
        return

    # Write the summarized output
    try:
        with open(output_filename, 'w', newline='', encoding='utf-8') as outfile:
            fieldnames = ['City', 'Title', 'Count']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            for city, title_counts in city_dict.items():
                for title, count in title_counts.items():
                    writer.writerow({'City': city, 'Title': title, 'Count': count})

        print(f"Summary written to '{output_filename}'.")

    except IOError as e:
        print(f"Error writing file: {e}")


if __name__ == '__main__':
    printing_csv('sample_names.csv')
    add_record_to_csv('sample_names.csv')
    summarize_city_titles('sample_names.csv')
