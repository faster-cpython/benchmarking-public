# Results

- fork: brandtbucher
- version: 3.14.0a0
- config: JIT
- commit hash: [d467f6c](https://github.com/brandtbucher/cpython/commit/d467f6c)
- commit date: 2024-09-04T19:11:46-07:00
- commit merge base: [5fce482c9a9d18d36c8177bdd0028cd2fef9f09f](https://github.com/brandtbucher/cpython/commit/5fce482c9a9d18d36c8177bdd0028cd2fef9f09f)
- ref: ujb0_project_confide

## linux x86_64 (azure)

- [pystats raw](bm-20240904-azure-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c-pystats.json)
- [pystats table](bm-20240904-azure-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c-pystats.md)

### vs. base

- [pystats diff](bm-20240904-azure-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10712649403)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-192-generic-x86_64-with-glibc2.31
- [raw results](bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c.json)

### vs. 3.10.4

- Geometric mean: 1.37x faster (HPT: reliability of 100.00%, 1.18x faster at 99th %ile)
- Memory usage: 1.36x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c-vs-3.10.4.md)
- [📈time plot](bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x faster (HPT: reliability of 93.85%, 1.00x faster at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c-vs-3.12.0.md)
- [📈time plot](bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.00x faster (HPT: reliability of 67.47%, 1.00x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c-vs-3.13.0b2.md)
- [📈time plot](bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.04x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 1.12x
- [🧠memory plot](bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c-vs-base-mem.svg)
- [📄table](bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c-vs-base.md)
- [📈time plot](bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c-vs-base.svg)

