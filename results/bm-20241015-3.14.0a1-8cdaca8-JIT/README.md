# Results

- fork: python/v3.14.0a1
- version: 3.14.0a1
- config: JIT
- commit hash: [8cdaca8](https://github.com/python/cpython/commit/8cdaca8)
- commit date: 2024-10-15T22:34:54+03:00
- commit merge base: [3ea488aac44887a7cdb30be69580c81a0ca6afe2](https://github.com/python/cpython/commit/3ea488aac44887a7cdb30be69580c81a0ca6afe2)
- ref: v3.14.0a1

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11404965313)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8.json)

### vs. 3.10.4

- Geometric mean: 1.165x faster (HPT: reliability of 99.97%, 1.03x faster at 99th %ile)
- Memory usage: 1.37x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx, unpack_sequence
- [📄table](bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.10.4.md)
- [📈time plot](bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.085x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, sphinx, unpack_sequence
- [📄table](bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.12.0.md)
- [📈time plot](bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.094x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.13.0.md)
- [📈time plot](bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.111x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: 1.06x
- [🧠memory plot](bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-base-mem.svg)
- [📄table](bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-base.md)
- [📈time plot](bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11404965313)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json)

### vs. 3.10.4

- Geometric mean: 1.393x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.10.4.md)
- [📈time plot](bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.063x faster (HPT: reliability of 99.88%, 1.01x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.12.0.md)
- [📈time plot](bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.006x faster (HPT: reliability of 62.80%, 1.00x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.13.0.md)
- [📈time plot](bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.013x slower (HPT: reliability of 83.10%, 1.00x slower at 99th %ile)
- Memory usage: 1.06x
- [🧠memory plot](bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-base-mem.svg)
- [📄table](bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-base.md)
- [📈time plot](bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11404965313)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json)

### vs. 3.10.4

- Geometric mean: 1.286x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.10.4.md)
- [📈time plot](bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.006x slower (HPT: reliability of 61.16%, 1.00x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.12.0.md)
- [📈time plot](bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.002x slower (HPT: reliability of 55.32%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.13.0.md)
- [📈time plot](bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.028x slower (HPT: reliability of 99.87%, 1.00x slower at 99th %ile)
- Memory usage: 1.06x
- [🧠memory plot](bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-base-mem.svg)
- [📄table](bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-base.md)
- [📈time plot](bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11404965313)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8.json)

### vs. 3.10.4

- Geometric mean: 1.169x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx
- [📄table](bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.10.4.md)
- [📈time plot](bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.178x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.12.0.md)
- [📈time plot](bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.056x faster (HPT: reliability of 53.80%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.13.0.md)
- [📈time plot](bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.041x faster (HPT: reliability of 83.45%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-base.md)
- [📈time plot](bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11404965313)
- cpu model: missing
- platform: macOS-15.0.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8.json)

### vs. 3.10.4

- Geometric mean: 1.230x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: 1.43x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.10.4.md)
- [📈time plot](bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.034x faster (HPT: reliability of 99.09%, 1.00x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.12.0.md)
- [📈time plot](bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.037x faster (HPT: reliability of 99.76%, 1.00x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.13.0.md)
- [📈time plot](bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.042x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 1.09x
- [🧠memory plot](bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-base-mem.svg)
- [📄table](bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-base.md)
- [📈time plot](bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8-vs-base.svg)

