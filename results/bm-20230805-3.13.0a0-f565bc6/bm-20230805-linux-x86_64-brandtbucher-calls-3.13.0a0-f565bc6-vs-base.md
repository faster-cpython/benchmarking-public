
# Results vs. base

- fork: brandtbucher
- ref: calls
- machine: linux-x86_64
- commit hash: f565bc6
- commit date: 2023-08-05
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230808-linux-x86_64-python-aab6f7173a3b82559962-3.13.0a0-aab6f71 | bm-20230805-linux-x86_64-brandtbucher-calls-3.13.0a0-f565bc6 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| pidigits       | 201 ms                                                                | 189 ms: 1.06x faster                                         |
| nbody          | 90.2 ms                                                               | 88.2 ms: 1.02x faster                                        |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                 |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230808-linux-x86_64-python-aab6f7173a3b82559962-3.13.0a0-aab6f71 | bm-20230805-linux-x86_64-brandtbucher-calls-3.13.0a0-f565bc6 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_dna      | 203 ms                                                                | 212 ms: 1.04x slower                                         |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                 |

Benchmark hidden because not significant (3): regex_effbot, regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230808-linux-x86_64-python-aab6f7173a3b82559962-3.13.0a0-aab6f71 | bm-20230805-linux-x86_64-brandtbucher-calls-3.13.0a0-f565bc6 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| pickle               | 10.9 us                                                               | 10.5 us: 1.03x faster                                        |
| xml_etree_parse      | 155 ms                                                                | 152 ms: 1.02x faster                                         |
| xml_etree_iterparse  | 103 ms                                                                | 102 ms: 1.01x faster                                         |
| xml_etree_process    | 57.5 ms                                                               | 57.1 ms: 1.01x faster                                        |
| json_loads           | 25.4 us                                                               | 25.5 us: 1.01x slower                                        |
| pickle_list          | 4.63 us                                                               | 4.72 us: 1.02x slower                                        |
| unpickle             | 14.7 us                                                               | 15.0 us: 1.02x slower                                        |
| unpickle_pure_python | 211 us                                                                | 216 us: 1.03x slower                                         |
| pickle_pure_python   | 297 us                                                                | 305 us: 1.03x slower                                         |
| pickle_dict          | 31.4 us                                                               | 33.4 us: 1.06x slower                                        |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                 |

Benchmark hidden because not significant (4): tomli_loads, xml_etree_generate, unpickle_list, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230808-linux-x86_64-python-aab6f7173a3b82559962-3.13.0a0-aab6f71 | bm-20230805-linux-x86_64-brandtbucher-calls-3.13.0a0-f565bc6 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 6.84 ms                                                               | 6.85 ms: 1.00x slower                                        |
| python_startup         | 9.36 ms                                                               | 9.37 ms: 1.00x slower                                        |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230808-linux-x86_64-python-aab6f7173a3b82559962-3.13.0a0-aab6f71 | bm-20230805-linux-x86_64-brandtbucher-calls-3.13.0a0-f565bc6 |
|-----------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| mako      | 10.7 ms                                                               | 10.6 ms: 1.01x faster                                        |

All benchmarks:
===============

