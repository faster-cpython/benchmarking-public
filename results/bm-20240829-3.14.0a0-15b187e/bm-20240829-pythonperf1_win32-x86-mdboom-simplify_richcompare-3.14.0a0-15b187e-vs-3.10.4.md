# Results vs. 3.10.4

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-x86
- commit hash: 15b187e
- commit date: 2024-08-29
- overall geometric mean: 1.12x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 251 ms: 1.06x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.86 sec: 1.05x faster                                                         |
| html5lib       | 52.1 ms                                                         | 46.5 ms: 1.12x faster                                                          |
| tornado_http   | 118 ms                                                          | 105 ms: 1.12x faster                                                           |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 465 ms: 1.98x faster                                                           |
| async_tree_none         | 394 ms                                                          | 215 ms: 1.83x faster                                                           |
| async_tree_io           | 940 ms                                                          | 539 ms: 1.74x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 276 ms: 1.69x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.81x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 202 ms: 2.49x faster                                                           |
| float          | 69.6 ms                                                         | 62.0 ms: 1.12x faster                                                          |
| nbody          | 79.1 ms                                                         | 95.8 ms: 1.21x slower                                                          |
| Geometric mean | (ref)                                                           | 1.32x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 107 ms: 1.09x faster                                                           |
| regex_dna      | 131 ms                                                          | 122 ms: 1.07x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 16.2 ms: 1.03x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.94 ms: 1.17x slower                                                          |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.74 ms: 1.27x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 107 ms: 1.12x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 254 us: 1.10x faster                                                           |
| json_loads           | 22.4 us                                                         | 20.4 us: 1.10x faster                                                          |
| unpickle_pure_python | 189 us                                                          | 179 us: 1.06x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 67.9 ms: 1.04x faster                                                          |
| tomli_loads          | 1.91 sec                                                        | 1.86 sec: 1.03x faster                                                         |
| xml_etree_process    | 48.1 ms                                                         | 51.0 ms: 1.06x slower                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 68.4 ms: 1.11x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.06x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 24.1 ms: 1.05x slower                                                          |
| python_startup_no_site | 18.1 ms                                                         | 19.7 ms: 1.09x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.07x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 32.8 ms: 1.10x faster                                                          |
| mako            | 9.10 ms                                                         | 8.41 ms: 1.08x faster                                                          |
| genshi_text     | 21.0 ms                                                         | 21.8 ms: 1.04x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.03x faster                                                                   |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 148 us: 2.68x faster                                                           |
| pidigits                 | 502 ms                                                          | 202 ms: 2.49x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 465 ms: 1.98x faster                                                           |
| async_tree_none          | 394 ms                                                          | 215 ms: 1.83x faster                                                           |
| async_tree_io            | 940 ms                                                          | 539 ms: 1.74x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 276 ms: 1.69x faster                                                           |
| pylint                   | 384 ms                                                          | 233 ms: 1.65x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.72 ms: 1.48x faster                                                          |
| go                       | 146 ms                                                          | 103 ms: 1.42x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 58.2 ms: 1.40x faster                                                          |
| chaos                    | 74.4 ms                                                         | 53.5 ms: 1.39x faster                                                          |
| deepcopy_memo            | 29.6 us                                                         | 22.0 us: 1.34x faster                                                          |
| logging_silent           | 97.9 ns                                                         | 74.5 ns: 1.31x faster                                                          |
| comprehensions           | 17.7 us                                                         | 13.5 us: 1.31x faster                                                          |
| raytrace                 | 303 ms                                                          | 236 ms: 1.28x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 70.6 ms: 1.27x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 7.74 ms: 1.27x faster                                                          |
| deepcopy                 | 310 us                                                          | 246 us: 1.26x faster                                                           |
| thrift                   | 902 us                                                          | 727 us: 1.24x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 1.07 ms: 1.24x faster                                                          |
| pycparser                | 1.04 sec                                                        | 857 ms: 1.22x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.32 ms: 1.20x faster                                                          |
| pyflate                  | 422 ms                                                          | 358 ms: 1.18x faster                                                           |
| dulwich_log              | 58.5 ms                                                         | 50.0 ms: 1.17x faster                                                          |
| hexiom                   | 6.13 ms                                                         | 5.29 ms: 1.16x faster                                                          |
| nqueens                  | 87.1 ms                                                         | 75.9 ms: 1.15x faster                                                          |
| sympy_sum                | 122 ms                                                          | 107 ms: 1.14x faster                                                           |
| generators               | 31.6 ms                                                         | 27.9 ms: 1.13x faster                                                          |
| scimark_sor              | 115 ms                                                          | 102 ms: 1.12x faster                                                           |
| tornado_http             | 118 ms                                                          | 105 ms: 1.12x faster                                                           |
| float                    | 69.6 ms                                                         | 62.0 ms: 1.12x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 46.5 ms: 1.12x faster                                                          |
| xml_etree_parse          | 120 ms                                                          | 107 ms: 1.12x faster                                                           |
| json                     | 4.76 ms                                                         | 4.27 ms: 1.12x faster                                                          |
| richards_super           | 49.9 ms                                                         | 44.8 ms: 1.11x faster                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 1.01 ms: 1.11x faster                                                          |
| pickle_pure_python       | 280 us                                                          | 254 us: 1.10x faster                                                           |
| django_template          | 36.0 ms                                                         | 32.8 ms: 1.10x faster                                                          |
| json_loads               | 22.4 us                                                         | 20.4 us: 1.10x faster                                                          |
| regex_compile            | 117 ms                                                          | 107 ms: 1.09x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 56.6 ms: 1.09x faster                                                          |
| sympy_integrate          | 16.6 ms                                                         | 15.3 ms: 1.09x faster                                                          |
| mako                     | 9.10 ms                                                         | 8.41 ms: 1.08x faster                                                          |
| mdp                      | 1.83 sec                                                        | 1.70 sec: 1.07x faster                                                         |
| regex_dna                | 131 ms                                                          | 122 ms: 1.07x faster                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.51 us: 1.07x faster                                                          |
| spectral_norm            | 80.2 ms                                                         | 75.6 ms: 1.06x faster                                                          |
| unpickle_pure_python     | 189 us                                                          | 179 us: 1.06x faster                                                           |
| sympy_str                | 229 ms                                                          | 216 ms: 1.06x faster                                                           |
| 2to3                     | 265 ms                                                          | 251 ms: 1.06x faster                                                           |
| docutils                 | 1.95 sec                                                        | 1.86 sec: 1.05x faster                                                         |
| xml_etree_iterparse      | 70.8 ms                                                         | 67.9 ms: 1.04x faster                                                          |
| sqlglot_normalize        | 230 ms                                                          | 223 ms: 1.03x faster                                                           |
| richards                 | 40.3 ms                                                         | 39.0 ms: 1.03x faster                                                          |
| sqlglot_optimize         | 44.7 ms                                                         | 43.5 ms: 1.03x faster                                                          |
| tomli_loads              | 1.91 sec                                                        | 1.86 sec: 1.03x faster                                                         |
| pprint_pformat           | 1.37 sec                                                        | 1.33 sec: 1.03x faster                                                         |
| sympy_expand             | 391 ms                                                          | 381 ms: 1.02x faster                                                           |
| coroutines               | 17.9 ms                                                         | 17.5 ms: 1.02x faster                                                          |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.19 ms: 1.01x faster                                                          |
| regex_v8                 | 15.8 ms                                                         | 16.2 ms: 1.03x slower                                                          |
| genshi_text              | 21.0 ms                                                         | 21.8 ms: 1.04x slower                                                          |
| fannkuch                 | 317 ms                                                          | 332 ms: 1.05x slower                                                           |
| python_startup           | 22.9 ms                                                         | 24.1 ms: 1.05x slower                                                          |
| xml_etree_process        | 48.1 ms                                                         | 51.0 ms: 1.06x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 86.9 ms: 1.07x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 751 us: 1.08x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 19.7 ms: 1.09x slower                                                          |
| scimark_fft              | 216 ms                                                          | 237 ms: 1.09x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 72.8 ms: 1.10x slower                                                          |
| logging_simple           | 7.29 us                                                         | 8.02 us: 1.10x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.78 us: 1.11x slower                                                          |
| xml_etree_generate       | 61.6 ms                                                         | 68.4 ms: 1.11x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.44 ms: 1.12x slower                                                          |
| coverage                 | 46.6 ms                                                         | 54.0 ms: 1.16x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.94 ms: 1.17x slower                                                          |
| nbody                    | 79.1 ms                                                         | 95.8 ms: 1.21x slower                                                          |
| async_generators         | 241 ms                                                          | 307 ms: 1.27x slower                                                           |
| telco                    | 4.83 ms                                                         | 7.08 ms: 1.47x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.12x faster                                                                   |

Benchmark hidden because not significant (5): pprint_safe_repr, meteor_contest, asyncio_tcp_ssl, genshi_xml, asyncio_tcp
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240829-3.14.0a0-15b187e/bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown