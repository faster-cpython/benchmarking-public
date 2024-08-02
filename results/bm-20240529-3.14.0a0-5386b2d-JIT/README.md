# Results

- fork: faster-cpython
- version: 3.14.0a0
- config: JIT
- commit hash: [5386b2d](https://github.com/faster%2dcpython/cpython/commit/5386b2d)
- commit date: 2024-05-29T16:01:19+01:00
- commit merge base: [1f481fd3275dbc12a88c16129621de19ea20e4ca](https://github.com/faster%2dcpython/cpython/commit/1f481fd3275dbc12a88c16129621de19ea20e4ca)
- ref: specialize_binary_op

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9404548675)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240529-linux-x86_64-faster%252dcpython-specialize_binary_op-3.14.0a0-5386b2d.json)

### vs. 3.10.4

- Geometric mean: 1.34x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240529-linux-x86_64-faster%252dcpython-specialize_binary_op-3.14.0a0-5386b2d-vs-3.10.4.md)
- [📈time plot](bm-20240529-linux-x86_64-faster%252dcpython-specialize_binary_op-3.14.0a0-5386b2d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 91.82%, 1.00x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240529-linux-x86_64-faster%252dcpython-specialize_binary_op-3.14.0a0-5386b2d-vs-3.12.0.md)
- [📈time plot](bm-20240529-linux-x86_64-faster%252dcpython-specialize_binary_op-3.14.0a0-5386b2d-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.00x faster (HPT: reliability of 68.26%, 1.00x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, bpe_tokeniser, chameleon, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240529-linux-x86_64-faster%252dcpython-specialize_binary_op-3.14.0a0-5386b2d-vs-3.13.0b2.md)
- [📈time plot](bm-20240529-linux-x86_64-faster%252dcpython-specialize_binary_op-3.14.0a0-5386b2d-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 56.05%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- new benchmarks: docutils
- [🧠memory plot](bm-20240529-linux-x86_64-faster%252dcpython-specialize_binary_op-3.14.0a0-5386b2d-vs-base-mem.svg)
- [📄table](bm-20240529-linux-x86_64-faster%252dcpython-specialize_binary_op-3.14.0a0-5386b2d-vs-base.md)
- [📈time plot](bm-20240529-linux-x86_64-faster%252dcpython-specialize_binary_op-3.14.0a0-5386b2d-vs-base.svg)

