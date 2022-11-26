from argparse import ArgumentParser, RawTextHelpFormatter, SUPPRESS, Namespace
from dbsoup.cli import actions

DESC = """

        <<<---------- dbsoup Help -------------->>>

List of Commands:

     version -->  print the project version to the terminal 

"""


def parse_args() -> Namespace:

    parser = ArgumentParser(description=DESC, formatter_class=RawTextHelpFormatter, usage=SUPPRESS)
    sub_parsers = parser.add_subparsers(dest='command')
    sub_parsers.required = True

    init_parser = sub_parsers.add_parser("init")
    init_parser.set_defaults(func=actions.init)

    destroy_parser = sub_parsers.add_parser("destroy")
    destroy_parser.set_defaults(func=actions.destroy)

    new_parser = sub_parsers.add_parser("new")
    new_parser.set_defaults(func=actions.new)

    up_parser = sub_parsers.add_parser("up")
    up_parser.set_defaults(func=actions.up)

    down_parser = sub_parsers.add_parser("down")
    down_parser.set_defaults(func=actions.down)

    version_parser = sub_parsers.add_parser('version')
    version_parser.set_defaults(func=actions.version)

    return parser.parse_args()
