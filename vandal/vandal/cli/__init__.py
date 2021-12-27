# import all relevant contents from the associated module.
from .cli import (
    __CLIversion__,
    menu,
    greet,
    save_to,
    CLI, #main client.
    MonteCarloCLI,
    DijkstraCLI,
    EOQCLI,
)

# all relevant contents.
__all__ = [
    __CLIversion__,
    menu,
    greet,
    save_to,
    CLI, #main client.
    MonteCarloCLI,
    DijkstraCLI,
    EOQCLI,
]
