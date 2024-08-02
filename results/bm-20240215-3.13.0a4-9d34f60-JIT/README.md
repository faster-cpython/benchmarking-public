# Results

- fork: python
- version: 3.13.0a4
- config: JIT
- commit hash: [9d34f60](https://github.com/python/cpython/commit/9d34f60)
- commit date: 2024-02-15T14:38:42+01:00
- commit merge base: [b0e5c35ded6d4a16d7a021c10c99bac94250edd0](https://github.com/python/cpython/commit/b0e5c35ded6d4a16d7a021c10c99bac94250edd0)
- ref: v3.13.0a4

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8145060170)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json)

### vs. 3.10.4

- Geometric mean: 1.31x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-3.10.4.md)
- [📈time plot](bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.01x faster (HPT: reliability of 72.82%, 1.00x slower at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: aiohttp, django_template, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-3.12.0.md)
- [📈time plot](bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x slower (HPT: reliability of 97.88%, 1.00x slower at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: aiohttp, bpe_tokeniser, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, thrift
- new benchmarks: unpack_sequence
- [📄table](bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-3.13.0b2.md)
- [📈time plot](bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.02x slower (HPT: reliability of 91.27%, 1.00x slower at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: 🔴 aiohttp, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, thrift
- new benchmarks: dask, unpack_sequence
- [🧠memory plot](bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-base-mem.svg)
- [📄table](bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-base.md)
- [📈time plot](bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8145060170)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-97-generic-x86_64-with-glibc2.35
- [raw results](bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json)

### vs. 3.10.4

- Geometric mean: 1.25x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-3.10.4.md)
- [📈time plot](bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: aiohttp, django_template, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-3.12.0.md)
- [📈time plot](bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.04x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, bpe_tokeniser, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, thrift
- new benchmarks: unpack_sequence
- [📄table](bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-3.13.0b2.md)
- [📈time plot](bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.03x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: 🔴 aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, thrift
- new benchmarks: dask, unpack_sequence
- [🧠memory plot](bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-base-mem.svg)
- [📄table](bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-base.md)
- [📈time plot](bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8145060170)
- cpu model: missing
- platform: Windows-11-10.0.22621-SP0
- [raw results](bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60.json)

### vs. 3.10.4

- Geometric mean: 1.23x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-3.10.4.md)
- [📈time plot](bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, django_template, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-3.12.0.md)
- [📈time plot](bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.04x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- new benchmarks: dask, unpack_sequence
- [📄table](bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-3.13.0b2.md)
- [📈time plot](bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 83.44%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: 🔴 aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- new benchmarks: dask, unpack_sequence
- [📄table](bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-base.md)
- [📈time plot](bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8145060170)
- cpu model: missing
- platform: Windows-11-10.0.22621-SP0
- [raw results](bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60.json)

### vs. 3.10.4

- Geometric mean: 1.09x faster (HPT: reliability of 99.97%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, django_template, dulwich_log, flaskblogging, genshi_text, genshi_xml, html5lib, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60-vs-3.10.4.md)
- [📈time plot](bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.10x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, django_template, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60-vs-3.12.0.md)
- [📈time plot](bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.08x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- new benchmarks: dask, unpack_sequence
- [📄table](bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60-vs-3.13.0b2.md)
- [📈time plot](bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.10x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: 🔴 django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- new benchmarks: dask, unpack_sequence
- [📄table](bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60-vs-base.md)
- [📈time plot](bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8145060170)
- cpu model: missing
- platform: macOS-14.3-arm64-arm-64bit-Mach-O
- [raw results](bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60.json)

### vs. 3.10.4

- Geometric mean: 1.18x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: 1.26x
- missing benchmarks: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-3.10.4.md)
- [📈time plot](bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.01x slower (HPT: reliability of 83.43%, 1.00x slower at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: aiohttp, django_template, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-3.12.0.md)
- [📈time plot](bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.09x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, thrift
- new benchmarks: unpack_sequence
- [📄table](bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-3.13.0b2.md)
- [📈time plot](bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 94.81%, 1.00x slower at 99th %ile)
- Memory usage: 6.97x
- missing benchmarks: 🔴 aiohttp, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, thrift
- new benchmarks: dask, unpack_sequence
- [🧠memory plot](bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-base-mem.svg)
- [📄table](bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-base.md)
- [📈time plot](bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60-vs-base.svg)

