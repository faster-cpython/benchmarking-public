# Results

- fork: python
- version: 3.13.0a3+
- tier 2: False
- jit: False
- commit hash: [52eade2](https://github.com/python/cpython/commit/52eade2)
- commit date: 2024-01-20T14:10:43-07:00
- commit merge base: [c48b8f8db8625fe543691e3306f4226435f77ec8](https://github.com/python/cpython/commit/c48b8f8db8625fe543691e3306f4226435f77ec8)
- ref: 52eade22237eef1f3843

## linux x86_64 (azure)

- [pystats raw](bm-20240120-azure-x86_64-python-52eade22237eef1f3843-3.13.0a3%2B-52eade2-pystats.json)
- [pystats table](bm-20240120-azure-x86_64-python-52eade22237eef1f3843-3.13.0a3%2B-52eade2-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/7597787721)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240120-linux-x86_64-python-52eade22237eef1f3843-3.13.0a3%2B-52eade2.json)

### vs. 3.10.4

- Geometric mean: 1.36x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240120-linux-x86_64-python-52eade22237eef1f3843-3.13.0a3%2B-52eade2-vs-3.10.4.md)
- [📈time plot](bm-20240120-linux-x86_64-python-52eade22237eef1f3843-3.13.0a3%2B-52eade2-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
- [📄table](bm-20240120-linux-x86_64-python-52eade22237eef1f3843-3.13.0a3%2B-52eade2-vs-3.11.0.md)
- [📈time plot](bm-20240120-linux-x86_64-python-52eade22237eef1f3843-3.13.0a3%2B-52eade2-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.05x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, django_template, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240120-linux-x86_64-python-52eade22237eef1f3843-3.13.0a3%2B-52eade2-vs-3.12.0.md)
- [📈time plot](bm-20240120-linux-x86_64-python-52eade22237eef1f3843-3.13.0a3%2B-52eade2-vs-3.12.0.png)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/7597787721)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-88-generic-x86_64-with-glibc2.35
- [raw results](bm-20240120-pythonperf2-x86_64-python-52eade22237eef1f3843-3.13.0a3%2B-52eade2.json)

### vs. 3.10.4

- Geometric mean: 1.29x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240120-pythonperf2-x86_64-python-52eade22237eef1f3843-3.13.0a3%2B-52eade2-vs-3.10.4.md)
- [📈time plot](bm-20240120-pythonperf2-x86_64-python-52eade22237eef1f3843-3.13.0a3%2B-52eade2-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.07x faster (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
- [📄table](bm-20240120-pythonperf2-x86_64-python-52eade22237eef1f3843-3.13.0a3%2B-52eade2-vs-3.11.0.md)
- [📈time plot](bm-20240120-pythonperf2-x86_64-python-52eade22237eef1f3843-3.13.0a3%2B-52eade2-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.01x slower (HPT: reliability of 62.69%, 1.00x slower at 99th %ile)
- Memory usage: 0.88x
- missing benchmarks: aiohttp, django_template, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240120-pythonperf2-x86_64-python-52eade22237eef1f3843-3.13.0a3%2B-52eade2-vs-3.12.0.md)
- [📈time plot](bm-20240120-pythonperf2-x86_64-python-52eade22237eef1f3843-3.13.0a3%2B-52eade2-vs-3.12.0.png)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/7597787721)
- cpu model: missing
- platform: Windows-11-10.0.22621-SP0
- [raw results](bm-20240120-pythonperf1-amd64-python-52eade22237eef1f3843-3.13.0a3%2B-52eade2.json)

### vs. 3.10.4

- Geometric mean: 1.24x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240120-pythonperf1-amd64-python-52eade22237eef1f3843-3.13.0a3%2B-52eade2-vs-3.10.4.md)
- [📈time plot](bm-20240120-pythonperf1-amd64-python-52eade22237eef1f3843-3.13.0a3%2B-52eade2-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.11x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
- [📄table](bm-20240120-pythonperf1-amd64-python-52eade22237eef1f3843-3.13.0a3%2B-52eade2-vs-3.11.0.md)
- [📈time plot](bm-20240120-pythonperf1-amd64-python-52eade22237eef1f3843-3.13.0a3%2B-52eade2-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.04x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, django_template, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240120-pythonperf1-amd64-python-52eade22237eef1f3843-3.13.0a3%2B-52eade2-vs-3.12.0.md)
- [📈time plot](bm-20240120-pythonperf1-amd64-python-52eade22237eef1f3843-3.13.0a3%2B-52eade2-vs-3.12.0.png)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/7597787721)
- cpu model: missing
- platform: Windows-11-10.0.22621-SP0
- [raw results](bm-20240120-pythonperf1_win32-x86-python-52eade22237eef1f3843-3.13.0a3%2B-52eade2.json)

### vs. 3.10.4

- Geometric mean: 1.19x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, django_template, dulwich_log, flaskblogging, genshi_text, genshi_xml, html5lib, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240120-pythonperf1_win32-x86-python-52eade22237eef1f3843-3.13.0a3%2B-52eade2-vs-3.10.4.md)
- [📈time plot](bm-20240120-pythonperf1_win32-x86-python-52eade22237eef1f3843-3.13.0a3%2B-52eade2-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.30x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, django_template, dulwich_log, flaskblogging, genshi_text, genshi_xml, html5lib, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
- [📄table](bm-20240120-pythonperf1_win32-x86-python-52eade22237eef1f3843-3.13.0a3%2B-52eade2-vs-3.11.0.md)
- [📈time plot](bm-20240120-pythonperf1_win32-x86-python-52eade22237eef1f3843-3.13.0a3%2B-52eade2-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.19x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, django_template, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240120-pythonperf1_win32-x86-python-52eade22237eef1f3843-3.13.0a3%2B-52eade2-vs-3.12.0.md)
- [📈time plot](bm-20240120-pythonperf1_win32-x86-python-52eade22237eef1f3843-3.13.0a3%2B-52eade2-vs-3.12.0.png)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/7597787721)
- cpu model: missing
- platform: macOS-14.2.1-arm64-arm-64bit
- [raw results](bm-20240120-darwin-arm64-python-52eade22237eef1f3843-3.13.0a3%2B-52eade2.json)

### vs. 3.10.4

- Geometric mean: 1.19x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240120-darwin-arm64-python-52eade22237eef1f3843-3.13.0a3%2B-52eade2-vs-3.10.4.md)
- [📈time plot](bm-20240120-darwin-arm64-python-52eade22237eef1f3843-3.13.0a3%2B-52eade2-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.03x slower (HPT: reliability of 99.99%, 1.01x slower at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
- [📄table](bm-20240120-darwin-arm64-python-52eade22237eef1f3843-3.13.0a3%2B-52eade2-vs-3.11.0.md)
- [📈time plot](bm-20240120-darwin-arm64-python-52eade22237eef1f3843-3.13.0a3%2B-52eade2-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.00x slower (HPT: reliability of 69.01%, 1.00x slower at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: aiohttp, django_template, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240120-darwin-arm64-python-52eade22237eef1f3843-3.13.0a3%2B-52eade2-vs-3.12.0.md)
- [📈time plot](bm-20240120-darwin-arm64-python-52eade22237eef1f3843-3.13.0a3%2B-52eade2-vs-3.12.0.png)

