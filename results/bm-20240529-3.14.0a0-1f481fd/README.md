# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [1f481fd](https://github.com/python/cpython/commit/1f481fd)
- commit date: 2024-05-29T12:44:09+00:00
- commit merge base: [055c739536ad63b55ad7cd0b91ccacc33064fe11](https://github.com/python/cpython/commit/055c739536ad63b55ad7cd0b91ccacc33064fe11)
- ref: 1f481fd3275dbc12a88c

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9305462175)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240529-linux-x86_64-python-1f481fd3275dbc12a88c-3.14.0a0-1f481fd.json)

### vs. 3.10.4

- Geometric mean: 1.34x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240529-linux-x86_64-python-1f481fd3275dbc12a88c-3.14.0a0-1f481fd-vs-3.10.4.md)
- [📈time plot](bm-20240529-linux-x86_64-python-1f481fd3275dbc12a88c-3.14.0a0-1f481fd-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 99.98%, 1.00x faster at 99th %ile)
- Memory usage: 0.96x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240529-linux-x86_64-python-1f481fd3275dbc12a88c-3.14.0a0-1f481fd-vs-3.12.0.md)
- [📈time plot](bm-20240529-linux-x86_64-python-1f481fd3275dbc12a88c-3.14.0a0-1f481fd-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x faster (HPT: reliability of 99.99%, 1.00x faster at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: aiohttp, bpe_tokeniser, chameleon, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240529-linux-x86_64-python-1f481fd3275dbc12a88c-3.14.0a0-1f481fd-vs-3.13.0b2.md)
- [📈time plot](bm-20240529-linux-x86_64-python-1f481fd3275dbc12a88c-3.14.0a0-1f481fd-vs-3.13.0b2.svg)

