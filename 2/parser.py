import sys
import typer
from pathlib import Path
from typing import List

app = typer.Typer()

class parser:
    def __init__(self, filename):
        self.filename = filename

    def validate(self):
        


@app.command
def validate_json(filenames: List[str] = typer.Argument(..., help="json file")
    ):
    pass

if __name__=="__main__":
    app



