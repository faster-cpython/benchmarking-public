# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [4717aaa](https://github.com/python/cpython/commit/4717aaa)
- commit date: 2024-06-22T10:58:35-07:00
- commit merge base: [e21347549535b16f51a39986b78a2c2cd4ed09f4](https://github.com/python/cpython/commit/e21347549535b16f51a39986b78a2c2cd4ed09f4)
- ref: 4717aaa1a72d1964f153

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9629150542)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240622-arminc-aarch64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa.json)

### vs. 3.10.4

- Geometric mean: 1.30x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240622-arminc-aarch64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.10.4.md)
- [📈time plot](bm-20240622-arminc-aarch64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.02x faster (HPT: reliability of 79.76%, 1.00x faster at 99th %ile)
- Memory usage: 0.92x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240622-arminc-aarch64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.12.0.md)
- [📈time plot](bm-20240622-arminc-aarch64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x faster (HPT: reliability of 52.22%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240622-arminc-aarch64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.13.0b2.md)
- [📈time plot](bm-20240622-arminc-aarch64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.13.0b2.svg)

## linux x86_64 (azure)

- [pystats raw](bm-20240622-azure-x86_64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-pystats.json)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9646892753)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240622-linux-x86_64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa.json)

### vs. 3.10.4

- Geometric mean: 1.38x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240622-linux-x86_64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.10.4.md)
- [📈time plot](bm-20240622-linux-x86_64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240622-linux-x86_64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.12.0.md)
- [📈time plot](bm-20240622-linux-x86_64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.04x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240622-linux-x86_64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.13.0b2.md)
- [📈time plot](bm-20240622-linux-x86_64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x faster (HPT: reliability of 99.97%, 1.00x faster at 99th %ile)
- Memory usage: 0.98x
- [🧠memory plot](bm-20240622-linux-x86_64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-base-mem.svg)
- [📄table](bm-20240622-linux-x86_64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-base.md)
- [📈time plot](bm-20240622-linux-x86_64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9629150542)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240622-pythonperf2-x86_64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa.json)

### vs. 3.10.4

- Geometric mean: 1.31x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240622-pythonperf2-x86_64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.10.4.md)
- [📈time plot](bm-20240622-pythonperf2-x86_64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.02x faster (HPT: reliability of 63.32%, 1.00x faster at 99th %ile)
- Memory usage: 0.92x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240622-pythonperf2-x86_64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.12.0.md)
- [📈time plot](bm-20240622-pythonperf2-x86_64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x faster (HPT: reliability of 97.30%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240622-pythonperf2-x86_64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.13.0b2.md)
- [📈time plot](bm-20240622-pythonperf2-x86_64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.13.0b2.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9629150542)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa.json)

### vs. 3.10.4

- Geometric mean: 1.28x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.10.4.md)
- [📈time plot](bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.09x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.12.0.md)
- [📈time plot](bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.04x faster (HPT: reliability of 85.79%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2
- [📄table](bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.13.0b2.md)
- [📈time plot](bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.13.0b2.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9629150542)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240622-pythonperf1_win32-x86-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa.json)

### vs. 3.10.4

- Geometric mean: 1.13x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240622-pythonperf1_win32-x86-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.10.4.md)
- [📈time plot](bm-20240622-pythonperf1_win32-x86-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.14x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240622-pythonperf1_win32-x86-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.12.0.md)
- [📈time plot](bm-20240622-pythonperf1_win32-x86-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, flaskblogging
- [📄table](bm-20240622-pythonperf1_win32-x86-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.13.0b2.md)
- [📈time plot](bm-20240622-pythonperf1_win32-x86-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9629150542)
- cpu model: missing
- platform: macOS-14.5-arm64-arm-64bit-Mach-O
- [raw results](bm-20240622-darwin-arm64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa.json)

### vs. 3.10.4

- Geometric mean: 1.28x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240622-darwin-arm64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.10.4.md)
- [📈time plot](bm-20240622-darwin-arm64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.09x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240622-darwin-arm64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.12.0.md)
- [📈time plot](bm-20240622-darwin-arm64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x faster (HPT: reliability of 87.04%, 1.00x slower at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240622-darwin-arm64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.13.0b2.md)
- [📈time plot](bm-20240622-darwin-arm64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa-vs-3.13.0b2.svg)

