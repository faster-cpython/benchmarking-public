# Results

- fork: savannahostrowski
- version: 3.14.0a0
- config: JIT
- commit hash: [985d4c1](https://github.com/savannahostrowski/cpython/commit/985d4c1)
- commit date: 2024-08-19T20:20:52-07:00
- commit merge base: [e913d2c87f1ae4e7a4aef5ba78368ef31d060767](https://github.com/savannahostrowski/cpython/commit/e913d2c87f1ae4e7a4aef5ba78368ef31d060767)
- ref: jit_mem_gc_increment

## linux x86_64 (azure)

- [pystats raw](bm-20240819-azure-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1-pystats.json)
- [pystats table](bm-20240819-azure-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1-pystats.md)

### vs. base

- [pystats diff](bm-20240819-azure-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10475776139)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-192-generic-x86_64-with-glibc2.31
- [raw results](bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1.json)

### vs. 3.10.4

- Geometric mean: 1.42x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.18x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1-vs-3.10.4.md)
- [📈time plot](bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 99.63%, 1.00x faster at 99th %ile)
- Memory usage: 1.03x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1-vs-3.12.0.md)
- [📈time plot](bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.04x faster (HPT: reliability of 99.95%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1-vs-3.13.0b2.md)
- [📈time plot](bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 82.08%, 1.00x slower at 99th %ile)
- Memory usage: 0.98x
- [🧠memory plot](bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1-vs-base-mem.svg)
- [📄table](bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1-vs-base.md)
- [📈time plot](bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1-vs-base.svg)

