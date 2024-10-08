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

- Geometric mean: 1.22x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence
- [📄table](bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.10.4.md)
- [📈time plot](bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x slower (HPT: reliability of 98.13%, 1.00x faster at 99th %ile)
- Memory usage: 0.92x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, unpack_sequence
- [📄table](bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.12.0.md)
- [📈time plot](bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x slower (HPT: reliability of 99.91%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.13.0b2.md)
- [📈time plot](bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 71.70%, 1.00x faster at 99th %ile)
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

- Geometric mean: 1.39x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.10.4.md)
- [📈time plot](bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.12.0.md)
- [📈time plot](bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.04x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.13.0b2.md)
- [📈time plot](bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 95.94%, 1.00x slower at 99th %ile)
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

- Geometric mean: 1.25x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.10.4.md)
- [📈time plot](bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x slower (HPT: reliability of 97.82%, 1.00x faster at 99th %ile)
- Memory usage: 0.92x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.12.0.md)
- [📈time plot](bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x slower (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.13.0b2.md)
- [📈time plot](bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 97.96%, 1.00x faster at 99th %ile)
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

- Geometric mean: 1.17x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.10.4.md)
- [📈time plot](bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.01x slower (HPT: reliability of 99.55%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.12.0.md)
- [📈time plot](bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, flaskblogging, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.13.0b2.md)
- [📈time plot](bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.02x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-base.md)
- [📈time plot](bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11222287399)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7.json)

### vs. 3.10.4

- Geometric mean: 1.09x faster (HPT: reliability of 99.72%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.10.4.md)
- [📈time plot](bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.10x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.12.0.md)
- [📈time plot](bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, flaskblogging
- new benchmarks: dulwich_log, unpack_sequence
- [📄table](bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.13.0b2.md)
- [📈time plot](bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 99.51%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-base.md)
- [📈time plot](bm-20241007-pythonperf1_win32-x86-mdboom-marshal_slice-3.14.0a0-0e19ac7-vs-base.svg)

