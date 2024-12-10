# Results

- fork: python/760872efecb95017db8e
- version: 3.14.0a1+
- config: JIT
- commit hash: [760872e](https://github.com/python/cpython/commit/760872e)
- commit date: 2024-10-16T11:39:17-04:00
- commit merge base: [d83fcf8371f2f33c7797bc8f5423a8bca8c46e5c](https://github.com/python/cpython/commit/d83fcf8371f2f33c7797bc8f5423a8bca8c46e5c)
- ref: 760872efecb95017db8e

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11373872551)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1%2B-760872e.json)

### vs. 3.10.4

- Geometric mean: 1.170x faster (HPT: reliability of 99.99%, 1.04x faster at 99th %ile)
- Memory usage: 1.37x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx, unpack_sequence
- [📄table](bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1%2B-760872e-vs-3.10.4.md)
- [📈time plot](bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1%2B-760872e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.081x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, sphinx, unpack_sequence
- [📄table](bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1%2B-760872e-vs-3.12.0.md)
- [📈time plot](bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1%2B-760872e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.091x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1%2B-760872e-vs-3.13.0.md)
- [📈time plot](bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1%2B-760872e-vs-3.13.0.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20241016-azure-x86_64-python-760872efecb95017db8e-3.14.0a1%2B-760872e-pystats.json)
- [pystats table](bm-20241016-azure-x86_64-python-760872efecb95017db8e-3.14.0a1%2B-760872e-pystats.md)

### vs. base

- [pystats diff](bm-20241016-azure-x86_64-python-760872efecb95017db8e-3.14.0a1%2B-760872e-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11373872551)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241016-linux-x86_64-python-760872efecb95017db8e-3.14.0a1%2B-760872e.json)

### vs. 3.10.4

- Geometric mean: 1.393x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241016-linux-x86_64-python-760872efecb95017db8e-3.14.0a1%2B-760872e-vs-3.10.4.md)
- [📈time plot](bm-20241016-linux-x86_64-python-760872efecb95017db8e-3.14.0a1%2B-760872e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.064x faster (HPT: reliability of 99.95%, 1.01x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241016-linux-x86_64-python-760872efecb95017db8e-3.14.0a1%2B-760872e-vs-3.12.0.md)
- [📈time plot](bm-20241016-linux-x86_64-python-760872efecb95017db8e-3.14.0a1%2B-760872e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.006x faster (HPT: reliability of 59.10%, 1.00x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241016-linux-x86_64-python-760872efecb95017db8e-3.14.0a1%2B-760872e-vs-3.13.0.md)
- [📈time plot](bm-20241016-linux-x86_64-python-760872efecb95017db8e-3.14.0a1%2B-760872e-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.016x slower (HPT: reliability of 61.29%, 1.00x slower at 99th %ile)
- Memory usage: 1.06x
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [🧠memory plot](bm-20241016-linux-x86_64-python-760872efecb95017db8e-3.14.0a1%2B-760872e-vs-base-mem.svg)
- [📄table](bm-20241016-linux-x86_64-python-760872efecb95017db8e-3.14.0a1%2B-760872e-vs-base.md)
- [📈time plot](bm-20241016-linux-x86_64-python-760872efecb95017db8e-3.14.0a1%2B-760872e-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11373872551)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1%2B-760872e.json)

### vs. 3.10.4

- Geometric mean: 1.285x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1%2B-760872e-vs-3.10.4.md)
- [📈time plot](bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1%2B-760872e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.007x slower (HPT: reliability of 70.12%, 1.00x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1%2B-760872e-vs-3.12.0.md)
- [📈time plot](bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1%2B-760872e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.003x slower (HPT: reliability of 64.77%, 1.00x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1%2B-760872e-vs-3.13.0.md)
- [📈time plot](bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1%2B-760872e-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11373872551)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1%2B-760872e.json)

### vs. 3.10.4

- Geometric mean: 1.199x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx
- [📄table](bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1%2B-760872e-vs-3.10.4.md)
- [📈time plot](bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1%2B-760872e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.014x faster (HPT: reliability of 76.42%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1%2B-760872e-vs-3.12.0.md)
- [📈time plot](bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1%2B-760872e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.008x slower (HPT: reliability of 99.86%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1%2B-760872e-vs-3.13.0.md)
- [📈time plot](bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1%2B-760872e-vs-3.13.0.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11373872551)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1%2B-760872e.json)

### vs. 3.10.4

- Geometric mean: 1.180x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx
- [📄table](bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1%2B-760872e-vs-3.10.4.md)
- [📈time plot](bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1%2B-760872e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.188x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1%2B-760872e-vs-3.12.0.md)
- [📈time plot](bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1%2B-760872e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.066x faster (HPT: reliability of 64.85%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1%2B-760872e-vs-3.13.0.md)
- [📈time plot](bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1%2B-760872e-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11373872551)
- cpu model: missing
- platform: macOS-15.0.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1%2B-760872e.json)

### vs. 3.10.4

- Geometric mean: 1.231x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: 1.43x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1%2B-760872e-vs-3.10.4.md)
- [📈time plot](bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1%2B-760872e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.039x faster (HPT: reliability of 99.39%, 1.00x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1%2B-760872e-vs-3.12.0.md)
- [📈time plot](bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1%2B-760872e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.041x faster (HPT: reliability of 99.93%, 1.00x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1%2B-760872e-vs-3.13.0.md)
- [📈time plot](bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1%2B-760872e-vs-3.13.0.svg)

