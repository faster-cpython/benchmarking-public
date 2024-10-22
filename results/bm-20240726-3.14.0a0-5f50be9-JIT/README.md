# Results

- fork: brandtbucher
- version: 3.14.0a0
- config: JIT
- commit hash: [5f50be9](https://github.com/brandtbucher/cpython/commit/5f50be9)
- commit date: 2024-07-26T10:35:51-07:00
- commit merge base: [5f6001130f8ada871193377954cfcfee01ef93b6](https://github.com/brandtbucher/cpython/commit/5f6001130f8ada871193377954cfcfee01ef93b6)
- ref: inline_class_call_de

## linux x86_64 (azure)

- [pystats raw](bm-20240726-azure-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9-pystats.json)
- [pystats table](bm-20240726-azure-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9-pystats.md)

### vs. base

- [pystats diff](bm-20240726-azure-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10115469504)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9.json)

### vs. 3.10.4

- Geometric mean: 1.42x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9-vs-3.10.4.md)
- [📈time plot](bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9-vs-3.12.0.md)
- [📈time plot](bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x faster (HPT: reliability of 65.43%, 1.00x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9-vs-3.13.0.md)
- [📈time plot](bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 99.88%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9-vs-base-mem.svg)
- [📄table](bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9-vs-base.md)
- [📈time plot](bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9-vs-3.13.0b2.md)
- [📈time plot](bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9-vs-3.13.0b2.svg)

