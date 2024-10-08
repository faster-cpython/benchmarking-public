# Results

- fork: brandtbucher
- version: 3.14.0a0
- config: JIT
- commit hash: [a4c1908](https://github.com/brandtbucher/cpython/commit/a4c1908)
- commit date: 2024-07-13T10:31:36-07:00
- commit merge base: [006b53a42f72be83ecdfc39f3603cdd66bfcdc45](https://github.com/brandtbucher/cpython/commit/006b53a42f72be83ecdfc39f3603cdd66bfcdc45)
- ref: no_progress_needed

## linux x86_64 (azure)

- [pystats raw](bm-20240713-azure-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908-pystats.json)
- [pystats table](bm-20240713-azure-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908-pystats.md)

### vs. base

- [pystats diff](bm-20240713-azure-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9921856614)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908.json)

### vs. 3.10.4

- Geometric mean: 1.43x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908-vs-3.10.4.md)
- [📈time plot](bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.09x faster (HPT: reliability of 99.99%, 1.02x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908-vs-3.12.0.md)
- [📈time plot](bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x faster (HPT: reliability of 99.94%, 1.01x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908-vs-3.13.0b2.md)
- [📈time plot](bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 98.69%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908-vs-base-mem.svg)
- [📄table](bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908-vs-base.md)
- [📈time plot](bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908-vs-base.svg)

