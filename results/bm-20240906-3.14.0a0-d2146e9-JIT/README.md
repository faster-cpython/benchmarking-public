# Results

- fork: brandtbucher
- version: 3.14.0a0
- config: JIT
- commit hash: [d2146e9](https://github.com/brandtbucher/cpython/commit/d2146e9)
- commit date: 2024-09-06T15:15:58-07:00
- commit merge base: [cfbc841ef3c27b3e65d1223bf8fedf1f652137bc](https://github.com/brandtbucher/cpython/commit/cfbc841ef3c27b3e65d1223bf8fedf1f652137bc)
- ref: confidence

## linux x86_64 (azure)

- [pystats raw](bm-20240906-azure-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9-pystats.json)
- [pystats table](bm-20240906-azure-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9-pystats.md)

### vs. base

- [pystats diff](bm-20240906-azure-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10745967527)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-193-generic-x86_64-with-glibc2.31
- [raw results](bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9.json)

### vs. 3.10.4

- Geometric mean: 1.38x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9-vs-3.10.4.md)
- [📈time plot](bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x faster (HPT: reliability of 99.99%, 1.02x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9-vs-3.12.0.md)
- [📈time plot](bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.00x faster (HPT: reliability of 88.31%, 1.00x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9-vs-3.13.0.md)
- [📈time plot](bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 71.90%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- new benchmarks: pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [🧠memory plot](bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9-vs-base-mem.svg)
- [📄table](bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9-vs-base.md)
- [📈time plot](bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9-vs-3.13.0b2.md)
- [📈time plot](bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9-vs-3.13.0b2.svg)

