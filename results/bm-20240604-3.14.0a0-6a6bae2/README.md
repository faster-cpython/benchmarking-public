# Results

- fork: Fidget-Spinner
- version: 3.14.0a0
- config: 
- commit hash: [6a6bae2](https://github.com/Fidget%2dSpinner/cpython/commit/6a6bae2)
- commit date: 2024-06-04T21:20:18+08:00
- commit merge base: [31a4fb3c74a0284436343858803b54471e2dc9c7](https://github.com/Fidget%2dSpinner/cpython/commit/31a4fb3c74a0284436343858803b54471e2dc9c7)
- ref: stackref_all

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9368053695)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240604-linux-x86_64-Fidget%252dSpinner-stackref_all-3.14.0a0-6a6bae2.json)

### vs. 3.10.4

- Geometric mean: 1.34x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240604-linux-x86_64-Fidget%252dSpinner-stackref_all-3.14.0a0-6a6bae2-vs-3.10.4.md)
- [📈time plot](bm-20240604-linux-x86_64-Fidget%252dSpinner-stackref_all-3.14.0a0-6a6bae2-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x faster (HPT: reliability of 99.98%, 1.01x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240604-linux-x86_64-Fidget%252dSpinner-stackref_all-3.14.0a0-6a6bae2-vs-3.12.0.md)
- [📈time plot](bm-20240604-linux-x86_64-Fidget%252dSpinner-stackref_all-3.14.0a0-6a6bae2-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, bpe_tokeniser, chameleon, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240604-linux-x86_64-Fidget%252dSpinner-stackref_all-3.14.0a0-6a6bae2-vs-3.13.0b2.md)
- [📈time plot](bm-20240604-linux-x86_64-Fidget%252dSpinner-stackref_all-3.14.0a0-6a6bae2-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 90.27%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240604-linux-x86_64-Fidget%252dSpinner-stackref_all-3.14.0a0-6a6bae2-vs-base-mem.svg)
- [📄table](bm-20240604-linux-x86_64-Fidget%252dSpinner-stackref_all-3.14.0a0-6a6bae2-vs-base.md)
- [📈time plot](bm-20240604-linux-x86_64-Fidget%252dSpinner-stackref_all-3.14.0a0-6a6bae2-vs-base.svg)

