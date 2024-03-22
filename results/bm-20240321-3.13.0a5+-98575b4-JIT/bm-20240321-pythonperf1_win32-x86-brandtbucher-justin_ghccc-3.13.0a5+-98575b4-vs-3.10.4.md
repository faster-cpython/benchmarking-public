# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_ghccc
- machine: windows-x86
- commit hash: 98575b4
- commit date: 2024-03-21
- overall geometric mean: 1.02x faster
- HPT reliability: 99.88%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240321-pythonperf1_win32-x86-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 259 ms: 1.02x faster                                                          |
| chameleon      | 6.42 ms                                                         | 5.92 ms: 1.09x faster                                                         |
| docutils       | 1.95 sec                                                        | 2.42 sec: 1.24x slower                                                        |
| html5lib       | 52.1 ms                                                         | 48.9 ms: 1.07x faster                                                         |
| tornado_http   | 118 ms                                                          | 101 ms: 1.16x faster                                                          |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240321-pythonperf1_win32-x86-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|-------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 1.58 sec: 1.72x slower                                                        |
| async_tree_none         | 394 ms                                                          | 1.21 sec: 3.08x slower                                                        |
| async_tree_memoization  | 467 ms                                                          | 1.46 sec: 3.12x slower                                                        |
| async_tree_io           | 940 ms                                                          | 4.63 sec: 4.93x slower                                                        |
| Geometric mean          | (ref)                                                           | 3.00x slower                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240321-pythonperf1_win32-x86-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 197 ms: 2.55x faster                                                          |
| nbody          | 79.1 ms                                                         | 53.7 ms: 1.47x faster                                                         |
| float          | 69.6 ms                                                         | 75.6 ms: 1.09x slower                                                         |
| Geometric mean | (ref)                                                           | 1.51x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240321-pythonperf1_win32-x86-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 101 ms: 1.15x faster                                                          |
| regex_dna      | 131 ms                                                          | 118 ms: 1.11x faster                                                          |
| regex_v8       | 15.8 ms                                                         | 15.9 ms: 1.01x slower                                                         |
| regex_effbot   | 1.66 ms                                                         | 1.93 ms: 1.16x slower                                                         |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240321-pythonperf1_win32-x86-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.95 ms: 1.41x faster                                                         |
| unpickle_pure_python | 189 us                                                          | 136 us: 1.39x faster                                                          |
| tomli_loads          | 1.91 sec                                                        | 1.42 sec: 1.35x faster                                                        |
| pickle_pure_python   | 280 us                                                          | 228 us: 1.23x faster                                                          |
| unpickle_list        | 2.98 us                                                         | 2.61 us: 1.14x faster                                                         |
| json_loads           | 22.4 us                                                         | 20.1 us: 1.11x faster                                                         |
| pickle_list          | 3.22 us                                                         | 3.15 us: 1.02x faster                                                         |
| pickle               | 7.83 us                                                         | 7.67 us: 1.02x faster                                                         |
| xml_etree_process    | 48.1 ms                                                         | 47.9 ms: 1.01x faster                                                         |
| xml_etree_generate   | 61.6 ms                                                         | 65.9 ms: 1.07x slower                                                         |
| xml_etree_parse      | 120 ms                                                          | 130 ms: 1.08x slower                                                          |
| pickle_dict          | 18.2 us                                                         | 19.8 us: 1.09x slower                                                         |
| xml_etree_iterparse  | 70.8 ms                                                         | 88.7 ms: 1.25x slower                                                         |
| Geometric mean       | (ref)                                                           | 1.07x faster                                                                  |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240321-pythonperf1_win32-x86-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 26.3 ms: 1.15x slower                                                         |
| python_startup_no_site | 18.1 ms                                                         | 23.7 ms: 1.31x slower                                                         |
| Geometric mean         | (ref)                                                           | 1.23x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240321-pythonperf1_win32-x86-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|-----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.46 ms: 1.67x faster                                                         |
| django_template | 36.0 ms                                                         | 31.1 ms: 1.16x faster                                                         |
| genshi_text     | 21.0 ms                                                         | 21.7 ms: 1.04x slower                                                         |
| genshi_xml      | 46.6 ms                                                         | 51.0 ms: 1.09x slower                                                         |
| Geometric mean  | (ref)                                                           | 1.14x faster                                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240321-pythonperf1_win32-x86-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|--------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 90.9 us: 4.35x faster                                                         |
| pidigits                 | 502 ms                                                          | 197 ms: 2.55x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 48.2 ms: 1.69x faster                                                         |
| mako                     | 9.10 ms                                                         | 5.46 ms: 1.67x faster                                                         |
| deltablue                | 4.04 ms                                                         | 2.49 ms: 1.62x faster                                                         |
| spectral_norm            | 80.2 ms                                                         | 51.1 ms: 1.57x faster                                                         |
| comprehensions           | 17.7 us                                                         | 11.6 us: 1.53x faster                                                         |
| pyflate                  | 422 ms                                                          | 276 ms: 1.53x faster                                                          |
| nbody                    | 79.1 ms                                                         | 53.7 ms: 1.47x faster                                                         |
| scimark_monte_carlo      | 61.9 ms                                                         | 42.6 ms: 1.45x faster                                                         |
| logging_silent           | 97.9 ns                                                         | 67.7 ns: 1.45x faster                                                         |
| json_dumps               | 9.82 ms                                                         | 6.95 ms: 1.41x faster                                                         |
| chaos                    | 74.4 ms                                                         | 53.0 ms: 1.40x faster                                                         |
| unpickle_pure_python     | 189 us                                                          | 136 us: 1.39x faster                                                          |
| richards_super           | 49.9 ms                                                         | 36.0 ms: 1.39x faster                                                         |
| fannkuch                 | 317 ms                                                          | 231 ms: 1.37x faster                                                          |
| hexiom                   | 6.13 ms                                                         | 4.55 ms: 1.35x faster                                                         |
| tomli_loads              | 1.91 sec                                                        | 1.42 sec: 1.35x faster                                                        |
| sqlglot_parse            | 1.33 ms                                                         | 1.01 ms: 1.32x faster                                                         |
| generators               | 31.6 ms                                                         | 24.0 ms: 1.32x faster                                                         |
| richards                 | 40.3 ms                                                         | 31.0 ms: 1.30x faster                                                         |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.50 ms: 1.30x faster                                                         |
| go                       | 146 ms                                                          | 114 ms: 1.27x faster                                                          |
| scimark_fft              | 216 ms                                                          | 170 ms: 1.27x faster                                                          |
| scimark_sor              | 115 ms                                                          | 90.9 ms: 1.27x faster                                                         |
| sqlglot_transpile        | 1.58 ms                                                         | 1.27 ms: 1.25x faster                                                         |
| raytrace                 | 303 ms                                                          | 244 ms: 1.24x faster                                                          |
| pickle_pure_python       | 280 us                                                          | 228 us: 1.23x faster                                                          |
| sqlite_synth             | 2.29 us                                                         | 1.91 us: 1.20x faster                                                         |
| coroutines               | 17.9 ms                                                         | 15.2 ms: 1.18x faster                                                         |
| scimark_lu               | 89.8 ms                                                         | 76.7 ms: 1.17x faster                                                         |
| deepcopy_memo            | 29.6 us                                                         | 25.4 us: 1.16x faster                                                         |
| tornado_http             | 118 ms                                                          | 101 ms: 1.16x faster                                                          |
| django_template          | 36.0 ms                                                         | 31.1 ms: 1.16x faster                                                         |
| sympy_sum                | 122 ms                                                          | 106 ms: 1.16x faster                                                          |
| regex_compile            | 117 ms                                                          | 101 ms: 1.15x faster                                                          |
| unpickle_list            | 2.98 us                                                         | 2.61 us: 1.14x faster                                                         |
| pprint_pformat           | 1.37 sec                                                        | 1.20 sec: 1.14x faster                                                        |
| asyncio_tcp              | 744 ms                                                          | 654 ms: 1.14x faster                                                          |
| json                     | 4.76 ms                                                         | 4.22 ms: 1.13x faster                                                         |
| pprint_safe_repr         | 658 ms                                                          | 585 ms: 1.12x faster                                                          |
| json_loads               | 22.4 us                                                         | 20.1 us: 1.11x faster                                                         |
| bench_thread_pool        | 1.12 ms                                                         | 1.01 ms: 1.11x faster                                                         |
| nqueens                  | 87.1 ms                                                         | 78.5 ms: 1.11x faster                                                         |
| regex_dna                | 131 ms                                                          | 118 ms: 1.11x faster                                                          |
| pycparser                | 1.04 sec                                                        | 951 ms: 1.10x faster                                                          |
| sympy_str                | 229 ms                                                          | 210 ms: 1.09x faster                                                          |
| chameleon                | 6.42 ms                                                         | 5.92 ms: 1.09x faster                                                         |
| meteor_contest           | 80.0 ms                                                         | 74.3 ms: 1.08x faster                                                         |
| sympy_integrate          | 16.6 ms                                                         | 15.5 ms: 1.07x faster                                                         |
| sqlglot_normalize        | 230 ms                                                          | 216 ms: 1.07x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 48.9 ms: 1.07x faster                                                         |
| deepcopy                 | 310 us                                                          | 291 us: 1.06x faster                                                          |
| mdp                      | 1.83 sec                                                        | 1.73 sec: 1.05x faster                                                        |
| sympy_expand             | 391 ms                                                          | 372 ms: 1.05x faster                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.56 us: 1.05x faster                                                         |
| sqlglot_optimize         | 44.7 ms                                                         | 43.1 ms: 1.04x faster                                                         |
| create_gc_cycles         | 694 us                                                          | 670 us: 1.04x faster                                                          |
| 2to3                     | 265 ms                                                          | 259 ms: 1.02x faster                                                          |
| pickle_list              | 3.22 us                                                         | 3.15 us: 1.02x faster                                                         |
| pickle                   | 7.83 us                                                         | 7.67 us: 1.02x faster                                                         |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 16.8 sec: 1.01x faster                                                        |
| xml_etree_process        | 48.1 ms                                                         | 47.9 ms: 1.01x faster                                                         |
| regex_v8                 | 15.8 ms                                                         | 15.9 ms: 1.01x slower                                                         |
| genshi_text              | 21.0 ms                                                         | 21.7 ms: 1.04x slower                                                         |
| pathlib                  | 81.2 ms                                                         | 86.5 ms: 1.06x slower                                                         |
| xml_etree_generate       | 61.6 ms                                                         | 65.9 ms: 1.07x slower                                                         |
| logging_format           | 7.91 us                                                         | 8.48 us: 1.07x slower                                                         |
| pylint                   | 384 ms                                                          | 412 ms: 1.07x slower                                                          |
| logging_simple           | 7.29 us                                                         | 7.83 us: 1.07x slower                                                         |
| xml_etree_parse          | 120 ms                                                          | 130 ms: 1.08x slower                                                          |
| float                    | 69.6 ms                                                         | 75.6 ms: 1.09x slower                                                         |
| pickle_dict              | 18.2 us                                                         | 19.8 us: 1.09x slower                                                         |
| genshi_xml               | 46.6 ms                                                         | 51.0 ms: 1.09x slower                                                         |
| python_startup           | 22.9 ms                                                         | 26.3 ms: 1.15x slower                                                         |
| bench_mp_pool            | 66.4 ms                                                         | 76.2 ms: 1.15x slower                                                         |
| regex_effbot             | 1.66 ms                                                         | 1.93 ms: 1.16x slower                                                         |
| telco                    | 4.83 ms                                                         | 5.80 ms: 1.20x slower                                                         |
| docutils                 | 1.95 sec                                                        | 2.42 sec: 1.24x slower                                                        |
| xml_etree_iterparse      | 70.8 ms                                                         | 88.7 ms: 1.25x slower                                                         |
| async_generators         | 241 ms                                                          | 315 ms: 1.31x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 23.7 ms: 1.31x slower                                                         |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 1.58 sec: 1.72x slower                                                        |
| unpack_sequence          | 40.0 ns                                                         | 73.1 ns: 1.83x slower                                                         |
| async_tree_none          | 394 ms                                                          | 1.21 sec: 3.08x slower                                                        |
| async_tree_memoization   | 467 ms                                                          | 1.46 sec: 3.12x slower                                                        |
| async_tree_io            | 940 ms                                                          | 4.63 sec: 4.93x slower                                                        |
| coverage                 | 46.6 ms                                                         | 513 ms: 11.01x slower                                                         |
| thrift                   | 902 us                                                          | 11.1 ms: 12.25x slower                                                        |
| Geometric mean           | (ref)                                                           | 1.02x faster                                                                  |

Benchmark hidden because not significant (2): gc_traversal, unpickle
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240321-3.13.0a5+-98575b4-JIT/bm-20240321-pythonperf1_win32-x86-brandtbucher-justin_ghccc-3.13.0a5+-98575b4.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 99.88% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.02x


# Memory

- memory change: unknown