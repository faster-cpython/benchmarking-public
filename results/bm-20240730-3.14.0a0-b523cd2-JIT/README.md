# Results

- fork: brandtbucher
- version: 3.14.0a0
- config: JIT
- commit hash: [b523cd2](https://github.com/brandtbucher/cpython/commit/b523cd2)
- commit date: 2024-07-30T18:38:55-07:00
- commit merge base: [7797182b78baf78f64fe16f436aa2279cf6afc23](https://github.com/brandtbucher/cpython/commit/7797182b78baf78f64fe16f436aa2279cf6afc23)
- ref: underflow

## linux x86_64 (azure)

- [pystats raw](bm-20240730-azure-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2-pystats.json)
- [pystats table](bm-20240730-azure-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2-pystats.md)

### vs. base

- [pystats diff](bm-20240730-azure-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10172689570)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2.json)

### vs. 3.10.4

- Geometric mean: 1.41x faster (HPT: reliability of 100.00%, 1.25x faster at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2-vs-3.10.4.md)
- [📈time plot](bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x faster (HPT: reliability of 99.50%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2-vs-3.12.0.md)
- [📈time plot](bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.00x faster (HPT: reliability of 70.22%, 1.00x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2-vs-3.13.0.md)
- [📈time plot](bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 99.23%, 1.00x slower at 99th %ile)
- Memory usage: 1.02x
- [🧠memory plot](bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2-vs-base-mem.svg)
- [📄table](bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2-vs-base.md)
- [📈time plot](bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2-vs-3.13.0b2.md)
- [📈time plot](bm-20240730-linux-x86_64-brandtbucher-underflow-3.14.0a0-b523cd2-vs-3.13.0b2.svg)

