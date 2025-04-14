# Results

- fork: python/e82c2ca2a59235bc1965
- version: 3.14.0a6+
- config: CLANG
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

- Geometric mean: 1.349x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.35x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.10.4.md)
- [📈time plot](bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.065x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.12.0.md)
- [📈time plot](bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.063x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.13.0.md)
- [📈time plot](bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.015x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.03x
- [🧠memory plot](bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-base-mem.svg)
- [📄table](bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-base.md)
- [📈time plot](bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13877830682)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250315-linux-x86_64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca.json)

### vs. 3.10.4

- Geometric mean: 1.486x faster (HPT: reliability of 100.00%, 1.35x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250315-linux-x86_64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.10.4.md)
- [📈time plot](bm-20250315-linux-x86_64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.146x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250315-linux-x86_64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.12.0.md)
- [📈time plot](bm-20250315-linux-x86_64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.072x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250315-linux-x86_64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.13.0.md)
- [📈time plot](bm-20250315-linux-x86_64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.028x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250315-linux-x86_64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-base-mem.svg)
- [📄table](bm-20250315-linux-x86_64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-base.md)
- [📈time plot](bm-20250315-linux-x86_64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13877830682)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250315-pythonperf2-x86_64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca.json)

### vs. 3.10.4

- Geometric mean: 1.371x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250315-pythonperf2-x86_64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.10.4.md)
- [📈time plot](bm-20250315-pythonperf2-x86_64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.065x faster (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250315-pythonperf2-x86_64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.12.0.md)
- [📈time plot](bm-20250315-pythonperf2-x86_64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.076x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250315-pythonperf2-x86_64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.13.0.md)
- [📈time plot](bm-20250315-pythonperf2-x86_64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.040x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.03x
- [🧠memory plot](bm-20250315-pythonperf2-x86_64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-base-mem.svg)
- [📄table](bm-20250315-pythonperf2-x86_64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-base.md)
- [📈time plot](bm-20250315-pythonperf2-x86_64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13877830682)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca.json)

### vs. 3.10.4

- Geometric mean: 1.406x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.10.4.md)
- [📈time plot](bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.196x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.12.0.md)
- [📈time plot](bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.145x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.13.0.md)
- [📈time plot](bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.148x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-base.md)
- [📈time plot](bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13877830682)
- cpu model: missing
- platform: macOS-15.3-arm64-arm-64bit-Mach-O
- [raw results](bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca.json)

### vs. 3.10.4

- Geometric mean: 1.394x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.10.4.md)
- [📈time plot](bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.098x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.12.0.md)
- [📈time plot](bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.099x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.13.0.md)
- [📈time plot](bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.060x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.99x
- [🧠memory plot](bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-base-mem.svg)
- [📄table](bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-base.md)
- [📈time plot](bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6%2B-e82c2ca-vs-base.svg)

