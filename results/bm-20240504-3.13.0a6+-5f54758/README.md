# Results

- fork: python
- version: 3.13.0a6+
- config: 
- commit hash: [5f54758](https://github.com/python/cpython/commit/5f54758)
- commit date: 2024-05-04T18:08:38+03:00
- commit merge base: [f34e965e52b9bdf157b829371870edfde45b80bf](https://github.com/python/cpython/commit/f34e965e52b9bdf157b829371870edfde45b80bf)
- ref: 5f547585fa56c94c5d83

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8952860821)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240504-arminc-aarch64-python-5f547585fa56c94c5d83-3.13.0a6%2B-5f54758.json)

### vs. 3.10.4

- Geometric mean: 1.28x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240504-arminc-aarch64-python-5f547585fa56c94c5d83-3.13.0a6%2B-5f54758-vs-3.10.4.md)
- [📈time plot](bm-20240504-arminc-aarch64-python-5f547585fa56c94c5d83-3.13.0a6%2B-5f54758-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.01x faster (HPT: reliability of 61.53%, 1.00x faster at 99th %ile)
- Memory usage: 0.91x
- missing benchmarks: mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: flaskblogging
- [📄table](bm-20240504-arminc-aarch64-python-5f547585fa56c94c5d83-3.13.0a6%2B-5f54758-vs-3.12.0.md)
- [📈time plot](bm-20240504-arminc-aarch64-python-5f547585fa56c94c5d83-3.13.0a6%2B-5f54758-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.00x slower (HPT: reliability of 99.40%, 1.00x slower at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: bpe_tokeniser, mypy2
- [📄table](bm-20240504-arminc-aarch64-python-5f547585fa56c94c5d83-3.13.0a6%2B-5f54758-vs-3.13.0b2.md)
- [📈time plot](bm-20240504-arminc-aarch64-python-5f547585fa56c94c5d83-3.13.0a6%2B-5f54758-vs-3.13.0b2.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8952860821)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240504-linux-x86_64-python-5f547585fa56c94c5d83-3.13.0a6%2B-5f54758.json)

### vs. 3.10.4

- Geometric mean: 1.32x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240504-linux-x86_64-python-5f547585fa56c94c5d83-3.13.0a6%2B-5f54758-vs-3.10.4.md)
- [📈time plot](bm-20240504-linux-x86_64-python-5f547585fa56c94c5d83-3.13.0a6%2B-5f54758-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.02x faster (HPT: reliability of 98.52%, 1.00x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240504-linux-x86_64-python-5f547585fa56c94c5d83-3.13.0a6%2B-5f54758-vs-3.12.0.md)
- [📈time plot](bm-20240504-linux-x86_64-python-5f547585fa56c94c5d83-3.13.0a6%2B-5f54758-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x slower (HPT: reliability of 98.45%, 1.00x slower at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: bpe_tokeniser
- [📄table](bm-20240504-linux-x86_64-python-5f547585fa56c94c5d83-3.13.0a6%2B-5f54758-vs-3.13.0b2.md)
- [📈time plot](bm-20240504-linux-x86_64-python-5f547585fa56c94c5d83-3.13.0a6%2B-5f54758-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8952860821)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240504-pythonperf2-x86_64-python-5f547585fa56c94c5d83-3.13.0a6%2B-5f54758.json)

### vs. 3.10.4

- Geometric mean: 1.28x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240504-pythonperf2-x86_64-python-5f547585fa56c94c5d83-3.13.0a6%2B-5f54758-vs-3.10.4.md)
- [📈time plot](bm-20240504-pythonperf2-x86_64-python-5f547585fa56c94c5d83-3.13.0a6%2B-5f54758-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.00x slower (HPT: reliability of 69.05%, 1.00x slower at 99th %ile)
- Memory usage: 0.92x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240504-pythonperf2-x86_64-python-5f547585fa56c94c5d83-3.13.0a6%2B-5f54758-vs-3.12.0.md)
- [📈time plot](bm-20240504-pythonperf2-x86_64-python-5f547585fa56c94c5d83-3.13.0a6%2B-5f54758-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.00x slower (HPT: reliability of 98.56%, 1.00x slower at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: bpe_tokeniser
- [📄table](bm-20240504-pythonperf2-x86_64-python-5f547585fa56c94c5d83-3.13.0a6%2B-5f54758-vs-3.13.0b2.md)
- [📈time plot](bm-20240504-pythonperf2-x86_64-python-5f547585fa56c94c5d83-3.13.0a6%2B-5f54758-vs-3.13.0b2.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8952860821)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240504-pythonperf1-amd64-python-5f547585fa56c94c5d83-3.13.0a6%2B-5f54758.json)

### vs. 3.10.4

- Geometric mean: 1.22x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240504-pythonperf1-amd64-python-5f547585fa56c94c5d83-3.13.0a6%2B-5f54758-vs-3.10.4.md)
- [📈time plot](bm-20240504-pythonperf1-amd64-python-5f547585fa56c94c5d83-3.13.0a6%2B-5f54758-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240504-pythonperf1-amd64-python-5f547585fa56c94c5d83-3.13.0a6%2B-5f54758-vs-3.12.0.md)
- [📈time plot](bm-20240504-pythonperf1-amd64-python-5f547585fa56c94c5d83-3.13.0a6%2B-5f54758-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x slower (HPT: reliability of 99.21%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- new benchmarks: dask
- [📄table](bm-20240504-pythonperf1-amd64-python-5f547585fa56c94c5d83-3.13.0a6%2B-5f54758-vs-3.13.0b2.md)
- [📈time plot](bm-20240504-pythonperf1-amd64-python-5f547585fa56c94c5d83-3.13.0a6%2B-5f54758-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8952860821)
- cpu model: missing
- platform: macOS-14.4.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240504-darwin-arm64-python-5f547585fa56c94c5d83-3.13.0a6%2B-5f54758.json)

### vs. 3.10.4

- Geometric mean: 1.25x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240504-darwin-arm64-python-5f547585fa56c94c5d83-3.13.0a6%2B-5f54758-vs-3.10.4.md)
- [📈time plot](bm-20240504-darwin-arm64-python-5f547585fa56c94c5d83-3.13.0a6%2B-5f54758-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240504-darwin-arm64-python-5f547585fa56c94c5d83-3.13.0a6%2B-5f54758-vs-3.12.0.md)
- [📈time plot](bm-20240504-darwin-arm64-python-5f547585fa56c94c5d83-3.13.0a6%2B-5f54758-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x slower (HPT: reliability of 63.20%, 1.00x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: bpe_tokeniser
- [📄table](bm-20240504-darwin-arm64-python-5f547585fa56c94c5d83-3.13.0a6%2B-5f54758-vs-3.13.0b2.md)
- [📈time plot](bm-20240504-darwin-arm64-python-5f547585fa56c94c5d83-3.13.0a6%2B-5f54758-vs-3.13.0b2.svg)

