import unittest

from voice_lab.core import AudioChunk, evaluate


class EvaluateTest(unittest.TestCase):
    def test_detects_gap_and_latency(self):
        chunks = [AudioChunk(0, 0, 20, (0, 1)), AudioChunk(2, 10, 60, (1000, -1000))]
        report = evaluate(chunks)
        self.assertEqual(report["dropped_chunks"], 1)
        self.assertEqual(report["speech_chunks"], 1)
        self.assertEqual(report["p95_latency_ms"], 50)


if __name__ == "__main__":
    unittest.main()
