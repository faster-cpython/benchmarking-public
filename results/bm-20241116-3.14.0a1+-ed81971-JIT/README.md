# Results

- fork: python/ed81971e6b26c34445f0
- version: 3.14.0a1+
- config: JIT
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

- Geometric mean: 1.164x faster (HPT: reliability of 99.98%, 1.03x faster at 99th %ile)
- Memory usage: 1.38x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241116-arminc-aarch64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.10.4.md)
- [📈time plot](bm-20241116-arminc-aarch64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.085x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241116-arminc-aarch64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.12.0.md)
- [📈time plot](bm-20241116-arminc-aarch64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.099x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20241116-arminc-aarch64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.13.0.md)
- [📈time plot](bm-20241116-arminc-aarch64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.084x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.07x
- [🧠memory plot](bm-20241116-arminc-aarch64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-base-mem.svg)
- [📄table](bm-20241116-arminc-aarch64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-base.md)
- [📈time plot](bm-20241116-arminc-aarch64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11874226481)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241116-linux-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971.json)

### vs. 3.10.4

- Geometric mean: 1.387x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241116-linux-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.10.4.md)
- [📈time plot](bm-20241116-linux-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.059x faster (HPT: reliability of 99.97%, 1.01x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241116-linux-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.12.0.md)
- [📈time plot](bm-20241116-linux-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.003x slower (HPT: reliability of 89.21%, 1.00x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241116-linux-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.13.0.md)
- [📈time plot](bm-20241116-linux-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x faster (HPT: reliability of 99.98%, 1.00x faster at 99th %ile)
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

- Geometric mean: 1.257x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: 1.35x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241116-pythonperf2-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.10.4.md)
- [📈time plot](bm-20241116-pythonperf2-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.027x slower (HPT: reliability of 95.87%, 1.00x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241116-pythonperf2-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.12.0.md)
- [📈time plot](bm-20241116-pythonperf2-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.023x slower (HPT: reliability of 95.23%, 1.00x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241116-pythonperf2-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.13.0.md)
- [📈time plot](bm-20241116-pythonperf2-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.025x slower (HPT: reliability of 99.36%, 1.00x slower at 99th %ile)
- Memory usage: 1.06x
- [🧠memory plot](bm-20241116-pythonperf2-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-base-mem.svg)
- [📄table](bm-20241116-pythonperf2-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-base.md)
- [📈time plot](bm-20241116-pythonperf2-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11874226481)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971.json)

### vs. 3.10.4

- Geometric mean: 1.213x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.10.4.md)
- [📈time plot](bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.026x faster (HPT: reliability of 90.36%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.12.0.md)
- [📈time plot](bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.002x faster (HPT: reliability of 92.67%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.13.0.md)
- [📈time plot](bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.042x faster (HPT: reliability of 98.66%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-base.md)
- [📈time plot](bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11874226481)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241116-pythonperf1_win32-x86-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971.json)

### vs. 3.10.4

- Geometric mean: 1.038x faster (HPT: reliability of 50.89%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241116-pythonperf1_win32-x86-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.10.4.md)
- [📈time plot](bm-20241116-pythonperf1_win32-x86-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.046x faster (HPT: reliability of 99.53%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241116-pythonperf1_win32-x86-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.12.0.md)
- [📈time plot](bm-20241116-pythonperf1_win32-x86-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.063x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20241116-pythonperf1_win32-x86-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.13.0.md)
- [📈time plot](bm-20241116-pythonperf1_win32-x86-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.082x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241116-pythonperf1_win32-x86-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-base.md)
- [📈time plot](bm-20241116-pythonperf1_win32-x86-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11874226481)
- cpu model: missing
- platform: macOS-15.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241116-darwin-arm64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971.json)

### vs. 3.10.4

- Geometric mean: 1.212x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: 1.44x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20241116-darwin-arm64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.10.4.md)
- [📈time plot](bm-20241116-darwin-arm64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.017x faster (HPT: reliability of 86.08%, 1.00x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241116-darwin-arm64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.12.0.md)
- [📈time plot](bm-20241116-darwin-arm64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.018x faster (HPT: reliability of 87.19%, 1.00x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241116-darwin-arm64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.13.0.md)
- [📈time plot](bm-20241116-darwin-arm64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.023x slower (HPT: reliability of 99.46%, 1.00x slower at 99th %ile)
- Memory usage: 1.08x
- [🧠memory plot](bm-20241116-darwin-arm64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-base-mem.svg)
- [📄table](bm-20241116-darwin-arm64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-base.md)
- [📈time plot](bm-20241116-darwin-arm64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-base.svg)

