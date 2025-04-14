# Results

- fork: faster-cpython/close_escapes_2
- version: 3.14.0a4+
- config: 
- commit hash: [fa5c6fd](https://github.com/faster%2dcpython/cpython/commit/fa5c6fd)
- commit date: 2025-01-28T14:29:57+00:00
- commit merge base: [75b49621578a45415bfeedd6cc68d50e821d8281](https://github.com/python/cpython/commit/75b49621578a45415bfeedd6cc68d50e821d8281)
- ref: close_escapes_2

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13012838767)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250128-linux-x86_64-faster%252dcpython-close_escapes_2-3.14.0a4%2B-fa5c6fd.json)

### vs. 3.10.4

- Geometric mean: 1.453x faster (HPT: reliability of 100.00%, 1.32x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250128-linux-x86_64-faster%252dcpython-close_escapes_2-3.14.0a4%2B-fa5c6fd-vs-3.10.4.md)
- [📈time plot](bm-20250128-linux-x86_64-faster%252dcpython-close_escapes_2-3.14.0a4%2B-fa5c6fd-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.116x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250128-linux-x86_64-faster%252dcpython-close_escapes_2-3.14.0a4%2B-fa5c6fd-vs-3.12.0.md)
- [📈time plot](bm-20250128-linux-x86_64-faster%252dcpython-close_escapes_2-3.14.0a4%2B-fa5c6fd-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.048x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250128-linux-x86_64-faster%252dcpython-close_escapes_2-3.14.0a4%2B-fa5c6fd-vs-3.13.0.md)
- [📈time plot](bm-20250128-linux-x86_64-faster%252dcpython-close_escapes_2-3.14.0a4%2B-fa5c6fd-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x faster (HPT: reliability of 79.66%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250128-linux-x86_64-faster%252dcpython-close_escapes_2-3.14.0a4%2B-fa5c6fd-vs-base-mem.svg)
- [📄table](bm-20250128-linux-x86_64-faster%252dcpython-close_escapes_2-3.14.0a4%2B-fa5c6fd-vs-base.md)
- [📈time plot](bm-20250128-linux-x86_64-faster%252dcpython-close_escapes_2-3.14.0a4%2B-fa5c6fd-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13014320952)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20250128-pythonperf1-amd64-faster%252dcpython-close_escapes_2-3.14.0a4%2B-fa5c6fd.json)

### vs. 3.10.4

- Geometric mean: 1.179x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250128-pythonperf1-amd64-faster%252dcpython-close_escapes_2-3.14.0a4%2B-fa5c6fd-vs-3.10.4.md)
- [📈time plot](bm-20250128-pythonperf1-amd64-faster%252dcpython-close_escapes_2-3.14.0a4%2B-fa5c6fd-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.002x slower (HPT: reliability of 97.85%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250128-pythonperf1-amd64-faster%252dcpython-close_escapes_2-3.14.0a4%2B-fa5c6fd-vs-3.12.0.md)
- [📈time plot](bm-20250128-pythonperf1-amd64-faster%252dcpython-close_escapes_2-3.14.0a4%2B-fa5c6fd-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.027x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
- [📄table](bm-20250128-pythonperf1-amd64-faster%252dcpython-close_escapes_2-3.14.0a4%2B-fa5c6fd-vs-3.13.0.md)
- [📈time plot](bm-20250128-pythonperf1-amd64-faster%252dcpython-close_escapes_2-3.14.0a4%2B-fa5c6fd-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.007x slower (HPT: reliability of 99.94%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250128-pythonperf1-amd64-faster%252dcpython-close_escapes_2-3.14.0a4%2B-fa5c6fd-vs-base.md)
- [📈time plot](bm-20250128-pythonperf1-amd64-faster%252dcpython-close_escapes_2-3.14.0a4%2B-fa5c6fd-vs-base.svg)

