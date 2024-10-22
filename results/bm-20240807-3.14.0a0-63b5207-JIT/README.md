# Results

- fork: brandtbucher
- version: 3.14.0a0
- config: JIT
- commit hash: [63b5207](https://github.com/brandtbucher/cpython/commit/63b5207)
- commit date: 2024-08-07T19:30:49-07:00
- commit merge base: [b5e142ba7c2063efe9bb8065c3b0bad33e2a9afa](https://github.com/brandtbucher/cpython/commit/b5e142ba7c2063efe9bb8065c3b0bad33e2a9afa)
- ref: 63b52076b9636908a2cc

## linux x86_64 (azure)

- [pystats raw](bm-20240807-azure-x86_64-brandtbucher-63b52076b9636908a2cc-3.14.0a0-63b5207-pystats.json)
- [pystats table](bm-20240807-azure-x86_64-brandtbucher-63b52076b9636908a2cc-3.14.0a0-63b5207-pystats.md)

### vs. base

- [pystats diff](bm-20240807-azure-x86_64-brandtbucher-63b52076b9636908a2cc-3.14.0a0-63b5207-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10305213965)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240807-linux-x86_64-brandtbucher-63b52076b9636908a2cc-3.14.0a0-63b5207.json)

### vs. 3.10.4

- Geometric mean: 1.42x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240807-linux-x86_64-brandtbucher-63b52076b9636908a2cc-3.14.0a0-63b5207-vs-3.10.4.md)
- [📈time plot](bm-20240807-linux-x86_64-brandtbucher-63b52076b9636908a2cc-3.14.0a0-63b5207-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 99.92%, 1.01x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240807-linux-x86_64-brandtbucher-63b52076b9636908a2cc-3.14.0a0-63b5207-vs-3.12.0.md)
- [📈time plot](bm-20240807-linux-x86_64-brandtbucher-63b52076b9636908a2cc-3.14.0a0-63b5207-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x faster (HPT: reliability of 70.55%, 1.00x faster at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240807-linux-x86_64-brandtbucher-63b52076b9636908a2cc-3.14.0a0-63b5207-vs-3.13.0.md)
- [📈time plot](bm-20240807-linux-x86_64-brandtbucher-63b52076b9636908a2cc-3.14.0a0-63b5207-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 99.77%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20240807-linux-x86_64-brandtbucher-63b52076b9636908a2cc-3.14.0a0-63b5207-vs-base-mem.svg)
- [📄table](bm-20240807-linux-x86_64-brandtbucher-63b52076b9636908a2cc-3.14.0a0-63b5207-vs-base.md)
- [📈time plot](bm-20240807-linux-x86_64-brandtbucher-63b52076b9636908a2cc-3.14.0a0-63b5207-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240807-linux-x86_64-brandtbucher-63b52076b9636908a2cc-3.14.0a0-63b5207-vs-3.13.0b2.md)
- [📈time plot](bm-20240807-linux-x86_64-brandtbucher-63b52076b9636908a2cc-3.14.0a0-63b5207-vs-3.13.0b2.svg)

