
# Results vs. base

- fork: gvanrossum
- ref: new_for_iter_uops
- machine: linux-x86_64
- commit hash: 4ccb873
- commit date: 2023-07-12
- overall geometric mean: 1.00x faster
- HPT reliability: 99.90%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230712-linux-x86_64-python-7f55f58b6c97306da350-3.13.0a0-7f55f58 | bm-20230712-linux-x86_64-gvanrossum-new_for_iter_uops-3.13.0a0-4ccb873 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| docutils       | 2.66 sec                                                              | 2.65 sec: 1.00x faster                                                 |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230712-linux-x86_64-python-7f55f58b6c97306da350-3.13.0a0-7f55f58 | bm-20230712-linux-x86_64-gvanrossum-new_for_iter_uops-3.13.0a0-4ccb873 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 22.8 ms                                                               | 22.5 ms: 1.01x faster                                                  |
| regex_effbot   | 3.72 ms                                                               | 3.68 ms: 1.01x faster                                                  |
| regex_compile  | 137 ms                                                                | 136 ms: 1.01x faster                                                   |
| regex_dna      | 209 ms                                                                | 211 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230712-linux-x86_64-python-7f55f58b6c97306da350-3.13.0a0-7f55f58 | bm-20230712-linux-x86_64-gvanrossum-new_for_iter_uops-3.13.0a0-4ccb873 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_list          | 4.76 us                                                               | 4.55 us: 1.05x faster                                                  |
| unpickle_list        | 5.12 us                                                               | 4.94 us: 1.03x faster                                                  |
| unpickle             | 15.1 us                                                               | 14.8 us: 1.02x faster                                                  |
| unpickle_pure_python | 214 us                                                                | 211 us: 1.01x faster                                                   |
| tomli_loads          | 2.32 sec                                                              | 2.30 sec: 1.01x faster                                                 |
| json_loads           | 25.9 us                                                               | 25.7 us: 1.01x faster                                                  |
| xml_etree_generate   | 84.5 ms                                                               | 83.7 ms: 1.01x faster                                                  |
| xml_etree_process    | 58.1 ms                                                               | 57.6 ms: 1.01x faster                                                  |
| pickle               | 10.5 us                                                               | 10.5 us: 1.01x faster                                                  |
| json_dumps           | 9.72 ms                                                               | 9.82 ms: 1.01x slower                                                  |
| pickle_dict          | 31.6 us                                                               | 32.6 us: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                           |

Benchmark hidden because not significant (3): xml_etree_iterparse, pickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230712-linux-x86_64-python-7f55f58b6c97306da350-3.13.0a0-7f55f58 | bm-20230712-linux-x86_64-gvanrossum-new_for_iter_uops-3.13.0a0-4ccb873 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.72 ms                                                               | 6.70 ms: 1.00x faster                                                  |
| python_startup         | 9.22 ms                                                               | 9.22 ms: 1.00x faster                                                  |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230712-linux-x86_64-python-7f55f58b6c97306da350-3.13.0a0-7f55f58 | bm-20230712-linux-x86_64-gvanrossum-new_for_iter_uops-3.13.0a0-4ccb873 |
|-----------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako      | 10.9 ms                                                               | 10.8 ms: 1.01x faster                                                  |

All benchmarks:
===============

