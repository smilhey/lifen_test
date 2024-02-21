import json
import sys
import argparse


def page_to_string(document, page):
    """
    Reorders the words in a page by their y_min and x_min coordinates into a string.
    """
    try:
        words = document["pages"][page]["words"]
        sorted_words = sorted(
            words, key=lambda x: (x["bbox"]["y_min"], x["bbox"]["x_min"])
        )
        reordered_text = " ".join(word["text"] for word in sorted_words)
        return reordered_text
    except KeyError:
        print("Error: Invalid document format. Words are missing.")
        sys.exit(1)


def extract_patient_name(text):
    """
    Extracts the patient's first and last name from a string.
    """
    keywords = ["Monsieur", "Madame", "M.", "Mme"]
    split_text = text.split()
    for i in range(len(split_text)):
        if split_text[i] in keywords:
            first_name = split_text[i + 1]
            last_name = split_text[i + 2] if i + 2 < len(split_text) else ""
            return {"first_name": first_name, "last_name": last_name}
    return {}


def load_json(input_file):
    """
    Loads the JSON file.
    """
    try:
        with open(input_file, "r") as f:
            document = json.load(f)
        return document
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{input_file}'.")
        sys.exit(1)


def parse_arguments():
    """
    Parse command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Extract patient's name from JSON document."
    )
    parser.add_argument("input_file", help="Input JSON file containing medical report")
    parser.add_argument(
        "output_file",
        nargs="?",
        help="Output JSON file to write the extracted name (optional)",
    )
    return parser.parse_args()


def main(input_file, output_file=None):
    """
    Extracts name from the input JSON document and writes to output file if specified, print it otherwise.
    """
    document = load_json(input_file)
    text_document = " ".join(
        page_to_string(document, i) for i in range(len(document["pages"]))
    )
    extracted_name = extract_patient_name(text_document)

    if output_file:
        with open(output_file, "w") as f:
            json.dump(extracted_name, f)
    else:
        print(
            f"First name: {extracted_name['first_name']}, Last name: {extracted_name['last_name']}"
        )


if __name__ == "__main__":
    args = parse_arguments()
    main(args.input_file, args.output_file)
