# Results

- fork: faster-cpython/immortal_stickiness
- version: 3.14.0a5+
- config: 
- commit hash: [490cf8d](https://github.com/faster%2dcpython/cpython/commit/490cf8d)
- commit date: 2025-03-12T10:19:54+00:00
- commit merge base: [155c44b9015089eacc6e2ace449391c12bfb8b8d](https://github.com/python/cpython/commit/155c44b9015089eacc6e2ace449391c12bfb8b8d)
- ref: immortal_stickiness

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13808999028)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250312-arminc-aarch64-faster%252dcpython-immortal_stickiness-3.14.0a5%2B-490cf8d.json)

### vs. 3.10.4

- Geometric mean: 1.322x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250312-arminc-aarch64-faster%252dcpython-immortal_stickiness-3.14.0a5%2B-490cf8d-vs-3.10.4.md)
- [📈time plot](bm-20250312-arminc-aarch64-faster%252dcpython-immortal_stickiness-3.14.0a5%2B-490cf8d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.047x faster (HPT: reliability of 99.43%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250312-arminc-aarch64-faster%252dcpython-immortal_stickiness-3.14.0a5%2B-490cf8d-vs-3.12.0.md)
- [📈time plot](bm-20250312-arminc-aarch64-faster%252dcpython-immortal_stickiness-3.14.0a5%2B-490cf8d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.044x faster (HPT: reliability of 99.98%, 1.00x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250312-arminc-aarch64-faster%252dcpython-immortal_stickiness-3.14.0a5%2B-490cf8d-vs-3.13.0.md)
- [📈time plot](bm-20250312-arminc-aarch64-faster%252dcpython-immortal_stickiness-3.14.0a5%2B-490cf8d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x slower (HPT: reliability of 99.99%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250312-arminc-aarch64-faster%252dcpython-immortal_stickiness-3.14.0a5%2B-490cf8d-vs-base-mem.svg)
- [📄table](bm-20250312-arminc-aarch64-faster%252dcpython-immortal_stickiness-3.14.0a5%2B-490cf8d-vs-base.md)
- [📈time plot](bm-20250312-arminc-aarch64-faster%252dcpython-immortal_stickiness-3.14.0a5%2B-490cf8d-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13808999028)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250312-linux-x86_64-faster%252dcpython-immortal_stickiness-3.14.0a5%2B-490cf8d.json)

### vs. 3.10.4

- Geometric mean: 1.433x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250312-linux-x86_64-faster%252dcpython-immortal_stickiness-3.14.0a5%2B-490cf8d-vs-3.10.4.md)
- [📈time plot](bm-20250312-linux-x86_64-faster%252dcpython-immortal_stickiness-3.14.0a5%2B-490cf8d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.106x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250312-linux-x86_64-faster%252dcpython-immortal_stickiness-3.14.0a5%2B-490cf8d-vs-3.12.0.md)
- [📈time plot](bm-20250312-linux-x86_64-faster%252dcpython-immortal_stickiness-3.14.0a5%2B-490cf8d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.037x faster (HPT: reliability of 99.90%, 1.00x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250312-linux-x86_64-faster%252dcpython-immortal_stickiness-3.14.0a5%2B-490cf8d-vs-3.13.0.md)
- [📈time plot](bm-20250312-linux-x86_64-faster%252dcpython-immortal_stickiness-3.14.0a5%2B-490cf8d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.007x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 0.99x
- [🧠memory plot](bm-20250312-linux-x86_64-faster%252dcpython-immortal_stickiness-3.14.0a5%2B-490cf8d-vs-base-mem.svg)
- [📄table](bm-20250312-linux-x86_64-faster%252dcpython-immortal_stickiness-3.14.0a5%2B-490cf8d-vs-base.md)
- [📈time plot](bm-20250312-linux-x86_64-faster%252dcpython-immortal_stickiness-3.14.0a5%2B-490cf8d-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13808999028)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250312-pythonperf1-amd64-faster%252dcpython-immortal_stickiness-3.14.0a5%2B-490cf8d.json)

### vs. 3.10.4

- Geometric mean: 1.226x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250312-pythonperf1-amd64-faster%252dcpython-immortal_stickiness-3.14.0a5%2B-490cf8d-vs-3.10.4.md)
- [📈time plot](bm-20250312-pythonperf1-amd64-faster%252dcpython-immortal_stickiness-3.14.0a5%2B-490cf8d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.046x faster (HPT: reliability of 66.50%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250312-pythonperf1-amd64-faster%252dcpython-immortal_stickiness-3.14.0a5%2B-490cf8d-vs-3.12.0.md)
- [📈time plot](bm-20250312-pythonperf1-amd64-faster%252dcpython-immortal_stickiness-3.14.0a5%2B-490cf8d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.010x faster (HPT: reliability of 99.99%, 1.02x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250312-pythonperf1-amd64-faster%252dcpython-immortal_stickiness-3.14.0a5%2B-490cf8d-vs-3.13.0.md)
- [📈time plot](bm-20250312-pythonperf1-amd64-faster%252dcpython-immortal_stickiness-3.14.0a5%2B-490cf8d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.009x faster (HPT: reliability of 98.74%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250312-pythonperf1-amd64-faster%252dcpython-immortal_stickiness-3.14.0a5%2B-490cf8d-vs-base.md)
- [📈time plot](bm-20250312-pythonperf1-amd64-faster%252dcpython-immortal_stickiness-3.14.0a5%2B-490cf8d-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13808999028)
- cpu model: missing
- platform: macOS-15.3-arm64-arm-64bit-Mach-O
- [raw results](bm-20250312-darwin-arm64-faster%252dcpython-immortal_stickiness-3.14.0a5%2B-490cf8d.json)

### vs. 3.10.4

- Geometric mean: 1.290x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250312-darwin-arm64-faster%252dcpython-immortal_stickiness-3.14.0a5%2B-490cf8d-vs-3.10.4.md)
- [📈time plot](bm-20250312-darwin-arm64-faster%252dcpython-immortal_stickiness-3.14.0a5%2B-490cf8d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.017x faster (HPT: reliability of 53.23%, 1.00x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250312-darwin-arm64-faster%252dcpython-immortal_stickiness-3.14.0a5%2B-490cf8d-vs-3.12.0.md)
- [📈time plot](bm-20250312-darwin-arm64-faster%252dcpython-immortal_stickiness-3.14.0a5%2B-490cf8d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.018x faster (HPT: reliability of 97.96%, 1.00x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250312-darwin-arm64-faster%252dcpython-immortal_stickiness-3.14.0a5%2B-490cf8d-vs-3.13.0.md)
- [📈time plot](bm-20250312-darwin-arm64-faster%252dcpython-immortal_stickiness-3.14.0a5%2B-490cf8d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x faster (HPT: reliability of 69.85%, 1.00x faster at 99th %ile)
- Memory usage: 0.99x
- [🧠memory plot](bm-20250312-darwin-arm64-faster%252dcpython-immortal_stickiness-3.14.0a5%2B-490cf8d-vs-base-mem.svg)
- [📄table](bm-20250312-darwin-arm64-faster%252dcpython-immortal_stickiness-3.14.0a5%2B-490cf8d-vs-base.md)
- [📈time plot](bm-20250312-darwin-arm64-faster%252dcpython-immortal_stickiness-3.14.0a5%2B-490cf8d-vs-base.svg)

