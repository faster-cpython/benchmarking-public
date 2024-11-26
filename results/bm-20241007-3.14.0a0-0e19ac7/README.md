# Results

- fork: mdboom
- version: 3.14.0a0
- config: 
- commit hash: [0e19ac7](https://github.com/mdboom/cpython/commit/0e19ac7)
- commit date: 2024-10-07T15:01:53-04:00
- commit merge base: [c8db0e817e7e0db501533fc8bf5b30c18e60aa3d](https://github.com/mdboom/cpython/commit/c8db0e817e7e0db501533fc8bf5b30c18e60aa3d)
- ref: marshal_slice

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11222287399)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7.json)

### vs. 3.10.4

- Geometric mean: 1.331x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence
- [📄table](bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.10.4.md)
- [📈time plot](bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.040x faster (HPT: reliability of 99.14%, 1.00x faster at 99th %ile)
- Memory usage: 0.92x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, unpack_sequence
- [📄table](bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.12.0.md)
- [📈time plot](bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.030x faster (HPT: reliability of 99.91%, 1.00x faster at 99th %ile)
- Memory usage: 0.90x
- missing benchmarks: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.13.0.md)
- [📈time plot](bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.001x faster (HPT: reliability of 67.02%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-base-mem.svg)
- [📄table](bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-base.md)
- [📈time plot](bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-base.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20241007-azure-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7-pystats.json)
- [pystats table](bm-20241007-azure-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7-pystats.md)

### vs. base

- [pystats diff](bm-20241007-azure-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11222287399)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7.json)

### vs. 3.10.4

- Geometric mean: 1.435x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.10.4.md)
- [📈time plot](bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.089x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.12.0.md)
- [📈time plot](bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.036x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.13.0.md)
- [📈time plot](bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.005x slower (HPT: reliability of 96.70%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-base-mem.svg)
- [📄table](bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-base.md)
- [📈time plot](bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11222287399)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7.json)

### vs. 3.10.4

- Geometric mean: 1.346x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.10.4.md)
- [📈time plot](bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.035x faster (HPT: reliability of 98.32%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.12.0.md)
- [📈time plot](bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.045x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.13.0.md)
- [📈time plot](bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.004x faster (HPT: reliability of 99.53%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-base-mem.svg)
- [📄table](bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-base.md)
- [📈time plot](bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11222287399)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7.json)

### vs. 3.10.4

- Geometric mean: 1.181x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.10.4.md)
- [📈time plot](bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.007x slower (HPT: reliability of 99.64%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.12.0.md)
- [📈time plot](bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.016x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.13.0.md)
- [📈time plot](bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.022x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-base.md)
- [📈time plot](bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11222287399)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7.json)

### vs. 3.10.4

- Geometric mean: 1.107x faster (HPT: reliability of 99.87%, 1.01x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.10.4.md)
- [📈time plot](bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.111x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.12.0.md)
- [📈time plot](bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.007x faster (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.13.0.md)
- [📈time plot](bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.008x slower (HPT: reliability of 98.81%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-base.md)
- [📈time plot](bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-base.svg)

