import os


def main() -> None:
    """Writes a single fix commit message to entry.txt under $MAKEFUN_OUTPUT_DIR."""
    MESSAGE = "fix: prevent unauthorized access by disabling login\n"

    made_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(made_dir, exist_ok=True)
    out_path = os.path.join(made_dir, "entry.txt")

    content = MESSAGE
    # Gate: entry.txt is 1-100 chars, UTF-8, not only whitespace (judge reads it pairwise).
    if not (1 <= len(content) <= 100 and content.strip()):
        raise ValueError("entry content length or whitespace rule violated")

    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(content)

    print(out_path)
    print(len(content))


if __name__ == "__main__":
    main()
