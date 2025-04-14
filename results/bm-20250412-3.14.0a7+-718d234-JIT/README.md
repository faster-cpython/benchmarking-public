# Results

- fork: python/718d234e4086a65d78c8
- version: 3.14.0a7+
- config: JIT
- commit hash: [718d234](https://github.com/python/cpython/commit/718d234)
- commit date: 2025-04-12T22:35:28+00:00
- commit merge base: [f2f86d3f459a89273ea22389bb57eed402908302](https://github.com/python/cpython/commit/f2f86d3f459a89273ea22389bb57eed402908302)
- ref: 718d234e4086a65d78c8

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14424474015)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234.json)

### vs. 3.10.4

- Geometric mean: 1.318x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.md)
- [📈time plot](bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.041x faster (HPT: reliability of 99.12%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.md)
- [📈time plot](bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.043x faster (HPT: reliability of 96.62%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.md)
- [📈time plot](bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.025x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base-mem.svg)
- [📄table](bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.md)
- [📈time plot](bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14424474015)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234.json)

### vs. 3.10.4

- Geometric mean: 1.468x faster (HPT: reliability of 100.00%, 1.33x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.md)
- [📈time plot](bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.132x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.md)
- [📈time plot](bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.059x faster (HPT: reliability of 99.94%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.md)
- [📈time plot](bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x faster (HPT: reliability of 99.43%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base-mem.svg)
- [📄table](bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.md)
- [📈time plot](bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14424474015)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234.json)

### vs. 3.10.4

- Geometric mean: 1.368x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.md)
- [📈time plot](bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.064x faster (HPT: reliability of 99.89%, 1.02x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.md)
- [📈time plot](bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.075x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.md)
- [📈time plot](bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.004x slower (HPT: reliability of 94.81%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base-mem.svg)
- [📄table](bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.md)
- [📈time plot](bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14424474015)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234.json)

### vs. 3.10.4

- Geometric mean: 1.292x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.md)
- [📈time plot](bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.101x faster (HPT: reliability of 99.99%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.md)
- [📈time plot](bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.035x faster (HPT: reliability of 62.46%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.md)
- [📈time plot](bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.013x faster (HPT: reliability of 93.52%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.md)
- [📈time plot](bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14424474015)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250412-pythonperf1_win32-x86-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234.json)

### vs. 3.10.4

- Geometric mean: 1.079x faster (HPT: reliability of 97.69%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250412-pythonperf1_win32-x86-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.md)
- [📈time plot](bm-20250412-pythonperf1_win32-x86-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.102x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250412-pythonperf1_win32-x86-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.md)
- [📈time plot](bm-20250412-pythonperf1_win32-x86-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.057x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250412-pythonperf1_win32-x86-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.md)
- [📈time plot](bm-20250412-pythonperf1_win32-x86-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.071x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250412-pythonperf1_win32-x86-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.md)
- [📈time plot](bm-20250412-pythonperf1_win32-x86-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14424474015)
- cpu model: missing
- platform: macOS-15.4-arm64-arm-64bit-Mach-O
- [raw results](bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234.json)

### vs. 3.10.4

- Geometric mean: 1.399x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.md)
- [📈time plot](bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.099x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.md)
- [📈time plot](bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.101x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.md)
- [📈time plot](bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.143x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base-mem.svg)
- [📄table](bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.md)
- [📈time plot](bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.svg)

