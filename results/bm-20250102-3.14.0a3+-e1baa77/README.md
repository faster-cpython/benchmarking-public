# Results

- fork: python/e1baa778f602ede66831
- version: 3.14.0a3+
- config: 
- commit hash: [e1baa77](https://github.com/python/cpython/commit/e1baa77)
- commit date: 2025-01-02T11:45:07+02:00
- commit merge base: [60c65184695a3eab766b3bc26fc99f695deb998f](https://github.com/python/cpython/commit/60c65184695a3eab766b3bc26fc99f695deb998f)
- ref: e1baa778f602ede66831

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12585926978)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250102-arminc-aarch64-python-e1baa778f602ede66831-3.14.0a3%2B-e1baa77.json)

### vs. 3.10.4

- Geometric mean: 1.313x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250102-arminc-aarch64-python-e1baa778f602ede66831-3.14.0a3%2B-e1baa77-vs-3.10.4.md)
- [📈time plot](bm-20250102-arminc-aarch64-python-e1baa778f602ede66831-3.14.0a3%2B-e1baa77-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.034x faster (HPT: reliability of 98.83%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250102-arminc-aarch64-python-e1baa778f602ede66831-3.14.0a3%2B-e1baa77-vs-3.12.0.md)
- [📈time plot](bm-20250102-arminc-aarch64-python-e1baa778f602ede66831-3.14.0a3%2B-e1baa77-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.038x faster (HPT: reliability of 99.99%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: dulwich_log, mypy2
- [📄table](bm-20250102-arminc-aarch64-python-e1baa778f602ede66831-3.14.0a3%2B-e1baa77-vs-3.13.0.md)
- [📈time plot](bm-20250102-arminc-aarch64-python-e1baa778f602ede66831-3.14.0a3%2B-e1baa77-vs-3.13.0.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12696203820)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250102-linux-x86_64-python-e1baa778f602ede66831-3.14.0a3%2B-e1baa77.json)

### vs. 3.10.4

- Geometric mean: 1.433x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250102-linux-x86_64-python-e1baa778f602ede66831-3.14.0a3%2B-e1baa77-vs-3.10.4.md)
- [📈time plot](bm-20250102-linux-x86_64-python-e1baa778f602ede66831-3.14.0a3%2B-e1baa77-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.104x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250102-linux-x86_64-python-e1baa778f602ede66831-3.14.0a3%2B-e1baa77-vs-3.12.0.md)
- [📈time plot](bm-20250102-linux-x86_64-python-e1baa778f602ede66831-3.14.0a3%2B-e1baa77-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.038x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250102-linux-x86_64-python-e1baa778f602ede66831-3.14.0a3%2B-e1baa77-vs-3.13.0.md)
- [📈time plot](bm-20250102-linux-x86_64-python-e1baa778f602ede66831-3.14.0a3%2B-e1baa77-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12585926978)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250102-pythonperf2-x86_64-python-e1baa778f602ede66831-3.14.0a3%2B-e1baa77.json)

### vs. 3.10.4

- Geometric mean: 1.341x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250102-pythonperf2-x86_64-python-e1baa778f602ede66831-3.14.0a3%2B-e1baa77-vs-3.10.4.md)
- [📈time plot](bm-20250102-pythonperf2-x86_64-python-e1baa778f602ede66831-3.14.0a3%2B-e1baa77-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.042x faster (HPT: reliability of 99.80%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250102-pythonperf2-x86_64-python-e1baa778f602ede66831-3.14.0a3%2B-e1baa77-vs-3.12.0.md)
- [📈time plot](bm-20250102-pythonperf2-x86_64-python-e1baa778f602ede66831-3.14.0a3%2B-e1baa77-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.057x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250102-pythonperf2-x86_64-python-e1baa778f602ede66831-3.14.0a3%2B-e1baa77-vs-3.13.0.md)
- [📈time plot](bm-20250102-pythonperf2-x86_64-python-e1baa778f602ede66831-3.14.0a3%2B-e1baa77-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12585926978)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20250102-pythonperf1-amd64-python-e1baa778f602ede66831-3.14.0a3%2B-e1baa77.json)

### vs. 3.10.4

- Geometric mean: 1.195x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250102-pythonperf1-amd64-python-e1baa778f602ede66831-3.14.0a3%2B-e1baa77-vs-3.10.4.md)
- [📈time plot](bm-20250102-pythonperf1-amd64-python-e1baa778f602ede66831-3.14.0a3%2B-e1baa77-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.015x faster (HPT: reliability of 89.57%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250102-pythonperf1-amd64-python-e1baa778f602ede66831-3.14.0a3%2B-e1baa77-vs-3.12.0.md)
- [📈time plot](bm-20250102-pythonperf1-amd64-python-e1baa778f602ede66831-3.14.0a3%2B-e1baa77-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.013x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250102-pythonperf1-amd64-python-e1baa778f602ede66831-3.14.0a3%2B-e1baa77-vs-3.13.0.md)
- [📈time plot](bm-20250102-pythonperf1-amd64-python-e1baa778f602ede66831-3.14.0a3%2B-e1baa77-vs-3.13.0.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12585926978)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20250102-pythonperf1_win32-x86-python-e1baa778f602ede66831-3.14.0a3%2B-e1baa77.json)

### vs. 3.10.4

- Geometric mean: 1.157x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250102-pythonperf1_win32-x86-python-e1baa778f602ede66831-3.14.0a3%2B-e1baa77-vs-3.10.4.md)
- [📈time plot](bm-20250102-pythonperf1_win32-x86-python-e1baa778f602ede66831-3.14.0a3%2B-e1baa77-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.167x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250102-pythonperf1_win32-x86-python-e1baa778f602ede66831-3.14.0a3%2B-e1baa77-vs-3.12.0.md)
- [📈time plot](bm-20250102-pythonperf1_win32-x86-python-e1baa778f602ede66831-3.14.0a3%2B-e1baa77-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.041x faster (HPT: reliability of 59.93%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250102-pythonperf1_win32-x86-python-e1baa778f602ede66831-3.14.0a3%2B-e1baa77-vs-3.13.0.md)
- [📈time plot](bm-20250102-pythonperf1_win32-x86-python-e1baa778f602ede66831-3.14.0a3%2B-e1baa77-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12600005891)
- cpu model: missing
- platform: macOS-15.2-arm64-arm-64bit-Mach-O
- [raw results](bm-20250102-darwin-arm64-python-e1baa778f602ede66831-3.14.0a3%2B-e1baa77.json)

### vs. 3.10.4

- Geometric mean: 1.317x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, mypy2
- [📄table](bm-20250102-darwin-arm64-python-e1baa778f602ede66831-3.14.0a3%2B-e1baa77-vs-3.10.4.md)
- [📈time plot](bm-20250102-darwin-arm64-python-e1baa778f602ede66831-3.14.0a3%2B-e1baa77-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.109x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250102-darwin-arm64-python-e1baa778f602ede66831-3.14.0a3%2B-e1baa77-vs-3.12.0.md)
- [📈time plot](bm-20250102-darwin-arm64-python-e1baa778f602ede66831-3.14.0a3%2B-e1baa77-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.124x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
- new benchmarks: mypy2
- [📄table](bm-20250102-darwin-arm64-python-e1baa778f602ede66831-3.14.0a3%2B-e1baa77-vs-3.13.0.md)
- [📈time plot](bm-20250102-darwin-arm64-python-e1baa778f602ede66831-3.14.0a3%2B-e1baa77-vs-3.13.0.svg)

