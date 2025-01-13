# Results

- fork: python/v3.13.0rc2
- version: 3.13.0rc2
- config: 
- commit hash: [ec61006](https://github.com/python/cpython/commit/ec61006)
- commit date: 2024-09-06T23:15:21+02:00
- ref: v3.13.0rc2

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10774975746)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006.json)

### vs. 3.10.4

- Geometric mean: 1.297x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: dulwich_log, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence
- [📄table](bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006-vs-3.10.4.md)
- [📈time plot](bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.016x faster (HPT: reliability of 87.69%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: dulwich_log, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, flaskblogging, unpack_sequence
- [📄table](bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006-vs-3.12.0.md)
- [📈time plot](bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.011x faster (HPT: reliability of 90.00%, 1.00x faster at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006-vs-3.13.0.md)
- [📈time plot](bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006-vs-3.13.0.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10774975746)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-193-generic-x86_64-with-glibc2.31
- [raw results](bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006.json)

### vs. 3.10.4

- Geometric mean: 1.383x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006-vs-3.10.4.md)
- [📈time plot](bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.060x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006-vs-3.12.0.md)
- [📈time plot](bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.012x faster (HPT: reliability of 68.44%, 1.00x slower at 99th %ile)
- Memory usage: 0.92x
- missing benchmarks: connected_components, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006-vs-3.13.0.md)
- [📈time plot](bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10774975746)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006.json)

### vs. 3.10.4

- Geometric mean: 1.288x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006-vs-3.10.4.md)
- [📈time plot](bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.004x slower (HPT: reliability of 88.90%, 1.00x slower at 99th %ile)
- Memory usage: 0.94x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006-vs-3.12.0.md)
- [📈time plot](bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.008x faster (HPT: reliability of 71.58%, 1.00x slower at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006-vs-3.13.0.md)
- [📈time plot](bm-20240906-pythonperf2-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10774975746)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006.json)

### vs. 3.10.4

- Geometric mean: 1.219x faster (HPT: reliability of 100.00%, 1.15x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006-vs-3.10.4.md)
- [📈time plot](bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.059x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006-vs-3.12.0.md)
- [📈time plot](bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.018x faster (HPT: reliability of 58.13%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006-vs-3.13.0.md)
- [📈time plot](bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006-vs-3.13.0.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10774975746)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006.json)

### vs. 3.10.4

- Geometric mean: 1.132x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006-vs-3.10.4.md)
- [📈time plot](bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.172x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006-vs-3.12.0.md)
- [📈time plot](bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.030x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, flaskblogging, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006-vs-3.13.0.md)
- [📈time plot](bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10774975746)
- cpu model: missing
- platform: macOS-14.6.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006.json)

### vs. 3.10.4

- Geometric mean: 1.265x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: 0.76x
- missing benchmarks: connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006-vs-3.10.4.md)
- [📈time plot](bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.064x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.79x
- missing benchmarks: connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006-vs-3.12.0.md)
- [📈time plot](bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.092x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 0.45x
- missing benchmarks: connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006-vs-3.13.0.md)
- [📈time plot](bm-20240906-darwin-arm64-python-v3.13.0rc2-3.13.0rc2-ec61006-vs-3.13.0.svg)

