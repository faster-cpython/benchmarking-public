# Results vs. 3.10.4

- fork: mdboom
- ref: pysequence_tuple
- machine: windows-x86
- commit hash: 3b5fdc8
- commit date: 2024-09-11
- overall geometric mean: 1.12x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 248 ms: 1.07x faster                                                       |
| docutils       | 1.95 sec                                                        | 1.86 sec: 1.05x faster                                                     |
| html5lib       | 52.1 ms                                                         | 45.7 ms: 1.14x faster                                                      |
| tornado_http   | 118 ms                                                          | 94.2 ms: 1.25x faster                                                      |
| Geometric mean | (ref)                                                           | 1.12x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 488 ms: 1.89x faster                                                       |
| async_tree_none         | 394 ms                                                          | 226 ms: 1.74x faster                                                       |
| async_tree_io           | 940 ms                                                          | 551 ms: 1.71x faster                                                       |
| async_tree_memoization  | 467 ms                                                          | 278 ms: 1.68x faster                                                       |
| Geometric mean          | (ref)                                                           | 1.75x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 197 ms: 2.55x faster                                                       |
| float          | 69.6 ms                                                         | 61.0 ms: 1.14x faster                                                      |
| nbody          | 79.1 ms                                                         | 91.4 ms: 1.16x slower                                                      |
| Geometric mean | (ref)                                                           | 1.36x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 117 ms: 1.11x faster                                                       |
| regex_compile  | 117 ms                                                          | 107 ms: 1.09x faster                                                       |
| regex_v8       | 15.8 ms                                                         | 16.4 ms: 1.04x slower                                                      |
| regex_effbot   | 1.66 ms                                                         | 1.91 ms: 1.15x slower                                                      |
| Geometric mean | (ref)                                                           | 1.00x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.70 ms: 1.28x faster                                                      |
| xml_etree_parse      | 120 ms                                                          | 107 ms: 1.12x faster                                                       |
| pickle_pure_python   | 280 us                                                          | 256 us: 1.10x faster                                                       |
| json_loads           | 22.4 us                                                         | 20.9 us: 1.07x faster                                                      |
| xml_etree_iterparse  | 70.8 ms                                                         | 66.8 ms: 1.06x faster                                                      |
| unpickle_pure_python | 189 us                                                          | 182 us: 1.04x faster                                                       |
| tomli_loads          | 1.91 sec                                                        | 1.85 sec: 1.03x faster                                                     |
| unpickle_list        | 2.98 us                                                         | 2.94 us: 1.02x faster                                                      |
| pickle               | 7.83 us                                                         | 7.94 us: 1.01x slower                                                      |
| pickle_list          | 3.22 us                                                         | 3.34 us: 1.04x slower                                                      |
| xml_etree_process    | 48.1 ms                                                         | 50.7 ms: 1.05x slower                                                      |
| unpickle             | 9.82 us                                                         | 10.5 us: 1.07x slower                                                      |
| pickle_dict          | 18.2 us                                                         | 20.3 us: 1.11x slower                                                      |
| xml_etree_generate   | 61.6 ms                                                         | 69.2 ms: 1.12x slower                                                      |
| Geometric mean       | (ref)                                                           | 1.02x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 23.6 ms: 1.03x slower                                                      |
| python_startup_no_site | 18.1 ms                                                         | 19.4 ms: 1.07x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.05x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 8.08 ms: 1.13x faster                                                      |
| django_template | 36.0 ms                                                         | 32.4 ms: 1.11x faster                                                      |
| genshi_xml      | 46.6 ms                                                         | 47.0 ms: 1.01x slower                                                      |
| genshi_text     | 21.0 ms                                                         | 22.2 ms: 1.06x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.04x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 141 us: 2.80x faster                                                       |
| pidigits                 | 502 ms                                                          | 197 ms: 2.55x faster                                                       |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 488 ms: 1.89x faster                                                       |
| async_tree_none          | 394 ms                                                          | 226 ms: 1.74x faster                                                       |
| async_tree_io            | 940 ms                                                          | 551 ms: 1.71x faster                                                       |
| async_tree_memoization   | 467 ms                                                          | 278 ms: 1.68x faster                                                       |
| pylint                   | 384 ms                                                          | 232 ms: 1.65x faster                                                       |
| deltablue                | 4.04 ms                                                         | 2.70 ms: 1.50x faster                                                      |
| chaos                    | 74.4 ms                                                         | 51.8 ms: 1.44x faster                                                      |
| crypto_pyaes             | 81.3 ms                                                         | 56.8 ms: 1.43x faster                                                      |
| go                       | 146 ms                                                          | 103 ms: 1.42x faster                                                       |
| deepcopy_memo            | 29.6 us                                                         | 22.0 us: 1.34x faster                                                      |
| raytrace                 | 303 ms                                                          | 227 ms: 1.33x faster                                                       |
| logging_silent           | 97.9 ns                                                         | 74.4 ns: 1.32x faster                                                      |
| scimark_lu               | 89.8 ms                                                         | 68.5 ms: 1.31x faster                                                      |
| deepcopy                 | 310 us                                                          | 242 us: 1.28x faster                                                       |
| comprehensions           | 17.7 us                                                         | 13.9 us: 1.28x faster                                                      |
| json_dumps               | 9.82 ms                                                         | 7.70 ms: 1.28x faster                                                      |
| sqlglot_parse            | 1.33 ms                                                         | 1.06 ms: 1.26x faster                                                      |
| tornado_http             | 118 ms                                                          | 94.2 ms: 1.25x faster                                                      |
| sqlglot_transpile        | 1.58 ms                                                         | 1.31 ms: 1.21x faster                                                      |
| hexiom                   | 6.13 ms                                                         | 5.13 ms: 1.19x faster                                                      |
| nqueens                  | 87.1 ms                                                         | 73.3 ms: 1.19x faster                                                      |
| thrift                   | 902 us                                                          | 763 us: 1.18x faster                                                       |
| pycparser                | 1.04 sec                                                        | 882 ms: 1.18x faster                                                       |
| scimark_sor              | 115 ms                                                          | 97.5 ms: 1.18x faster                                                      |
| generators               | 31.6 ms                                                         | 26.8 ms: 1.18x faster                                                      |
| dulwich_log              | 58.5 ms                                                         | 49.8 ms: 1.17x faster                                                      |
| pyflate                  | 422 ms                                                          | 360 ms: 1.17x faster                                                       |
| sqlite_synth             | 2.29 us                                                         | 1.98 us: 1.16x faster                                                      |
| asyncio_tcp              | 744 ms                                                          | 650 ms: 1.14x faster                                                       |
| float                    | 69.6 ms                                                         | 61.0 ms: 1.14x faster                                                      |
| sympy_sum                | 122 ms                                                          | 107 ms: 1.14x faster                                                       |
| richards_super           | 49.9 ms                                                         | 43.8 ms: 1.14x faster                                                      |
| html5lib                 | 52.1 ms                                                         | 45.7 ms: 1.14x faster                                                      |
| scimark_monte_carlo      | 61.9 ms                                                         | 54.8 ms: 1.13x faster                                                      |
| mako                     | 9.10 ms                                                         | 8.08 ms: 1.13x faster                                                      |
| bench_thread_pool        | 1.12 ms                                                         | 995 us: 1.13x faster                                                       |
| xml_etree_parse          | 120 ms                                                          | 107 ms: 1.12x faster                                                       |
| json                     | 4.76 ms                                                         | 4.27 ms: 1.12x faster                                                      |
| regex_dna                | 131 ms                                                          | 117 ms: 1.11x faster                                                       |
| django_template          | 36.0 ms                                                         | 32.4 ms: 1.11x faster                                                      |
| pickle_pure_python       | 280 us                                                          | 256 us: 1.10x faster                                                       |
| regex_compile            | 117 ms                                                          | 107 ms: 1.09x faster                                                       |
| deepcopy_reduce          | 2.68 us                                                         | 2.49 us: 1.08x faster                                                      |
| sympy_integrate          | 16.6 ms                                                         | 15.5 ms: 1.08x faster                                                      |
| json_loads               | 22.4 us                                                         | 20.9 us: 1.07x faster                                                      |
| 2to3                     | 265 ms                                                          | 248 ms: 1.07x faster                                                       |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.04 ms: 1.06x faster                                                      |
| mdp                      | 1.83 sec                                                        | 1.72 sec: 1.06x faster                                                     |
| xml_etree_iterparse      | 70.8 ms                                                         | 66.8 ms: 1.06x faster                                                      |
| spectral_norm            | 80.2 ms                                                         | 75.7 ms: 1.06x faster                                                      |
| sympy_str                | 229 ms                                                          | 218 ms: 1.05x faster                                                       |
| docutils                 | 1.95 sec                                                        | 1.86 sec: 1.05x faster                                                     |
| unpickle_pure_python     | 189 us                                                          | 182 us: 1.04x faster                                                       |
| tomli_loads              | 1.91 sec                                                        | 1.85 sec: 1.03x faster                                                     |
| unpickle_list            | 2.98 us                                                         | 2.94 us: 1.02x faster                                                      |
| pprint_pformat           | 1.37 sec                                                        | 1.36 sec: 1.01x faster                                                     |
| richards                 | 40.3 ms                                                         | 40.0 ms: 1.01x faster                                                      |
| sqlglot_optimize         | 44.7 ms                                                         | 44.4 ms: 1.01x faster                                                      |
| sympy_expand             | 391 ms                                                          | 388 ms: 1.01x faster                                                       |
| meteor_contest           | 80.0 ms                                                         | 80.5 ms: 1.01x slower                                                      |
| genshi_xml               | 46.6 ms                                                         | 47.0 ms: 1.01x slower                                                      |
| pathlib                  | 81.2 ms                                                         | 82.1 ms: 1.01x slower                                                      |
| pprint_safe_repr         | 658 ms                                                          | 666 ms: 1.01x slower                                                       |
| pickle                   | 7.83 us                                                         | 7.94 us: 1.01x slower                                                      |
| coroutines               | 17.9 ms                                                         | 18.3 ms: 1.02x slower                                                      |
| sqlglot_normalize        | 230 ms                                                          | 236 ms: 1.03x slower                                                       |
| python_startup           | 22.9 ms                                                         | 23.6 ms: 1.03x slower                                                      |
| fannkuch                 | 317 ms                                                          | 328 ms: 1.03x slower                                                       |
| pickle_list              | 3.22 us                                                         | 3.34 us: 1.04x slower                                                      |
| regex_v8                 | 15.8 ms                                                         | 16.4 ms: 1.04x slower                                                      |
| xml_etree_process        | 48.1 ms                                                         | 50.7 ms: 1.05x slower                                                      |
| genshi_text              | 21.0 ms                                                         | 22.2 ms: 1.06x slower                                                      |
| create_gc_cycles         | 694 us                                                          | 741 us: 1.07x slower                                                       |
| scimark_fft              | 216 ms                                                          | 231 ms: 1.07x slower                                                       |
| python_startup_no_site   | 18.1 ms                                                         | 19.4 ms: 1.07x slower                                                      |
| unpickle                 | 9.82 us                                                         | 10.5 us: 1.07x slower                                                      |
| bench_mp_pool            | 66.4 ms                                                         | 71.5 ms: 1.08x slower                                                      |
| logging_format           | 7.91 us                                                         | 8.55 us: 1.08x slower                                                      |
| logging_simple           | 7.29 us                                                         | 7.89 us: 1.08x slower                                                      |
| gc_traversal             | 1.28 ms                                                         | 1.42 ms: 1.11x slower                                                      |
| pickle_dict              | 18.2 us                                                         | 20.3 us: 1.11x slower                                                      |
| xml_etree_generate       | 61.6 ms                                                         | 69.2 ms: 1.12x slower                                                      |
| coverage                 | 46.6 ms                                                         | 53.1 ms: 1.14x slower                                                      |
| regex_effbot             | 1.66 ms                                                         | 1.91 ms: 1.15x slower                                                      |
| nbody                    | 79.1 ms                                                         | 91.4 ms: 1.16x slower                                                      |
| unpack_sequence          | 40.0 ns                                                         | 46.6 ns: 1.16x slower                                                      |
| async_generators         | 241 ms                                                          | 294 ms: 1.22x slower                                                       |
| telco                    | 4.83 ms                                                         | 6.19 ms: 1.28x slower                                                      |
| Geometric mean           | (ref)                                                           | 1.12x faster                                                               |

Benchmark hidden because not significant (1): asyncio_tcp_ssl
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240911-3.14.0a0-3b5fdc8/bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown