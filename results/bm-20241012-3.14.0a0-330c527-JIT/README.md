# Results

- fork: python/330c527299a5380f39c6
- version: 3.14.0a0
- config: JIT
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

- Geometric mean: 1.150x faster (HPT: reliability of 99.93%, 1.02x faster at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, unpack_sequence
- [📄table](bm-20241012-arminc-aarch64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.10.4.md)
- [📈time plot](bm-20241012-arminc-aarch64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.103x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, unpack_sequence
- [📄table](bm-20241012-arminc-aarch64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.12.0.md)
- [📈time plot](bm-20241012-arminc-aarch64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.093x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: 0.96x
- missing benchmarks: async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241012-arminc-aarch64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.13.0.md)
- [📈time plot](bm-20241012-arminc-aarch64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.117x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: 1.07x
- [🧠memory plot](bm-20241012-arminc-aarch64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-base-mem.svg)
- [📄table](bm-20241012-arminc-aarch64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-base.md)
- [📈time plot](bm-20241012-arminc-aarch64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11309716372)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241012-linux-x86_64-python-330c527299a5380f39c6-3.14.0a0-330c527.json)

### vs. 3.10.4

- Geometric mean: 1.385x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser
- [📄table](bm-20241012-linux-x86_64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.10.4.md)
- [📈time plot](bm-20241012-linux-x86_64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.050x faster (HPT: reliability of 97.99%, 1.00x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241012-linux-x86_64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.12.0.md)
- [📈time plot](bm-20241012-linux-x86_64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.020x faster (HPT: reliability of 54.94%, 1.00x faster at 99th %ile)
- Memory usage: 0.96x
- missing benchmarks: async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241012-linux-x86_64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.13.0.md)
- [📈time plot](bm-20241012-linux-x86_64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.009x slower (HPT: reliability of 69.15%, 1.00x slower at 99th %ile)
- Memory usage: 1.06x
- [🧠memory plot](bm-20241012-linux-x86_64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-base-mem.svg)
- [📄table](bm-20241012-linux-x86_64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-base.md)
- [📈time plot](bm-20241012-linux-x86_64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11309716372)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20241012-pythonperf2-x86_64-python-330c527299a5380f39c6-3.14.0a0-330c527.json)

### vs. 3.10.4

- Geometric mean: 1.277x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser
- [📄table](bm-20241012-pythonperf2-x86_64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.10.4.md)
- [📈time plot](bm-20241012-pythonperf2-x86_64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.021x slower (HPT: reliability of 92.72%, 1.00x slower at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241012-pythonperf2-x86_64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.12.0.md)
- [📈time plot](bm-20241012-pythonperf2-x86_64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.007x faster (HPT: reliability of 54.94%, 1.00x faster at 99th %ile)
- Memory usage: 0.96x
- missing benchmarks: async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241012-pythonperf2-x86_64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.13.0.md)
- [📈time plot](bm-20241012-pythonperf2-x86_64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.024x slower (HPT: reliability of 89.56%, 1.00x slower at 99th %ile)
- Memory usage: 1.06x
- [🧠memory plot](bm-20241012-pythonperf2-x86_64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-base-mem.svg)
- [📄table](bm-20241012-pythonperf2-x86_64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-base.md)
- [📈time plot](bm-20241012-pythonperf2-x86_64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11309716372)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241012-pythonperf1_win32-x86-python-330c527299a5380f39c6-3.14.0a0-330c527.json)

### vs. 3.10.4

- Geometric mean: 1.179x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20241012-pythonperf1_win32-x86-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.10.4.md)
- [📈time plot](bm-20241012-pythonperf1_win32-x86-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.205x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241012-pythonperf1_win32-x86-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.12.0.md)
- [📈time plot](bm-20241012-pythonperf1_win32-x86-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.096x faster (HPT: reliability of 76.07%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, chameleon, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241012-pythonperf1_win32-x86-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.13.0.md)
- [📈time plot](bm-20241012-pythonperf1_win32-x86-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.070x faster (HPT: reliability of 99.82%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241012-pythonperf1_win32-x86-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-base.md)
- [📈time plot](bm-20241012-pythonperf1_win32-x86-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11309716372)
- cpu model: missing
- platform: macOS-15.0.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241012-darwin-arm64-python-330c527299a5380f39c6-3.14.0a0-330c527.json)

### vs. 3.10.4

- Geometric mean: 1.211x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: 0.81x
- missing benchmarks: async_tree_cpu_io_mixed, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_io, async_tree_eager_memoization, async_tree_io, async_tree_memoization, async_tree_none, chameleon, connected_components, dask, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241012-darwin-arm64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.10.4.md)
- [📈time plot](bm-20241012-darwin-arm64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.024x faster (HPT: reliability of 82.92%, 1.00x faster at 99th %ile)
- Memory usage: 0.73x
- missing benchmarks: aiohttp, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241012-darwin-arm64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.12.0.md)
- [📈time plot](bm-20241012-darwin-arm64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.058x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 0.65x
- missing benchmarks: async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241012-darwin-arm64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.13.0.md)
- [📈time plot](bm-20241012-darwin-arm64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.049x slower (HPT: reliability of 99.99%, 1.01x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241012-darwin-arm64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-base-mem.svg)
- [📄table](bm-20241012-darwin-arm64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-base.md)
- [📈time plot](bm-20241012-darwin-arm64-python-330c527299a5380f39c6-3.14.0a0-330c527-vs-base.svg)

