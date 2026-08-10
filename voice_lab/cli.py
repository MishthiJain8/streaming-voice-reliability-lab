import argparse
import json

from voice_lab.core import AudioChunk, evaluate


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("session")
    parser.add_argument("--max-p95-ms", type=float, default=300.0)
    args = parser.parse_args()
    with open(args.session, encoding="utf-8") as stream:
        payload = json.load(stream)
    chunks = [AudioChunk(item["sequence"], item["captured_ms"], item["processed_ms"], tuple(item["samples"])) for item in payload]
    report = evaluate(chunks)
    print(json.dumps(report, indent=2))
    return int(report["p95_latency_ms"] > args.max_p95_ms or report["dropped_chunks"] > 0)


if __name__ == "__main__":
    raise SystemExit(main())
