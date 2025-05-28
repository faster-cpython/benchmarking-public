# Results

- fork: faster-cpython/specialize_for_iter_
- version: 3.15.0a0
- config: 
- commit hash: [a684067](https://github.com/faster%2dcpython/cpython/commit/a684067)
- commit date: 2025-05-28T09:26:26+01:00
- commit merge base: [f6f4e8a6622d556641799b02aed7ac018d878cdc](https://github.com/python/cpython/commit/f6f4e8a6622d556641799b02aed7ac018d878cdc)
- ref: specialize_for_iter_

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15295821692)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250528-arminc-aarch64-faster%252dcpython-specialize_for_iter_-3.15.0a0-a684067.json)

### vs. 3.10.4

- Geometric mean: 1.223x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.35x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250528-arminc-aarch64-faster%252dcpython-specialize_for_iter_-3.15.0a0-a684067-vs-3.10.4.md)
- [📈time plot](bm-20250528-arminc-aarch64-faster%252dcpython-specialize_for_iter_-3.15.0a0-a684067-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.031x slower (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250528-arminc-aarch64-faster%252dcpython-specialize_for_iter_-3.15.0a0-a684067-vs-3.12.0.md)
- [📈time plot](bm-20250528-arminc-aarch64-faster%252dcpython-specialize_for_iter_-3.15.0a0-a684067-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.025x slower (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250528-arminc-aarch64-faster%252dcpython-specialize_for_iter_-3.15.0a0-a684067-vs-3.13.0.md)
- [📈time plot](bm-20250528-arminc-aarch64-faster%252dcpython-specialize_for_iter_-3.15.0a0-a684067-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x slower (HPT: reliability of 68.47%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250528-arminc-aarch64-faster%252dcpython-specialize_for_iter_-3.15.0a0-a684067-vs-base-mem.svg)
- [📄table](bm-20250528-arminc-aarch64-faster%252dcpython-specialize_for_iter_-3.15.0a0-a684067-vs-base.md)
- [📈time plot](bm-20250528-arminc-aarch64-faster%252dcpython-specialize_for_iter_-3.15.0a0-a684067-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15295821692)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250528-linux-x86_64-faster%252dcpython-specialize_for_iter_-3.15.0a0-a684067.json)

### vs. 3.10.4

- Geometric mean: 1.306x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250528-linux-x86_64-faster%252dcpython-specialize_for_iter_-3.15.0a0-a684067-vs-3.10.4.md)
- [📈time plot](bm-20250528-linux-x86_64-faster%252dcpython-specialize_for_iter_-3.15.0a0-a684067-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.079x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250528-linux-x86_64-faster%252dcpython-specialize_for_iter_-3.15.0a0-a684067-vs-3.12.0.md)
- [📈time plot](bm-20250528-linux-x86_64-faster%252dcpython-specialize_for_iter_-3.15.0a0-a684067-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.035x slower (HPT: reliability of 99.90%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, dask, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250528-linux-x86_64-faster%252dcpython-specialize_for_iter_-3.15.0a0-a684067-vs-3.13.0.md)
- [📈time plot](bm-20250528-linux-x86_64-faster%252dcpython-specialize_for_iter_-3.15.0a0-a684067-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x faster (HPT: reliability of 98.56%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250528-linux-x86_64-faster%252dcpython-specialize_for_iter_-3.15.0a0-a684067-vs-base-mem.svg)
- [📄table](bm-20250528-linux-x86_64-faster%252dcpython-specialize_for_iter_-3.15.0a0-a684067-vs-base.md)
- [📈time plot](bm-20250528-linux-x86_64-faster%252dcpython-specialize_for_iter_-3.15.0a0-a684067-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15295821692)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250528-pythonperf1-amd64-faster%252dcpython-specialize_for_iter_-3.15.0a0-a684067.json)

### vs. 3.10.4

- Geometric mean: 1.159x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250528-pythonperf1-amd64-faster%252dcpython-specialize_for_iter_-3.15.0a0-a684067-vs-3.10.4.md)
- [📈time plot](bm-20250528-pythonperf1-amd64-faster%252dcpython-specialize_for_iter_-3.15.0a0-a684067-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.059x faster (HPT: reliability of 99.92%, 1.01x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250528-pythonperf1-amd64-faster%252dcpython-specialize_for_iter_-3.15.0a0-a684067-vs-3.12.0.md)
- [📈time plot](bm-20250528-pythonperf1-amd64-faster%252dcpython-specialize_for_iter_-3.15.0a0-a684067-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.027x slower (HPT: reliability of 99.32%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250528-pythonperf1-amd64-faster%252dcpython-specialize_for_iter_-3.15.0a0-a684067-vs-3.13.0.md)
- [📈time plot](bm-20250528-pythonperf1-amd64-faster%252dcpython-specialize_for_iter_-3.15.0a0-a684067-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x faster (HPT: reliability of 69.18%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250528-pythonperf1-amd64-faster%252dcpython-specialize_for_iter_-3.15.0a0-a684067-vs-base.md)
- [📈time plot](bm-20250528-pythonperf1-amd64-faster%252dcpython-specialize_for_iter_-3.15.0a0-a684067-vs-base.svg)

