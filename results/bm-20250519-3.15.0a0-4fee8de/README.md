# Results

- fork: faster-cpython/make_decref_a_call
- version: 3.15.0a0
- config: 
- commit hash: [4fee8de](https://github.com/faster%2dcpython/cpython/commit/4fee8de)
- commit date: 2025-05-19T10:36:51-04:00
- commit merge base: [605022aeb69ae19cae1c020a6993ab5c433ce907](https://github.com/python/cpython/commit/605022aeb69ae19cae1c020a6993ab5c433ce907)
- ref: make_decref_a_call

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15115913369)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250519-arminc-aarch64-faster%252dcpython-make_decref_a_call-3.15.0a0-4fee8de.json)

### vs. 3.10.4

- Geometric mean: 1.302x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250519-arminc-aarch64-faster%252dcpython-make_decref_a_call-3.15.0a0-4fee8de-vs-3.10.4.md)
- [📈time plot](bm-20250519-arminc-aarch64-faster%252dcpython-make_decref_a_call-3.15.0a0-4fee8de-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.029x faster (HPT: reliability of 82.97%, 1.00x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250519-arminc-aarch64-faster%252dcpython-make_decref_a_call-3.15.0a0-4fee8de-vs-3.12.0.md)
- [📈time plot](bm-20250519-arminc-aarch64-faster%252dcpython-make_decref_a_call-3.15.0a0-4fee8de-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.027x faster (HPT: reliability of 94.98%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250519-arminc-aarch64-faster%252dcpython-make_decref_a_call-3.15.0a0-4fee8de-vs-3.13.0.md)
- [📈time plot](bm-20250519-arminc-aarch64-faster%252dcpython-make_decref_a_call-3.15.0a0-4fee8de-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.060x faster (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 0.99x
- new benchmarks: djangocms
- [🧠memory plot](bm-20250519-arminc-aarch64-faster%252dcpython-make_decref_a_call-3.15.0a0-4fee8de-vs-base-mem.svg)
- [📄table](bm-20250519-arminc-aarch64-faster%252dcpython-make_decref_a_call-3.15.0a0-4fee8de-vs-base.md)
- [📈time plot](bm-20250519-arminc-aarch64-faster%252dcpython-make_decref_a_call-3.15.0a0-4fee8de-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15115913369)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-208-generic-x86_64-with-glibc2.31
- [raw results](bm-20250519-linux-x86_64-faster%252dcpython-make_decref_a_call-3.15.0a0-4fee8de.json)

### vs. 3.10.4

- Geometric mean: 1.384x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.30x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250519-linux-x86_64-faster%252dcpython-make_decref_a_call-3.15.0a0-4fee8de-vs-3.10.4.md)
- [📈time plot](bm-20250519-linux-x86_64-faster%252dcpython-make_decref_a_call-3.15.0a0-4fee8de-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.066x faster (HPT: reliability of 99.92%, 1.00x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250519-linux-x86_64-faster%252dcpython-make_decref_a_call-3.15.0a0-4fee8de-vs-3.12.0.md)
- [📈time plot](bm-20250519-linux-x86_64-faster%252dcpython-make_decref_a_call-3.15.0a0-4fee8de-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.008x faster (HPT: reliability of 85.31%, 1.00x slower at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, dask, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250519-linux-x86_64-faster%252dcpython-make_decref_a_call-3.15.0a0-4fee8de-vs-3.13.0.md)
- [📈time plot](bm-20250519-linux-x86_64-faster%252dcpython-make_decref_a_call-3.15.0a0-4fee8de-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.040x faster (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 0.99x
- new benchmarks: djangocms
- [🧠memory plot](bm-20250519-linux-x86_64-faster%252dcpython-make_decref_a_call-3.15.0a0-4fee8de-vs-base-mem.svg)
- [📄table](bm-20250519-linux-x86_64-faster%252dcpython-make_decref_a_call-3.15.0a0-4fee8de-vs-base.md)
- [📈time plot](bm-20250519-linux-x86_64-faster%252dcpython-make_decref_a_call-3.15.0a0-4fee8de-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15115913369)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250519-pythonperf1-amd64-faster%252dcpython-make_decref_a_call-3.15.0a0-4fee8de.json)

### vs. 3.10.4

- Geometric mean: 1.248x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250519-pythonperf1-amd64-faster%252dcpython-make_decref_a_call-3.15.0a0-4fee8de-vs-3.10.4.md)
- [📈time plot](bm-20250519-pythonperf1-amd64-faster%252dcpython-make_decref_a_call-3.15.0a0-4fee8de-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.064x faster (HPT: reliability of 90.88%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250519-pythonperf1-amd64-faster%252dcpython-make_decref_a_call-3.15.0a0-4fee8de-vs-3.12.0.md)
- [📈time plot](bm-20250519-pythonperf1-amd64-faster%252dcpython-make_decref_a_call-3.15.0a0-4fee8de-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.033x faster (HPT: reliability of 99.62%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250519-pythonperf1-amd64-faster%252dcpython-make_decref_a_call-3.15.0a0-4fee8de-vs-3.13.0.md)
- [📈time plot](bm-20250519-pythonperf1-amd64-faster%252dcpython-make_decref_a_call-3.15.0a0-4fee8de-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.046x faster (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250519-pythonperf1-amd64-faster%252dcpython-make_decref_a_call-3.15.0a0-4fee8de-vs-base.md)
- [📈time plot](bm-20250519-pythonperf1-amd64-faster%252dcpython-make_decref_a_call-3.15.0a0-4fee8de-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/15115913369)
- cpu model: missing
- platform: macOS-15.4.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20250519-darwin-arm64-faster%252dcpython-make_decref_a_call-3.15.0a0-4fee8de.json)

### vs. 3.10.4

- Geometric mean: 1.209x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.16x
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250519-darwin-arm64-faster%252dcpython-make_decref_a_call-3.15.0a0-4fee8de-vs-3.10.4.md)
- [📈time plot](bm-20250519-darwin-arm64-faster%252dcpython-make_decref_a_call-3.15.0a0-4fee8de-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.045x slower (HPT: reliability of 99.93%, 1.01x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250519-darwin-arm64-faster%252dcpython-make_decref_a_call-3.15.0a0-4fee8de-vs-3.12.0.md)
- [📈time plot](bm-20250519-darwin-arm64-faster%252dcpython-make_decref_a_call-3.15.0a0-4fee8de-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.044x slower (HPT: reliability of 99.42%, 1.00x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile
- [📄table](bm-20250519-darwin-arm64-faster%252dcpython-make_decref_a_call-3.15.0a0-4fee8de-vs-3.13.0.md)
- [📈time plot](bm-20250519-darwin-arm64-faster%252dcpython-make_decref_a_call-3.15.0a0-4fee8de-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.065x faster (HPT: reliability of 96.98%, 1.00x slower at 99th %ile)
- Memory usage: 0.99x
- [🧠memory plot](bm-20250519-darwin-arm64-faster%252dcpython-make_decref_a_call-3.15.0a0-4fee8de-vs-base-mem.svg)
- [📄table](bm-20250519-darwin-arm64-faster%252dcpython-make_decref_a_call-3.15.0a0-4fee8de-vs-base.md)
- [📈time plot](bm-20250519-darwin-arm64-faster%252dcpython-make_decref_a_call-3.15.0a0-4fee8de-vs-base.svg)

