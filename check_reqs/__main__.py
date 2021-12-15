# type: ignore[attr-defined]
from enum import Enum
from pathlib import Path
from random import choice

import typer
from rich.console import Console

from check_reqs import version
from check_reqs.check_reqs import _output_rich, _process_file


class Color(str, Enum):
    white = "white"
    red = "red"
    cyan = "cyan"
    magenta = "magenta"
    yellow = "yellow"
    green = "green"


app = typer.Typer(
    name="check_reqs",
    help="Checks if all requirements from a file are installed in the current Python env",
    add_completion=False,
)
console = Console()


def version_callback(print_version: bool) -> None:
    """Print the version of the package."""
    if print_version:
        console.print(f"[yellow]check_reqs[/] version: [bold blue]{version}[/]")
        raise typer.Exit()


@app.command(name="")
def main(
    requirements_file: Path = typer.Argument(
        ...,
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
    ),
) -> None:
    """Check a given requirements file"""
    status = _process_file(requirements_file)
    _output_rich(requirements_file, status)
    fails = sum(int(st is not None) for st in status.values())
    raise typer.Exit(code=fails)


if __name__ == "__main__":
    app()
