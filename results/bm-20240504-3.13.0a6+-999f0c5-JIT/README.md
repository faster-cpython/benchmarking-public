# Results

- fork: python
- version: 3.13.0a6+
- config: JIT
- commit hash: [999f0c5](https://github.com/python/cpython/commit/999f0c5)
- commit date: 2024-05-04T18:22:33-05:00
- commit merge base: [08d169f14a715ceaae3d563ced2ff1633d009359](https://github.com/python/cpython/commit/08d169f14a715ceaae3d563ced2ff1633d009359)
- ref: 999f0c512281995fb61a

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8954088503)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240504-arminc-aarch64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5.json)

### vs. 3.10.4

- Geometric mean: 1.19x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: 1.23x
- missing benchmarks: docutils, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240504-arminc-aarch64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5-vs-3.10.4.md)
- [📈time plot](bm-20240504-arminc-aarch64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: docutils, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: flaskblogging
- [📄table](bm-20240504-arminc-aarch64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5-vs-3.12.0.md)
- [📈time plot](bm-20240504-arminc-aarch64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.08x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: bpe_tokeniser, docutils, mypy2
- [📄table](bm-20240504-arminc-aarch64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5-vs-3.13.0b2.md)
- [📈time plot](bm-20240504-arminc-aarch64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.08x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: 🔴 docutils
- [🧠memory plot](bm-20240504-arminc-aarch64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5-vs-base-mem.svg)
- [📄table](bm-20240504-arminc-aarch64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5-vs-base.md)
- [📈time plot](bm-20240504-arminc-aarch64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8954088503)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240504-linux-x86_64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5.json)

### vs. 3.10.4

- Geometric mean: 1.32x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: docutils, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240504-linux-x86_64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5-vs-3.10.4.md)
- [📈time plot](bm-20240504-linux-x86_64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 96.32%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: docutils, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240504-linux-x86_64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5-vs-3.12.0.md)
- [📈time plot](bm-20240504-linux-x86_64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.00x slower (HPT: reliability of 86.78%, 1.00x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: bpe_tokeniser, docutils
- [📄table](bm-20240504-linux-x86_64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5-vs-3.13.0b2.md)
- [📈time plot](bm-20240504-linux-x86_64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 90.48%, 1.00x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: 🔴 docutils
- [🧠memory plot](bm-20240504-linux-x86_64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5-vs-base-mem.svg)
- [📄table](bm-20240504-linux-x86_64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5-vs-base.md)
- [📈time plot](bm-20240504-linux-x86_64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8954088503)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240504-pythonperf2-x86_64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5.json)

### vs. 3.10.4

- Geometric mean: 1.27x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: docutils, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240504-pythonperf2-x86_64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5-vs-3.10.4.md)
- [📈time plot](bm-20240504-pythonperf2-x86_64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.01x slower (HPT: reliability of 72.25%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: docutils, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240504-pythonperf2-x86_64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5-vs-3.12.0.md)
- [📈time plot](bm-20240504-pythonperf2-x86_64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x slower (HPT: reliability of 96.14%, 1.00x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: bpe_tokeniser, docutils
- [📄table](bm-20240504-pythonperf2-x86_64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5-vs-3.13.0b2.md)
- [📈time plot](bm-20240504-pythonperf2-x86_64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 92.94%, 1.00x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: 🔴 docutils
- [🧠memory plot](bm-20240504-pythonperf2-x86_64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5-vs-base-mem.svg)
- [📄table](bm-20240504-pythonperf2-x86_64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5-vs-base.md)
- [📈time plot](bm-20240504-pythonperf2-x86_64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8954088503)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240504-pythonperf1-amd64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5.json)

### vs. 3.10.4

- Geometric mean: 1.18x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: docutils, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240504-pythonperf1-amd64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5-vs-3.10.4.md)
- [📈time plot](bm-20240504-pythonperf1-amd64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x faster (HPT: reliability of 99.30%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: docutils, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240504-pythonperf1-amd64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5-vs-3.12.0.md)
- [📈time plot](bm-20240504-pythonperf1-amd64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.04x slower (HPT: reliability of 99.99%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: docutils, sqlglot_normalize
- new benchmarks: dask
- [📄table](bm-20240504-pythonperf1-amd64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5-vs-3.13.0b2.md)
- [📈time plot](bm-20240504-pythonperf1-amd64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.04x slower (HPT: reliability of 99.98%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: 🔴 docutils, sqlglot_normalize
- [📄table](bm-20240504-pythonperf1-amd64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5-vs-base.md)
- [📈time plot](bm-20240504-pythonperf1-amd64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5-vs-base.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8954088503)
- cpu model: missing
- platform: macOS-14.4.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240504-darwin-arm64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5.json)

### vs. 3.10.4

- Geometric mean: 1.23x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 1.43x
- missing benchmarks: docutils, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240504-darwin-arm64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5-vs-3.10.4.md)
- [📈time plot](bm-20240504-darwin-arm64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.05x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: docutils, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240504-darwin-arm64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5-vs-3.12.0.md)
- [📈time plot](bm-20240504-darwin-arm64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x slower (HPT: reliability of 99.37%, 1.00x slower at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: bpe_tokeniser, docutils, sqlglot_normalize
- [📄table](bm-20240504-darwin-arm64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5-vs-3.13.0b2.md)
- [📈time plot](bm-20240504-darwin-arm64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.02x slower (HPT: reliability of 99.99%, 1.00x slower at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: 🔴 docutils, sqlglot_normalize
- [🧠memory plot](bm-20240504-darwin-arm64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5-vs-base-mem.svg)
- [📄table](bm-20240504-darwin-arm64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5-vs-base.md)
- [📈time plot](bm-20240504-darwin-arm64-python-999f0c512281995fb61a-3.13.0a6%2B-999f0c5-vs-base.svg)

