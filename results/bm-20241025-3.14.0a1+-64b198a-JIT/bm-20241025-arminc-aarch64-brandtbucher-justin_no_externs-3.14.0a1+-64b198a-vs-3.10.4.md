# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_no_externs
- machine: linux-aarch64
- commit hash: 64b198a
- commit date: 2024-10-25
- overall geometric mean: 1.155x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.37x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 390 ms: 1.02x slower                                                        |
| docutils       | 3.53 sec                                                              | 3.62 sec: 1.03x slower                                                      |
| html5lib       | 86.5 ms                                                               | 71.6 ms: 1.21x faster                                                       |
| tornado_http   | 178 ms                                                                | 148 ms: 1.21x faster                                                        |
| Geometric mean | (ref)                                                                 | 1.08x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 469 ms: 2.03x faster                                                        |
| async_tree_io           | 2.28 sec                                                              | 1.17 sec: 1.95x faster                                                      |
| async_tree_memoization  | 1.13 sec                                                              | 608 ms: 1.87x faster                                                        |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 758 ms: 1.68x faster                                                        |
| Geometric mean          | (ref)                                                                 | 1.88x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 117 ms: 1.42x faster                                                        |
| float          | 135 ms                                                                | 95.9 ms: 1.41x faster                                                       |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 30.7 ms: 1.05x faster                                                       |
| regex_dna      | 257 ms                                                                | 251 ms: 1.02x faster                                                        |
| regex_effbot   | 4.25 ms                                                               | 4.93 ms: 1.16x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 268 us: 1.37x faster                                                        |
| pickle_pure_python   | 529 us                                                                | 394 us: 1.34x faster                                                        |
| tomli_loads          | 3.36 sec                                                              | 2.71 sec: 1.24x faster                                                      |
| xml_etree_process    | 99.5 ms                                                               | 81.6 ms: 1.22x faster                                                       |
| json_dumps           | 16.7 ms                                                               | 14.2 ms: 1.17x faster                                                       |
| xml_etree_parse      | 212 ms                                                                | 192 ms: 1.10x faster                                                        |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.09x faster                                                        |
| xml_etree_iterparse  | 156 ms                                                                | 151 ms: 1.04x faster                                                        |
| json_loads           | 30.9 us                                                               | 31.8 us: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                                 | 1.16x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.78 ms: 1.27x slower                                                       |
| python_startup         | 11.2 ms                                                               | 14.6 ms: 1.31x slower                                                       |
| Geometric mean         | (ref)                                                                 | 1.29x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako           | 18.9 ms                                                               | 13.3 ms: 1.42x faster                                                       |
| genshi_text    | 35.2 ms                                                               | 34.0 ms: 1.03x faster                                                       |
| genshi_xml     | 69.8 ms                                                               | 84.8 ms: 1.21x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.05x faster                                                                |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 215 us: 3.08x faster                                                        |
| async_tree_none          | 950 ms                                                                | 469 ms: 2.03x faster                                                        |
| deltablue                | 8.94 ms                                                               | 4.51 ms: 1.98x faster                                                       |
| async_tree_io            | 2.28 sec                                                              | 1.17 sec: 1.95x faster                                                      |
| async_tree_memoization   | 1.13 sec                                                              | 608 ms: 1.87x faster                                                        |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 758 ms: 1.68x faster                                                        |
| raytrace                 | 573 ms                                                                | 357 ms: 1.61x faster                                                        |
| deepcopy_memo            | 61.7 us                                                               | 39.6 us: 1.56x faster                                                       |
| scimark_sor              | 246 ms                                                                | 161 ms: 1.53x faster                                                        |
| logging_silent           | 222 ns                                                                | 149 ns: 1.49x faster                                                        |
| scimark_lu               | 227 ms                                                                | 152 ms: 1.49x faster                                                        |
| crypto_pyaes             | 134 ms                                                                | 91.2 ms: 1.47x faster                                                       |
| richards_super           | 107 ms                                                                | 74.4 ms: 1.44x faster                                                       |
| nbody                    | 166 ms                                                                | 117 ms: 1.42x faster                                                        |
| mako                     | 18.9 ms                                                               | 13.3 ms: 1.42x faster                                                       |
| float                    | 135 ms                                                                | 95.9 ms: 1.41x faster                                                       |
| go                       | 264 ms                                                                | 189 ms: 1.40x faster                                                        |
| sqlglot_parse            | 2.40 ms                                                               | 1.75 ms: 1.38x faster                                                       |
| unpickle_pure_python     | 366 us                                                                | 268 us: 1.37x faster                                                        |
| scimark_monte_carlo      | 128 ms                                                                | 94.3 ms: 1.36x faster                                                       |
| chaos                    | 121 ms                                                                | 89.8 ms: 1.35x faster                                                       |
| pickle_pure_python       | 529 us                                                                | 394 us: 1.34x faster                                                        |
| deepcopy                 | 511 us                                                                | 386 us: 1.32x faster                                                        |
| logging_format           | 10.6 us                                                               | 8.04 us: 1.32x faster                                                       |
| logging_simple           | 9.78 us                                                               | 7.42 us: 1.32x faster                                                       |
| thrift                   | 1.26 ms                                                               | 965 us: 1.31x faster                                                        |
| comprehensions           | 33.1 us                                                               | 25.5 us: 1.30x faster                                                       |
| coroutines               | 37.2 ms                                                               | 28.8 ms: 1.29x faster                                                       |
| sqlglot_transpile        | 2.84 ms                                                               | 2.21 ms: 1.29x faster                                                       |
| richards                 | 91.7 ms                                                               | 71.9 ms: 1.27x faster                                                       |
| tomli_loads              | 3.36 sec                                                              | 2.71 sec: 1.24x faster                                                      |
| xml_etree_process        | 99.5 ms                                                               | 81.6 ms: 1.22x faster                                                       |
| pyflate                  | 795 ms                                                                | 652 ms: 1.22x faster                                                        |
| pathlib                  | 26.3 ms                                                               | 21.6 ms: 1.22x faster                                                       |
| html5lib                 | 86.5 ms                                                               | 71.6 ms: 1.21x faster                                                       |
| tornado_http             | 178 ms                                                                | 148 ms: 1.21x faster                                                        |
| json_dumps               | 16.7 ms                                                               | 14.2 ms: 1.17x faster                                                       |
| bench_thread_pool        | 1.59 ms                                                               | 1.36 ms: 1.17x faster                                                       |
| spectral_norm            | 186 ms                                                                | 161 ms: 1.16x faster                                                        |
| generators               | 68.1 ms                                                               | 59.1 ms: 1.15x faster                                                       |
| deepcopy_reduce          | 4.60 us                                                               | 4.03 us: 1.14x faster                                                       |
| pycparser                | 1.69 sec                                                              | 1.51 sec: 1.12x faster                                                      |
| sqlalchemy_imperative    | 20.5 ms                                                               | 18.4 ms: 1.12x faster                                                       |
| xml_etree_parse          | 212 ms                                                                | 192 ms: 1.10x faster                                                        |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.09x faster                                                        |
| scimark_fft              | 500 ms                                                                | 459 ms: 1.09x faster                                                        |
| pylint                   | 485 ms                                                                | 450 ms: 1.08x faster                                                        |
| sqlalchemy_declarative   | 197 ms                                                                | 187 ms: 1.06x faster                                                        |
| regex_v8                 | 32.2 ms                                                               | 30.7 ms: 1.05x faster                                                       |
| mdp                      | 3.70 sec                                                              | 3.53 sec: 1.05x faster                                                      |
| hexiom                   | 10.9 ms                                                               | 10.4 ms: 1.05x faster                                                       |
| fannkuch                 | 546 ms                                                                | 522 ms: 1.05x faster                                                        |
| json                     | 5.88 ms                                                               | 5.67 ms: 1.04x faster                                                       |
| xml_etree_iterparse      | 156 ms                                                                | 151 ms: 1.04x faster                                                        |
| genshi_text              | 35.2 ms                                                               | 34.0 ms: 1.03x faster                                                       |
| regex_dna                | 257 ms                                                                | 251 ms: 1.02x faster                                                        |
| meteor_contest           | 126 ms                                                                | 125 ms: 1.01x faster                                                        |
| asyncio_websockets       | 657 ms                                                                | 665 ms: 1.01x slower                                                        |
| 2to3                     | 381 ms                                                                | 390 ms: 1.02x slower                                                        |
| docutils                 | 3.53 sec                                                              | 3.62 sec: 1.03x slower                                                      |
| json_loads               | 30.9 us                                                               | 31.8 us: 1.03x slower                                                       |
| dulwich_log              | 73.5 ms                                                               | 78.4 ms: 1.07x slower                                                       |
| sqlglot_optimize         | 75.4 ms                                                               | 82.0 ms: 1.09x slower                                                       |
| sympy_str                | 329 ms                                                                | 359 ms: 1.09x slower                                                        |
| pprint_safe_repr         | 1.15 sec                                                              | 1.26 sec: 1.10x slower                                                      |
| sympy_expand             | 543 ms                                                                | 597 ms: 1.10x slower                                                        |
| nqueens                  | 117 ms                                                                | 130 ms: 1.10x slower                                                        |
| pprint_pformat           | 2.36 sec                                                              | 2.62 sec: 1.11x slower                                                      |
| sympy_integrate          | 26.5 ms                                                               | 29.6 ms: 1.11x slower                                                       |
| telco                    | 8.49 ms                                                               | 9.55 ms: 1.12x slower                                                       |
| async_generators         | 452 ms                                                                | 513 ms: 1.13x slower                                                        |
| regex_effbot             | 4.25 ms                                                               | 4.93 ms: 1.16x slower                                                       |
| sympy_sum                | 184 ms                                                                | 216 ms: 1.18x slower                                                        |
| coverage                 | 83.6 ms                                                               | 98.7 ms: 1.18x slower                                                       |
| genshi_xml               | 69.8 ms                                                               | 84.8 ms: 1.21x slower                                                       |
| python_startup_no_site   | 6.89 ms                                                               | 8.78 ms: 1.27x slower                                                       |
| python_startup           | 11.2 ms                                                               | 14.6 ms: 1.31x slower                                                       |
| gc_traversal             | 4.15 ms                                                               | 6.12 ms: 1.47x slower                                                       |
| create_gc_cycles         | 2.26 ms                                                               | 3.64 ms: 1.61x slower                                                       |
| bench_mp_pool            | 14.5 ms                                                               | 1.51 sec: 103.76x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.09x faster                                                                |

Benchmark hidden because not significant (5): scimark_sparse_mat_mult, django_template, pidigits, regex_compile, sqlglot_normalize
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241025-3.14.0a1+-64b198a-JIT/bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.155x faster
# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.37x