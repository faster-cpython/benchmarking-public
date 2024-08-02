# Results

- fork: brandtbucher
- version: 3.14.0a0
- config: JIT
- commit hash: [ecb7974](https://github.com/brandtbucher/cpython/commit/ecb7974)
- commit date: 2024-06-07T15:43:17-07:00
- commit merge base: [e83ce850f433fd8bbf8ff4e8d7649b942639db31](https://github.com/brandtbucher/cpython/commit/e83ce850f433fd8bbf8ff4e8d7649b942639db31)
- ref: inline_class_call_de

## linux x86_64 (azure)

- [pystats raw](bm-20240607-azure-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-ecb7974-pystats.json)
- [pystats table](bm-20240607-azure-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-ecb7974-pystats.md)

### vs. base

- [pystats diff](bm-20240607-azure-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-ecb7974-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9423966742)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240607-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-ecb7974.json)

### vs. 3.10.4

- Geometric mean: 1.34x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240607-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-ecb7974-vs-3.10.4.md)
- [📈time plot](bm-20240607-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-ecb7974-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x faster (HPT: reliability of 96.91%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240607-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-ecb7974-vs-3.12.0.md)
- [📈time plot](bm-20240607-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-ecb7974-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.00x faster (HPT: reliability of 78.40%, 1.00x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, bpe_tokeniser, chameleon, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240607-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-ecb7974-vs-3.13.0b2.md)
- [📈time plot](bm-20240607-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-ecb7974-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 99.88%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240607-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-ecb7974-vs-base-mem.svg)
- [📄table](bm-20240607-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-ecb7974-vs-base.md)
- [📈time plot](bm-20240607-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-ecb7974-vs-base.svg)

