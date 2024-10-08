# Results

- fork: mdboom
- version: 3.12.0
- config: 
- commit hash: [c408bcb](https://github.com/mdboom/cpython/commit/c408bcb)
- commit date: 2024-09-03T12:47:07+02:00
- ref: cmq

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10941608962)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-193-generic-x86_64-with-glibc2.31
- [raw results](bm-20240903-linux-x86_64-mdboom-cmq-3.12.0-c408bcb.json)

### vs. 3.10.4

- Geometric mean: 1.30x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 0.67x
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240903-linux-x86_64-mdboom-cmq-3.12.0-c408bcb-vs-3.10.4.md)
- [📈time plot](bm-20240903-linux-x86_64-mdboom-cmq-3.12.0-c408bcb-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.00x faster (HPT: reliability of 80.59%, 1.00x faster at 99th %ile)
- Memory usage: 0.57x
- new benchmarks: bpe_tokeniser, djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240903-linux-x86_64-mdboom-cmq-3.12.0-c408bcb-vs-3.12.0.md)
- [📈time plot](bm-20240903-linux-x86_64-mdboom-cmq-3.12.0-c408bcb-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x slower (HPT: reliability of 96.35%, 1.00x slower at 99th %ile)
- Memory usage: 0.59x
- new benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- [📄table](bm-20240903-linux-x86_64-mdboom-cmq-3.12.0-c408bcb-vs-3.13.0b2.md)
- [📈time plot](bm-20240903-linux-x86_64-mdboom-cmq-3.12.0-c408bcb-vs-3.13.0b2.svg)

