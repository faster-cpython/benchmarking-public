# Results

- fork: python
- version: 3.13.0a3+
- tier 2: True
- jit: False
- commit hash: [68a7b78](https://github.com/python/cpython/commit/68a7b78)
- commit date: 2024-01-18T21:04:40+01:00
- commit merge base: [7fa511ba576b9a760f3971ad16dbbbbf91c3f39c](https://github.com/python/cpython/commit/7fa511ba576b9a760f3971ad16dbbbbf91c3f39c)
- ref: 68a7b78cd5185cbd9456

## linux x86_64 (azure)

- [pystats raw](bm-20240118-azure-x86_64-python-68a7b78cd5185cbd9456-3.13.0a3%2B-68a7b78-pystats.json)
- [pystats table](bm-20240118-azure-x86_64-python-68a7b78cd5185cbd9456-3.13.0a3%2B-68a7b78-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/7589857594)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240118-linux-x86_64-python-68a7b78cd5185cbd9456-3.13.0a3%2B-68a7b78.json)

### vs. 3.10.4

- Geometric mean: 1.26x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240118-linux-x86_64-python-68a7b78cd5185cbd9456-3.13.0a3%2B-68a7b78-vs-3.10.4.md)
- [📈time plot](bm-20240118-linux-x86_64-python-68a7b78cd5185cbd9456-3.13.0a3%2B-68a7b78-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.00x slower (HPT: reliability of 95.75%, 1.00x slower at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: aiohttp, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
- [📄table](bm-20240118-linux-x86_64-python-68a7b78cd5185cbd9456-3.13.0a3%2B-68a7b78-vs-3.11.0.md)
- [📈time plot](bm-20240118-linux-x86_64-python-68a7b78cd5185cbd9456-3.13.0a3%2B-68a7b78-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.03x slower (HPT: reliability of 99.99%, 1.00x slower at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, django_template, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240118-linux-x86_64-python-68a7b78cd5185cbd9456-3.13.0a3%2B-68a7b78-vs-3.12.0.md)
- [📈time plot](bm-20240118-linux-x86_64-python-68a7b78cd5185cbd9456-3.13.0a3%2B-68a7b78-vs-3.12.0.png)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/7589857594)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-88-generic-x86_64-with-glibc2.35
- [raw results](bm-20240118-pythonperf2-x86_64-python-68a7b78cd5185cbd9456-3.13.0a3%2B-68a7b78.json)

### vs. 3.10.4

- Geometric mean: 1.20x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240118-pythonperf2-x86_64-python-68a7b78cd5185cbd9456-3.13.0a3%2B-68a7b78-vs-3.10.4.md)
- [📈time plot](bm-20240118-pythonperf2-x86_64-python-68a7b78cd5185cbd9456-3.13.0a3%2B-68a7b78-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.01x slower (HPT: reliability of 78.00%, 1.00x slower at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
- [📄table](bm-20240118-pythonperf2-x86_64-python-68a7b78cd5185cbd9456-3.13.0a3%2B-68a7b78-vs-3.11.0.md)
- [📈time plot](bm-20240118-pythonperf2-x86_64-python-68a7b78cd5185cbd9456-3.13.0a3%2B-68a7b78-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.08x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 0.88x
- missing benchmarks: aiohttp, django_template, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240118-pythonperf2-x86_64-python-68a7b78cd5185cbd9456-3.13.0a3%2B-68a7b78-vs-3.12.0.md)
- [📈time plot](bm-20240118-pythonperf2-x86_64-python-68a7b78cd5185cbd9456-3.13.0a3%2B-68a7b78-vs-3.12.0.png)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/7589857594)
- cpu model: missing
- platform: Windows-11-10.0.22621-SP0
- [raw results](bm-20240118-pythonperf1-amd64-python-68a7b78cd5185cbd9456-3.13.0a3%2B-68a7b78.json)

### vs. 3.10.4

- Geometric mean: 1.19x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240118-pythonperf1-amd64-python-68a7b78cd5185cbd9456-3.13.0a3%2B-68a7b78-vs-3.10.4.md)
- [📈time plot](bm-20240118-pythonperf1-amd64-python-68a7b78cd5185cbd9456-3.13.0a3%2B-68a7b78-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.06x faster (HPT: reliability of 99.95%, 1.01x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
- [📄table](bm-20240118-pythonperf1-amd64-python-68a7b78cd5185cbd9456-3.13.0a3%2B-68a7b78-vs-3.11.0.md)
- [📈time plot](bm-20240118-pythonperf1-amd64-python-68a7b78cd5185cbd9456-3.13.0a3%2B-68a7b78-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.00x faster (HPT: reliability of 96.70%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, django_template, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240118-pythonperf1-amd64-python-68a7b78cd5185cbd9456-3.13.0a3%2B-68a7b78-vs-3.12.0.md)
- [📈time plot](bm-20240118-pythonperf1-amd64-python-68a7b78cd5185cbd9456-3.13.0a3%2B-68a7b78-vs-3.12.0.png)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/7589857594)
- cpu model: missing
- platform: Windows-11-10.0.22621-SP0
- [raw results](bm-20240118-pythonperf1_win32-x86-python-68a7b78cd5185cbd9456-3.13.0a3%2B-68a7b78.json)

### vs. 3.10.4

- Geometric mean: 1.14x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, django_template, dulwich_log, flaskblogging, genshi_text, genshi_xml, html5lib, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240118-pythonperf1_win32-x86-python-68a7b78cd5185cbd9456-3.13.0a3%2B-68a7b78-vs-3.10.4.md)
- [📈time plot](bm-20240118-pythonperf1_win32-x86-python-68a7b78cd5185cbd9456-3.13.0a3%2B-68a7b78-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.25x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, django_template, dulwich_log, flaskblogging, genshi_text, genshi_xml, html5lib, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
- [📄table](bm-20240118-pythonperf1_win32-x86-python-68a7b78cd5185cbd9456-3.13.0a3%2B-68a7b78-vs-3.11.0.md)
- [📈time plot](bm-20240118-pythonperf1_win32-x86-python-68a7b78cd5185cbd9456-3.13.0a3%2B-68a7b78-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.15x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, django_template, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240118-pythonperf1_win32-x86-python-68a7b78cd5185cbd9456-3.13.0a3%2B-68a7b78-vs-3.12.0.md)
- [📈time plot](bm-20240118-pythonperf1_win32-x86-python-68a7b78cd5185cbd9456-3.13.0a3%2B-68a7b78-vs-3.12.0.png)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/7589857594)
- cpu model: missing
- platform: macOS-14.2.1-arm64-arm-64bit
- [raw results](bm-20240118-darwin-arm64-python-68a7b78cd5185cbd9456-3.13.0a3%2B-68a7b78.json)

### vs. 3.10.4

- Geometric mean: 1.12x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240118-darwin-arm64-python-68a7b78cd5185cbd9456-3.13.0a3%2B-68a7b78-vs-3.10.4.md)
- [📈time plot](bm-20240118-darwin-arm64-python-68a7b78cd5185cbd9456-3.13.0a3%2B-68a7b78-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.09x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
- [📄table](bm-20240118-darwin-arm64-python-68a7b78cd5185cbd9456-3.13.0a3%2B-68a7b78-vs-3.11.0.md)
- [📈time plot](bm-20240118-darwin-arm64-python-68a7b78cd5185cbd9456-3.13.0a3%2B-68a7b78-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.06x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: aiohttp, django_template, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240118-darwin-arm64-python-68a7b78cd5185cbd9456-3.13.0a3%2B-68a7b78-vs-3.12.0.md)
- [📈time plot](bm-20240118-darwin-arm64-python-68a7b78cd5185cbd9456-3.13.0a3%2B-68a7b78-vs-3.12.0.png)