| Benchmark                | bm-20230808-linux-x86_64-python-aab6f7173a3b82559962-3.13.0a0-aab6f71 | bm-20230805-linux-x86_64-brandtbucher-calls-3.13.0a0-f565bc6 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| gc_traversal             | 4.32 ms                                                               | 3.84 ms: 1.12x faster                                        |
| unpack_sequence          | 43.6 ns                                                               | 40.0 ns: 1.09x faster                                        |
| pidigits                 | 201 ms                                                                | 189 ms: 1.06x faster                                         |
| typing_runtime_protocols | 147 us                                                                | 143 us: 1.03x faster                                         |
| pickle                   | 10.9 us                                                               | 10.5 us: 1.03x faster                                        |
| nqueens                  | 81.1 ms                                                               | 78.8 ms: 1.03x faster                                        |
| spectral_norm            | 107 ms                                                                | 105 ms: 1.02x faster                                         |
| nbody                    | 90.2 ms                                                               | 88.2 ms: 1.02x faster                                        |
| deepcopy                 | 356 us                                                                | 350 us: 1.02x faster                                         |
| logging_silent           | 103 ns                                                                | 101 ns: 1.02x faster                                         |
| xml_etree_parse          | 155 ms                                                                | 152 ms: 1.02x faster                                         |
| telco                    | 7.92 ms                                                               | 7.82 ms: 1.01x faster                                        |
| xml_etree_iterparse      | 103 ms                                                                | 102 ms: 1.01x faster                                         |
| async_tree_none          | 484 ms                                                                | 479 ms: 1.01x faster                                         |
| sqlglot_normalize        | 105 ms                                                                | 104 ms: 1.01x faster                                         |
| async_tree_io            | 1.20 sec                                                              | 1.19 sec: 1.01x faster                                       |
| xml_etree_process        | 57.5 ms                                                               | 57.1 ms: 1.01x faster                                        |
| bench_thread_pool        | 826 us                                                                | 819 us: 1.01x faster                                         |
| scimark_fft              | 359 ms                                                                | 357 ms: 1.01x faster                                         |
| mako                     | 10.7 ms                                                               | 10.6 ms: 1.01x faster                                        |
| pprint_pformat           | 1.47 sec                                                              | 1.46 sec: 1.01x faster                                       |
| mdp                      | 2.53 sec                                                              | 2.52 sec: 1.00x faster                                       |
| sqlglot_optimize         | 52.8 ms                                                               | 52.6 ms: 1.00x faster                                        |
| create_gc_cycles         | 1.49 ms                                                               | 1.48 ms: 1.00x faster                                        |
| asyncio_tcp_ssl          | 1.80 sec                                                              | 1.79 sec: 1.00x faster                                       |
| python_startup_no_site   | 6.84 ms                                                               | 6.85 ms: 1.00x slower                                        |
| python_startup           | 9.36 ms                                                               | 9.37 ms: 1.00x slower                                        |
| deepcopy_memo            | 37.6 us                                                               | 37.8 us: 1.01x slower                                        |
| json_loads               | 25.4 us                                                               | 25.5 us: 1.01x slower                                        |
| asyncio_tcp              | 484 ms                                                                | 487 ms: 1.01x slower                                         |
| raytrace                 | 270 ms                                                                | 272 ms: 1.01x slower                                         |
| async_generators         | 448 ms                                                                | 452 ms: 1.01x slower                                         |
| richards_super           | 53.1 ms                                                               | 53.6 ms: 1.01x slower                                        |
| pathlib                  | 18.5 ms                                                               | 18.7 ms: 1.01x slower                                        |
| scimark_monte_carlo      | 67.2 ms                                                               | 68.0 ms: 1.01x slower                                        |
| dask                     | 516 ms                                                                | 523 ms: 1.01x slower                                         |
| pycparser                | 1.14 sec                                                              | 1.16 sec: 1.01x slower                                       |
| sqlglot_transpile        | 1.60 ms                                                               | 1.63 ms: 1.02x slower                                        |
| meteor_contest           | 105 ms                                                                | 107 ms: 1.02x slower                                         |
| logging_simple           | 6.00 us                                                               | 6.10 us: 1.02x slower                                        |
| sqlglot_parse            | 1.29 ms                                                               | 1.31 ms: 1.02x slower                                        |
| crypto_pyaes             | 68.7 ms                                                               | 69.9 ms: 1.02x slower                                        |
| hexiom                   | 5.93 ms                                                               | 6.04 ms: 1.02x slower                                        |
| pickle_list              | 4.63 us                                                               | 4.72 us: 1.02x slower                                        |
| scimark_lu               | 110 ms                                                                | 112 ms: 1.02x slower                                         |
| scimark_sor              | 120 ms                                                                | 122 ms: 1.02x slower                                         |
| fannkuch                 | 388 ms                                                                | 396 ms: 1.02x slower                                         |
| unpickle                 | 14.7 us                                                               | 15.0 us: 1.02x slower                                        |
| unpickle_pure_python     | 211 us                                                                | 216 us: 1.03x slower                                         |
| go                       | 137 ms                                                                | 140 ms: 1.03x slower                                         |
| pickle_pure_python       | 297 us                                                                | 305 us: 1.03x slower                                         |
| deltablue                | 3.18 ms                                                               | 3.30 ms: 1.04x slower                                        |
| logging_format           | 6.55 us                                                               | 6.79 us: 1.04x slower                                        |
| regex_dna                | 203 ms                                                                | 212 ms: 1.04x slower                                         |
| pickle_dict              | 31.4 us                                                               | 33.4 us: 1.06x slower                                        |
| generators               | 28.3 ms                                                               | 30.2 ms: 1.07x slower                                        |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                 |

Benchmark hidden because not significant (26): json, tomli_loads, coverage, async_tree_cpu_io_mixed, pyflate, coroutines, async_tree_memoization, pprint_safe_repr, scimark_sparse_mat_mult, xml_etree_generate, unpickle_list, regex_effbot, dulwich_log, chaos, bench_mp_pool, regex_compile, regex_v8, sqlite_synth, comprehensions, docutils, mypy2, float, deepcopy_reduce, richards, tornado_http, json_dumps
