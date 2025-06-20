# Results

- fork: faster-cpython/explicit_check_perio
- version: 3.15.0a0
- config: 
- commit hash: [494c825](https://github.com/faster%2dcpython/cpython/commit/494c825)
- commit date: 2025-06-20T11:24:58+01:00
- commit merge base: [7cc89496922b7edb033e2ed47550c7c9e2ae8525](https://github.com/python/cpython/commit/7cc89496922b7edb033e2ed47550c7c9e2ae8525)
- ref: explicit_check_perio

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15776874923)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250620-arminc-aarch64-faster%252dcpython-explicit_check_perio-3.15.0a0-494c825.json)

### vs. 3.10.4

- Geometric mean: 1.330x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.37x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250620-arminc-aarch64-faster%252dcpython-explicit_check_perio-3.15.0a0-494c825-vs-3.10.4.md)
- [📈time plot](bm-20250620-arminc-aarch64-faster%252dcpython-explicit_check_perio-3.15.0a0-494c825-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.049x faster (HPT: reliability of 99.78%, 1.00x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250620-arminc-aarch64-faster%252dcpython-explicit_check_perio-3.15.0a0-494c825-vs-3.12.0.md)
- [📈time plot](bm-20250620-arminc-aarch64-faster%252dcpython-explicit_check_perio-3.15.0a0-494c825-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.052x faster (HPT: reliability of 99.57%, 1.00x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250620-arminc-aarch64-faster%252dcpython-explicit_check_perio-3.15.0a0-494c825-vs-3.13.0.md)
- [📈time plot](bm-20250620-arminc-aarch64-faster%252dcpython-explicit_check_perio-3.15.0a0-494c825-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.005x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250620-arminc-aarch64-faster%252dcpython-explicit_check_perio-3.15.0a0-494c825-vs-base-mem.svg)
- [📄table](bm-20250620-arminc-aarch64-faster%252dcpython-explicit_check_perio-3.15.0a0-494c825-vs-base.md)
- [📈time plot](bm-20250620-arminc-aarch64-faster%252dcpython-explicit_check_perio-3.15.0a0-494c825-vs-base.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20250620-azure-x86_64-faster%252dcpython-explicit_check_perio-3.15.0a0-494c825-pystats.json)
- [pystats table](bm-20250620-azure-x86_64-faster%252dcpython-explicit_check_perio-3.15.0a0-494c825-pystats.md)

### vs. base

- [pystats diff](bm-20250620-azure-x86_64-faster%252dcpython-explicit_check_perio-3.15.0a0-494c825-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15776874923)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-216-generic-x86_64-with-glibc2.31
- [raw results](bm-20250620-linux-x86_64-faster%252dcpython-explicit_check_perio-3.15.0a0-494c825.json)

### vs. 3.10.4

- Geometric mean: 1.443x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250620-linux-x86_64-faster%252dcpython-explicit_check_perio-3.15.0a0-494c825-vs-3.10.4.md)
- [📈time plot](bm-20250620-linux-x86_64-faster%252dcpython-explicit_check_perio-3.15.0a0-494c825-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.109x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250620-linux-x86_64-faster%252dcpython-explicit_check_perio-3.15.0a0-494c825-vs-3.12.0.md)
- [📈time plot](bm-20250620-linux-x86_64-faster%252dcpython-explicit_check_perio-3.15.0a0-494c825-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.037x faster (HPT: reliability of 99.55%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250620-linux-x86_64-faster%252dcpython-explicit_check_perio-3.15.0a0-494c825-vs-3.13.0.md)
- [📈time plot](bm-20250620-linux-x86_64-faster%252dcpython-explicit_check_perio-3.15.0a0-494c825-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.004x slower (HPT: reliability of 94.24%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250620-linux-x86_64-faster%252dcpython-explicit_check_perio-3.15.0a0-494c825-vs-base-mem.svg)
- [📄table](bm-20250620-linux-x86_64-faster%252dcpython-explicit_check_perio-3.15.0a0-494c825-vs-base.md)
- [📈time plot](bm-20250620-linux-x86_64-faster%252dcpython-explicit_check_perio-3.15.0a0-494c825-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15776874923)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250620-pythonperf1-amd64-faster%252dcpython-explicit_check_perio-3.15.0a0-494c825.json)

### vs. 3.10.4

- Geometric mean: 1.262x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250620-pythonperf1-amd64-faster%252dcpython-explicit_check_perio-3.15.0a0-494c825-vs-3.10.4.md)
- [📈time plot](bm-20250620-pythonperf1-amd64-faster%252dcpython-explicit_check_perio-3.15.0a0-494c825-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.073x faster (HPT: reliability of 99.66%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250620-pythonperf1-amd64-faster%252dcpython-explicit_check_perio-3.15.0a0-494c825-vs-3.12.0.md)
- [📈time plot](bm-20250620-pythonperf1-amd64-faster%252dcpython-explicit_check_perio-3.15.0a0-494c825-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.045x faster (HPT: reliability of 99.36%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250620-pythonperf1-amd64-faster%252dcpython-explicit_check_perio-3.15.0a0-494c825-vs-3.13.0.md)
- [📈time plot](bm-20250620-pythonperf1-amd64-faster%252dcpython-explicit_check_perio-3.15.0a0-494c825-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.003x slower (HPT: reliability of 98.33%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250620-pythonperf1-amd64-faster%252dcpython-explicit_check_perio-3.15.0a0-494c825-vs-base.md)
- [📈time plot](bm-20250620-pythonperf1-amd64-faster%252dcpython-explicit_check_perio-3.15.0a0-494c825-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15776874923)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250620-darwin-arm64-faster%252dcpython-explicit_check_perio-3.15.0a0-494c825.json)

### vs. 3.10.4

- Geometric mean: 1.240x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250620-darwin-arm64-faster%252dcpython-explicit_check_perio-3.15.0a0-494c825-vs-3.10.4.md)
- [📈time plot](bm-20250620-darwin-arm64-faster%252dcpython-explicit_check_perio-3.15.0a0-494c825-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.021x slower (HPT: reliability of 98.89%, 1.00x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250620-darwin-arm64-faster%252dcpython-explicit_check_perio-3.15.0a0-494c825-vs-3.12.0.md)
- [📈time plot](bm-20250620-darwin-arm64-faster%252dcpython-explicit_check_perio-3.15.0a0-494c825-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.020x slower (HPT: reliability of 83.37%, 1.00x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250620-darwin-arm64-faster%252dcpython-explicit_check_perio-3.15.0a0-494c825-vs-3.13.0.md)
- [📈time plot](bm-20250620-darwin-arm64-faster%252dcpython-explicit_check_perio-3.15.0a0-494c825-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.007x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250620-darwin-arm64-faster%252dcpython-explicit_check_perio-3.15.0a0-494c825-vs-base-mem.svg)
- [📄table](bm-20250620-darwin-arm64-faster%252dcpython-explicit_check_perio-3.15.0a0-494c825-vs-base.md)
- [📈time plot](bm-20250620-darwin-arm64-faster%252dcpython-explicit_check_perio-3.15.0a0-494c825-vs-base.svg)

