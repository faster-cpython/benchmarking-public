# Results

- fork: mdboom
- version: 3.14.0a0
- config: 
- commit hash: [3b5fdc8](https://github.com/mdboom/cpython/commit/3b5fdc8)
- commit date: 2024-09-11T11:49:04-04:00
- commit merge base: [5436d8b9c397c48d9b0d5f9d4ad5e1d5a5d500f6](https://github.com/mdboom/cpython/commit/5436d8b9c397c48d9b0d5f9d4ad5e1d5a5d500f6)
- ref: pysequence_tuple

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10815139509)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8.json)

### vs. 3.10.4

- Geometric mean: 1.32x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence
- [📄table](bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-3.10.4.md)
- [📈time plot](bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 95.15%, 1.00x faster at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, unpack_sequence
- [📄table](bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-3.12.0.md)
- [📈time plot](bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x faster (HPT: reliability of 99.99%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-3.13.0b2.md)
- [📈time plot](bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 70.84%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-base-mem.svg)
- [📄table](bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-base.md)
- [📈time plot](bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10815139509)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-193-generic-x86_64-with-glibc2.31
- [raw results](bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8.json)

### vs. 3.10.4

- Geometric mean: 1.40x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-3.10.4.md)
- [📈time plot](bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.09x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-3.12.0.md)
- [📈time plot](bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.06x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-3.13.0b2.md)
- [📈time plot](bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 65.59%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-base-mem.svg)
- [📄table](bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-base.md)
- [📈time plot](bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10815139509)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8.json)

### vs. 3.10.4

- Geometric mean: 1.32x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-3.10.4.md)
- [📈time plot](bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.02x faster (HPT: reliability of 68.54%, 1.00x faster at 99th %ile)
- Memory usage: 0.92x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-3.12.0.md)
- [📈time plot](bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x faster (HPT: reliability of 99.94%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-3.13.0b2.md)
- [📈time plot](bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-base-mem.svg)
- [📄table](bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-base.md)
- [📈time plot](bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10815139509)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8.json)

### vs. 3.10.4

- Geometric mean: 1.17x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-3.10.4.md)
- [📈time plot](bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.00x slower (HPT: reliability of 90.42%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-3.12.0.md)
- [📈time plot](bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, flaskblogging, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-3.13.0b2.md)
- [📈time plot](bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-base.md)
- [📈time plot](bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10815139509)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8.json)

### vs. 3.10.4

- Geometric mean: 1.12x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-3.10.4.md)
- [📈time plot](bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.13x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-3.12.0.md)
- [📈time plot](bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, flaskblogging
- new benchmarks: dulwich_log, unpack_sequence
- [📄table](bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-3.13.0b2.md)
- [📈time plot](bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 76.88%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-base.md)
- [📈time plot](bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10815139509)
- cpu model: missing
- platform: macOS-14.6.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8.json)

### vs. 3.10.4

- Geometric mean: 1.28x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 0.90x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-3.10.4.md)
- [📈time plot](bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 0.70x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-3.12.0.md)
- [📈time plot](bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x faster (HPT: reliability of 75.92%, 1.00x slower at 99th %ile)
- Memory usage: 0.59x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-3.13.0b2.md)
- [📈time plot](bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 83.72%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-base-mem.svg)
- [📄table](bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-base.md)
- [📈time plot](bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8-vs-base.svg)

