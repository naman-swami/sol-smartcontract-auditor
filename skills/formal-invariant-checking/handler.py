import argparse
import json

def run(data):
    return {
        "skill": "formal-invariant-checking",
        "status": "success",
        "processed_input": data
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="sample_input")
    args = parser.parse_args()
    print(json.dumps(run(args.data), indent=2))
