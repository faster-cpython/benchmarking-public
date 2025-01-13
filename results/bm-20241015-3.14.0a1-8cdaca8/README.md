# Results

- fork: python/v3.14.0a1
- version: 3.14.0a1
- config: 
- commit hash: [8cdaca8](https://github.com/python/cpython/commit/8cdaca8)
- commit date: 2024-10-15T22:34:54+03:00
- commit merge base: [3ea488aac44887a7cdb30be69580c81a0ca6afe2](https://github.com/python/cpython/commit/3ea488aac44887a7cdb30be69580c81a0ca6afe2)
- ref: v3.14.0a1

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11404961853)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8.json)

### vs. 3.10.4

- Geometric mean: 1.319x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.29x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx, unpack_sequence
- [📄table](bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.10.4.md)
- [📈time plot](bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.029x faster (HPT: reliability of 99.86%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, sphinx, unpack_sequence
- [📄table](bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.12.0.md)
- [📈time plot](bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.020x faster (HPT: reliability of 99.96%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.13.0.md)
- [📈time plot](bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.13.0.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11404961853)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json)

### vs. 3.10.4

- Geometric mean: 1.414x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.10.4.md)
- [📈time plot](bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.073x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.12.0.md)
- [📈time plot](bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.020x faster (HPT: reliability of 93.82%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.13.0.md)
- [📈time plot](bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11404961853)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json)

### vs. 3.10.4

- Geometric mean: 1.325x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.10.4.md)
- [📈time plot](bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.018x faster (HPT: reliability of 96.36%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.12.0.md)
- [📈time plot](bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.027x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.13.0.md)
- [📈time plot](bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11404961853)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8.json)

### vs. 3.10.4

- Geometric mean: 1.153x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx
- [📄table](bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.10.4.md)
- [📈time plot](bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.032x slower (HPT: reliability of 99.93%, 1.02x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.12.0.md)
- [📈time plot](bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.042x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.13.0.md)
- [📈time plot](bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.13.0.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11404961853)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8.json)

### vs. 3.10.4

- Geometric mean: 1.119x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx
- [📄table](bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.10.4.md)
- [📈time plot](bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.118x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.12.0.md)
- [📈time plot](bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.015x faster (HPT: reliability of 99.95%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.13.0.md)
- [📈time plot](bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11404961853)
- cpu model: missing
- platform: macOS-15.0.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8.json)

### vs. 3.10.4

- Geometric mean: 1.285x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 1.32x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.10.4.md)
- [📈time plot](bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.075x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.12.0.md)
- [📈time plot](bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.083x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.13.0.md)
- [📈time plot](bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.13.0.svg)

