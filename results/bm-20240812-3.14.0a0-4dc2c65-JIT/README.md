# Results

- fork: brandtbucher
- version: 3.14.0a0
- config: JIT
- commit hash: [4dc2c65](https://github.com/brandtbucher/cpython/commit/4dc2c65)
- commit date: 2024-08-12T22:19:32-07:00
- commit merge base: [9621a7d0170bf1ec48bcfc35825007cdf75265ea](https://github.com/brandtbucher/cpython/commit/9621a7d0170bf1ec48bcfc35825007cdf75265ea)
- ref: underflow_static

## linux x86_64 (azure)

- [pystats raw](bm-20240812-azure-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65-pystats.json)
- [pystats table](bm-20240812-azure-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65-pystats.md)

### vs. base

- [pystats diff](bm-20240812-azure-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10364436719)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65.json)

### vs. 3.10.4

- Geometric mean: 1.41x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.23x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65-vs-3.10.4.md)
- [📈time plot](bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x faster (HPT: reliability of 99.62%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65-vs-3.12.0.md)
- [📈time plot](bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.00x slower (HPT: reliability of 72.85%, 1.00x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65-vs-3.13.0.md)
- [📈time plot](bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 93.64%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65-vs-base-mem.svg)
- [📄table](bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65-vs-base.md)
- [📈time plot](bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65-vs-3.13.0b2.md)
- [📈time plot](bm-20240812-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-4dc2c65-vs-3.13.0b2.svg)

