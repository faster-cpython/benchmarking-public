
# Results vs. base

- fork: faster-cpython
- ref: specialize_more_load
- machine: linux-x86_64
- commit hash: 16a2718
- commit date: 2023-07-05
- overall geometric mean: 1.01x faster
- HPT reliability: 92.11%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230706-pythonperf2-x86_64-python-e1d45b8ed43e15908623-3.13.0a0-e1d45b8 | bm-20230705-pythonperf2-x86_64-faster%2dcpython-specialize_more_load-3.13.0a0-16a2718 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| docutils       | 2.92 sec                                                                    | 2.92 sec: 1.00x faster                                                                |
| tornado_http   | 123 ms                                                                      | 121 ms: 1.02x faster                                                                  |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230706-pythonperf2-x86_64-python-e1d45b8ed43e15908623-3.13.0a0-e1d45b8 | bm-20230705-pythonperf2-x86_64-faster%2dcpython-specialize_more_load-3.13.0a0-16a2718 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 90.9 ms                                                                     | 89.1 ms: 1.02x faster                                                                 |
| float          | 82.1 ms                                                                     | 81.3 ms: 1.01x faster                                                                 |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230706-pythonperf2-x86_64-python-e1d45b8ed43e15908623-3.13.0a0-e1d45b8 | bm-20230705-pythonperf2-x86_64-faster%2dcpython-specialize_more_load-3.13.0a0-16a2718 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_dna      | 237 ms                                                                      | 241 ms: 1.02x slower                                                                  |
| regex_effbot   | 3.50 ms                                                                     | 3.58 ms: 1.02x slower                                                                 |
| regex_v8       | 23.5 ms                                                                     | 24.2 ms: 1.03x slower                                                                 |
| Geometric mean | (ref)                                                                       | 1.02x slower                                                                          |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230706-pythonperf2-x86_64-python-e1d45b8ed43e15908623-3.13.0a0-e1d45b8 | bm-20230705-pythonperf2-x86_64-faster%2dcpython-specialize_more_load-3.13.0a0-16a2718 |
|----------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| unpickle             | 15.2 us                                                                     | 14.6 us: 1.04x faster                                                                 |
| unpickle_list        | 4.71 us                                                                     | 4.61 us: 1.02x faster                                                                 |
| xml_etree_generate   | 87.1 ms                                                                     | 85.4 ms: 1.02x faster                                                                 |
| pickle_list          | 4.43 us                                                                     | 4.34 us: 1.02x faster                                                                 |
| json_dumps           | 10.3 ms                                                                     | 10.1 ms: 1.02x faster                                                                 |
| xml_etree_iterparse  | 107 ms                                                                      | 105 ms: 1.02x faster                                                                  |
| pickle_pure_python   | 321 us                                                                      | 316 us: 1.02x faster                                                                  |
| json_loads           | 25.3 us                                                                     | 24.9 us: 1.02x faster                                                                 |
| unpickle_pure_python | 222 us                                                                      | 219 us: 1.01x faster                                                                  |
| xml_etree_process    | 59.6 ms                                                                     | 58.8 ms: 1.01x faster                                                                 |
| pickle_dict          | 31.7 us                                                                     | 31.4 us: 1.01x faster                                                                 |
| pickle               | 9.98 us                                                                     | 10.2 us: 1.03x slower                                                                 |
| tomli_loads          | 2.32 sec                                                                    | 2.40 sec: 1.04x slower                                                                |
| Geometric mean       | (ref)                                                                       | 1.01x faster                                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20230706-pythonperf2-x86_64-python-e1d45b8ed43e15908623-3.13.0a0-e1d45b8 | bm-20230705-pythonperf2-x86_64-faster%2dcpython-specialize_more_load-3.13.0a0-16a2718 |
|--------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| crypto_pyaes             | 82.5 ms                                                                     | 74.1 ms: 1.11x faster                                                                 |
| unpack_sequence          | 51.7 ns                                                                     | 46.8 ns: 1.11x faster                                                                 |
| scimark_monte_carlo      | 74.3 ms                                                                     | 67.9 ms: 1.09x faster                                                                 |
| unpickle                 | 15.2 us                                                                     | 14.6 us: 1.04x faster                                                                 |
| pycparser                | 1.35 sec                                                                    | 1.31 sec: 1.03x faster                                                                |
| sqlglot_transpile        | 1.90 ms                                                                     | 1.85 ms: 1.03x faster                                                                 |
| sqlglot_parse            | 1.48 ms                                                                     | 1.45 ms: 1.02x faster                                                                 |
| unpickle_list            | 4.71 us                                                                     | 4.61 us: 1.02x faster                                                                 |
| async_generators         | 399 ms                                                                      | 391 ms: 1.02x faster                                                                  |
| raytrace                 | 281 ms                                                                      | 275 ms: 1.02x faster                                                                  |
| comprehensions           | 22.4 us                                                                     | 22.0 us: 1.02x faster                                                                 |
| scimark_sparse_mat_mult  | 4.46 ms                                                                     | 4.37 ms: 1.02x faster                                                                 |
| xml_etree_generate       | 87.1 ms                                                                     | 85.4 ms: 1.02x faster                                                                 |
| nbody                    | 90.9 ms                                                                     | 89.1 ms: 1.02x faster                                                                 |
| logging_silent           | 98.4 ns                                                                     | 96.5 ns: 1.02x faster                                                                 |
| coverage                 | 90.9 ms                                                                     | 89.2 ms: 1.02x faster                                                                 |
| tornado_http             | 123 ms                                                                      | 121 ms: 1.02x faster                                                                  |
| pickle_list              | 4.43 us                                                                     | 4.34 us: 1.02x faster                                                                 |
| json_dumps               | 10.3 ms                                                                     | 10.1 ms: 1.02x faster                                                                 |
| xml_etree_iterparse      | 107 ms                                                                      | 105 ms: 1.02x faster                                                                  |
| pickle_pure_python       | 321 us                                                                      | 316 us: 1.02x faster                                                                  |
| json_loads               | 25.3 us                                                                     | 24.9 us: 1.02x faster                                                                 |
| logging_format           | 7.53 us                                                                     | 7.41 us: 1.02x faster                                                                 |
| unpickle_pure_python     | 222 us                                                                      | 219 us: 1.01x faster                                                                  |
| scimark_lu               | 100 ms                                                                      | 98.8 ms: 1.01x faster                                                                 |
| mdp                      | 2.60 sec                                                                    | 2.57 sec: 1.01x faster                                                                |
| deepcopy                 | 386 us                                                                      | 381 us: 1.01x faster                                                                  |
| xml_etree_process        | 59.6 ms                                                                     | 58.8 ms: 1.01x faster                                                                 |
| gc_traversal             | 3.58 ms                                                                     | 3.53 ms: 1.01x faster                                                                 |
| sqlite_synth             | 2.76 us                                                                     | 2.73 us: 1.01x faster                                                                 |
| chaos                    | 62.0 ms                                                                     | 61.4 ms: 1.01x faster                                                                 |
| float                    | 82.1 ms                                                                     | 81.3 ms: 1.01x faster                                                                 |
| hexiom                   | 6.54 ms                                                                     | 6.48 ms: 1.01x faster                                                                 |
| mypy2                    | 374 ms                                                                      | 371 ms: 1.01x faster                                                                  |
| pickle_dict              | 31.7 us                                                                     | 31.4 us: 1.01x faster                                                                 |
| pathlib                  | 19.7 ms                                                                     | 19.6 ms: 1.01x faster                                                                 |
| pprint_pformat           | 1.71 sec                                                                    | 1.70 sec: 1.01x faster                                                                |
| go                       | 174 ms                                                                      | 174 ms: 1.00x faster                                                                  |
| docutils                 | 2.92 sec                                                                    | 2.92 sec: 1.00x faster                                                                |
| asyncio_tcp_ssl          | 1.57 sec                                                                    | 1.57 sec: 1.00x slower                                                                |
| async_tree_io            | 1.08 sec                                                                    | 1.08 sec: 1.00x slower                                                                |
| sqlglot_normalize        | 118 ms                                                                      | 118 ms: 1.00x slower                                                                  |
| async_tree_none          | 467 ms                                                                      | 469 ms: 1.00x slower                                                                  |
| generators               | 36.9 ms                                                                     | 37.1 ms: 1.01x slower                                                                 |
| json                     | 5.15 ms                                                                     | 5.18 ms: 1.01x slower                                                                 |
| asyncio_tcp              | 379 ms                                                                      | 382 ms: 1.01x slower                                                                  |
| scimark_fft              | 313 ms                                                                      | 315 ms: 1.01x slower                                                                  |
| deepcopy_memo            | 37.7 us                                                                     | 38.1 us: 1.01x slower                                                                 |
| create_gc_cycles         | 1.66 ms                                                                     | 1.68 ms: 1.01x slower                                                                 |
| typing_runtime_protocols | 152 us                                                                      | 154 us: 1.01x slower                                                                  |
| fannkuch                 | 395 ms                                                                      | 401 ms: 1.02x slower                                                                  |
| regex_dna                | 237 ms                                                                      | 241 ms: 1.02x slower                                                                  |
| deltablue                | 3.55 ms                                                                     | 3.61 ms: 1.02x slower                                                                 |
| regex_effbot             | 3.50 ms                                                                     | 3.58 ms: 1.02x slower                                                                 |
| pickle                   | 9.98 us                                                                     | 10.2 us: 1.03x slower                                                                 |
| regex_v8                 | 23.5 ms                                                                     | 24.2 ms: 1.03x slower                                                                 |
| tomli_loads              | 2.32 sec                                                                    | 2.40 sec: 1.04x slower                                                                |
| telco                    | 7.65 ms                                                                     | 7.96 ms: 1.04x slower                                                                 |
| Geometric mean           | (ref)                                                                       | 1.01x faster                                                                          |

Benchmark hidden because not significant (24): xml_etree_parse, logging_simple, richards_super, mako, coroutines, async_tree_cpu_io_mixed, richards, async_tree_memoization, python_startup_no_site, python_startup, meteor_contest, pprint_safe_repr, pyflate, dask, nqueens, sqlglot_optimize, scimark_sor, pidigits, spectral_norm, regex_compile, dulwich_log, deepcopy_reduce, bench_thread_pool, bench_mp_pool


# HPT report

- Reliability score: 92.11% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
