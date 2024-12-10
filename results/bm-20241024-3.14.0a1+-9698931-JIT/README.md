# Results

- fork: brandtbucher/justin_no_externs
- version: 3.14.0a1+
- config: JIT
- commit hash: [9698931](https://github.com/brandtbucher/cpython/commit/9698931)
- commit date: 2024-10-24T23:54:12-07:00
- commit merge base: [34653bba644aa5481613f398153757d7357e39ea](https://github.com/python/cpython/commit/34653bba644aa5481613f398153757d7357e39ea)
- ref: justin_no_externs

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11513820912)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241024-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931.json)

### vs. 3.10.4

- Geometric mean: 1.117x faster (HPT: reliability of 99.50%, 1.00x faster at 99th %ile)
- Memory usage: 1.38x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241024-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-3.10.4.md)
- [📈time plot](bm-20241024-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.123x slower (HPT: reliability of 100.00%, 1.08x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, sphinx
- [📄table](bm-20241024-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-3.12.0.md)
- [📈time plot](bm-20241024-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.132x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlite_synth, subparsers
- new benchmarks: dulwich_log
- [📄table](bm-20241024-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-3.13.0.md)
- [📈time plot](bm-20241024-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.040x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20241024-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-base-mem.svg)
- [📄table](bm-20241024-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-base.md)
- [📈time plot](bm-20241024-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-base.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20241024-azure-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-pystats.json)
- [pystats table](bm-20241024-azure-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-pystats.md)

### vs. base

- [pystats diff](bm-20241024-azure-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11513820912)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241024-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931.json)

### vs. 3.10.4

- Geometric mean: 1.267x faster (HPT: reliability of 100.00%, 1.15x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241024-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-3.10.4.md)
- [📈time plot](bm-20241024-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.034x slower (HPT: reliability of 99.95%, 1.00x slower at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241024-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-3.12.0.md)
- [📈time plot](bm-20241024-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.085x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlite_synth, subparsers
- [📄table](bm-20241024-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-3.13.0.md)
- [📈time plot](bm-20241024-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.086x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241024-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-base-mem.svg)
- [📄table](bm-20241024-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-base.md)
- [📈time plot](bm-20241024-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11513820912)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20241024-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931.json)

### vs. 3.10.4

- Geometric mean: 1.192x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241024-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-3.10.4.md)
- [📈time plot](bm-20241024-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.077x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241024-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-3.12.0.md)
- [📈time plot](bm-20241024-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.074x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlite_synth, subparsers
- [📄table](bm-20241024-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-3.13.0.md)
- [📈time plot](bm-20241024-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.063x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241024-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-base-mem.svg)
- [📄table](bm-20241024-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-base.md)
- [📈time plot](bm-20241024-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11513820912)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241024-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931.json)

### vs. 3.10.4

- Geometric mean: 1.133x faster (HPT: reliability of 99.99%, 1.03x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx
- [📄table](bm-20241024-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-3.10.4.md)
- [📈time plot](bm-20241024-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.041x slower (HPT: reliability of 97.27%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241024-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-3.12.0.md)
- [📈time plot](bm-20241024-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.060x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- [📄table](bm-20241024-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-3.13.0.md)
- [📈time plot](bm-20241024-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.054x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241024-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-base.md)
- [📈time plot](bm-20241024-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11513820912)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241024-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931.json)

### vs. 3.10.4

- Geometric mean: 1.112x faster (HPT: reliability of 99.99%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx
- [📄table](bm-20241024-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-3.10.4.md)
- [📈time plot](bm-20241024-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.123x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241024-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-3.12.0.md)
- [📈time plot](bm-20241024-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.007x faster (HPT: reliability of 99.95%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- [📄table](bm-20241024-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-3.13.0.md)
- [📈time plot](bm-20241024-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.055x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241024-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-base.md)
- [📈time plot](bm-20241024-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11513820912)
- cpu model: missing
- platform: macOS-15.0.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241024-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931.json)

### vs. 3.10.4

- Geometric mean: 1.201x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: 1.42x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241024-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-3.10.4.md)
- [📈time plot](bm-20241024-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.006x faster (HPT: reliability of 57.79%, 1.00x slower at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241024-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-3.12.0.md)
- [📈time plot](bm-20241024-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.010x faster (HPT: reliability of 58.96%, 1.00x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlite_synth, subparsers
- [📄table](bm-20241024-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-3.13.0.md)
- [📈time plot](bm-20241024-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.024x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241024-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-base-mem.svg)
- [📄table](bm-20241024-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-base.md)
- [📈time plot](bm-20241024-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1%2B-9698931-vs-base.svg)

