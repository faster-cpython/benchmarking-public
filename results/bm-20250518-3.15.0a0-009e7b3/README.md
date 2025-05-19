# Results

- fork: python/009e7b36981fd07f7cca
- version: 3.15.0a0
- config: 
- commit hash: [009e7b3](https://github.com/python/cpython/commit/009e7b3)
- commit date: 2025-05-18T00:24:40+02:00
- commit merge base: [fc7f4c36664314393bd4c30355e21bd7aeac524d](https://github.com/python/cpython/commit/fc7f4c36664314393bd4c30355e21bd7aeac524d)
- ref: 009e7b36981fd07f7cca

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15090293379)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json)

### vs. 3.10.4

- Geometric mean: 1.229x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-vs-3.10.4.md)
- [📈time plot](bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.028x slower (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-vs-3.12.0.md)
- [📈time plot](bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.021x slower (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-vs-3.13.0.md)
- [📈time plot](bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-vs-3.13.0.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20250518-azure-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-pystats.json)
- [pystats table](bm-20250518-azure-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15090293379)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json)

### vs. 3.10.4

- Geometric mean: 1.299x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-vs-3.10.4.md)
- [📈time plot](bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.073x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-vs-3.12.0.md)
- [📈time plot](bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.039x slower (HPT: reliability of 98.71%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, asyncio_tcp, asyncio_tcp_ssl, dask, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-vs-3.13.0.md)
- [📈time plot](bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15090293379)
- cpu model: missing
- platform: macOS-15.4.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json)

### vs. 3.10.4

- Geometric mean: 1.124x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-vs-3.10.4.md)
- [📈time plot](bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.107x slower (HPT: reliability of 99.96%, 1.01x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-vs-3.12.0.md)
- [📈time plot](bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.105x slower (HPT: reliability of 98.53%, 1.00x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-vs-3.13.0.md)
- [📈time plot](bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-vs-3.13.0.svg)

