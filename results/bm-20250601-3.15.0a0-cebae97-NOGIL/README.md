# Results

- fork: python/cebae977a63f32c3c03d
- version: 3.15.0a0
- config: NOGIL
- commit hash: [cebae97](https://github.com/python/cpython/commit/cebae97)
- commit date: 2025-06-01T00:33:02+03:00
- commit merge base: [3704171415c1ea6ebbeb2f992758b6565f42e378](https://github.com/python/cpython/commit/3704171415c1ea6ebbeb2f992758b6565f42e378)
- ref: cebae977a63f32c3c03d

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15368744364)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json)

### vs. 3.10.4

- Geometric mean: 1.074x slower (HPT: reliability of 97.14%, 1.00x slower at 99th %ile)
- Memory usage: 1.71x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.10.4.md)
- [📈time plot](bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.261x slower (HPT: reliability of 100.00%, 1.23x slower at 99th %ile)
- Memory usage: 1.37x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.12.0.md)
- [📈time plot](bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.261x slower (HPT: reliability of 100.00%, 1.24x slower at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.13.0.md)
- [📈time plot](bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.13.0.svg)

### vs. base

- [🧠memory plot](bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-base-mem.svg)
- [📄table](bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-base.md)
- [📈time plot](bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15368744364)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json)

### vs. 3.10.4

- Geometric mean: 1.076x faster (HPT: reliability of 98.75%, 1.00x faster at 99th %ile)
- Memory usage: 1.58x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.10.4.md)
- [📈time plot](bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.154x slower (HPT: reliability of 99.98%, 1.06x slower at 99th %ile)
- Memory usage: 1.37x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.12.0.md)
- [📈time plot](bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.207x slower (HPT: reliability of 100.00%, 1.15x slower at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.13.0.md)
- [📈time plot](bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.061x slower (HPT: reliability of 100.00%, 1.09x slower at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: 🔴 djangocms
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [🧠memory plot](bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-base-mem.svg)
- [📄table](bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-base.md)
- [📈time plot](bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15368744364)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json)

### vs. 3.10.4

- Geometric mean: 1.014x faster (HPT: reliability of 87.91%, 1.00x faster at 99th %ile)
- Memory usage: 1.67x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.10.4.md)
- [📈time plot](bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.202x slower (HPT: reliability of 100.00%, 1.12x slower at 99th %ile)
- Memory usage: 1.37x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.12.0.md)
- [📈time plot](bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.188x slower (HPT: reliability of 100.00%, 1.12x slower at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.13.0.md)
- [📈time plot](bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.13.0.svg)

### vs. base

- [🧠memory plot](bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-base-mem.svg)
- [📄table](bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-base.md)
- [📈time plot](bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15368744364)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json)

### vs. 3.10.4

- Geometric mean: 1.314x slower (HPT: reliability of 100.00%, 1.41x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.10.4.md)
- [📈time plot](bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.406x slower (HPT: reliability of 100.00%, 1.54x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.12.0.md)
- [📈time plot](bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.418x slower (HPT: reliability of 100.00%, 1.66x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.13.0.md)
- [📈time plot](bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.149x slower (HPT: reliability of 100.00%, 1.19x slower at 99th %ile)
- Memory usage: unknown
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-base.md)
- [📈time plot](bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-base.svg)

## windows amd64 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15368744364)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json)

### vs. 3.10.4

- Geometric mean: 1.229x slower (HPT: reliability of 100.00%, 1.27x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.10.4.md)
- [📈time plot](bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.210x slower (HPT: reliability of 100.00%, 1.19x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.12.0.md)
- [📈time plot](bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.301x slower (HPT: reliability of 100.00%, 1.35x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.13.0.md)
- [📈time plot](bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.13.0.svg)

### vs. base

- [📄table](bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-base.md)
- [📈time plot](bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15368744364)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json)

### vs. 3.10.4

- Geometric mean: 1.153x faster (HPT: reliability of 98.43%, 1.00x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.10.4.md)
- [📈time plot](bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.072x slower (HPT: reliability of 99.96%, 1.03x slower at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.12.0.md)
- [📈time plot](bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.070x slower (HPT: reliability of 99.82%, 1.01x slower at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.13.0.md)
- [📈time plot](bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.13.0.svg)

### vs. base

- [🧠memory plot](bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-base-mem.svg)
- [📄table](bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-base.md)
- [📈time plot](bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-base.svg)

