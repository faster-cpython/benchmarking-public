# Results

- fork: brandtbucher
- version: 3.14.0a0
- config: JIT
- commit hash: [7c404a8](https://github.com/brandtbucher/cpython/commit/7c404a8)
- commit date: 2024-07-26T11:27:59-07:00
- commit merge base: [9ac606080a0074cdf7589d9b7c9413a73e0ddf37](https://github.com/brandtbucher/cpython/commit/9ac606080a0074cdf7589d9b7c9413a73e0ddf37)
- ref: tracing_jumps

## linux x86_64 (azure)

- [pystats raw](bm-20240726-azure-x86_64-brandtbucher-tracing_jumps-3.14.0a0-7c404a8-pystats.json)
- [pystats table](bm-20240726-azure-x86_64-brandtbucher-tracing_jumps-3.14.0a0-7c404a8-pystats.md)

### vs. base

- [pystats diff](bm-20240726-azure-x86_64-brandtbucher-tracing_jumps-3.14.0a0-7c404a8-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10115853984)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240726-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-7c404a8.json)

### vs. 3.10.4

- Geometric mean: 1.42x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240726-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-7c404a8-vs-3.10.4.md)
- [📈time plot](bm-20240726-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-7c404a8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240726-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-7c404a8-vs-3.12.0.md)
- [📈time plot](bm-20240726-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-7c404a8-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x faster (HPT: reliability of 64.28%, 1.00x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240726-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-7c404a8-vs-3.13.0.md)
- [📈time plot](bm-20240726-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-7c404a8-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 73.81%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20240726-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-7c404a8-vs-base-mem.svg)
- [📄table](bm-20240726-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-7c404a8-vs-base.md)
- [📈time plot](bm-20240726-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-7c404a8-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240726-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-7c404a8-vs-3.13.0b2.md)
- [📈time plot](bm-20240726-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-7c404a8-vs-3.13.0b2.svg)

