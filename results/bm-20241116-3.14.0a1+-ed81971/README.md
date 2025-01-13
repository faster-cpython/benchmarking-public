# Results

- fork: python/ed81971e6b26c34445f0
- version: 3.14.0a1+
- config: 
- commit hash: [ed81971](https://github.com/python/cpython/commit/ed81971)
- commit date: 2024-11-16T18:01:52-05:00
- commit merge base: [2313f8421080ceb3343c6f5d291279adea85e073](https://github.com/python/cpython/commit/2313f8421080ceb3343c6f5d291279adea85e073)
- ref: ed81971e6b26c34445f0

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11874226481)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241116-arminc-aarch64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971.json)

### vs. 3.10.4

- Geometric mean: 1.286x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241116-arminc-aarch64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.10.4.md)
- [📈time plot](bm-20241116-arminc-aarch64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.000x faster (HPT: reliability of 51.14%, 1.00x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241116-arminc-aarch64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.12.0.md)
- [📈time plot](bm-20241116-arminc-aarch64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.011x slower (HPT: reliability of 99.52%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20241116-arminc-aarch64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.13.0.md)
- [📈time plot](bm-20241116-arminc-aarch64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x slower (HPT: reliability of 99.18%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241116-arminc-aarch64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-base-mem.svg)
- [📄table](bm-20241116-arminc-aarch64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-base.md)
- [📈time plot](bm-20241116-arminc-aarch64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-base.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20241116-azure-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-pystats.json)
- [pystats table](bm-20241116-azure-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11874226481)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241116-linux-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971.json)

### vs. 3.10.4

- Geometric mean: 1.403x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241116-linux-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.10.4.md)
- [📈time plot](bm-20241116-linux-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.063x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241116-linux-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.12.0.md)
- [📈time plot](bm-20241116-linux-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.007x faster (HPT: reliability of 88.35%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241116-linux-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.13.0.md)
- [📈time plot](bm-20241116-linux-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x slower (HPT: reliability of 86.55%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241116-linux-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-base-mem.svg)
- [📄table](bm-20241116-linux-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-base.md)
- [📈time plot](bm-20241116-linux-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11874226481)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20241116-pythonperf2-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971.json)

### vs. 3.10.4

- Geometric mean: 1.293x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241116-pythonperf2-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.10.4.md)
- [📈time plot](bm-20241116-pythonperf2-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.003x slower (HPT: reliability of 65.12%, 1.00x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241116-pythonperf2-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.12.0.md)
- [📈time plot](bm-20241116-pythonperf2-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.001x faster (HPT: reliability of 84.24%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241116-pythonperf2-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.13.0.md)
- [📈time plot](bm-20241116-pythonperf2-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.006x slower (HPT: reliability of 99.90%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20241116-pythonperf2-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-base-mem.svg)
- [📄table](bm-20241116-pythonperf2-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-base.md)
- [📈time plot](bm-20241116-pythonperf2-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11874226481)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971.json)

### vs. 3.10.4

- Geometric mean: 1.161x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.10.4.md)
- [📈time plot](bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.025x slower (HPT: reliability of 99.54%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.12.0.md)
- [📈time plot](bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.039x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.13.0.md)
- [📈time plot](bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x slower (HPT: reliability of 56.63%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-base.md)
- [📈time plot](bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11874226481)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241116-pythonperf1_win32-x86-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971.json)

### vs. 3.10.4

- Geometric mean: 1.134x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241116-pythonperf1_win32-x86-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.10.4.md)
- [📈time plot](bm-20241116-pythonperf1_win32-x86-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.136x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241116-pythonperf1_win32-x86-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.12.0.md)
- [📈time plot](bm-20241116-pythonperf1_win32-x86-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.023x faster (HPT: reliability of 99.83%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20241116-pythonperf1_win32-x86-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.13.0.md)
- [📈time plot](bm-20241116-pythonperf1_win32-x86-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x slower (HPT: reliability of 99.78%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241116-pythonperf1_win32-x86-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-base.md)
- [📈time plot](bm-20241116-pythonperf1_win32-x86-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11874226481)
- cpu model: missing
- platform: macOS-15.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241116-darwin-arm64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971.json)

### vs. 3.10.4

- Geometric mean: 1.245x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20241116-darwin-arm64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.10.4.md)
- [📈time plot](bm-20241116-darwin-arm64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.038x faster (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241116-darwin-arm64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.12.0.md)
- [📈time plot](bm-20241116-darwin-arm64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.041x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241116-darwin-arm64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.13.0.md)
- [📈time plot](bm-20241116-darwin-arm64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x slower (HPT: reliability of 73.65%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241116-darwin-arm64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-base-mem.svg)
- [📄table](bm-20241116-darwin-arm64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-base.md)
- [📈time plot](bm-20241116-darwin-arm64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-base.svg)

