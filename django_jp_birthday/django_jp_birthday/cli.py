"""Console script for django_jp_birthday."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for django_jp_birthday."""
    click.echo(
        "Replace this message by putting your code into " "django_jp_birthday.cli.main"
    )
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
