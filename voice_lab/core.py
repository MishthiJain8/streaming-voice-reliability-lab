from __future__ import annotations

import math
from dataclasses import dataclass
from statistics import mean


@dataclass(frozen=True)
class AudioChunk:
    sequence: int
    captured_ms: float
    processed_ms: float
    samples: tuple[int, ...]


def rms(samples: tuple[int, ...]) -> float:
    if not samples:
        return 0.0
    return math.sqrt(mean(sample * sample for sample in samples))


def percentile(values: list[float], fraction: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    index = math.ceil(fraction * len(ordered)) - 1
    return ordered[max(0, index)]


def evaluate(chunks: list[AudioChunk], speech_threshold: float = 500.0) -> dict:
    sequences = [chunk.sequence for chunk in chunks]
    unique = set(sequences)
    expected = set(range(min(unique), max(unique) + 1)) if unique else set()
    latencies = [max(0.0, chunk.processed_ms - chunk.captured_ms) for chunk in chunks]
    speech_chunks = sum(rms(chunk.samples) >= speech_threshold for chunk in chunks)
    return {
        "chunks": len(chunks),
        "speech_chunks": speech_chunks,
        "duplicate_chunks": len(sequences) - len(unique),
        "dropped_chunks": len(expected - unique),
        "out_of_order": sequences != sorted(sequences),
        "mean_latency_ms": round(mean(latencies), 2) if latencies else 0.0,
        "p95_latency_ms": round(percentile(latencies, 0.95), 2),
    }
