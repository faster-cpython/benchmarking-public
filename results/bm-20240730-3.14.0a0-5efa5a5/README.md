# Results

- fork: serhiy-storchaka
- version: 3.14.0a0
- config: 
- commit hash: [5efa5a5](https://github.com/serhiy%2dstorchaka/cpython/commit/5efa5a5)
- commit date: 2024-07-30T15:58:01+03:00
- commit merge base: [d1a1bca1f0550a4715f1bf32b1586caa7bc4487b](https://github.com/serhiy%2dstorchaka/cpython/commit/d1a1bca1f0550a4715f1bf32b1586caa7bc4487b)
- ref: pickle_save_global3

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10180691537)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240730-linux-x86_64-serhiy%252dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5.json)

### vs. 3.10.4

- Geometric mean: 1.43x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240730-linux-x86_64-serhiy%252dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5-vs-3.10.4.md)
- [📈time plot](bm-20240730-linux-x86_64-serhiy%252dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240730-linux-x86_64-serhiy%252dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5-vs-3.12.0.md)
- [📈time plot](bm-20240730-linux-x86_64-serhiy%252dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.02x faster (HPT: reliability of 88.99%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240730-linux-x86_64-serhiy%252dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5-vs-3.13.0.md)
- [📈time plot](bm-20240730-linux-x86_64-serhiy%252dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 99.99%, 1.00x slower at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: 🔴 dask
- [🧠memory plot](bm-20240730-linux-x86_64-serhiy%252dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5-vs-base-mem.svg)
- [📄table](bm-20240730-linux-x86_64-serhiy%252dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5-vs-base.md)
- [📈time plot](bm-20240730-linux-x86_64-serhiy%252dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240730-linux-x86_64-serhiy%252dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5-vs-3.13.0b2.md)
- [📈time plot](bm-20240730-linux-x86_64-serhiy%252dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5-vs-3.13.0b2.svg)

