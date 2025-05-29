# Results

- fork: python/f6f4e8a6622d55664179
- version: 3.15.0a0
- config: 
- commit hash: [f6f4e8a](https://github.com/python/cpython/commit/f6f4e8a)
- commit date: 2025-05-27T15:59:45+01:00
- commit merge base: [9300a596d37d058e6e58d00a2ad70617c863a3de](https://github.com/python/cpython/commit/9300a596d37d058e6e58d00a2ad70617c863a3de)
- ref: f6f4e8a6622d55664179

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15295821692)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250527-arminc-aarch64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a.json)

### vs. 3.10.4

- Geometric mean: 1.229x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.35x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250527-arminc-aarch64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a-vs-3.10.4.md)
- [📈time plot](bm-20250527-arminc-aarch64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.027x slower (HPT: reliability of 99.99%, 1.02x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250527-arminc-aarch64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a-vs-3.12.0.md)
- [📈time plot](bm-20250527-arminc-aarch64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.021x slower (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250527-arminc-aarch64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a-vs-3.13.0.md)
- [📈time plot](bm-20250527-arminc-aarch64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a-vs-3.13.0.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20250527-azure-x86_64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a-pystats.json)
- [pystats table](bm-20250527-azure-x86_64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15295821692)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250527-linux-x86_64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a.json)

### vs. 3.10.4

- Geometric mean: 1.304x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250527-linux-x86_64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a-vs-3.10.4.md)
- [📈time plot](bm-20250527-linux-x86_64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.077x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250527-linux-x86_64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a-vs-3.12.0.md)
- [📈time plot](bm-20250527-linux-x86_64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.037x slower (HPT: reliability of 99.60%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, dask, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250527-linux-x86_64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a-vs-3.13.0.md)
- [📈time plot](bm-20250527-linux-x86_64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15295821692)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250527-pythonperf1-amd64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a.json)

### vs. 3.10.4

- Geometric mean: 1.162x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250527-pythonperf1-amd64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a-vs-3.10.4.md)
- [📈time plot](bm-20250527-pythonperf1-amd64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.061x faster (HPT: reliability of 99.95%, 1.01x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250527-pythonperf1-amd64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a-vs-3.12.0.md)
- [📈time plot](bm-20250527-pythonperf1-amd64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.025x slower (HPT: reliability of 96.14%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250527-pythonperf1-amd64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a-vs-3.13.0.md)
- [📈time plot](bm-20250527-pythonperf1-amd64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15295821692)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250527-darwin-arm64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a.json)

### vs. 3.10.4

- Geometric mean: 1.151x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250527-darwin-arm64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a-vs-3.10.4.md)
- [📈time plot](bm-20250527-darwin-arm64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.086x slower (HPT: reliability of 98.98%, 1.00x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250527-darwin-arm64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a-vs-3.12.0.md)
- [📈time plot](bm-20250527-darwin-arm64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.084x slower (HPT: reliability of 90.18%, 1.00x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250527-darwin-arm64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a-vs-3.13.0.md)
- [📈time plot](bm-20250527-darwin-arm64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a-vs-3.13.0.svg)

