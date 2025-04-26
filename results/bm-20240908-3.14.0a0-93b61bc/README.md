# Results

- fork: python/93b61bc1245fb318a11d
- version: 3.14.0a0
- config: 
- commit hash: [93b61bc](https://github.com/python/cpython/commit/93b61bc)
- commit date: 2024-09-08T22:39:23-04:00
- commit merge base: [aa3f11f80a644dac7184e8546ddfcc9b68be364c](https://github.com/python/cpython/commit/aa3f11f80a644dac7184e8546ddfcc9b68be364c)
- ref: 93b61bc1245fb318a11d

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/14673981835)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20240908-linux-x86_64-python-93b61bc1245fb318a11d-3.14.0a0-93b61bc.json)

### vs. 3.10.4

- Geometric mean: 1.402x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20240908-linux-x86_64-python-93b61bc1245fb318a11d-3.14.0a0-93b61bc-vs-3.10.4.md)
- [📈time plot](bm-20240908-linux-x86_64-python-93b61bc1245fb318a11d-3.14.0a0-93b61bc-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.070x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20240908-linux-x86_64-python-93b61bc1245fb318a11d-3.14.0a0-93b61bc-vs-3.12.0.md)
- [📈time plot](bm-20240908-linux-x86_64-python-93b61bc1245fb318a11d-3.14.0a0-93b61bc-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.012x faster (HPT: reliability of 95.77%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, dask, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20240908-linux-x86_64-python-93b61bc1245fb318a11d-3.14.0a0-93b61bc-vs-3.13.0.md)
- [📈time plot](bm-20240908-linux-x86_64-python-93b61bc1245fb318a11d-3.14.0a0-93b61bc-vs-3.13.0.svg)

