# Results

- fork: python
- version: 3.14.0a1+
- config: NOGIL
- commit hash: [7d7d56d](https://github.com/python/cpython/commit/7d7d56d)
- commit date: 2024-11-02T10:11:12-07:00
- commit merge base: [868bfcc02ed42a1042851830b79c6877b7f1c7a8](https://github.com/python/cpython/commit/868bfcc02ed42a1042851830b79c6877b7f1c7a8)
- ref: 7d7d56d8b1147a6b85e1

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11646770951)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d.json)

### vs. 3.10.4

- Geometric mean: 1.203x slower (HPT: reliability of 100.00%, 1.21x slower at 99th %ile)
- Memory usage: 1.51x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.10.4.md)
- [📈time plot](bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.370x slower (HPT: reliability of 100.00%, 1.40x slower at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.12.0.md)
- [📈time plot](bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.374x slower (HPT: reliability of 100.00%, 1.38x slower at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: chameleon, gevent_hub, mypy2
- new benchmarks: dulwich_log, sqlite_synth
- [📄table](bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.13.0.md)
- [📈time plot](bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.361x slower (HPT: reliability of 100.00%, 1.38x slower at 99th %ile)
- Memory usage: 1.17x
- [🧠memory plot](bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-base-mem.svg)
- [📄table](bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-base.md)
- [📈time plot](bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11646770951)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241102-linux-x86_64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d.json)

### vs. 3.10.4

- Geometric mean: 1.057x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.45x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241102-linux-x86_64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.10.4.md)
- [📈time plot](bm-20241102-linux-x86_64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.269x slower (HPT: reliability of 100.00%, 1.26x slower at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241102-linux-x86_64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.12.0.md)
- [📈time plot](bm-20241102-linux-x86_64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.305x slower (HPT: reliability of 100.00%, 1.30x slower at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: chameleon, gevent_hub, mypy2
- new benchmarks: sqlite_synth
- [📄table](bm-20241102-linux-x86_64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.13.0.md)
- [📈time plot](bm-20241102-linux-x86_64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.306x slower (HPT: reliability of 100.00%, 1.31x slower at 99th %ile)
- Memory usage: 1.15x
- [🧠memory plot](bm-20241102-linux-x86_64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-base-mem.svg)
- [📄table](bm-20241102-linux-x86_64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-base.md)
- [📈time plot](bm-20241102-linux-x86_64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11646770951)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20241102-pythonperf2-x86_64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d.json)

### vs. 3.10.4

- Geometric mean: 1.105x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: 1.47x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241102-pythonperf2-x86_64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.10.4.md)
- [📈time plot](bm-20241102-pythonperf2-x86_64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.302x slower (HPT: reliability of 100.00%, 1.28x slower at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241102-pythonperf2-x86_64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.12.0.md)
- [📈time plot](bm-20241102-pythonperf2-x86_64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.294x slower (HPT: reliability of 100.00%, 1.28x slower at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: chameleon, gevent_hub, mypy2
- new benchmarks: sqlite_synth
- [📄table](bm-20241102-pythonperf2-x86_64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.13.0.md)
- [📈time plot](bm-20241102-pythonperf2-x86_64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.302x slower (HPT: reliability of 100.00%, 1.32x slower at 99th %ile)
- Memory usage: 1.16x
- [🧠memory plot](bm-20241102-pythonperf2-x86_64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-base-mem.svg)
- [📄table](bm-20241102-pythonperf2-x86_64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-base.md)
- [📈time plot](bm-20241102-pythonperf2-x86_64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11646770951)
- cpu model: missing
- platform: macOS-15.0.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241102-darwin-arm64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d.json)

### vs. 3.10.4

- Geometric mean: 1.095x slower (HPT: reliability of 100.00%, 1.09x slower at 99th %ile)
- Memory usage: 1.45x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241102-darwin-arm64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.10.4.md)
- [📈time plot](bm-20241102-darwin-arm64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.228x slower (HPT: reliability of 100.00%, 1.14x slower at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241102-darwin-arm64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.12.0.md)
- [📈time plot](bm-20241102-darwin-arm64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.211x slower (HPT: reliability of 100.00%, 1.15x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: chameleon, dask, gevent_hub, mypy2
- new benchmarks: sqlite_synth
- [📄table](bm-20241102-darwin-arm64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.13.0.md)
- [📈time plot](bm-20241102-darwin-arm64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.268x slower (HPT: reliability of 100.00%, 1.19x slower at 99th %ile)
- Memory usage: 1.10x
- [🧠memory plot](bm-20241102-darwin-arm64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-base-mem.svg)
- [📄table](bm-20241102-darwin-arm64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-base.md)
- [📈time plot](bm-20241102-darwin-arm64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-base.svg)

