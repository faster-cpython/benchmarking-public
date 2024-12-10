# Results

- fork: brandtbucher/jump_backoff
- version: 3.14.0a1+
- config: JIT
- commit hash: [2e7a174](https://github.com/brandtbucher/cpython/commit/2e7a174)
- commit date: 2024-11-13T17:25:49-08:00
- commit merge base: [c695e37a3f95c225ee08d1e882d23fa200b5ec34](https://github.com/python/cpython/commit/c695e37a3f95c225ee08d1e882d23fa200b5ec34)
- ref: jump_backoff

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11828918805)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20241113-pythonperf2-x86_64-brandtbucher-jump_backoff-3.14.0a1%2B-2e7a174.json)

### vs. 3.10.4

- Geometric mean: 1.274x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241113-pythonperf2-x86_64-brandtbucher-jump_backoff-3.14.0a1%2B-2e7a174-vs-3.10.4.md)
- [📈time plot](bm-20241113-pythonperf2-x86_64-brandtbucher-jump_backoff-3.14.0a1%2B-2e7a174-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.016x slower (HPT: reliability of 93.99%, 1.00x slower at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241113-pythonperf2-x86_64-brandtbucher-jump_backoff-3.14.0a1%2B-2e7a174-vs-3.12.0.md)
- [📈time plot](bm-20241113-pythonperf2-x86_64-brandtbucher-jump_backoff-3.14.0a1%2B-2e7a174-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.011x slower (HPT: reliability of 73.10%, 1.00x slower at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, many_optionals, subparsers, tornado_http
- [📄table](bm-20241113-pythonperf2-x86_64-brandtbucher-jump_backoff-3.14.0a1%2B-2e7a174-vs-3.13.0.md)
- [📈time plot](bm-20241113-pythonperf2-x86_64-brandtbucher-jump_backoff-3.14.0a1%2B-2e7a174-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.010x faster (HPT: reliability of 90.28%, 1.00x faster at 99th %ile)
- Memory usage: 0.96x
- [🧠memory plot](bm-20241113-pythonperf2-x86_64-brandtbucher-jump_backoff-3.14.0a1%2B-2e7a174-vs-base-mem.svg)
- [📄table](bm-20241113-pythonperf2-x86_64-brandtbucher-jump_backoff-3.14.0a1%2B-2e7a174-vs-base.md)
- [📈time plot](bm-20241113-pythonperf2-x86_64-brandtbucher-jump_backoff-3.14.0a1%2B-2e7a174-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11828918805)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241113-pythonperf1_win32-x86-brandtbucher-jump_backoff-3.14.0a1%2B-2e7a174.json)

### vs. 3.10.4

- Geometric mean: 1.046x faster (HPT: reliability of 54.26%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241113-pythonperf1_win32-x86-brandtbucher-jump_backoff-3.14.0a1%2B-2e7a174-vs-3.10.4.md)
- [📈time plot](bm-20241113-pythonperf1_win32-x86-brandtbucher-jump_backoff-3.14.0a1%2B-2e7a174-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.054x faster (HPT: reliability of 99.56%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241113-pythonperf1_win32-x86-brandtbucher-jump_backoff-3.14.0a1%2B-2e7a174-vs-3.12.0.md)
- [📈time plot](bm-20241113-pythonperf1_win32-x86-brandtbucher-jump_backoff-3.14.0a1%2B-2e7a174-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.055x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, many_optionals, sqlalchemy_declarative, sqlalchemy_imperative, subparsers, tornado_http
- [📄table](bm-20241113-pythonperf1_win32-x86-brandtbucher-jump_backoff-3.14.0a1%2B-2e7a174-vs-3.13.0.md)
- [📈time plot](bm-20241113-pythonperf1_win32-x86-brandtbucher-jump_backoff-3.14.0a1%2B-2e7a174-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.010x faster (HPT: reliability of 94.07%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241113-pythonperf1_win32-x86-brandtbucher-jump_backoff-3.14.0a1%2B-2e7a174-vs-base.md)
- [📈time plot](bm-20241113-pythonperf1_win32-x86-brandtbucher-jump_backoff-3.14.0a1%2B-2e7a174-vs-base.svg)

