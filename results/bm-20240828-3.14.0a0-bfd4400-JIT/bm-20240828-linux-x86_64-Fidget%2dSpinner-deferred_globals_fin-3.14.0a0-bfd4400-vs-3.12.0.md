# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: deferred_globals_fin
- machine: linux-x86_64
- commit hash: bfd4400
- commit date: 2024-08-28
- overall geometric mean: 1.08x faster
- HPT reliability: 99.94%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 281 ms: 1.02x slower                                                            |
| docutils       | 2.77 sec                                               | 3.00 sec: 1.08x slower                                                          |
| tornado_http   | 103 ms                                                 | 93.0 ms: 1.10x faster                                                           |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 302 ms: 1.49x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 396 ms: 1.45x faster                                                            |
| async_tree_none            | 472 ms                                                 | 328 ms: 1.44x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 530 ms: 1.37x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 866 ms: 1.36x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 429 ms: 1.35x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 566 ms: 1.28x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 904 ms: 1.28x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.38x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 80.0 ms: 1.21x faster                                                           |
| float          | 84.7 ms                                                | 70.5 ms: 1.20x faster                                                           |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                  | 1.14x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 141 ms: 1.05x faster                                                            |
| regex_effbot   | 3.61 ms                                                | 3.50 ms: 1.03x faster                                                           |
| regex_dna      | 212 ms                                                 | 217 ms: 1.02x slower                                                            |
| regex_v8       | 23.1 ms                                                | 24.4 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                          |
| unpickle_pure_python | 230 us                                                 | 209 us: 1.10x faster                                                            |
| xml_etree_generate   | 89.2 ms                                                | 81.9 ms: 1.09x faster                                                           |
| xml_etree_iterparse  | 107 ms                                                 | 98.8 ms: 1.08x faster                                                           |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.07x faster                                                            |
| pickle_pure_python   | 324 us                                                 | 303 us: 1.07x faster                                                            |
| xml_etree_process    | 61.7 ms                                                | 57.7 ms: 1.07x faster                                                           |
| json_loads           | 28.5 us                                                | 28.7 us: 1.01x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                                    |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.15 ms: 1.03x slower                                                           |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.85 ms: 1.21x faster                                                           |
| django_template | 34.6 ms                                                | 35.7 ms: 1.03x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 26.5 us: 1.54x faster                                                           |
| async_tree_none_tg         | 450 ms                                                 | 302 ms: 1.49x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 396 ms: 1.45x faster                                                            |
| async_tree_none            | 472 ms                                                 | 328 ms: 1.44x faster                                                            |
| deepcopy                   | 371 us                                                 | 268 us: 1.39x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 530 ms: 1.37x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 866 ms: 1.36x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 429 ms: 1.35x faster                                                            |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                           |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 566 ms: 1.28x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 904 ms: 1.28x faster                                                            |
| crypto_pyaes               | 81.9 ms                                                | 65.5 ms: 1.25x faster                                                           |
| scimark_fft                | 382 ms                                                 | 306 ms: 1.25x faster                                                            |
| nbody                      | 97.0 ms                                                | 80.0 ms: 1.21x faster                                                           |
| deepcopy_reduce            | 3.35 us                                                | 2.77 us: 1.21x faster                                                           |
| mako                       | 11.9 ms                                                | 9.85 ms: 1.21x faster                                                           |
| tomli_loads                | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                          |
| scimark_monte_carlo        | 75.1 ms                                                | 62.4 ms: 1.20x faster                                                           |
| logging_format             | 7.23 us                                                | 6.02 us: 1.20x faster                                                           |
| float                      | 84.7 ms                                                | 70.5 ms: 1.20x faster                                                           |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.19x faster                                                           |
| deltablue                  | 3.72 ms                                                | 3.12 ms: 1.19x faster                                                           |
| raytrace                   | 312 ms                                                 | 263 ms: 1.19x faster                                                            |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.30 ms: 1.18x faster                                                           |
| richards                   | 45.8 ms                                                | 39.0 ms: 1.17x faster                                                           |
| logging_simple             | 6.46 us                                                | 5.51 us: 1.17x faster                                                           |
| spectral_norm              | 115 ms                                                 | 98.6 ms: 1.17x faster                                                           |
| richards_super             | 51.5 ms                                                | 44.3 ms: 1.16x faster                                                           |
| chaos                      | 67.0 ms                                                | 58.3 ms: 1.15x faster                                                           |
| scimark_sor                | 129 ms                                                 | 114 ms: 1.14x faster                                                            |
| fannkuch                   | 417 ms                                                 | 377 ms: 1.11x faster                                                            |
| tornado_http               | 103 ms                                                 | 93.0 ms: 1.10x faster                                                           |
| unpickle_pure_python       | 230 us                                                 | 209 us: 1.10x faster                                                            |
| xml_etree_generate         | 89.2 ms                                                | 81.9 ms: 1.09x faster                                                           |
| xml_etree_iterparse        | 107 ms                                                 | 98.8 ms: 1.08x faster                                                           |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.07x faster                                                            |
| pickle_pure_python         | 324 us                                                 | 303 us: 1.07x faster                                                            |
| xml_etree_process          | 61.7 ms                                                | 57.7 ms: 1.07x faster                                                           |
| pyflate                    | 482 ms                                                 | 456 ms: 1.06x faster                                                            |
| logging_silent             | 104 ns                                                 | 98.7 ns: 1.06x faster                                                           |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                            |
| scimark_lu                 | 118 ms                                                 | 112 ms: 1.06x faster                                                            |
| pprint_safe_repr           | 776 ms                                                 | 736 ms: 1.05x faster                                                            |
| regex_compile              | 148 ms                                                 | 141 ms: 1.05x faster                                                            |
| bench_thread_pool          | 842 us                                                 | 816 us: 1.03x faster                                                            |
| regex_effbot               | 3.61 ms                                                | 3.50 ms: 1.03x faster                                                           |
| sqlglot_parse              | 1.36 ms                                                | 1.32 ms: 1.03x faster                                                           |
| gc_traversal               | 3.79 ms                                                | 3.69 ms: 1.03x faster                                                           |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.03x faster                                                          |
| async_generators           | 463 ms                                                 | 452 ms: 1.03x faster                                                            |
| coroutines                 | 23.2 ms                                                | 22.9 ms: 1.01x faster                                                           |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                            |
| sqlglot_transpile          | 1.68 ms                                                | 1.68 ms: 1.00x faster                                                           |
| json_loads                 | 28.5 us                                                | 28.7 us: 1.01x slower                                                           |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                            |
| mdp                        | 2.63 sec                                               | 2.66 sec: 1.01x slower                                                          |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                          |
| sympy_str                  | 300 ms                                                 | 305 ms: 1.02x slower                                                            |
| asyncio_tcp                | 491 ms                                                 | 499 ms: 1.02x slower                                                            |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.02x slower                                                            |
| json                       | 5.26 ms                                                | 5.37 ms: 1.02x slower                                                           |
| regex_dna                  | 212 ms                                                 | 217 ms: 1.02x slower                                                            |
| 2to3                       | 274 ms                                                 | 281 ms: 1.02x slower                                                            |
| python_startup_no_site     | 6.94 ms                                                | 7.15 ms: 1.03x slower                                                           |
| django_template            | 34.6 ms                                                | 35.7 ms: 1.03x slower                                                           |
| nqueens                    | 83.3 ms                                                | 86.6 ms: 1.04x slower                                                           |
| go                         | 139 ms                                                 | 145 ms: 1.04x slower                                                            |
| sympy_sum                  | 169 ms                                                 | 176 ms: 1.04x slower                                                            |
| generators                 | 31.2 ms                                                | 32.8 ms: 1.05x slower                                                           |
| regex_v8                   | 23.1 ms                                                | 24.4 ms: 1.05x slower                                                           |
| hexiom                     | 6.41 ms                                                | 6.76 ms: 1.05x slower                                                           |
| sqlglot_optimize           | 54.8 ms                                                | 57.9 ms: 1.06x slower                                                           |
| sympy_integrate            | 21.4 ms                                                | 23.0 ms: 1.07x slower                                                           |
| sympy_expand               | 478 ms                                                 | 513 ms: 1.07x slower                                                            |
| docutils                   | 2.77 sec                                               | 3.00 sec: 1.08x slower                                                          |
| telco                      | 7.10 ms                                                | 7.77 ms: 1.09x slower                                                           |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                           |
| typing_runtime_protocols   | 158 us                                                 | 174 us: 1.10x slower                                                            |
| coverage                   | 72.7 ms                                                | 84.9 ms: 1.17x slower                                                           |
| create_gc_cycles           | 1.48 ms                                                | 1.76 ms: 1.19x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                                    |

Benchmark hidden because not significant (3): pprint_pformat, bench_mp_pool, json_dumps
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240828-3.14.0a0-bfd4400-JIT/bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.94% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.06x