# Results

- fork: faster-cpython/explicit_check_perio
- version: 3.15.0a0
- config: 
- commit hash: [be0ebdc](https://github.com/faster%2dcpython/cpython/commit/be0ebdc)
- commit date: 2025-06-20T18:48:55+01:00
- commit merge base: [7cc89496922b7edb033e2ed47550c7c9e2ae8525](https://github.com/python/cpython/commit/7cc89496922b7edb033e2ed47550c7c9e2ae8525)
- ref: explicit_check_perio

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15805029572)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250620-arminc-aarch64-faster%252dcpython-explicit_check_perio-3.15.0a0-be0ebdc.json)

### vs. 3.10.4

- Geometric mean: 1.342x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.37x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250620-arminc-aarch64-faster%252dcpython-explicit_check_perio-3.15.0a0-be0ebdc-vs-3.10.4.md)
- [📈time plot](bm-20250620-arminc-aarch64-faster%252dcpython-explicit_check_perio-3.15.0a0-be0ebdc-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.058x faster (HPT: reliability of 99.98%, 1.01x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250620-arminc-aarch64-faster%252dcpython-explicit_check_perio-3.15.0a0-be0ebdc-vs-3.12.0.md)
- [📈time plot](bm-20250620-arminc-aarch64-faster%252dcpython-explicit_check_perio-3.15.0a0-be0ebdc-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.058x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250620-arminc-aarch64-faster%252dcpython-explicit_check_perio-3.15.0a0-be0ebdc-vs-3.13.0.md)
- [📈time plot](bm-20250620-arminc-aarch64-faster%252dcpython-explicit_check_perio-3.15.0a0-be0ebdc-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.003x slower (HPT: reliability of 96.86%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250620-arminc-aarch64-faster%252dcpython-explicit_check_perio-3.15.0a0-be0ebdc-vs-base-mem.svg)
- [📄table](bm-20250620-arminc-aarch64-faster%252dcpython-explicit_check_perio-3.15.0a0-be0ebdc-vs-base.md)
- [📈time plot](bm-20250620-arminc-aarch64-faster%252dcpython-explicit_check_perio-3.15.0a0-be0ebdc-vs-base.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20250620-azure-x86_64-faster%252dcpython-explicit_check_perio-3.15.0a0-be0ebdc-pystats.json)
- [pystats table](bm-20250620-azure-x86_64-faster%252dcpython-explicit_check_perio-3.15.0a0-be0ebdc-pystats.md)

### vs. base

- [pystats diff](bm-20250620-azure-x86_64-faster%252dcpython-explicit_check_perio-3.15.0a0-be0ebdc-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15805029572)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-216-generic-x86_64-with-glibc2.31
- [raw results](bm-20250620-linux-x86_64-faster%252dcpython-explicit_check_perio-3.15.0a0-be0ebdc.json)

### vs. 3.10.4

- Geometric mean: 1.431x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250620-linux-x86_64-faster%252dcpython-explicit_check_perio-3.15.0a0-be0ebdc-vs-3.10.4.md)
- [📈time plot](bm-20250620-linux-x86_64-faster%252dcpython-explicit_check_perio-3.15.0a0-be0ebdc-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.100x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250620-linux-x86_64-faster%252dcpython-explicit_check_perio-3.15.0a0-be0ebdc-vs-3.12.0.md)
- [📈time plot](bm-20250620-linux-x86_64-faster%252dcpython-explicit_check_perio-3.15.0a0-be0ebdc-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.028x faster (HPT: reliability of 95.64%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250620-linux-x86_64-faster%252dcpython-explicit_check_perio-3.15.0a0-be0ebdc-vs-3.13.0.md)
- [📈time plot](bm-20250620-linux-x86_64-faster%252dcpython-explicit_check_perio-3.15.0a0-be0ebdc-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.005x slower (HPT: reliability of 99.99%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250620-linux-x86_64-faster%252dcpython-explicit_check_perio-3.15.0a0-be0ebdc-vs-base-mem.svg)
- [📄table](bm-20250620-linux-x86_64-faster%252dcpython-explicit_check_perio-3.15.0a0-be0ebdc-vs-base.md)
- [📈time plot](bm-20250620-linux-x86_64-faster%252dcpython-explicit_check_perio-3.15.0a0-be0ebdc-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15805029572)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250620-pythonperf1-amd64-faster%252dcpython-explicit_check_perio-3.15.0a0-be0ebdc.json)

### vs. 3.10.4

- Geometric mean: 1.277x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250620-pythonperf1-amd64-faster%252dcpython-explicit_check_perio-3.15.0a0-be0ebdc-vs-3.10.4.md)
- [📈time plot](bm-20250620-pythonperf1-amd64-faster%252dcpython-explicit_check_perio-3.15.0a0-be0ebdc-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.089x faster (HPT: reliability of 99.98%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250620-pythonperf1-amd64-faster%252dcpython-explicit_check_perio-3.15.0a0-be0ebdc-vs-3.12.0.md)
- [📈time plot](bm-20250620-pythonperf1-amd64-faster%252dcpython-explicit_check_perio-3.15.0a0-be0ebdc-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.057x faster (HPT: reliability of 95.28%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250620-pythonperf1-amd64-faster%252dcpython-explicit_check_perio-3.15.0a0-be0ebdc-vs-3.13.0.md)
- [📈time plot](bm-20250620-pythonperf1-amd64-faster%252dcpython-explicit_check_perio-3.15.0a0-be0ebdc-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.003x slower (HPT: reliability of 97.62%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250620-pythonperf1-amd64-faster%252dcpython-explicit_check_perio-3.15.0a0-be0ebdc-vs-base.md)
- [📈time plot](bm-20250620-pythonperf1-amd64-faster%252dcpython-explicit_check_perio-3.15.0a0-be0ebdc-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15805029572)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250620-darwin-arm64-faster%252dcpython-explicit_check_perio-3.15.0a0-be0ebdc.json)

### vs. 3.10.4

- Geometric mean: 1.244x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250620-darwin-arm64-faster%252dcpython-explicit_check_perio-3.15.0a0-be0ebdc-vs-3.10.4.md)
- [📈time plot](bm-20250620-darwin-arm64-faster%252dcpython-explicit_check_perio-3.15.0a0-be0ebdc-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.018x slower (HPT: reliability of 97.98%, 1.00x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250620-darwin-arm64-faster%252dcpython-explicit_check_perio-3.15.0a0-be0ebdc-vs-3.12.0.md)
- [📈time plot](bm-20250620-darwin-arm64-faster%252dcpython-explicit_check_perio-3.15.0a0-be0ebdc-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.016x slower (HPT: reliability of 76.65%, 1.00x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250620-darwin-arm64-faster%252dcpython-explicit_check_perio-3.15.0a0-be0ebdc-vs-3.13.0.md)
- [📈time plot](bm-20250620-darwin-arm64-faster%252dcpython-explicit_check_perio-3.15.0a0-be0ebdc-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.004x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250620-darwin-arm64-faster%252dcpython-explicit_check_perio-3.15.0a0-be0ebdc-vs-base-mem.svg)
- [📄table](bm-20250620-darwin-arm64-faster%252dcpython-explicit_check_perio-3.15.0a0-be0ebdc-vs-base.md)
- [📈time plot](bm-20250620-darwin-arm64-faster%252dcpython-explicit_check_perio-3.15.0a0-be0ebdc-vs-base.svg)

