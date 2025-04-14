# Results

- fork: python/f81990024554a75e2ab3
- version: 3.14.0a6+
- config: 
- commit hash: [f819900](https://github.com/python/cpython/commit/f819900)
- commit date: 2025-03-18T17:34:01+01:00
- commit merge base: [49234c065cf2b1ea32c5a3976d834b1d07b9b831](https://github.com/python/cpython/commit/49234c065cf2b1ea32c5a3976d834b1d07b9b831)
- ref: f81990024554a75e2ab3

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13934097220)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250318-linux-x86_64-python-f81990024554a75e2ab3-3.14.0a6%2B-f819900.json)

### vs. 3.10.4

- Geometric mean: 1.435x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250318-linux-x86_64-python-f81990024554a75e2ab3-3.14.0a6%2B-f819900-vs-3.10.4.md)
- [📈time plot](bm-20250318-linux-x86_64-python-f81990024554a75e2ab3-3.14.0a6%2B-f819900-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.108x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250318-linux-x86_64-python-f81990024554a75e2ab3-3.14.0a6%2B-f819900-vs-3.12.0.md)
- [📈time plot](bm-20250318-linux-x86_64-python-f81990024554a75e2ab3-3.14.0a6%2B-f819900-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.038x faster (HPT: reliability of 99.89%, 1.00x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250318-linux-x86_64-python-f81990024554a75e2ab3-3.14.0a6%2B-f819900-vs-3.13.0.md)
- [📈time plot](bm-20250318-linux-x86_64-python-f81990024554a75e2ab3-3.14.0a6%2B-f819900-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x slower (HPT: reliability of 72.95%, 1.00x slower at 99th %ile)
- Memory usage: 0.99x
- [🧠memory plot](bm-20250318-linux-x86_64-python-f81990024554a75e2ab3-3.14.0a6%2B-f819900-vs-base-mem.svg)
- [📄table](bm-20250318-linux-x86_64-python-f81990024554a75e2ab3-3.14.0a6%2B-f819900-vs-base.md)
- [📈time plot](bm-20250318-linux-x86_64-python-f81990024554a75e2ab3-3.14.0a6%2B-f819900-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13952663745)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250318-pythonperf2-x86_64-python-f81990024554a75e2ab3-3.14.0a6%2B-f819900.json)

### vs. 3.10.4

- Geometric mean: 1.309x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250318-pythonperf2-x86_64-python-f81990024554a75e2ab3-3.14.0a6%2B-f819900-vs-3.10.4.md)
- [📈time plot](bm-20250318-pythonperf2-x86_64-python-f81990024554a75e2ab3-3.14.0a6%2B-f819900-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.019x faster (HPT: reliability of 64.92%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250318-pythonperf2-x86_64-python-f81990024554a75e2ab3-3.14.0a6%2B-f819900-vs-3.12.0.md)
- [📈time plot](bm-20250318-pythonperf2-x86_64-python-f81990024554a75e2ab3-3.14.0a6%2B-f819900-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.030x faster (HPT: reliability of 99.97%, 1.00x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250318-pythonperf2-x86_64-python-f81990024554a75e2ab3-3.14.0a6%2B-f819900-vs-3.13.0.md)
- [📈time plot](bm-20250318-pythonperf2-x86_64-python-f81990024554a75e2ab3-3.14.0a6%2B-f819900-vs-3.13.0.svg)

