import click


@click.group()
def main():
    """This is an "click" example CLI argument parsing."""
    pass


@main.command()
@click.option("--times", default=1, type=click.IntRange(1, 5), help="Number of greetings: 1-5")
@click.argument("name")
def hello(name, times):
    """This says hello a particular number of times using the provided name argument."""
    for _ in range(times):
        click.echo("Hello, {}!".format(name))


@main.command()
@click.argument("name", default="Cruel World")
def goodbye(name):
    """This says goodbye using the optional name argument."""
    utterance = "Goodbye, {}!".format(name)
    if name == "Cruel World":
        utterance = click.style(utterance, fg="red")
    click.echo(utterance)

