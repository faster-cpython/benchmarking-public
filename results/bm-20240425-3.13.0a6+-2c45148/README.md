# Results

- fork: python
- version: 3.13.0a6+
- config: 
- commit hash: [2c45148](https://github.com/python/cpython/commit/2c45148)
- commit date: 2024-04-25T13:51:31+02:00
- commit merge base: [f180b31e7629d36265fa36f1560365358b4fd47c](https://github.com/python/cpython/commit/f180b31e7629d36265fa36f1560365358b4fd47c)
- ref: 2c451489122d539080c8

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9273657041)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240425-linux-x86_64-python-2c451489122d539080c8-3.13.0a6%2B-2c45148.json)

### vs. 3.10.4

- Geometric mean: 1.34x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240425-linux-x86_64-python-2c451489122d539080c8-3.13.0a6%2B-2c45148-vs-3.10.4.md)
- [📈time plot](bm-20240425-linux-x86_64-python-2c451489122d539080c8-3.13.0a6%2B-2c45148-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x faster (HPT: reliability of 99.96%, 1.01x faster at 99th %ile)
- Memory usage: 0.96x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240425-linux-x86_64-python-2c451489122d539080c8-3.13.0a6%2B-2c45148-vs-3.12.0.md)
- [📈time plot](bm-20240425-linux-x86_64-python-2c451489122d539080c8-3.13.0a6%2B-2c45148-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: bpe_tokeniser
- [📄table](bm-20240425-linux-x86_64-python-2c451489122d539080c8-3.13.0a6%2B-2c45148-vs-3.13.0b2.md)
- [📈time plot](bm-20240425-linux-x86_64-python-2c451489122d539080c8-3.13.0a6%2B-2c45148-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 0.99x
- [🧠memory plot](bm-20240425-linux-x86_64-python-2c451489122d539080c8-3.13.0a6%2B-2c45148-vs-base-mem.svg)
- [📄table](bm-20240425-linux-x86_64-python-2c451489122d539080c8-3.13.0a6%2B-2c45148-vs-base.md)
- [📈time plot](bm-20240425-linux-x86_64-python-2c451489122d539080c8-3.13.0a6%2B-2c45148-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8849402063)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240425-pythonperf2-x86_64-python-2c451489122d539080c8-3.13.0a6%2B-2c45148.json)

### vs. 3.10.4

- Geometric mean: 1.31x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240425-pythonperf2-x86_64-python-2c451489122d539080c8-3.13.0a6%2B-2c45148-vs-3.10.4.md)
- [📈time plot](bm-20240425-pythonperf2-x86_64-python-2c451489122d539080c8-3.13.0a6%2B-2c45148-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.01x faster (HPT: reliability of 93.83%, 1.00x faster at 99th %ile)
- Memory usage: 0.92x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240425-pythonperf2-x86_64-python-2c451489122d539080c8-3.13.0a6%2B-2c45148-vs-3.12.0.md)
- [📈time plot](bm-20240425-pythonperf2-x86_64-python-2c451489122d539080c8-3.13.0a6%2B-2c45148-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: bpe_tokeniser, flaskblogging
- [📄table](bm-20240425-pythonperf2-x86_64-python-2c451489122d539080c8-3.13.0a6%2B-2c45148-vs-3.13.0b2.md)
- [📈time plot](bm-20240425-pythonperf2-x86_64-python-2c451489122d539080c8-3.13.0a6%2B-2c45148-vs-3.13.0b2.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8849402063)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240425-pythonperf1-amd64-python-2c451489122d539080c8-3.13.0a6%2B-2c45148.json)

### vs. 3.10.4

- Geometric mean: 1.18x faster (HPT: reliability of 100.00%, 1.15x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: dask, flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240425-pythonperf1-amd64-python-2c451489122d539080c8-3.13.0a6%2B-2c45148-vs-3.10.4.md)
- [📈time plot](bm-20240425-pythonperf1-amd64-python-2c451489122d539080c8-3.13.0a6%2B-2c45148-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240425-pythonperf1-amd64-python-2c451489122d539080c8-3.13.0a6%2B-2c45148-vs-3.12.0.md)
- [📈time plot](bm-20240425-pythonperf1-amd64-python-2c451489122d539080c8-3.13.0a6%2B-2c45148-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: flaskblogging
- [📄table](bm-20240425-pythonperf1-amd64-python-2c451489122d539080c8-3.13.0a6%2B-2c45148-vs-3.13.0b2.md)
- [📈time plot](bm-20240425-pythonperf1-amd64-python-2c451489122d539080c8-3.13.0a6%2B-2c45148-vs-3.13.0b2.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8849402063)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240425-pythonperf1_win32-x86-python-2c451489122d539080c8-3.13.0a6%2B-2c45148.json)

### vs. 3.10.4

- Geometric mean: 1.15x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240425-pythonperf1_win32-x86-python-2c451489122d539080c8-3.13.0a6%2B-2c45148-vs-3.10.4.md)
- [📈time plot](bm-20240425-pythonperf1_win32-x86-python-2c451489122d539080c8-3.13.0a6%2B-2c45148-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.19x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240425-pythonperf1_win32-x86-python-2c451489122d539080c8-3.13.0a6%2B-2c45148-vs-3.12.0.md)
- [📈time plot](bm-20240425-pythonperf1_win32-x86-python-2c451489122d539080c8-3.13.0a6%2B-2c45148-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.00x slower (HPT: reliability of 50.83%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: flaskblogging
- [📄table](bm-20240425-pythonperf1_win32-x86-python-2c451489122d539080c8-3.13.0a6%2B-2c45148-vs-3.13.0b2.md)
- [📈time plot](bm-20240425-pythonperf1_win32-x86-python-2c451489122d539080c8-3.13.0a6%2B-2c45148-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8849402063)
- cpu model: missing
- platform: macOS-14.4.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240425-darwin-arm64-python-2c451489122d539080c8-3.13.0a6%2B-2c45148.json)

### vs. 3.10.4

- Geometric mean: 1.25x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240425-darwin-arm64-python-2c451489122d539080c8-3.13.0a6%2B-2c45148-vs-3.10.4.md)
- [📈time plot](bm-20240425-darwin-arm64-python-2c451489122d539080c8-3.13.0a6%2B-2c45148-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.05x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240425-darwin-arm64-python-2c451489122d539080c8-3.13.0a6%2B-2c45148-vs-3.12.0.md)
- [📈time plot](bm-20240425-darwin-arm64-python-2c451489122d539080c8-3.13.0a6%2B-2c45148-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: bpe_tokeniser, flaskblogging
- [📄table](bm-20240425-darwin-arm64-python-2c451489122d539080c8-3.13.0a6%2B-2c45148-vs-3.13.0b2.md)
- [📈time plot](bm-20240425-darwin-arm64-python-2c451489122d539080c8-3.13.0a6%2B-2c45148-vs-3.13.0b2.svg)

