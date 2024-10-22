# Results

- fork: brandtbucher
- version: 3.14.0a0
- config: JIT
- commit hash: [f135fa1](https://github.com/brandtbucher/cpython/commit/f135fa1)
- commit date: 2024-08-06T17:45:35-07:00
- commit merge base: [b5e142ba7c2063efe9bb8065c3b0bad33e2a9afa](https://github.com/brandtbucher/cpython/commit/b5e142ba7c2063efe9bb8065c3b0bad33e2a9afa)
- ref: tier_two_constants

## linux x86_64 (azure)

- [pystats raw](bm-20240806-azure-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1-pystats.json)
- [pystats table](bm-20240806-azure-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1-pystats.md)

### vs. base

- [pystats diff](bm-20240806-azure-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10276289512)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1.json)

### vs. 3.10.4

- Geometric mean: 1.43x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1-vs-3.10.4.md)
- [📈time plot](bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 99.99%, 1.03x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1-vs-3.12.0.md)
- [📈time plot](bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x faster (HPT: reliability of 83.55%, 1.00x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1-vs-3.13.0.md)
- [📈time plot](bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 99.09%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1-vs-base-mem.svg)
- [📄table](bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1-vs-base.md)
- [📈time plot](bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1-vs-3.13.0b2.md)
- [📈time plot](bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1-vs-3.13.0b2.svg)

