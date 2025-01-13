# Results

- fork: python/d8c864816121547338ef
- version: 3.14.0a1+
- config: JIT
- commit hash: [d8c8648](https://github.com/python/cpython/commit/d8c8648)
- commit date: 2024-10-17T20:10:55+02:00
- commit merge base: [b454662921fd3a1fc27169e91aca03aadea08817](https://github.com/python/cpython/commit/b454662921fd3a1fc27169e91aca03aadea08817)
- ref: d8c864816121547338ef

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11407873273)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648.json)

### vs. 3.10.4

- Geometric mean: 1.164x faster (HPT: reliability of 99.98%, 1.03x faster at 99th %ile)
- Memory usage: 1.37x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx, unpack_sequence
- [📄table](bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.10.4.md)
- [📈time plot](bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.086x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, sphinx, unpack_sequence
- [📄table](bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.12.0.md)
- [📈time plot](bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.093x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.13.0.md)
- [📈time plot](bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.13.0.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20241017-azure-x86_64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-pystats.json)
- [pystats table](bm-20241017-azure-x86_64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11407873273)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648.json)

### vs. 3.10.4

- Geometric mean: 1.394x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.10.4.md)
- [📈time plot](bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.064x faster (HPT: reliability of 99.94%, 1.01x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.12.0.md)
- [📈time plot](bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.006x faster (HPT: reliability of 67.65%, 1.00x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.13.0.md)
- [📈time plot](bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11407873273)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648.json)

### vs. 3.10.4

- Geometric mean: 1.281x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.10.4.md)
- [📈time plot](bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.010x slower (HPT: reliability of 74.84%, 1.00x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.12.0.md)
- [📈time plot](bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.007x slower (HPT: reliability of 69.21%, 1.00x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.13.0.md)
- [📈time plot](bm-20241017-pythonperf2-x86_64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11407873273)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241017-pythonperf1-amd64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648.json)

### vs. 3.10.4

- Geometric mean: 1.197x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx
- [📄table](bm-20241017-pythonperf1-amd64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.10.4.md)
- [📈time plot](bm-20241017-pythonperf1-amd64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.012x faster (HPT: reliability of 72.91%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241017-pythonperf1-amd64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.12.0.md)
- [📈time plot](bm-20241017-pythonperf1-amd64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.009x slower (HPT: reliability of 99.60%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241017-pythonperf1-amd64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.13.0.md)
- [📈time plot](bm-20241017-pythonperf1-amd64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.13.0.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11407873273)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648.json)

### vs. 3.10.4

- Geometric mean: 1.185x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx
- [📄table](bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.10.4.md)
- [📈time plot](bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.193x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.12.0.md)
- [📈time plot](bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.070x faster (HPT: reliability of 75.21%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.13.0.md)
- [📈time plot](bm-20241017-pythonperf1_win32-x86-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11407873273)
- cpu model: missing
- platform: macOS-15.0.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241017-darwin-arm64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648.json)

### vs. 3.10.4

- Geometric mean: 1.228x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: 1.43x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241017-darwin-arm64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.10.4.md)
- [📈time plot](bm-20241017-darwin-arm64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.033x faster (HPT: reliability of 97.50%, 1.00x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241017-darwin-arm64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.12.0.md)
- [📈time plot](bm-20241017-darwin-arm64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.035x faster (HPT: reliability of 99.36%, 1.00x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241017-darwin-arm64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.13.0.md)
- [📈time plot](bm-20241017-darwin-arm64-python-d8c864816121547338ef-3.14.0a1%2B-d8c8648-vs-3.13.0.svg)

