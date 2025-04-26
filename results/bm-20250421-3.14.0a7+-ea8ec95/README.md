# Results

- fork: python/ea8ec95cfadbf58a11ef
- version: 3.14.0a7+
- config: 
- commit hash: [ea8ec95](https://github.com/python/cpython/commit/ea8ec95)
- commit date: 2025-04-21T18:48:48+01:00
- commit merge base: [8516343d3aeb12e5871ecd1701649fd1fcf46fc0](https://github.com/python/cpython/commit/8516343d3aeb12e5871ecd1701649fd1fcf46fc0)
- ref: ea8ec95cfadbf58a11ef

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14673713067)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7%2B-ea8ec95.json)

### vs. 3.10.4

- Geometric mean: 1.348x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7%2B-ea8ec95-vs-3.10.4.md)
- [📈time plot](bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7%2B-ea8ec95-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.064x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7%2B-ea8ec95-vs-3.12.0.md)
- [📈time plot](bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7%2B-ea8ec95-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.063x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7%2B-ea8ec95-vs-3.13.0.md)
- [📈time plot](bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7%2B-ea8ec95-vs-3.13.0.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14673713067)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7%2B-ea8ec95.json)

### vs. 3.10.4

- Geometric mean: 1.453x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7%2B-ea8ec95-vs-3.10.4.md)
- [📈time plot](bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7%2B-ea8ec95-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.119x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7%2B-ea8ec95-vs-3.12.0.md)
- [📈time plot](bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7%2B-ea8ec95-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.049x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7%2B-ea8ec95-vs-3.13.0.md)
- [📈time plot](bm-20250421-linux-x86_64-python-ea8ec95cfadbf58a11ef-3.14.0a7%2B-ea8ec95-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14673713067)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250421-pythonperf1-amd64-python-ea8ec95cfadbf58a11ef-3.14.0a7%2B-ea8ec95.json)

### vs. 3.10.4

- Geometric mean: 1.292x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250421-pythonperf1-amd64-python-ea8ec95cfadbf58a11ef-3.14.0a7%2B-ea8ec95-vs-3.10.4.md)
- [📈time plot](bm-20250421-pythonperf1-amd64-python-ea8ec95cfadbf58a11ef-3.14.0a7%2B-ea8ec95-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.100x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250421-pythonperf1-amd64-python-ea8ec95cfadbf58a11ef-3.14.0a7%2B-ea8ec95-vs-3.12.0.md)
- [📈time plot](bm-20250421-pythonperf1-amd64-python-ea8ec95cfadbf58a11ef-3.14.0a7%2B-ea8ec95-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.035x faster (HPT: reliability of 78.16%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250421-pythonperf1-amd64-python-ea8ec95cfadbf58a11ef-3.14.0a7%2B-ea8ec95-vs-3.13.0.md)
- [📈time plot](bm-20250421-pythonperf1-amd64-python-ea8ec95cfadbf58a11ef-3.14.0a7%2B-ea8ec95-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14673713067)
- cpu model: missing
- platform: macOS-15.4-arm64-arm-64bit-Mach-O
- [raw results](bm-20250421-darwin-arm64-python-ea8ec95cfadbf58a11ef-3.14.0a7%2B-ea8ec95.json)

### vs. 3.10.4

- Geometric mean: 1.214x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250421-darwin-arm64-python-ea8ec95cfadbf58a11ef-3.14.0a7%2B-ea8ec95-vs-3.10.4.md)
- [📈time plot](bm-20250421-darwin-arm64-python-ea8ec95cfadbf58a11ef-3.14.0a7%2B-ea8ec95-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.045x slower (HPT: reliability of 99.95%, 1.01x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250421-darwin-arm64-python-ea8ec95cfadbf58a11ef-3.14.0a7%2B-ea8ec95-vs-3.12.0.md)
- [📈time plot](bm-20250421-darwin-arm64-python-ea8ec95cfadbf58a11ef-3.14.0a7%2B-ea8ec95-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.043x slower (HPT: reliability of 98.01%, 1.00x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250421-darwin-arm64-python-ea8ec95cfadbf58a11ef-3.14.0a7%2B-ea8ec95-vs-3.13.0.md)
- [📈time plot](bm-20250421-darwin-arm64-python-ea8ec95cfadbf58a11ef-3.14.0a7%2B-ea8ec95-vs-3.13.0.svg)

