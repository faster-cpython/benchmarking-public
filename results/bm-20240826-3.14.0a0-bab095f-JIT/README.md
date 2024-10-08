# Results

- fork: brandtbucher
- version: 3.14.0a0
- config: JIT
- commit hash: [bab095f](https://github.com/brandtbucher/cpython/commit/bab095f)
- commit date: 2024-08-26T23:09:22-07:00
- commit merge base: [5fce482c9a9d18d36c8177bdd0028cd2fef9f09f](https://github.com/brandtbucher/cpython/commit/5fce482c9a9d18d36c8177bdd0028cd2fef9f09f)
- ref: underflow_static_no_

## linux x86_64 (azure)

- [pystats raw](bm-20240826-azure-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f-pystats.json)
- [pystats table](bm-20240826-azure-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f-pystats.md)

### vs. base

- [pystats diff](bm-20240826-azure-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10572674212)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-192-generic-x86_64-with-glibc2.31
- [raw results](bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f.json)

### vs. 3.10.4

- Geometric mean: 1.40x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.24x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f-vs-3.10.4.md)
- [📈time plot](bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.06x faster (HPT: reliability of 97.37%, 1.00x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f-vs-3.12.0.md)
- [📈time plot](bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x faster (HPT: reliability of 98.28%, 1.00x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f-vs-3.13.0b2.md)
- [📈time plot](bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.02x slower (HPT: reliability of 99.98%, 1.00x slower at 99th %ile)
- Memory usage: 1.03x
- [🧠memory plot](bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f-vs-base-mem.svg)
- [📄table](bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f-vs-base.md)
- [📈time plot](bm-20240826-linux-x86_64-brandtbucher-underflow_static_no_-3.14.0a0-bab095f-vs-base.svg)

