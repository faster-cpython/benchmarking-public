# Results

- fork: python/f6cc7c8bd01d8468af70
- version: 3.14.0a1+
- config: 
- commit hash: [f6cc7c8](https://github.com/python/cpython/commit/f6cc7c8)
- commit date: 2024-10-26T23:40:31+02:00
- commit merge base: [26d627779f79d8d5650fe7be348432eccc28f8f9](https://github.com/python/cpython/commit/26d627779f79d8d5650fe7be348432eccc28f8f9)
- ref: f6cc7c8bd01d8468af70

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11535901955)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8.json)

### vs. 3.10.4

- Geometric mean: 1.316x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.10.4.md)
- [📈time plot](bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.025x faster (HPT: reliability of 93.77%, 1.00x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, sphinx
- [📄table](bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.12.0.md)
- [📈time plot](bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.014x faster (HPT: reliability of 88.97%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlite_synth, subparsers
- new benchmarks: dulwich_log
- [📄table](bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.13.0.md)
- [📈time plot](bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.13.0.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20241026-azure-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-pystats.json)
- [pystats table](bm-20241026-azure-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11535901955)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241026-linux-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8.json)

### vs. 3.10.4

- Geometric mean: 1.403x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241026-linux-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.10.4.md)
- [📈time plot](bm-20241026-linux-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.064x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241026-linux-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.12.0.md)
- [📈time plot](bm-20241026-linux-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.010x faster (HPT: reliability of 63.89%, 1.00x faster at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlite_synth, subparsers
- [📄table](bm-20241026-linux-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.13.0.md)
- [📈time plot](bm-20241026-linux-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11535901955)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8.json)

### vs. 3.10.4

- Geometric mean: 1.320x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.10.4.md)
- [📈time plot](bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.014x faster (HPT: reliability of 93.40%, 1.00x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.12.0.md)
- [📈time plot](bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.022x faster (HPT: reliability of 99.94%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlite_synth, subparsers
- [📄table](bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.13.0.md)
- [📈time plot](bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11535901955)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8.json)

### vs. 3.10.4

- Geometric mean: 1.159x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx
- [📄table](bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.10.4.md)
- [📈time plot](bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.027x slower (HPT: reliability of 99.85%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.12.0.md)
- [📈time plot](bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.037x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- [📄table](bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.13.0.md)
- [📈time plot](bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.13.0.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11535901955)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8.json)

### vs. 3.10.4

- Geometric mean: 1.111x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx
- [📄table](bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.10.4.md)
- [📈time plot](bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.111x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.12.0.md)
- [📈time plot](bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.008x faster (HPT: reliability of 99.99%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- [📄table](bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.13.0.md)
- [📈time plot](bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11535901955)
- cpu model: missing
- platform: macOS-15.0.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8.json)

### vs. 3.10.4

- Geometric mean: 1.299x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.31x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sqlite_synth, subparsers
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.10.4.md)
- [📈time plot](bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.076x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlite_synth, subparsers
- [📄table](bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.12.0.md)
- [📈time plot](bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.083x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sqlite_synth, subparsers
- [📄table](bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.13.0.md)
- [📈time plot](bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1%2B-f6cc7c8-vs-3.13.0.svg)

