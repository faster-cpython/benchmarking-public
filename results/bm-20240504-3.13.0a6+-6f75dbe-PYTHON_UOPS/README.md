# Results

- fork: faster-cpython
- version: 3.13.0a6+
- config: T2
- commit hash: [6f75dbe](https://github.com/faster%2dcpython/cpython/commit/6f75dbe)
- commit date: 2024-05-04T12:15:01+01:00
- commit merge base: [b034f14a4b6e9197d3926046721b8b4b4b4f5b3d](https://github.com/faster%2dcpython/cpython/commit/b034f14a4b6e9197d3926046721b8b4b4b4f5b3d)
- ref: dynamic_underflow

## linux x86_64 (azure)

- [pystats raw](bm-20240504-azure-x86_64-faster%252dcpython-dynamic_underflow-3.13.0a6%2B-6f75dbe-pystats.json)
- [pystats table](bm-20240504-azure-x86_64-faster%252dcpython-dynamic_underflow-3.13.0a6%2B-6f75dbe-pystats.md)

### vs. base

- [pystats diff](bm-20240504-azure-x86_64-faster%252dcpython-dynamic_underflow-3.13.0a6%2B-6f75dbe-pystats-vs-base.md)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8950109465)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240504-pythonperf2-x86_64-faster%252dcpython-dynamic_underflow-3.13.0a6%2B-6f75dbe.json)

### vs. 3.10.4

- Geometric mean: 1.06x faster (HPT: reliability of 91.17%, 1.00x faster at 99th %ile)
- Memory usage: 1.13x
- missing benchmarks: 2to3, docutils, genshi_text, genshi_xml, html5lib, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240504-pythonperf2-x86_64-faster%252dcpython-dynamic_underflow-3.13.0a6%2B-6f75dbe-vs-3.10.4.md)
- [📈time plot](bm-20240504-pythonperf2-x86_64-faster%252dcpython-dynamic_underflow-3.13.0a6%2B-6f75dbe-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.21x slower (HPT: reliability of 100.00%, 1.12x slower at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: 2to3, docutils, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, pylint, thrift
- [📄table](bm-20240504-pythonperf2-x86_64-faster%252dcpython-dynamic_underflow-3.13.0a6%2B-6f75dbe-vs-3.12.0.md)
- [📈time plot](bm-20240504-pythonperf2-x86_64-faster%252dcpython-dynamic_underflow-3.13.0a6%2B-6f75dbe-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.21x slower (HPT: reliability of 100.00%, 1.12x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: 2to3, bpe_tokeniser, docutils, genshi_text, genshi_xml, html5lib
- [📄table](bm-20240504-pythonperf2-x86_64-faster%252dcpython-dynamic_underflow-3.13.0a6%2B-6f75dbe-vs-3.13.0b2.md)
- [📈time plot](bm-20240504-pythonperf2-x86_64-faster%252dcpython-dynamic_underflow-3.13.0a6%2B-6f75dbe-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.03x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: 🔴 2to3, genshi_text, genshi_xml, html5lib
- [🧠memory plot](bm-20240504-pythonperf2-x86_64-faster%252dcpython-dynamic_underflow-3.13.0a6%2B-6f75dbe-vs-base-mem.svg)
- [📄table](bm-20240504-pythonperf2-x86_64-faster%252dcpython-dynamic_underflow-3.13.0a6%2B-6f75dbe-vs-base.md)
- [📈time plot](bm-20240504-pythonperf2-x86_64-faster%252dcpython-dynamic_underflow-3.13.0a6%2B-6f75dbe-vs-base.svg)

