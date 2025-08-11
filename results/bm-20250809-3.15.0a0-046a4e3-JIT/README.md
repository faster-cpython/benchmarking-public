# Results

- fork: python/046a4e39b3f8ac5cb13e
- version: 3.15.0a0
- config: JIT
- commit hash: [046a4e3](https://github.com/python/cpython/commit/046a4e3)
- commit date: 2025-08-09T18:25:49+00:00
- commit merge base: [af15e1d13ea26575afbb94b814e541586547a706](https://github.com/python/cpython/commit/af15e1d13ea26575afbb94b814e541586547a706)
- ref: 046a4e39b3f8ac5cb13e

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16855058191)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json)

### vs. 3.10.4

- Geometric mean: 1.295x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.41x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.10.4.md)
- [📈time plot](bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.025x faster (HPT: reliability of 99.86%, 1.01x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.12.0.md)
- [📈time plot](bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.016x faster (HPT: reliability of 99.24%, 1.00x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.13.0.md)
- [📈time plot](bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.014x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-base-mem.svg)
- [📄table](bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-base.md)
- [📈time plot](bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16855058191)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json)

### vs. 3.10.4

- Geometric mean: 1.335x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.40x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.10.4.md)
- [📈time plot](bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.036x faster (HPT: reliability of 99.99%, 1.03x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.12.0.md)
- [📈time plot](bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.043x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.13.0.md)
- [📈time plot](bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.005x faster (HPT: reliability of 82.40%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-base-mem.svg)
- [📄table](bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-base.md)
- [📈time plot](bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16855058191)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json)

### vs. 3.10.4

- Geometric mean: 1.315x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.10.4.md)
- [📈time plot](bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.122x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.12.0.md)
- [📈time plot](bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.079x faster (HPT: reliability of 91.94%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.13.0.md)
- [📈time plot](bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.010x faster (HPT: reliability of 97.13%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-base.md)
- [📈time plot](bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-base.svg)

## windows amd64 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16855058191)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json)

### vs. 3.10.4

- Geometric mean: 1.477x faster (HPT: reliability of 100.00%, 1.38x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.10.4.md)
- [📈time plot](bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.497x faster (HPT: reliability of 100.00%, 1.44x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.12.0.md)
- [📈time plot](bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.292x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.13.0.md)
- [📈time plot](bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.028x faster (HPT: reliability of 92.63%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-base.md)
- [📈time plot](bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16855058191)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json)

### vs. 3.10.4

- Geometric mean: 1.342x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.10.4.md)
- [📈time plot](bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.060x faster (HPT: reliability of 99.78%, 1.00x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.12.0.md)
- [📈time plot](bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.062x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.13.0.md)
- [📈time plot](bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.013x faster (HPT: reliability of 65.75%, 1.00x slower at 99th %ile)
- Memory usage: 1.03x
- [🧠memory plot](bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-base-mem.svg)
- [📄table](bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-base.md)
- [📈time plot](bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3-vs-base.svg)

