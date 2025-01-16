# Results

- fork: mdboom/tail_call_no_preserv
- version: 3.14.0a4+
- config: CLANG
- commit hash: [09f3d0f](https://github.com/mdboom/cpython/commit/09f3d0f)
- commit date: 2025-01-16T14:42:06-05:00
- commit merge base: [313b96eb8b8d0ad3bac58d633822a0a3705ce60b](https://github.com/python/cpython/commit/313b96eb8b8d0ad3bac58d633822a0a3705ce60b)
- ref: tail_call_no_preserv

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12816391983)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35
- [raw results](bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4%2B-09f3d0f.json)

### vs. 3.10.4

- Geometric mean: 1.350x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4%2B-09f3d0f-vs-3.10.4.md)
- [📈time plot](bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4%2B-09f3d0f-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.046x faster (HPT: reliability of 95.61%, 1.00x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4%2B-09f3d0f-vs-3.12.0.md)
- [📈time plot](bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4%2B-09f3d0f-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.059x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4%2B-09f3d0f-vs-3.13.0.md)
- [📈time plot](bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4%2B-09f3d0f-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.029x faster (HPT: reliability of 99.75%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4%2B-09f3d0f-vs-base-mem.svg)
- [📄table](bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4%2B-09f3d0f-vs-base.md)
- [📈time plot](bm-20250116-pythonperf2-x86_64-mdboom-tail_call_no_preserv-3.14.0a4%2B-09f3d0f-vs-base.svg)

