# Results

- fork: brandtbucher
- version: 3.14.0a0
- config: JIT
- commit hash: [84bca09](https://github.com/brandtbucher/cpython/commit/84bca09)
- commit date: 2024-07-17T12:51:18-07:00
- commit merge base: [8b209fd4f8a9bf9603888bda2c44b5cfd4ebf47a](https://github.com/brandtbucher/cpython/commit/8b209fd4f8a9bf9603888bda2c44b5cfd4ebf47a)
- ref: tracing_jumps

## linux x86_64 (azure)

- [pystats raw](bm-20240717-azure-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09-pystats.json)
- [pystats table](bm-20240717-azure-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09-pystats.md)

### vs. base

- [pystats diff](bm-20240717-azure-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9981199927)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09.json)

### vs. 3.10.4

- Geometric mean: 1.42x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09-vs-3.10.4.md)
- [📈time plot](bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 99.90%, 1.01x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09-vs-3.12.0.md)
- [📈time plot](bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.04x faster (HPT: reliability of 99.93%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09-vs-3.13.0b2.md)
- [📈time plot](bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 55.29%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09-vs-base-mem.svg)
- [📄table](bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09-vs-base.md)
- [📈time plot](bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09-vs-base.svg)

