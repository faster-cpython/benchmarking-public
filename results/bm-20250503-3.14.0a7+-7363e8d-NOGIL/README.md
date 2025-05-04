# Results

- fork: python/7363e8d24d14abf65163
- version: 3.14.0a7+
- config: NOGIL
- commit hash: [7363e8d](https://github.com/python/cpython/commit/7363e8d)
- commit date: 2025-05-03T23:33:22+03:00
- commit merge base: [3e256b9118eded25e6aca61e3939fd4e03b87082](https://github.com/python/cpython/commit/3e256b9118eded25e6aca61e3939fd4e03b87082)
- ref: 7363e8d24d14abf65163

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14815732722)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d.json)

### vs. 3.10.4

- Geometric mean: 1.177x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.60x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-3.10.4.md)
- [📈time plot](bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.058x slower (HPT: reliability of 99.86%, 1.02x slower at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-3.12.0.md)
- [📈time plot](bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.067x slower (HPT: reliability of 99.97%, 1.02x slower at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-3.13.0.md)
- [📈time plot](bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.123x slower (HPT: reliability of 100.00%, 1.10x slower at 99th %ile)
- Memory usage: 1.21x
- [🧠memory plot](bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-base-mem.svg)
- [📄table](bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-base.md)
- [📈time plot](bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14815732722)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250503-linux-x86_64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d.json)

### vs. 3.10.4

- Geometric mean: 1.317x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 1.53x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250503-linux-x86_64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-3.10.4.md)
- [📈time plot](bm-20250503-linux-x86_64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.029x faster (HPT: reliability of 70.49%, 1.00x slower at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250503-linux-x86_64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-3.12.0.md)
- [📈time plot](bm-20250503-linux-x86_64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.041x slower (HPT: reliability of 99.76%, 1.01x slower at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250503-linux-x86_64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-3.13.0.md)
- [📈time plot](bm-20250503-linux-x86_64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.074x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: 1.18x
- [🧠memory plot](bm-20250503-linux-x86_64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-base-mem.svg)
- [📄table](bm-20250503-linux-x86_64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-base.md)
- [📈time plot](bm-20250503-linux-x86_64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14815732722)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250503-pythonperf2-x86_64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d.json)

### vs. 3.10.4

- Geometric mean: 1.239x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: 1.56x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: bpe_tokeniser, many_optionals, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250503-pythonperf2-x86_64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-3.10.4.md)
- [📈time plot](bm-20250503-pythonperf2-x86_64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.055x slower (HPT: reliability of 99.92%, 1.02x slower at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, many_optionals, pylint, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250503-pythonperf2-x86_64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-3.12.0.md)
- [📈time plot](bm-20250503-pythonperf2-x86_64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.034x slower (HPT: reliability of 99.03%, 1.00x slower at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, shortest_path, sphinx, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250503-pythonperf2-x86_64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-3.13.0.md)
- [📈time plot](bm-20250503-pythonperf2-x86_64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.085x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: 1.21x
- [🧠memory plot](bm-20250503-pythonperf2-x86_64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-base-mem.svg)
- [📄table](bm-20250503-pythonperf2-x86_64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-base.md)
- [📈time plot](bm-20250503-pythonperf2-x86_64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14815732722)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d.json)

### vs. 3.10.4

- Geometric mean: 1.170x faster (HPT: reliability of 99.97%, 1.05x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-3.10.4.md)
- [📈time plot](bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.010x faster (HPT: reliability of 96.00%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-3.12.0.md)
- [📈time plot](bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.041x slower (HPT: reliability of 99.95%, 1.05x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-3.13.0.md)
- [📈time plot](bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.088x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: unknown
- new benchmarks: thrift
- [📄table](bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-base.md)
- [📈time plot](bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14815732722)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250503-pythonperf1_win32-x86-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d.json)

### vs. 3.10.4

- Geometric mean: 1.030x faster (HPT: reliability of 51.61%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250503-pythonperf1_win32-x86-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-3.10.4.md)
- [📈time plot](bm-20250503-pythonperf1_win32-x86-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.062x faster (HPT: reliability of 99.40%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250503-pythonperf1_win32-x86-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-3.12.0.md)
- [📈time plot](bm-20250503-pythonperf1_win32-x86-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.088x slower (HPT: reliability of 100.00%, 1.08x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250503-pythonperf1_win32-x86-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-3.13.0.md)
- [📈time plot](bm-20250503-pythonperf1_win32-x86-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.122x slower (HPT: reliability of 100.00%, 1.08x slower at 99th %ile)
- Memory usage: unknown
- new benchmarks: thrift
- [📄table](bm-20250503-pythonperf1_win32-x86-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-base.md)
- [📈time plot](bm-20250503-pythonperf1_win32-x86-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14815732722)
- cpu model: missing
- platform: macOS-15.4-arm64-arm-64bit-Mach-O
- [raw results](bm-20250503-darwin-arm64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d.json)

### vs. 3.10.4

- Geometric mean: 1.201x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250503-darwin-arm64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-3.10.4.md)
- [📈time plot](bm-20250503-darwin-arm64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.040x slower (HPT: reliability of 99.09%, 1.00x slower at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250503-darwin-arm64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-3.12.0.md)
- [📈time plot](bm-20250503-darwin-arm64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.039x slower (HPT: reliability of 98.08%, 1.00x slower at 99th %ile)
- Memory usage: 1.23x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250503-darwin-arm64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-3.13.0.md)
- [📈time plot](bm-20250503-darwin-arm64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x faster (HPT: reliability of 92.63%, 1.00x slower at 99th %ile)
- Memory usage: 1.15x
- [🧠memory plot](bm-20250503-darwin-arm64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-base-mem.svg)
- [📄table](bm-20250503-darwin-arm64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-base.md)
- [📈time plot](bm-20250503-darwin-arm64-python-7363e8d24d14abf65163-3.14.0a7%2B-7363e8d-vs-base.svg)

