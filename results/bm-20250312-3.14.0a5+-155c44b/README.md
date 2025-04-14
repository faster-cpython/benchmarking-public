# Results

- fork: python/155c44b9015089eacc6e
- version: 3.14.0a5+
- config: 
- commit hash: [155c44b](https://github.com/python/cpython/commit/155c44b)
- commit date: 2025-03-12T08:12:57+00:00
- commit merge base: [15a8412b5e12ae46761843d4442c7b56ffa75176](https://github.com/python/cpython/commit/15a8412b5e12ae46761843d4442c7b56ffa75176)
- ref: 155c44b9015089eacc6e

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13830797954)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250312-arminc-aarch64-python-155c44b9015089eacc6e-3.14.0a5%2B-155c44b.json)

### vs. 3.10.4

- Geometric mean: 1.328x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250312-arminc-aarch64-python-155c44b9015089eacc6e-3.14.0a5%2B-155c44b-vs-3.10.4.md)
- [📈time plot](bm-20250312-arminc-aarch64-python-155c44b9015089eacc6e-3.14.0a5%2B-155c44b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.051x faster (HPT: reliability of 99.97%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250312-arminc-aarch64-python-155c44b9015089eacc6e-3.14.0a5%2B-155c44b-vs-3.12.0.md)
- [📈time plot](bm-20250312-arminc-aarch64-python-155c44b9015089eacc6e-3.14.0a5%2B-155c44b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.051x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250312-arminc-aarch64-python-155c44b9015089eacc6e-3.14.0a5%2B-155c44b-vs-3.13.0.md)
- [📈time plot](bm-20250312-arminc-aarch64-python-155c44b9015089eacc6e-3.14.0a5%2B-155c44b-vs-3.13.0.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13830797954)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250312-linux-x86_64-python-155c44b9015089eacc6e-3.14.0a5%2B-155c44b.json)

### vs. 3.10.4

- Geometric mean: 1.445x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250312-linux-x86_64-python-155c44b9015089eacc6e-3.14.0a5%2B-155c44b-vs-3.10.4.md)
- [📈time plot](bm-20250312-linux-x86_64-python-155c44b9015089eacc6e-3.14.0a5%2B-155c44b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.115x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250312-linux-x86_64-python-155c44b9015089eacc6e-3.14.0a5%2B-155c44b-vs-3.12.0.md)
- [📈time plot](bm-20250312-linux-x86_64-python-155c44b9015089eacc6e-3.14.0a5%2B-155c44b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.045x faster (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250312-linux-x86_64-python-155c44b9015089eacc6e-3.14.0a5%2B-155c44b-vs-3.13.0.md)
- [📈time plot](bm-20250312-linux-x86_64-python-155c44b9015089eacc6e-3.14.0a5%2B-155c44b-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13830797954)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5%2B-155c44b.json)

### vs. 3.10.4

- Geometric mean: 1.214x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5%2B-155c44b-vs-3.10.4.md)
- [📈time plot](bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5%2B-155c44b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.035x faster (HPT: reliability of 55.57%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5%2B-155c44b-vs-3.12.0.md)
- [📈time plot](bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5%2B-155c44b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.001x faster (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5%2B-155c44b-vs-3.13.0.md)
- [📈time plot](bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5%2B-155c44b-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13830797954)
- cpu model: missing
- platform: macOS-15.3-arm64-arm-64bit-Mach-O
- [raw results](bm-20250312-darwin-arm64-python-155c44b9015089eacc6e-3.14.0a5%2B-155c44b.json)

### vs. 3.10.4

- Geometric mean: 1.290x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250312-darwin-arm64-python-155c44b9015089eacc6e-3.14.0a5%2B-155c44b-vs-3.10.4.md)
- [📈time plot](bm-20250312-darwin-arm64-python-155c44b9015089eacc6e-3.14.0a5%2B-155c44b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.016x faster (HPT: reliability of 58.48%, 1.00x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250312-darwin-arm64-python-155c44b9015089eacc6e-3.14.0a5%2B-155c44b-vs-3.12.0.md)
- [📈time plot](bm-20250312-darwin-arm64-python-155c44b9015089eacc6e-3.14.0a5%2B-155c44b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.018x faster (HPT: reliability of 97.68%, 1.00x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250312-darwin-arm64-python-155c44b9015089eacc6e-3.14.0a5%2B-155c44b-vs-3.13.0.md)
- [📈time plot](bm-20250312-darwin-arm64-python-155c44b9015089eacc6e-3.14.0a5%2B-155c44b-vs-3.13.0.svg)

