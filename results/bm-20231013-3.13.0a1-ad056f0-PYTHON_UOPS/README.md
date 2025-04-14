# Results

- fork: python/ad056f03aee8000a1564
- version: 3.13.0a1
- config: T2
- commit hash: [ad056f0](https://github.com/python/cpython/commit/ad056f0)
- commit date: 2023-10-13T10:52:10+02:00
- commit merge base: [b7f9661bc12fdfec98684c89f03177ae5d3d74c1](https://github.com/python/cpython/commit/b7f9661bc12fdfec98684c89f03177ae5d3d74c1)
- ref: ad056f03aee8000a1564

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/7583592155)
- cpu model: missing
- platform: Windows-11-10.0.22621-SP0
- [raw results](bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0.json)

### vs. 3.10.4

- Geometric mean: 1.164x slower (HPT: reliability of 100.00%, 1.11x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, django_template, dulwich_log, flaskblogging, genshi_text, genshi_xml, html5lib, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0-vs-3.10.4.md)
- [📈time plot](bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.161x slower (HPT: reliability of 100.00%, 1.10x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, django_template, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0-vs-3.12.0.md)
- [📈time plot](bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.266x slower (HPT: reliability of 100.00%, 1.29x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, django_template, djangocms, dulwich_log, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers, thrift
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0-vs-3.13.0.md)
- [📈time plot](bm-20231013-pythonperf1_win32-x86-python-ad056f03aee8000a1564-3.13.0a1-ad056f0-vs-3.13.0.svg)

