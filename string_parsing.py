"""
The following program will consist of multiple methods in which consist of manipulating, handling, changing, and etc
of strings, list of strings, list of list of strings, and etc.
"""

import csv


def parse_queries():
    """
    Used for the query_parsing function
    :return: the string containing all queries
    """
    query_string = ''
    with open("string_file.csv", "r") as csv_file:
        reader = csv.reader(csv_file)
        query_parse = False
        for row in reader:
            if "query_parsing_problem" in row:
                query_parse = True
                continue
            if "end_query_parsing_problem" in row:
                break
            # print(row)
            if query_parse and row and row[0][0] != '#':
                query_string += ''.join(row)
        # print(query_string)
        return query_string


def query_parsing(query_string):
    """
    This function deals with query parsing.

    Imagine if you had a long string with a bunch of queries where the semicolon (;) is the delimiter for each
    query. Your goal is to devise an algorithm that can parse said string correctly.

    Step 1: Read from csv file and store into a long string
    Step 2: Parse the string
    During the parsing stage- things to note:
        Escape character is backslash: \
        There can be semicolons within quotation marks in which case those should not be used as delimiters
        There can be back-slashing within the quotation marks that potentially will not be an escape character. ex: "\\"
        should read as, "\" after parsing
        There can be quotation marks inside quotation marks. Ex: "\"" should not have the backslash after parsing.
    """

    if len(query_string) < 0:
        return []

    result = []
    in_quotes = False
    is_escape = False
    string_result = ''

    for c in query_string:
        if c == "\"" and not in_quotes:
            in_quotes = True
        elif in_quotes and not is_escape and c == "\\":
            is_escape = True
            continue
        elif in_quotes and is_escape and c == "\\":
            is_escape = False
        elif in_quotes and is_escape and c == "\"":
            is_escape = False
        elif in_quotes and not is_escape and c == "\"":
            in_quotes = False
        if not in_quotes and not is_escape and c == ';':
            string_result += c
            result.append(string_result)
            string_result = ''
            continue
        string_result += c
    return result


def main():
    query_string = parse_queries()
    result = query_parsing(query_string)
    print("\nPrinting results for query_parsing:")
    for r in result:
        print(r)


if __name__ == '__main__':
    main()
