# Results

- fork: python/3f2cfd0462e13368092a
- version: 3.14.0a4+
- config: NOGIL
- commit hash: [3f2cfd0](https://github.com/python/cpython/commit/3f2cfd0)
- commit date: 2025-01-25T23:50:09+05:30
- commit merge base: [be98fda7c6698e8468afd528c864aca1f532af59](https://github.com/python/cpython/commit/be98fda7c6698e8468afd528c864aca1f532af59)
- ref: 3f2cfd0462e13368092a

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12969510537)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250125-arminc-aarch64-python-3f2cfd0462e13368092a-3.14.0a4%2B-3f2cfd0.json)

### vs. 3.10.4

- Geometric mean: 1.088x faster (HPT: reliability of 99.87%, 1.01x faster at 99th %ile)
- Memory usage: 1.57x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence
- [📄table](bm-20250125-arminc-aarch64-python-3f2cfd0462e13368092a-3.14.0a4%2B-3f2cfd0-vs-3.10.4.md)
- [📈time plot](bm-20250125-arminc-aarch64-python-3f2cfd0462e13368092a-3.14.0a4%2B-3f2cfd0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.133x slower (HPT: reliability of 100.00%, 1.11x slower at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence
- [📄table](bm-20250125-arminc-aarch64-python-3f2cfd0462e13368092a-3.14.0a4%2B-3f2cfd0-vs-3.12.0.md)
- [📈time plot](bm-20250125-arminc-aarch64-python-3f2cfd0462e13368092a-3.14.0a4%2B-3f2cfd0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.135x slower (HPT: reliability of 100.00%, 1.10x slower at 99th %ile)
- Memory usage: 1.23x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250125-arminc-aarch64-python-3f2cfd0462e13368092a-3.14.0a4%2B-3f2cfd0-vs-3.13.0.md)
- [📈time plot](bm-20250125-arminc-aarch64-python-3f2cfd0462e13368092a-3.14.0a4%2B-3f2cfd0-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.168x slower (HPT: reliability of 100.00%, 1.16x slower at 99th %ile)
- Memory usage: 1.20x
- [🧠memory plot](bm-20250125-arminc-aarch64-python-3f2cfd0462e13368092a-3.14.0a4%2B-3f2cfd0-vs-base-mem.svg)
- [📄table](bm-20250125-arminc-aarch64-python-3f2cfd0462e13368092a-3.14.0a4%2B-3f2cfd0-vs-base.md)
- [📈time plot](bm-20250125-arminc-aarch64-python-3f2cfd0462e13368092a-3.14.0a4%2B-3f2cfd0-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12969510537)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250125-linux-x86_64-python-3f2cfd0462e13368092a-3.14.0a4%2B-3f2cfd0.json)

### vs. 3.10.4

- Geometric mean: 1.229x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: 1.51x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250125-linux-x86_64-python-3f2cfd0462e13368092a-3.14.0a4%2B-3f2cfd0-vs-3.10.4.md)
- [📈time plot](bm-20250125-linux-x86_64-python-3f2cfd0462e13368092a-3.14.0a4%2B-3f2cfd0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.045x slower (HPT: reliability of 99.97%, 1.03x slower at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250125-linux-x86_64-python-3f2cfd0462e13368092a-3.14.0a4%2B-3f2cfd0-vs-3.12.0.md)
- [📈time plot](bm-20250125-linux-x86_64-python-3f2cfd0462e13368092a-3.14.0a4%2B-3f2cfd0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.106x slower (HPT: reliability of 100.00%, 1.08x slower at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250125-linux-x86_64-python-3f2cfd0462e13368092a-3.14.0a4%2B-3f2cfd0-vs-3.13.0.md)
- [📈time plot](bm-20250125-linux-x86_64-python-3f2cfd0462e13368092a-3.14.0a4%2B-3f2cfd0-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.147x slower (HPT: reliability of 100.00%, 1.12x slower at 99th %ile)
- Memory usage: 1.19x
- [🧠memory plot](bm-20250125-linux-x86_64-python-3f2cfd0462e13368092a-3.14.0a4%2B-3f2cfd0-vs-base-mem.svg)
- [📄table](bm-20250125-linux-x86_64-python-3f2cfd0462e13368092a-3.14.0a4%2B-3f2cfd0-vs-base.md)
- [📈time plot](bm-20250125-linux-x86_64-python-3f2cfd0462e13368092a-3.14.0a4%2B-3f2cfd0-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12969510537)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250125-pythonperf2-x86_64-python-3f2cfd0462e13368092a-3.14.0a4%2B-3f2cfd0.json)

### vs. 3.10.4

- Geometric mean: 1.182x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.53x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250125-pythonperf2-x86_64-python-3f2cfd0462e13368092a-3.14.0a4%2B-3f2cfd0-vs-3.10.4.md)
- [📈time plot](bm-20250125-pythonperf2-x86_64-python-3f2cfd0462e13368092a-3.14.0a4%2B-3f2cfd0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.075x slower (HPT: reliability of 99.95%, 1.03x slower at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250125-pythonperf2-x86_64-python-3f2cfd0462e13368092a-3.14.0a4%2B-3f2cfd0-vs-3.12.0.md)
- [📈time plot](bm-20250125-pythonperf2-x86_64-python-3f2cfd0462e13368092a-3.14.0a4%2B-3f2cfd0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.065x slower (HPT: reliability of 99.95%, 1.02x slower at 99th %ile)
- Memory usage: 1.23x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250125-pythonperf2-x86_64-python-3f2cfd0462e13368092a-3.14.0a4%2B-3f2cfd0-vs-3.13.0.md)
- [📈time plot](bm-20250125-pythonperf2-x86_64-python-3f2cfd0462e13368092a-3.14.0a4%2B-3f2cfd0-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.119x slower (HPT: reliability of 100.00%, 1.10x slower at 99th %ile)
- Memory usage: 1.20x
- [🧠memory plot](bm-20250125-pythonperf2-x86_64-python-3f2cfd0462e13368092a-3.14.0a4%2B-3f2cfd0-vs-base-mem.svg)
- [📄table](bm-20250125-pythonperf2-x86_64-python-3f2cfd0462e13368092a-3.14.0a4%2B-3f2cfd0-vs-base.md)
- [📈time plot](bm-20250125-pythonperf2-x86_64-python-3f2cfd0462e13368092a-3.14.0a4%2B-3f2cfd0-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12969510537)
- cpu model: missing
- platform: macOS-15.2-arm64-arm-64bit-Mach-O
- [raw results](bm-20250125-darwin-arm64-python-3f2cfd0462e13368092a-3.14.0a4%2B-3f2cfd0.json)

### vs. 3.10.4

- Geometric mean: 1.295x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250125-darwin-arm64-python-3f2cfd0462e13368092a-3.14.0a4%2B-3f2cfd0-vs-3.10.4.md)
- [📈time plot](bm-20250125-darwin-arm64-python-3f2cfd0462e13368092a-3.14.0a4%2B-3f2cfd0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.029x faster (HPT: reliability of 57.09%, 1.00x slower at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250125-darwin-arm64-python-3f2cfd0462e13368092a-3.14.0a4%2B-3f2cfd0-vs-3.12.0.md)
- [📈time plot](bm-20250125-darwin-arm64-python-3f2cfd0462e13368092a-3.14.0a4%2B-3f2cfd0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.032x faster (HPT: reliability of 92.37%, 1.00x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250125-darwin-arm64-python-3f2cfd0462e13368092a-3.14.0a4%2B-3f2cfd0-vs-3.13.0.md)
- [📈time plot](bm-20250125-darwin-arm64-python-3f2cfd0462e13368092a-3.14.0a4%2B-3f2cfd0-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.060x slower (HPT: reliability of 99.99%, 1.03x slower at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: 🔴 dask
- [🧠memory plot](bm-20250125-darwin-arm64-python-3f2cfd0462e13368092a-3.14.0a4%2B-3f2cfd0-vs-base-mem.svg)
- [📄table](bm-20250125-darwin-arm64-python-3f2cfd0462e13368092a-3.14.0a4%2B-3f2cfd0-vs-base.md)
- [📈time plot](bm-20250125-darwin-arm64-python-3f2cfd0462e13368092a-3.14.0a4%2B-3f2cfd0-vs-base.svg)

