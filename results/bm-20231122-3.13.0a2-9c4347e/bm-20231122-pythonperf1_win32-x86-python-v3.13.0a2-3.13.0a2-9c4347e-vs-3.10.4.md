# Results vs. 3.10.4

- fork: python
- ref: v3.13.0a2
- machine: windows-x86
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.09x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 246 ms: 1.08x faster                                                |
| chameleon      | 6.42 ms                                                         | 5.96 ms: 1.08x faster                                               |
| docutils       | 1.95 sec                                                        | 1.78 sec: 1.10x faster                                              |
| html5lib       | 52.1 ms                                                         | 45.7 ms: 1.14x faster                                               |
| tornado_http   | 118 ms                                                          | 98.2 ms: 1.20x faster                                               |
| Geometric mean | (ref)                                                           | 1.12x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 511 ms: 1.81x faster                                                |
| async_tree_none         | 394 ms                                                          | 254 ms: 1.55x faster                                                |
| async_tree_io           | 940 ms                                                          | 623 ms: 1.51x faster                                                |
| async_tree_memoization  | 467 ms                                                          | 317 ms: 1.47x faster                                                |
| Geometric mean          | (ref)                                                           | 1.58x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 200 ms: 2.51x faster                                                |
| float          | 69.6 ms                                                         | 59.8 ms: 1.16x faster                                               |
| nbody          | 79.1 ms                                                         | 88.9 ms: 1.12x slower                                               |
| Geometric mean | (ref)                                                           | 1.38x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 106 ms: 1.10x faster                                                |
| regex_dna      | 131 ms                                                          | 120 ms: 1.08x faster                                                |
| regex_v8       | 15.8 ms                                                         | 16.2 ms: 1.03x slower                                               |
| regex_effbot   | 1.66 ms                                                         | 1.92 ms: 1.15x slower                                               |
| Geometric mean | (ref)                                                           | 1.00x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.96 ms: 1.41x faster                                               |
| pickle_pure_python   | 280 us                                                          | 231 us: 1.22x faster                                                |
| unpickle_pure_python | 189 us                                                          | 156 us: 1.21x faster                                                |
| json_loads           | 22.4 us                                                         | 19.8 us: 1.13x faster                                               |
| xml_etree_parse      | 120 ms                                                          | 108 ms: 1.11x faster                                                |
| tomli_loads          | 1.91 sec                                                        | 1.81 sec: 1.06x faster                                              |
| xml_etree_process    | 48.1 ms                                                         | 45.8 ms: 1.05x faster                                               |
| pickle               | 7.83 us                                                         | 7.57 us: 1.03x faster                                               |
| unpickle             | 9.82 us                                                         | 9.58 us: 1.03x faster                                               |
| xml_etree_iterparse  | 70.8 ms                                                         | 69.5 ms: 1.02x faster                                               |
| unpickle_list        | 2.98 us                                                         | 2.94 us: 1.01x faster                                               |
| pickle_list          | 3.22 us                                                         | 3.17 us: 1.01x faster                                               |
| xml_etree_generate   | 61.6 ms                                                         | 62.8 ms: 1.02x slower                                               |
| pickle_dict          | 18.2 us                                                         | 19.8 us: 1.09x slower                                               |
| Geometric mean       | (ref)                                                           | 1.08x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 22.2 ms: 1.03x faster                                               |
| python_startup_no_site | 18.1 ms                                                         | 20.0 ms: 1.11x slower                                               |
| Geometric mean         | (ref)                                                           | 1.04x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.72 ms: 1.18x faster                                               |
| django_template | 36.0 ms                                                         | 31.2 ms: 1.16x faster                                               |
| genshi_text     | 21.0 ms                                                         | 21.7 ms: 1.03x slower                                               |
| genshi_xml      | 46.6 ms                                                         | 48.4 ms: 1.04x slower                                               |
| Geometric mean  | (ref)                                                           | 1.06x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 98.7 us: 4.01x faster                                               |
| pidigits                 | 502 ms                                                          | 200 ms: 2.51x faster                                                |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 511 ms: 1.81x faster                                                |
| pylint                   | 384 ms                                                          | 226 ms: 1.70x faster                                                |
| deltablue                | 4.04 ms                                                         | 2.55 ms: 1.58x faster                                               |
| async_tree_none          | 394 ms                                                          | 254 ms: 1.55x faster                                                |
| async_tree_io            | 940 ms                                                          | 623 ms: 1.51x faster                                                |
| async_tree_memoization   | 467 ms                                                          | 317 ms: 1.47x faster                                                |
| crypto_pyaes             | 81.3 ms                                                         | 55.4 ms: 1.47x faster                                               |
| chaos                    | 74.4 ms                                                         | 51.8 ms: 1.44x faster                                               |
| comprehensions           | 17.7 us                                                         | 12.6 us: 1.41x faster                                               |
| json_dumps               | 9.82 ms                                                         | 6.96 ms: 1.41x faster                                               |
| sqlglot_parse            | 1.33 ms                                                         | 953 us: 1.40x faster                                                |
| logging_silent           | 97.9 ns                                                         | 70.3 ns: 1.39x faster                                               |
| raytrace                 | 303 ms                                                          | 223 ms: 1.36x faster                                                |
| go                       | 146 ms                                                          | 108 ms: 1.35x faster                                                |
| sqlglot_transpile        | 1.58 ms                                                         | 1.21 ms: 1.31x faster                                               |
| richards_super           | 49.9 ms                                                         | 38.0 ms: 1.31x faster                                               |
| scimark_lu               | 89.8 ms                                                         | 69.0 ms: 1.30x faster                                               |
| pyflate                  | 422 ms                                                          | 335 ms: 1.26x faster                                                |
| sqlite_synth             | 2.29 us                                                         | 1.84 us: 1.25x faster                                               |
| hexiom                   | 6.13 ms                                                         | 4.97 ms: 1.23x faster                                               |
| scimark_monte_carlo      | 61.9 ms                                                         | 50.6 ms: 1.22x faster                                               |
| pickle_pure_python       | 280 us                                                          | 231 us: 1.22x faster                                                |
| unpickle_pure_python     | 189 us                                                          | 156 us: 1.21x faster                                                |
| pycparser                | 1.04 sec                                                        | 862 ms: 1.21x faster                                                |
| tornado_http             | 118 ms                                                          | 98.2 ms: 1.20x faster                                               |
| richards                 | 40.3 ms                                                         | 33.7 ms: 1.19x faster                                               |
| sympy_sum                | 122 ms                                                          | 104 ms: 1.18x faster                                                |
| mako                     | 9.10 ms                                                         | 7.72 ms: 1.18x faster                                               |
| scimark_sor              | 115 ms                                                          | 97.7 ms: 1.18x faster                                               |
| generators               | 31.6 ms                                                         | 27.0 ms: 1.17x faster                                               |
| float                    | 69.6 ms                                                         | 59.8 ms: 1.16x faster                                               |
| django_template          | 36.0 ms                                                         | 31.2 ms: 1.16x faster                                               |
| json                     | 4.76 ms                                                         | 4.14 ms: 1.15x faster                                               |
| html5lib                 | 52.1 ms                                                         | 45.7 ms: 1.14x faster                                               |
| asyncio_tcp              | 744 ms                                                          | 654 ms: 1.14x faster                                                |
| json_loads               | 22.4 us                                                         | 19.8 us: 1.13x faster                                               |
| sympy_integrate          | 16.6 ms                                                         | 14.9 ms: 1.12x faster                                               |
| xml_etree_parse          | 120 ms                                                          | 108 ms: 1.11x faster                                                |
| deepcopy_memo            | 29.6 us                                                         | 26.6 us: 1.11x faster                                               |
| sympy_str                | 229 ms                                                          | 207 ms: 1.10x faster                                                |
| regex_compile            | 117 ms                                                          | 106 ms: 1.10x faster                                                |
| docutils                 | 1.95 sec                                                        | 1.78 sec: 1.10x faster                                              |
| sqlglot_normalize        | 230 ms                                                          | 212 ms: 1.09x faster                                                |
| nqueens                  | 87.1 ms                                                         | 80.1 ms: 1.09x faster                                               |
| regex_dna                | 131 ms                                                          | 120 ms: 1.08x faster                                                |
| 2to3                     | 265 ms                                                          | 246 ms: 1.08x faster                                                |
| sympy_expand             | 391 ms                                                          | 362 ms: 1.08x faster                                                |
| chameleon                | 6.42 ms                                                         | 5.96 ms: 1.08x faster                                               |
| sqlglot_optimize         | 44.7 ms                                                         | 41.5 ms: 1.08x faster                                               |
| create_gc_cycles         | 694 us                                                          | 645 us: 1.08x faster                                                |
| pprint_pformat           | 1.37 sec                                                        | 1.28 sec: 1.07x faster                                              |
| mdp                      | 1.83 sec                                                        | 1.70 sec: 1.07x faster                                              |
| bench_thread_pool        | 1.12 ms                                                         | 1.05 ms: 1.07x faster                                               |
| coroutines               | 17.9 ms                                                         | 16.7 ms: 1.07x faster                                               |
| spectral_norm            | 80.2 ms                                                         | 75.0 ms: 1.07x faster                                               |
| pprint_safe_repr         | 658 ms                                                          | 621 ms: 1.06x faster                                                |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.07 ms: 1.06x faster                                               |
| tomli_loads              | 1.91 sec                                                        | 1.81 sec: 1.06x faster                                              |
| fannkuch                 | 317 ms                                                          | 302 ms: 1.05x faster                                                |
| xml_etree_process        | 48.1 ms                                                         | 45.8 ms: 1.05x faster                                               |
| deepcopy                 | 310 us                                                          | 295 us: 1.05x faster                                                |
| pickle                   | 7.83 us                                                         | 7.57 us: 1.03x faster                                               |
| python_startup           | 22.9 ms                                                         | 22.2 ms: 1.03x faster                                               |
| unpickle                 | 9.82 us                                                         | 9.58 us: 1.03x faster                                               |
| deepcopy_reduce          | 2.68 us                                                         | 2.63 us: 1.02x faster                                               |
| xml_etree_iterparse      | 70.8 ms                                                         | 69.5 ms: 1.02x faster                                               |
| unpickle_list            | 2.98 us                                                         | 2.94 us: 1.01x faster                                               |
| pickle_list              | 3.22 us                                                         | 3.17 us: 1.01x faster                                               |
| meteor_contest           | 80.0 ms                                                         | 80.4 ms: 1.00x slower                                               |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.2 sec: 1.02x slower                                              |
| scimark_fft              | 216 ms                                                          | 220 ms: 1.02x slower                                                |
| xml_etree_generate       | 61.6 ms                                                         | 62.8 ms: 1.02x slower                                               |
| regex_v8                 | 15.8 ms                                                         | 16.2 ms: 1.03x slower                                               |
| genshi_text              | 21.0 ms                                                         | 21.7 ms: 1.03x slower                                               |
| genshi_xml               | 46.6 ms                                                         | 48.4 ms: 1.04x slower                                               |
| bench_mp_pool            | 66.4 ms                                                         | 69.3 ms: 1.04x slower                                               |
| gc_traversal             | 1.28 ms                                                         | 1.39 ms: 1.08x slower                                               |
| pickle_dict              | 18.2 us                                                         | 19.8 us: 1.09x slower                                               |
| pathlib                  | 81.2 ms                                                         | 89.7 ms: 1.10x slower                                               |
| python_startup_no_site   | 18.1 ms                                                         | 20.0 ms: 1.11x slower                                               |
| nbody                    | 79.1 ms                                                         | 88.9 ms: 1.12x slower                                               |
| logging_format           | 7.91 us                                                         | 8.90 us: 1.13x slower                                               |
| logging_simple           | 7.29 us                                                         | 8.35 us: 1.15x slower                                               |
| async_generators         | 241 ms                                                          | 278 ms: 1.15x slower                                                |
| regex_effbot             | 1.66 ms                                                         | 1.92 ms: 1.15x slower                                               |
| telco                    | 4.83 ms                                                         | 6.08 ms: 1.26x slower                                               |
| coverage                 | 46.6 ms                                                         | 512 ms: 11.01x slower                                               |
| thrift                   | 902 us                                                          | 10.7 ms: 11.85x slower                                              |
| Geometric mean           | (ref)                                                           | 1.09x faster                                                        |

Benchmark hidden because not significant (1): flaskblogging
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: unknown