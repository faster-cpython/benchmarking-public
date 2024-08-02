# Results

- fork: brandtbucher
- version: 3.13.0a6+
- config: JIT
- commit hash: [345fc71](https://github.com/brandtbucher/cpython/commit/345fc71)
- commit date: 2024-05-04T09:38:17-07:00
- commit merge base: [f34e965e52b9bdf157b829371870edfde45b80bf](https://github.com/brandtbucher/cpython/commit/f34e965e52b9bdf157b829371870edfde45b80bf)
- ref: exits

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8951900451)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240504-linux-x86_64-brandtbucher-exits-3.13.0a6%2B-345fc71.json)

### vs. 3.10.4

- Geometric mean: 1.33x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: docutils, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240504-linux-x86_64-brandtbucher-exits-3.13.0a6%2B-345fc71-vs-3.10.4.md)
- [📈time plot](bm-20240504-linux-x86_64-brandtbucher-exits-3.13.0a6%2B-345fc71-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 92.96%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: docutils, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240504-linux-x86_64-brandtbucher-exits-3.13.0a6%2B-345fc71-vs-3.12.0.md)
- [📈time plot](bm-20240504-linux-x86_64-brandtbucher-exits-3.13.0a6%2B-345fc71-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.00x faster (HPT: reliability of 89.77%, 1.00x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: bpe_tokeniser, docutils
- [📄table](bm-20240504-linux-x86_64-brandtbucher-exits-3.13.0a6%2B-345fc71-vs-3.13.0b2.md)
- [📈time plot](bm-20240504-linux-x86_64-brandtbucher-exits-3.13.0a6%2B-345fc71-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 52.09%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240504-linux-x86_64-brandtbucher-exits-3.13.0a6%2B-345fc71-vs-base-mem.svg)
- [📄table](bm-20240504-linux-x86_64-brandtbucher-exits-3.13.0a6%2B-345fc71-vs-base.md)
- [📈time plot](bm-20240504-linux-x86_64-brandtbucher-exits-3.13.0a6%2B-345fc71-vs-base.svg)

