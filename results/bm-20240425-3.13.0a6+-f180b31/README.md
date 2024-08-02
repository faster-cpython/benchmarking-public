# Results

- fork: python
- version: 3.13.0a6+
- config: 
- commit hash: [f180b31](https://github.com/python/cpython/commit/f180b31)
- commit date: 2024-04-25T11:32:47+01:00
- commit merge base: [10bb90ed49a81a525b126ce8e4d8564c1616d0b3](https://github.com/python/cpython/commit/10bb90ed49a81a525b126ce8e4d8564c1616d0b3)
- ref: f180b31e7629d36265fa

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9273657041)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240425-linux-x86_64-python-f180b31e7629d36265fa-3.13.0a6%2B-f180b31.json)

### vs. 3.10.4

- Geometric mean: 1.33x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240425-linux-x86_64-python-f180b31e7629d36265fa-3.13.0a6%2B-f180b31-vs-3.10.4.md)
- [📈time plot](bm-20240425-linux-x86_64-python-f180b31e7629d36265fa-3.13.0a6%2B-f180b31-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x faster (HPT: reliability of 99.90%, 1.00x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240425-linux-x86_64-python-f180b31e7629d36265fa-3.13.0a6%2B-f180b31-vs-3.12.0.md)
- [📈time plot](bm-20240425-linux-x86_64-python-f180b31e7629d36265fa-3.13.0a6%2B-f180b31-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x faster (HPT: reliability of 99.83%, 1.00x faster at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: bpe_tokeniser
- [📄table](bm-20240425-linux-x86_64-python-f180b31e7629d36265fa-3.13.0a6%2B-f180b31-vs-3.13.0b2.md)
- [📈time plot](bm-20240425-linux-x86_64-python-f180b31e7629d36265fa-3.13.0a6%2B-f180b31-vs-3.13.0b2.svg)

