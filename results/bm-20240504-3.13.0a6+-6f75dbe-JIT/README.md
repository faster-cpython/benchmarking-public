# Results

- fork: faster-cpython
- version: 3.13.0a6+
- config: JIT
- commit hash: [6f75dbe](https://github.com/faster%2dcpython/cpython/commit/6f75dbe)
- commit date: 2024-05-04T12:15:01+01:00
- commit merge base: [b034f14a4b6e9197d3926046721b8b4b4b4f5b3d](https://github.com/faster%2dcpython/cpython/commit/b034f14a4b6e9197d3926046721b8b4b4b4f5b3d)
- ref: dynamic_underflow

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8950111256)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240504-linux-x86_64-faster%252dcpython-dynamic_underflow-3.13.0a6%2B-6f75dbe.json)

### vs. 3.10.4

- Geometric mean: 1.31x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: docutils, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240504-linux-x86_64-faster%252dcpython-dynamic_underflow-3.13.0a6%2B-6f75dbe-vs-3.10.4.md)
- [📈time plot](bm-20240504-linux-x86_64-faster%252dcpython-dynamic_underflow-3.13.0a6%2B-6f75dbe-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.02x faster (HPT: reliability of 86.98%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: docutils, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240504-linux-x86_64-faster%252dcpython-dynamic_underflow-3.13.0a6%2B-6f75dbe-vs-3.12.0.md)
- [📈time plot](bm-20240504-linux-x86_64-faster%252dcpython-dynamic_underflow-3.13.0a6%2B-6f75dbe-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x slower (HPT: reliability of 92.43%, 1.00x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: bpe_tokeniser, docutils
- [📄table](bm-20240504-linux-x86_64-faster%252dcpython-dynamic_underflow-3.13.0a6%2B-6f75dbe-vs-3.13.0b2.md)
- [📈time plot](bm-20240504-linux-x86_64-faster%252dcpython-dynamic_underflow-3.13.0a6%2B-6f75dbe-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 99.76%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20240504-linux-x86_64-faster%252dcpython-dynamic_underflow-3.13.0a6%2B-6f75dbe-vs-base-mem.svg)
- [📄table](bm-20240504-linux-x86_64-faster%252dcpython-dynamic_underflow-3.13.0a6%2B-6f75dbe-vs-base.md)
- [📈time plot](bm-20240504-linux-x86_64-faster%252dcpython-dynamic_underflow-3.13.0a6%2B-6f75dbe-vs-base.svg)

