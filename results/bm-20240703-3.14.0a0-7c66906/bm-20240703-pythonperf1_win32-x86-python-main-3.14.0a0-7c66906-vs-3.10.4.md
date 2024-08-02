# Results vs. 3.10.4

- fork: python
- ref: main
- machine: windows-x86
- commit hash: 7c66906
- commit date: 2024-07-03
- overall geometric mean: 1.15x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240703-pythonperf1_win32-x86-python-main-3.14.0a0-7c66906 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 249 ms: 1.07x faster                                           |
| docutils       | 1.95 sec                                                        | 1.87 sec: 1.04x faster                                         |
| html5lib       | 52.1 ms                                                         | 48.2 ms: 1.08x faster                                          |
| tornado_http   | 118 ms                                                          | 95.4 ms: 1.23x faster                                          |
| Geometric mean | (ref)                                                           | 1.10x faster                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240703-pythonperf1_win32-x86-python-main-3.14.0a0-7c66906 |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 463 ms: 1.99x faster                                           |
| async_tree_none         | 394 ms                                                          | 221 ms: 1.78x faster                                           |
| async_tree_io           | 940 ms                                                          | 536 ms: 1.76x faster                                           |
| async_tree_memoization  | 467 ms                                                          | 270 ms: 1.73x faster                                           |
| Geometric mean          | (ref)                                                           | 1.81x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240703-pythonperf1_win32-x86-python-main-3.14.0a0-7c66906 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 200 ms: 2.52x faster                                           |
| float          | 69.6 ms                                                         | 60.0 ms: 1.16x faster                                          |
| nbody          | 79.1 ms                                                         | 93.9 ms: 1.19x slower                                          |
| Geometric mean | (ref)                                                           | 1.35x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240703-pythonperf1_win32-x86-python-main-3.14.0a0-7c66906 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 106 ms: 1.10x faster                                           |
| regex_dna      | 131 ms                                                          | 119 ms: 1.10x faster                                           |
| regex_v8       | 15.8 ms                                                         | 15.9 ms: 1.01x slower                                          |
| regex_effbot   | 1.66 ms                                                         | 1.87 ms: 1.13x slower                                          |
| Geometric mean | (ref)                                                           | 1.02x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240703-pythonperf1_win32-x86-python-main-3.14.0a0-7c66906 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.93 ms: 1.42x faster                                          |
| pickle_pure_python   | 280 us                                                          | 245 us: 1.14x faster                                           |
| xml_etree_parse      | 120 ms                                                          | 105 ms: 1.14x faster                                           |
| unpickle_pure_python | 189 us                                                          | 170 us: 1.11x faster                                           |
| json_loads           | 22.4 us                                                         | 20.4 us: 1.10x faster                                          |
| tomli_loads          | 1.91 sec                                                        | 1.77 sec: 1.08x faster                                         |
| xml_etree_iterparse  | 70.8 ms                                                         | 67.1 ms: 1.06x faster                                          |
| xml_etree_process    | 48.1 ms                                                         | 49.8 ms: 1.04x slower                                          |
| xml_etree_generate   | 61.6 ms                                                         | 66.0 ms: 1.07x slower                                          |
| Geometric mean       | (ref)                                                           | 1.10x faster                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240703-pythonperf1_win32-x86-python-main-3.14.0a0-7c66906 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 23.1 ms: 1.01x slower                                          |
| python_startup_no_site | 18.1 ms                                                         | 19.0 ms: 1.05x slower                                          |
| Geometric mean         | (ref)                                                           | 1.03x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240703-pythonperf1_win32-x86-python-main-3.14.0a0-7c66906 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.93 ms: 1.15x faster                                          |
| django_template | 36.0 ms                                                         | 33.2 ms: 1.08x faster                                          |
| genshi_text     | 21.0 ms                                                         | 21.9 ms: 1.04x slower                                          |
| Geometric mean  | (ref)                                                           | 1.05x faster                                                   |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240703-pythonperf1_win32-x86-python-main-3.14.0a0-7c66906 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 151 us: 2.62x faster                                           |
| pidigits                 | 502 ms                                                          | 200 ms: 2.52x faster                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 463 ms: 1.99x faster                                           |
| async_tree_none          | 394 ms                                                          | 221 ms: 1.78x faster                                           |
| async_tree_io            | 940 ms                                                          | 536 ms: 1.76x faster                                           |
| async_tree_memoization   | 467 ms                                                          | 270 ms: 1.73x faster                                           |
| pylint                   | 384 ms                                                          | 228 ms: 1.69x faster                                           |
| deltablue                | 4.04 ms                                                         | 2.66 ms: 1.52x faster                                          |
| json_dumps               | 9.82 ms                                                         | 6.93 ms: 1.42x faster                                          |
| chaos                    | 74.4 ms                                                         | 52.6 ms: 1.41x faster                                          |
| crypto_pyaes             | 81.3 ms                                                         | 57.7 ms: 1.41x faster                                          |
| raytrace                 | 303 ms                                                          | 220 ms: 1.37x faster                                           |
| deepcopy_memo            | 29.6 us                                                         | 21.6 us: 1.37x faster                                          |
| logging_silent           | 97.9 ns                                                         | 74.2 ns: 1.32x faster                                          |
| scimark_lu               | 89.8 ms                                                         | 68.4 ms: 1.31x faster                                          |
| comprehensions           | 17.7 us                                                         | 13.6 us: 1.31x faster                                          |
| deepcopy                 | 310 us                                                          | 241 us: 1.28x faster                                           |
| go                       | 146 ms                                                          | 114 ms: 1.28x faster                                           |
| sqlglot_parse            | 1.33 ms                                                         | 1.04 ms: 1.28x faster                                          |
| pyflate                  | 422 ms                                                          | 338 ms: 1.25x faster                                           |
| pycparser                | 1.04 sec                                                        | 841 ms: 1.24x faster                                           |
| tornado_http             | 118 ms                                                          | 95.4 ms: 1.23x faster                                          |
| sqlglot_transpile        | 1.58 ms                                                         | 1.29 ms: 1.23x faster                                          |
| hexiom                   | 6.13 ms                                                         | 5.12 ms: 1.20x faster                                          |
| thrift                   | 902 us                                                          | 763 us: 1.18x faster                                           |
| richards_super           | 49.9 ms                                                         | 42.5 ms: 1.17x faster                                          |
| generators               | 31.6 ms                                                         | 27.0 ms: 1.17x faster                                          |
| scimark_sor              | 115 ms                                                          | 98.4 ms: 1.17x faster                                          |
| float                    | 69.6 ms                                                         | 60.0 ms: 1.16x faster                                          |
| bench_thread_pool        | 1.12 ms                                                         | 971 us: 1.15x faster                                           |
| nqueens                  | 87.1 ms                                                         | 75.5 ms: 1.15x faster                                          |
| json                     | 4.76 ms                                                         | 4.14 ms: 1.15x faster                                          |
| mako                     | 9.10 ms                                                         | 7.93 ms: 1.15x faster                                          |
| scimark_monte_carlo      | 61.9 ms                                                         | 54.0 ms: 1.15x faster                                          |
| pickle_pure_python       | 280 us                                                          | 245 us: 1.14x faster                                           |
| xml_etree_parse          | 120 ms                                                          | 105 ms: 1.14x faster                                           |
| sympy_sum                | 122 ms                                                          | 109 ms: 1.13x faster                                           |
| asyncio_tcp              | 744 ms                                                          | 661 ms: 1.12x faster                                           |
| unpickle_pure_python     | 189 us                                                          | 170 us: 1.11x faster                                           |
| regex_compile            | 117 ms                                                          | 106 ms: 1.10x faster                                           |
| regex_dna                | 131 ms                                                          | 119 ms: 1.10x faster                                           |
| json_loads               | 22.4 us                                                         | 20.4 us: 1.10x faster                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.45 us: 1.10x faster                                          |
| mdp                      | 1.83 sec                                                        | 1.68 sec: 1.09x faster                                         |
| richards                 | 40.3 ms                                                         | 37.1 ms: 1.08x faster                                          |
| django_template          | 36.0 ms                                                         | 33.2 ms: 1.08x faster                                          |
| tomli_loads              | 1.91 sec                                                        | 1.77 sec: 1.08x faster                                         |
| html5lib                 | 52.1 ms                                                         | 48.2 ms: 1.08x faster                                          |
| sympy_integrate          | 16.6 ms                                                         | 15.4 ms: 1.08x faster                                          |
| 2to3                     | 265 ms                                                          | 249 ms: 1.07x faster                                           |
| spectral_norm            | 80.2 ms                                                         | 75.3 ms: 1.06x faster                                          |
| xml_etree_iterparse      | 70.8 ms                                                         | 67.1 ms: 1.06x faster                                          |
| sympy_str                | 229 ms                                                          | 217 ms: 1.05x faster                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.30 sec: 1.05x faster                                         |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.10 ms: 1.04x faster                                          |
| docutils                 | 1.95 sec                                                        | 1.87 sec: 1.04x faster                                         |
| pprint_safe_repr         | 658 ms                                                          | 638 ms: 1.03x faster                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 43.7 ms: 1.02x faster                                          |
| coroutines               | 17.9 ms                                                         | 17.5 ms: 1.02x faster                                          |
| sympy_expand             | 391 ms                                                          | 383 ms: 1.02x faster                                           |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 16.8 sec: 1.01x faster                                         |
| sqlglot_normalize        | 230 ms                                                          | 228 ms: 1.01x faster                                           |
| meteor_contest           | 80.0 ms                                                         | 79.7 ms: 1.00x faster                                          |
| python_startup           | 22.9 ms                                                         | 23.1 ms: 1.01x slower                                          |
| regex_v8                 | 15.8 ms                                                         | 15.9 ms: 1.01x slower                                          |
| scimark_fft              | 216 ms                                                          | 220 ms: 1.02x slower                                           |
| pathlib                  | 81.2 ms                                                         | 83.5 ms: 1.03x slower                                          |
| xml_etree_process        | 48.1 ms                                                         | 49.8 ms: 1.04x slower                                          |
| genshi_text              | 21.0 ms                                                         | 21.9 ms: 1.04x slower                                          |
| python_startup_no_site   | 18.1 ms                                                         | 19.0 ms: 1.05x slower                                          |
| bench_mp_pool            | 66.4 ms                                                         | 70.4 ms: 1.06x slower                                          |
| xml_etree_generate       | 61.6 ms                                                         | 66.0 ms: 1.07x slower                                          |
| logging_simple           | 7.29 us                                                         | 7.82 us: 1.07x slower                                          |
| logging_format           | 7.91 us                                                         | 8.52 us: 1.08x slower                                          |
| create_gc_cycles         | 694 us                                                          | 753 us: 1.08x slower                                           |
| coverage                 | 46.6 ms                                                         | 51.3 ms: 1.10x slower                                          |
| gc_traversal             | 1.28 ms                                                         | 1.43 ms: 1.12x slower                                          |
| regex_effbot             | 1.66 ms                                                         | 1.87 ms: 1.13x slower                                          |
| nbody                    | 79.1 ms                                                         | 93.9 ms: 1.19x slower                                          |
| async_generators         | 241 ms                                                          | 287 ms: 1.19x slower                                           |
| telco                    | 4.83 ms                                                         | 6.02 ms: 1.25x slower                                          |
| Geometric mean           | (ref)                                                           | 1.15x faster                                                   |

Benchmark hidden because not significant (2): genshi_xml, fannkuch
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240703-3.14.0a0-7c66906/bm-20240703-pythonperf1_win32-x86-python-main-3.14.0a0-7c66906.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: unknown