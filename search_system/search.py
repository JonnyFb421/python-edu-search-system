import argparse


def search_system_for_text(text, file_types):
    """
    This method should be the entry point to your solution.
    :param text: String text to search files with
    :param file_types: List of file types to search for
    :return:
    """


def main():
    parser = argparse.ArgumentParser(description='Searches files for a string')
    parser.add_argument('-t', '--text', required=True)
    parser.add_argument('-f', '--file-types', nargs='*', default=None)
    args = parser.parse_args()
    search_system_for_text(args.text, args.file_type)


if __name__ == '__main__':
    main()