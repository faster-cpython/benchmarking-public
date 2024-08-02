# Results

- fork: python
- version: 3.13.0a1
- config: 
- commit hash: [ad056f0](https://github.com/python/cpython/commit/ad056f0)
- commit date: 2023-10-13T10:52:10+02:00
- commit merge base: [b7f9661bc12fdfec98684c89f03177ae5d3d74c1](https://github.com/python/cpython/commit/b7f9661bc12fdfec98684c89f03177ae5d3d74c1)
- ref: v3.13.0a1

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/6855745543)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0.json)

### vs. 3.10.4

- Geometric mean: 1.34x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, dask, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0-vs-3.10.4.md)
- [📈time plot](bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.02x faster (HPT: reliability of 99.98%, 1.00x faster at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: aiohttp, dask, django_template, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0-vs-3.12.0.md)
- [📈time plot](bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x slower (HPT: reliability of 95.47%, 1.00x faster at 99th %ile)
- Memory usage: 0.94x
- missing benchmarks: aiohttp, bpe_tokeniser, dask, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, mypy2, pylint, thrift
- new benchmarks: unpack_sequence
- [📄table](bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0-vs-3.13.0b2.md)
- [📈time plot](bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/6855745543)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-76-generic-x86_64-with-glibc2.35
- [raw results](bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0.json)

### vs. 3.10.4

- Geometric mean: 1.26x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, dask, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0-vs-3.10.4.md)
- [📈time plot](bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 0.86x
- missing benchmarks: aiohttp, dask, django_template, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0-vs-3.12.0.md)
- [📈time plot](bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 0.94x
- missing benchmarks: aiohttp, bpe_tokeniser, dask, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, mypy2, pylint, thrift
- new benchmarks: unpack_sequence
- [📄table](bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0-vs-3.13.0b2.md)
- [📈time plot](bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0-vs-3.13.0b2.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/6855745543)
- cpu model: missing
- platform: Windows-11-10.0.22621-SP0
- [raw results](bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0.json)

### vs. 3.10.4

- Geometric mean: 1.19x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0-vs-3.10.4.md)
- [📈time plot](bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.01x faster (HPT: reliability of 99.92%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, django_template, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0-vs-3.12.0.md)
- [📈time plot](bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.07x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, mypy2, pylint, thrift
- new benchmarks: unpack_sequence
- [📄table](bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0-vs-3.13.0b2.md)
- [📈time plot](bm-20231013-pythonperf1-amd64-python-v3.13.0a1-3.13.0a1-ad056f0-vs-3.13.0b2.svg)

