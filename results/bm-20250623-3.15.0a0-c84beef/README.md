# Results

- fork: faster-cpython/explicit_check_perio
- version: 3.15.0a0
- config: 
- commit hash: [c84beef](https://github.com/faster%2dcpython/cpython/commit/c84beef)
- commit date: 2025-06-23T11:40:38+01:00
- commit merge base: [7cc89496922b7edb033e2ed47550c7c9e2ae8525](https://github.com/python/cpython/commit/7cc89496922b7edb033e2ed47550c7c9e2ae8525)
- ref: explicit_check_perio

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15822102952)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250623-arminc-aarch64-faster%252dcpython-explicit_check_perio-3.15.0a0-c84beef.json)

### vs. 3.10.4

- Geometric mean: 1.351x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.37x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250623-arminc-aarch64-faster%252dcpython-explicit_check_perio-3.15.0a0-c84beef-vs-3.10.4.md)
- [📈time plot](bm-20250623-arminc-aarch64-faster%252dcpython-explicit_check_perio-3.15.0a0-c84beef-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.065x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250623-arminc-aarch64-faster%252dcpython-explicit_check_perio-3.15.0a0-c84beef-vs-3.12.0.md)
- [📈time plot](bm-20250623-arminc-aarch64-faster%252dcpython-explicit_check_perio-3.15.0a0-c84beef-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.065x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250623-arminc-aarch64-faster%252dcpython-explicit_check_perio-3.15.0a0-c84beef-vs-3.13.0.md)
- [📈time plot](bm-20250623-arminc-aarch64-faster%252dcpython-explicit_check_perio-3.15.0a0-c84beef-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x slower (HPT: reliability of 52.37%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250623-arminc-aarch64-faster%252dcpython-explicit_check_perio-3.15.0a0-c84beef-vs-base-mem.svg)
- [📄table](bm-20250623-arminc-aarch64-faster%252dcpython-explicit_check_perio-3.15.0a0-c84beef-vs-base.md)
- [📈time plot](bm-20250623-arminc-aarch64-faster%252dcpython-explicit_check_perio-3.15.0a0-c84beef-vs-base.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20250623-azure-x86_64-faster%252dcpython-explicit_check_perio-3.15.0a0-c84beef-pystats.json)
- [pystats table](bm-20250623-azure-x86_64-faster%252dcpython-explicit_check_perio-3.15.0a0-c84beef-pystats.md)

### vs. base

- [pystats diff](bm-20250623-azure-x86_64-faster%252dcpython-explicit_check_perio-3.15.0a0-c84beef-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15822102952)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-216-generic-x86_64-with-glibc2.31
- [raw results](bm-20250623-linux-x86_64-faster%252dcpython-explicit_check_perio-3.15.0a0-c84beef.json)

### vs. 3.10.4

- Geometric mean: 1.449x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250623-linux-x86_64-faster%252dcpython-explicit_check_perio-3.15.0a0-c84beef-vs-3.10.4.md)
- [📈time plot](bm-20250623-linux-x86_64-faster%252dcpython-explicit_check_perio-3.15.0a0-c84beef-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.113x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250623-linux-x86_64-faster%252dcpython-explicit_check_perio-3.15.0a0-c84beef-vs-3.12.0.md)
- [📈time plot](bm-20250623-linux-x86_64-faster%252dcpython-explicit_check_perio-3.15.0a0-c84beef-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.040x faster (HPT: reliability of 99.85%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250623-linux-x86_64-faster%252dcpython-explicit_check_perio-3.15.0a0-c84beef-vs-3.13.0.md)
- [📈time plot](bm-20250623-linux-x86_64-faster%252dcpython-explicit_check_perio-3.15.0a0-c84beef-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.003x faster (HPT: reliability of 57.38%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250623-linux-x86_64-faster%252dcpython-explicit_check_perio-3.15.0a0-c84beef-vs-base-mem.svg)
- [📄table](bm-20250623-linux-x86_64-faster%252dcpython-explicit_check_perio-3.15.0a0-c84beef-vs-base.md)
- [📈time plot](bm-20250623-linux-x86_64-faster%252dcpython-explicit_check_perio-3.15.0a0-c84beef-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15822102952)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250623-pythonperf1-amd64-faster%252dcpython-explicit_check_perio-3.15.0a0-c84beef.json)

### vs. 3.10.4

- Geometric mean: 1.243x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250623-pythonperf1-amd64-faster%252dcpython-explicit_check_perio-3.15.0a0-c84beef-vs-3.10.4.md)
- [📈time plot](bm-20250623-pythonperf1-amd64-faster%252dcpython-explicit_check_perio-3.15.0a0-c84beef-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.058x faster (HPT: reliability of 93.51%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250623-pythonperf1-amd64-faster%252dcpython-explicit_check_perio-3.15.0a0-c84beef-vs-3.12.0.md)
- [📈time plot](bm-20250623-pythonperf1-amd64-faster%252dcpython-explicit_check_perio-3.15.0a0-c84beef-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.028x faster (HPT: reliability of 99.51%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250623-pythonperf1-amd64-faster%252dcpython-explicit_check_perio-3.15.0a0-c84beef-vs-3.13.0.md)
- [📈time plot](bm-20250623-pythonperf1-amd64-faster%252dcpython-explicit_check_perio-3.15.0a0-c84beef-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.020x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250623-pythonperf1-amd64-faster%252dcpython-explicit_check_perio-3.15.0a0-c84beef-vs-base.md)
- [📈time plot](bm-20250623-pythonperf1-amd64-faster%252dcpython-explicit_check_perio-3.15.0a0-c84beef-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15822102952)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250623-darwin-arm64-faster%252dcpython-explicit_check_perio-3.15.0a0-c84beef.json)

### vs. 3.10.4

- Geometric mean: 1.247x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250623-darwin-arm64-faster%252dcpython-explicit_check_perio-3.15.0a0-c84beef-vs-3.10.4.md)
- [📈time plot](bm-20250623-darwin-arm64-faster%252dcpython-explicit_check_perio-3.15.0a0-c84beef-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.016x slower (HPT: reliability of 95.26%, 1.00x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250623-darwin-arm64-faster%252dcpython-explicit_check_perio-3.15.0a0-c84beef-vs-3.12.0.md)
- [📈time plot](bm-20250623-darwin-arm64-faster%252dcpython-explicit_check_perio-3.15.0a0-c84beef-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.014x slower (HPT: reliability of 71.87%, 1.00x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250623-darwin-arm64-faster%252dcpython-explicit_check_perio-3.15.0a0-c84beef-vs-3.13.0.md)
- [📈time plot](bm-20250623-darwin-arm64-faster%252dcpython-explicit_check_perio-3.15.0a0-c84beef-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.003x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250623-darwin-arm64-faster%252dcpython-explicit_check_perio-3.15.0a0-c84beef-vs-base-mem.svg)
- [📄table](bm-20250623-darwin-arm64-faster%252dcpython-explicit_check_perio-3.15.0a0-c84beef-vs-base.md)
- [📈time plot](bm-20250623-darwin-arm64-faster%252dcpython-explicit_check_perio-3.15.0a0-c84beef-vs-base.svg)

