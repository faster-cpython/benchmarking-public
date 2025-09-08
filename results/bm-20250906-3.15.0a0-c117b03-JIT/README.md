# Results

- fork: python/c117b033856ab7873972
- version: 3.15.0a0
- config: JIT
- commit hash: [c117b03](https://github.com/python/cpython/commit/c117b03)
- commit date: 2025-09-06T16:53:49-04:00
- commit merge base: [bbe00d53e9f598b012470cf077357cbbcbee737f](https://github.com/python/cpython/commit/bbe00d53e9f598b012470cf077357cbbcbee737f)
- ref: c117b033856ab7873972

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/17521143321)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20250906-pythonperf2-x86_64-python-c117b033856ab7873972-3.15.0a0-c117b03.json)

### vs. 3.10.4

- Geometric mean: 1.335x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.40x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250906-pythonperf2-x86_64-python-c117b033856ab7873972-3.15.0a0-c117b03-vs-3.10.4.md)
- [📈time plot](bm-20250906-pythonperf2-x86_64-python-c117b033856ab7873972-3.15.0a0-c117b03-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.038x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250906-pythonperf2-x86_64-python-c117b033856ab7873972-3.15.0a0-c117b03-vs-3.12.0.md)
- [📈time plot](bm-20250906-pythonperf2-x86_64-python-c117b033856ab7873972-3.15.0a0-c117b03-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.043x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250906-pythonperf2-x86_64-python-c117b033856ab7873972-3.15.0a0-c117b03-vs-3.13.0.md)
- [📈time plot](bm-20250906-pythonperf2-x86_64-python-c117b033856ab7873972-3.15.0a0-c117b03-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x slower (HPT: reliability of 77.62%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250906-pythonperf2-x86_64-python-c117b033856ab7873972-3.15.0a0-c117b03-vs-base-mem.svg)
- [📄table](bm-20250906-pythonperf2-x86_64-python-c117b033856ab7873972-3.15.0a0-c117b03-vs-base.md)
- [📈time plot](bm-20250906-pythonperf2-x86_64-python-c117b033856ab7873972-3.15.0a0-c117b03-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/17521143321)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250906-pythonperf1-amd64-python-c117b033856ab7873972-3.15.0a0-c117b03.json)

### vs. 3.10.4

- Geometric mean: 1.338x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250906-pythonperf1-amd64-python-c117b033856ab7873972-3.15.0a0-c117b03-vs-3.10.4.md)
- [📈time plot](bm-20250906-pythonperf1-amd64-python-c117b033856ab7873972-3.15.0a0-c117b03-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.141x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250906-pythonperf1-amd64-python-c117b033856ab7873972-3.15.0a0-c117b03-vs-3.12.0.md)
- [📈time plot](bm-20250906-pythonperf1-amd64-python-c117b033856ab7873972-3.15.0a0-c117b03-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.094x faster (HPT: reliability of 96.72%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250906-pythonperf1-amd64-python-c117b033856ab7873972-3.15.0a0-c117b03-vs-3.13.0.md)
- [📈time plot](bm-20250906-pythonperf1-amd64-python-c117b033856ab7873972-3.15.0a0-c117b03-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.041x faster (HPT: reliability of 99.99%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250906-pythonperf1-amd64-python-c117b033856ab7873972-3.15.0a0-c117b03-vs-base.md)
- [📈time plot](bm-20250906-pythonperf1-amd64-python-c117b033856ab7873972-3.15.0a0-c117b03-vs-base.svg)

## windows amd64 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/17521143321)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250906-pythonperf1_win32-amd64-python-c117b033856ab7873972-3.15.0a0-c117b03.json)

### vs. 3.10.4

- Geometric mean: 1.522x faster (HPT: reliability of 100.00%, 1.41x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250906-pythonperf1_win32-amd64-python-c117b033856ab7873972-3.15.0a0-c117b03-vs-3.10.4.md)
- [📈time plot](bm-20250906-pythonperf1_win32-amd64-python-c117b033856ab7873972-3.15.0a0-c117b03-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.543x faster (HPT: reliability of 100.00%, 1.49x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250906-pythonperf1_win32-amd64-python-c117b033856ab7873972-3.15.0a0-c117b03-vs-3.12.0.md)
- [📈time plot](bm-20250906-pythonperf1_win32-amd64-python-c117b033856ab7873972-3.15.0a0-c117b03-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.329x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250906-pythonperf1_win32-amd64-python-c117b033856ab7873972-3.15.0a0-c117b03-vs-3.13.0.md)
- [📈time plot](bm-20250906-pythonperf1_win32-amd64-python-c117b033856ab7873972-3.15.0a0-c117b03-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.037x faster (HPT: reliability of 99.96%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250906-pythonperf1_win32-amd64-python-c117b033856ab7873972-3.15.0a0-c117b03-vs-base.md)
- [📈time plot](bm-20250906-pythonperf1_win32-amd64-python-c117b033856ab7873972-3.15.0a0-c117b03-vs-base.svg)

