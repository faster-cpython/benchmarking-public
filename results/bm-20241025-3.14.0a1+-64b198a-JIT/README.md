# Results

- fork: brandtbucher/justin_no_externs
- version: 3.14.0a1+
- config: JIT
- commit hash: [64b198a](https://github.com/brandtbucher/cpython/commit/64b198a)
- commit date: 2024-10-25T10:03:36-07:00
- commit merge base: [34653bba644aa5481613f398153757d7357e39ea](https://github.com/python/cpython/commit/34653bba644aa5481613f398153757d7357e39ea)
- ref: justin_no_externs

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11522888886)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a.json)

### vs. 3.10.4

- Geometric mean: 1.155x faster (HPT: reliability of 99.97%, 1.03x faster at 99th %ile)
- Memory usage: 1.37x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-3.10.4.md)
- [📈time plot](bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.094x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, sphinx
- [📄table](bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-3.12.0.md)
- [📈time plot](bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.104x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlite_synth, subparsers
- new benchmarks: dulwich_log
- [📄table](bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-3.13.0.md)
- [📈time plot](bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.009x slower (HPT: reliability of 98.85%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-base-mem.svg)
- [📄table](bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-base.md)
- [📈time plot](bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-base.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20241025-azure-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-pystats.json)
- [pystats table](bm-20241025-azure-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-pystats.md)

### vs. base

- [pystats diff](bm-20241025-azure-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11522888886)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a.json)

### vs. 3.10.4

- Geometric mean: 1.349x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-3.10.4.md)
- [📈time plot](bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.028x faster (HPT: reliability of 96.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-3.12.0.md)
- [📈time plot](bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.027x slower (HPT: reliability of 99.98%, 1.00x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlite_synth, subparsers
- [📄table](bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-3.13.0.md)
- [📈time plot](bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.029x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-base-mem.svg)
- [📄table](bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-base.md)
- [📈time plot](bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11522888886)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a.json)

### vs. 3.10.4

- Geometric mean: 1.261x faster (HPT: reliability of 100.00%, 1.15x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-3.10.4.md)
- [📈time plot](bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.025x slower (HPT: reliability of 99.14%, 1.00x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-3.12.0.md)
- [📈time plot](bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.022x slower (HPT: reliability of 93.35%, 1.00x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlite_synth, subparsers
- [📄table](bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-3.13.0.md)
- [📈time plot](bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.011x slower (HPT: reliability of 99.97%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-base-mem.svg)
- [📄table](bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-base.md)
- [📈time plot](bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11522888886)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a.json)

### vs. 3.10.4

- Geometric mean: 1.185x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx
- [📄table](bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-3.10.4.md)
- [📈time plot](bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.001x faster (HPT: reliability of 59.33%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-3.12.0.md)
- [📈time plot](bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.019x slower (HPT: reliability of 99.83%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- [📄table](bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-3.13.0.md)
- [📈time plot](bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.013x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-base.md)
- [📈time plot](bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11522888886)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a.json)

### vs. 3.10.4

- Geometric mean: 1.158x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx
- [📄table](bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-3.10.4.md)
- [📈time plot](bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.168x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-3.12.0.md)
- [📈time plot](bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.046x faster (HPT: reliability of 69.76%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- [📄table](bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-3.13.0.md)
- [📈time plot](bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.018x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-base.md)
- [📈time plot](bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11522888886)
- cpu model: missing
- platform: macOS-15.0.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a.json)

### vs. 3.10.4

- Geometric mean: 1.228x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: 1.43x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sqlite_synth, subparsers
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-3.10.4.md)
- [📈time plot](bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.028x faster (HPT: reliability of 92.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlite_synth, subparsers
- [📄table](bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-3.12.0.md)
- [📈time plot](bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.031x faster (HPT: reliability of 99.51%, 1.00x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlite_synth, subparsers
- [📄table](bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-3.13.0.md)
- [📈time plot](bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.005x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-base-mem.svg)
- [📄table](bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-base.md)
- [📈time plot](bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1%2B-64b198a-vs-base.svg)

