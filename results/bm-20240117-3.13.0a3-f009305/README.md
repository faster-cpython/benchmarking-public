# Results

- fork: python/v3.13.0a3
- version: 3.13.0a3
- config: 
- commit hash: [f009305](https://github.com/python/cpython/commit/f009305)
- commit date: 2024-01-17T13:14:40+01:00
- commit merge base: [b204c4beb44c1a9013f8da16984c9129374ed8c5](https://github.com/python/cpython/commit/b204c4beb44c1a9013f8da16984c9129374ed8c5)
- ref: v3.13.0a3

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8975028102)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305.json)

### vs. 3.10.4

- Geometric mean: 1.301x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.10.4.md)
- [📈time plot](bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.012x faster (HPT: reliability of 57.05%, 1.00x faster at 99th %ile)
- Memory usage: 0.89x
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: flaskblogging
- [📄table](bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.12.0.md)
- [📈time plot](bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.007x faster (HPT: reliability of 78.51%, 1.00x slower at 99th %ile)
- Memory usage: 0.86x
- missing benchmarks: bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
- [📄table](bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.13.0.md)
- [📈time plot](bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.13.0.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8975028102)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json)

### vs. 3.10.4

- Geometric mean: 1.356x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.10.4.md)
- [📈time plot](bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.024x faster (HPT: reliability of 99.50%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.12.0.md)
- [📈time plot](bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.021x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 0.87x
- missing benchmarks: bpe_tokeniser, connected_components, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
- [📄table](bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.13.0.md)
- [📈time plot](bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8975028102)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json)

### vs. 3.10.4

- Geometric mean: 1.291x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.10.4.md)
- [📈time plot](bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.014x slower (HPT: reliability of 98.26%, 1.00x slower at 99th %ile)
- Memory usage: 0.89x
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.12.0.md)
- [📈time plot](bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.001x slower (HPT: reliability of 71.48%, 1.00x slower at 99th %ile)
- Memory usage: 0.87x
- missing benchmarks: bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
- [📄table](bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.13.0.md)
- [📈time plot](bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8975028102)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305.json)

### vs. 3.10.4

- Geometric mean: 1.225x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.10.4.md)
- [📈time plot](bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.053x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.12.0.md)
- [📈time plot](bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.011x faster (HPT: reliability of 74.82%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
- [📄table](bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.13.0.md)
- [📈time plot](bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.13.0.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8975028102)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305.json)

### vs. 3.10.4

- Geometric mean: 1.192x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305-vs-3.10.4.md)
- [📈time plot](bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.229x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305-vs-3.12.0.md)
- [📈time plot](bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.078x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, djangocms, dulwich_log, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, flaskblogging, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
- [📄table](bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305-vs-3.13.0.md)
- [📈time plot](bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8975028102)
- cpu model: missing
- platform: macOS-14.4.1-arm64-arm-64bit
- [raw results](bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305.json)

### vs. 3.10.4

- Geometric mean: 1.190x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: bpe_tokeniser, connected_components, dask, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
- [📄table](bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.10.4.md)
- [📈time plot](bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.008x slower (HPT: reliability of 86.69%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: bpe_tokeniser, connected_components, dask, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
- [📄table](bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.12.0.md)
- [📈time plot](bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.010x faster (HPT: reliability of 94.26%, 1.00x faster at 99th %ile)
- Memory usage: 0.88x
- missing benchmarks: bpe_tokeniser, connected_components, dask, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
- [📄table](bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.13.0.md)
- [📈time plot](bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.13.0.svg)

