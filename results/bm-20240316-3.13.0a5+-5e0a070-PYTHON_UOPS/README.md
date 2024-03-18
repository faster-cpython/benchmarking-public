# Results

- fork: python
- version: 3.13.0a5+
- tier 2: True
- jit: False
- commit hash: [5e0a070](https://github.com/python/cpython/commit/5e0a070)
- commit date: 2024-03-16T21:37:11+01:00
- commit merge base: [259dbc448dabc1ad95fcf6f70eff4b6b5355e71c](https://github.com/python/cpython/commit/259dbc448dabc1ad95fcf6f70eff4b6b5355e71c)
- ref: 5e0a070dfe33530756fa

## linux x86_64 (azure)

- [pystats raw](bm-20240316-azure-x86_64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-pystats.json)
- [pystats table](bm-20240316-azure-x86_64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-pystats.md)

### vs. base

- [pystats diff](bm-20240316-azure-x86_64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8311374974)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240316-linux-x86_64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070.json)

### vs. 3.10.4

- Geometric mean: 1.22x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240316-linux-x86_64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.10.4.md)
- [📈time plot](bm-20240316-linux-x86_64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.04x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240316-linux-x86_64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.11.0.md)
- [📈time plot](bm-20240316-linux-x86_64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.06x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: 0.94x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: djangocms, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240316-linux-x86_64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.12.0.md)
- [📈time plot](bm-20240316-linux-x86_64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.12.0.png)

### vs. base

- Geometric mean: 1.09x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20240316-linux-x86_64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-base-mem.png)
- [📄table](bm-20240316-linux-x86_64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-base.md)
- [📈time plot](bm-20240316-linux-x86_64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-base.png)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8311374974)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-97-generic-x86_64-with-glibc2.35
- [raw results](bm-20240316-pythonperf2-x86_64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070.json)

### vs. 3.10.4

- Geometric mean: 1.17x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240316-pythonperf2-x86_64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.10.4.md)
- [📈time plot](bm-20240316-pythonperf2-x86_64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.03x slower (HPT: reliability of 99.36%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240316-pythonperf2-x86_64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.11.0.md)
- [📈time plot](bm-20240316-pythonperf2-x86_64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.10x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: 0.89x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240316-pythonperf2-x86_64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.12.0.md)
- [📈time plot](bm-20240316-pythonperf2-x86_64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.12.0.png)

### vs. base

- Geometric mean: 1.09x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20240316-pythonperf2-x86_64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-base-mem.png)
- [📄table](bm-20240316-pythonperf2-x86_64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-base.md)
- [📈time plot](bm-20240316-pythonperf2-x86_64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-base.png)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8311374974)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070.json)

### vs. 3.10.4

- Geometric mean: 1.14x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: dask, flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.10.4.md)
- [📈time plot](bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.02x faster (HPT: reliability of 97.98%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: dask, flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.11.0.md)
- [📈time plot](bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.01x slower (HPT: reliability of 84.64%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.12.0.md)
- [📈time plot](bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.12.0.png)

### vs. base

- Geometric mean: 1.06x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-base.md)
- [📈time plot](bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-base.png)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8311374974)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070.json)

### vs. 3.10.4

- Geometric mean: 1.10x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.10.4.md)
- [📈time plot](bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.21x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.11.0.md)
- [📈time plot](bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.14x faster (HPT: reliability of 100.00%, 1.12x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.12.0.md)
- [📈time plot](bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.12.0.png)

### vs. base

- Geometric mean: 1.07x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-base.md)
- [📈time plot](bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-base.png)

