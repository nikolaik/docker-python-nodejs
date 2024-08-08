from .cli import main, parse_args
from .logger import init_logging


def dpn() -> None:
    args = parse_args()
    init_logging(args.verbose)
    main(args)
