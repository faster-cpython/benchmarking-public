# Results

- fork: kumaraditya303/fast_state
- version: 3.14.0a3+
- config: NOGIL
- commit hash: [7de6e22](https://github.com/kumaraditya303/cpython/commit/7de6e22)
- commit date: 2025-01-07T13:18:23+00:00
- commit merge base: [2228e92da31ca7344a163498f848973a1b356597](https://github.com/python/cpython/commit/2228e92da31ca7344a163498f848973a1b356597)
- ref: fast_state

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12654396756)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22.json)

### vs. 3.10.4

- Geometric mean: 1.058x slower (HPT: reliability of 99.96%, 1.03x slower at 99th %ile)
- Memory usage: 1.55x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.10.4.md)
- [📈time plot](bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.252x slower (HPT: reliability of 100.00%, 1.23x slower at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.12.0.md)
- [📈time plot](bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.245x slower (HPT: reliability of 100.00%, 1.21x slower at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log, mypy2
- [📄table](bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.13.0.md)
- [📈time plot](bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x faster (HPT: reliability of 99.94%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-base-mem.svg)
- [📄table](bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-base.md)
- [📈time plot](bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12654396756)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22.json)

### vs. 3.10.4

- Geometric mean: 1.121x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.50x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.10.4.md)
- [📈time plot](bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.130x slower (HPT: reliability of 100.00%, 1.09x slower at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.12.0.md)
- [📈time plot](bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.178x slower (HPT: reliability of 100.00%, 1.14x slower at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.13.0.md)
- [📈time plot](bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x faster (HPT: reliability of 99.84%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-base-mem.svg)
- [📄table](bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-base.md)
- [📈time plot](bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12654396756)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22.json)

### vs. 3.10.4

- Geometric mean: 1.045x faster (HPT: reliability of 99.34%, 1.00x faster at 99th %ile)
- Memory usage: 1.53x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.10.4.md)
- [📈time plot](bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.184x slower (HPT: reliability of 100.00%, 1.13x slower at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.12.0.md)
- [📈time plot](bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.167x slower (HPT: reliability of 100.00%, 1.11x slower at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.13.0.md)
- [📈time plot](bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.005x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-base-mem.svg)
- [📄table](bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-base.md)
- [📈time plot](bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12654396756)
- cpu model: missing
- platform: macOS-15.2-arm64-arm-64bit-Mach-O
- [raw results](bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22.json)

### vs. 3.10.4

- Geometric mean: 1.081x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.53x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, mypy2
- [📄table](bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.10.4.md)
- [📈time plot](bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.084x slower (HPT: reliability of 99.56%, 1.01x slower at 99th %ile)
- Memory usage: 1.36x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.12.0.md)
- [📈time plot](bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.066x slower (HPT: reliability of 99.83%, 1.01x slower at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.13.0.md)
- [📈time plot](bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.004x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-base-mem.svg)
- [📄table](bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-base.md)
- [📈time plot](bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3%2B-7de6e22-vs-base.svg)

