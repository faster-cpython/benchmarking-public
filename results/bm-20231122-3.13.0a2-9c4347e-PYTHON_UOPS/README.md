# Results

- fork: python
- version: 3.13.0a2
- config: T2
- commit hash: [9c4347e](https://github.com/python/cpython/commit/9c4347e)
- commit date: 2023-11-22T12:20:24+01:00
- commit merge base: [ad0e2a9332626dac4588f18626a20c48f4a58a9c](https://github.com/python/cpython/commit/ad0e2a9332626dac4588f18626a20c48f4a58a9c)
- ref: 9c4347ef8b60f54dd357, v3.13.0a2

## linux x86_64 (azure)

- [pystats raw](bm-20231122-azure-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-pystats.json)
- [pystats table](bm-20231122-azure-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/7575579730)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json)

### vs. 3.10.4

- Geometric mean: 1.26x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.10.4.md)
- [📈time plot](bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: aiohttp, django_template, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.12.0.md)
- [📈time plot](bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.10x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: 0.95x
- missing benchmarks: aiohttp, bpe_tokeniser, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, thrift
- [📄table](bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.13.0.md)
- [📈time plot](bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.05x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: 🔴 aiohttp, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, thrift
- new benchmarks: dask, unpack_sequence
- [🧠memory plot](bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-base-mem.svg)
- [📄table](bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-base.md)
- [📈time plot](bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.13.0b2.md)
- [📈time plot](bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/7575579730)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-88-generic-x86_64-with-glibc2.35
- [raw results](bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json)

### vs. 3.10.4

- Geometric mean: 1.20x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.10.4.md)
- [📈time plot](bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.09x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: 0.87x
- missing benchmarks: aiohttp, django_template, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.12.0.md)
- [📈time plot](bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.08x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: 0.95x
- missing benchmarks: aiohttp, bpe_tokeniser, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, thrift
- [📄table](bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.13.0.md)
- [📈time plot](bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.08x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: 🔴 aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, thrift
- new benchmarks: dask, unpack_sequence
- [🧠memory plot](bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-base-mem.svg)
- [📄table](bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-base.md)
- [📈time plot](bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.13.0b2.md)
- [📈time plot](bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.13.0b2.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/7575579730)
- cpu model: missing
- platform: Windows-11-10.0.22621-SP0
- [raw results](bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e.json)

### vs. 3.10.4

- Geometric mean: 1.18x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.10.4.md)
- [📈time plot](bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.00x slower (HPT: reliability of 78.43%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, django_template, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.12.0.md)
- [📈time plot](bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.07x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- new benchmarks: dask
- [📄table](bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.13.0.md)
- [📈time plot](bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.05x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: 🔴 aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- new benchmarks: dask, unpack_sequence
- [📄table](bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-base.md)
- [📈time plot](bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.13.0b2.md)
- [📈time plot](bm-20231122-pythonperf1-amd64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.13.0b2.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/7583592361)
- cpu model: missing
- platform: Windows-11-10.0.22621-SP0
- [raw results](bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e.json)

### vs. 3.10.4

- Geometric mean: 1.04x faster (HPT: reliability of 94.43%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, django_template, dulwich_log, flaskblogging, genshi_text, genshi_xml, html5lib, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e-vs-3.10.4.md)
- [📈time plot](bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.05x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, django_template, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e-vs-3.12.0.md)
- [📈time plot](bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.07x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: django_template, dulwich_log, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- new benchmarks: dask
- [📄table](bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e-vs-3.13.0.md)
- [📈time plot](bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.07x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: 🔴 django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- new benchmarks: dask, unpack_sequence
- [📄table](bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e-vs-base.md)
- [📈time plot](bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e-vs-3.13.0b2.md)
- [📈time plot](bm-20231122-pythonperf1_win32-x86-python-9c4347ef8b60f54dd357-3.13.0a2-9c4347e-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10792613385)
- cpu model: missing
- platform: macOS-14.6.1-arm64-arm-64bit
- [raw results](bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json)

### vs. 3.10.4

- Geometric mean: 1.17x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: 0.52x
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.10.4.md)
- [📈time plot](bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.01x slower (HPT: reliability of 86.71%, 1.00x slower at 99th %ile)
- Memory usage: 0.55x
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.12.0.md)
- [📈time plot](bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x slower (HPT: reliability of 75.20%, 1.00x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: dask
- [📄table](bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.13.0.md)
- [📈time plot](bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 63.35%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-base-mem.svg)
- [📄table](bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-base.md)
- [📈time plot](bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.13.0b2.md)
- [📈time plot](bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.13.0b2.svg)

