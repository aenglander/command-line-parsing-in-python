import sys

from cliff.app import App
from cliff.commandmanager import CommandManager
from cliff.command import Command


class CliffExample(App):
    def __init__(self):
        """
        Set up the cliff application
        """
        super(CliffExample, self).__init__(
            description='This is an "cliff" example CLI argument parsing.',
            version='1.0.0',
            command_manager=CommandManager('cliff.example')
        )


class Hello(Command):

    def get_description(self):
        return "This says hello a particular number of times."

    def get_parser(self, prog_name):
        parser = super().get_parser(prog_name)
        parser.add_argument('name', help='Name to use when saying hello.')
        parser.add_argument('--times', nargs="?", default=1, type=int, help="Number of greetings: 1-5",
                            choices=range(1, 6))
        return parser

    def take_action(self, parsed_args):
        for _ in range(parsed_args.times):
            print("Hello, {}!".format(parsed_args.name))


class Goodbye(Command):

    def get_description(self):
        return "This says goodbye."

    def get_parser(self, prog_name):
        parser = super().get_parser(prog_name)
        parser.add_argument('name', nargs='?', help='Name to use when saying hello.', default="Cruel World")
        return parser

    def take_action(self, parsed_args):
        print("Goodbye, {}!".format(parsed_args.name))


def main(argv=sys.argv[1:]):
    """
    Main method that creates and runs app
    """
    app = CliffExample()

    return app.run(argv)
