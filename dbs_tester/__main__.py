import argparse
import json
import zipfile
from pathlib import Path

from jinja2 import Environment, TemplateSyntaxError

class Colors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Assignment Checker Utility - Evaluate, check, or report on SQL assignments."
    )

    parser.add_argument(
        "-d", "--definition",
        help="Assignment definition file",
        default=Path.cwd() / "data/2025-01/definition.json",
        type=Path
    )

    parser.add_argument(
        "-f", "--file",
        help="Path to submission zip file",
        required=True,
        type=Path
    )

    args = parser.parse_args()
    jinja = Environment()

    # Read definition file
    with open(args.definition, "r") as f:
        definition = json.load(f)

    print(f"Your AIS username is {Colors.BOLD}{args.file.stem}{Colors.ENDC}")


    with zipfile.ZipFile(args.file, 'r') as z:
        for task in definition.get('tasks'):
            with zipfile.ZipFile(args.file, 'r') as z:
                print(f"Checking {task['file']}", end=" ... ")
                try:
                    with z.open(task['file'], "r") as f:
                        jinja.parse(f.read().decode())
                    print(f"{Colors.OKGREEN}[OK]{Colors.ENDC}")
                except KeyError:
                    print(f"{Colors.FAIL}[NOT_FOUND]{Colors.ENDC}")
                except TemplateSyntaxError as e:
                    print(f"{Colors.FAIL}[TEMPLATE_SYNTAX_ERROR]{Colors.ENDC}: {e}")
