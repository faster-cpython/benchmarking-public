# Results

- fork: python/a3990df6121880e8c678
- version: 3.14.0a5+
- config: NOGIL
- commit hash: [a3990df](https://github.com/python/cpython/commit/a3990df)
- commit date: 2025-03-08T16:37:05-05:00
- commit merge base: [edd1eca336976b3431cf636aea87f08a40c94935](https://github.com/python/cpython/commit/edd1eca336976b3431cf636aea87f08a40c94935)
- ref: a3990df6121880e8c678

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13742662531)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df.json)

### vs. 3.10.4

- Geometric mean: 1.145x faster (HPT: reliability of 99.99%, 1.04x faster at 99th %ile)
- Memory usage: 1.58x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence
- [📄table](bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.10.4.md)
- [📈time plot](bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.090x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence
- [📄table](bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.12.0.md)
- [📈time plot](bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.095x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.13.0.md)
- [📈time plot](bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.155x slower (HPT: reliability of 100.00%, 1.14x slower at 99th %ile)
- Memory usage: 1.21x
- [🧠memory plot](bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-base-mem.svg)
- [📄table](bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-base.md)
- [📈time plot](bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13742662531)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-205-generic-x86_64-with-glibc2.31
- [raw results](bm-20250308-linux-x86_64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df.json)

### vs. 3.10.4

- Geometric mean: 1.276x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: 1.52x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250308-linux-x86_64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.10.4.md)
- [📈time plot](bm-20250308-linux-x86_64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.007x slower (HPT: reliability of 99.74%, 1.00x slower at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250308-linux-x86_64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.12.0.md)
- [📈time plot](bm-20250308-linux-x86_64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.072x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250308-linux-x86_64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.13.0.md)
- [📈time plot](bm-20250308-linux-x86_64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.111x slower (HPT: reliability of 100.00%, 1.10x slower at 99th %ile)
- Memory usage: 1.19x
- [🧠memory plot](bm-20250308-linux-x86_64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-base-mem.svg)
- [📄table](bm-20250308-linux-x86_64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-base.md)
- [📈time plot](bm-20250308-linux-x86_64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13742662531)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250308-pythonperf2-x86_64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df.json)

### vs. 3.10.4

- Geometric mean: 1.205x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: 1.55x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250308-pythonperf2-x86_64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.10.4.md)
- [📈time plot](bm-20250308-pythonperf2-x86_64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.055x slower (HPT: reliability of 99.94%, 1.03x slower at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250308-pythonperf2-x86_64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.12.0.md)
- [📈time plot](bm-20250308-pythonperf2-x86_64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.047x slower (HPT: reliability of 99.94%, 1.02x slower at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250308-pythonperf2-x86_64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.13.0.md)
- [📈time plot](bm-20250308-pythonperf2-x86_64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.086x slower (HPT: reliability of 100.00%, 1.08x slower at 99th %ile)
- Memory usage: 1.21x
- [🧠memory plot](bm-20250308-pythonperf2-x86_64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-base-mem.svg)
- [📄table](bm-20250308-pythonperf2-x86_64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-base.md)
- [📈time plot](bm-20250308-pythonperf2-x86_64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13742662531)
- cpu model: missing
- platform: macOS-15.3-arm64-arm-64bit-Mach-O
- [raw results](bm-20250308-darwin-arm64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df.json)

### vs. 3.10.4

- Geometric mean: 1.204x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250308-darwin-arm64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.10.4.md)
- [📈time plot](bm-20250308-darwin-arm64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.042x slower (HPT: reliability of 99.93%, 1.01x slower at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250308-darwin-arm64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.12.0.md)
- [📈time plot](bm-20250308-darwin-arm64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.039x slower (HPT: reliability of 99.84%, 1.01x slower at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250308-darwin-arm64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.13.0.md)
- [📈time plot](bm-20250308-darwin-arm64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.030x slower (HPT: reliability of 99.94%, 1.01x slower at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: 🔴 dask
- [🧠memory plot](bm-20250308-darwin-arm64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-base-mem.svg)
- [📄table](bm-20250308-darwin-arm64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-base.md)
- [📈time plot](bm-20250308-darwin-arm64-python-a3990df6121880e8c678-3.14.0a5%2B-a3990df-vs-base.svg)

