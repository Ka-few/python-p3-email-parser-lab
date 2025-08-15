# email_address_parser.py
import re

class EmailAddressParser:
    def __init__(self, text):
        self.text = text

    def parse(self):
        """
        Extracts all valid email addresses from the text,
        removes duplicates, and returns them sorted alphabetically.
        """
        # Basic email regex that matches letters/numbers, optional dots, then @, then domain
        emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", self.text)

        # Remove duplicates by converting to a set, then back to a list
        unique_emails = sorted(set(emails))

        return unique_emails
# your code goes here!