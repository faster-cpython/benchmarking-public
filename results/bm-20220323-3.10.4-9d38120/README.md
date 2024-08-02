# Results

- fork: python
- version: 3.10.4
- config: 
- commit hash: [9d38120](https://github.com/python/cpython/commit/9d38120)
- commit date: 2022-03-23T20:12:04+00:00
- ref: 9d38120e335357a3b294, v3.10.4

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8924024762)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json)

### vs. 3.12.0

- Geometric mean: 1.28x slower (HPT: reliability of 100.00%, 1.22x slower at 99th %ile)
- Memory usage: 0.83x
- missing benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- new benchmarks: flaskblogging
- [📄table](bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120-vs-3.12.0.md)
- [📈time plot](bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.28x slower (HPT: reliability of 100.00%, 1.22x slower at 99th %ile)
- Memory usage: 0.90x
- missing benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- new benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120-vs-3.13.0b2.md)
- [📈time plot](bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120-vs-3.13.0b2.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/7646924903)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json)

### vs. 3.12.0

- Geometric mean: 1.30x slower (HPT: reliability of 100.00%, 1.23x slower at 99th %ile)
- Memory usage: 0.89x
- missing benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- new benchmarks: djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120-vs-3.12.0.md)
- [📈time plot](bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.32x slower (HPT: reliability of 100.00%, 1.24x slower at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- new benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- [📄table](bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120-vs-3.13.0b2.md)
- [📈time plot](bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/7646924903)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-88-generic-x86_64-with-glibc2.35
- [raw results](bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json)

### vs. 3.12.0

- Geometric mean: 1.30x slower (HPT: reliability of 100.00%, 1.22x slower at 99th %ile)
- Memory usage: 0.84x
- missing benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120-vs-3.12.0.md)
- [📈time plot](bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.28x slower (HPT: reliability of 100.00%, 1.21x slower at 99th %ile)
- Memory usage: 0.90x
- missing benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- new benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- [📄table](bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120-vs-3.13.0b2.md)
- [📈time plot](bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120-vs-3.13.0b2.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/7646924903)
- cpu model: missing
- platform: Windows-10-10.0.22621-SP0
- [raw results](bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json)

### vs. 3.12.0

- Geometric mean: 1.19x slower (HPT: reliability of 100.00%, 1.11x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120-vs-3.12.0.md)
- [📈time plot](bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.23x slower (HPT: reliability of 100.00%, 1.19x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- new benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- [📄table](bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120-vs-3.13.0b2.md)
- [📈time plot](bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120-vs-3.13.0b2.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/7646924903)
- cpu model: missing
- platform: Windows-10-10.0.22621-SP0
- [raw results](bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json)

### vs. 3.12.0

- Geometric mean: 1.01x faster (HPT: reliability of 97.16%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120-vs-3.12.0.md)
- [📈time plot](bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.15x slower (HPT: reliability of 100.00%, 1.11x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- new benchmarks: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- [📄table](bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120-vs-3.13.0b2.md)
- [📈time plot](bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/7646924903)
- cpu model: missing
- platform: macOS-14.2.1-arm64-arm-64bit
- [raw results](bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json)

### vs. 3.12.0

- Geometric mean: 1.19x slower (HPT: reliability of 100.00%, 1.13x slower at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120-vs-3.12.0.md)
- [📈time plot](bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.27x slower (HPT: reliability of 100.00%, 1.21x slower at 99th %ile)
- Memory usage: 0.88x
- missing benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- new benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- [📄table](bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120-vs-3.13.0b2.md)
- [📈time plot](bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120-vs-3.13.0b2.svg)

