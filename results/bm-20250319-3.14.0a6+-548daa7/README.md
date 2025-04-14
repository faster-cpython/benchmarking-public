# Results

- fork: zooba/gh_91349
- version: 3.14.0a6+
- config: 
- commit hash: [548daa7](https://github.com/zooba/cpython/commit/548daa7)
- commit date: 2025-03-19T13:44:20+00:00
- commit merge base: [d783d7b51d31db568de6b3438f4e805acff663da](https://github.com/python/cpython/commit/d783d7b51d31db568de6b3438f4e805acff663da)
- ref: gh_91349

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13948931188)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250319-arminc-aarch64-zooba-gh_91349-3.14.0a6%2B-548daa7.json)

### vs. 3.10.4

- Geometric mean: 1.319x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250319-arminc-aarch64-zooba-gh_91349-3.14.0a6%2B-548daa7-vs-3.10.4.md)
- [📈time plot](bm-20250319-arminc-aarch64-zooba-gh_91349-3.14.0a6%2B-548daa7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.042x faster (HPT: reliability of 99.62%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250319-arminc-aarch64-zooba-gh_91349-3.14.0a6%2B-548daa7-vs-3.12.0.md)
- [📈time plot](bm-20250319-arminc-aarch64-zooba-gh_91349-3.14.0a6%2B-548daa7-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.042x faster (HPT: reliability of 99.95%, 1.00x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250319-arminc-aarch64-zooba-gh_91349-3.14.0a6%2B-548daa7-vs-3.13.0.md)
- [📈time plot](bm-20250319-arminc-aarch64-zooba-gh_91349-3.14.0a6%2B-548daa7-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x faster (HPT: reliability of 95.84%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250319-arminc-aarch64-zooba-gh_91349-3.14.0a6%2B-548daa7-vs-base-mem.svg)
- [📄table](bm-20250319-arminc-aarch64-zooba-gh_91349-3.14.0a6%2B-548daa7-vs-base.md)
- [📈time plot](bm-20250319-arminc-aarch64-zooba-gh_91349-3.14.0a6%2B-548daa7-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13948931188)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250319-linux-x86_64-zooba-gh_91349-3.14.0a6%2B-548daa7.json)

### vs. 3.10.4

- Geometric mean: 1.437x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250319-linux-x86_64-zooba-gh_91349-3.14.0a6%2B-548daa7-vs-3.10.4.md)
- [📈time plot](bm-20250319-linux-x86_64-zooba-gh_91349-3.14.0a6%2B-548daa7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.110x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250319-linux-x86_64-zooba-gh_91349-3.14.0a6%2B-548daa7-vs-3.12.0.md)
- [📈time plot](bm-20250319-linux-x86_64-zooba-gh_91349-3.14.0a6%2B-548daa7-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.040x faster (HPT: reliability of 99.98%, 1.00x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250319-linux-x86_64-zooba-gh_91349-3.14.0a6%2B-548daa7-vs-3.13.0.md)
- [📈time plot](bm-20250319-linux-x86_64-zooba-gh_91349-3.14.0a6%2B-548daa7-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.003x slower (HPT: reliability of 90.40%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250319-linux-x86_64-zooba-gh_91349-3.14.0a6%2B-548daa7-vs-base-mem.svg)
- [📄table](bm-20250319-linux-x86_64-zooba-gh_91349-3.14.0a6%2B-548daa7-vs-base.md)
- [📈time plot](bm-20250319-linux-x86_64-zooba-gh_91349-3.14.0a6%2B-548daa7-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13948931188)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250319-pythonperf1-amd64-zooba-gh_91349-3.14.0a6%2B-548daa7.json)

### vs. 3.10.4

- Geometric mean: 1.201x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250319-pythonperf1-amd64-zooba-gh_91349-3.14.0a6%2B-548daa7-vs-3.10.4.md)
- [📈time plot](bm-20250319-pythonperf1-amd64-zooba-gh_91349-3.14.0a6%2B-548daa7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.025x faster (HPT: reliability of 87.07%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250319-pythonperf1-amd64-zooba-gh_91349-3.14.0a6%2B-548daa7-vs-3.12.0.md)
- [📈time plot](bm-20250319-pythonperf1-amd64-zooba-gh_91349-3.14.0a6%2B-548daa7-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.001x slower (HPT: reliability of 99.99%, 1.04x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250319-pythonperf1-amd64-zooba-gh_91349-3.14.0a6%2B-548daa7-vs-3.13.0.md)
- [📈time plot](bm-20250319-pythonperf1-amd64-zooba-gh_91349-3.14.0a6%2B-548daa7-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x faster (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250319-pythonperf1-amd64-zooba-gh_91349-3.14.0a6%2B-548daa7-vs-base.md)
- [📈time plot](bm-20250319-pythonperf1-amd64-zooba-gh_91349-3.14.0a6%2B-548daa7-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13948931188)
- cpu model: missing
- platform: macOS-15.3.2-arm64-arm-64bit-Mach-O
- [raw results](bm-20250319-darwin-arm64-zooba-gh_91349-3.14.0a6%2B-548daa7.json)

### vs. 3.10.4

- Geometric mean: 1.358x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250319-darwin-arm64-zooba-gh_91349-3.14.0a6%2B-548daa7-vs-3.10.4.md)
- [📈time plot](bm-20250319-darwin-arm64-zooba-gh_91349-3.14.0a6%2B-548daa7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.070x faster (HPT: reliability of 99.98%, 1.01x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250319-darwin-arm64-zooba-gh_91349-3.14.0a6%2B-548daa7-vs-3.12.0.md)
- [📈time plot](bm-20250319-darwin-arm64-zooba-gh_91349-3.14.0a6%2B-548daa7-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.071x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250319-darwin-arm64-zooba-gh_91349-3.14.0a6%2B-548daa7-vs-3.13.0.md)
- [📈time plot](bm-20250319-darwin-arm64-zooba-gh_91349-3.14.0a6%2B-548daa7-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x faster (HPT: reliability of 71.71%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250319-darwin-arm64-zooba-gh_91349-3.14.0a6%2B-548daa7-vs-base-mem.svg)
- [📄table](bm-20250319-darwin-arm64-zooba-gh_91349-3.14.0a6%2B-548daa7-vs-base.md)
- [📈time plot](bm-20250319-darwin-arm64-zooba-gh_91349-3.14.0a6%2B-548daa7-vs-base.svg)

