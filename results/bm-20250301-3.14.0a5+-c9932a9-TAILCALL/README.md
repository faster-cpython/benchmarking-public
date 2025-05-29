# Results

- fork: python/c9932a9ec8a3077933a8
- version: 3.14.0a5+
- config: TAILCALL
- commit hash: [c9932a9](https://github.com/python/cpython/commit/c9932a9)
- commit date: 2025-03-01T21:25:38+00:00
- commit merge base: [a55dffd66dbddfd50c8f3de195218d041d26bd3c](https://github.com/python/cpython/commit/a55dffd66dbddfd50c8f3de195218d041d26bd3c)
- ref: c9932a9ec8a3077933a8

## linux aarch64 (arminc_clang)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13610054065)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250301-arminc_clang-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9.json)

### vs. 3.10.4

- [📄table](bm-20250301-arminc_clang-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-3.10.4.md)
- [📈time plot](bm-20250301-arminc_clang-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-3.10.4.svg)

### vs. 3.12.0

- [📄table](bm-20250301-arminc_clang-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-3.12.0.md)
- [📈time plot](bm-20250301-arminc_clang-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-3.12.0.svg)

### vs. 3.13.0

- [📄table](bm-20250301-arminc_clang-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-3.13.0.md)
- [📈time plot](bm-20250301-arminc_clang-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-3.13.0.svg)

### vs. base

- [🧠memory plot](bm-20250301-arminc_clang-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-base-mem.svg)
- [📄table](bm-20250301-arminc_clang-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-base.md)
- [📈time plot](bm-20250301-arminc_clang-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-base.svg)

## linux x86_64 (linux_clang)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13610054065)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250301-linux_clang-x86_64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9.json)

### vs. 3.10.4

- [📄table](bm-20250301-linux_clang-x86_64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-3.10.4.md)
- [📈time plot](bm-20250301-linux_clang-x86_64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-3.10.4.svg)

### vs. 3.12.0

- [📄table](bm-20250301-linux_clang-x86_64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-3.12.0.md)
- [📈time plot](bm-20250301-linux_clang-x86_64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-3.12.0.svg)

### vs. 3.13.0

- [📄table](bm-20250301-linux_clang-x86_64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-3.13.0.md)
- [📈time plot](bm-20250301-linux_clang-x86_64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-3.13.0.svg)

### vs. base

- [🧠memory plot](bm-20250301-linux_clang-x86_64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-base-mem.svg)
- [📄table](bm-20250301-linux_clang-x86_64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-base.md)
- [📈time plot](bm-20250301-linux_clang-x86_64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13610054065)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250301-pythonperf2-x86_64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9.json)

### vs. 3.10.4

- Geometric mean: 1.406x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250301-pythonperf2-x86_64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-3.10.4.md)
- [📈time plot](bm-20250301-pythonperf2-x86_64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.087x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250301-pythonperf2-x86_64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-3.12.0.md)
- [📈time plot](bm-20250301-pythonperf2-x86_64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.101x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250301-pythonperf2-x86_64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-3.13.0.md)
- [📈time plot](bm-20250301-pythonperf2-x86_64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.050x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.03x
- [🧠memory plot](bm-20250301-pythonperf2-x86_64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-base-mem.svg)
- [📄table](bm-20250301-pythonperf2-x86_64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-base.md)
- [📈time plot](bm-20250301-pythonperf2-x86_64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-base.svg)

## windows amd64 (pythonperf1_clang)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13610054065)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250301-pythonperf1_clang-amd64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9.json)

### vs. 3.10.4

- [📄table](bm-20250301-pythonperf1_clang-amd64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-3.10.4.md)
- [📈time plot](bm-20250301-pythonperf1_clang-amd64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-3.10.4.svg)

### vs. 3.12.0

- [📄table](bm-20250301-pythonperf1_clang-amd64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-3.12.0.md)
- [📈time plot](bm-20250301-pythonperf1_clang-amd64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-3.12.0.svg)

### vs. 3.13.0

- [📄table](bm-20250301-pythonperf1_clang-amd64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-3.13.0.md)
- [📈time plot](bm-20250301-pythonperf1_clang-amd64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-3.13.0.svg)

### vs. base

- [📄table](bm-20250301-pythonperf1_clang-amd64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-base.md)
- [📈time plot](bm-20250301-pythonperf1_clang-amd64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-base.svg)

## windows x86 (pythonperf1_win32_clang)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13610054065)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250301-pythonperf1_win32_clang-x86-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9.json)

### vs. 3.10.4

- [📄table](bm-20250301-pythonperf1_win32_clang-x86-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-3.10.4.md)
- [📈time plot](bm-20250301-pythonperf1_win32_clang-x86-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-3.10.4.svg)

### vs. 3.12.0

- [📄table](bm-20250301-pythonperf1_win32_clang-x86-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-3.12.0.md)
- [📈time plot](bm-20250301-pythonperf1_win32_clang-x86-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-3.12.0.svg)

### vs. 3.13.0

- [📄table](bm-20250301-pythonperf1_win32_clang-x86-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-3.13.0.md)
- [📈time plot](bm-20250301-pythonperf1_win32_clang-x86-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-3.13.0.svg)

### vs. base

- [📄table](bm-20250301-pythonperf1_win32_clang-x86-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-base.md)
- [📈time plot](bm-20250301-pythonperf1_win32_clang-x86-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-base.svg)

## darwin arm64 (darwin_clang)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13610054065)
- cpu model: missing
- platform: macOS-15.3-arm64-arm-64bit-Mach-O
- [raw results](bm-20250301-darwin_clang-arm64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9.json)

### vs. 3.10.4

- [📄table](bm-20250301-darwin_clang-arm64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-3.10.4.md)
- [📈time plot](bm-20250301-darwin_clang-arm64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-3.10.4.svg)

### vs. 3.12.0

- [📄table](bm-20250301-darwin_clang-arm64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-3.12.0.md)
- [📈time plot](bm-20250301-darwin_clang-arm64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-3.12.0.svg)

### vs. 3.13.0

- [📄table](bm-20250301-darwin_clang-arm64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-3.13.0.md)
- [📈time plot](bm-20250301-darwin_clang-arm64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-3.13.0.svg)

### vs. base

- [🧠memory plot](bm-20250301-darwin_clang-arm64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-base-mem.svg)
- [📄table](bm-20250301-darwin_clang-arm64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-base.md)
- [📈time plot](bm-20250301-darwin_clang-arm64-python-c9932a9ec8a3077933a8-3.14.0a5%2B-c9932a9-vs-base.svg)

