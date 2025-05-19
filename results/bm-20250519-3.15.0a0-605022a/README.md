# Results

- fork: python/605022aeb69ae19cae1c
- version: 3.15.0a0
- config: 
- commit hash: [605022a](https://github.com/python/cpython/commit/605022a)
- commit date: 2025-05-19T12:15:04+00:00
- commit merge base: [986c3670285670558b6e6f77ff1507dfcc2c99fa](https://github.com/python/cpython/commit/986c3670285670558b6e6f77ff1507dfcc2c99fa)
- ref: 605022aeb69ae19cae1c

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15115913369)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250519-arminc-aarch64-python-605022aeb69ae19cae1c-3.15.0a0-605022a.json)

### vs. 3.10.4

- Geometric mean: 1.221x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250519-arminc-aarch64-python-605022aeb69ae19cae1c-3.15.0a0-605022a-vs-3.10.4.md)
- [📈time plot](bm-20250519-arminc-aarch64-python-605022aeb69ae19cae1c-3.15.0a0-605022a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.033x slower (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250519-arminc-aarch64-python-605022aeb69ae19cae1c-3.15.0a0-605022a-vs-3.12.0.md)
- [📈time plot](bm-20250519-arminc-aarch64-python-605022aeb69ae19cae1c-3.15.0a0-605022a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.029x slower (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250519-arminc-aarch64-python-605022aeb69ae19cae1c-3.15.0a0-605022a-vs-3.13.0.md)
- [📈time plot](bm-20250519-arminc-aarch64-python-605022aeb69ae19cae1c-3.15.0a0-605022a-vs-3.13.0.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15115913369)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250519-linux-x86_64-python-605022aeb69ae19cae1c-3.15.0a0-605022a.json)

### vs. 3.10.4

- Geometric mean: 1.302x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250519-linux-x86_64-python-605022aeb69ae19cae1c-3.15.0a0-605022a-vs-3.10.4.md)
- [📈time plot](bm-20250519-linux-x86_64-python-605022aeb69ae19cae1c-3.15.0a0-605022a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.076x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250519-linux-x86_64-python-605022aeb69ae19cae1c-3.15.0a0-605022a-vs-3.12.0.md)
- [📈time plot](bm-20250519-linux-x86_64-python-605022aeb69ae19cae1c-3.15.0a0-605022a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.038x slower (HPT: reliability of 99.76%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, dask, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250519-linux-x86_64-python-605022aeb69ae19cae1c-3.15.0a0-605022a-vs-3.13.0.md)
- [📈time plot](bm-20250519-linux-x86_64-python-605022aeb69ae19cae1c-3.15.0a0-605022a-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15115913369)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250519-pythonperf1-amd64-python-605022aeb69ae19cae1c-3.15.0a0-605022a.json)

### vs. 3.10.4

- Geometric mean: 1.175x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250519-pythonperf1-amd64-python-605022aeb69ae19cae1c-3.15.0a0-605022a-vs-3.10.4.md)
- [📈time plot](bm-20250519-pythonperf1-amd64-python-605022aeb69ae19cae1c-3.15.0a0-605022a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.075x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250519-pythonperf1-amd64-python-605022aeb69ae19cae1c-3.15.0a0-605022a-vs-3.12.0.md)
- [📈time plot](bm-20250519-pythonperf1-amd64-python-605022aeb69ae19cae1c-3.15.0a0-605022a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.014x slower (HPT: reliability of 73.03%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250519-pythonperf1-amd64-python-605022aeb69ae19cae1c-3.15.0a0-605022a-vs-3.13.0.md)
- [📈time plot](bm-20250519-pythonperf1-amd64-python-605022aeb69ae19cae1c-3.15.0a0-605022a-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15115913369)
- cpu model: missing
- platform: macOS-15.4.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20250519-darwin-arm64-python-605022aeb69ae19cae1c-3.15.0a0-605022a.json)

### vs. 3.10.4

- Geometric mean: 1.124x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250519-darwin-arm64-python-605022aeb69ae19cae1c-3.15.0a0-605022a-vs-3.10.4.md)
- [📈time plot](bm-20250519-darwin-arm64-python-605022aeb69ae19cae1c-3.15.0a0-605022a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.106x slower (HPT: reliability of 99.94%, 1.01x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250519-darwin-arm64-python-605022aeb69ae19cae1c-3.15.0a0-605022a-vs-3.12.0.md)
- [📈time plot](bm-20250519-darwin-arm64-python-605022aeb69ae19cae1c-3.15.0a0-605022a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.105x slower (HPT: reliability of 98.61%, 1.00x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250519-darwin-arm64-python-605022aeb69ae19cae1c-3.15.0a0-605022a-vs-3.13.0.md)
- [📈time plot](bm-20250519-darwin-arm64-python-605022aeb69ae19cae1c-3.15.0a0-605022a-vs-3.13.0.svg)

