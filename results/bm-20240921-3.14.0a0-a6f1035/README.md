# Results

- fork: brandtbucher
- version: 3.14.0a0
- config: 
- commit hash: [a6f1035](https://github.com/brandtbucher/cpython/commit/a6f1035)
- commit date: 2024-09-21T23:12:25-07:00
- commit merge base: [6e06e01881dcffbeef5baac0c112ffb14cfa0b27](https://github.com/brandtbucher/cpython/commit/6e06e01881dcffbeef5baac0c112ffb14cfa0b27)
- ref: nojit

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10978846909)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035.json)

### vs. 3.10.4

- Geometric mean: 1.329x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence
- [📄table](bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.10.4.md)
- [📈time plot](bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.038x faster (HPT: reliability of 97.99%, 1.00x faster at 99th %ile)
- Memory usage: 0.94x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, unpack_sequence
- [📄table](bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.12.0.md)
- [📈time plot](bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.027x faster (HPT: reliability of 99.97%, 1.00x faster at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.13.0.md)
- [📈time plot](bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x faster (HPT: reliability of 60.28%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-base-mem.svg)
- [📄table](bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-base.md)
- [📈time plot](bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-base.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20240921-azure-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035-pystats.json)
- [pystats table](bm-20240921-azure-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035-pystats.md)

### vs. base

- [pystats diff](bm-20240921-azure-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10978846909)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-193-generic-x86_64-with-glibc2.31
- [raw results](bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035.json)

### vs. 3.10.4

- Geometric mean: 1.428x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.10.4.md)
- [📈time plot](bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.086x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.12.0.md)
- [📈time plot](bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.032x faster (HPT: reliability of 99.94%, 1.00x faster at 99th %ile)
- Memory usage: 0.92x
- missing benchmarks: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.13.0.md)
- [📈time plot](bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.006x slower (HPT: reliability of 80.42%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-base-mem.svg)
- [📄table](bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-base.md)
- [📈time plot](bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10978846909)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035.json)

### vs. 3.10.4

- Geometric mean: 1.325x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.10.4.md)
- [📈time plot](bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.020x faster (HPT: reliability of 65.03%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.12.0.md)
- [📈time plot](bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.029x faster (HPT: reliability of 99.96%, 1.00x faster at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.13.0.md)
- [📈time plot](bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.007x slower (HPT: reliability of 89.61%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-base-mem.svg)
- [📄table](bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-base.md)
- [📈time plot](bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10978846909)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035.json)

### vs. 3.10.4

- Geometric mean: 1.171x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.10.4.md)
- [📈time plot](bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.015x slower (HPT: reliability of 99.37%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.12.0.md)
- [📈time plot](bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.024x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.13.0.md)
- [📈time plot](bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.014x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-base.md)
- [📈time plot](bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10978846909)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035.json)

### vs. 3.10.4

- Geometric mean: 1.125x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.10.4.md)
- [📈time plot](bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.129x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.12.0.md)
- [📈time plot](bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.023x faster (HPT: reliability of 99.65%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.13.0.md)
- [📈time plot](bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.012x slower (HPT: reliability of 99.88%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035-vs-base.md)
- [📈time plot](bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10978846909)
- cpu model: missing
- platform: macOS-14.6.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035.json)

### vs. 3.10.4

- Geometric mean: 1.298x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 0.58x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.10.4.md)
- [📈time plot](bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.088x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 0.51x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.12.0.md)
- [📈time plot](bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.095x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.46x
- missing benchmarks: chameleon, connected_components, dask, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.13.0.md)
- [📈time plot](bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x slower (HPT: reliability of 99.93%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-base-mem.svg)
- [📄table](bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-base.md)
- [📈time plot](bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035-vs-base.svg)

