# Results

- fork: python/bc26f95e8ff60ccca981
- version: 3.14.0a6+
- config: CLANG
- commit hash: [bc26f95](https://github.com/python/cpython/commit/bc26f95)
- commit date: 2025-03-22T15:44:56-07:00
- commit merge base: [18249d938335312d618a3962ec7590bea709d58e](https://github.com/python/cpython/commit/18249d938335312d618a3962ec7590bea709d58e)
- ref: bc26f95e8ff60ccca981

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14013521701)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6%2B-bc26f95.json)

### vs. 3.10.4

- Geometric mean: 1.352x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.36x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6%2B-bc26f95-vs-3.10.4.md)
- [📈time plot](bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6%2B-bc26f95-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.066x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6%2B-bc26f95-vs-3.12.0.md)
- [📈time plot](bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6%2B-bc26f95-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.062x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6%2B-bc26f95-vs-3.13.0.md)
- [📈time plot](bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6%2B-bc26f95-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.014x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.03x
- [🧠memory plot](bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6%2B-bc26f95-vs-base-mem.svg)
- [📄table](bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6%2B-bc26f95-vs-base.md)
- [📈time plot](bm-20250322-arminc-aarch64-python-bc26f95e8ff60ccca981-3.14.0a6%2B-bc26f95-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14013521701)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6%2B-bc26f95.json)

### vs. 3.10.4

- Geometric mean: 1.480x faster (HPT: reliability of 100.00%, 1.34x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6%2B-bc26f95-vs-3.10.4.md)
- [📈time plot](bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6%2B-bc26f95-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.142x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6%2B-bc26f95-vs-3.12.0.md)
- [📈time plot](bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6%2B-bc26f95-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.068x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6%2B-bc26f95-vs-3.13.0.md)
- [📈time plot](bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6%2B-bc26f95-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.024x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6%2B-bc26f95-vs-base-mem.svg)
- [📄table](bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6%2B-bc26f95-vs-base.md)
- [📈time plot](bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6%2B-bc26f95-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14013521701)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6%2B-bc26f95.json)

### vs. 3.10.4

- Geometric mean: 1.380x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6%2B-bc26f95-vs-3.10.4.md)
- [📈time plot](bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6%2B-bc26f95-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.074x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6%2B-bc26f95-vs-3.12.0.md)
- [📈time plot](bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6%2B-bc26f95-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.084x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6%2B-bc26f95-vs-3.13.0.md)
- [📈time plot](bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6%2B-bc26f95-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.049x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.03x
- [🧠memory plot](bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6%2B-bc26f95-vs-base-mem.svg)
- [📄table](bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6%2B-bc26f95-vs-base.md)
- [📈time plot](bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6%2B-bc26f95-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14013521701)
- cpu model: missing
- platform: macOS-15.3.2-arm64-arm-64bit-Mach-O
- [raw results](bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6%2B-bc26f95.json)

### vs. 3.10.4

- Geometric mean: 1.435x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6%2B-bc26f95-vs-3.10.4.md)
- [📈time plot](bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6%2B-bc26f95-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.131x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6%2B-bc26f95-vs-3.12.0.md)
- [📈time plot](bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6%2B-bc26f95-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.133x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6%2B-bc26f95-vs-3.13.0.md)
- [📈time plot](bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6%2B-bc26f95-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.114x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 0.99x
- [🧠memory plot](bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6%2B-bc26f95-vs-base-mem.svg)
- [📄table](bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6%2B-bc26f95-vs-base.md)
- [📈time plot](bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6%2B-bc26f95-vs-base.svg)

