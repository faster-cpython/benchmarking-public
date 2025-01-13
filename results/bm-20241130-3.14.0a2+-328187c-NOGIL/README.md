# Results

- fork: python/328187cc4fcdd578db42
- version: 3.14.0a2+
- config: NOGIL
- commit hash: [328187c](https://github.com/python/cpython/commit/328187c)
- commit date: 2024-11-30T18:39:39+00:00
- commit merge base: [4e0a4cafe8d8ecb43db62aed1d5671af583104e7](https://github.com/python/cpython/commit/4e0a4cafe8d8ecb43db62aed1d5671af583104e7)
- ref: 328187cc4fcdd578db42

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12100442442)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c.json)

### vs. 3.10.4

- Geometric mean: 1.149x slower (HPT: reliability of 100.00%, 1.15x slower at 99th %ile)
- Memory usage: 1.55x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.10.4.md)
- [📈time plot](bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.328x slower (HPT: reliability of 100.00%, 1.32x slower at 99th %ile)
- Memory usage: 1.23x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.12.0.md)
- [📈time plot](bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.332x slower (HPT: reliability of 100.00%, 1.31x slower at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.13.0.md)
- [📈time plot](bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.329x slower (HPT: reliability of 100.00%, 1.31x slower at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-base-mem.svg)
- [📄table](bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-base.md)
- [📈time plot](bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12100442442)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241130-linux-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c.json)

### vs. 3.10.4

- Geometric mean: 1.018x faster (HPT: reliability of 79.17%, 1.00x slower at 99th %ile)
- Memory usage: 1.49x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241130-linux-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.10.4.md)
- [📈time plot](bm-20241130-linux-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.214x slower (HPT: reliability of 100.00%, 1.17x slower at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241130-linux-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.12.0.md)
- [📈time plot](bm-20241130-linux-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.251x slower (HPT: reliability of 100.00%, 1.22x slower at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241130-linux-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.13.0.md)
- [📈time plot](bm-20241130-linux-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.258x slower (HPT: reliability of 100.00%, 1.23x slower at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20241130-linux-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-base-mem.svg)
- [📄table](bm-20241130-linux-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-base.md)
- [📈time plot](bm-20241130-linux-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12100442442)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c.json)

### vs. 3.10.4

- Geometric mean: 1.037x slower (HPT: reliability of 99.64%, 1.00x slower at 99th %ile)
- Memory usage: 1.52x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.10.4.md)
- [📈time plot](bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.251x slower (HPT: reliability of 100.00%, 1.20x slower at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.12.0.md)
- [📈time plot](bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.242x slower (HPT: reliability of 100.00%, 1.19x slower at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.13.0.md)
- [📈time plot](bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.247x slower (HPT: reliability of 100.00%, 1.20x slower at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-base-mem.svg)
- [📄table](bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-base.md)
- [📈time plot](bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12100442442)
- cpu model: missing
- platform: macOS-15.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c.json)

### vs. 3.10.4

- Geometric mean: 1.023x slower (HPT: reliability of 99.46%, 1.00x slower at 99th %ile)
- Memory usage: 1.51x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.10.4.md)
- [📈time plot](bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.170x slower (HPT: reliability of 99.99%, 1.05x slower at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.12.0.md)
- [📈time plot](bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.151x slower (HPT: reliability of 100.00%, 1.08x slower at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.13.0.md)
- [📈time plot](bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.182x slower (HPT: reliability of 100.00%, 1.10x slower at 99th %ile)
- Memory usage: 1.14x
- [🧠memory plot](bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-base-mem.svg)
- [📄table](bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-base.md)
- [📈time plot](bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2%2B-328187c-vs-base.svg)

