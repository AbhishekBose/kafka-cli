from pyfiglet import figlet_format
import six

try:
    import colorama
    colorama.init()
except ImportError:
    colorama = None


try:
    from termcolor import colored
except ImportError:
    colored = None

def log(string, color, font="slant", figlet=False):
    if colored:
        if not figlet:
            six.print_(colored(string, color))
        else:
            six.print_(colored(figlet_format(
                string, font=font), color))
    else:
        six.print_(string)

if __name__ == "__main__":
    log("Hello world",color="green")