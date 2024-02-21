#### Patient Name Extractor

This script extracts the first and last names of a patient from a JSON document
containing medical reports. It reorders the words in the document based on
their positions and extracts the patient's name using predefined keywords.

#### Usage

To extract the patient's name from a JSON document:

```
python name.py <input_file>.json
```

This will print a dictionary with the patient's first and last names to the
console.

To write the extracted name to an output file:


```
python name.py <input_file>.json <output_file>.json
```

This will write the dictionary with the patient's first and last names to the
specified output file in JSON format. 

##### Input Format

The input JSON document should follow a specific format:

```json
{
  "pages": [
    {
      "words": [
        {
          "text": "word1",
          "bbox": { "x_min": 0.1, "x_max": 0.2, "y_min": 0.3, "y_max": 0.4 }
        },
        {
          "text": "word2",
          "bbox": { "x_min": 0.2, "x_max": 0.3, "y_min": 0.4, "y_max": 0.5 }
        }
      ]
    }
  ]
}
```

##### Output Format

The output is a dictionary with the patient's first and last names in JSON
format:

```json

{ "first_name": "John", "last_name": "Doe" }

```

#### Potential Improvements:

- The json to string conversion is probably not optimal. It would be better to
  first extract upper case words before putting them back in the right order
  for performance reasons.

- The method does not work if first name and last name are separated by other
  words or if the documents does not use a "titre de civilité" like "Mme".

- This script returns the first result it finds. It would be better to extract
  names before differentiating between patient and other persons names. It
  could be done by checking for all words that begins with uppercase letters.
  Obviously, you would have to take into accounts words at the beginning of a
  sentence. You could also compare words against a dictionary of common names
  to do that.

- To distinguish between patient and doctor names or even other persons' name,
  you could check for the presence of words like "Dr." or "Doctor" before the
  name or even look for the position of the name in the text. The doctor's name
  is more likely to be towards the end. Names can also be ranked by distance to
  other keywords like "patient".




