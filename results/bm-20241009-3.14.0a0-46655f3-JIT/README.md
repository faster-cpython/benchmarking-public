# Results

- fork: mdboom/disable_interpreter_
- version: 3.14.0a0
- config: JIT
- commit hash: [46655f3](https://github.com/mdboom/cpython/commit/46655f3)
- commit date: 2024-10-09T17:24:15-04:00
- commit merge base: [cbfd39247983309a9ef0ae6da6c61cc71665b967](https://github.com/python/cpython/commit/cbfd39247983309a9ef0ae6da6c61cc71665b967)
- ref: disable_interpreter_

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11274221715)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3.json)

### vs. 3.10.4

- Geometric mean: 1.224x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3-vs-3.10.4.md)
- [📈time plot](bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.235x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3-vs-3.12.0.md)
- [📈time plot](bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.109x faster (HPT: reliability of 90.10%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3-vs-3.13.0.md)
- [📈time plot](bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3-vs-3.13.0.svg)

