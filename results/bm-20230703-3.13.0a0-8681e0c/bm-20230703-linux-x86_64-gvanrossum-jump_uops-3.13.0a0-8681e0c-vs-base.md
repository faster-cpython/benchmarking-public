
# Results vs. base

- fork: gvanrossum
- ref: jump_uops
- machine: linux-x86_64
- commit hash: 8681e0c
- commit date: 2023-07-03
- overall geometric mean: 1.01x faster

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230703-linux-x86_64-python-3406f8cce542ea4edf41-3.13.0a0-3406f8c | bm-20230703-linux-x86_64-gvanrossum-jump_uops-3.13.0a0-8681e0c |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 92.5 ms                                                               | 89.8 ms: 1.03x faster                                          |
| float          | 79.6 ms                                                               | 78.9 ms: 1.01x faster                                          |
| pidigits       | 197 ms                                                                | 197 ms: 1.00x slower                                           |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230703-linux-x86_64-python-3406f8cce542ea4edf41-3.13.0a0-3406f8c | bm-20230703-linux-x86_64-gvanrossum-jump_uops-3.13.0a0-8681e0c |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 135 ms: 1.02x faster                                           |
| regex_effbot   | 3.64 ms                                                               | 3.68 ms: 1.01x slower                                          |
| regex_v8       | 22.7 ms                                                               | 23.0 ms: 1.01x slower                                          |
| regex_dna      | 214 ms                                                                | 217 ms: 1.02x slower                                           |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20230703-linux-x86_64-python-3406f8cce542ea4edf41-3.13.0a0-3406f8c | bm-20230703-linux-x86_64-gvanrossum-jump_uops-3.13.0a0-8681e0c |
|--------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| tomli_loads        | 2.30 sec                                                              | 2.17 sec: 1.06x faster                                         |
| pickle_list        | 4.77 us                                                               | 4.55 us: 1.05x faster                                          |
| pickle_dict        | 31.7 us                                                               | 31.2 us: 1.02x faster                                          |
| pickle_pure_python | 302 us                                                                | 301 us: 1.01x faster                                           |
| json_loads         | 25.7 us                                                               | 26.0 us: 1.01x slower                                          |
| Geometric mean     | (ref)                                                                 | 1.01x faster                                                   |

