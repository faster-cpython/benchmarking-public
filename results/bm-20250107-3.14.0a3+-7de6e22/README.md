# Results

- fork: kumaraditya303/fast_state
- version: 3.14.0a3+
- config: 
- commit hash: [7de6e22](https://github.com/kumaraditya303/cpython/commit/7de6e22)
- commit date: 2025-01-07T13:18:23+00:00
- commit merge base: [2228e92da31ca7344a163498f848973a1b356597](https://github.com/python/cpython/commit/2228e92da31ca7344a163498f848973a1b356597)
- ref: fast_state

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12654392642)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22.json)

### vs. 3.10.4

- Geometric mean: 1.308x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.10.4.md)
- [📈time plot](bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.033x faster (HPT: reliability of 93.44%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.12.0.md)
- [📈time plot](bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.036x faster (HPT: reliability of 99.77%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log, mypy2
- [📄table](bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.13.0.md)
- [📈time plot](bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x faster (HPT: reliability of 97.12%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-base-mem.svg)
- [📄table](bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-base.md)
- [📈time plot](bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12654392642)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22.json)

### vs. 3.10.4

- Geometric mean: 1.430x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.10.4.md)
- [📈time plot](bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.103x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.12.0.md)
- [📈time plot](bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.039x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.13.0.md)
- [📈time plot](bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x faster (HPT: reliability of 89.66%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-base-mem.svg)
- [📄table](bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-base.md)
- [📈time plot](bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12654392642)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22.json)

### vs. 3.10.4

- Geometric mean: 1.353x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.10.4.md)
- [📈time plot](bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.053x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.12.0.md)
- [📈time plot](bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.068x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.13.0.md)
- [📈time plot](bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.008x faster (HPT: reliability of 99.99%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-base-mem.svg)
- [📄table](bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-base.md)
- [📈time plot](bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12654392642)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20250107-pythonperf1-amd64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22.json)

### vs. 3.10.4

- Geometric mean: 1.192x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250107-pythonperf1-amd64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.10.4.md)
- [📈time plot](bm-20250107-pythonperf1-amd64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.014x faster (HPT: reliability of 90.36%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250107-pythonperf1-amd64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.12.0.md)
- [📈time plot](bm-20250107-pythonperf1-amd64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.013x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250107-pythonperf1-amd64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.13.0.md)
- [📈time plot](bm-20250107-pythonperf1-amd64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x slower (HPT: reliability of 98.10%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- new benchmarks: mypy2
- [📄table](bm-20250107-pythonperf1-amd64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-base.md)
- [📈time plot](bm-20250107-pythonperf1-amd64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12654392642)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20250107-pythonperf1_win32-x86-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22.json)

### vs. 3.10.4

- Geometric mean: 1.163x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250107-pythonperf1_win32-x86-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.10.4.md)
- [📈time plot](bm-20250107-pythonperf1_win32-x86-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.174x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250107-pythonperf1_win32-x86-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.12.0.md)
- [📈time plot](bm-20250107-pythonperf1_win32-x86-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.047x faster (HPT: reliability of 53.93%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250107-pythonperf1_win32-x86-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.13.0.md)
- [📈time plot](bm-20250107-pythonperf1_win32-x86-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.003x slower (HPT: reliability of 58.46%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250107-pythonperf1_win32-x86-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-base.md)
- [📈time plot](bm-20250107-pythonperf1_win32-x86-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12654392642)
- cpu model: missing
- platform: macOS-15.2-arm64-arm-64bit-Mach-O
- [raw results](bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22.json)

### vs. 3.10.4

- Geometric mean: 1.317x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, mypy2
- [📄table](bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.10.4.md)
- [📈time plot](bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.109x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.12.0.md)
- [📈time plot](bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.127x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.13.0.md)
- [📈time plot](bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.003x faster (HPT: reliability of 98.27%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-base-mem.svg)
- [📄table](bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-base.md)
- [📈time plot](bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-base.svg)

