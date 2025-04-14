# Results

- fork: faster-cpython/close_escapes_2
- version: 3.14.0a4+
- config: 
- commit hash: [620dde2](https://github.com/faster%2dcpython/cpython/commit/620dde2)
- commit date: 2025-01-29T12:18:10+00:00
- commit merge base: [75b49621578a45415bfeedd6cc68d50e821d8281](https://github.com/python/cpython/commit/75b49621578a45415bfeedd6cc68d50e821d8281)
- ref: close_escapes_2

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13031170147)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250129-pythonperf2-x86_64-faster%252dcpython-close_escapes_2-3.14.0a4%2B-620dde2.json)

### vs. 3.10.4

- Geometric mean: 1.353x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250129-pythonperf2-x86_64-faster%252dcpython-close_escapes_2-3.14.0a4%2B-620dde2-vs-3.10.4.md)
- [📈time plot](bm-20250129-pythonperf2-x86_64-faster%252dcpython-close_escapes_2-3.14.0a4%2B-620dde2-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.047x faster (HPT: reliability of 99.97%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250129-pythonperf2-x86_64-faster%252dcpython-close_escapes_2-3.14.0a4%2B-620dde2-vs-3.12.0.md)
- [📈time plot](bm-20250129-pythonperf2-x86_64-faster%252dcpython-close_escapes_2-3.14.0a4%2B-620dde2-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.061x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250129-pythonperf2-x86_64-faster%252dcpython-close_escapes_2-3.14.0a4%2B-620dde2-vs-3.13.0.md)
- [📈time plot](bm-20250129-pythonperf2-x86_64-faster%252dcpython-close_escapes_2-3.14.0a4%2B-620dde2-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x faster (HPT: reliability of 86.73%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250129-pythonperf2-x86_64-faster%252dcpython-close_escapes_2-3.14.0a4%2B-620dde2-vs-base-mem.svg)
- [📄table](bm-20250129-pythonperf2-x86_64-faster%252dcpython-close_escapes_2-3.14.0a4%2B-620dde2-vs-base.md)
- [📈time plot](bm-20250129-pythonperf2-x86_64-faster%252dcpython-close_escapes_2-3.14.0a4%2B-620dde2-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13035120953)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20250129-pythonperf1-amd64-faster%252dcpython-close_escapes_2-3.14.0a4%2B-620dde2.json)

### vs. 3.10.4

- Geometric mean: 1.172x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250129-pythonperf1-amd64-faster%252dcpython-close_escapes_2-3.14.0a4%2B-620dde2-vs-3.10.4.md)
- [📈time plot](bm-20250129-pythonperf1-amd64-faster%252dcpython-close_escapes_2-3.14.0a4%2B-620dde2-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.006x slower (HPT: reliability of 98.54%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250129-pythonperf1-amd64-faster%252dcpython-close_escapes_2-3.14.0a4%2B-620dde2-vs-3.12.0.md)
- [📈time plot](bm-20250129-pythonperf1-amd64-faster%252dcpython-close_escapes_2-3.14.0a4%2B-620dde2-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.032x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250129-pythonperf1-amd64-faster%252dcpython-close_escapes_2-3.14.0a4%2B-620dde2-vs-3.13.0.md)
- [📈time plot](bm-20250129-pythonperf1-amd64-faster%252dcpython-close_escapes_2-3.14.0a4%2B-620dde2-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.012x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250129-pythonperf1-amd64-faster%252dcpython-close_escapes_2-3.14.0a4%2B-620dde2-vs-base.md)
- [📈time plot](bm-20250129-pythonperf1-amd64-faster%252dcpython-close_escapes_2-3.14.0a4%2B-620dde2-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13031160420)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20250129-pythonperf1_win32-x86-faster%252dcpython-close_escapes_2-3.14.0a4%2B-620dde2.json)

### vs. 3.10.4

- Geometric mean: 1.103x faster (HPT: reliability of 99.99%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250129-pythonperf1_win32-x86-faster%252dcpython-close_escapes_2-3.14.0a4%2B-620dde2-vs-3.10.4.md)
- [📈time plot](bm-20250129-pythonperf1_win32-x86-faster%252dcpython-close_escapes_2-3.14.0a4%2B-620dde2-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.109x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250129-pythonperf1_win32-x86-faster%252dcpython-close_escapes_2-3.14.0a4%2B-620dde2-vs-3.12.0.md)
- [📈time plot](bm-20250129-pythonperf1_win32-x86-faster%252dcpython-close_escapes_2-3.14.0a4%2B-620dde2-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.011x slower (HPT: reliability of 99.99%, 1.02x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250129-pythonperf1_win32-x86-faster%252dcpython-close_escapes_2-3.14.0a4%2B-620dde2-vs-3.13.0.md)
- [📈time plot](bm-20250129-pythonperf1_win32-x86-faster%252dcpython-close_escapes_2-3.14.0a4%2B-620dde2-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.023x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250129-pythonperf1_win32-x86-faster%252dcpython-close_escapes_2-3.14.0a4%2B-620dde2-vs-base.md)
- [📈time plot](bm-20250129-pythonperf1_win32-x86-faster%252dcpython-close_escapes_2-3.14.0a4%2B-620dde2-vs-base.svg)

