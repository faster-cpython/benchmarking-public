# Results vs. 3.10.4

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-x86
- commit hash: 2fa7b0e
- commit date: 2024-09-04
- overall geometric mean: 1.13x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 251 ms: 1.06x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.86 sec: 1.05x faster                                                         |
| html5lib       | 52.1 ms                                                         | 46.5 ms: 1.12x faster                                                          |
| tornado_http   | 118 ms                                                          | 105 ms: 1.12x faster                                                           |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 460 ms: 2.00x faster                                                           |
| async_tree_none         | 394 ms                                                          | 217 ms: 1.81x faster                                                           |
| async_tree_io           | 940 ms                                                          | 537 ms: 1.75x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 273 ms: 1.71x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.82x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 201 ms: 2.50x faster                                                           |
| float          | 69.6 ms                                                         | 60.8 ms: 1.15x faster                                                          |
| nbody          | 79.1 ms                                                         | 96.8 ms: 1.22x slower                                                          |
| Geometric mean | (ref)                                                           | 1.33x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 107 ms: 1.09x faster                                                           |
| regex_dna      | 131 ms                                                          | 123 ms: 1.06x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 16.3 ms: 1.03x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.93 ms: 1.16x slower                                                          |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.42 ms: 1.32x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 108 ms: 1.11x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 171 us: 1.11x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 254 us: 1.10x faster                                                           |
| json_loads           | 22.4 us                                                         | 20.4 us: 1.10x faster                                                          |
| xml_etree_iterparse  | 70.8 ms                                                         | 67.9 ms: 1.04x faster                                                          |
| tomli_loads          | 1.91 sec                                                        | 1.89 sec: 1.01x faster                                                         |
| xml_etree_process    | 48.1 ms                                                         | 49.3 ms: 1.02x slower                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 67.9 ms: 1.10x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.07x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 24.2 ms: 1.05x slower                                                          |
| python_startup_no_site | 18.1 ms                                                         | 20.0 ms: 1.11x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 32.3 ms: 1.11x faster                                                          |
| mako            | 9.10 ms                                                         | 8.38 ms: 1.09x faster                                                          |
| genshi_text     | 21.0 ms                                                         | 21.6 ms: 1.03x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.04x faster                                                                   |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 151 us: 2.63x faster                                                           |
| pidigits                 | 502 ms                                                          | 201 ms: 2.50x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 460 ms: 2.00x faster                                                           |
| async_tree_none          | 394 ms                                                          | 217 ms: 1.81x faster                                                           |
| async_tree_io            | 940 ms                                                          | 537 ms: 1.75x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 273 ms: 1.71x faster                                                           |
| pylint                   | 384 ms                                                          | 235 ms: 1.63x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.64 ms: 1.53x faster                                                          |
| go                       | 146 ms                                                          | 102 ms: 1.43x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 57.8 ms: 1.41x faster                                                          |
| chaos                    | 74.4 ms                                                         | 54.6 ms: 1.36x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 7.42 ms: 1.32x faster                                                          |
| deepcopy_memo            | 29.6 us                                                         | 22.5 us: 1.32x faster                                                          |
| comprehensions           | 17.7 us                                                         | 13.5 us: 1.31x faster                                                          |
| logging_silent           | 97.9 ns                                                         | 74.7 ns: 1.31x faster                                                          |
| raytrace                 | 303 ms                                                          | 236 ms: 1.28x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 70.2 ms: 1.28x faster                                                          |
| deepcopy                 | 310 us                                                          | 247 us: 1.25x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 1.08 ms: 1.23x faster                                                          |
| thrift                   | 902 us                                                          | 735 us: 1.23x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.33 ms: 1.19x faster                                                          |
| pycparser                | 1.04 sec                                                        | 878 ms: 1.19x faster                                                           |
| pyflate                  | 422 ms                                                          | 357 ms: 1.18x faster                                                           |
| dulwich_log              | 58.5 ms                                                         | 49.7 ms: 1.18x faster                                                          |
| scimark_sor              | 115 ms                                                          | 98.5 ms: 1.17x faster                                                          |
| hexiom                   | 6.13 ms                                                         | 5.27 ms: 1.16x faster                                                          |
| richards_super           | 49.9 ms                                                         | 43.3 ms: 1.15x faster                                                          |
| nqueens                  | 87.1 ms                                                         | 76.1 ms: 1.15x faster                                                          |
| float                    | 69.6 ms                                                         | 60.8 ms: 1.15x faster                                                          |
| sympy_sum                | 122 ms                                                          | 107 ms: 1.14x faster                                                           |
| generators               | 31.6 ms                                                         | 27.7 ms: 1.14x faster                                                          |
| json                     | 4.76 ms                                                         | 4.19 ms: 1.14x faster                                                          |
| scimark_monte_carlo      | 61.9 ms                                                         | 55.0 ms: 1.13x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 46.5 ms: 1.12x faster                                                          |
| tornado_http             | 118 ms                                                          | 105 ms: 1.12x faster                                                           |
| django_template          | 36.0 ms                                                         | 32.3 ms: 1.11x faster                                                          |
| xml_etree_parse          | 120 ms                                                          | 108 ms: 1.11x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 171 us: 1.11x faster                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.43 us: 1.10x faster                                                          |
| pickle_pure_python       | 280 us                                                          | 254 us: 1.10x faster                                                           |
| json_loads               | 22.4 us                                                         | 20.4 us: 1.10x faster                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 1.03 ms: 1.09x faster                                                          |
| regex_compile            | 117 ms                                                          | 107 ms: 1.09x faster                                                           |
| mako                     | 9.10 ms                                                         | 8.38 ms: 1.09x faster                                                          |
| sympy_integrate          | 16.6 ms                                                         | 15.5 ms: 1.07x faster                                                          |
| mdp                      | 1.83 sec                                                        | 1.70 sec: 1.07x faster                                                         |
| regex_dna                | 131 ms                                                          | 123 ms: 1.06x faster                                                           |
| sympy_str                | 229 ms                                                          | 217 ms: 1.06x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 75.8 ms: 1.06x faster                                                          |
| 2to3                     | 265 ms                                                          | 251 ms: 1.06x faster                                                           |
| docutils                 | 1.95 sec                                                        | 1.86 sec: 1.05x faster                                                         |
| richards                 | 40.3 ms                                                         | 38.5 ms: 1.05x faster                                                          |
| sqlglot_optimize         | 44.7 ms                                                         | 42.8 ms: 1.05x faster                                                          |
| xml_etree_iterparse      | 70.8 ms                                                         | 67.9 ms: 1.04x faster                                                          |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.12 ms: 1.04x faster                                                          |
| sqlglot_normalize        | 230 ms                                                          | 223 ms: 1.03x faster                                                           |
| sympy_expand             | 391 ms                                                          | 379 ms: 1.03x faster                                                           |
| coroutines               | 17.9 ms                                                         | 17.5 ms: 1.02x faster                                                          |
| pprint_pformat           | 1.37 sec                                                        | 1.34 sec: 1.02x faster                                                         |
| tomli_loads              | 1.91 sec                                                        | 1.89 sec: 1.01x faster                                                         |
| pprint_safe_repr         | 658 ms                                                          | 651 ms: 1.01x faster                                                           |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.1 sec: 1.01x slower                                                         |
| xml_etree_process        | 48.1 ms                                                         | 49.3 ms: 1.02x slower                                                          |
| meteor_contest           | 80.0 ms                                                         | 82.2 ms: 1.03x slower                                                          |
| genshi_text              | 21.0 ms                                                         | 21.6 ms: 1.03x slower                                                          |
| regex_v8                 | 15.8 ms                                                         | 16.3 ms: 1.03x slower                                                          |
| fannkuch                 | 317 ms                                                          | 328 ms: 1.03x slower                                                           |
| python_startup           | 22.9 ms                                                         | 24.2 ms: 1.05x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 87.8 ms: 1.08x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.55 us: 1.08x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 751 us: 1.08x slower                                                           |
| logging_simple           | 7.29 us                                                         | 7.92 us: 1.09x slower                                                          |
| xml_etree_generate       | 61.6 ms                                                         | 67.9 ms: 1.10x slower                                                          |
| coverage                 | 46.6 ms                                                         | 51.5 ms: 1.11x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.42 ms: 1.11x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 20.0 ms: 1.11x slower                                                          |
| scimark_fft              | 216 ms                                                          | 241 ms: 1.12x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 74.9 ms: 1.13x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.93 ms: 1.16x slower                                                          |
| nbody                    | 79.1 ms                                                         | 96.8 ms: 1.22x slower                                                          |
| async_generators         | 241 ms                                                          | 299 ms: 1.24x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.92 ms: 1.43x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.13x faster                                                                   |

Benchmark hidden because not significant (2): genshi_xml, asyncio_tcp
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240904-3.14.0a0-2fa7b0e/bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown