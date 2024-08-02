# Results

- fork: python
- version: 3.13.0a6+
- config: 
- commit hash: [9762122](https://github.com/python/cpython/commit/9762122)
- commit date: 2024-05-07T09:23:06+00:00
- commit merge base: [fe47d9bee319528ffeb5fd60a615d7f02c7b5585](https://github.com/python/cpython/commit/fe47d9bee319528ffeb5fd60a615d7f02c7b5585)
- ref: 976212223541b89329d8

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9007446271)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240507-arminc-aarch64-python-976212223541b89329d8-3.13.0a6%2B-9762122.json)

### vs. 3.10.4

- Geometric mean: 1.24x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240507-arminc-aarch64-python-976212223541b89329d8-3.13.0a6%2B-9762122-vs-3.10.4.md)
- [📈time plot](bm-20240507-arminc-aarch64-python-976212223541b89329d8-3.13.0a6%2B-9762122-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.02x slower (HPT: reliability of 50.69%, 1.00x slower at 99th %ile)
- Memory usage: 0.92x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: flaskblogging
- [📄table](bm-20240507-arminc-aarch64-python-976212223541b89329d8-3.13.0a6%2B-9762122-vs-3.12.0.md)
- [📈time plot](bm-20240507-arminc-aarch64-python-976212223541b89329d8-3.13.0a6%2B-9762122-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x slower (HPT: reliability of 99.84%, 1.00x slower at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: bpe_tokeniser
- [📄table](bm-20240507-arminc-aarch64-python-976212223541b89329d8-3.13.0a6%2B-9762122-vs-3.13.0b2.md)
- [📈time plot](bm-20240507-arminc-aarch64-python-976212223541b89329d8-3.13.0a6%2B-9762122-vs-3.13.0b2.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9007446271)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240507-linux-x86_64-python-976212223541b89329d8-3.13.0a6%2B-9762122.json)

### vs. 3.10.4

- Geometric mean: 1.28x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240507-linux-x86_64-python-976212223541b89329d8-3.13.0a6%2B-9762122-vs-3.10.4.md)
- [📈time plot](bm-20240507-linux-x86_64-python-976212223541b89329d8-3.13.0a6%2B-9762122-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.01x slower (HPT: reliability of 99.55%, 1.00x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240507-linux-x86_64-python-976212223541b89329d8-3.13.0a6%2B-9762122-vs-3.12.0.md)
- [📈time plot](bm-20240507-linux-x86_64-python-976212223541b89329d8-3.13.0a6%2B-9762122-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x slower (HPT: reliability of 61.23%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: bpe_tokeniser
- [📄table](bm-20240507-linux-x86_64-python-976212223541b89329d8-3.13.0a6%2B-9762122-vs-3.13.0b2.md)
- [📈time plot](bm-20240507-linux-x86_64-python-976212223541b89329d8-3.13.0a6%2B-9762122-vs-3.13.0b2.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9007446271)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240507-pythonperf2-x86_64-python-976212223541b89329d8-3.13.0a6%2B-9762122.json)

### vs. 3.10.4

- Geometric mean: 1.24x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240507-pythonperf2-x86_64-python-976212223541b89329d8-3.13.0a6%2B-9762122-vs-3.10.4.md)
- [📈time plot](bm-20240507-pythonperf2-x86_64-python-976212223541b89329d8-3.13.0a6%2B-9762122-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x slower (HPT: reliability of 90.31%, 1.00x slower at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240507-pythonperf2-x86_64-python-976212223541b89329d8-3.13.0a6%2B-9762122-vs-3.12.0.md)
- [📈time plot](bm-20240507-pythonperf2-x86_64-python-976212223541b89329d8-3.13.0a6%2B-9762122-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x slower (HPT: reliability of 99.34%, 1.00x slower at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: bpe_tokeniser
- [📄table](bm-20240507-pythonperf2-x86_64-python-976212223541b89329d8-3.13.0a6%2B-9762122-vs-3.13.0b2.md)
- [📈time plot](bm-20240507-pythonperf2-x86_64-python-976212223541b89329d8-3.13.0a6%2B-9762122-vs-3.13.0b2.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9007446271)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240507-pythonperf1-amd64-python-976212223541b89329d8-3.13.0a6%2B-9762122.json)

### vs. 3.10.4

- Geometric mean: 1.22x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240507-pythonperf1-amd64-python-976212223541b89329d8-3.13.0a6%2B-9762122-vs-3.10.4.md)
- [📈time plot](bm-20240507-pythonperf1-amd64-python-976212223541b89329d8-3.13.0a6%2B-9762122-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240507-pythonperf1-amd64-python-976212223541b89329d8-3.13.0a6%2B-9762122-vs-3.12.0.md)
- [📈time plot](bm-20240507-pythonperf1-amd64-python-976212223541b89329d8-3.13.0a6%2B-9762122-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x slower (HPT: reliability of 99.99%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- new benchmarks: dask
- [📄table](bm-20240507-pythonperf1-amd64-python-976212223541b89329d8-3.13.0a6%2B-9762122-vs-3.13.0b2.md)
- [📈time plot](bm-20240507-pythonperf1-amd64-python-976212223541b89329d8-3.13.0a6%2B-9762122-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9007446271)
- cpu model: missing
- platform: macOS-14.4.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240507-darwin-arm64-python-976212223541b89329d8-3.13.0a6%2B-9762122.json)

### vs. 3.10.4

- Geometric mean: 1.25x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: 1.17x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240507-darwin-arm64-python-976212223541b89329d8-3.13.0a6%2B-9762122-vs-3.10.4.md)
- [📈time plot](bm-20240507-darwin-arm64-python-976212223541b89329d8-3.13.0a6%2B-9762122-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.06x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240507-darwin-arm64-python-976212223541b89329d8-3.13.0a6%2B-9762122-vs-3.12.0.md)
- [📈time plot](bm-20240507-darwin-arm64-python-976212223541b89329d8-3.13.0a6%2B-9762122-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: bpe_tokeniser
- [📄table](bm-20240507-darwin-arm64-python-976212223541b89329d8-3.13.0a6%2B-9762122-vs-3.13.0b2.md)
- [📈time plot](bm-20240507-darwin-arm64-python-976212223541b89329d8-3.13.0a6%2B-9762122-vs-3.13.0b2.svg)

