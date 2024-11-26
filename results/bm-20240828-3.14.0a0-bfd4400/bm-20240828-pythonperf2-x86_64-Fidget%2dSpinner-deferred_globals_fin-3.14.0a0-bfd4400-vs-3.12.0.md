# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: deferred_globals_fin
- machine: linux-x86_64
- commit hash: bfd4400
- commit date: 2024-08-28
- overall geometric mean: 1.029x faster
- HPT reliability: 86.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 287 ms: 1.01x slower                                                                  |
| docutils       | 2.87 sec                                                     | 2.97 sec: 1.04x slower                                                                |
| tornado_http   | 121 ms                                                       | 116 ms: 1.04x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 300 ms: 1.44x faster                                                                  |
| async_tree_memoization_tg  | 540 ms                                                       | 380 ms: 1.42x faster                                                                  |
| async_tree_io_tg           | 1.05 sec                                                     | 771 ms: 1.37x faster                                                                  |
| async_tree_none            | 452 ms                                                       | 332 ms: 1.36x faster                                                                  |
| async_tree_memoization     | 544 ms                                                       | 401 ms: 1.35x faster                                                                  |
| async_tree_io              | 1.04 sec                                                     | 804 ms: 1.30x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 539 ms: 1.29x faster                                                                  |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 574 ms: 1.21x faster                                                                  |
| Geometric mean             | (ref)                                                        | 1.34x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                                                  |
| float          | 76.6 ms                                                      | 82.4 ms: 1.07x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 139 ms: 1.04x faster                                                                  |
| regex_effbot   | 3.57 ms                                                      | 3.46 ms: 1.03x faster                                                                 |
| regex_dna      | 239 ms                                                       | 234 ms: 1.02x faster                                                                  |
| regex_v8       | 23.6 ms                                                      | 25.4 ms: 1.08x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| pickle_pure_python   | 318 us                                                       | 311 us: 1.02x faster                                                                  |
| xml_etree_generate   | 86.1 ms                                                      | 84.6 ms: 1.02x faster                                                                 |
| xml_etree_iterparse  | 103 ms                                                       | 101 ms: 1.02x faster                                                                  |
| unpickle_pure_python | 210 us                                                       | 211 us: 1.01x slower                                                                  |
| xml_etree_process    | 58.4 ms                                                      | 59.1 ms: 1.01x slower                                                                 |
| json_loads           | 24.4 us                                                      | 25.3 us: 1.04x slower                                                                 |
| tomli_loads          | 2.16 sec                                                     | 2.30 sec: 1.06x slower                                                                |
| json_dumps           | 10.2 ms                                                      | 10.9 ms: 1.07x slower                                                                 |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.03 ms: 1.05x slower                                                                 |
| python_startup         | 11.6 ms                                                      | 13.3 ms: 1.15x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 39.3 ms: 1.03x slower                                                                 |
| mako            | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                                                 |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 300 ms: 1.44x faster                                                                  |
| async_tree_memoization_tg  | 540 ms                                                       | 380 ms: 1.42x faster                                                                  |
| async_tree_io_tg           | 1.05 sec                                                     | 771 ms: 1.37x faster                                                                  |
| async_tree_none            | 452 ms                                                       | 332 ms: 1.36x faster                                                                  |
| async_tree_memoization     | 544 ms                                                       | 401 ms: 1.35x faster                                                                  |
| generators                 | 37.4 ms                                                      | 28.9 ms: 1.30x faster                                                                 |
| async_tree_io              | 1.04 sec                                                     | 804 ms: 1.30x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 539 ms: 1.29x faster                                                                  |
| deepcopy                   | 368 us                                                       | 292 us: 1.26x faster                                                                  |
| comprehensions             | 21.9 us                                                      | 17.4 us: 1.26x faster                                                                 |
| deepcopy_memo              | 36.8 us                                                      | 29.4 us: 1.25x faster                                                                 |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 574 ms: 1.21x faster                                                                  |
| pathlib                    | 18.9 ms                                                      | 16.0 ms: 1.18x faster                                                                 |
| deepcopy_reduce            | 3.37 us                                                      | 2.96 us: 1.14x faster                                                                 |
| crypto_pyaes               | 80.3 ms                                                      | 71.5 ms: 1.12x faster                                                                 |
| raytrace                   | 298 ms                                                       | 265 ms: 1.12x faster                                                                  |
| logging_format             | 7.48 us                                                      | 6.81 us: 1.10x faster                                                                 |
| async_generators           | 390 ms                                                       | 356 ms: 1.10x faster                                                                  |
| bench_thread_pool          | 950 us                                                       | 869 us: 1.09x faster                                                                  |
| logging_simple             | 6.71 us                                                      | 6.19 us: 1.08x faster                                                                 |
| coroutines                 | 23.0 ms                                                      | 21.7 ms: 1.06x faster                                                                 |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                                                  |
| sympy_sum                  | 162 ms                                                       | 155 ms: 1.05x faster                                                                  |
| tornado_http               | 121 ms                                                       | 116 ms: 1.04x faster                                                                  |
| scimark_lu                 | 98.8 ms                                                      | 94.8 ms: 1.04x faster                                                                 |
| regex_compile              | 144 ms                                                       | 139 ms: 1.04x faster                                                                  |
| mdp                        | 2.57 sec                                                     | 2.48 sec: 1.04x faster                                                                |
| regex_effbot               | 3.57 ms                                                      | 3.46 ms: 1.03x faster                                                                 |
| chaos                      | 64.0 ms                                                      | 62.0 ms: 1.03x faster                                                                 |
| scimark_monte_carlo        | 69.0 ms                                                      | 67.1 ms: 1.03x faster                                                                 |
| sympy_str                  | 302 ms                                                       | 296 ms: 1.02x faster                                                                  |
| pickle_pure_python         | 318 us                                                       | 311 us: 1.02x faster                                                                  |
| regex_dna                  | 239 ms                                                       | 234 ms: 1.02x faster                                                                  |
| sympy_integrate            | 23.9 ms                                                      | 23.5 ms: 1.02x faster                                                                 |
| xml_etree_generate         | 86.1 ms                                                      | 84.6 ms: 1.02x faster                                                                 |
| scimark_sor                | 109 ms                                                       | 107 ms: 1.02x faster                                                                  |
| xml_etree_iterparse        | 103 ms                                                       | 101 ms: 1.02x faster                                                                  |
| meteor_contest             | 128 ms                                                       | 127 ms: 1.01x faster                                                                  |
| asyncio_tcp                | 378 ms                                                       | 374 ms: 1.01x faster                                                                  |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.18 ms: 1.01x faster                                                                 |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                                                |
| 2to3                       | 285 ms                                                       | 287 ms: 1.01x slower                                                                  |
| unpickle_pure_python       | 210 us                                                       | 211 us: 1.01x slower                                                                  |
| xml_etree_process          | 58.4 ms                                                      | 59.1 ms: 1.01x slower                                                                 |
| sqlglot_transpile          | 1.78 ms                                                      | 1.80 ms: 1.01x slower                                                                 |
| pycparser                  | 1.23 sec                                                     | 1.26 sec: 1.02x slower                                                                |
| fannkuch                   | 350 ms                                                       | 358 ms: 1.02x slower                                                                  |
| pprint_safe_repr           | 807 ms                                                       | 827 ms: 1.02x slower                                                                  |
| sqlglot_optimize           | 57.5 ms                                                      | 58.9 ms: 1.03x slower                                                                 |
| django_template            | 38.2 ms                                                      | 39.3 ms: 1.03x slower                                                                 |
| mako                       | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                                                 |
| pprint_pformat             | 1.65 sec                                                     | 1.70 sec: 1.03x slower                                                                |
| logging_silent             | 94.4 ns                                                      | 97.2 ns: 1.03x slower                                                                 |
| sqlglot_normalize          | 116 ms                                                       | 120 ms: 1.03x slower                                                                  |
| sqlglot_parse              | 1.38 ms                                                      | 1.43 ms: 1.03x slower                                                                 |
| docutils                   | 2.87 sec                                                     | 2.97 sec: 1.04x slower                                                                |
| json_loads                 | 24.4 us                                                      | 25.3 us: 1.04x slower                                                                 |
| sympy_expand               | 484 ms                                                       | 503 ms: 1.04x slower                                                                  |
| spectral_norm              | 91.6 ms                                                      | 95.7 ms: 1.04x slower                                                                 |
| python_startup_no_site     | 8.64 ms                                                      | 9.03 ms: 1.05x slower                                                                 |
| json                       | 5.12 ms                                                      | 5.37 ms: 1.05x slower                                                                 |
| deltablue                  | 3.24 ms                                                      | 3.43 ms: 1.06x slower                                                                 |
| hexiom                     | 5.96 ms                                                      | 6.34 ms: 1.06x slower                                                                 |
| tomli_loads                | 2.16 sec                                                     | 2.30 sec: 1.06x slower                                                                |
| json_dumps                 | 10.2 ms                                                      | 10.9 ms: 1.07x slower                                                                 |
| float                      | 76.6 ms                                                      | 82.4 ms: 1.07x slower                                                                 |
| regex_v8                   | 23.6 ms                                                      | 25.4 ms: 1.08x slower                                                                 |
| go                         | 150 ms                                                       | 162 ms: 1.08x slower                                                                  |
| pyflate                    | 439 ms                                                       | 478 ms: 1.09x slower                                                                  |
| richards_super             | 51.3 ms                                                      | 56.2 ms: 1.09x slower                                                                 |
| richards                   | 45.7 ms                                                      | 50.2 ms: 1.10x slower                                                                 |
| telco                      | 6.96 ms                                                      | 7.98 ms: 1.15x slower                                                                 |
| python_startup             | 11.6 ms                                                      | 13.3 ms: 1.15x slower                                                                 |
| typing_runtime_protocols   | 152 us                                                       | 174 us: 1.15x slower                                                                  |
| create_gc_cycles           | 1.59 ms                                                      | 1.99 ms: 1.25x slower                                                                 |
| coverage                   | 66.7 ms                                                      | 83.6 ms: 1.25x slower                                                                 |
| gc_traversal               | 3.48 ms                                                      | 4.45 ms: 1.28x slower                                                                 |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                          |

Benchmark hidden because not significant (6): bench_mp_pool, nbody, nqueens, xml_etree_parse, scimark_fft, asyncio_websockets
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240828-3.14.0a0-bfd4400/bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.029x faster
# HPT report

- Reliability score: 86.96% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x