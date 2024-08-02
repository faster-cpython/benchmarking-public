# Results

- fork: Fidget-Spinner
- version: 3.14.0a0
- config: JIT
- commit hash: [3330a62](https://github.com/Fidget%2dSpinner/cpython/commit/3330a62)
- commit date: 2024-06-15T22:21:49+08:00
- commit merge base: [99d62f902e43c08ebec5a292fd3b30a9fc4cba69](https://github.com/Fidget%2dSpinner/cpython/commit/99d62f902e43c08ebec5a292fd3b30a9fc4cba69)
- ref: optimizer_constant_p

## linux x86_64 (azure)

- [pystats raw](bm-20240615-azure-x86_64-Fidget%252dSpinner-optimizer_constant_p-3.14.0a0-3330a62-pystats.json)
- [pystats table](bm-20240615-azure-x86_64-Fidget%252dSpinner-optimizer_constant_p-3.14.0a0-3330a62-pystats.md)

### vs. base

- [pystats diff](bm-20240615-azure-x86_64-Fidget%252dSpinner-optimizer_constant_p-3.14.0a0-3330a62-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9576601818)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240615-linux-x86_64-Fidget%252dSpinner-optimizer_constant_p-3.14.0a0-3330a62.json)

### vs. 3.10.4

- Geometric mean: 1.36x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240615-linux-x86_64-Fidget%252dSpinner-optimizer_constant_p-3.14.0a0-3330a62-vs-3.10.4.md)
- [📈time plot](bm-20240615-linux-x86_64-Fidget%252dSpinner-optimizer_constant_p-3.14.0a0-3330a62-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.05x faster (HPT: reliability of 96.63%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240615-linux-x86_64-Fidget%252dSpinner-optimizer_constant_p-3.14.0a0-3330a62-vs-3.12.0.md)
- [📈time plot](bm-20240615-linux-x86_64-Fidget%252dSpinner-optimizer_constant_p-3.14.0a0-3330a62-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x faster (HPT: reliability of 59.18%, 1.00x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240615-linux-x86_64-Fidget%252dSpinner-optimizer_constant_p-3.14.0a0-3330a62-vs-3.13.0b2.md)
- [📈time plot](bm-20240615-linux-x86_64-Fidget%252dSpinner-optimizer_constant_p-3.14.0a0-3330a62-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x faster (HPT: reliability of 85.04%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240615-linux-x86_64-Fidget%252dSpinner-optimizer_constant_p-3.14.0a0-3330a62-vs-base-mem.svg)
- [📄table](bm-20240615-linux-x86_64-Fidget%252dSpinner-optimizer_constant_p-3.14.0a0-3330a62-vs-base.md)
- [📈time plot](bm-20240615-linux-x86_64-Fidget%252dSpinner-optimizer_constant_p-3.14.0a0-3330a62-vs-base.svg)

