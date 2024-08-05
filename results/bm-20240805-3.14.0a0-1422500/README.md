# Results

- fork: python
- version: 3.14.0a0
- config: 
- commit hash: [1422500](https://github.com/python/cpython/commit/1422500)
- commit date: 2024-08-05T10:17:55+01:00
- commit merge base: [5207adf228547273b0e8d0253c23c69b95d7fe11](https://github.com/python/cpython/commit/5207adf228547273b0e8d0253c23c69b95d7fe11)
- ref: 1422500d020bd199b263

## linux x86_64 (azure)

- [pystats raw](bm-20240805-azure-x86_64-python-1422500d020bd199b263-3.14.0a0-1422500-pystats.json)
- [pystats table](bm-20240805-azure-x86_64-python-1422500d020bd199b263-3.14.0a0-1422500-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10246545320)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240805-linux-x86_64-python-1422500d020bd199b263-3.14.0a0-1422500.json)

### vs. 3.10.4

- Geometric mean: 1.43x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240805-linux-x86_64-python-1422500d020bd199b263-3.14.0a0-1422500-vs-3.10.4.md)
- [📈time plot](bm-20240805-linux-x86_64-python-1422500d020bd199b263-3.14.0a0-1422500-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.09x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240805-linux-x86_64-python-1422500d020bd199b263-3.14.0a0-1422500-vs-3.12.0.md)
- [📈time plot](bm-20240805-linux-x86_64-python-1422500d020bd199b263-3.14.0a0-1422500-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240805-linux-x86_64-python-1422500d020bd199b263-3.14.0a0-1422500-vs-3.13.0b2.md)
- [📈time plot](bm-20240805-linux-x86_64-python-1422500d020bd199b263-3.14.0a0-1422500-vs-3.13.0b2.svg)

