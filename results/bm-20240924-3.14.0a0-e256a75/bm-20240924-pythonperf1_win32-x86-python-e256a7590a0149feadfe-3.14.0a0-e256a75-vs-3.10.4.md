# Results vs. 3.10.4

- fork: python
- ref: e256a7590a0149feadfe
- machine: windows-x86
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.128x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 249 ms: 1.06x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.87 sec: 1.04x faster                                                         |
| html5lib       | 52.1 ms                                                         | 46.5 ms: 1.12x faster                                                          |
| tornado_http   | 118 ms                                                          | 94.9 ms: 1.24x faster                                                          |
| Geometric mean | (ref)                                                           | 1.11x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 464 ms: 1.99x faster                                                           |
| async_tree_none         | 394 ms                                                          | 218 ms: 1.80x faster                                                           |
| async_tree_io           | 940 ms                                                          | 534 ms: 1.76x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 273 ms: 1.71x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.81x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 197 ms: 2.55x faster                                                           |
| float          | 69.6 ms                                                         | 62.8 ms: 1.11x faster                                                          |
| nbody          | 79.1 ms                                                         | 93.0 ms: 1.18x slower                                                          |
| Geometric mean | (ref)                                                           | 1.34x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 121 ms: 1.08x faster                                                           |
| regex_compile  | 117 ms                                                          | 109 ms: 1.07x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 16.2 ms: 1.03x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.90 ms: 1.14x slower                                                          |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.68 ms: 1.28x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 107 ms: 1.12x faster                                                           |
| json_loads           | 22.4 us                                                         | 21.0 us: 1.07x faster                                                          |
| pickle_pure_python   | 280 us                                                          | 262 us: 1.07x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 67.5 ms: 1.05x faster                                                          |
| unpickle_pure_python | 189 us                                                          | 180 us: 1.05x faster                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.85 sec: 1.03x faster                                                         |
| pickle               | 7.83 us                                                         | 7.94 us: 1.01x slower                                                          |
| xml_etree_process    | 48.1 ms                                                         | 49.4 ms: 1.03x slower                                                          |
| pickle_list          | 3.22 us                                                         | 3.35 us: 1.04x slower                                                          |
| unpickle             | 9.82 us                                                         | 10.3 us: 1.04x slower                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 67.5 ms: 1.09x slower                                                          |
| pickle_dict          | 18.2 us                                                         | 20.6 us: 1.13x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.02x faster                                                                   |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 23.5 ms: 1.03x slower                                                          |
| python_startup_no_site | 18.1 ms                                                         | 19.4 ms: 1.08x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.05x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 8.16 ms: 1.12x faster                                                          |
| django_template | 36.0 ms                                                         | 33.6 ms: 1.07x faster                                                          |
| genshi_xml      | 46.6 ms                                                         | 50.3 ms: 1.08x slower                                                          |
| genshi_text     | 21.0 ms                                                         | 24.2 ms: 1.15x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.01x slower                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 143 us: 2.76x faster                                                           |
| pidigits                 | 502 ms                                                          | 197 ms: 2.55x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 464 ms: 1.99x faster                                                           |
| async_tree_none          | 394 ms                                                          | 218 ms: 1.80x faster                                                           |
| async_tree_io            | 940 ms                                                          | 534 ms: 1.76x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 273 ms: 1.71x faster                                                           |
| pylint                   | 384 ms                                                          | 232 ms: 1.65x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.67 ms: 1.51x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 57.2 ms: 1.42x faster                                                          |
| chaos                    | 74.4 ms                                                         | 54.3 ms: 1.37x faster                                                          |
| go                       | 146 ms                                                          | 107 ms: 1.36x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 74.6 ns: 1.31x faster                                                          |
| deepcopy_memo            | 29.6 us                                                         | 22.6 us: 1.31x faster                                                          |
| scimark_lu               | 89.8 ms                                                         | 68.7 ms: 1.31x faster                                                          |
| raytrace                 | 303 ms                                                          | 233 ms: 1.30x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 7.68 ms: 1.28x faster                                                          |
| comprehensions           | 17.7 us                                                         | 14.1 us: 1.26x faster                                                          |
| deepcopy                 | 310 us                                                          | 250 us: 1.24x faster                                                           |
| tornado_http             | 118 ms                                                          | 94.9 ms: 1.24x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 1.10 ms: 1.21x faster                                                          |
| generators               | 31.6 ms                                                         | 26.0 ms: 1.21x faster                                                          |
| thrift                   | 902 us                                                          | 746 us: 1.21x faster                                                           |
| pycparser                | 1.04 sec                                                        | 877 ms: 1.19x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 5.17 ms: 1.19x faster                                                          |
| sqlglot_transpile        | 1.58 ms                                                         | 1.35 ms: 1.18x faster                                                          |
| pyflate                  | 422 ms                                                          | 362 ms: 1.17x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.98 us: 1.16x faster                                                          |
| dulwich_log              | 58.5 ms                                                         | 51.2 ms: 1.14x faster                                                          |
| sympy_sum                | 122 ms                                                          | 107 ms: 1.14x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 77.3 ms: 1.13x faster                                                          |
| richards_super           | 49.9 ms                                                         | 44.3 ms: 1.13x faster                                                          |
| asyncio_tcp              | 744 ms                                                          | 662 ms: 1.12x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 998 us: 1.12x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 46.5 ms: 1.12x faster                                                          |
| xml_etree_parse          | 120 ms                                                          | 107 ms: 1.12x faster                                                           |
| mako                     | 9.10 ms                                                         | 8.16 ms: 1.12x faster                                                          |
| float                    | 69.6 ms                                                         | 62.8 ms: 1.11x faster                                                          |
| json                     | 4.76 ms                                                         | 4.32 ms: 1.10x faster                                                          |
| mdp                      | 1.83 sec                                                        | 1.66 sec: 1.10x faster                                                         |
| scimark_sor              | 115 ms                                                          | 105 ms: 1.10x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 56.9 ms: 1.09x faster                                                          |
| sympy_integrate          | 16.6 ms                                                         | 15.3 ms: 1.09x faster                                                          |
| regex_dna                | 131 ms                                                          | 121 ms: 1.08x faster                                                           |
| django_template          | 36.0 ms                                                         | 33.6 ms: 1.07x faster                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.50 us: 1.07x faster                                                          |
| regex_compile            | 117 ms                                                          | 109 ms: 1.07x faster                                                           |
| json_loads               | 22.4 us                                                         | 21.0 us: 1.07x faster                                                          |
| pickle_pure_python       | 280 us                                                          | 262 us: 1.07x faster                                                           |
| 2to3                     | 265 ms                                                          | 249 ms: 1.06x faster                                                           |
| sympy_str                | 229 ms                                                          | 216 ms: 1.06x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.06 ms: 1.06x faster                                                          |
| spectral_norm            | 80.2 ms                                                         | 75.9 ms: 1.06x faster                                                          |
| xml_etree_iterparse      | 70.8 ms                                                         | 67.5 ms: 1.05x faster                                                          |
| unpickle_pure_python     | 189 us                                                          | 180 us: 1.05x faster                                                           |
| docutils                 | 1.95 sec                                                        | 1.87 sec: 1.04x faster                                                         |
| tomli_loads              | 1.91 sec                                                        | 1.85 sec: 1.03x faster                                                         |
| sympy_expand             | 391 ms                                                          | 381 ms: 1.02x faster                                                           |
| richards                 | 40.3 ms                                                         | 39.4 ms: 1.02x faster                                                          |
| coroutines               | 17.9 ms                                                         | 18.0 ms: 1.01x slower                                                          |
| sqlglot_normalize        | 230 ms                                                          | 233 ms: 1.01x slower                                                           |
| pickle                   | 7.83 us                                                         | 7.94 us: 1.01x slower                                                          |
| meteor_contest           | 80.0 ms                                                         | 81.4 ms: 1.02x slower                                                          |
| pprint_pformat           | 1.37 sec                                                        | 1.40 sec: 1.02x slower                                                         |
| python_startup           | 22.9 ms                                                         | 23.5 ms: 1.03x slower                                                          |
| xml_etree_process        | 48.1 ms                                                         | 49.4 ms: 1.03x slower                                                          |
| regex_v8                 | 15.8 ms                                                         | 16.2 ms: 1.03x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 83.5 ms: 1.03x slower                                                          |
| pprint_safe_repr         | 658 ms                                                          | 684 ms: 1.04x slower                                                           |
| pickle_list              | 3.22 us                                                         | 3.35 us: 1.04x slower                                                          |
| unpickle                 | 9.82 us                                                         | 10.3 us: 1.04x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 727 us: 1.05x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 69.9 ms: 1.05x slower                                                          |
| fannkuch                 | 317 ms                                                          | 336 ms: 1.06x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 19.4 ms: 1.08x slower                                                          |
| genshi_xml               | 46.6 ms                                                         | 50.3 ms: 1.08x slower                                                          |
| logging_simple           | 7.29 us                                                         | 7.93 us: 1.09x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.66 us: 1.09x slower                                                          |
| xml_etree_generate       | 61.6 ms                                                         | 67.5 ms: 1.09x slower                                                          |
| scimark_fft              | 216 ms                                                          | 239 ms: 1.10x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.42 ms: 1.10x slower                                                          |
| pickle_dict              | 18.2 us                                                         | 20.6 us: 1.13x slower                                                          |
| unpack_sequence          | 40.0 ns                                                         | 45.3 ns: 1.13x slower                                                          |
| coverage                 | 46.6 ms                                                         | 53.2 ms: 1.14x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.90 ms: 1.14x slower                                                          |
| genshi_text              | 21.0 ms                                                         | 24.2 ms: 1.15x slower                                                          |
| nbody                    | 79.1 ms                                                         | 93.0 ms: 1.18x slower                                                          |
| async_generators         | 241 ms                                                          | 301 ms: 1.25x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.61 ms: 1.37x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.11x faster                                                                   |

Benchmark hidden because not significant (3): sqlglot_optimize, asyncio_tcp_ssl, unpickle_list
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240924-3.14.0a0-e256a75/bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.128x faster
# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown