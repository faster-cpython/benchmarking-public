# Results

- fork: brandtbucher
- version: 3.14.0a1+
- config: JIT
- commit hash: [15229e0](https://github.com/brandtbucher/cpython/commit/15229e0)
- commit date: 2024-10-17T16:34:26-07:00
- commit merge base: [d8c864816121547338efa43c56e3f75ead98a924](https://github.com/brandtbucher/cpython/commit/d8c864816121547338efa43c56e3f75ead98a924)
- ref: justin_unlikely

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11394692387)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0.json)

### vs. 3.10.4

- Geometric mean: 1.163x faster (HPT: reliability of 99.97%, 1.03x faster at 99th %ile)
- Memory usage: 1.37x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx, unpack_sequence
- [📄table](bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.10.4.md)
- [📈time plot](bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.086x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, sphinx, unpack_sequence
- [📄table](bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.12.0.md)
- [📈time plot](bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.095x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.13.0.md)
- [📈time plot](bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x slower (HPT: reliability of 78.65%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-base-mem.svg)
- [📄table](bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-base.md)
- [📈time plot](bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-base.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20241017-azure-x86_64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-pystats.json)
- [pystats table](bm-20241017-azure-x86_64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-pystats.md)

### vs. base

- [pystats diff](bm-20241017-azure-x86_64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11394692387)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0.json)

### vs. 3.10.4

- Geometric mean: 1.397x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.10.4.md)
- [📈time plot](bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.066x faster (HPT: reliability of 99.97%, 1.02x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.12.0.md)
- [📈time plot](bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.008x faster (HPT: reliability of 62.13%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.13.0.md)
- [📈time plot](bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x faster (HPT: reliability of 50.26%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-base-mem.svg)
- [📄table](bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-base.md)
- [📈time plot](bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11394692387)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0.json)

### vs. 3.10.4

- Geometric mean: 1.288x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.10.4.md)
- [📈time plot](bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.004x slower (HPT: reliability of 53.12%, 1.00x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.12.0.md)
- [📈time plot](bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.001x slower (HPT: reliability of 53.06%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.13.0.md)
- [📈time plot](bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.006x faster (HPT: reliability of 99.96%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-base-mem.svg)
- [📄table](bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-base.md)
- [📈time plot](bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11394692387)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0.json)

### vs. 3.10.4

- Geometric mean: 1.194x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx
- [📄table](bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.10.4.md)
- [📈time plot](bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.010x faster (HPT: reliability of 73.08%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.12.0.md)
- [📈time plot](bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.012x slower (HPT: reliability of 99.75%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.13.0.md)
- [📈time plot](bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x slower (HPT: reliability of 95.78%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-base.md)
- [📈time plot](bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11394692387)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0.json)

### vs. 3.10.4

- Geometric mean: 1.191x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx
- [📄table](bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.10.4.md)
- [📈time plot](bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.201x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.12.0.md)
- [📈time plot](bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.075x faster (HPT: reliability of 72.40%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.13.0.md)
- [📈time plot](bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.005x faster (HPT: reliability of 93.41%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-base.md)
- [📈time plot](bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11394692387)
- cpu model: missing
- platform: macOS-15.0.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0.json)

### vs. 3.10.4

- Geometric mean: 1.217x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: 1.43x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.10.4.md)
- [📈time plot](bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.032x faster (HPT: reliability of 96.43%, 1.00x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.12.0.md)
- [📈time plot](bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.035x faster (HPT: reliability of 98.99%, 1.00x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.13.0.md)
- [📈time plot](bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x slower (HPT: reliability of 96.17%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-base-mem.svg)
- [📄table](bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-base.md)
- [📈time plot](bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1%2B-15229e0-vs-base.svg)

