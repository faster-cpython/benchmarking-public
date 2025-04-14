# Results

- fork: brandtbucher/justin_mcmodel_again
- version: 3.14.0a4+
- config: JIT
- commit hash: [86ef9a1](https://github.com/brandtbucher/cpython/commit/86ef9a1)
- commit date: 2025-02-12T17:40:38-08:00
- commit merge base: [f72977b2f4a29063ae3019e50360f4af869f4149](https://github.com/python/cpython/commit/f72977b2f4a29063ae3019e50360f4af869f4149)
- ref: justin_mcmodel_again

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13298795568)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250212-arminc-aarch64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1.json)

### vs. 3.10.4

- Geometric mean: 1.266x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250212-arminc-aarch64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-3.10.4.md)
- [📈time plot](bm-20250212-arminc-aarch64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.003x slower (HPT: reliability of 67.02%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250212-arminc-aarch64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-3.12.0.md)
- [📈time plot](bm-20250212-arminc-aarch64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.004x slower (HPT: reliability of 69.38%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20250212-arminc-aarch64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-3.13.0.md)
- [📈time plot](bm-20250212-arminc-aarch64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x faster (HPT: reliability of 99.46%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250212-arminc-aarch64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-base-mem.svg)
- [📄table](bm-20250212-arminc-aarch64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-base.md)
- [📈time plot](bm-20250212-arminc-aarch64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13298795568)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250212-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1.json)

### vs. 3.10.4

- Geometric mean: 1.462x faster (HPT: reliability of 100.00%, 1.32x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250212-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-3.10.4.md)
- [📈time plot](bm-20250212-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.123x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250212-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-3.12.0.md)
- [📈time plot](bm-20250212-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.053x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250212-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-3.13.0.md)
- [📈time plot](bm-20250212-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.007x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250212-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-base-mem.svg)
- [📄table](bm-20250212-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-base.md)
- [📈time plot](bm-20250212-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13298795568)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250212-pythonperf2-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1.json)

### vs. 3.10.4

- Geometric mean: 1.341x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250212-pythonperf2-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-3.10.4.md)
- [📈time plot](bm-20250212-pythonperf2-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.039x faster (HPT: reliability of 99.35%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250212-pythonperf2-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-3.12.0.md)
- [📈time plot](bm-20250212-pythonperf2-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.053x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250212-pythonperf2-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-3.13.0.md)
- [📈time plot](bm-20250212-pythonperf2-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.010x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250212-pythonperf2-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-base-mem.svg)
- [📄table](bm-20250212-pythonperf2-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-base.md)
- [📈time plot](bm-20250212-pythonperf2-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13298795568)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250212-pythonperf1-amd64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1.json)

### vs. 3.10.4

- Geometric mean: 1.220x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250212-pythonperf1-amd64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-3.10.4.md)
- [📈time plot](bm-20250212-pythonperf1-amd64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.034x faster (HPT: reliability of 57.95%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250212-pythonperf1-amd64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-3.12.0.md)
- [📈time plot](bm-20250212-pythonperf1-amd64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.003x faster (HPT: reliability of 96.81%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250212-pythonperf1-amd64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-3.13.0.md)
- [📈time plot](bm-20250212-pythonperf1-amd64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.031x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250212-pythonperf1-amd64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-base.md)
- [📈time plot](bm-20250212-pythonperf1-amd64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13298795568)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250212-pythonperf1_win32-x86-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1.json)

### vs. 3.10.4

- Geometric mean: 1.083x faster (HPT: reliability of 93.90%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250212-pythonperf1_win32-x86-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-3.10.4.md)
- [📈time plot](bm-20250212-pythonperf1_win32-x86-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.090x faster (HPT: reliability of 99.96%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250212-pythonperf1_win32-x86-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-3.12.0.md)
- [📈time plot](bm-20250212-pythonperf1_win32-x86-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.034x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250212-pythonperf1_win32-x86-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-3.13.0.md)
- [📈time plot](bm-20250212-pythonperf1_win32-x86-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x faster (HPT: reliability of 74.21%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250212-pythonperf1_win32-x86-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-base.md)
- [📈time plot](bm-20250212-pythonperf1_win32-x86-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13298795568)
- cpu model: missing
- platform: macOS-15.3-arm64-arm-64bit-Mach-O
- [raw results](bm-20250212-darwin-arm64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1.json)

### vs. 3.10.4

- Geometric mean: 1.371x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: chameleon, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20250212-darwin-arm64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-3.10.4.md)
- [📈time plot](bm-20250212-darwin-arm64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.077x faster (HPT: reliability of 99.85%, 1.00x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250212-darwin-arm64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-3.12.0.md)
- [📈time plot](bm-20250212-darwin-arm64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.080x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250212-darwin-arm64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-3.13.0.md)
- [📈time plot](bm-20250212-darwin-arm64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250212-darwin-arm64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-base-mem.svg)
- [📄table](bm-20250212-darwin-arm64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-base.md)
- [📈time plot](bm-20250212-darwin-arm64-brandtbucher-justin_mcmodel_again-3.14.0a4%2B-86ef9a1-vs-base.svg)

