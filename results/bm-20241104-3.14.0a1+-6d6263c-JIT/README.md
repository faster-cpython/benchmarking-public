# Results

- fork: Fidget-Spinner/eliminate_func_guard
- version: 3.14.0a1+
- config: JIT
- commit hash: [6d6263c](https://github.com/Fidget%2dSpinner/cpython/commit/6d6263c)
- commit date: 2024-11-04T12:01:37+08:00
- commit merge base: [9441993f272f42e4a97d90616ec629a11c06aa3a](https://github.com/python/cpython/commit/9441993f272f42e4a97d90616ec629a11c06aa3a)
- ref: eliminate_func_guard

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11669925450)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20241104-linux-x86_64-Fidget%252dSpinner-eliminate_func_guard-3.14.0a1%2B-6d6263c.json)

### vs. 3.10.4

- Geometric mean: 1.382x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.33x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx
- [📄table](bm-20241104-linux-x86_64-Fidget%252dSpinner-eliminate_func_guard-3.14.0a1%2B-6d6263c-vs-3.10.4.md)
- [📈time plot](bm-20241104-linux-x86_64-Fidget%252dSpinner-eliminate_func_guard-3.14.0a1%2B-6d6263c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.057x faster (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift
- [📄table](bm-20241104-linux-x86_64-Fidget%252dSpinner-eliminate_func_guard-3.14.0a1%2B-6d6263c-vs-3.12.0.md)
- [📈time plot](bm-20241104-linux-x86_64-Fidget%252dSpinner-eliminate_func_guard-3.14.0a1%2B-6d6263c-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.006x slower (HPT: reliability of 84.99%, 1.00x slower at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: chameleon, djangocms, gevent_hub, gunicorn, many_optionals, subparsers
- [📄table](bm-20241104-linux-x86_64-Fidget%252dSpinner-eliminate_func_guard-3.14.0a1%2B-6d6263c-vs-3.13.0.md)
- [📈time plot](bm-20241104-linux-x86_64-Fidget%252dSpinner-eliminate_func_guard-3.14.0a1%2B-6d6263c-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.002x faster (HPT: reliability of 86.61%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241104-linux-x86_64-Fidget%252dSpinner-eliminate_func_guard-3.14.0a1%2B-6d6263c-vs-base-mem.svg)
- [📄table](bm-20241104-linux-x86_64-Fidget%252dSpinner-eliminate_func_guard-3.14.0a1%2B-6d6263c-vs-base.md)
- [📈time plot](bm-20241104-linux-x86_64-Fidget%252dSpinner-eliminate_func_guard-3.14.0a1%2B-6d6263c-vs-base.svg)

