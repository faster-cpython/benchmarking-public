# Results

- fork: brandtbucher/jit_cached_consts_un
- version: 3.14.0a7+
- config: JIT
- commit hash: [7e6d8a4](https://github.com/brandtbucher/cpython/commit/7e6d8a4)
- commit date: 2025-04-24T16:19:34-07:00
- commit merge base: [09b624b80f54e1f97812981cfff9fa374bd5360f](https://github.com/python/cpython/commit/09b624b80f54e1f97812981cfff9fa374bd5360f)
- ref: jit_cached_consts_un

## linux x86_64 (azure)

- [pystats raw](bm-20250424-azure-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7%2B-7e6d8a4-pystats.json)
- [pystats table](bm-20250424-azure-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7%2B-7e6d8a4-pystats.md)

### vs. base

- [pystats diff](bm-20250424-azure-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7%2B-7e6d8a4-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14653880445)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7%2B-7e6d8a4.json)

### vs. 3.10.4

- Geometric mean: 1.459x faster (HPT: reliability of 100.00%, 1.33x faster at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7%2B-7e6d8a4-vs-3.10.4.md)
- [📈time plot](bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7%2B-7e6d8a4-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.125x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7%2B-7e6d8a4-vs-3.12.0.md)
- [📈time plot](bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7%2B-7e6d8a4-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.053x faster (HPT: reliability of 99.84%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7%2B-7e6d8a4-vs-3.13.0.md)
- [📈time plot](bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7%2B-7e6d8a4-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x slower (HPT: reliability of 99.87%, 1.00x slower at 99th %ile)
- Memory usage: 0.99x
- [🧠memory plot](bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7%2B-7e6d8a4-vs-base-mem.svg)
- [📄table](bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7%2B-7e6d8a4-vs-base.md)
- [📈time plot](bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7%2B-7e6d8a4-vs-base.svg)

