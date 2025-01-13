# Results

- fork: python/v3.13.0a2
- version: 3.13.0a2
- config: 
- commit hash: [9c4347e](https://github.com/python/cpython/commit/9c4347e)
- commit date: 2023-11-22T12:20:24+01:00
- commit merge base: [ad0e2a9332626dac4588f18626a20c48f4a58a9c](https://github.com/python/cpython/commit/ad0e2a9332626dac4588f18626a20c48f4a58a9c)
- ref: v3.13.0a2

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8975024045)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e.json)

### vs. 3.10.4

- Geometric mean: 1.305x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.10.4.md)
- [📈time plot](bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.013x faster (HPT: reliability of 87.86%, 1.00x faster at 99th %ile)
- Memory usage: 0.88x
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: flaskblogging
- [📄table](bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.12.0.md)
- [📈time plot](bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.008x faster (HPT: reliability of 74.68%, 1.00x faster at 99th %ile)
- Memory usage: 0.86x
- missing benchmarks: bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
- [📄table](bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.13.0.md)
- [📈time plot](bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.13.0.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20231122-azure-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-pystats.json)
- [pystats table](bm-20231122-azure-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8975024045)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json)

### vs. 3.10.4

- Geometric mean: 1.339x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.10.4.md)
- [📈time plot](bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.009x faster (HPT: reliability of 87.66%, 1.00x faster at 99th %ile)
- Memory usage: 0.92x
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.12.0.md)
- [📈time plot](bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.036x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 0.86x
- missing benchmarks: bpe_tokeniser, connected_components, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
- [📄table](bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.13.0.md)
- [📈time plot](bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8975024045)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json)

### vs. 3.10.4

- Geometric mean: 1.291x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.10.4.md)
- [📈time plot](bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.015x slower (HPT: reliability of 95.27%, 1.00x slower at 99th %ile)
- Memory usage: 0.88x
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.12.0.md)
- [📈time plot](bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.002x slower (HPT: reliability of 76.58%, 1.00x slower at 99th %ile)
- Memory usage: 0.86x
- missing benchmarks: bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
- [📄table](bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.13.0.md)
- [📈time plot](bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8975024045)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e.json)

### vs. 3.10.4

- Geometric mean: 1.221x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.10.4.md)
- [📈time plot](bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.048x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.12.0.md)
- [📈time plot](bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.004x faster (HPT: reliability of 74.54%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
- [📄table](bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.13.0.md)
- [📈time plot](bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.13.0.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8975024045)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e.json)

### vs. 3.10.4

- Geometric mean: 1.095x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.10.4.md)
- [📈time plot](bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.129x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.12.0.md)
- [📈time plot](bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.011x slower (HPT: reliability of 99.42%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, djangocms, dulwich_log, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, flaskblogging, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
- [📄table](bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.13.0.md)
- [📈time plot](bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10798317704)
- cpu model: missing
- platform: macOS-14.6.1-arm64-arm-64bit
- [raw results](bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json)

### vs. 3.10.4

- Geometric mean: 1.190x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: 0.49x
- missing benchmarks: connected_components, dask, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.10.4.md)
- [📈time plot](bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.008x slower (HPT: reliability of 80.44%, 1.00x slower at 99th %ile)
- Memory usage: 0.64x
- missing benchmarks: connected_components, dask, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.12.0.md)
- [📈time plot](bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.008x faster (HPT: reliability of 78.85%, 1.00x faster at 99th %ile)
- Memory usage: 0.57x
- missing benchmarks: connected_components, dask, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.13.0.md)
- [📈time plot](bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.13.0.svg)

