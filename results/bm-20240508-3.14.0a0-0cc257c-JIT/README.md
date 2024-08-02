# Results

- fork: brandtbucher
- version: 3.14.0a0
- config: JIT
- commit hash: [0cc257c](https://github.com/brandtbucher/cpython/commit/0cc257c)
- commit date: 2024-05-08T12:31:45-07:00
- commit merge base: [7b0c247f1c176e092777fce4677a00f22c738b3c](https://github.com/brandtbucher/cpython/commit/7b0c247f1c176e092777fce4677a00f22c738b3c)
- ref: justin_recompile

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9009448216)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240508-linux-x86_64-brandtbucher-justin_recompile-3.14.0a0-0cc257c.json)

### vs. 3.10.4

- Geometric mean: 1.24x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: djangocms, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240508-linux-x86_64-brandtbucher-justin_recompile-3.14.0a0-0cc257c-vs-3.10.4.md)
- [📈time plot](bm-20240508-linux-x86_64-brandtbucher-justin_recompile-3.14.0a0-0cc257c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.05x slower (HPT: reliability of 99.24%, 1.00x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240508-linux-x86_64-brandtbucher-justin_recompile-3.14.0a0-0cc257c-vs-3.12.0.md)
- [📈time plot](bm-20240508-linux-x86_64-brandtbucher-justin_recompile-3.14.0a0-0cc257c-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.08x slower (HPT: reliability of 99.99%, 1.01x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: bpe_tokeniser, djangocms, mypy2
- [📄table](bm-20240508-linux-x86_64-brandtbucher-justin_recompile-3.14.0a0-0cc257c-vs-3.13.0b2.md)
- [📈time plot](bm-20240508-linux-x86_64-brandtbucher-justin_recompile-3.14.0a0-0cc257c-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.04x slower (HPT: reliability of 99.99%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240508-linux-x86_64-brandtbucher-justin_recompile-3.14.0a0-0cc257c-vs-base-mem.svg)
- [📄table](bm-20240508-linux-x86_64-brandtbucher-justin_recompile-3.14.0a0-0cc257c-vs-base.md)
- [📈time plot](bm-20240508-linux-x86_64-brandtbucher-justin_recompile-3.14.0a0-0cc257c-vs-base.svg)

