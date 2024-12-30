# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: init_slots
- machine: linux-x86_64
- commit hash: 8757207
- commit date: 2024-12-25
- overall geometric mean: 1.046x faster
- HPT reliability: 99.76%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241225-pythonperf2-x86_64-Fidget%2dSpinner-init_slots-3.14.0a3+-8757207 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 283 ms: 1.01x faster                                                         |
| docutils       | 2.87 sec                                                     | 2.89 sec: 1.01x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241225-pythonperf2-x86_64-Fidget%2dSpinner-init_slots-3.14.0a3+-8757207 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 625 ms: 1.69x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 326 ms: 1.66x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 635 ms: 1.64x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 265 ms: 1.63x faster                                                         |
| async_tree_none            | 452 ms                                                       | 286 ms: 1.58x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 349 ms: 1.56x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 492 ms: 1.42x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 509 ms: 1.37x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.56x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241225-pythonperf2-x86_64-Fidget%2dSpinner-init_slots-3.14.0a3+-8757207 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 70.7 ms: 1.08x faster                                                        |
| pidigits       | 265 ms                                                       | 252 ms: 1.05x faster                                                         |
| nbody          | 88.0 ms                                                      | 86.5 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241225-pythonperf2-x86_64-Fidget%2dSpinner-init_slots-3.14.0a3+-8757207 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.21 ms: 1.11x faster                                                        |
| regex_compile  | 144 ms                                                       | 137 ms: 1.05x faster                                                         |
| regex_dna      | 239 ms                                                       | 236 ms: 1.01x faster                                                         |
| regex_v8       | 23.6 ms                                                      | 25.9 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241225-pythonperf2-x86_64-Fidget%2dSpinner-init_slots-3.14.0a3+-8757207 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 95.6 ms: 1.08x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 136 ms: 1.06x faster                                                         |
| tomli_loads          | 2.16 sec                                                     | 2.05 sec: 1.05x faster                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 83.7 ms: 1.03x faster                                                        |
| unpickle_pure_python | 210 us                                                       | 205 us: 1.02x faster                                                         |
| json_loads           | 24.4 us                                                      | 24.0 us: 1.01x faster                                                        |
| xml_etree_process    | 58.4 ms                                                      | 59.5 ms: 1.02x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 326 us: 1.02x slower                                                         |
| json_dumps           | 10.2 ms                                                      | 11.3 ms: 1.11x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241225-pythonperf2-x86_64-Fidget%2dSpinner-init_slots-3.14.0a3+-8757207 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.04 ms: 1.05x slower                                                        |
| python_startup         | 11.6 ms                                                      | 16.1 ms: 1.39x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241225-pythonperf2-x86_64-Fidget%2dSpinner-init_slots-3.14.0a3+-8757207 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.6 ms: 1.07x faster                                                        |
| mako            | 10.0 ms                                                      | 11.0 ms: 1.10x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.01x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241225-pythonperf2-x86_64-Fidget%2dSpinner-init_slots-3.14.0a3+-8757207 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 625 ms: 1.69x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 326 ms: 1.66x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 635 ms: 1.64x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 265 ms: 1.63x faster                                                         |
| async_tree_none            | 452 ms                                                       | 286 ms: 1.58x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 349 ms: 1.56x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 492 ms: 1.42x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 509 ms: 1.37x faster                                                         |
| generators                 | 37.4 ms                                                      | 28.5 ms: 1.31x faster                                                        |
| deepcopy                   | 368 us                                                       | 284 us: 1.30x faster                                                         |
| comprehensions             | 21.9 us                                                      | 17.5 us: 1.25x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 30.4 us: 1.21x faster                                                        |
| go                         | 150 ms                                                       | 125 ms: 1.20x faster                                                         |
| deepcopy_reduce            | 3.37 us                                                      | 2.87 us: 1.18x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 16.1 ms: 1.17x faster                                                        |
| raytrace                   | 298 ms                                                       | 264 ms: 1.13x faster                                                         |
| regex_effbot               | 3.57 ms                                                      | 3.21 ms: 1.11x faster                                                        |
| sqlalchemy_declarative     | 159 ms                                                       | 144 ms: 1.11x faster                                                         |
| crypto_pyaes               | 80.3 ms                                                      | 72.8 ms: 1.10x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 62.6 ms: 1.10x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 20.9 ms: 1.10x faster                                                        |
| logging_format             | 7.48 us                                                      | 6.86 us: 1.09x faster                                                        |
| float                      | 76.6 ms                                                      | 70.7 ms: 1.08x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 95.6 ms: 1.08x faster                                                        |
| django_template            | 38.2 ms                                                      | 35.6 ms: 1.07x faster                                                        |
| sympy_sum                  | 162 ms                                                       | 152 ms: 1.06x faster                                                         |
| logging_simple             | 6.71 us                                                      | 6.31 us: 1.06x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 136 ms: 1.06x faster                                                         |
| pprint_pformat             | 1.65 sec                                                     | 1.57 sec: 1.05x faster                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.05 sec: 1.05x faster                                                       |
| regex_compile              | 144 ms                                                       | 137 ms: 1.05x faster                                                         |
| pidigits                   | 265 ms                                                       | 252 ms: 1.05x faster                                                         |
| pprint_safe_repr           | 807 ms                                                       | 771 ms: 1.05x faster                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                      | 17.9 ms: 1.05x faster                                                        |
| sympy_str                  | 302 ms                                                       | 291 ms: 1.04x faster                                                         |
| mdp                        | 2.57 sec                                                     | 2.48 sec: 1.04x faster                                                       |
| spectral_norm              | 91.6 ms                                                      | 88.5 ms: 1.04x faster                                                        |
| scimark_lu                 | 98.8 ms                                                      | 95.4 ms: 1.04x faster                                                        |
| sympy_integrate            | 23.9 ms                                                      | 23.2 ms: 1.03x faster                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.33 ms: 1.03x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 83.7 ms: 1.03x faster                                                        |
| chaos                      | 64.0 ms                                                      | 62.5 ms: 1.02x faster                                                        |
| unpickle_pure_python       | 210 us                                                       | 205 us: 1.02x faster                                                         |
| bench_thread_pool          | 950 us                                                       | 930 us: 1.02x faster                                                         |
| sqlglot_transpile          | 1.78 ms                                                      | 1.74 ms: 1.02x faster                                                        |
| meteor_contest             | 128 ms                                                       | 126 ms: 1.02x faster                                                         |
| nqueens                    | 89.9 ms                                                      | 88.2 ms: 1.02x faster                                                        |
| nbody                      | 88.0 ms                                                      | 86.5 ms: 1.02x faster                                                        |
| json_loads                 | 24.4 us                                                      | 24.0 us: 1.01x faster                                                        |
| regex_dna                  | 239 ms                                                       | 236 ms: 1.01x faster                                                         |
| 2to3                       | 285 ms                                                       | 283 ms: 1.01x faster                                                         |
| sqlglot_optimize           | 57.5 ms                                                      | 57.8 ms: 1.01x slower                                                        |
| richards_super             | 51.3 ms                                                      | 51.7 ms: 1.01x slower                                                        |
| docutils                   | 2.87 sec                                                     | 2.89 sec: 1.01x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 6.01 ms: 1.01x slower                                                        |
| json                       | 5.12 ms                                                      | 5.17 ms: 1.01x slower                                                        |
| xml_etree_process          | 58.4 ms                                                      | 59.5 ms: 1.02x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.26 sec: 1.02x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 326 us: 1.02x slower                                                         |
| sqlite_synth               | 2.77 us                                                      | 2.84 us: 1.02x slower                                                        |
| dulwich_log                | 65.4 ms                                                      | 67.1 ms: 1.03x slower                                                        |
| sympy_expand               | 484 ms                                                       | 498 ms: 1.03x slower                                                         |
| deltablue                  | 3.24 ms                                                      | 3.34 ms: 1.03x slower                                                        |
| scimark_fft                | 301 ms                                                       | 311 ms: 1.03x slower                                                         |
| pyflate                    | 439 ms                                                       | 454 ms: 1.04x slower                                                         |
| fannkuch                   | 350 ms                                                       | 364 ms: 1.04x slower                                                         |
| scimark_sor                | 109 ms                                                       | 113 ms: 1.04x slower                                                         |
| logging_silent             | 94.4 ns                                                      | 98.7 ns: 1.05x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 9.04 ms: 1.05x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 25.9 ms: 1.09x slower                                                        |
| async_generators           | 390 ms                                                       | 430 ms: 1.10x slower                                                         |
| mako                       | 10.0 ms                                                      | 11.0 ms: 1.10x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 11.3 ms: 1.11x slower                                                        |
| telco                      | 6.96 ms                                                      | 7.85 ms: 1.13x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 172 us: 1.14x slower                                                         |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.84 ms: 1.15x slower                                                        |
| coverage                   | 66.7 ms                                                      | 78.3 ms: 1.17x slower                                                        |
| mypy2                      | 830 ms                                                       | 1.02 sec: 1.23x slower                                                       |
| python_startup             | 11.6 ms                                                      | 16.1 ms: 1.39x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.78 ms: 1.75x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 6.58 ms: 1.89x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 1.44 sec: 301.45x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                                 |

Benchmark hidden because not significant (3): sqlglot_normalize, richards, asyncio_websockets
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241225-3.14.0a3+-8757207/bm-20241225-pythonperf2-x86_64-Fidget%2dSpinner-init_slots-3.14.0a3+-8757207.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.046x faster

# HPT report

- Reliability score: 99.76% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x