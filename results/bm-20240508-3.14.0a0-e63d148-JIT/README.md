# Results

- fork: brandtbucher
- version: 3.14.0a0
- config: JIT
- commit hash: [e63d148](https://github.com/brandtbucher/cpython/commit/e63d148)
- commit date: 2024-05-08T12:18:02-07:00
- commit merge base: [7b0c247f1c176e092777fce4677a00f22c738b3c](https://github.com/brandtbucher/cpython/commit/7b0c247f1c176e092777fce4677a00f22c738b3c)
- ref: justin_invalidate

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9007419889)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240508-linux-x86_64-brandtbucher-justin_invalidate-3.14.0a0-e63d148.json)

### vs. 3.10.4

- Geometric mean: 1.27x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 1.23x
- missing benchmarks: djangocms, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240508-linux-x86_64-brandtbucher-justin_invalidate-3.14.0a0-e63d148-vs-3.10.4.md)
- [📈time plot](bm-20240508-linux-x86_64-brandtbucher-justin_invalidate-3.14.0a0-e63d148-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.01x slower (HPT: reliability of 77.41%, 1.00x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240508-linux-x86_64-brandtbucher-justin_invalidate-3.14.0a0-e63d148-vs-3.12.0.md)
- [📈time plot](bm-20240508-linux-x86_64-brandtbucher-justin_invalidate-3.14.0a0-e63d148-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.04x slower (HPT: reliability of 97.98%, 1.00x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: bpe_tokeniser, djangocms, mypy2
- [📄table](bm-20240508-linux-x86_64-brandtbucher-justin_invalidate-3.14.0a0-e63d148-vs-3.13.0b2.md)
- [📈time plot](bm-20240508-linux-x86_64-brandtbucher-justin_invalidate-3.14.0a0-e63d148-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 99.53%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20240508-linux-x86_64-brandtbucher-justin_invalidate-3.14.0a0-e63d148-vs-base-mem.svg)
- [📄table](bm-20240508-linux-x86_64-brandtbucher-justin_invalidate-3.14.0a0-e63d148-vs-base.md)
- [📈time plot](bm-20240508-linux-x86_64-brandtbucher-justin_invalidate-3.14.0a0-e63d148-vs-base.svg)

