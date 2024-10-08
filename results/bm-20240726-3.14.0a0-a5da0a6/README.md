# Results

- fork: encukou
- version: 3.14.0a0
- config: 
- commit hash: [a5da0a6](https://github.com/encukou/cpython/commit/a5da0a6)
- commit date: 2024-07-26T11:41:40+02:00
- commit merge base: [d9efa45d7457b0dfea467bb1c2d22c69056ffc73](https://github.com/encukou/cpython/commit/d9efa45d7457b0dfea467bb1c2d22c69056ffc73)
- ref: intern_ūnus

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10117278718)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240726-linux-x86_64-encukou-intern_%C5%ABnus-3.14.0a0-a5da0a6.json)

### vs. 3.10.4

- Geometric mean: 1.43x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240726-linux-x86_64-encukou-intern_%C5%ABnus-3.14.0a0-a5da0a6-vs-3.10.4.md)
- [📈time plot](bm-20240726-linux-x86_64-encukou-intern_%C5%ABnus-3.14.0a0-a5da0a6-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240726-linux-x86_64-encukou-intern_%C5%ABnus-3.14.0a0-a5da0a6-vs-3.12.0.md)
- [📈time plot](bm-20240726-linux-x86_64-encukou-intern_%C5%ABnus-3.14.0a0-a5da0a6-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240726-linux-x86_64-encukou-intern_%C5%ABnus-3.14.0a0-a5da0a6-vs-3.13.0b2.md)
- [📈time plot](bm-20240726-linux-x86_64-encukou-intern_%C5%ABnus-3.14.0a0-a5da0a6-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 62.41%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20240726-linux-x86_64-encukou-intern_%C5%ABnus-3.14.0a0-a5da0a6-vs-base-mem.svg)
- [📄table](bm-20240726-linux-x86_64-encukou-intern_%C5%ABnus-3.14.0a0-a5da0a6-vs-base.md)
- [📈time plot](bm-20240726-linux-x86_64-encukou-intern_%C5%ABnus-3.14.0a0-a5da0a6-vs-base.svg)

