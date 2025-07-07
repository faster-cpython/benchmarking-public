# Results

- fork: python/1953713d0d67a4f54ff7
- version: 3.15.0a0
- config: 
- commit hash: [1953713](https://github.com/python/cpython/commit/1953713)
- commit date: 2025-07-05T15:54:26-07:00
- commit merge base: [5dac137b9f75c5c1d5096101bcd33d565d0526e4](https://github.com/python/cpython/commit/5dac137b9f75c5c1d5096101bcd33d565d0526e4)
- ref: 1953713d0d67a4f54ff7

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16093257761)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250705-arminc-aarch64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json)

### vs. 3.10.4

- Geometric mean: 1.309x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.38x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250705-arminc-aarch64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.10.4.md)
- [📈time plot](bm-20250705-arminc-aarch64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.035x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250705-arminc-aarch64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.12.0.md)
- [📈time plot](bm-20250705-arminc-aarch64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.034x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250705-arminc-aarch64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.13.0.md)
- [📈time plot](bm-20250705-arminc-aarch64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.13.0.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20250705-azure-x86_64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-pystats.json)
- [pystats table](bm-20250705-azure-x86_64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-pystats.md)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16093257761)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20250705-pythonperf2-x86_64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json)

### vs. 3.10.4

- Geometric mean: 1.325x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.38x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250705-pythonperf2-x86_64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.10.4.md)
- [📈time plot](bm-20250705-pythonperf2-x86_64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.028x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250705-pythonperf2-x86_64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.12.0.md)
- [📈time plot](bm-20250705-pythonperf2-x86_64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.043x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250705-pythonperf2-x86_64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.13.0.md)
- [📈time plot](bm-20250705-pythonperf2-x86_64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16093257761)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json)

### vs. 3.10.4

- Geometric mean: 1.277x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.10.4.md)
- [📈time plot](bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.089x faster (HPT: reliability of 99.99%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.12.0.md)
- [📈time plot](bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.058x faster (HPT: reliability of 98.63%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.13.0.md)
- [📈time plot](bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.13.0.svg)

## windows amd64 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16093257761)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json)

### vs. 3.10.4

- Geometric mean: 1.450x faster (HPT: reliability of 100.00%, 1.35x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.10.4.md)
- [📈time plot](bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.467x faster (HPT: reliability of 100.00%, 1.42x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.12.0.md)
- [📈time plot](bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.281x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.13.0.md)
- [📈time plot](bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16093257761)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250705-darwin-arm64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json)

### vs. 3.10.4

- Geometric mean: 1.247x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250705-darwin-arm64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.10.4.md)
- [📈time plot](bm-20250705-darwin-arm64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.014x slower (HPT: reliability of 97.20%, 1.00x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250705-darwin-arm64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.12.0.md)
- [📈time plot](bm-20250705-darwin-arm64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.012x slower (HPT: reliability of 71.82%, 1.00x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250705-darwin-arm64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.13.0.md)
- [📈time plot](bm-20250705-darwin-arm64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713-vs-3.13.0.svg)

