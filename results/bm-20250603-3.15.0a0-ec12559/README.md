# Results

- fork: python/ec12559ebafca01ded22
- version: 3.15.0a0
- config: 
- commit hash: [ec12559](https://github.com/python/cpython/commit/ec12559)
- commit date: 2025-06-03T10:40:25+03:00
- commit merge base: [485b499610eefe362faf171f258b3a3588378ff1](https://github.com/python/cpython/commit/485b499610eefe362faf171f258b3a3588378ff1)
- ref: ec12559ebafca01ded22

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15414280923)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250603-arminc-aarch64-python-ec12559ebafca01ded22-3.15.0a0-ec12559.json)

### vs. 3.10.4

- Geometric mean: 1.225x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.35x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250603-arminc-aarch64-python-ec12559ebafca01ded22-3.15.0a0-ec12559-vs-3.10.4.md)
- [📈time plot](bm-20250603-arminc-aarch64-python-ec12559ebafca01ded22-3.15.0a0-ec12559-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.028x slower (HPT: reliability of 99.91%, 1.01x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250603-arminc-aarch64-python-ec12559ebafca01ded22-3.15.0a0-ec12559-vs-3.12.0.md)
- [📈time plot](bm-20250603-arminc-aarch64-python-ec12559ebafca01ded22-3.15.0a0-ec12559-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.026x slower (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250603-arminc-aarch64-python-ec12559ebafca01ded22-3.15.0a0-ec12559-vs-3.13.0.md)
- [📈time plot](bm-20250603-arminc-aarch64-python-ec12559ebafca01ded22-3.15.0a0-ec12559-vs-3.13.0.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20250603-azure-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559-pystats.json)
- [pystats table](bm-20250603-azure-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15414280923)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559.json)

### vs. 3.10.4

- Geometric mean: 1.319x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559-vs-3.10.4.md)
- [📈time plot](bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.089x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559-vs-3.12.0.md)
- [📈time plot](bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.039x slower (HPT: reliability of 99.36%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559-vs-3.13.0.md)
- [📈time plot](bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15414280923)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250603-pythonperf1-amd64-python-ec12559ebafca01ded22-3.15.0a0-ec12559.json)

### vs. 3.10.4

- Geometric mean: 1.164x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250603-pythonperf1-amd64-python-ec12559ebafca01ded22-3.15.0a0-ec12559-vs-3.10.4.md)
- [📈time plot](bm-20250603-pythonperf1-amd64-python-ec12559ebafca01ded22-3.15.0a0-ec12559-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.064x faster (HPT: reliability of 99.97%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250603-pythonperf1-amd64-python-ec12559ebafca01ded22-3.15.0a0-ec12559-vs-3.12.0.md)
- [📈time plot](bm-20250603-pythonperf1-amd64-python-ec12559ebafca01ded22-3.15.0a0-ec12559-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.026x slower (HPT: reliability of 94.89%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250603-pythonperf1-amd64-python-ec12559ebafca01ded22-3.15.0a0-ec12559-vs-3.13.0.md)
- [📈time plot](bm-20250603-pythonperf1-amd64-python-ec12559ebafca01ded22-3.15.0a0-ec12559-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15414280923)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250603-darwin-arm64-python-ec12559ebafca01ded22-3.15.0a0-ec12559.json)

### vs. 3.10.4

- Geometric mean: 1.228x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250603-darwin-arm64-python-ec12559ebafca01ded22-3.15.0a0-ec12559-vs-3.10.4.md)
- [📈time plot](bm-20250603-darwin-arm64-python-ec12559ebafca01ded22-3.15.0a0-ec12559-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.024x slower (HPT: reliability of 61.25%, 1.00x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250603-darwin-arm64-python-ec12559ebafca01ded22-3.15.0a0-ec12559-vs-3.12.0.md)
- [📈time plot](bm-20250603-darwin-arm64-python-ec12559ebafca01ded22-3.15.0a0-ec12559-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.022x slower (HPT: reliability of 99.93%, 1.00x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250603-darwin-arm64-python-ec12559ebafca01ded22-3.15.0a0-ec12559-vs-3.13.0.md)
- [📈time plot](bm-20250603-darwin-arm64-python-ec12559ebafca01ded22-3.15.0a0-ec12559-vs-3.13.0.svg)

