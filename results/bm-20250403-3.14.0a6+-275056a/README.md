# Results

- fork: python/275056a7fdcbe36aaac4
- version: 3.14.0a6+
- config: 
- commit hash: [275056a](https://github.com/python/cpython/commit/275056a)
- commit date: 2025-04-03T09:40:37+01:00
- commit merge base: [b3e3cc054c2c7718c0ad7c4690f76716649a2588](https://github.com/python/cpython/commit/b3e3cc054c2c7718c0ad7c4690f76716649a2588)
- ref: 275056a7fdcbe36aaac4

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14250947630)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a.json)

### vs. 3.10.4

- Geometric mean: 1.466x faster (HPT: reliability of 100.00%, 1.34x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a-vs-3.10.4.md)
- [📈time plot](bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.130x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a-vs-3.12.0.md)
- [📈time plot](bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.058x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a-vs-3.13.0.md)
- [📈time plot](bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14266936556)
- cpu model: missing
- platform: macOS-15.3.2-arm64-arm-64bit-Mach-O
- [raw results](bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a.json)

### vs. 3.10.4

- Geometric mean: 1.328x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a-vs-3.10.4.md)
- [📈time plot](bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.045x faster (HPT: reliability of 73.84%, 1.00x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a-vs-3.12.0.md)
- [📈time plot](bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.046x faster (HPT: reliability of 99.97%, 1.01x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a-vs-3.13.0.md)
- [📈time plot](bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6%2B-275056a-vs-3.13.0.svg)

