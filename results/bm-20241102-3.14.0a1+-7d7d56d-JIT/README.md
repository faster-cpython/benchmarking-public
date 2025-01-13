# Results

- fork: python/7d7d56d8b1147a6b85e1
- version: 3.14.0a1+
- config: JIT
- commit hash: [7d7d56d](https://github.com/python/cpython/commit/7d7d56d)
- commit date: 2024-11-02T10:11:12-07:00
- commit merge base: [868bfcc02ed42a1042851830b79c6877b7f1c7a8](https://github.com/python/cpython/commit/868bfcc02ed42a1042851830b79c6877b7f1c7a8)
- ref: 7d7d56d8b1147a6b85e1

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11646770951)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d.json)

### vs. 3.10.4

- Geometric mean: 1.160x faster (HPT: reliability of 99.99%, 1.03x faster at 99th %ile)
- Memory usage: 1.37x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.10.4.md)
- [📈time plot](bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.088x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.12.0.md)
- [📈time plot](bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.099x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, many_optionals, subparsers
- new benchmarks: dulwich_log
- [📄table](bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.13.0.md)
- [📈time plot](bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.086x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.06x
- [🧠memory plot](bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-base-mem.svg)
- [📄table](bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-base.md)
- [📈time plot](bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11646770951)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241102-linux-x86_64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d.json)

### vs. 3.10.4

- Geometric mean: 1.379x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241102-linux-x86_64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.10.4.md)
- [📈time plot](bm-20241102-linux-x86_64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.055x faster (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241102-linux-x86_64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.12.0.md)
- [📈time plot](bm-20241102-linux-x86_64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.008x slower (HPT: reliability of 88.98%, 1.00x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, many_optionals, subparsers
- [📄table](bm-20241102-linux-x86_64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.13.0.md)
- [📈time plot](bm-20241102-linux-x86_64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.012x slower (HPT: reliability of 94.06%, 1.00x slower at 99th %ile)
- Memory usage: 1.06x
- [🧠memory plot](bm-20241102-linux-x86_64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-base-mem.svg)
- [📄table](bm-20241102-linux-x86_64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-base.md)
- [📈time plot](bm-20241102-linux-x86_64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11646770951)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20241102-pythonperf2-x86_64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d.json)

### vs. 3.10.4

- Geometric mean: 1.277x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241102-pythonperf2-x86_64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.10.4.md)
- [📈time plot](bm-20241102-pythonperf2-x86_64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.013x slower (HPT: reliability of 87.03%, 1.00x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241102-pythonperf2-x86_64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.12.0.md)
- [📈time plot](bm-20241102-pythonperf2-x86_64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.010x slower (HPT: reliability of 78.54%, 1.00x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, many_optionals, subparsers
- [📄table](bm-20241102-pythonperf2-x86_64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.13.0.md)
- [📈time plot](bm-20241102-pythonperf2-x86_64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.023x slower (HPT: reliability of 98.92%, 1.00x slower at 99th %ile)
- Memory usage: 1.06x
- [🧠memory plot](bm-20241102-pythonperf2-x86_64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-base-mem.svg)
- [📄table](bm-20241102-pythonperf2-x86_64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-base.md)
- [📈time plot](bm-20241102-pythonperf2-x86_64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11646770951)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d.json)

### vs. 3.10.4

- Geometric mean: 1.209x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.10.4.md)
- [📈time plot](bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.020x faster (HPT: reliability of 75.17%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.12.0.md)
- [📈time plot](bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.002x slower (HPT: reliability of 96.01%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, many_optionals, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- [📄table](bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.13.0.md)
- [📈time plot](bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.040x faster (HPT: reliability of 94.22%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-base.md)
- [📈time plot](bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11646770951)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d.json)

### vs. 3.10.4

- Geometric mean: 1.027x faster (HPT: reliability of 67.35%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.10.4.md)
- [📈time plot](bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.035x faster (HPT: reliability of 97.80%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence, unpickle, unpickle_list
- new benchmarks: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.12.0.md)
- [📈time plot](bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.072x slower (HPT: reliability of 100.00%, 1.08x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, djangocms, gevent_hub, many_optionals, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- [📄table](bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.13.0.md)
- [📈time plot](bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.093x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-base.md)
- [📈time plot](bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11646770951)
- cpu model: missing
- platform: macOS-15.0.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241102-darwin-arm64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d.json)

### vs. 3.10.4

- Geometric mean: 1.243x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: 1.43x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, many_optionals, subparsers
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20241102-darwin-arm64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.10.4.md)
- [📈time plot](bm-20241102-darwin-arm64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.046x faster (HPT: reliability of 99.84%, 1.01x faster at 99th %ile)
- Memory usage: 1.27x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, many_optionals, subparsers
- [📄table](bm-20241102-darwin-arm64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.12.0.md)
- [📈time plot](bm-20241102-darwin-arm64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.045x faster (HPT: reliability of 99.89%, 1.00x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: chameleon, dask, djangocms, gevent_hub, gunicorn, many_optionals, subparsers
- [📄table](bm-20241102-darwin-arm64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.13.0.md)
- [📈time plot](bm-20241102-darwin-arm64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.034x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.08x
- [🧠memory plot](bm-20241102-darwin-arm64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-base-mem.svg)
- [📄table](bm-20241102-darwin-arm64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-base.md)
- [📈time plot](bm-20241102-darwin-arm64-python-7d7d56d8b1147a6b85e1-3.14.0a1%2B-7d7d56d-vs-base.svg)

