# Results

- fork: mdboom/simplify_richcompare
- version: 3.14.0a0
- config: 
- commit hash: [15b187e](https://github.com/mdboom/cpython/commit/15b187e)
- commit date: 2024-08-29T11:00:39-04:00
- commit merge base: [58ce131037ecb34d506a613f21993cde2056f628](https://github.com/python/cpython/commit/58ce131037ecb34d506a613f21993cde2056f628)
- ref: simplify_richcompare

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10707835585)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e.json)

### vs. 3.10.4

- Geometric mean: 1.338x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-3.10.4.md)
- [📈time plot](bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.042x faster (HPT: reliability of 99.74%, 1.00x faster at 99th %ile)
- Memory usage: 0.94x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-3.12.0.md)
- [📈time plot](bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.031x faster (HPT: reliability of 99.98%, 1.00x faster at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl
- [📄table](bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-3.13.0.md)
- [📈time plot](bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.000x faster (HPT: reliability of 66.52%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-base-mem.svg)
- [📄table](bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-base.md)
- [📈time plot](bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10707835585)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-192-generic-x86_64-with-glibc2.31
- [raw results](bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e.json)

### vs. 3.10.4

- Geometric mean: 1.436x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-3.10.4.md)
- [📈time plot](bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.087x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-3.12.0.md)
- [📈time plot](bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.033x faster (HPT: reliability of 99.52%, 1.00x faster at 99th %ile)
- Memory usage: 0.92x
- missing benchmarks: chameleon, connected_components, djangocms, dulwich_log, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl
- [📄table](bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-3.13.0.md)
- [📈time plot](bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x slower (HPT: reliability of 53.08%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-base-mem.svg)
- [📄table](bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-base.md)
- [📈time plot](bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10707835585)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e.json)

### vs. 3.10.4

- Geometric mean: 1.342x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-3.10.4.md)
- [📈time plot](bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.031x faster (HPT: reliability of 94.92%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-3.12.0.md)
- [📈time plot](bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.039x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: chameleon, connected_components, djangocms, dulwich_log, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl
- [📄table](bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-3.13.0.md)
- [📈time plot](bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x slower (HPT: reliability of 65.86%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-base-mem.svg)
- [📄table](bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-base.md)
- [📈time plot](bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10707835585)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e.json)

### vs. 3.10.4

- Geometric mean: 1.183x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-3.10.4.md)
- [📈time plot](bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.007x slower (HPT: reliability of 98.54%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-3.12.0.md)
- [📈time plot](bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.015x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl
- [📄table](bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-3.13.0.md)
- [📈time plot](bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.017x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-base.md)
- [📈time plot](bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10707835585)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e.json)

### vs. 3.10.4

- Geometric mean: 1.129x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-3.10.4.md)
- [📈time plot](bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.133x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-3.12.0.md)
- [📈time plot](bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.026x faster (HPT: reliability of 99.68%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl
- [📄table](bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-3.13.0.md)
- [📈time plot](bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x faster (HPT: reliability of 61.01%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-base.md)
- [📈time plot](bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10707835585)
- cpu model: missing
- platform: macOS-14.6.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-15b187e.json)

### vs. 3.10.4

- Geometric mean: 1.304x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 0.53x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl
- [📄table](bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-3.10.4.md)
- [📈time plot](bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.089x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.48x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl
- [📄table](bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-3.12.0.md)
- [📈time plot](bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.094x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.42x
- missing benchmarks: chameleon, connected_components, dask, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl
- [📄table](bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-3.13.0.md)
- [📈time plot](bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x slower (HPT: reliability of 94.57%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-base-mem.svg)
- [📄table](bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-base.md)
- [📈time plot](bm-20240829-darwin-arm64-mdboom-simplify_richcompare-3.14.0a0-15b187e-vs-base.svg)

