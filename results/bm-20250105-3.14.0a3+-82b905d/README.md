# Results

- fork: kumaraditya303/future_iter
- version: 3.14.0a3+
- config: 
- commit hash: [82b905d](https://github.com/kumaraditya303/cpython/commit/82b905d)
- commit date: 2025-01-05T17:40:30+00:00
- commit merge base: [2228e92da31ca7344a163498f848973a1b356597](https://github.com/python/cpython/commit/2228e92da31ca7344a163498f848973a1b356597)
- ref: future_iter

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12654182488)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250105-arminc-aarch64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d.json)

### vs. 3.10.4

- Geometric mean: 1.311x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250105-arminc-aarch64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-3.10.4.md)
- [📈time plot](bm-20250105-arminc-aarch64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.035x faster (HPT: reliability of 97.30%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250105-arminc-aarch64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-3.12.0.md)
- [📈time plot](bm-20250105-arminc-aarch64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.040x faster (HPT: reliability of 99.99%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log, mypy2
- [📄table](bm-20250105-arminc-aarch64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-3.13.0.md)
- [📈time plot](bm-20250105-arminc-aarch64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.004x faster (HPT: reliability of 99.99%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250105-arminc-aarch64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-base-mem.svg)
- [📄table](bm-20250105-arminc-aarch64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-base.md)
- [📈time plot](bm-20250105-arminc-aarch64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12654182488)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250105-linux-x86_64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d.json)

### vs. 3.10.4

- Geometric mean: 1.427x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250105-linux-x86_64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-3.10.4.md)
- [📈time plot](bm-20250105-linux-x86_64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.102x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250105-linux-x86_64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-3.12.0.md)
- [📈time plot](bm-20250105-linux-x86_64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.037x faster (HPT: reliability of 99.90%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250105-linux-x86_64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-3.13.0.md)
- [📈time plot](bm-20250105-linux-x86_64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x slower (HPT: reliability of 98.59%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250105-linux-x86_64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-base-mem.svg)
- [📄table](bm-20250105-linux-x86_64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-base.md)
- [📈time plot](bm-20250105-linux-x86_64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12654182488)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250105-pythonperf2-x86_64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d.json)

### vs. 3.10.4

- Geometric mean: 1.349x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250105-pythonperf2-x86_64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-3.10.4.md)
- [📈time plot](bm-20250105-pythonperf2-x86_64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.048x faster (HPT: reliability of 99.75%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250105-pythonperf2-x86_64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-3.12.0.md)
- [📈time plot](bm-20250105-pythonperf2-x86_64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.064x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250105-pythonperf2-x86_64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-3.13.0.md)
- [📈time plot](bm-20250105-pythonperf2-x86_64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.005x faster (HPT: reliability of 99.91%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250105-pythonperf2-x86_64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-base-mem.svg)
- [📄table](bm-20250105-pythonperf2-x86_64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-base.md)
- [📈time plot](bm-20250105-pythonperf2-x86_64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12654182488)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20250105-pythonperf1-amd64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d.json)

### vs. 3.10.4

- Geometric mean: 1.182x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250105-pythonperf1-amd64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-3.10.4.md)
- [📈time plot](bm-20250105-pythonperf1-amd64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.004x faster (HPT: reliability of 95.36%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250105-pythonperf1-amd64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-3.12.0.md)
- [📈time plot](bm-20250105-pythonperf1-amd64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.023x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250105-pythonperf1-amd64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-3.13.0.md)
- [📈time plot](bm-20250105-pythonperf1-amd64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.011x slower (HPT: reliability of 99.98%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- new benchmarks: mypy2
- [📄table](bm-20250105-pythonperf1-amd64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-base.md)
- [📈time plot](bm-20250105-pythonperf1-amd64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12654182488)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20250105-pythonperf1_win32-x86-kumaraditya303-future_iter-3.14.0a3%2B-82b905d.json)

### vs. 3.10.4

- Geometric mean: 1.175x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250105-pythonperf1_win32-x86-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-3.10.4.md)
- [📈time plot](bm-20250105-pythonperf1_win32-x86-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.184x faster (HPT: reliability of 100.00%, 1.15x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250105-pythonperf1_win32-x86-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-3.12.0.md)
- [📈time plot](bm-20250105-pythonperf1_win32-x86-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.055x faster (HPT: reliability of 71.13%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250105-pythonperf1_win32-x86-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-3.13.0.md)
- [📈time plot](bm-20250105-pythonperf1_win32-x86-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.004x faster (HPT: reliability of 93.62%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250105-pythonperf1_win32-x86-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-base.md)
- [📈time plot](bm-20250105-pythonperf1_win32-x86-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12654182488)
- cpu model: missing
- platform: macOS-15.2-arm64-arm-64bit-Mach-O
- [raw results](bm-20250105-darwin-arm64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d.json)

### vs. 3.10.4

- Geometric mean: 1.315x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, mypy2
- [📄table](bm-20250105-darwin-arm64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-3.10.4.md)
- [📈time plot](bm-20250105-darwin-arm64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.107x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250105-darwin-arm64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-3.12.0.md)
- [📈time plot](bm-20250105-darwin-arm64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.125x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250105-darwin-arm64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-3.13.0.md)
- [📈time plot](bm-20250105-darwin-arm64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x faster (HPT: reliability of 74.94%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250105-darwin-arm64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-base-mem.svg)
- [📄table](bm-20250105-darwin-arm64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-base.md)
- [📈time plot](bm-20250105-darwin-arm64-kumaraditya303-future_iter-3.14.0a3%2B-82b905d-vs-base.svg)

