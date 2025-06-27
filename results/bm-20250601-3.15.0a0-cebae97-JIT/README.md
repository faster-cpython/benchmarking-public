# Results

- fork: python/cebae977a63f32c3c03d
- version: 3.15.0a0
- config: JIT
- commit hash: [cebae97](https://github.com/python/cpython/commit/cebae97)
- commit date: 2025-06-01T00:33:02+03:00
- commit merge base: [3704171415c1ea6ebbeb2f992758b6565f42e378](https://github.com/python/cpython/commit/3704171415c1ea6ebbeb2f992758b6565f42e378)
- ref: cebae977a63f32c3c03d

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15927043826)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json)

### vs. 3.10.4

- Geometric mean: 1.925x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.37x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, regex_compile, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.10.4.md)
- [📈time plot](bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.488x faster (HPT: reliability of 99.83%, 1.00x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, regex_compile, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.12.0.md)
- [📈time plot](bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.448x faster (HPT: reliability of 99.67%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, regex_compile, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.13.0.md)
- [📈time plot](bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.344x faster (HPT: reliability of 99.98%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: 🔴 regex_compile
- [🧠memory plot](bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-base-mem.svg)
- [📄table](bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-base.md)
- [📈time plot](bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15927043826)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-216-generic-x86_64-with-glibc2.31
- [raw results](bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json)

### vs. 3.10.4

- Geometric mean: 2.127x faster (HPT: reliability of 100.00%, 1.33x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, regex_compile, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.10.4.md)
- [📈time plot](bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.652x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, regex_compile, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.12.0.md)
- [📈time plot](bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.458x faster (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, regex_compile, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.13.0.md)
- [📈time plot](bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.374x faster (HPT: reliability of 81.03%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: 🔴 regex_compile
- [🧠memory plot](bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-base-mem.svg)
- [📄table](bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-base.md)
- [📈time plot](bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15927043826)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json)

### vs. 3.10.4

- Geometric mean: 1.895x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.10.4.md)
- [📈time plot](bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.623x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.12.0.md)
- [📈time plot](bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.487x faster (HPT: reliability of 85.96%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.13.0.md)
- [📈time plot](bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.370x faster (HPT: reliability of 59.62%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-base.md)
- [📈time plot](bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15927043826)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json)

### vs. 3.10.4

- Geometric mean: 1.738x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.10.4.md)
- [📈time plot](bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.336x faster (HPT: reliability of 70.22%, 1.00x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.12.0.md)
- [📈time plot](bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.338x faster (HPT: reliability of 81.25%, 1.00x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.13.0.md)
- [📈time plot](bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.251x faster (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-base-mem.svg)
- [📄table](bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-base.md)
- [📈time plot](bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97-vs-base.svg)

