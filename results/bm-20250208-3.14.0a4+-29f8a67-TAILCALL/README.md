# Results

- fork: python/29f8a67ae00081a36fdc
- version: 3.14.0a4+
- config: TAILCALL
- commit hash: [29f8a67](https://github.com/python/cpython/commit/29f8a67)
- commit date: 2025-02-08T23:35:28+00:00
- commit merge base: [c1f352bf0813803bb795b796c16040a5cd4115f2](https://github.com/python/cpython/commit/c1f352bf0813803bb795b796c16040a5cd4115f2)
- ref: 29f8a67ae00081a36fdc

## linux aarch64 (arminc_clang)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13271618637)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250208-arminc_clang-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67.json)

### vs. 3.10.4

- [📄table](bm-20250208-arminc_clang-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.10.4.md)
- [📈time plot](bm-20250208-arminc_clang-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.10.4.svg)

### vs. 3.12.0

- [📄table](bm-20250208-arminc_clang-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.12.0.md)
- [📈time plot](bm-20250208-arminc_clang-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.12.0.svg)

### vs. 3.13.0

- [📄table](bm-20250208-arminc_clang-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.13.0.md)
- [📈time plot](bm-20250208-arminc_clang-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.13.0.svg)

### vs. base

- [🧠memory plot](bm-20250208-arminc_clang-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base-mem.svg)
- [📄table](bm-20250208-arminc_clang-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base.md)
- [📈time plot](bm-20250208-arminc_clang-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base.svg)

## linux x86_64 (linux_clang)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13271618637)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250208-linux_clang-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67.json)

### vs. 3.10.4

- [📄table](bm-20250208-linux_clang-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.10.4.md)
- [📈time plot](bm-20250208-linux_clang-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.10.4.svg)

### vs. 3.12.0

- [📄table](bm-20250208-linux_clang-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.12.0.md)
- [📈time plot](bm-20250208-linux_clang-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.12.0.svg)

### vs. 3.13.0

- [📄table](bm-20250208-linux_clang-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.13.0.md)
- [📈time plot](bm-20250208-linux_clang-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.13.0.svg)

### vs. base

- [🧠memory plot](bm-20250208-linux_clang-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base-mem.svg)
- [📄table](bm-20250208-linux_clang-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base.md)
- [📈time plot](bm-20250208-linux_clang-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13271618637)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67.json)

### vs. 3.10.4

- Geometric mean: 1.421x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.10.4.md)
- [📈time plot](bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.098x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.12.0.md)
- [📈time plot](bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.111x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.13.0.md)
- [📈time plot](bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.047x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: 🔴 asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [🧠memory plot](bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base-mem.svg)
- [📄table](bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base.md)
- [📈time plot](bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base.svg)

## windows amd64 (pythonperf1_clang)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13271618637)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250208-pythonperf1_clang-amd64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67.json)

### vs. 3.10.4

- [📄table](bm-20250208-pythonperf1_clang-amd64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.10.4.md)
- [📈time plot](bm-20250208-pythonperf1_clang-amd64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.10.4.svg)

### vs. 3.12.0

- [📄table](bm-20250208-pythonperf1_clang-amd64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.12.0.md)
- [📈time plot](bm-20250208-pythonperf1_clang-amd64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.12.0.svg)

### vs. 3.13.0

- [📄table](bm-20250208-pythonperf1_clang-amd64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.13.0.md)
- [📈time plot](bm-20250208-pythonperf1_clang-amd64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.13.0.svg)

### vs. base

- [📄table](bm-20250208-pythonperf1_clang-amd64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base.md)
- [📈time plot](bm-20250208-pythonperf1_clang-amd64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base.svg)

## windows x86 (pythonperf1_win32_clang)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13271618637)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250208-pythonperf1_win32_clang-x86-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67.json)

### vs. 3.10.4

- [📄table](bm-20250208-pythonperf1_win32_clang-x86-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.10.4.md)
- [📈time plot](bm-20250208-pythonperf1_win32_clang-x86-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.10.4.svg)

### vs. 3.12.0

- [📄table](bm-20250208-pythonperf1_win32_clang-x86-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.12.0.md)
- [📈time plot](bm-20250208-pythonperf1_win32_clang-x86-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.12.0.svg)

### vs. 3.13.0

- [📄table](bm-20250208-pythonperf1_win32_clang-x86-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.13.0.md)
- [📈time plot](bm-20250208-pythonperf1_win32_clang-x86-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.13.0.svg)

### vs. base

- [📄table](bm-20250208-pythonperf1_win32_clang-x86-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base.md)
- [📈time plot](bm-20250208-pythonperf1_win32_clang-x86-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base.svg)

## darwin arm64 (darwin_clang)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13271618637)
- cpu model: missing
- platform: macOS-15.3-arm64-arm-64bit-Mach-O
- [raw results](bm-20250208-darwin_clang-arm64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67.json)

### vs. 3.10.4

- [📄table](bm-20250208-darwin_clang-arm64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.10.4.md)
- [📈time plot](bm-20250208-darwin_clang-arm64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.10.4.svg)

### vs. 3.12.0

- [📄table](bm-20250208-darwin_clang-arm64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.12.0.md)
- [📈time plot](bm-20250208-darwin_clang-arm64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.12.0.svg)

### vs. 3.13.0

- [📄table](bm-20250208-darwin_clang-arm64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.13.0.md)
- [📈time plot](bm-20250208-darwin_clang-arm64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-3.13.0.svg)

### vs. base

- [🧠memory plot](bm-20250208-darwin_clang-arm64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base-mem.svg)
- [📄table](bm-20250208-darwin_clang-arm64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base.md)
- [📈time plot](bm-20250208-darwin_clang-arm64-python-29f8a67ae00081a36fdc-3.14.0a4%2B-29f8a67-vs-base.svg)

