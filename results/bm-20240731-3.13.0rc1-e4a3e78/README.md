# Results

- fork: python/v3.13.0rc1
- version: 3.13.0rc1
- config: 
- commit hash: [e4a3e78](https://github.com/python/cpython/commit/e4a3e78)
- commit date: 2024-07-31T20:18:39+02:00
- ref: v3.13.0rc1

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10202928782)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78.json)

### vs. 3.10.4

- Geometric mean: 1.305x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, dulwich_log, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78-vs-3.10.4.md)
- [📈time plot](bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.016x faster (HPT: reliability of 83.19%, 1.00x faster at 99th %ile)
- Memory usage: 0.92x
- missing benchmarks: aiohttp, dulwich_log, gunicorn, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78-vs-3.12.0.md)
- [📈time plot](bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.011x faster (HPT: reliability of 64.28%, 1.00x slower at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dask, mypy2
- [📄table](bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78-vs-3.13.0.md)
- [📈time plot](bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78-vs-3.13.0.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10202928782)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78.json)

### vs. 3.10.4

- Geometric mean: 1.399x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, djangocms, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78-vs-3.10.4.md)
- [📈time plot](bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.062x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, gunicorn, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78-vs-3.12.0.md)
- [📈time plot](bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.012x faster (HPT: reliability of 64.36%, 1.00x faster at 99th %ile)
- Memory usage: 0.92x
- missing benchmarks: connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dask, mypy2
- [📄table](bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78-vs-3.13.0.md)
- [📈time plot](bm-20240731-linux-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10202928782)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78.json)

### vs. 3.10.4

- Geometric mean: 1.305x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78-vs-3.10.4.md)
- [📈time plot](bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.000x slower (HPT: reliability of 81.76%, 1.00x slower at 99th %ile)
- Memory usage: 0.94x
- missing benchmarks: aiohttp, gunicorn, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78-vs-3.12.0.md)
- [📈time plot](bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.013x faster (HPT: reliability of 77.64%, 1.00x faster at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dask, mypy2
- [📄table](bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78-vs-3.13.0.md)
- [📈time plot](bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10202928782)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78.json)

### vs. 3.10.4

- Geometric mean: 1.184x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78-vs-3.10.4.md)
- [📈time plot](bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.027x faster (HPT: reliability of 94.82%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78-vs-3.12.0.md)
- [📈time plot](bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.012x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, mypy2
- [📄table](bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78-vs-3.13.0.md)
- [📈time plot](bm-20240731-pythonperf1-amd64-python-v3.13.0rc1-3.13.0rc1-e4a3e78-vs-3.13.0.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10202928782)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78.json)

### vs. 3.10.4

- Geometric mean: 1.139x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78-vs-3.10.4.md)
- [📈time plot](bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.182x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78-vs-3.12.0.md)
- [📈time plot](bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.034x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl
- [📄table](bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78-vs-3.13.0.md)
- [📈time plot](bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10202928782)
- cpu model: missing
- platform: macOS-14.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78.json)

### vs. 3.10.4

- Geometric mean: 1.291x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 0.65x
- missing benchmarks: connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, mypy2
- [📄table](bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78-vs-3.10.4.md)
- [📈time plot](bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.071x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.59x
- missing benchmarks: connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, mypy2
- [📄table](bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78-vs-3.12.0.md)
- [📈time plot](bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.098x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 0.38x
- missing benchmarks: connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, mypy2
- [📄table](bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78-vs-3.13.0.md)
- [📈time plot](bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78-vs-3.13.0.svg)

