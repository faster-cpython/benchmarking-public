# Results

- fork: python/117a8acdab997b73ada8
- version: 3.14.0a0
- config: 
- commit hash: [117a8ac](https://github.com/python/cpython/commit/117a8ac)
- commit date: 2024-06-02T17:43:03-07:00
- commit merge base: [bd6d4ed6454378e48dab06f50a9be0bae6baa3a2](https://github.com/python/cpython/commit/bd6d4ed6454378e48dab06f50a9be0bae6baa3a2)
- ref: 117a8acdab997b73ada8

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14715514575)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20240602-linux-x86_64-python-117a8acdab997b73ada8-3.14.0a0-117a8ac.json)

### vs. 3.10.4

- Geometric mean: 1.385x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20240602-linux-x86_64-python-117a8acdab997b73ada8-3.14.0a0-117a8ac-vs-3.10.4.md)
- [📈time plot](bm-20240602-linux-x86_64-python-117a8acdab997b73ada8-3.14.0a0-117a8ac-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.052x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20240602-linux-x86_64-python-117a8acdab997b73ada8-3.14.0a0-117a8ac-vs-3.12.0.md)
- [📈time plot](bm-20240602-linux-x86_64-python-117a8acdab997b73ada8-3.14.0a0-117a8ac-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.012x slower (HPT: reliability of 93.82%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: chameleon, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20240602-linux-x86_64-python-117a8acdab997b73ada8-3.14.0a0-117a8ac-vs-3.13.0.md)
- [📈time plot](bm-20240602-linux-x86_64-python-117a8acdab997b73ada8-3.14.0a0-117a8ac-vs-3.13.0.svg)

