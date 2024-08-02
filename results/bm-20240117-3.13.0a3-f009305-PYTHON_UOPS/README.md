# Results

- fork: python
- version: 3.13.0a3
- config: T2
- commit hash: [f009305](https://github.com/python/cpython/commit/f009305)
- commit date: 2024-01-17T13:14:40+01:00
- commit merge base: [b204c4beb44c1a9013f8da16984c9129374ed8c5](https://github.com/python/cpython/commit/b204c4beb44c1a9013f8da16984c9129374ed8c5)
- ref: f009305a7d635f86440c, v3.13.0a3

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/7575581884)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json)

### vs. 3.10.4

- Geometric mean: 1.26x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.10.4.md)
- [📈time plot](bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, django_template, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.12.0.md)
- [📈time plot](bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.07x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 0.95x
- missing benchmarks: aiohttp, bpe_tokeniser, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, thrift
- new benchmarks: unpack_sequence
- [📄table](bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.13.0b2.md)
- [📈time plot](bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.06x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: 🔴 aiohttp, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, thrift
- new benchmarks: dask, unpack_sequence
- [🧠memory plot](bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-base-mem.svg)
- [📄table](bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-base.md)
- [📈time plot](bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/7575581884)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-88-generic-x86_64-with-glibc2.35
- [raw results](bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json)

### vs. 3.10.4

- Geometric mean: 1.18x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.10.4.md)
- [📈time plot](bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.10x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: 0.88x
- missing benchmarks: aiohttp, django_template, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.12.0.md)
- [📈time plot](bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.10x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: 0.95x
- missing benchmarks: aiohttp, bpe_tokeniser, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, thrift
- new benchmarks: unpack_sequence
- [📄table](bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.13.0b2.md)
- [📈time plot](bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.09x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: 🔴 aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, thrift
- new benchmarks: dask, unpack_sequence
- [🧠memory plot](bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-base-mem.svg)
- [📄table](bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-base.md)
- [📈time plot](bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/7575581884)
- cpu model: missing
- platform: Windows-11-10.0.22621-SP0
- [raw results](bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305.json)

### vs. 3.10.4

- Geometric mean: 1.19x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.10.4.md)
- [📈time plot](bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.00x faster (HPT: reliability of 98.39%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, django_template, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.12.0.md)
- [📈time plot](bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.08x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- new benchmarks: dask, unpack_sequence
- [📄table](bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.13.0b2.md)
- [📈time plot](bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.04x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: 🔴 aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- new benchmarks: dask, unpack_sequence
- [📄table](bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305-vs-base.md)
- [📈time plot](bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/7583593375)
- cpu model: missing
- platform: Windows-11-10.0.22621-SP0
- [raw results](bm-20240117-pythonperf1_win32-x86-python-f009305a7d635f86440c-3.13.0a3-f009305.json)

### vs. 3.10.4

- Geometric mean: 1.14x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, django_template, dulwich_log, flaskblogging, genshi_text, genshi_xml, html5lib, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240117-pythonperf1_win32-x86-python-f009305a7d635f86440c-3.13.0a3-f009305-vs-3.10.4.md)
- [📈time plot](bm-20240117-pythonperf1_win32-x86-python-f009305a7d635f86440c-3.13.0a3-f009305-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.15x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, django_template, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240117-pythonperf1_win32-x86-python-f009305a7d635f86440c-3.13.0a3-f009305-vs-3.12.0.md)
- [📈time plot](bm-20240117-pythonperf1_win32-x86-python-f009305a7d635f86440c-3.13.0a3-f009305-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.04x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- new benchmarks: dask, unpack_sequence
- [📄table](bm-20240117-pythonperf1_win32-x86-python-f009305a7d635f86440c-3.13.0a3-f009305-vs-3.13.0b2.md)
- [📈time plot](bm-20240117-pythonperf1_win32-x86-python-f009305a7d635f86440c-3.13.0a3-f009305-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.06x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: 🔴 django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- new benchmarks: dask, unpack_sequence
- [📄table](bm-20240117-pythonperf1_win32-x86-python-f009305a7d635f86440c-3.13.0a3-f009305-vs-base.md)
- [📈time plot](bm-20240117-pythonperf1_win32-x86-python-f009305a7d635f86440c-3.13.0a3-f009305-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/7575581884)
- cpu model: missing
- platform: macOS-14.2.1-arm64-arm-64bit
- [raw results](bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305.json)

### vs. 3.10.4

- Geometric mean: 1.12x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.10.4.md)
- [📈time plot](bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.06x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, django_template, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.12.0.md)
- [📈time plot](bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.14x slower (HPT: reliability of 100.00%, 1.09x slower at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, thrift
- new benchmarks: unpack_sequence
- [📄table](bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.13.0b2.md)
- [📈time plot](bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.06x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: 🔴 aiohttp, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, thrift
- new benchmarks: dask, unpack_sequence
- [🧠memory plot](bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305-vs-base-mem.svg)
- [📄table](bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305-vs-base.md)
- [📈time plot](bm-20240117-darwin-arm64-python-v3.13.0a3-3.13.0a3-f009305-vs-base.svg)

