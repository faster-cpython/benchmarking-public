# Results

- fork: python/42b0b0667e67ff444a03
- version: 3.14.0a7+
- config: 
- commit hash: [42b0b06](https://github.com/python/cpython/commit/42b0b06)
- commit date: 2025-04-30T05:35:36+08:00
- commit merge base: [c46635aa5a20fc1b4c5e85370fa0fa2303c47c14](https://github.com/python/cpython/commit/c46635aa5a20fc1b4c5e85370fa0fa2303c47c14)
- ref: 42b0b0667e67ff444a03

## linux x86_64 (azure)

- [pystats raw](bm-20250430-azure-x86_64-python-42b0b0667e67ff444a03-3.14.0a7%2B-42b0b06-pystats.json)
- [pystats table](bm-20250430-azure-x86_64-python-42b0b0667e67ff444a03-3.14.0a7%2B-42b0b06-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14742419446)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250430-linux-x86_64-python-42b0b0667e67ff444a03-3.14.0a7%2B-42b0b06.json)

### vs. 3.10.4

- Geometric mean: 1.457x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250430-linux-x86_64-python-42b0b0667e67ff444a03-3.14.0a7%2B-42b0b06-vs-3.10.4.md)
- [📈time plot](bm-20250430-linux-x86_64-python-42b0b0667e67ff444a03-3.14.0a7%2B-42b0b06-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.124x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250430-linux-x86_64-python-42b0b0667e67ff444a03-3.14.0a7%2B-42b0b06-vs-3.12.0.md)
- [📈time plot](bm-20250430-linux-x86_64-python-42b0b0667e67ff444a03-3.14.0a7%2B-42b0b06-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.053x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250430-linux-x86_64-python-42b0b0667e67ff444a03-3.14.0a7%2B-42b0b06-vs-3.13.0.md)
- [📈time plot](bm-20250430-linux-x86_64-python-42b0b0667e67ff444a03-3.14.0a7%2B-42b0b06-vs-3.13.0.svg)

