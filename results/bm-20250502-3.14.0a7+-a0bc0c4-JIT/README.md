# Results

- fork: python/a0bc0c462ff55b4112be
- version: 3.14.0a7+
- config: JIT
- commit hash: [a0bc0c4](https://github.com/python/cpython/commit/a0bc0c4)
- commit date: 2025-05-02T19:06:37+02:00
- commit merge base: [7e7e49be78e26d0a3b861a04bbec1635aabb71b9](https://github.com/python/cpython/commit/7e7e49be78e26d0a3b861a04bbec1635aabb71b9)
- ref: a0bc0c462ff55b4112be

## linux x86_64 (azure)

- [pystats raw](bm-20250502-azure-x86_64-python-a0bc0c462ff55b4112be-3.14.0a7%2B-a0bc0c4-pystats.json)
- [pystats table](bm-20250502-azure-x86_64-python-a0bc0c462ff55b4112be-3.14.0a7%2B-a0bc0c4-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14812950861)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250502-linux-x86_64-python-a0bc0c462ff55b4112be-3.14.0a7%2B-a0bc0c4.json)

### vs. 3.10.4

- Geometric mean: 1.447x faster (HPT: reliability of 100.00%, 1.32x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250502-linux-x86_64-python-a0bc0c462ff55b4112be-3.14.0a7%2B-a0bc0c4-vs-3.10.4.md)
- [📈time plot](bm-20250502-linux-x86_64-python-a0bc0c462ff55b4112be-3.14.0a7%2B-a0bc0c4-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.116x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250502-linux-x86_64-python-a0bc0c462ff55b4112be-3.14.0a7%2B-a0bc0c4-vs-3.12.0.md)
- [📈time plot](bm-20250502-linux-x86_64-python-a0bc0c462ff55b4112be-3.14.0a7%2B-a0bc0c4-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.044x faster (HPT: reliability of 96.33%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250502-linux-x86_64-python-a0bc0c462ff55b4112be-3.14.0a7%2B-a0bc0c4-vs-3.13.0.md)
- [📈time plot](bm-20250502-linux-x86_64-python-a0bc0c462ff55b4112be-3.14.0a7%2B-a0bc0c4-vs-3.13.0.svg)

