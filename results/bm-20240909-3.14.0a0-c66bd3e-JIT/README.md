# Results

- fork: brandtbucher
- version: 3.14.0a0
- config: JIT
- commit hash: [c66bd3e](https://github.com/brandtbucher/cpython/commit/c66bd3e)
- commit date: 2024-09-09T17:31:41-07:00
- commit merge base: [5fce482c9a9d18d36c8177bdd0028cd2fef9f09f](https://github.com/brandtbucher/cpython/commit/5fce482c9a9d18d36c8177bdd0028cd2fef9f09f)
- ref: ujb0_project_warmup

## linux x86_64 (azure)

- [pystats raw](bm-20240909-azure-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e-pystats.json)
- [pystats table](bm-20240909-azure-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e-pystats.md)

### vs. base

- [pystats diff](bm-20240909-azure-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10783543606)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-193-generic-x86_64-with-glibc2.31
- [raw results](bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e.json)

### vs. 3.10.4

- Geometric mean: 1.32x faster (HPT: reliability of 100.00%, 1.19x faster at 99th %ile)
- Memory usage: 1.34x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e-vs-3.10.4.md)
- [📈time plot](bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 97.90%, 1.00x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e-vs-3.12.0.md)
- [📈time plot](bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.00x faster (HPT: reliability of 87.96%, 1.00x faster at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e-vs-3.13.0b2.md)
- [📈time plot](bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.04x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 1.09x
- new benchmarks: pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [🧠memory plot](bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e-vs-base-mem.svg)
- [📄table](bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e-vs-base.md)
- [📈time plot](bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-c66bd3e-vs-base.svg)

