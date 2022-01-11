from tika import parser
import urllib.parse


def print_and_log(logger, level, message):
    """ Prints the log messages
        :param logger: logger name
        :param level: log level
        :param message: log message
    """
    print(message)
    getattr(logger, level.lower())(message)


def extract(content):
    """ Extracts the contents
        :param content: content to be extracted
        Returns:
            parsed_test: parsed text
    """
    parsed = parser.from_buffer(content)
    parsed_text = parsed['content']
    return parsed_text


def encode(object_name):
    """Performs encoding on the name of objects
        containing special characters in their url, and
        replaces single quote with two single quote since quote
        is treated as an escape character in odata
        :param object_name: name that contains special characters
    """
    name = urllib.parse.quote(object_name, safe="'")
    return name.replace("'", "''")
