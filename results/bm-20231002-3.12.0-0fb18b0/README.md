# Results

- fork: python
- version: 3.12.0
- config: 
- commit hash: [0fb18b0](https://github.com/python/cpython/commit/0fb18b0)
- commit date: 2023-10-02T13:48:14+02:00
- ref: 0fb18b02c8ad56299d6a, v3.12.0

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8924024991)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json)

### vs. 3.10.4

- Geometric mean: 1.28x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: flaskblogging
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0-vs-3.10.4.md)
- [📈time plot](bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0-vs-3.10.4.svg)

### vs. 3.13.0

- Geometric mean: 1.01x slower (HPT: reliability of 97.91%, 1.00x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: bpe_tokeniser, flaskblogging, unpack_sequence
- new benchmarks: dulwich_log, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0-vs-3.13.0.md)
- [📈time plot](bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0-vs-3.13.0b2.md)
- [📈time plot](bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0-vs-3.13.0b2.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/7646930307)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json)

### vs. 3.10.4

- Geometric mean: 1.30x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0-vs-3.10.4.md)
- [📈time plot](bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0-vs-3.10.4.svg)

### vs. 3.13.0

- Geometric mean: 1.06x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: bpe_tokeniser, djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- new benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0-vs-3.13.0.md)
- [📈time plot](bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0-vs-3.13.0b2.md)
- [📈time plot](bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/7646930307)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-88-generic-x86_64-with-glibc2.35
- [raw results](bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json)

### vs. 3.10.4

- Geometric mean: 1.30x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0-vs-3.10.4.md)
- [📈time plot](bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0-vs-3.10.4.svg)

### vs. 3.13.0

- Geometric mean: 1.00x faster (HPT: reliability of 63.18%, 1.00x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: bpe_tokeniser, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- new benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0-vs-3.13.0.md)
- [📈time plot](bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0-vs-3.13.0b2.md)
- [📈time plot](bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0-vs-3.13.0b2.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/7646930307)
- cpu model: missing
- platform: Windows-11-10.0.22621-SP0
- [raw results](bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json)

### vs. 3.10.4

- Geometric mean: 1.19x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0-vs-3.10.4.md)
- [📈time plot](bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0-vs-3.10.4.svg)

### vs. 3.13.0

- Geometric mean: 1.07x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- new benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0-vs-3.13.0.md)
- [📈time plot](bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0-vs-3.13.0b2.md)
- [📈time plot](bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0-vs-3.13.0b2.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/7646930307)
- cpu model: missing
- platform: Windows-11-10.0.22621-SP0
- [raw results](bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json)

### vs. 3.10.4

- Geometric mean: 1.01x slower (HPT: reliability of 96.37%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0-vs-3.10.4.md)
- [📈time plot](bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0-vs-3.10.4.svg)

### vs. 3.13.0

- Geometric mean: 1.13x slower (HPT: reliability of 100.00%, 1.14x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- new benchmarks: aiohttp, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0-vs-3.13.0.md)
- [📈time plot](bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0-vs-3.13.0b2.md)
- [📈time plot](bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/7646930307)
- cpu model: missing
- platform: macOS-14.2.1-arm64-arm-64bit
- [raw results](bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json)

### vs. 3.10.4

- Geometric mean: 1.19x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0-vs-3.10.4.md)
- [📈time plot](bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0-vs-3.10.4.svg)

### vs. 3.13.0

- Geometric mean: 1.01x faster (HPT: reliability of 90.11%, 1.00x faster at 99th %ile)
- Memory usage: 5.78x
- missing benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- new benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0-vs-3.13.0.md)
- [📈time plot](bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0-vs-3.13.0b2.md)
- [📈time plot](bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0-vs-3.13.0b2.svg)

