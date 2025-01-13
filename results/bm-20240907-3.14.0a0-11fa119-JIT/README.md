# Results

- fork: python/11fa11987990eb7ed75b
- version: 3.14.0a0
- config: JIT
- commit hash: [11fa119](https://github.com/python/cpython/commit/11fa119)
- commit date: 2024-09-07T21:46:56+03:00
- commit merge base: [93050e46144c5864fbf2b39eac798387d5758a2d](https://github.com/python/cpython/commit/93050e46144c5864fbf2b39eac798387d5758a2d)
- ref: 11fa11987990eb7ed75b

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10755364735)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json)

### vs. 3.10.4

- Geometric mean: 1.181x faster (HPT: reliability of 99.99%, 1.04x faster at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence
- [📄table](bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-3.10.4.md)
- [📈time plot](bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.071x slower (HPT: reliability of 99.99%, 1.02x slower at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, unpack_sequence
- [📄table](bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-3.12.0.md)
- [📈time plot](bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.079x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-3.13.0.md)
- [📈time plot](bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.106x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: 1.09x
- [🧠memory plot](bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-base-mem.svg)
- [📄table](bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-base.md)
- [📈time plot](bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10755364735)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-193-generic-x86_64-with-glibc2.31
- [raw results](bm-20240907-linux-x86_64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json)

### vs. 3.10.4

- Geometric mean: 1.427x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240907-linux-x86_64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-3.10.4.md)
- [📈time plot](bm-20240907-linux-x86_64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.090x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240907-linux-x86_64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-3.12.0.md)
- [📈time plot](bm-20240907-linux-x86_64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.031x faster (HPT: reliability of 94.23%, 1.00x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240907-linux-x86_64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-3.13.0.md)
- [📈time plot](bm-20240907-linux-x86_64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x faster (HPT: reliability of 77.91%, 1.00x slower at 99th %ile)
- Memory usage: 1.08x
- [🧠memory plot](bm-20240907-linux-x86_64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-base-mem.svg)
- [📄table](bm-20240907-linux-x86_64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-base.md)
- [📈time plot](bm-20240907-linux-x86_64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10755364735)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240907-pythonperf2-x86_64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json)

### vs. 3.10.4

- Geometric mean: 1.312x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 1.23x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240907-pythonperf2-x86_64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-3.10.4.md)
- [📈time plot](bm-20240907-pythonperf2-x86_64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.017x faster (HPT: reliability of 64.67%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240907-pythonperf2-x86_64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-3.12.0.md)
- [📈time plot](bm-20240907-pythonperf2-x86_64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.020x faster (HPT: reliability of 90.43%, 1.00x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240907-pythonperf2-x86_64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-3.13.0.md)
- [📈time plot](bm-20240907-pythonperf2-x86_64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.019x slower (HPT: reliability of 95.88%, 1.00x slower at 99th %ile)
- Memory usage: 1.08x
- [🧠memory plot](bm-20240907-pythonperf2-x86_64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-base-mem.svg)
- [📄table](bm-20240907-pythonperf2-x86_64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-base.md)
- [📈time plot](bm-20240907-pythonperf2-x86_64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10755364735)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json)

### vs. 3.10.4

- Geometric mean: 1.239x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-3.10.4.md)
- [📈time plot](bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.050x faster (HPT: reliability of 93.96%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-3.12.0.md)
- [📈time plot](bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.029x faster (HPT: reliability of 98.90%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-3.13.0.md)
- [📈time plot](bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.050x faster (HPT: reliability of 90.68%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-base.md)
- [📈time plot](bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10755364735)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json)

### vs. 3.10.4

- Geometric mean: 1.229x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-3.10.4.md)
- [📈time plot](bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.239x faster (HPT: reliability of 100.00%, 1.15x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-3.12.0.md)
- [📈time plot](bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.112x faster (HPT: reliability of 95.83%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-3.13.0.md)
- [📈time plot](bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.085x faster (HPT: reliability of 99.60%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-base.md)
- [📈time plot](bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10755364735)
- cpu model: missing
- platform: macOS-14.6.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240907-darwin-arm64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json)

### vs. 3.10.4

- Geometric mean: 1.223x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: 0.72x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240907-darwin-arm64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-3.10.4.md)
- [📈time plot](bm-20240907-darwin-arm64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.033x faster (HPT: reliability of 90.15%, 1.00x faster at 99th %ile)
- Memory usage: 0.70x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240907-darwin-arm64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-3.12.0.md)
- [📈time plot](bm-20240907-darwin-arm64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.038x faster (HPT: reliability of 99.92%, 1.01x faster at 99th %ile)
- Memory usage: 0.48x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240907-darwin-arm64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-3.13.0.md)
- [📈time plot](bm-20240907-darwin-arm64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.047x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240907-darwin-arm64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-base-mem.svg)
- [📄table](bm-20240907-darwin-arm64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-base.md)
- [📈time plot](bm-20240907-darwin-arm64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119-vs-base.svg)

