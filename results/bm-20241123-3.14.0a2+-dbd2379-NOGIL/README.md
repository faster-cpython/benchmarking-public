# Results

- fork: python/dbd23790dbd662169905
- version: 3.14.0a2+
- config: NOGIL
- commit hash: [dbd2379](https://github.com/python/cpython/commit/dbd2379)
- commit date: 2024-11-23T16:41:01-05:00
- commit merge base: [e3038e976b25a58f512d8c7083a752c89436eb0d](https://github.com/python/cpython/commit/e3038e976b25a58f512d8c7083a752c89436eb0d)
- ref: dbd23790dbd662169905

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11991412016)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241123-arminc-aarch64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379.json)

### vs. 3.10.4

- Geometric mean: 1.150x slower (HPT: reliability of 100.00%, 1.15x slower at 99th %ile)
- Memory usage: 1.55x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241123-arminc-aarch64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.10.4.md)
- [📈time plot](bm-20241123-arminc-aarch64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.330x slower (HPT: reliability of 100.00%, 1.33x slower at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241123-arminc-aarch64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.12.0.md)
- [📈time plot](bm-20241123-arminc-aarch64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.334x slower (HPT: reliability of 100.00%, 1.31x slower at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20241123-arminc-aarch64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.13.0.md)
- [📈time plot](bm-20241123-arminc-aarch64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.329x slower (HPT: reliability of 100.00%, 1.32x slower at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20241123-arminc-aarch64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-base-mem.svg)
- [📄table](bm-20241123-arminc-aarch64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-base.md)
- [📈time plot](bm-20241123-arminc-aarch64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11991412016)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241123-linux-x86_64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379.json)

### vs. 3.10.4

- Geometric mean: 1.007x faster (HPT: reliability of 89.18%, 1.00x slower at 99th %ile)
- Memory usage: 1.49x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241123-linux-x86_64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.10.4.md)
- [📈time plot](bm-20241123-linux-x86_64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.222x slower (HPT: reliability of 100.00%, 1.19x slower at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241123-linux-x86_64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.12.0.md)
- [📈time plot](bm-20241123-linux-x86_64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.259x slower (HPT: reliability of 100.00%, 1.23x slower at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241123-linux-x86_64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.13.0.md)
- [📈time plot](bm-20241123-linux-x86_64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.265x slower (HPT: reliability of 100.00%, 1.24x slower at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20241123-linux-x86_64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-base-mem.svg)
- [📄table](bm-20241123-linux-x86_64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-base.md)
- [📈time plot](bm-20241123-linux-x86_64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11991412016)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20241123-pythonperf2-x86_64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379.json)

### vs. 3.10.4

- Geometric mean: 1.044x slower (HPT: reliability of 99.78%, 1.01x slower at 99th %ile)
- Memory usage: 1.52x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241123-pythonperf2-x86_64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.10.4.md)
- [📈time plot](bm-20241123-pythonperf2-x86_64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.257x slower (HPT: reliability of 100.00%, 1.21x slower at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241123-pythonperf2-x86_64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.12.0.md)
- [📈time plot](bm-20241123-pythonperf2-x86_64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.248x slower (HPT: reliability of 100.00%, 1.21x slower at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241123-pythonperf2-x86_64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.13.0.md)
- [📈time plot](bm-20241123-pythonperf2-x86_64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.254x slower (HPT: reliability of 100.00%, 1.22x slower at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20241123-pythonperf2-x86_64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-base-mem.svg)
- [📄table](bm-20241123-pythonperf2-x86_64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-base.md)
- [📈time plot](bm-20241123-pythonperf2-x86_64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11991412016)
- cpu model: missing
- platform: macOS-15.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241123-darwin-arm64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379.json)

### vs. 3.10.4

- Geometric mean: 1.023x slower (HPT: reliability of 98.83%, 1.00x slower at 99th %ile)
- Memory usage: 1.51x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20241123-darwin-arm64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.10.4.md)
- [📈time plot](bm-20241123-darwin-arm64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.170x slower (HPT: reliability of 99.99%, 1.06x slower at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241123-darwin-arm64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.12.0.md)
- [📈time plot](bm-20241123-darwin-arm64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.152x slower (HPT: reliability of 100.00%, 1.08x slower at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241123-darwin-arm64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.13.0.md)
- [📈time plot](bm-20241123-darwin-arm64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.186x slower (HPT: reliability of 100.00%, 1.10x slower at 99th %ile)
- Memory usage: 1.13x
- [🧠memory plot](bm-20241123-darwin-arm64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-base-mem.svg)
- [📄table](bm-20241123-darwin-arm64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-base.md)
- [📈time plot](bm-20241123-darwin-arm64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-base.svg)

