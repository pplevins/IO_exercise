import csv
import json


def csv_to_json(input_csv, output_json="people.json"):
    people = []

    try:
        with open(input_csv, 'r', encoding='utf-8-sig') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                people.append(row)

        with open(output_json, 'w', encoding='utf-8') as json_file:
            json.dump(people, json_file, ensure_ascii=False, indent=2)

        print(f"JSON file '{output_json}' created successfully with {len(people)} people.")

    except Exception as e:
        print(f"Error during CSV to JSON conversion: {e}")


def count_people_per_city(json_file="people.json"):
    try:
        with open(json_file, 'r', encoding='utf-8') as file:
            people = json.load(file)

        city_counts = {}
        for person in people:
            city = person.get('City', '').strip()
            if city:
                city_counts[city] = city_counts.get(city, 0) + 1

        print("Number of people per city:")
        for city, count in city_counts.items():
            print(f"- {city}: {count}")

    except Exception as e:
        print(f"Error reading JSON file: {e}")


if __name__ == '__main__':
    csv_to_json("sample_names.csv")
    count_people_per_city()
