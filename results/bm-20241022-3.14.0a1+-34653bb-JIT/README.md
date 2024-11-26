# Results

- fork: python
- version: 3.14.0a1+
- config: JIT
- commit hash: [34653bb](https://github.com/python/cpython/commit/34653bb)
- commit date: 2024-10-22T13:42:22-07:00
- commit merge base: [aaed91cabcedc16c089c4b1c9abb1114659a83d3](https://github.com/python/cpython/commit/aaed91cabcedc16c089c4b1c9abb1114659a83d3)
- ref: 34653bba644aa5481613

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11526508734)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241022-arminc-aarch64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb.json)

### vs. 3.10.4

- Geometric mean: 1.166x faster (HPT: reliability of 99.99%, 1.04x faster at 99th %ile)
- Memory usage: 1.37x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241022-arminc-aarch64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.10.4.md)
- [📈time plot](bm-20241022-arminc-aarch64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.086x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, sphinx
- [📄table](bm-20241022-arminc-aarch64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.12.0.md)
- [📈time plot](bm-20241022-arminc-aarch64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.095x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path
- new benchmarks: dulwich_log
- [📄table](bm-20241022-arminc-aarch64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.13.0.md)
- [📈time plot](bm-20241022-arminc-aarch64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.13.0.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20241022-azure-x86_64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-pystats.json)
- [pystats table](bm-20241022-azure-x86_64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11526508734)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb.json)

### vs. 3.10.4

- Geometric mean: 1.392x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.10.4.md)
- [📈time plot](bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.061x faster (HPT: reliability of 99.98%, 1.01x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.12.0.md)
- [📈time plot](bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.003x faster (HPT: reliability of 67.32%, 1.00x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path
- [📄table](bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.13.0.md)
- [📈time plot](bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.13.0.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11526508734)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20241022-pythonperf2-x86_64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb.json)

### vs. 3.10.4

- Geometric mean: 1.276x faster (HPT: reliability of 100.00%, 1.15x faster at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241022-pythonperf2-x86_64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.10.4.md)
- [📈time plot](bm-20241022-pythonperf2-x86_64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.013x slower (HPT: reliability of 73.51%, 1.00x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241022-pythonperf2-x86_64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.12.0.md)
- [📈time plot](bm-20241022-pythonperf2-x86_64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.011x slower (HPT: reliability of 67.16%, 1.00x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path
- [📄table](bm-20241022-pythonperf2-x86_64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.13.0.md)
- [📈time plot](bm-20241022-pythonperf2-x86_64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.13.0.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11526508734)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241022-pythonperf1-amd64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb.json)

### vs. 3.10.4

- Geometric mean: 1.203x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx
- [📄table](bm-20241022-pythonperf1-amd64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.10.4.md)
- [📈time plot](bm-20241022-pythonperf1-amd64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.016x faster (HPT: reliability of 83.20%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241022-pythonperf1-amd64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.12.0.md)
- [📈time plot](bm-20241022-pythonperf1-amd64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.005x slower (HPT: reliability of 99.32%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20241022-pythonperf1-amd64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.13.0.md)
- [📈time plot](bm-20241022-pythonperf1-amd64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.13.0.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11526508734)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241022-pythonperf1_win32-x86-python-34653bba644aa5481613-3.14.0a1%2B-34653bb.json)

### vs. 3.10.4

- Geometric mean: 1.180x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx
- [📄table](bm-20241022-pythonperf1_win32-x86-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.10.4.md)
- [📈time plot](bm-20241022-pythonperf1_win32-x86-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.191x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241022-pythonperf1_win32-x86-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.12.0.md)
- [📈time plot](bm-20241022-pythonperf1_win32-x86-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.066x faster (HPT: reliability of 53.62%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20241022-pythonperf1_win32-x86-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.13.0.md)
- [📈time plot](bm-20241022-pythonperf1_win32-x86-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.13.0.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11526508734)
- cpu model: missing
- platform: macOS-15.0.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241022-darwin-arm64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb.json)

### vs. 3.10.4

- Geometric mean: 1.233x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: 1.43x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx
- [📄table](bm-20241022-darwin-arm64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.10.4.md)
- [📈time plot](bm-20241022-darwin-arm64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.034x faster (HPT: reliability of 97.75%, 1.00x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift
- [📄table](bm-20241022-darwin-arm64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.12.0.md)
- [📈time plot](bm-20241022-darwin-arm64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.037x faster (HPT: reliability of 99.67%, 1.00x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: chameleon, connected_components, dask, gevent_hub, k_core, mypy2, shortest_path
- [📄table](bm-20241022-darwin-arm64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.13.0.md)
- [📈time plot](bm-20241022-darwin-arm64-python-34653bba644aa5481613-3.14.0a1%2B-34653bb-vs-3.13.0.svg)

