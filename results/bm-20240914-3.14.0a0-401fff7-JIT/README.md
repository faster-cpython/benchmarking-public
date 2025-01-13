# Results

- fork: python/401fff7423ca3c8bf1d0
- version: 3.14.0a0
- config: JIT
- commit hash: [401fff7](https://github.com/python/cpython/commit/401fff7)
- commit date: 2024-09-14T14:29:55-04:00
- commit merge base: [9dacf430c2f4af2acd870291a649b7b957efcd2c](https://github.com/python/cpython/commit/9dacf430c2f4af2acd870291a649b7b957efcd2c)
- ref: 401fff7423ca3c8bf1d0

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10866440409)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json)

### vs. 3.10.4

- Geometric mean: 1.177x faster (HPT: reliability of 99.98%, 1.04x faster at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence
- [📄table](bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.10.4.md)
- [📈time plot](bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.074x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, unpack_sequence
- [📄table](bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.12.0.md)
- [📈time plot](bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.081x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.13.0.md)
- [📈time plot](bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.110x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.09x
- [🧠memory plot](bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-base-mem.svg)
- [📄table](bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-base.md)
- [📈time plot](bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-base.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20240914-azure-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-pystats.json)
- [pystats table](bm-20240914-azure-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-pystats.md)

### vs. base

- [pystats diff](bm-20240914-azure-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10866440409)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-193-generic-x86_64-with-glibc2.31
- [raw results](bm-20240914-linux-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json)

### vs. 3.10.4

- Geometric mean: 1.428x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240914-linux-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.10.4.md)
- [📈time plot](bm-20240914-linux-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.092x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240914-linux-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.12.0.md)
- [📈time plot](bm-20240914-linux-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.033x faster (HPT: reliability of 96.69%, 1.00x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240914-linux-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.13.0.md)
- [📈time plot](bm-20240914-linux-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.003x slower (HPT: reliability of 54.97%, 1.00x slower at 99th %ile)
- Memory usage: 1.08x
- [🧠memory plot](bm-20240914-linux-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-base-mem.svg)
- [📄table](bm-20240914-linux-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-base.md)
- [📈time plot](bm-20240914-linux-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10866440409)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json)

### vs. 3.10.4

- Geometric mean: 1.321x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.10.4.md)
- [📈time plot](bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.023x faster (HPT: reliability of 82.72%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.12.0.md)
- [📈time plot](bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.026x faster (HPT: reliability of 95.41%, 1.00x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.13.0.md)
- [📈time plot](bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.010x slower (HPT: reliability of 67.33%, 1.00x slower at 99th %ile)
- Memory usage: 1.08x
- [🧠memory plot](bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-base-mem.svg)
- [📄table](bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-base.md)
- [📈time plot](bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10866440409)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json)

### vs. 3.10.4

- Geometric mean: 1.242x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.10.4.md)
- [📈time plot](bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.053x faster (HPT: reliability of 95.46%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.12.0.md)
- [📈time plot](bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.031x faster (HPT: reliability of 97.23%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.13.0.md)
- [📈time plot](bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.057x faster (HPT: reliability of 91.27%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-base.md)
- [📈time plot](bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10866440409)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json)

### vs. 3.10.4

- Geometric mean: 1.230x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.10.4.md)
- [📈time plot](bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.241x faster (HPT: reliability of 100.00%, 1.15x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.12.0.md)
- [📈time plot](bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.112x faster (HPT: reliability of 94.89%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.13.0.md)
- [📈time plot](bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.085x faster (HPT: reliability of 96.70%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-base.md)
- [📈time plot](bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10866440409)
- cpu model: missing
- platform: macOS-14.6.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json)

### vs. 3.10.4

- Geometric mean: 1.226x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: 0.52x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.10.4.md)
- [📈time plot](bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.036x faster (HPT: reliability of 93.81%, 1.00x faster at 99th %ile)
- Memory usage: 0.49x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.12.0.md)
- [📈time plot](bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.041x faster (HPT: reliability of 99.84%, 1.00x faster at 99th %ile)
- Memory usage: 0.41x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.13.0.md)
- [📈time plot](bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.049x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-base-mem.svg)
- [📄table](bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-base.md)
- [📈time plot](bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7-vs-base.svg)

