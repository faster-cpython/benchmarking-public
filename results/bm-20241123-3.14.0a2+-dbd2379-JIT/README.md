# Results

- fork: python/dbd23790dbd662169905
- version: 3.14.0a2+
- config: JIT
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

- Geometric mean: 1.193x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241123-arminc-aarch64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.10.4.md)
- [📈time plot](bm-20241123-arminc-aarch64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.063x slower (HPT: reliability of 99.99%, 1.02x slower at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241123-arminc-aarch64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.12.0.md)
- [📈time plot](bm-20241123-arminc-aarch64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.071x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log
- [📄table](bm-20241123-arminc-aarch64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.13.0.md)
- [📈time plot](bm-20241123-arminc-aarch64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.066x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20241123-arminc-aarch64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-base-mem.svg)
- [📄table](bm-20241123-arminc-aarch64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-base.md)
- [📈time plot](bm-20241123-arminc-aarch64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11991412016)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241123-linux-x86_64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379.json)

### vs. 3.10.4

- Geometric mean: 1.415x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241123-linux-x86_64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.10.4.md)
- [📈time plot](bm-20241123-linux-x86_64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.076x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241123-linux-x86_64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.12.0.md)
- [📈time plot](bm-20241123-linux-x86_64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.017x faster (HPT: reliability of 93.21%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241123-linux-x86_64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.13.0.md)
- [📈time plot](bm-20241123-linux-x86_64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.006x faster (HPT: reliability of 52.83%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20241123-linux-x86_64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-base-mem.svg)
- [📄table](bm-20241123-linux-x86_64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-base.md)
- [📈time plot](bm-20241123-linux-x86_64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11991412016)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20241123-pythonperf2-x86_64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379.json)

### vs. 3.10.4

- Geometric mean: 1.276x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241123-pythonperf2-x86_64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.10.4.md)
- [📈time plot](bm-20241123-pythonperf2-x86_64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.016x slower (HPT: reliability of 97.09%, 1.00x slower at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241123-pythonperf2-x86_64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.12.0.md)
- [📈time plot](bm-20241123-pythonperf2-x86_64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.009x slower (HPT: reliability of 86.04%, 1.00x slower at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241123-pythonperf2-x86_64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.13.0.md)
- [📈time plot](bm-20241123-pythonperf2-x86_64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.018x slower (HPT: reliability of 99.95%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20241123-pythonperf2-x86_64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-base-mem.svg)
- [📄table](bm-20241123-pythonperf2-x86_64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-base.md)
- [📈time plot](bm-20241123-pythonperf2-x86_64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11991412016)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379.json)

### vs. 3.10.4

- Geometric mean: 1.233x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.10.4.md)
- [📈time plot](bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.040x faster (HPT: reliability of 94.37%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.12.0.md)
- [📈time plot](bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.021x faster (HPT: reliability of 93.78%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.13.0.md)
- [📈time plot](bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.050x faster (HPT: reliability of 98.36%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-base.md)
- [📈time plot](bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11991412016)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241123-pythonperf1_win32-x86-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379.json)

### vs. 3.10.4

- Geometric mean: 1.053x faster (HPT: reliability of 55.25%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20241123-pythonperf1_win32-x86-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.10.4.md)
- [📈time plot](bm-20241123-pythonperf1_win32-x86-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.060x faster (HPT: reliability of 99.91%, 1.01x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20241123-pythonperf1_win32-x86-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.12.0.md)
- [📈time plot](bm-20241123-pythonperf1_win32-x86-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.046x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20241123-pythonperf1_win32-x86-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.13.0.md)
- [📈time plot](bm-20241123-pythonperf1_win32-x86-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.072x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241123-pythonperf1_win32-x86-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-base.md)
- [📈time plot](bm-20241123-pythonperf1_win32-x86-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11991412016)
- cpu model: missing
- platform: macOS-15.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241123-darwin-arm64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379.json)

### vs. 3.10.4

- Geometric mean: 1.227x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: 1.36x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20241123-darwin-arm64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.10.4.md)
- [📈time plot](bm-20241123-darwin-arm64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.027x faster (HPT: reliability of 94.10%, 1.00x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241123-darwin-arm64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.12.0.md)
- [📈time plot](bm-20241123-darwin-arm64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.030x faster (HPT: reliability of 95.65%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20241123-darwin-arm64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.13.0.md)
- [📈time plot](bm-20241123-darwin-arm64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.015x slower (HPT: reliability of 97.73%, 1.00x slower at 99th %ile)
- Memory usage: 1.03x
- [🧠memory plot](bm-20241123-darwin-arm64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-base-mem.svg)
- [📄table](bm-20241123-darwin-arm64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-base.md)
- [📈time plot](bm-20241123-darwin-arm64-python-dbd23790dbd662169905-3.14.0a2%2B-dbd2379-vs-base.svg)

