# Results

- fork: python
- version: 3.13.0a5+
- tier 2: False
- jit: False
- commit hash: [5e0a070](https://github.com/python/cpython/commit/5e0a070)
- commit date: 2024-03-16T21:37:11+01:00
- commit merge base: [259dbc448dabc1ad95fcf6f70eff4b6b5355e71c](https://github.com/python/cpython/commit/259dbc448dabc1ad95fcf6f70eff4b6b5355e71c)
- ref: 5e0a070dfe33530756fa

## linux x86_64 (azure)

- [pystats raw](bm-20240316-azure-x86_64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-pystats.json)
- [pystats table](bm-20240316-azure-x86_64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8311374974)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240316-linux-x86_64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070.json)

### vs. 3.10.4

- Geometric mean: 1.34x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240316-linux-x86_64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.10.4.md)
- [📈time plot](bm-20240316-linux-x86_64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.05x faster (HPT: reliability of 99.74%, 1.00x faster at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240316-linux-x86_64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.11.0.md)
- [📈time plot](bm-20240316-linux-x86_64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.02x faster (HPT: reliability of 99.54%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: djangocms, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240316-linux-x86_64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.12.0.md)
- [📈time plot](bm-20240316-linux-x86_64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.12.0.png)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8311374974)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-97-generic-x86_64-with-glibc2.35
- [raw results](bm-20240316-pythonperf2-x86_64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070.json)

### vs. 3.10.4

- Geometric mean: 1.28x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240316-pythonperf2-x86_64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.10.4.md)
- [📈time plot](bm-20240316-pythonperf2-x86_64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.06x faster (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240316-pythonperf2-x86_64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.11.0.md)
- [📈time plot](bm-20240316-pythonperf2-x86_64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.01x slower (HPT: reliability of 94.19%, 1.00x slower at 99th %ile)
- Memory usage: 0.88x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240316-pythonperf2-x86_64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.12.0.md)
- [📈time plot](bm-20240316-pythonperf2-x86_64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.12.0.png)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8311374974)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070.json)

### vs. 3.10.4

- Geometric mean: 1.21x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: dask, flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.10.4.md)
- [📈time plot](bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: dask, flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.11.0.md)
- [📈time plot](bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.05x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.12.0.md)
- [📈time plot](bm-20240316-pythonperf1-amd64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.12.0.png)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8311374974)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070.json)

### vs. 3.10.4

- Geometric mean: 1.18x faster (HPT: reliability of 100.00%, 1.15x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.10.4.md)
- [📈time plot](bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.30x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.11.0.md)
- [📈time plot](bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.22x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.12.0.md)
- [📈time plot](bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.12.0.png)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8350627475)
- cpu model: missing
- platform: macOS-14.4-arm64-arm-64bit-Mach-O
- [raw results](bm-20240316-darwin-arm64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070.json)

### vs. 3.10.4

- Geometric mean: 1.18x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240316-darwin-arm64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.10.4.md)
- [📈time plot](bm-20240316-darwin-arm64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.04x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg
- [📄table](bm-20240316-darwin-arm64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.11.0.md)
- [📈time plot](bm-20240316-darwin-arm64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.01x slower (HPT: reliability of 96.93%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240316-darwin-arm64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.12.0.md)
- [📈time plot](bm-20240316-darwin-arm64-python-5e0a070dfe33530756fa-3.13.0a5%2B-5e0a070-vs-3.12.0.png)

