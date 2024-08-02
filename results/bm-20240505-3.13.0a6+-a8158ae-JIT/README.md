# Results

- fork: brandtbucher
- version: 3.13.0a6+
- config: JIT
- commit hash: [a8158ae](https://github.com/brandtbucher/cpython/commit/a8158ae)
- commit date: 2024-05-05T13:51:13-07:00
- commit merge base: [d8d94911e2393bd30ca58a32b33d792307fdc00d](https://github.com/brandtbucher/cpython/commit/d8d94911e2393bd30ca58a32b33d792307fdc00d)
- ref: dynamic_exit

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8961097755)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6%2B-a8158ae.json)

### vs. 3.10.4

- Geometric mean: 1.32x faster (HPT: reliability of 100.00%, 1.21x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: docutils, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6%2B-a8158ae-vs-3.10.4.md)
- [📈time plot](bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6%2B-a8158ae-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 95.60%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: docutils, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6%2B-a8158ae-vs-3.12.0.md)
- [📈time plot](bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6%2B-a8158ae-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x slower (HPT: reliability of 88.84%, 1.00x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: bpe_tokeniser, docutils
- [📄table](bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6%2B-a8158ae-vs-3.13.0b2.md)
- [📈time plot](bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6%2B-a8158ae-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 99.83%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6%2B-a8158ae-vs-base-mem.svg)
- [📄table](bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6%2B-a8158ae-vs-base.md)
- [📈time plot](bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6%2B-a8158ae-vs-base.svg)

