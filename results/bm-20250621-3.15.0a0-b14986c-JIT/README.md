# Results

- fork: python/b14986c91464b06e9016
- version: 3.15.0a0
- config: JIT
- commit hash: [b14986c](https://github.com/python/cpython/commit/b14986c)
- commit date: 2025-06-21T22:03:17+05:30
- commit merge base: [6a16b3c440cf9ecabecd3e90f44310e3b0765780](https://github.com/python/cpython/commit/6a16b3c440cf9ecabecd3e90f44310e3b0765780)
- ref: b14986c91464b06e9016

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15800872473)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250621-arminc-aarch64-python-b14986c91464b06e9016-3.15.0a0-b14986c.json)

### vs. 3.10.4

- Geometric mean: 1.058x faster (HPT: reliability of 98.72%, 1.00x faster at 99th %ile)
- Memory usage: 1.40x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250621-arminc-aarch64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.10.4.md)
- [📈time plot](bm-20250621-arminc-aarch64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.163x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250621-arminc-aarch64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.12.0.md)
- [📈time plot](bm-20250621-arminc-aarch64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.155x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250621-arminc-aarch64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.13.0.md)
- [📈time plot](bm-20250621-arminc-aarch64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.017x faster (HPT: reliability of 99.42%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [🧠memory plot](bm-20250621-arminc-aarch64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-base-mem.svg)
- [📄table](bm-20250621-arminc-aarch64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-base.md)
- [📈time plot](bm-20250621-arminc-aarch64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15800872473)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-216-generic-x86_64-with-glibc2.31
- [raw results](bm-20250621-linux-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c.json)

### vs. 3.10.4

- Geometric mean: 1.270x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250621-linux-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.10.4.md)
- [📈time plot](bm-20250621-linux-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.019x slower (HPT: reliability of 67.75%, 1.00x slower at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250621-linux-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.12.0.md)
- [📈time plot](bm-20250621-linux-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.079x slower (HPT: reliability of 99.98%, 1.03x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250621-linux-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.13.0.md)
- [📈time plot](bm-20250621-linux-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.015x faster (HPT: reliability of 85.62%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [🧠memory plot](bm-20250621-linux-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-base-mem.svg)
- [📄table](bm-20250621-linux-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-base.md)
- [📈time plot](bm-20250621-linux-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15800872473)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20250621-pythonperf2-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c.json)

### vs. 3.10.4

- Geometric mean: 1.134x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.40x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250621-pythonperf2-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.10.4.md)
- [📈time plot](bm-20250621-pythonperf2-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.120x slower (HPT: reliability of 99.89%, 1.02x slower at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250621-pythonperf2-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.12.0.md)
- [📈time plot](bm-20250621-pythonperf2-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.099x slower (HPT: reliability of 99.91%, 1.02x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250621-pythonperf2-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.13.0.md)
- [📈time plot](bm-20250621-pythonperf2-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.13.0.svg)

### vs. base

- [🧠memory plot](bm-20250621-pythonperf2-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-base-mem.svg)
- [📄table](bm-20250621-pythonperf2-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-base.md)
- [📈time plot](bm-20250621-pythonperf2-x86_64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15909412358)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250621-pythonperf1-amd64-python-b14986c91464b06e9016-3.15.0a0-b14986c.json)

### vs. 3.10.4

- Geometric mean: 1.073x slower (HPT: reliability of 99.82%, 1.02x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250621-pythonperf1-amd64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.10.4.md)
- [📈time plot](bm-20250621-pythonperf1-amd64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.205x slower (HPT: reliability of 99.98%, 1.12x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250621-pythonperf1-amd64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.12.0.md)
- [📈time plot](bm-20250621-pythonperf1-amd64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.212x slower (HPT: reliability of 100.00%, 1.14x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250621-pythonperf1-amd64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.13.0.md)
- [📈time plot](bm-20250621-pythonperf1-amd64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.084x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250621-pythonperf1-amd64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-base.md)
- [📈time plot](bm-20250621-pythonperf1-amd64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-base.svg)

## windows amd64 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15800872473)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250621-pythonperf1_win32-amd64-python-b14986c91464b06e9016-3.15.0a0-b14986c.json)

### vs. 3.10.4

- Geometric mean: 1.040x faster (HPT: reliability of 53.92%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250621-pythonperf1_win32-amd64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.10.4.md)
- [📈time plot](bm-20250621-pythonperf1_win32-amd64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.058x faster (HPT: reliability of 99.73%, 1.01x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250621-pythonperf1_win32-amd64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.12.0.md)
- [📈time plot](bm-20250621-pythonperf1_win32-amd64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.056x slower (HPT: reliability of 99.94%, 1.03x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250621-pythonperf1_win32-amd64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.13.0.md)
- [📈time plot](bm-20250621-pythonperf1_win32-amd64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.13.0.svg)

### vs. base

- [📄table](bm-20250621-pythonperf1_win32-amd64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-base.md)
- [📈time plot](bm-20250621-pythonperf1_win32-amd64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15909412358)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250621-darwin-arm64-python-b14986c91464b06e9016-3.15.0a0-b14986c.json)

### vs. 3.10.4

- Geometric mean: 1.211x faster (HPT: reliability of 99.99%, 1.05x faster at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250621-darwin-arm64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.10.4.md)
- [📈time plot](bm-20250621-darwin-arm64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.036x slower (HPT: reliability of 99.67%, 1.00x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250621-darwin-arm64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.12.0.md)
- [📈time plot](bm-20250621-darwin-arm64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.034x slower (HPT: reliability of 94.63%, 1.00x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250621-darwin-arm64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.13.0.md)
- [📈time plot](bm-20250621-darwin-arm64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.016x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20250621-darwin-arm64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-base-mem.svg)
- [📄table](bm-20250621-darwin-arm64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-base.md)
- [📈time plot](bm-20250621-darwin-arm64-python-b14986c91464b06e9016-3.15.0a0-b14986c-vs-base.svg)