Benchmark hidden because not significant (9): xml_etree_parse, unpickle_pure_python, xml_etree_process, json_dumps, xml_etree_iterparse, pickle, xml_etree_generate, unpickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20230703-linux-x86_64-python-3406f8cce542ea4edf41-3.13.0a0-3406f8c | bm-20230703-linux-x86_64-gvanrossum-jump_uops-3.13.0a0-8681e0c |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup | 9.15 ms                                                               | 9.18 ms: 1.00x slower                                          |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20230703-linux-x86_64-python-3406f8cce542ea4edf41-3.13.0a0-3406f8c | bm-20230703-linux-x86_64-gvanrossum-jump_uops-3.13.0a0-8681e0c |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| gc_traversal             | 4.06 ms                                                               | 3.66 ms: 1.11x faster                                          |
| richards                 | 47.9 ms                                                               | 44.8 ms: 1.07x faster                                          |
| tomli_loads              | 2.30 sec                                                              | 2.17 sec: 1.06x faster                                         |
| richards_super           | 53.5 ms                                                               | 50.9 ms: 1.05x faster                                          |
| pickle_list              | 4.77 us                                                               | 4.55 us: 1.05x faster                                          |
| mdp                      | 2.65 sec                                                              | 2.53 sec: 1.05x faster                                         |
| spectral_norm            | 110 ms                                                                | 107 ms: 1.03x faster                                           |
| deltablue                | 3.30 ms                                                               | 3.21 ms: 1.03x faster                                          |
| nbody                    | 92.5 ms                                                               | 89.8 ms: 1.03x faster                                          |
| pycparser                | 1.16 sec                                                              | 1.14 sec: 1.02x faster                                         |
| go                       | 138 ms                                                                | 135 ms: 1.02x faster                                           |
| logging_simple           | 5.95 us                                                               | 5.82 us: 1.02x faster                                          |
| logging_format           | 6.54 us                                                               | 6.40 us: 1.02x faster                                          |
| regex_compile            | 137 ms                                                                | 135 ms: 1.02x faster                                           |
| hexiom                   | 6.09 ms                                                               | 5.97 ms: 1.02x faster                                          |
| scimark_sor              | 121 ms                                                                | 118 ms: 1.02x faster                                           |
| sqlglot_optimize         | 53.5 ms                                                               | 52.5 ms: 1.02x faster                                          |
| pprint_safe_repr         | 729 ms                                                                | 716 ms: 1.02x faster                                           |
| chaos                    | 60.2 ms                                                               | 59.2 ms: 1.02x faster                                          |
| pickle_dict              | 31.7 us                                                               | 31.2 us: 1.02x faster                                          |
| pathlib                  | 19.2 ms                                                               | 18.9 ms: 1.02x faster                                          |
| deepcopy_reduce          | 3.14 us                                                               | 3.10 us: 1.02x faster                                          |
| sqlglot_parse            | 1.33 ms                                                               | 1.31 ms: 1.02x faster                                          |
| deepcopy_memo            | 37.7 us                                                               | 37.1 us: 1.01x faster                                          |
| sqlglot_transpile        | 1.65 ms                                                               | 1.63 ms: 1.01x faster                                          |
| pprint_pformat           | 1.49 sec                                                              | 1.47 sec: 1.01x faster                                         |
| dask                     | 522 ms                                                                | 515 ms: 1.01x faster                                           |
| scimark_fft              | 355 ms                                                                | 351 ms: 1.01x faster                                           |
| meteor_contest           | 106 ms                                                                | 105 ms: 1.01x faster                                           |
| coverage                 | 93.0 ms                                                               | 91.9 ms: 1.01x faster                                          |
| raytrace                 | 269 ms                                                                | 266 ms: 1.01x faster                                           |
| comprehensions           | 20.4 us                                                               | 20.2 us: 1.01x faster                                          |
| sqlglot_normalize        | 106 ms                                                                | 105 ms: 1.01x faster                                           |
| mypy2                    | 338 ms                                                                | 334 ms: 1.01x faster                                           |
| float                    | 79.6 ms                                                               | 78.9 ms: 1.01x faster                                          |
| fannkuch                 | 398 ms                                                                | 396 ms: 1.01x faster                                           |
| pickle_pure_python       | 302 us                                                                | 301 us: 1.01x faster                                           |
| create_gc_cycles         | 1.49 ms                                                               | 1.48 ms: 1.01x faster                                          |
| async_tree_io            | 1.20 sec                                                              | 1.19 sec: 1.00x faster                                         |
| deepcopy                 | 348 us                                                                | 346 us: 1.00x faster                                           |
| generators               | 28.8 ms                                                               | 28.7 ms: 1.00x faster                                          |
| asyncio_tcp              | 516 ms                                                                | 514 ms: 1.00x faster                                           |
| pidigits                 | 197 ms                                                                | 197 ms: 1.00x slower                                           |
| python_startup           | 9.15 ms                                                               | 9.18 ms: 1.00x slower                                          |
| unpack_sequence          | 49.8 ns                                                               | 50.2 ns: 1.01x slower                                          |
| regex_effbot             | 3.64 ms                                                               | 3.68 ms: 1.01x slower                                          |
| regex_v8                 | 22.7 ms                                                               | 23.0 ms: 1.01x slower                                          |
| json                     | 4.90 ms                                                               | 4.95 ms: 1.01x slower                                          |
| typing_runtime_protocols | 146 us                                                                | 148 us: 1.01x slower                                           |
| json_loads               | 25.7 us                                                               | 26.0 us: 1.01x slower                                          |
| regex_dna                | 214 ms                                                                | 217 ms: 1.02x slower                                           |
| nqueens                  | 79.7 ms                                                               | 81.0 ms: 1.02x slower                                          |
| logging_silent           | 103 ns                                                                | 105 ns: 1.02x slower                                           |
| scimark_sparse_mat_mult  | 4.65 ms                                                               | 4.74 ms: 1.02x slower                                          |
| coroutines               | 22.6 ms                                                               | 23.2 ms: 1.03x slower                                          |
| Geometric mean           | (ref)                                                                 | 1.01x faster                                                   |

Benchmark hidden because not significant (27): scimark_monte_carlo, async_tree_memoization, async_tree_cpu_io_mixed, xml_etree_parse, sqlite_synth, unpickle_pure_python, xml_etree_process, json_dumps, async_tree_none, docutils, bench_thread_pool, async_generators, tornado_http, python_startup_no_site, crypto_pyaes, bench_mp_pool, asyncio_tcp_ssl, xml_etree_iterparse, dulwich_log, pyflate, mako, pickle, scimark_lu, xml_etree_generate, unpickle_list, unpickle, telco
