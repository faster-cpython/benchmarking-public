# Results

- fork: Fidget-Spinner
- version: 3.14.0a0
- config: JIT
- commit hash: [aaab6a6](https://github.com/Fidget%2dSpinner/cpython/commit/aaab6a6)
- commit date: 2024-09-20T03:24:44+08:00
- commit merge base: [401fff7423ca3c8bf1d02e594edfd1412616a559](https://github.com/Fidget%2dSpinner/cpython/commit/401fff7423ca3c8bf1d02e594edfd1412616a559)
- ref: partial_evaluator_un

## linux x86_64 (azure)

- [pystats raw](bm-20240920-azure-x86_64-Fidget%252dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6-pystats.json)
- [pystats table](bm-20240920-azure-x86_64-Fidget%252dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6-pystats.md)

### vs. base

- [pystats diff](bm-20240920-azure-x86_64-Fidget%252dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10950443606)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-193-generic-x86_64-with-glibc2.31
- [raw results](bm-20240920-linux-x86_64-Fidget%252dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6.json)

### vs. 3.10.4

- Geometric mean: 1.422x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.84x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240920-linux-x86_64-Fidget%252dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6-vs-3.10.4.md)
- [📈time plot](bm-20240920-linux-x86_64-Fidget%252dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.087x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 1.68x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240920-linux-x86_64-Fidget%252dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6-vs-3.12.0.md)
- [📈time plot](bm-20240920-linux-x86_64-Fidget%252dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.028x faster (HPT: reliability of 84.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.49x
- missing benchmarks: chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, many_optionals, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, subparsers
- new benchmarks: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240920-linux-x86_64-Fidget%252dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6-vs-3.13.0.md)
- [📈time plot](bm-20240920-linux-x86_64-Fidget%252dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.003x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.53x
- [🧠memory plot](bm-20240920-linux-x86_64-Fidget%252dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6-vs-base-mem.svg)
- [📄table](bm-20240920-linux-x86_64-Fidget%252dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6-vs-base.md)
- [📈time plot](bm-20240920-linux-x86_64-Fidget%252dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6-vs-base.svg)

