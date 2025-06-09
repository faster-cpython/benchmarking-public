# Results

- fork: faster-cpython/specialize_for_iter_
- version: 3.15.0a0
- config: 
- commit hash: [baf4722](https://github.com/faster%2dcpython/cpython/commit/baf4722)
- commit date: 2025-06-09T12:05:30+01:00
- commit merge base: [b150b6aca7b17efe1bb13c3058d61cdefb83237e](https://github.com/python/cpython/commit/b150b6aca7b17efe1bb13c3058d61cdefb83237e)
- ref: specialize_for_iter_

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15534200254)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-216-generic-x86_64-with-glibc2.31
- [raw results](bm-20250609-linux-x86_64-faster%252dcpython-specialize_for_iter_-3.15.0a0-baf4722.json)

### vs. 3.10.4

- Geometric mean: 1.319x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250609-linux-x86_64-faster%252dcpython-specialize_for_iter_-3.15.0a0-baf4722-vs-3.10.4.md)
- [📈time plot](bm-20250609-linux-x86_64-faster%252dcpython-specialize_for_iter_-3.15.0a0-baf4722-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.089x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250609-linux-x86_64-faster%252dcpython-specialize_for_iter_-3.15.0a0-baf4722-vs-3.12.0.md)
- [📈time plot](bm-20250609-linux-x86_64-faster%252dcpython-specialize_for_iter_-3.15.0a0-baf4722-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.038x slower (HPT: reliability of 99.55%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250609-linux-x86_64-faster%252dcpython-specialize_for_iter_-3.15.0a0-baf4722-vs-3.13.0.md)
- [📈time plot](bm-20250609-linux-x86_64-faster%252dcpython-specialize_for_iter_-3.15.0a0-baf4722-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x slower (HPT: reliability of 97.46%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250609-linux-x86_64-faster%252dcpython-specialize_for_iter_-3.15.0a0-baf4722-vs-base-mem.svg)
- [📄table](bm-20250609-linux-x86_64-faster%252dcpython-specialize_for_iter_-3.15.0a0-baf4722-vs-base.md)
- [📈time plot](bm-20250609-linux-x86_64-faster%252dcpython-specialize_for_iter_-3.15.0a0-baf4722-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15534215930)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250609-pythonperf1-amd64-faster%252dcpython-specialize_for_iter_-3.15.0a0-baf4722.json)

### vs. 3.10.4

- Geometric mean: 1.171x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250609-pythonperf1-amd64-faster%252dcpython-specialize_for_iter_-3.15.0a0-baf4722-vs-3.10.4.md)
- [📈time plot](bm-20250609-pythonperf1-amd64-faster%252dcpython-specialize_for_iter_-3.15.0a0-baf4722-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.071x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250609-pythonperf1-amd64-faster%252dcpython-specialize_for_iter_-3.15.0a0-baf4722-vs-3.12.0.md)
- [📈time plot](bm-20250609-pythonperf1-amd64-faster%252dcpython-specialize_for_iter_-3.15.0a0-baf4722-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.018x slower (HPT: reliability of 91.75%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250609-pythonperf1-amd64-faster%252dcpython-specialize_for_iter_-3.15.0a0-baf4722-vs-3.13.0.md)
- [📈time plot](bm-20250609-pythonperf1-amd64-faster%252dcpython-specialize_for_iter_-3.15.0a0-baf4722-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x slower (HPT: reliability of 68.90%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250609-pythonperf1-amd64-faster%252dcpython-specialize_for_iter_-3.15.0a0-baf4722-vs-base.md)
- [📈time plot](bm-20250609-pythonperf1-amd64-faster%252dcpython-specialize_for_iter_-3.15.0a0-baf4722-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15534208033)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250609-darwin-arm64-faster%252dcpython-specialize_for_iter_-3.15.0a0-baf4722.json)

### vs. 3.10.4

- Geometric mean: 1.155x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250609-darwin-arm64-faster%252dcpython-specialize_for_iter_-3.15.0a0-baf4722-vs-3.10.4.md)
- [📈time plot](bm-20250609-darwin-arm64-faster%252dcpython-specialize_for_iter_-3.15.0a0-baf4722-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.082x slower (HPT: reliability of 98.61%, 1.00x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250609-darwin-arm64-faster%252dcpython-specialize_for_iter_-3.15.0a0-baf4722-vs-3.12.0.md)
- [📈time plot](bm-20250609-darwin-arm64-faster%252dcpython-specialize_for_iter_-3.15.0a0-baf4722-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.080x slower (HPT: reliability of 76.43%, 1.00x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250609-darwin-arm64-faster%252dcpython-specialize_for_iter_-3.15.0a0-baf4722-vs-3.13.0.md)
- [📈time plot](bm-20250609-darwin-arm64-faster%252dcpython-specialize_for_iter_-3.15.0a0-baf4722-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x faster (HPT: reliability of 98.71%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250609-darwin-arm64-faster%252dcpython-specialize_for_iter_-3.15.0a0-baf4722-vs-base-mem.svg)
- [📄table](bm-20250609-darwin-arm64-faster%252dcpython-specialize_for_iter_-3.15.0a0-baf4722-vs-base.md)
- [📈time plot](bm-20250609-darwin-arm64-faster%252dcpython-specialize_for_iter_-3.15.0a0-baf4722-vs-base.svg)

