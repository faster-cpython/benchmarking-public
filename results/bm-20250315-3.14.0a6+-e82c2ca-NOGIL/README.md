# Results

- fork: python/e82c2ca2a59235bc1965
- version: 3.14.0a6+
- config: NOGIL
- commit hash: [e82c2ca](https://github.com/python/cpython/commit/e82c2ca)
- commit date: 2025-03-15T18:55:00+00:00
- commit merge base: [f104c19a94ae43f788e509019901b1f48fbd134e](https://github.com/python/cpython/commit/f104c19a94ae43f788e509019901b1f48fbd134e)
- ref: e82c2ca2a59235bc1965

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13877830682)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca.json)

### vs. 3.10.4

- Geometric mean: 1.142x faster (HPT: reliability of 99.99%, 1.04x faster at 99th %ile)
- Memory usage: 1.59x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.10.4.md)
- [📈time plot](bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.088x slower (HPT: reliability of 99.99%, 1.06x slower at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.12.0.md)
- [📈time plot](bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.093x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.13.0.md)
- [📈time plot](bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.133x slower (HPT: reliability of 100.00%, 1.11x slower at 99th %ile)
- Memory usage: 1.21x
- [🧠memory plot](bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-base-mem.svg)
- [📄table](bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-base.md)
- [📈time plot](bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13877830682)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250315-linux-x86_64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca.json)

### vs. 3.10.4

- Geometric mean: 1.278x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: 1.53x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250315-linux-x86_64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.10.4.md)
- [📈time plot](bm-20250315-linux-x86_64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.001x slower (HPT: reliability of 95.81%, 1.00x slower at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250315-linux-x86_64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.12.0.md)
- [📈time plot](bm-20250315-linux-x86_64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.067x slower (HPT: reliability of 99.99%, 1.04x slower at 99th %ile)
- Memory usage: 1.23x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250315-linux-x86_64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.13.0.md)
- [📈time plot](bm-20250315-linux-x86_64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.106x slower (HPT: reliability of 100.00%, 1.10x slower at 99th %ile)
- Memory usage: 1.20x
- [🧠memory plot](bm-20250315-linux-x86_64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-base-mem.svg)
- [📄table](bm-20250315-linux-x86_64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-base.md)
- [📈time plot](bm-20250315-linux-x86_64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13877830682)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250315-pythonperf2-x86_64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca.json)

### vs. 3.10.4

- Geometric mean: 1.203x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: 1.56x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250315-pythonperf2-x86_64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.10.4.md)
- [📈time plot](bm-20250315-pythonperf2-x86_64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.052x slower (HPT: reliability of 99.85%, 1.02x slower at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250315-pythonperf2-x86_64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.12.0.md)
- [📈time plot](bm-20250315-pythonperf2-x86_64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.045x slower (HPT: reliability of 99.75%, 1.01x slower at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250315-pythonperf2-x86_64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.13.0.md)
- [📈time plot](bm-20250315-pythonperf2-x86_64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.078x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: 1.21x
- [🧠memory plot](bm-20250315-pythonperf2-x86_64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-base-mem.svg)
- [📄table](bm-20250315-pythonperf2-x86_64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-base.md)
- [📈time plot](bm-20250315-pythonperf2-x86_64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13877830682)
- cpu model: missing
- platform: macOS-15.3-arm64-arm-64bit-Mach-O
- [raw results](bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca.json)

### vs. 3.10.4

- Geometric mean: 1.169x faster (HPT: reliability of 99.90%, 1.02x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.10.4.md)
- [📈time plot](bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.067x slower (HPT: reliability of 99.99%, 1.04x slower at 99th %ile)
- Memory usage: 1.23x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.12.0.md)
- [📈time plot](bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.066x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.13.0.md)
- [📈time plot](bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.103x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: 🔴 dask
- [🧠memory plot](bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-base-mem.svg)
- [📄table](bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-base.md)
- [📈time plot](bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-base.svg)

