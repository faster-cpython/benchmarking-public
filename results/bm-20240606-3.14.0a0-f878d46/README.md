# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [f878d46](https://github.com/python/cpython/commit/f878d46)
- commit date: 2024-06-06T00:52:40+03:00
- commit merge base: [e83ce850f433fd8bbf8ff4e8d7649b942639db31](https://github.com/python/cpython/commit/e83ce850f433fd8bbf8ff4e8d7649b942639db31)
- ref: f878d46e5614f08a9302

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9415712555)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240606-linux-x86_64-python-f878d46e5614f08a9302-3.14.0a0-f878d46.json)

### vs. 3.10.4

- Geometric mean: 1.34x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240606-linux-x86_64-python-f878d46e5614f08a9302-3.14.0a0-f878d46-vs-3.10.4.md)
- [📈time plot](bm-20240606-linux-x86_64-python-f878d46e5614f08a9302-3.14.0a0-f878d46-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 99.97%, 1.00x faster at 99th %ile)
- Memory usage: 0.96x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240606-linux-x86_64-python-f878d46e5614f08a9302-3.14.0a0-f878d46-vs-3.12.0.md)
- [📈time plot](bm-20240606-linux-x86_64-python-f878d46e5614f08a9302-3.14.0a0-f878d46-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x faster (HPT: reliability of 99.87%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, bpe_tokeniser, chameleon, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240606-linux-x86_64-python-f878d46e5614f08a9302-3.14.0a0-f878d46-vs-3.13.0b2.md)
- [📈time plot](bm-20240606-linux-x86_64-python-f878d46e5614f08a9302-3.14.0a0-f878d46-vs-3.13.0b2.svg)

