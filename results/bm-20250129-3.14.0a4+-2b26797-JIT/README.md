# Results

- fork: Fidget-Spinner/py_likely_unlikely
- version: 3.14.0a4+
- config: JIT
- commit hash: [2b26797](https://github.com/Fidget%2dSpinner/cpython/commit/2b26797)
- commit date: 2025-01-29T01:22:46+08:00
- commit merge base: [5c9a63f62c9e56d1576c2dc62c986f2be988729f](https://github.com/python/cpython/commit/5c9a63f62c9e56d1576c2dc62c986f2be988729f)
- ref: py_likely_unlikely

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/13017883637)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20250129-linux-x86_64-Fidget%252dSpinner-py_likely_unlikely-3.14.0a4%2B-2b26797.json)

### vs. 3.10.4

- Geometric mean: 1.422x faster (HPT: reliability of 100.00%, 1.28x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers
- [📄table](bm-20250129-linux-x86_64-Fidget%252dSpinner-py_likely_unlikely-3.14.0a4%2B-2b26797-vs-3.10.4.md)
- [📈time plot](bm-20250129-linux-x86_64-Fidget%252dSpinner-py_likely_unlikely-3.14.0a4%2B-2b26797-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.098x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift
- [📄table](bm-20250129-linux-x86_64-Fidget%252dSpinner-py_likely_unlikely-3.14.0a4%2B-2b26797-vs-3.12.0.md)
- [📈time plot](bm-20250129-linux-x86_64-Fidget%252dSpinner-py_likely_unlikely-3.14.0a4%2B-2b26797-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.027x faster (HPT: reliability of 95.02%, 1.00x faster at 99th %ile)
- Memory usage: 1.04x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
- [📄table](bm-20250129-linux-x86_64-Fidget%252dSpinner-py_likely_unlikely-3.14.0a4%2B-2b26797-vs-3.13.0.md)
- [📈time plot](bm-20250129-linux-x86_64-Fidget%252dSpinner-py_likely_unlikely-3.14.0a4%2B-2b26797-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.008x slower (HPT: reliability of 99.87%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20250129-linux-x86_64-Fidget%252dSpinner-py_likely_unlikely-3.14.0a4%2B-2b26797-vs-base-mem.svg)
- [📄table](bm-20250129-linux-x86_64-Fidget%252dSpinner-py_likely_unlikely-3.14.0a4%2B-2b26797-vs-base.md)
- [📈time plot](bm-20250129-linux-x86_64-Fidget%252dSpinner-py_likely_unlikely-3.14.0a4%2B-2b26797-vs-base.svg)

