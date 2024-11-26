# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_no_externs
- machine: windows-amd64
- commit hash: 64b198a
- commit date: 2024-10-25
- overall geometric mean: 1.185x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 248 ms: 1.01x slower                                                           |
| docutils       | 1.92 sec                                                    | 1.93 sec: 1.01x slower                                                         |
| html5lib       | 51.0 ms                                                     | 39.8 ms: 1.28x faster                                                          |
| tornado_http   | 108 ms                                                      | 99.0 ms: 1.09x faster                                                          |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|-------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 216 ms: 2.01x faster                                                           |
| async_tree_io           | 1.11 sec                                                    | 553 ms: 2.00x faster                                                           |
| async_tree_memoization  | 526 ms                                                      | 281 ms: 1.87x faster                                                           |
| async_tree_cpu_io_mixed | 638 ms                                                      | 383 ms: 1.66x faster                                                           |
| Geometric mean          | (ref)                                                       | 1.88x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 48.3 ms: 1.28x faster                                                          |
| nbody          | 71.3 ms                                                     | 56.2 ms: 1.27x faster                                                          |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 115 ms: 1.18x faster                                                           |
| regex_compile  | 106 ms                                                      | 92.5 ms: 1.15x faster                                                          |
| regex_effbot   | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                                          |
| regex_v8       | 15.4 ms                                                     | 14.7 ms: 1.05x faster                                                          |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.62 ms: 1.38x faster                                                          |
| pickle_pure_python   | 270 us                                                      | 204 us: 1.32x faster                                                           |
| tomli_loads          | 1.67 sec                                                    | 1.30 sec: 1.28x faster                                                         |
| unpickle_pure_python | 183 us                                                      | 147 us: 1.24x faster                                                           |
| xml_etree_process    | 44.5 ms                                                     | 36.7 ms: 1.21x faster                                                          |
| xml_etree_generate   | 55.5 ms                                                     | 51.7 ms: 1.07x faster                                                          |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.8 ms: 1.02x faster                                                          |
| xml_etree_parse      | 96.8 ms                                                     | 95.8 ms: 1.01x faster                                                          |
| json_loads           | 14.0 us                                                     | 14.6 us: 1.04x slower                                                          |
| Geometric mean       | (ref)                                                       | 1.16x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 24.4 ms: 1.18x slower                                                          |
| python_startup_no_site | 15.5 ms                                                     | 18.4 ms: 1.19x slower                                                          |
| Geometric mean         | (ref)                                                       | 1.19x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.14 ms: 1.76x faster                                                          |
| django_template | 28.9 ms                                                     | 27.0 ms: 1.07x faster                                                          |
| genshi_xml      | 41.0 ms                                                     | 46.8 ms: 1.14x slower                                                          |
| Geometric mean  | (ref)                                                       | 1.14x faster                                                                   |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 119 us: 2.83x faster                                                           |
| async_tree_none          | 435 ms                                                      | 216 ms: 2.01x faster                                                           |
| async_tree_io            | 1.11 sec                                                    | 553 ms: 2.00x faster                                                           |
| async_tree_memoization   | 526 ms                                                      | 281 ms: 1.87x faster                                                           |
| deltablue                | 4.19 ms                                                     | 2.35 ms: 1.78x faster                                                          |
| mako                     | 9.03 ms                                                     | 5.14 ms: 1.76x faster                                                          |
| deepcopy_memo            | 28.8 us                                                     | 17.0 us: 1.69x faster                                                          |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 383 ms: 1.66x faster                                                           |
| logging_silent           | 94.6 ns                                                     | 57.6 ns: 1.64x faster                                                          |
| scimark_sor              | 106 ms                                                      | 67.9 ms: 1.56x faster                                                          |
| go                       | 139 ms                                                      | 94.0 ms: 1.48x faster                                                          |
| scimark_lu               | 85.8 ms                                                     | 58.4 ms: 1.47x faster                                                          |
| crypto_pyaes             | 62.5 ms                                                     | 42.8 ms: 1.46x faster                                                          |
| scimark_monte_carlo      | 57.3 ms                                                     | 39.4 ms: 1.45x faster                                                          |
| spectral_norm            | 77.3 ms                                                     | 53.6 ms: 1.44x faster                                                          |
| chaos                    | 61.7 ms                                                     | 43.2 ms: 1.43x faster                                                          |
| generators               | 32.4 ms                                                     | 23.0 ms: 1.41x faster                                                          |
| comprehensions           | 16.5 us                                                     | 11.8 us: 1.40x faster                                                          |
| json_dumps               | 9.16 ms                                                     | 6.62 ms: 1.38x faster                                                          |
| pyflate                  | 409 ms                                                      | 300 ms: 1.37x faster                                                           |
| richards_super           | 52.2 ms                                                     | 38.3 ms: 1.36x faster                                                          |
| sqlglot_parse            | 1.22 ms                                                     | 908 us: 1.34x faster                                                           |
| raytrace                 | 273 ms                                                      | 207 ms: 1.32x faster                                                           |
| pickle_pure_python       | 270 us                                                      | 204 us: 1.32x faster                                                           |
| pprint_safe_repr         | 592 ms                                                      | 453 ms: 1.31x faster                                                           |
| deepcopy                 | 255 us                                                      | 196 us: 1.30x faster                                                           |
| pprint_pformat           | 1.22 sec                                                    | 945 ms: 1.29x faster                                                           |
| pycparser                | 930 ms                                                      | 722 ms: 1.29x faster                                                           |
| html5lib                 | 51.0 ms                                                     | 39.8 ms: 1.28x faster                                                          |
| tomli_loads              | 1.67 sec                                                    | 1.30 sec: 1.28x faster                                                         |
| float                    | 61.7 ms                                                     | 48.3 ms: 1.28x faster                                                          |
| nbody                    | 71.3 ms                                                     | 56.2 ms: 1.27x faster                                                          |
| unpickle_pure_python     | 183 us                                                      | 147 us: 1.24x faster                                                           |
| dulwich_log              | 50.5 ms                                                     | 40.6 ms: 1.24x faster                                                          |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.20 ms: 1.24x faster                                                          |
| richards                 | 42.4 ms                                                     | 34.2 ms: 1.24x faster                                                          |
| pylint                   | 350 ms                                                      | 283 ms: 1.24x faster                                                           |
| sqlglot_transpile        | 1.48 ms                                                     | 1.20 ms: 1.23x faster                                                          |
| xml_etree_process        | 44.5 ms                                                     | 36.7 ms: 1.21x faster                                                          |
| regex_dna                | 136 ms                                                      | 115 ms: 1.18x faster                                                           |
| thrift                   | 617 us                                                      | 525 us: 1.18x faster                                                           |
| deepcopy_reduce          | 2.20 us                                                     | 1.92 us: 1.15x faster                                                          |
| scimark_fft              | 187 ms                                                      | 163 ms: 1.15x faster                                                           |
| regex_compile            | 106 ms                                                      | 92.5 ms: 1.15x faster                                                          |
| coroutines               | 16.0 ms                                                     | 14.0 ms: 1.14x faster                                                          |
| bench_thread_pool        | 958 us                                                      | 849 us: 1.13x faster                                                           |
| mdp                      | 1.78 sec                                                    | 1.62 sec: 1.10x faster                                                         |
| fannkuch                 | 256 ms                                                      | 234 ms: 1.09x faster                                                           |
| tornado_http             | 108 ms                                                      | 99.0 ms: 1.09x faster                                                          |
| hexiom                   | 5.74 ms                                                     | 5.33 ms: 1.08x faster                                                          |
| xml_etree_generate       | 55.5 ms                                                     | 51.7 ms: 1.07x faster                                                          |
| django_template          | 28.9 ms                                                     | 27.0 ms: 1.07x faster                                                          |
| regex_effbot             | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                                          |
| regex_v8                 | 15.4 ms                                                     | 14.7 ms: 1.05x faster                                                          |
| nqueens                  | 66.6 ms                                                     | 63.7 ms: 1.05x faster                                                          |
| json                     | 3.14 ms                                                     | 3.01 ms: 1.04x faster                                                          |
| sympy_sum                | 107 ms                                                      | 104 ms: 1.03x faster                                                           |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.8 ms: 1.02x faster                                                          |
| xml_etree_parse          | 96.8 ms                                                     | 95.8 ms: 1.01x faster                                                          |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                                           |
| docutils                 | 1.92 sec                                                    | 1.93 sec: 1.01x slower                                                         |
| 2to3                     | 246 ms                                                      | 248 ms: 1.01x slower                                                           |
| sympy_integrate          | 15.3 ms                                                     | 15.7 ms: 1.02x slower                                                          |
| sqlglot_normalize        | 205 ms                                                      | 211 ms: 1.03x slower                                                           |
| sympy_expand             | 314 ms                                                      | 325 ms: 1.03x slower                                                           |
| json_loads               | 14.0 us                                                     | 14.6 us: 1.04x slower                                                          |
| pathlib                  | 75.7 ms                                                     | 80.9 ms: 1.07x slower                                                          |
| sqlglot_optimize         | 39.8 ms                                                     | 43.7 ms: 1.10x slower                                                          |
| genshi_xml               | 41.0 ms                                                     | 46.8 ms: 1.14x slower                                                          |
| python_startup           | 20.6 ms                                                     | 24.4 ms: 1.18x slower                                                          |
| python_startup_no_site   | 15.5 ms                                                     | 18.4 ms: 1.19x slower                                                          |
| telco                    | 3.94 ms                                                     | 4.77 ms: 1.21x slower                                                          |
| coverage                 | 39.0 ms                                                     | 47.2 ms: 1.21x slower                                                          |
| async_generators         | 222 ms                                                      | 270 ms: 1.22x slower                                                           |
| gc_traversal             | 1.41 ms                                                     | 1.97 ms: 1.40x slower                                                          |
| bench_mp_pool            | 62.0 ms                                                     | 89.6 ms: 1.44x slower                                                          |
| create_gc_cycles         | 800 us                                                      | 1.39 ms: 1.73x slower                                                          |
| Geometric mean           | (ref)                                                       | 1.18x faster                                                                   |

Benchmark hidden because not significant (5): genshi_text, logging_format, sympy_str, meteor_contest, logging_simple
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20241025-3.14.0a1+-64b198a-JIT/bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx

- Geometric mean (including insignificant results): 1.185x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown