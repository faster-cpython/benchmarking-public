# Results

- fork: python/275056a7fdcbe36aaac4
- version: 3.14.0a6+
- config: CLANG
- commit hash: [275056a](https://github.com/python/cpython/commit/275056a)
- commit date: 2025-04-03T09:40:37+01:00
- commit merge base: [b3e3cc054c2c7718c0ad7c4690f76716649a2588](https://github.com/python/cpython/commit/b3e3cc054c2c7718c0ad7c4690f76716649a2588)
- ref: 275056a7fdcbe36aaac4

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14334771971)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250403-arminc-aarch64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a.json)

### vs. 3.10.4

- Geometric mean: 1.371x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.36x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250403-arminc-aarch64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a-vs-3.10.4.md)
- [📈time plot](bm-20250403-arminc-aarch64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.084x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250403-arminc-aarch64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a-vs-3.12.0.md)
- [📈time plot](bm-20250403-arminc-aarch64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.080x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250403-arminc-aarch64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a-vs-3.13.0.md)
- [📈time plot](bm-20250403-arminc-aarch64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a-vs-3.13.0.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14334771971)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a.json)

### vs. 3.10.4

- Geometric mean: 1.514x faster (HPT: reliability of 100.00%, 1.36x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a-vs-3.10.4.md)
- [📈time plot](bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.166x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a-vs-3.12.0.md)
- [📈time plot](bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.090x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a-vs-3.13.0.md)
- [📈time plot](bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.030x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a-vs-base-mem.svg)
- [📄table](bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a-vs-base.md)
- [📈time plot](bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14334771971)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250403-pythonperf1-amd64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a.json)

### vs. 3.10.4

- Geometric mean: 1.513x faster (HPT: reliability of 100.00%, 1.35x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250403-pythonperf1-amd64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a-vs-3.10.4.md)
- [📈time plot](bm-20250403-pythonperf1-amd64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.283x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250403-pythonperf1-amd64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a-vs-3.12.0.md)
- [📈time plot](bm-20250403-pythonperf1-amd64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.197x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250403-pythonperf1-amd64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a-vs-3.13.0.md)
- [📈time plot](bm-20250403-pythonperf1-amd64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14334771971)
- cpu model: missing
- platform: macOS-15.3.2-arm64-arm-64bit-Mach-O
- [raw results](bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a.json)

### vs. 3.10.4

- Geometric mean: 1.464x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a-vs-3.10.4.md)
- [📈time plot](bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.149x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a-vs-3.12.0.md)
- [📈time plot](bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.151x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a-vs-3.13.0.md)
- [📈time plot](bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.103x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 0.99x
- [🧠memory plot](bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a-vs-base-mem.svg)
- [📄table](bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a-vs-base.md)
- [📈time plot](bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a-vs-base.svg)