| Benchmark                | bm-20230712-linux-x86_64-python-7f55f58b6c97306da350-3.13.0a0-7f55f58 | bm-20230712-linux-x86_64-gvanrossum-new_for_iter_uops-3.13.0a0-4ccb873 |
|--------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_list              | 4.76 us                                                               | 4.55 us: 1.05x faster                                                  |
| nqueens                  | 81.9 ms                                                               | 78.9 ms: 1.04x faster                                                  |
| unpickle_list            | 5.12 us                                                               | 4.94 us: 1.03x faster                                                  |
| typing_runtime_protocols | 147 us                                                                | 143 us: 1.03x faster                                                   |
| richards                 | 47.8 ms                                                               | 46.8 ms: 1.02x faster                                                  |
| async_generators         | 451 ms                                                                | 442 ms: 1.02x faster                                                   |
| unpickle                 | 15.1 us                                                               | 14.8 us: 1.02x faster                                                  |
| hexiom                   | 6.10 ms                                                               | 5.99 ms: 1.02x faster                                                  |
| meteor_contest           | 106 ms                                                                | 104 ms: 1.02x faster                                                   |
| crypto_pyaes             | 69.9 ms                                                               | 68.9 ms: 1.02x faster                                                  |
| mako                     | 10.9 ms                                                               | 10.8 ms: 1.01x faster                                                  |
| unpickle_pure_python     | 214 us                                                                | 211 us: 1.01x faster                                                   |
| sqlglot_parse            | 1.31 ms                                                               | 1.29 ms: 1.01x faster                                                  |
| create_gc_cycles         | 1.52 ms                                                               | 1.51 ms: 1.01x faster                                                  |
| regex_v8                 | 22.8 ms                                                               | 22.5 ms: 1.01x faster                                                  |
| tomli_loads              | 2.32 sec                                                              | 2.30 sec: 1.01x faster                                                 |
| regex_effbot             | 3.72 ms                                                               | 3.68 ms: 1.01x faster                                                  |
| dulwich_log              | 66.7 ms                                                               | 66.0 ms: 1.01x faster                                                  |
| pprint_safe_repr         | 724 ms                                                                | 716 ms: 1.01x faster                                                   |
| json_loads               | 25.9 us                                                               | 25.7 us: 1.01x faster                                                  |
| sqlglot_transpile        | 1.63 ms                                                               | 1.61 ms: 1.01x faster                                                  |
| xml_etree_generate       | 84.5 ms                                                               | 83.7 ms: 1.01x faster                                                  |
| dask                     | 522 ms                                                                | 517 ms: 1.01x faster                                                   |
| chaos                    | 59.3 ms                                                               | 58.8 ms: 1.01x faster                                                  |
| logging_format           | 6.53 us                                                               | 6.47 us: 1.01x faster                                                  |
| coroutines               | 22.8 ms                                                               | 22.6 ms: 1.01x faster                                                  |
| xml_etree_process        | 58.1 ms                                                               | 57.6 ms: 1.01x faster                                                  |
| scimark_monte_carlo      | 68.6 ms                                                               | 68.1 ms: 1.01x faster                                                  |
| scimark_sor              | 120 ms                                                                | 120 ms: 1.01x faster                                                   |
| fannkuch                 | 399 ms                                                                | 396 ms: 1.01x faster                                                   |
| spectral_norm            | 107 ms                                                                | 106 ms: 1.01x faster                                                   |
| go                       | 138 ms                                                                | 137 ms: 1.01x faster                                                   |
| asyncio_tcp              | 510 ms                                                                | 507 ms: 1.01x faster                                                   |
| regex_compile            | 137 ms                                                                | 136 ms: 1.01x faster                                                   |
| comprehensions           | 20.4 us                                                               | 20.3 us: 1.01x faster                                                  |
| pickle                   | 10.5 us                                                               | 10.5 us: 1.01x faster                                                  |
| docutils                 | 2.66 sec                                                              | 2.65 sec: 1.00x faster                                                 |
| bench_thread_pool        | 817 us                                                                | 814 us: 1.00x faster                                                   |
| python_startup_no_site   | 6.72 ms                                                               | 6.70 ms: 1.00x faster                                                  |
| python_startup           | 9.22 ms                                                               | 9.22 ms: 1.00x faster                                                  |
| sqlglot_normalize        | 105 ms                                                                | 106 ms: 1.01x slower                                                   |
| sqlglot_optimize         | 52.5 ms                                                               | 52.9 ms: 1.01x slower                                                  |
| raytrace                 | 268 ms                                                                | 270 ms: 1.01x slower                                                   |
| pyflate                  | 446 ms                                                                | 449 ms: 1.01x slower                                                   |
| sqlite_synth             | 2.75 us                                                               | 2.77 us: 1.01x slower                                                  |
| scimark_fft              | 354 ms                                                                | 357 ms: 1.01x slower                                                   |
| regex_dna                | 209 ms                                                                | 211 ms: 1.01x slower                                                   |
| json_dumps               | 9.72 ms                                                               | 9.82 ms: 1.01x slower                                                  |
| deepcopy_reduce          | 3.14 us                                                               | 3.18 us: 1.01x slower                                                  |
| logging_simple           | 5.88 us                                                               | 5.95 us: 1.01x slower                                                  |
| telco                    | 7.15 ms                                                               | 7.24 ms: 1.01x slower                                                  |
| generators               | 28.5 ms                                                               | 28.9 ms: 1.01x slower                                                  |
| deepcopy_memo            | 37.6 us                                                               | 38.1 us: 1.01x slower                                                  |
| deepcopy                 | 349 us                                                                | 354 us: 1.02x slower                                                   |
| scimark_lu               | 110 ms                                                                | 112 ms: 1.03x slower                                                   |
| unpack_sequence          | 44.2 ns                                                               | 45.3 ns: 1.03x slower                                                  |
| gc_traversal             | 3.84 ms                                                               | 3.96 ms: 1.03x slower                                                  |
| pickle_dict              | 31.6 us                                                               | 32.6 us: 1.03x slower                                                  |
| mdp                      | 2.54 sec                                                              | 2.65 sec: 1.04x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.00x faster                                                           |

Benchmark hidden because not significant (23): coverage, nbody, async_tree_memoization, xml_etree_iterparse, mypy2, pickle_pure_python, xml_etree_parse, tornado_http, async_tree_none, logging_silent, deltablue, asyncio_tcp_ssl, async_tree_io, float, pprint_pformat, pidigits, pathlib, bench_mp_pool, scimark_sparse_mat_mult, richards_super, pycparser, json, async_tree_cpu_io_mixed


# HPT report

- Reliability score: 99.90% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
