# Results

- fork: brandtbucher
- version: 3.14.0a0
- config: JIT
- commit hash: [994a9dc](https://github.com/brandtbucher/cpython/commit/994a9dc)
- commit date: 2024-05-22T15:59:51-04:00
- commit merge base: [d472b4f9fa4fb6061588d421f33a0388a2005bc6](https://github.com/brandtbucher/cpython/commit/d472b4f9fa4fb6061588d421f33a0388a2005bc6)
- ref: unbox_floats

## linux x86_64 (azure)

- [pystats raw](bm-20240522-azure-x86_64-brandtbucher-unbox_floats-3.14.0a0-994a9dc-pystats.json)
- [pystats table](bm-20240522-azure-x86_64-brandtbucher-unbox_floats-3.14.0a0-994a9dc-pystats.md)

### vs. base

- [pystats diff](bm-20240522-azure-x86_64-brandtbucher-unbox_floats-3.14.0a0-994a9dc-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9197624208)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240522-linux-x86_64-brandtbucher-unbox_floats-3.14.0a0-994a9dc.json)

### vs. 3.10.4

- Geometric mean: 1.33x faster (HPT: reliability of 100.00%, 1.22x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, djangocms, gunicorn, json, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, thrift, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240522-linux-x86_64-brandtbucher-unbox_floats-3.14.0a0-994a9dc-vs-3.10.4.md)
- [📈time plot](bm-20240522-linux-x86_64-brandtbucher-unbox_floats-3.14.0a0-994a9dc-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 92.68%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, gunicorn, json, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint
- [📄table](bm-20240522-linux-x86_64-brandtbucher-unbox_floats-3.14.0a0-994a9dc-vs-3.12.0.md)
- [📈time plot](bm-20240522-linux-x86_64-brandtbucher-unbox_floats-3.14.0a0-994a9dc-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.00x slower (HPT: reliability of 96.96%, 1.00x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, bpe_tokeniser, djangocms, gunicorn, json, mypy2, thrift
- [📄table](bm-20240522-linux-x86_64-brandtbucher-unbox_floats-3.14.0a0-994a9dc-vs-3.13.0b2.md)
- [📈time plot](bm-20240522-linux-x86_64-brandtbucher-unbox_floats-3.14.0a0-994a9dc-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 98.91%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: 🔴 json, thrift
- [🧠memory plot](bm-20240522-linux-x86_64-brandtbucher-unbox_floats-3.14.0a0-994a9dc-vs-base-mem.svg)
- [📄table](bm-20240522-linux-x86_64-brandtbucher-unbox_floats-3.14.0a0-994a9dc-vs-base.md)
- [📈time plot](bm-20240522-linux-x86_64-brandtbucher-unbox_floats-3.14.0a0-994a9dc-vs-base.svg)

