# Results vs. 3.10.4

- fork: python
- ref: a2bec77d25b11f50362a
- machine: windows-x86
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.15x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 249 ms: 1.07x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.87 sec: 1.04x faster                                                         |
| html5lib       | 52.1 ms                                                         | 48.6 ms: 1.07x faster                                                          |
| tornado_http   | 118 ms                                                          | 95.0 ms: 1.24x faster                                                          |
| Geometric mean | (ref)                                                           | 1.10x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 477 ms: 1.93x faster                                                           |
| async_tree_none         | 394 ms                                                          | 225 ms: 1.75x faster                                                           |
| async_tree_io           | 940 ms                                                          | 546 ms: 1.72x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 273 ms: 1.71x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.78x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 196 ms: 2.56x faster                                                           |
| float          | 69.6 ms                                                         | 58.9 ms: 1.18x faster                                                          |
| nbody          | 79.1 ms                                                         | 89.0 ms: 1.12x slower                                                          |
| Geometric mean | (ref)                                                           | 1.39x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 103 ms: 1.13x faster                                                           |
| regex_dna      | 131 ms                                                          | 124 ms: 1.06x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 16.0 ms: 1.01x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.92 ms: 1.15x slower                                                          |
| Geometric mean | (ref)                                                           | 1.00x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.14 ms: 1.38x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 105 ms: 1.14x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 167 us: 1.13x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 250 us: 1.12x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 66.0 ms: 1.07x faster                                                          |
| tomli_loads          | 1.91 sec                                                        | 1.79 sec: 1.06x faster                                                         |
| json_loads           | 22.4 us                                                         | 21.2 us: 1.06x faster                                                          |
| xml_etree_process    | 48.1 ms                                                         | 49.7 ms: 1.03x slower                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 68.3 ms: 1.11x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.09x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 18.9 ms: 1.05x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.02x slower                                                                   |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.95 ms: 1.15x faster                                                          |
| django_template | 36.0 ms                                                         | 33.3 ms: 1.08x faster                                                          |
| genshi_xml      | 46.6 ms                                                         | 46.3 ms: 1.01x faster                                                          |
| genshi_text     | 21.0 ms                                                         | 21.9 ms: 1.05x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.04x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 153 us: 2.59x faster                                                           |
| pidigits                 | 502 ms                                                          | 196 ms: 2.56x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 477 ms: 1.93x faster                                                           |
| async_tree_none          | 394 ms                                                          | 225 ms: 1.75x faster                                                           |
| async_tree_io            | 940 ms                                                          | 546 ms: 1.72x faster                                                           |
| pylint                   | 384 ms                                                          | 223 ms: 1.72x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 273 ms: 1.71x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.61 ms: 1.54x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 57.7 ms: 1.41x faster                                                          |
| raytrace                 | 303 ms                                                          | 215 ms: 1.41x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 21.4 us: 1.39x faster                                                          |
| chaos                    | 74.4 ms                                                         | 53.8 ms: 1.38x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 7.14 ms: 1.38x faster                                                          |
| scimark_lu               | 89.8 ms                                                         | 67.2 ms: 1.33x faster                                                          |
| comprehensions           | 17.7 us                                                         | 13.3 us: 1.33x faster                                                          |
| logging_silent           | 97.9 ns                                                         | 74.9 ns: 1.31x faster                                                          |
| deepcopy                 | 310 us                                                          | 241 us: 1.29x faster                                                           |
| go                       | 146 ms                                                          | 114 ms: 1.28x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 1.05 ms: 1.27x faster                                                          |
| pycparser                | 1.04 sec                                                        | 824 ms: 1.26x faster                                                           |
| pyflate                  | 422 ms                                                          | 335 ms: 1.26x faster                                                           |
| tornado_http             | 118 ms                                                          | 95.0 ms: 1.24x faster                                                          |
| sqlglot_transpile        | 1.58 ms                                                         | 1.28 ms: 1.23x faster                                                          |
| richards_super           | 49.9 ms                                                         | 40.7 ms: 1.23x faster                                                          |
| hexiom                   | 6.13 ms                                                         | 5.01 ms: 1.22x faster                                                          |
| scimark_sor              | 115 ms                                                          | 95.0 ms: 1.21x faster                                                          |
| nqueens                  | 87.1 ms                                                         | 73.1 ms: 1.19x faster                                                          |
| generators               | 31.6 ms                                                         | 26.6 ms: 1.18x faster                                                          |
| float                    | 69.6 ms                                                         | 58.9 ms: 1.18x faster                                                          |
| scimark_monte_carlo      | 61.9 ms                                                         | 52.4 ms: 1.18x faster                                                          |
| thrift                   | 902 us                                                          | 778 us: 1.16x faster                                                           |
| mako                     | 9.10 ms                                                         | 7.95 ms: 1.15x faster                                                          |
| asyncio_tcp              | 744 ms                                                          | 651 ms: 1.14x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 105 ms: 1.14x faster                                                           |
| sympy_sum                | 122 ms                                                          | 108 ms: 1.14x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 167 us: 1.13x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 990 us: 1.13x faster                                                           |
| regex_compile            | 117 ms                                                          | 103 ms: 1.13x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 250 us: 1.12x faster                                                           |
| richards                 | 40.3 ms                                                         | 36.8 ms: 1.09x faster                                                          |
| sympy_integrate          | 16.6 ms                                                         | 15.3 ms: 1.09x faster                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.47 us: 1.09x faster                                                          |
| mdp                      | 1.83 sec                                                        | 1.68 sec: 1.08x faster                                                         |
| django_template          | 36.0 ms                                                         | 33.3 ms: 1.08x faster                                                          |
| json                     | 4.76 ms                                                         | 4.41 ms: 1.08x faster                                                          |
| xml_etree_iterparse      | 70.8 ms                                                         | 66.0 ms: 1.07x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 48.6 ms: 1.07x faster                                                          |
| 2to3                     | 265 ms                                                          | 249 ms: 1.07x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.79 sec: 1.06x faster                                                         |
| spectral_norm            | 80.2 ms                                                         | 75.3 ms: 1.06x faster                                                          |
| regex_dna                | 131 ms                                                          | 124 ms: 1.06x faster                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.30 sec: 1.06x faster                                                         |
| json_loads               | 22.4 us                                                         | 21.2 us: 1.06x faster                                                          |
| sympy_str                | 229 ms                                                          | 218 ms: 1.05x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.09 ms: 1.05x faster                                                          |
| docutils                 | 1.95 sec                                                        | 1.87 sec: 1.04x faster                                                         |
| coroutines               | 17.9 ms                                                         | 17.2 ms: 1.04x faster                                                          |
| sqlglot_optimize         | 44.7 ms                                                         | 43.1 ms: 1.04x faster                                                          |
| pprint_safe_repr         | 658 ms                                                          | 634 ms: 1.04x faster                                                           |
| fannkuch                 | 317 ms                                                          | 309 ms: 1.03x faster                                                           |
| sympy_expand             | 391 ms                                                          | 381 ms: 1.03x faster                                                           |
| sqlglot_normalize        | 230 ms                                                          | 226 ms: 1.02x faster                                                           |
| meteor_contest           | 80.0 ms                                                         | 79.1 ms: 1.01x faster                                                          |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 16.8 sec: 1.01x faster                                                         |
| genshi_xml               | 46.6 ms                                                         | 46.3 ms: 1.01x faster                                                          |
| regex_v8                 | 15.8 ms                                                         | 16.0 ms: 1.01x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 82.2 ms: 1.01x slower                                                          |
| scimark_fft              | 216 ms                                                          | 220 ms: 1.02x slower                                                           |
| xml_etree_process        | 48.1 ms                                                         | 49.7 ms: 1.03x slower                                                          |
| genshi_text              | 21.0 ms                                                         | 21.9 ms: 1.05x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 18.9 ms: 1.05x slower                                                          |
| logging_simple           | 7.29 us                                                         | 7.74 us: 1.06x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 70.5 ms: 1.06x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.43 us: 1.07x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 748 us: 1.08x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 68.3 ms: 1.11x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.43 ms: 1.12x slower                                                          |
| nbody                    | 79.1 ms                                                         | 89.0 ms: 1.12x slower                                                          |
| coverage                 | 46.6 ms                                                         | 52.6 ms: 1.13x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.92 ms: 1.15x slower                                                          |
| async_generators         | 241 ms                                                          | 285 ms: 1.18x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.35 ms: 1.31x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.15x faster                                                                   |

Benchmark hidden because not significant (1): python_startup
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: unknown