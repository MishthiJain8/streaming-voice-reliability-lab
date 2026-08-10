# Streaming Voice Reliability Lab

A dependency-free Python lab for evaluating chunked voice pipelines before connecting a production speech-to-text provider. It measures end-to-end latency, detects speech using PCM energy, tracks dropped/out-of-order chunks, and emits JSON reports suitable for CI regression gates.

## Run

```bash
python -m voice_lab.cli examples/session.json --max-p95-ms 250
python -m unittest discover -s tests -v
```

## Engineering focus

- Stateful processing of ordered PCM audio chunks
- RMS-energy voice activity detection
- Latency percentiles and stream-integrity diagnostics
- Deterministic fixtures for repeatable evaluation
- CI failure thresholds for p95 latency and dropped chunks

## Next steps

- Add WebSocket ingestion and provider adapters for Deepgram/OpenAI
- Evaluate word error rate against golden transcripts
- Export OpenTelemetry spans and Prometheus metrics
# streaming-voice-reliability-lab
