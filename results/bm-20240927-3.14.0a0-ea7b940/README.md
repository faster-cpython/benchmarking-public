# Results

- fork: faster-cpython/experimental_gc_fix_
- version: 3.14.0a0
- config: 
- commit hash: [ea7b940](https://github.com/faster%2dcpython/cpython/commit/ea7b940)
- commit date: 2024-09-27T16:06:49-07:00
- commit merge base: [2c472d36b776636fb00881a717f69e43672588b1](https://github.com/python/cpython/commit/2c472d36b776636fb00881a717f69e43672588b1)
- ref: experimental_gc_fix_

## linux x86_64 (azure)

- [pystats raw](bm-20240927-azure-x86_64-faster%252dcpython-experimental_gc_fix_-3.14.0a0-ea7b940-pystats.json)
- [pystats table](bm-20240927-azure-x86_64-faster%252dcpython-experimental_gc_fix_-3.14.0a0-ea7b940-pystats.md)

### vs. base

- [pystats diff](bm-20240927-azure-x86_64-faster%252dcpython-experimental_gc_fix_-3.14.0a0-ea7b940-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11078839171)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-193-generic-x86_64-with-glibc2.31
- [raw results](bm-20240927-linux-x86_64-faster%252dcpython-experimental_gc_fix_-3.14.0a0-ea7b940.json)

### vs. 3.10.4

- Geometric mean: 1.422x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240927-linux-x86_64-faster%252dcpython-experimental_gc_fix_-3.14.0a0-ea7b940-vs-3.10.4.md)
- [📈time plot](bm-20240927-linux-x86_64-faster%252dcpython-experimental_gc_fix_-3.14.0a0-ea7b940-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.089x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 0.96x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240927-linux-x86_64-faster%252dcpython-experimental_gc_fix_-3.14.0a0-ea7b940-vs-3.12.0.md)
- [📈time plot](bm-20240927-linux-x86_64-faster%252dcpython-experimental_gc_fix_-3.14.0a0-ea7b940-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.034x faster (HPT: reliability of 98.52%, 1.00x faster at 99th %ile)
- Memory usage: 0.90x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240927-linux-x86_64-faster%252dcpython-experimental_gc_fix_-3.14.0a0-ea7b940-vs-3.13.0.md)
- [📈time plot](bm-20240927-linux-x86_64-faster%252dcpython-experimental_gc_fix_-3.14.0a0-ea7b940-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x faster (HPT: reliability of 93.98%, 1.00x slower at 99th %ile)
- Memory usage: 0.96x
- [🧠memory plot](bm-20240927-linux-x86_64-faster%252dcpython-experimental_gc_fix_-3.14.0a0-ea7b940-vs-base-mem.svg)
- [📄table](bm-20240927-linux-x86_64-faster%252dcpython-experimental_gc_fix_-3.14.0a0-ea7b940-vs-base.md)
- [📈time plot](bm-20240927-linux-x86_64-faster%252dcpython-experimental_gc_fix_-3.14.0a0-ea7b940-vs-base.svg)

