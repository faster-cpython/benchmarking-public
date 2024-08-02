# Results

- fork: faster-cpython
- version: 3.14.0a0
- config: 
- commit hash: [881df50](https://github.com/faster%2dcpython/cpython/commit/881df50)
- commit date: 2024-05-23T10:56:57+01:00
- commit merge base: [d472b4f9fa4fb6061588d421f33a0388a2005bc6](https://github.com/faster%2dcpython/cpython/commit/d472b4f9fa4fb6061588d421f33a0388a2005bc6)
- ref: specialize_binary_op

## linux x86_64 (azure)

- [pystats raw](bm-20240523-azure-x86_64-faster%252dcpython-specialize_binary_op-3.14.0a0-881df50-pystats.json)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9284542406)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240523-linux-x86_64-faster%252dcpython-specialize_binary_op-3.14.0a0-881df50.json)

### vs. 3.10.4

- Geometric mean: 1.34x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, djangocms, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240523-linux-x86_64-faster%252dcpython-specialize_binary_op-3.14.0a0-881df50-vs-3.10.4.md)
- [📈time plot](bm-20240523-linux-x86_64-faster%252dcpython-specialize_binary_op-3.14.0a0-881df50-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 99.92%, 1.00x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240523-linux-x86_64-faster%252dcpython-specialize_binary_op-3.14.0a0-881df50-vs-3.12.0.md)
- [📈time plot](bm-20240523-linux-x86_64-faster%252dcpython-specialize_binary_op-3.14.0a0-881df50-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.00x faster (HPT: reliability of 99.17%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, bpe_tokeniser, djangocms, gunicorn, mypy2
- [📄table](bm-20240523-linux-x86_64-faster%252dcpython-specialize_binary_op-3.14.0a0-881df50-vs-3.13.0b2.md)
- [📈time plot](bm-20240523-linux-x86_64-faster%252dcpython-specialize_binary_op-3.14.0a0-881df50-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 98.07%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240523-linux-x86_64-faster%252dcpython-specialize_binary_op-3.14.0a0-881df50-vs-base-mem.svg)
- [📄table](bm-20240523-linux-x86_64-faster%252dcpython-specialize_binary_op-3.14.0a0-881df50-vs-base.md)
- [📈time plot](bm-20240523-linux-x86_64-faster%252dcpython-specialize_binary_op-3.14.0a0-881df50-vs-base.svg)

