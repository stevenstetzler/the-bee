def main():
    import argparse
    import sys
    parser = argparse.ArgumentParser()

    parser.add_argument("answers", type=argparse.FileType('r'), nargs="?", default=sys.stdin, help="File containing answers, one per line.")
    parser.add_argument("--output", type=argparse.FileType('w'), default=sys.stdout, help="Output file to write formatted answers.")

    args = parser.parse_args()

    did_header = False
    while line := args.answers.readline():
        answer = line.strip()
        if not did_header:
            args.output.write("<h2>Answers</h2>\n")
            args.output.write(f"<p>{answer}</p>\n")
            args.output.write("<ul>\n")
            did_header = True
            continue
        if answer:
            args.output.write(f"  <li> {answer} </li>\n")
    args.output.write("</ul>\n")


if __name__ == "__main__":
    main()