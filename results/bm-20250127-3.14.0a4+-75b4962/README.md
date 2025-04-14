# Results

- fork: python/75b49621578a45415bfe
- version: 3.14.0a4+
- config: 
- commit hash: [75b4962](https://github.com/python/cpython/commit/75b4962)
- commit date: 2025-01-27T16:24:48+00:00
- commit merge base: [8ec76d90340287eb3587f0ae388bbfe158fb28d8](https://github.com/python/cpython/commit/8ec76d90340287eb3587f0ae388bbfe158fb28d8)
- ref: 75b49621578a45415bfe

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13012838767)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250127-linux-x86_64-python-75b49621578a45415bfe-3.14.0a4%2B-75b4962.json)

### vs. 3.10.4

- Geometric mean: 1.453x faster (HPT: reliability of 100.00%, 1.32x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250127-linux-x86_64-python-75b49621578a45415bfe-3.14.0a4%2B-75b4962-vs-3.10.4.md)
- [📈time plot](bm-20250127-linux-x86_64-python-75b49621578a45415bfe-3.14.0a4%2B-75b4962-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.116x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250127-linux-x86_64-python-75b49621578a45415bfe-3.14.0a4%2B-75b4962-vs-3.12.0.md)
- [📈time plot](bm-20250127-linux-x86_64-python-75b49621578a45415bfe-3.14.0a4%2B-75b4962-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.048x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250127-linux-x86_64-python-75b49621578a45415bfe-3.14.0a4%2B-75b4962-vs-3.13.0.md)
- [📈time plot](bm-20250127-linux-x86_64-python-75b49621578a45415bfe-3.14.0a4%2B-75b4962-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13031170147)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250127-pythonperf2-x86_64-python-75b49621578a45415bfe-3.14.0a4%2B-75b4962.json)

### vs. 3.10.4

- Geometric mean: 1.352x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250127-pythonperf2-x86_64-python-75b49621578a45415bfe-3.14.0a4%2B-75b4962-vs-3.10.4.md)
- [📈time plot](bm-20250127-pythonperf2-x86_64-python-75b49621578a45415bfe-3.14.0a4%2B-75b4962-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.047x faster (HPT: reliability of 99.96%, 1.01x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250127-pythonperf2-x86_64-python-75b49621578a45415bfe-3.14.0a4%2B-75b4962-vs-3.12.0.md)
- [📈time plot](bm-20250127-pythonperf2-x86_64-python-75b49621578a45415bfe-3.14.0a4%2B-75b4962-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.059x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250127-pythonperf2-x86_64-python-75b49621578a45415bfe-3.14.0a4%2B-75b4962-vs-3.13.0.md)
- [📈time plot](bm-20250127-pythonperf2-x86_64-python-75b49621578a45415bfe-3.14.0a4%2B-75b4962-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13014320952)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20250127-pythonperf1-amd64-python-75b49621578a45415bfe-3.14.0a4%2B-75b4962.json)

### vs. 3.10.4

- Geometric mean: 1.189x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250127-pythonperf1-amd64-python-75b49621578a45415bfe-3.14.0a4%2B-75b4962-vs-3.10.4.md)
- [📈time plot](bm-20250127-pythonperf1-amd64-python-75b49621578a45415bfe-3.14.0a4%2B-75b4962-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.007x faster (HPT: reliability of 95.08%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250127-pythonperf1-amd64-python-75b49621578a45415bfe-3.14.0a4%2B-75b4962-vs-3.12.0.md)
- [📈time plot](bm-20250127-pythonperf1-amd64-python-75b49621578a45415bfe-3.14.0a4%2B-75b4962-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.021x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250127-pythonperf1-amd64-python-75b49621578a45415bfe-3.14.0a4%2B-75b4962-vs-3.13.0.md)
- [📈time plot](bm-20250127-pythonperf1-amd64-python-75b49621578a45415bfe-3.14.0a4%2B-75b4962-vs-3.13.0.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13031160420)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20250127-pythonperf1_win32-x86-python-75b49621578a45415bfe-3.14.0a4%2B-75b4962.json)

### vs. 3.10.4

- Geometric mean: 1.130x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250127-pythonperf1_win32-x86-python-75b49621578a45415bfe-3.14.0a4%2B-75b4962-vs-3.10.4.md)
- [📈time plot](bm-20250127-pythonperf1_win32-x86-python-75b49621578a45415bfe-3.14.0a4%2B-75b4962-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.138x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250127-pythonperf1_win32-x86-python-75b49621578a45415bfe-3.14.0a4%2B-75b4962-vs-3.12.0.md)
- [📈time plot](bm-20250127-pythonperf1_win32-x86-python-75b49621578a45415bfe-3.14.0a4%2B-75b4962-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.012x faster (HPT: reliability of 99.11%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250127-pythonperf1_win32-x86-python-75b49621578a45415bfe-3.14.0a4%2B-75b4962-vs-3.13.0.md)
- [📈time plot](bm-20250127-pythonperf1_win32-x86-python-75b49621578a45415bfe-3.14.0a4%2B-75b4962-vs-3.13.0.svg)

