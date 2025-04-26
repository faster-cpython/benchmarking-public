# Results

- fork: python/081706f873b7d1a10b27
- version: 3.14.0a1+
- config: 
- commit hash: [081706f](https://github.com/python/cpython/commit/081706f)
- commit date: 2024-11-03T23:08:15-05:00
- commit merge base: [9441993f272f42e4a97d90616ec629a11c06aa3a](https://github.com/python/cpython/commit/9441993f272f42e4a97d90616ec629a11c06aa3a)
- ref: 081706f873b7d1a10b27

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14673983385)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20241103-linux-x86_64-python-081706f873b7d1a10b27-3.14.0a1%2B-081706f.json)

### vs. 3.10.4

- Geometric mean: 1.375x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20241103-linux-x86_64-python-081706f873b7d1a10b27-3.14.0a1%2B-081706f-vs-3.10.4.md)
- [📈time plot](bm-20241103-linux-x86_64-python-081706f873b7d1a10b27-3.14.0a1%2B-081706f-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.047x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20241103-linux-x86_64-python-081706f873b7d1a10b27-3.14.0a1%2B-081706f-vs-3.12.0.md)
- [📈time plot](bm-20241103-linux-x86_64-python-081706f873b7d1a10b27-3.14.0a1%2B-081706f-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.011x slower (HPT: reliability of 97.14%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, dask, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20241103-linux-x86_64-python-081706f873b7d1a10b27-3.14.0a1%2B-081706f-vs-3.13.0.md)
- [📈time plot](bm-20241103-linux-x86_64-python-081706f873b7d1a10b27-3.14.0a1%2B-081706f-vs-3.13.0.svg)

