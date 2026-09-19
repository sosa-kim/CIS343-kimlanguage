import sys


def run_file(path: str) -> None:
    try:
        with open(path, "r", encoding="utf-8") as f:
            source = f.read()
    except OSError as e:
        print(f"Could not open file {path}: {e}")
        sys.exit(74)
    run(source)


def run_prompt() -> None:
    print(">>> kim Interactive Shell <<<")
    while True:
        try:
            line = input("> ")
            run(line)
        except KeyboardInterrupt:
            print()
            break
        except EOFError:
            print()
            break


def run(source: str) -> None:
    print(source)
    print("Scanner Not Implemented")


def main() -> None:
    args = sys.argv[1:]

    if len(args) > 1:
        print("Usage: python kim.py [script]")
        sys.exit(64)
    elif len(args) == 1:
        run_file(args[0])
    else:
        run_prompt()


if __name__ == "__main__":
    main()