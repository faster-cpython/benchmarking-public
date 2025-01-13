# Results

- fork: python/b3aa1b5fe260382788a2
- version: 3.14.0a0
- config: 
- commit hash: [b3aa1b5](https://github.com/python/cpython/commit/b3aa1b5)
- commit date: 2024-10-11T11:08:03+02:00
- commit merge base: [18c74497681e0107d7cde53e63ea42feb38f2176](https://github.com/python/cpython/commit/18c74497681e0107d7cde53e63ea42feb38f2176)
- ref: b3aa1b5fe260382788a2

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11318191947)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5.json)

### vs. 3.10.4

- Geometric mean: 1.327x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence
- [📄table](bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5-vs-3.10.4.md)
- [📈time plot](bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.038x faster (HPT: reliability of 91.66%, 1.00x faster at 99th %ile)
- Memory usage: 0.92x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, unpack_sequence
- [📄table](bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5-vs-3.12.0.md)
- [📈time plot](bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.028x faster (HPT: reliability of 99.62%, 1.00x faster at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5-vs-3.13.0.md)
- [📈time plot](bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5-vs-3.13.0.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11318191947)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241011-linux-x86_64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5.json)

### vs. 3.10.4

- Geometric mean: 1.423x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20241011-linux-x86_64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5-vs-3.10.4.md)
- [📈time plot](bm-20241011-linux-x86_64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.080x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241011-linux-x86_64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5-vs-3.12.0.md)
- [📈time plot](bm-20241011-linux-x86_64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.027x faster (HPT: reliability of 98.84%, 1.00x faster at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241011-linux-x86_64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5-vs-3.13.0.md)
- [📈time plot](bm-20241011-linux-x86_64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11318191947)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20241011-pythonperf2-x86_64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5.json)

### vs. 3.10.4

- Geometric mean: 1.337x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20241011-pythonperf2-x86_64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5-vs-3.10.4.md)
- [📈time plot](bm-20241011-pythonperf2-x86_64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.028x faster (HPT: reliability of 98.09%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241011-pythonperf2-x86_64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5-vs-3.12.0.md)
- [📈time plot](bm-20241011-pythonperf2-x86_64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.038x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241011-pythonperf2-x86_64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5-vs-3.13.0.md)
- [📈time plot](bm-20241011-pythonperf2-x86_64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11318191947)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5.json)

### vs. 3.10.4

- Geometric mean: 1.172x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5-vs-3.10.4.md)
- [📈time plot](bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.014x slower (HPT: reliability of 99.79%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5-vs-3.12.0.md)
- [📈time plot](bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.025x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5-vs-3.13.0.md)
- [📈time plot](bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5-vs-3.13.0.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11318191947)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5.json)

### vs. 3.10.4

- Geometric mean: 1.137x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5-vs-3.10.4.md)
- [📈time plot](bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.141x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5-vs-3.12.0.md)
- [📈time plot](bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.033x faster (HPT: reliability of 98.68%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5-vs-3.13.0.md)
- [📈time plot](bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11318191947)
- cpu model: missing
- platform: macOS-15.0.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241011-darwin-arm64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5.json)

### vs. 3.10.4

- Geometric mean: 1.303x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 0.52x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241011-darwin-arm64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5-vs-3.10.4.md)
- [📈time plot](bm-20241011-darwin-arm64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.086x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 0.43x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241011-darwin-arm64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5-vs-3.12.0.md)
- [📈time plot](bm-20241011-darwin-arm64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.093x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.38x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241011-darwin-arm64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5-vs-3.13.0.md)
- [📈time plot](bm-20241011-darwin-arm64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5-vs-3.13.0.svg)

