# Results

- fork: mdboom/early_tail_call_load
- version: 3.14.0a4+
- config: TAILCALL
- commit hash: [e9c43a0](https://github.com/mdboom/cpython/commit/e9c43a0)
- commit date: 2025-02-12T17:09:18-06:00
- commit merge base: [d05053a203d922c8056f12ef3c9338229fdce043](https://github.com/python/cpython/commit/d05053a203d922c8056f12ef3c9338229fdce043)
- ref: early_tail_call_load

## linux x86_64 (linux_clang)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13313002500)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250212-linux_clang-x86_64-mdboom-early_tail_call_load-3.14.0a4%2B-e9c43a0.json)

### vs. base

- Geometric mean: 1.008x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250212-linux_clang-x86_64-mdboom-early_tail_call_load-3.14.0a4%2B-e9c43a0-vs-base-mem.svg)
- [📄table](bm-20250212-linux_clang-x86_64-mdboom-early_tail_call_load-3.14.0a4%2B-e9c43a0-vs-base.md)
- [📈time plot](bm-20250212-linux_clang-x86_64-mdboom-early_tail_call_load-3.14.0a4%2B-e9c43a0-vs-base.svg)

### vs. 3.10.4

- [📄table](bm-20250212-linux_clang-x86_64-mdboom-early_tail_call_load-3.14.0a4%2B-e9c43a0-vs-3.10.4.md)
- [📈time plot](bm-20250212-linux_clang-x86_64-mdboom-early_tail_call_load-3.14.0a4%2B-e9c43a0-vs-3.10.4.svg)

### vs. 3.12.0

- [📄table](bm-20250212-linux_clang-x86_64-mdboom-early_tail_call_load-3.14.0a4%2B-e9c43a0-vs-3.12.0.md)
- [📈time plot](bm-20250212-linux_clang-x86_64-mdboom-early_tail_call_load-3.14.0a4%2B-e9c43a0-vs-3.12.0.svg)

### vs. 3.13.0

- [📄table](bm-20250212-linux_clang-x86_64-mdboom-early_tail_call_load-3.14.0a4%2B-e9c43a0-vs-3.13.0.md)
- [📈time plot](bm-20250212-linux_clang-x86_64-mdboom-early_tail_call_load-3.14.0a4%2B-e9c43a0-vs-3.13.0.svg)

## darwin arm64 (darwin_clang)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13313006911)
- cpu model: missing
- platform: macOS-15.3-arm64-arm-64bit-Mach-O
- [raw results](bm-20250212-darwin_clang-arm64-mdboom-early_tail_call_load-3.14.0a4%2B-e9c43a0.json)

### vs. base

- Geometric mean: 1.001x slower (HPT: reliability of 99.66%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250212-darwin_clang-arm64-mdboom-early_tail_call_load-3.14.0a4%2B-e9c43a0-vs-base-mem.svg)
- [📄table](bm-20250212-darwin_clang-arm64-mdboom-early_tail_call_load-3.14.0a4%2B-e9c43a0-vs-base.md)
- [📈time plot](bm-20250212-darwin_clang-arm64-mdboom-early_tail_call_load-3.14.0a4%2B-e9c43a0-vs-base.svg)

### vs. 3.10.4

- [📄table](bm-20250212-darwin_clang-arm64-mdboom-early_tail_call_load-3.14.0a4%2B-e9c43a0-vs-3.10.4.md)
- [📈time plot](bm-20250212-darwin_clang-arm64-mdboom-early_tail_call_load-3.14.0a4%2B-e9c43a0-vs-3.10.4.svg)

### vs. 3.12.0

- [📄table](bm-20250212-darwin_clang-arm64-mdboom-early_tail_call_load-3.14.0a4%2B-e9c43a0-vs-3.12.0.md)
- [📈time plot](bm-20250212-darwin_clang-arm64-mdboom-early_tail_call_load-3.14.0a4%2B-e9c43a0-vs-3.12.0.svg)

### vs. 3.13.0

- [📄table](bm-20250212-darwin_clang-arm64-mdboom-early_tail_call_load-3.14.0a4%2B-e9c43a0-vs-3.13.0.md)
- [📈time plot](bm-20250212-darwin_clang-arm64-mdboom-early_tail_call_load-3.14.0a4%2B-e9c43a0-vs-3.13.0.svg)

