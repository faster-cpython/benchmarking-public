# Results

- fork: python/v3.13.0a5
- version: 3.13.0a5
- config: 
- commit hash: [076d169](https://github.com/python/cpython/commit/076d169)
- commit date: 2024-03-12T21:11:08+01:00
- commit merge base: [f6e7a6ce651b43c6e060608a4bb20685f39e9eaa](https://github.com/python/cpython/commit/f6e7a6ce651b43c6e060608a4bb20685f39e9eaa)
- ref: v3.13.0a5

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9038493794)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169.json)

### vs. 3.10.4

- Geometric mean: 1.299x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.10.4.md)
- [📈time plot](bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.012x faster (HPT: reliability of 90.36%, 1.00x faster at 99th %ile)
- Memory usage: 0.90x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: flaskblogging
- [📄table](bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.12.0.md)
- [📈time plot](bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.007x faster (HPT: reliability of 81.85%, 1.00x faster at 99th %ile)
- Memory usage: 0.88x
- missing benchmarks: bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
- [📄table](bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.13.0.md)
- [📈time plot](bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.13.0.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9038493794)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169.json)

### vs. 3.10.4

- Geometric mean: 1.361x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.10.4.md)
- [📈time plot](bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.029x faster (HPT: reliability of 99.94%, 1.00x faster at 99th %ile)
- Memory usage: 0.94x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.12.0.md)
- [📈time plot](bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.016x slower (HPT: reliability of 99.60%, 1.00x slower at 99th %ile)
- Memory usage: 0.88x
- missing benchmarks: bpe_tokeniser, connected_components, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
- [📄table](bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.13.0.md)
- [📈time plot](bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9038493794)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169.json)

### vs. 3.10.4

- Geometric mean: 1.293x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.10.4.md)
- [📈time plot](bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.011x slower (HPT: reliability of 98.97%, 1.00x slower at 99th %ile)
- Memory usage: 0.90x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.12.0.md)
- [📈time plot](bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.001x faster (HPT: reliability of 69.67%, 1.00x slower at 99th %ile)
- Memory usage: 0.88x
- missing benchmarks: bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
- [📄table](bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.13.0.md)
- [📈time plot](bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9038493794)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169.json)

### vs. 3.10.4

- Geometric mean: 1.226x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.10.4.md)
- [📈time plot](bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.054x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.12.0.md)
- [📈time plot](bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.013x faster (HPT: reliability of 94.73%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
- [📄table](bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.13.0.md)
- [📈time plot](bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.13.0.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9038493794)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169.json)

### vs. 3.10.4

- Geometric mean: 1.191x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169-vs-3.10.4.md)
- [📈time plot](bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.227x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169-vs-3.12.0.md)
- [📈time plot](bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.078x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, djangocms, dulwich_log, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, flaskblogging, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
- [📄table](bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169-vs-3.13.0.md)
- [📈time plot](bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9038493794)
- cpu model: missing
- platform: macOS-14.4.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169.json)

### vs. 3.10.4

- Geometric mean: 1.189x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: 0.46x
- missing benchmarks: bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
- [📄table](bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.10.4.md)
- [📈time plot](bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.011x slower (HPT: reliability of 99.10%, 1.00x slower at 99th %ile)
- Memory usage: 0.51x
- missing benchmarks: bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
- [📄table](bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.12.0.md)
- [📈time plot](bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.016x faster (HPT: reliability of 66.29%, 1.00x faster at 99th %ile)
- Memory usage: 0.50x
- missing benchmarks: bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
- [📄table](bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.13.0.md)
- [📈time plot](bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169-vs-3.13.0.svg)

