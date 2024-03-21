# Results

- fork: python
- version: 3.13.0a5+
- tier 2: False
- jit: False
- commit hash: [6547330](https://github.com/python/cpython/commit/6547330)
- commit date: 2024-03-21T03:49:10+00:00
- commit merge base: [667294d5b2ee812ebe0c9c1efd58e2006b61f827](https://github.com/python/cpython/commit/667294d5b2ee812ebe0c9c1efd58e2006b61f827)
- ref: 6547330f4e896c6748da

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8376571327)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240321-linux-x86_64-python-6547330f4e896c6748da-3.13.0a5%2B-6547330.json)

### vs. 3.10.4

- Geometric mean: 1.16x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240321-linux-x86_64-python-6547330f4e896c6748da-3.13.0a5%2B-6547330-vs-3.10.4.md)
- [📈time plot](bm-20240321-linux-x86_64-python-6547330f4e896c6748da-3.13.0a5%2B-6547330-vs-3.10.4.png)

### vs. 3.11.0

- Geometric mean: 1.19x slower (HPT: reliability of 98.55%, 1.00x slower at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
- [📄table](bm-20240321-linux-x86_64-python-6547330f4e896c6748da-3.13.0a5%2B-6547330-vs-3.11.0.md)
- [📈time plot](bm-20240321-linux-x86_64-python-6547330f4e896c6748da-3.13.0a5%2B-6547330-vs-3.11.0.png)

### vs. 3.12.0

- Geometric mean: 1.21x slower (HPT: reliability of 88.75%, 1.00x slower at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: djangocms, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240321-linux-x86_64-python-6547330f4e896c6748da-3.13.0a5%2B-6547330-vs-3.12.0.md)
- [📈time plot](bm-20240321-linux-x86_64-python-6547330f4e896c6748da-3.13.0a5%2B-6547330-vs-3.12.0.png)

