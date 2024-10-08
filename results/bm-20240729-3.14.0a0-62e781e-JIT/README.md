# Results

- fork: brandtbucher
- version: 3.14.0a0
- config: JIT
- commit hash: [62e781e](https://github.com/brandtbucher/cpython/commit/62e781e)
- commit date: 2024-07-29T21:06:31-07:00
- commit merge base: [7797182b78baf78f64fe16f436aa2279cf6afc23](https://github.com/brandtbucher/cpython/commit/7797182b78baf78f64fe16f436aa2279cf6afc23)
- ref: no_progress_needed

## linux x86_64 (azure)

- [pystats raw](bm-20240729-azure-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e-pystats.json)
- [pystats table](bm-20240729-azure-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e-pystats.md)

### vs. base

- [pystats diff](bm-20240729-azure-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10155976234)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e.json)

### vs. 3.10.4

- Geometric mean: 1.42x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e-vs-3.10.4.md)
- [📈time plot](bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 99.86%, 1.01x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e-vs-3.12.0.md)
- [📈time plot](bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.04x faster (HPT: reliability of 99.88%, 1.00x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e-vs-3.13.0b2.md)
- [📈time plot](bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 98.66%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e-vs-base-mem.svg)
- [📄table](bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e-vs-base.md)
- [📈time plot](bm-20240729-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-62e781e-vs-base.svg)

