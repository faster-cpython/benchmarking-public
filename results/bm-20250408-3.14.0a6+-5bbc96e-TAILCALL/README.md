# Results

- fork: faster-cpython/tos_caching_1
- version: 3.14.0a6+
- config: TAILCALL
- commit hash: [5bbc96e](https://github.com/faster%2dcpython/cpython/commit/5bbc96e)
- commit date: 2025-04-08T14:26:05+01:00
- commit merge base: [275056a7fdcbe36aaac494b4183ae59943a338eb](https://github.com/python/cpython/commit/275056a7fdcbe36aaac494b4183ae59943a338eb)
- ref: tos_caching_1

## linux aarch64 (arminc_clang)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14334771971)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250408-arminc_clang-aarch64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e.json)

### vs. base

- Geometric mean: 1.002x faster (HPT: reliability of 99.78%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250408-arminc_clang-aarch64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-base-mem.svg)
- [📄table](bm-20250408-arminc_clang-aarch64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-base.md)
- [📈time plot](bm-20250408-arminc_clang-aarch64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-base.svg)

### vs. 3.10.4

- [📄table](bm-20250408-arminc_clang-aarch64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.10.4.md)
- [📈time plot](bm-20250408-arminc_clang-aarch64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.10.4.svg)

### vs. 3.12.0

- [📄table](bm-20250408-arminc_clang-aarch64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.12.0.md)
- [📈time plot](bm-20250408-arminc_clang-aarch64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.12.0.svg)

### vs. 3.13.0

- [📄table](bm-20250408-arminc_clang-aarch64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.13.0.md)
- [📈time plot](bm-20250408-arminc_clang-aarch64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.13.0.svg)

## linux x86_64 (linux_clang)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14334771971)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250408-linux_clang-x86_64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e.json)

### vs. base

- Geometric mean: 1.009x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250408-linux_clang-x86_64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-base-mem.svg)
- [📄table](bm-20250408-linux_clang-x86_64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-base.md)
- [📈time plot](bm-20250408-linux_clang-x86_64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-base.svg)

### vs. 3.10.4

- [📄table](bm-20250408-linux_clang-x86_64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.10.4.md)
- [📈time plot](bm-20250408-linux_clang-x86_64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.10.4.svg)

### vs. 3.12.0

- [📄table](bm-20250408-linux_clang-x86_64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.12.0.md)
- [📈time plot](bm-20250408-linux_clang-x86_64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.12.0.svg)

### vs. 3.13.0

- [📄table](bm-20250408-linux_clang-x86_64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.13.0.md)
- [📈time plot](bm-20250408-linux_clang-x86_64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.13.0.svg)

## windows amd64 (pythonperf1_clang)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14334771971)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250408-pythonperf1_clang-amd64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e.json)

### vs. base

- Geometric mean: 1.011x faster (HPT: reliability of 98.36%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250408-pythonperf1_clang-amd64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-base.md)
- [📈time plot](bm-20250408-pythonperf1_clang-amd64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-base.svg)

### vs. 3.10.4

- [📄table](bm-20250408-pythonperf1_clang-amd64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.10.4.md)
- [📈time plot](bm-20250408-pythonperf1_clang-amd64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.10.4.svg)

### vs. 3.12.0

- [📄table](bm-20250408-pythonperf1_clang-amd64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.12.0.md)
- [📈time plot](bm-20250408-pythonperf1_clang-amd64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.12.0.svg)

### vs. 3.13.0

- [📄table](bm-20250408-pythonperf1_clang-amd64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.13.0.md)
- [📈time plot](bm-20250408-pythonperf1_clang-amd64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.13.0.svg)

## darwin arm64 (darwin_clang)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14334771971)
- cpu model: missing
- platform: macOS-15.3.2-arm64-arm-64bit-Mach-O
- [raw results](bm-20250408-darwin_clang-arm64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e.json)

### vs. base

- Geometric mean: 1.011x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250408-darwin_clang-arm64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-base-mem.svg)
- [📄table](bm-20250408-darwin_clang-arm64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-base.md)
- [📈time plot](bm-20250408-darwin_clang-arm64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-base.svg)

### vs. 3.10.4

- [📄table](bm-20250408-darwin_clang-arm64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.10.4.md)
- [📈time plot](bm-20250408-darwin_clang-arm64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.10.4.svg)

### vs. 3.12.0

- [📄table](bm-20250408-darwin_clang-arm64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.12.0.md)
- [📈time plot](bm-20250408-darwin_clang-arm64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.12.0.svg)

### vs. 3.13.0

- [📄table](bm-20250408-darwin_clang-arm64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.13.0.md)
- [📈time plot](bm-20250408-darwin_clang-arm64-faster%252dcpython-tos_caching_1-3.14.0a6%2B-5bbc96e-vs-3.13.0.svg)

