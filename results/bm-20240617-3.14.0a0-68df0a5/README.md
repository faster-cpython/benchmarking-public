# Results

- fork: faster-cpython
- version: 3.14.0a0
- config: 
- commit hash: [68df0a5](https://github.com/faster%2dcpython/cpython/commit/68df0a5)
- commit date: 2024-06-17T09:28:13+01:00
- commit merge base: [3df2022931f77c5cadb3f51b371be6ae17587ede](https://github.com/faster%2dcpython/cpython/commit/3df2022931f77c5cadb3f51b371be6ae17587ede)
- ref: lower_before

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9544495349)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240617-linux-x86_64-faster%252dcpython-lower_before-3.14.0a0-68df0a5.json)

### vs. 3.10.4

- Geometric mean: 1.35x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240617-linux-x86_64-faster%252dcpython-lower_before-3.14.0a0-68df0a5-vs-3.10.4.md)
- [📈time plot](bm-20240617-linux-x86_64-faster%252dcpython-lower_before-3.14.0a0-68df0a5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x faster (HPT: reliability of 99.98%, 1.00x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240617-linux-x86_64-faster%252dcpython-lower_before-3.14.0a0-68df0a5-vs-3.12.0.md)
- [📈time plot](bm-20240617-linux-x86_64-faster%252dcpython-lower_before-3.14.0a0-68df0a5-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240617-linux-x86_64-faster%252dcpython-lower_before-3.14.0a0-68df0a5-vs-3.13.0b2.md)
- [📈time plot](bm-20240617-linux-x86_64-faster%252dcpython-lower_before-3.14.0a0-68df0a5-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 65.19%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240617-linux-x86_64-faster%252dcpython-lower_before-3.14.0a0-68df0a5-vs-base-mem.svg)
- [📄table](bm-20240617-linux-x86_64-faster%252dcpython-lower_before-3.14.0a0-68df0a5-vs-base.md)
- [📈time plot](bm-20240617-linux-x86_64-faster%252dcpython-lower_before-3.14.0a0-68df0a5-vs-base.svg)

