import json
import requests

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("time_range", help="Time range to get answers over. One of: today, yesterday, thisWeek, and lastWeek.")

    args = parser.parse_args()

    url = "https://www.nytimes.com/puzzles/spelling-bee"
    r = requests.get(url)

    data = r.text.split("window.gameData = ")[1]
    data = data.split("</script>")[0]
    data = json.loads(data)
    if args.time_range in ["thisWeek", "lastWeek"]:
        data = data['pastPuzzles'][args.time_range]
        for d in data:
            print(d['displayDate'])
            answers = d['answers']
            print("\n".join(sorted(answers)))
            print()
    else:
        data = data[args.time_range]
        print(data['displayDate'])
        answers = data['answers']
        print("\n".join(sorted(answers)))
        print()

if __name__ == "__main__":
    main()
