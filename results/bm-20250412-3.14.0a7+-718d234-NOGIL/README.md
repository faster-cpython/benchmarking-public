# Results

- fork: python/718d234e4086a65d78c8
- version: 3.14.0a7+
- config: NOGIL
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

- Geometric mean: 1.181x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.59x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.md)
- [📈time plot](bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.054x slower (HPT: reliability of 99.83%, 1.01x slower at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.md)
- [📈time plot](bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.063x slower (HPT: reliability of 99.84%, 1.02x slower at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.md)
- [📈time plot](bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.128x slower (HPT: reliability of 100.00%, 1.10x slower at 99th %ile)
- Memory usage: 1.20x
- [🧠memory plot](bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base-mem.svg)
- [📄table](bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.md)
- [📈time plot](bm-20250412-arminc-aarch64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14424474015)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234.json)

### vs. 3.10.4

- Geometric mean: 1.327x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 1.53x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.md)
- [📈time plot](bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.037x faster (HPT: reliability of 61.21%, 1.00x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.md)
- [📈time plot](bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.033x slower (HPT: reliability of 99.71%, 1.00x slower at 99th %ile)
- Memory usage: 1.23x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.md)
- [📈time plot](bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.087x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: 1.19x
- [🧠memory plot](bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base-mem.svg)
- [📄table](bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.md)
- [📈time plot](bm-20250412-linux-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14424474015)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234.json)

### vs. 3.10.4

- Geometric mean: 1.254x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: 1.55x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.md)
- [📈time plot](bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.011x slower (HPT: reliability of 96.08%, 1.00x slower at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.md)
- [📈time plot](bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.005x slower (HPT: reliability of 89.72%, 1.00x slower at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.md)
- [📈time plot](bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.081x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: 1.20x
- [🧠memory plot](bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base-mem.svg)
- [📄table](bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.md)
- [📈time plot](bm-20250412-pythonperf2-x86_64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14424474015)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234.json)

### vs. 3.10.4

- Geometric mean: 1.158x faster (HPT: reliability of 99.95%, 1.03x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.md)
- [📈time plot](bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.000x slower (HPT: reliability of 96.41%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.md)
- [📈time plot](bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.050x slower (HPT: reliability of 99.95%, 1.06x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.md)
- [📈time plot](bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.100x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: unknown
- new benchmarks: thrift
- [📄table](bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.md)
- [📈time plot](bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14424474015)
- cpu model: missing
- platform: macOS-15.4-arm64-arm-64bit-Mach-O
- [raw results](bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234.json)

### vs. 3.10.4

- Geometric mean: 1.213x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.md)
- [📈time plot](bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.032x slower (HPT: reliability of 98.76%, 1.00x slower at 99th %ile)
- Memory usage: 1.23x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.md)
- [📈time plot](bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.030x slower (HPT: reliability of 97.37%, 1.00x slower at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.md)
- [📈time plot](bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.003x faster (HPT: reliability of 79.20%, 1.00x slower at 99th %ile)
- Memory usage: 1.14x
- [🧠memory plot](bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base-mem.svg)
- [📄table](bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.md)
- [📈time plot](bm-20250412-darwin-arm64-python-718d234e4086a65d78c8-3.14.0a7%2B-718d234-vs-base.svg)

