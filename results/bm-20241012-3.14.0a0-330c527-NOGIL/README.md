# Results

- fork: python
- version: 3.14.0a0
- config: NOGIL
- commit hash: [330c527](https://github.com/python/cpython/commit/330c527)
- commit date: 2024-10-12T13:57:27-07:00
- commit merge base: [fa52b82c91a8e1a0971bd5fef656473ec93f41e3](https://github.com/python/cpython/commit/fa52b82c91a8e1a0971bd5fef656473ec93f41e3)
- ref: 330c527299a5380f39c6

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11309716372)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241012-arminc-aarch64-python-330c527299a5380f39c6-3.14.0a0-330c527.json)

### vs. 3.10.4

- Geometric mean: 1.206x slower (HPT: reliability of 100.00%, 1.22x slower at 99th %ile)
- Memory usage: 1.36x
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, unpack_sequence
- [📄table](bm-20241012-arminc-aarch64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.10.4.md)
- [📈time plot](bm-20241012-arminc-aarch64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.381x slower (HPT: reliability of 100.00%, 1.50x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, unpack_sequence
- [📄table](bm-20241012-arminc-aarch64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.12.0.md)
- [📈time plot](bm-20241012-arminc-aarch64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.379x slower (HPT: reliability of 100.00%, 1.53x slower at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241012-arminc-aarch64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.13.0.md)
- [📈time plot](bm-20241012-arminc-aarch64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.391x slower (HPT: reliability of 100.00%, 1.57x slower at 99th %ile)
- Memory usage: 1.17x
- [🧠memory plot](bm-20241012-arminc-aarch64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-base-mem.svg)
- [📄table](bm-20241012-arminc-aarch64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-base.md)
- [📈time plot](bm-20241012-arminc-aarch64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11309716372)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241012-linux-x86_64-python-330c527299a5380f39c6-3.14.0a0-330c527.json)

### vs. 3.10.4

- Geometric mean: 1.070x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser
- [📄table](bm-20241012-linux-x86_64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.10.4.md)
- [📈time plot](bm-20241012-linux-x86_64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.299x slower (HPT: reliability of 100.00%, 1.35x slower at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241012-linux-x86_64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.12.0.md)
- [📈time plot](bm-20241012-linux-x86_64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.318x slower (HPT: reliability of 100.00%, 1.36x slower at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241012-linux-x86_64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.13.0.md)
- [📈time plot](bm-20241012-linux-x86_64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.335x slower (HPT: reliability of 100.00%, 1.38x slower at 99th %ile)
- Memory usage: 1.16x
- [🧠memory plot](bm-20241012-linux-x86_64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-base-mem.svg)
- [📄table](bm-20241012-linux-x86_64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-base.md)
- [📈time plot](bm-20241012-linux-x86_64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11309716372)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20241012-pythonperf2-x86_64-python-330c527299a5380f39c6-3.14.0a0-330c527.json)

### vs. 3.10.4

- Geometric mean: 1.118x slower (HPT: reliability of 100.00%, 1.08x slower at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser
- [📄table](bm-20241012-pythonperf2-x86_64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.10.4.md)
- [📈time plot](bm-20241012-pythonperf2-x86_64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.327x slower (HPT: reliability of 100.00%, 1.37x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241012-pythonperf2-x86_64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.12.0.md)
- [📈time plot](bm-20241012-pythonperf2-x86_64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.306x slower (HPT: reliability of 100.00%, 1.34x slower at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241012-pythonperf2-x86_64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.13.0.md)
- [📈time plot](bm-20241012-pythonperf2-x86_64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.325x slower (HPT: reliability of 100.00%, 1.37x slower at 99th %ile)
- Memory usage: 1.17x
- [🧠memory plot](bm-20241012-pythonperf2-x86_64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-base-mem.svg)
- [📄table](bm-20241012-pythonperf2-x86_64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-base.md)
- [📈time plot](bm-20241012-pythonperf2-x86_64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11309716372)
- cpu model: missing
- platform: macOS-15.0.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241012-darwin-arm64-python-330c527299a5380f39c6-3.14.0a0-330c527.json)

### vs. 3.10.4

- Geometric mean: 1.130x slower (HPT: reliability of 100.00%, 1.12x slower at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser
- [📄table](bm-20241012-darwin-arm64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.10.4.md)
- [📈time plot](bm-20241012-darwin-arm64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.271x slower (HPT: reliability of 100.00%, 1.32x slower at 99th %ile)
- Memory usage: 0.84x
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241012-darwin-arm64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.12.0.md)
- [📈time plot](bm-20241012-darwin-arm64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.246x slower (HPT: reliability of 100.00%, 1.25x slower at 99th %ile)
- Memory usage: 0.76x
- missing benchmarks: async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241012-darwin-arm64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.13.0.md)
- [📈time plot](bm-20241012-darwin-arm64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.320x slower (HPT: reliability of 100.00%, 1.35x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241012-darwin-arm64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-base-mem.svg)
- [📄table](bm-20241012-darwin-arm64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-base.md)
- [📈time plot](bm-20241012-darwin-arm64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-base.svg)

