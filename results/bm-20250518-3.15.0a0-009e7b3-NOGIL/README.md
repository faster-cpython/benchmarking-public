# Results

- fork: python/009e7b36981fd07f7cca
- version: 3.15.0a0
- config: NOGIL
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

- Geometric mean: 1.180x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.64x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-vs-3.10.4.md)
- [📈time plot](bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.057x slower (HPT: reliability of 99.77%, 1.01x slower at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-vs-3.12.0.md)
- [📈time plot](bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.064x slower (HPT: reliability of 99.91%, 1.02x slower at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-vs-3.13.0.md)
- [📈time plot](bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.052x slower (HPT: reliability of 100.00%, 1.09x slower at 99th %ile)
- Memory usage: 1.22x
- [🧠memory plot](bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-vs-base-mem.svg)
- [📄table](bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-vs-base.md)
- [📈time plot](bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15090293379)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json)

### vs. 3.10.4

- Geometric mean: 1.313x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 1.58x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-vs-3.10.4.md)
- [📈time plot](bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.024x faster (HPT: reliability of 68.90%, 1.00x slower at 99th %ile)
- Memory usage: 1.37x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-vs-3.12.0.md)
- [📈time plot](bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.045x slower (HPT: reliability of 99.73%, 1.01x slower at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-vs-3.13.0.md)
- [📈time plot](bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.008x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: 🔴 dask
- [🧠memory plot](bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-vs-base-mem.svg)
- [📄table](bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-vs-base.md)
- [📈time plot](bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15090293379)
- cpu model: missing
- platform: macOS-15.4.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json)

### vs. 3.10.4

- Geometric mean: 1.191x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-vs-3.10.4.md)
- [📈time plot](bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.053x slower (HPT: reliability of 99.04%, 1.00x slower at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-vs-3.12.0.md)
- [📈time plot](bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.051x slower (HPT: reliability of 99.67%, 1.00x slower at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-vs-3.13.0.md)
- [📈time plot](bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.056x faster (HPT: reliability of 95.37%, 1.00x slower at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: 🔴 dask
- [🧠memory plot](bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-vs-base-mem.svg)
- [📄table](bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-vs-base.md)
- [📈time plot](bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3-vs-base.svg)

