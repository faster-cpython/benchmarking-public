# Results

- fork: python/ed81971e6b26c34445f0
- version: 3.14.0a1+
- config: NOGIL
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

- Geometric mean: 1.207x slower (HPT: reliability of 100.00%, 1.22x slower at 99th %ile)
- Memory usage: 1.55x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241116-arminc-aarch64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.10.4.md)
- [📈time plot](bm-20241116-arminc-aarch64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.373x slower (HPT: reliability of 100.00%, 1.41x slower at 99th %ile)
- Memory usage: 1.23x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241116-arminc-aarch64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.12.0.md)
- [📈time plot](bm-20241116-arminc-aarch64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.376x slower (HPT: reliability of 100.00%, 1.39x slower at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20241116-arminc-aarch64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.13.0.md)
- [📈time plot](bm-20241116-arminc-aarch64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.366x slower (HPT: reliability of 100.00%, 1.38x slower at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20241116-arminc-aarch64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-base-mem.svg)
- [📄table](bm-20241116-arminc-aarch64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-base.md)
- [📈time plot](bm-20241116-arminc-aarch64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11874226481)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241116-linux-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971.json)

### vs. 3.10.4

- Geometric mean: 1.045x slower (HPT: reliability of 99.99%, 1.01x slower at 99th %ile)
- Memory usage: 1.49x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241116-linux-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.10.4.md)
- [📈time plot](bm-20241116-linux-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.261x slower (HPT: reliability of 100.00%, 1.23x slower at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241116-linux-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.12.0.md)
- [📈time plot](bm-20241116-linux-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.296x slower (HPT: reliability of 100.00%, 1.28x slower at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241116-linux-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.13.0.md)
- [📈time plot](bm-20241116-linux-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.299x slower (HPT: reliability of 100.00%, 1.29x slower at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20241116-linux-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-base-mem.svg)
- [📄table](bm-20241116-linux-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-base.md)
- [📈time plot](bm-20241116-linux-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11874226481)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20241116-pythonperf2-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971.json)

### vs. 3.10.4

- Geometric mean: 1.110x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: 1.52x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241116-pythonperf2-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.10.4.md)
- [📈time plot](bm-20241116-pythonperf2-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.306x slower (HPT: reliability of 100.00%, 1.27x slower at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241116-pythonperf2-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.12.0.md)
- [📈time plot](bm-20241116-pythonperf2-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.297x slower (HPT: reliability of 100.00%, 1.26x slower at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241116-pythonperf2-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.13.0.md)
- [📈time plot](bm-20241116-pythonperf2-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.295x slower (HPT: reliability of 100.00%, 1.29x slower at 99th %ile)
- Memory usage: 1.20x
- [🧠memory plot](bm-20241116-pythonperf2-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-base-mem.svg)
- [📄table](bm-20241116-pythonperf2-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-base.md)
- [📈time plot](bm-20241116-pythonperf2-x86_64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11874226481)
- cpu model: missing
- platform: macOS-15.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241116-darwin-arm64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971.json)

### vs. 3.10.4

- Geometric mean: 1.095x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: 1.51x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20241116-darwin-arm64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.10.4.md)
- [📈time plot](bm-20241116-darwin-arm64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.228x slower (HPT: reliability of 100.00%, 1.13x slower at 99th %ile)
- Memory usage: 1.35x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241116-darwin-arm64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.12.0.md)
- [📈time plot](bm-20241116-darwin-arm64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.210x slower (HPT: reliability of 100.00%, 1.14x slower at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241116-darwin-arm64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.13.0.md)
- [📈time plot](bm-20241116-darwin-arm64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.239x slower (HPT: reliability of 100.00%, 1.18x slower at 99th %ile)
- Memory usage: 1.13x
- [🧠memory plot](bm-20241116-darwin-arm64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-base-mem.svg)
- [📄table](bm-20241116-darwin-arm64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-base.md)
- [📈time plot](bm-20241116-darwin-arm64-python-ed81971e6b26c34445f0-3.14.0a1%2B-ed81971-vs-base.svg)

