# Results

- fork: mdboom/remove_redundant_typ
- version: 3.14.0a0
- config: 
- commit hash: [b0f5f3a](https://github.com/mdboom/cpython/commit/b0f5f3a)
- commit date: 2024-09-23T20:53:22-04:00
- commit merge base: [e256a7590a0149feadfef161ed000991376dc0e8](https://github.com/python/cpython/commit/e256a7590a0149feadfef161ed000991376dc0e8)
- ref: remove_redundant_typ

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11005035708)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a.json)

### vs. 3.10.4

- Geometric mean: 1.332x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence
- [📄table](bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-3.10.4.md)
- [📈time plot](bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.040x faster (HPT: reliability of 97.33%, 1.00x faster at 99th %ile)
- Memory usage: 0.92x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, unpack_sequence
- [📄table](bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-3.12.0.md)
- [📈time plot](bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.031x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 0.90x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-3.13.0.md)
- [📈time plot](bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x slower (HPT: reliability of 67.96%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-base-mem.svg)
- [📄table](bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-base.md)
- [📈time plot](bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11005035708)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-193-generic-x86_64-with-glibc2.31
- [raw results](bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a.json)

### vs. 3.10.4

- Geometric mean: 1.435x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-3.10.4.md)
- [📈time plot](bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.090x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-3.12.0.md)
- [📈time plot](bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.037x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-3.13.0.md)
- [📈time plot](bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.003x slower (HPT: reliability of 99.90%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-base-mem.svg)
- [📄table](bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-base.md)
- [📈time plot](bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11005035708)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a.json)

### vs. 3.10.4

- Geometric mean: 1.336x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-3.10.4.md)
- [📈time plot](bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.028x faster (HPT: reliability of 90.65%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-3.12.0.md)
- [📈time plot](bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.038x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-3.13.0.md)
- [📈time plot](bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.003x faster (HPT: reliability of 89.29%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-base-mem.svg)
- [📄table](bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-base.md)
- [📈time plot](bm-20240923-pythonperf2-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11005035708)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a.json)

### vs. 3.10.4

- Geometric mean: 1.181x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-3.10.4.md)
- [📈time plot](bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.006x slower (HPT: reliability of 98.08%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-3.12.0.md)
- [📈time plot](bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.018x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-3.13.0.md)
- [📈time plot](bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x faster (HPT: reliability of 73.75%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-base.md)
- [📈time plot](bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11005035708)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a.json)

### vs. 3.10.4

- Geometric mean: 1.130x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-3.10.4.md)
- [📈time plot](bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.134x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-3.12.0.md)
- [📈time plot](bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.027x faster (HPT: reliability of 99.95%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-3.13.0.md)
- [📈time plot](bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x faster (HPT: reliability of 81.20%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-base.md)
- [📈time plot](bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11005035708)
- cpu model: missing
- platform: macOS-14.6.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a.json)

### vs. 3.10.4

- Geometric mean: 1.304x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 0.74x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-3.10.4.md)
- [📈time plot](bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.092x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 0.70x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-3.12.0.md)
- [📈time plot](bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.099x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 0.46x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-3.13.0.md)
- [📈time plot](bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x slower (HPT: reliability of 99.98%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-base-mem.svg)
- [📄table](bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-base.md)
- [📈time plot](bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a-vs-base.svg)

