# Results

- fork: python/47b01da4ccedd9c00fad
- version: 3.15.0a0
- config: 
- commit hash: [47b01da](https://github.com/python/cpython/commit/47b01da)
- commit date: 2025-07-12T21:15:04+03:00
- commit merge base: [9be3649f5eccfbda1b3c9c3195927951a9ae9b90](https://github.com/python/cpython/commit/9be3649f5eccfbda1b3c9c3195927951a9ae9b90)
- ref: 47b01da4ccedd9c00fad

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16243275875)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json)

### vs. 3.10.4

- Geometric mean: 1.305x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.38x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da-vs-3.10.4.md)
- [📈time plot](bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.030x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence
- [📄table](bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da-vs-3.12.0.md)
- [📈time plot](bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.033x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da-vs-3.13.0.md)
- [📈time plot](bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da-vs-3.13.0.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20250712-azure-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da-pystats.json)
- [pystats table](bm-20250712-azure-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da-pystats.md)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16243275875)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-141-generic-x86_64-with-glibc2.35
- [raw results](bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json)

### vs. 3.10.4

- Geometric mean: 1.319x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.38x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da-vs-3.10.4.md)
- [📈time plot](bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.024x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da-vs-3.12.0.md)
- [📈time plot](bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.039x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da-vs-3.13.0.md)
- [📈time plot](bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16243275875)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json)

### vs. 3.10.4

- Geometric mean: 1.291x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da-vs-3.10.4.md)
- [📈time plot](bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.101x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da-vs-3.12.0.md)
- [📈time plot](bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.069x faster (HPT: reliability of 85.98%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da-vs-3.13.0.md)
- [📈time plot](bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da-vs-3.13.0.svg)

## windows amd64 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16243275875)
- cpu model: missing
- platform: Windows-11-10.0.26100-SP0
- [raw results](bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json)

### vs. 3.10.4

- Geometric mean: 1.455x faster (HPT: reliability of 100.00%, 1.35x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers
- [📄table](bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da-vs-3.10.4.md)
- [📈time plot](bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.472x faster (HPT: reliability of 100.00%, 1.42x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift
- [📄table](bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da-vs-3.12.0.md)
- [📈time plot](bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.284x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da-vs-3.13.0.md)
- [📈time plot](bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/16243275875)
- cpu model: missing
- platform: macOS-15.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json)

### vs. 3.10.4

- Geometric mean: 1.249x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da-vs-3.10.4.md)
- [📈time plot](bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.012x slower (HPT: reliability of 96.59%, 1.00x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da-vs-3.12.0.md)
- [📈time plot](bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.010x slower (HPT: reliability of 63.44%, 1.00x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da-vs-3.13.0.md)
- [📈time plot](bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da-vs-3.13.0.svg)

