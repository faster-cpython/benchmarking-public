# Results

- fork: Fidget-Spinner
- version: 3.14.0a0
- config: NOGIL
- commit hash: [6a6bae2](https://github.com/Fidget%2dSpinner/cpython/commit/6a6bae2)
- commit date: 2024-06-04T21:20:18+08:00
- commit merge base: [31a4fb3c74a0284436343858803b54471e2dc9c7](https://github.com/Fidget%2dSpinner/cpython/commit/31a4fb3c74a0284436343858803b54471e2dc9c7)
- ref: stackref_all

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9380328408)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240604-linux-x86_64-Fidget%252dSpinner-stackref_all-3.14.0a0-6a6bae2.json)

### vs. 3.10.4

- Geometric mean: 1.15x slower (HPT: reliability of 100.00%, 1.05x slower at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240604-linux-x86_64-Fidget%252dSpinner-stackref_all-3.14.0a0-6a6bae2-vs-3.10.4.md)
- [📈time plot](bm-20240604-linux-x86_64-Fidget%252dSpinner-stackref_all-3.14.0a0-6a6bae2-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.43x slower (HPT: reliability of 100.00%, 1.26x slower at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240604-linux-x86_64-Fidget%252dSpinner-stackref_all-3.14.0a0-6a6bae2-vs-3.12.0.md)
- [📈time plot](bm-20240604-linux-x86_64-Fidget%252dSpinner-stackref_all-3.14.0a0-6a6bae2-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.51x slower (HPT: reliability of 100.00%, 1.31x slower at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, bpe_tokeniser, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240604-linux-x86_64-Fidget%252dSpinner-stackref_all-3.14.0a0-6a6bae2-vs-3.13.0b2.md)
- [📈time plot](bm-20240604-linux-x86_64-Fidget%252dSpinner-stackref_all-3.14.0a0-6a6bae2-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.05x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20240604-linux-x86_64-Fidget%252dSpinner-stackref_all-3.14.0a0-6a6bae2-vs-base-mem.svg)
- [📄table](bm-20240604-linux-x86_64-Fidget%252dSpinner-stackref_all-3.14.0a0-6a6bae2-vs-base.md)
- [📈time plot](bm-20240604-linux-x86_64-Fidget%252dSpinner-stackref_all-3.14.0a0-6a6bae2-vs-base.svg)

