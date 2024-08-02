# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_align
- machine: windows-x86
- commit hash: 0081bcd
- commit date: 2024-05-23
- overall geometric mean: 1.22x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240523-pythonperf1_win32-x86-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 249 ms: 1.06x faster                                                         |
| chameleon      | 6.42 ms                                                         | 6.18 ms: 1.04x faster                                                        |
| docutils       | 1.95 sec                                                        | 1.90 sec: 1.02x faster                                                       |
| html5lib       | 52.1 ms                                                         | 46.0 ms: 1.13x faster                                                        |
| tornado_http   | 118 ms                                                          | 97.3 ms: 1.21x faster                                                        |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240523-pythonperf1_win32-x86-brandtbucher-justin_align-3.14.0a0-0081bcd |
|-------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 478 ms: 1.93x faster                                                         |
| async_tree_io           | 940 ms                                                          | 545 ms: 1.73x faster                                                         |
| async_tree_none         | 394 ms                                                          | 232 ms: 1.70x faster                                                         |
| async_tree_memoization  | 467 ms                                                          | 284 ms: 1.64x faster                                                         |
| Geometric mean          | (ref)                                                           | 1.75x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240523-pythonperf1_win32-x86-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 198 ms: 2.53x faster                                                         |
| float          | 69.6 ms                                                         | 40.9 ms: 1.70x faster                                                        |
| nbody          | 79.1 ms                                                         | 51.8 ms: 1.53x faster                                                        |
| Geometric mean | (ref)                                                           | 1.87x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240523-pythonperf1_win32-x86-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 96.3 ms: 1.21x faster                                                        |
| regex_dna      | 131 ms                                                          | 119 ms: 1.10x faster                                                         |
| regex_v8       | 15.8 ms                                                         | 15.7 ms: 1.01x faster                                                        |
| regex_effbot   | 1.66 ms                                                         | 1.88 ms: 1.13x slower                                                        |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240523-pythonperf1_win32-x86-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.63 ms: 1.48x faster                                                        |
| tomli_loads          | 1.91 sec                                                        | 1.37 sec: 1.40x faster                                                       |
| unpickle_pure_python | 189 us                                                          | 137 us: 1.39x faster                                                         |
| pickle_pure_python   | 280 us                                                          | 204 us: 1.37x faster                                                         |
| xml_etree_iterparse  | 70.8 ms                                                         | 59.9 ms: 1.18x faster                                                        |
| xml_etree_parse      | 120 ms                                                          | 102 ms: 1.18x faster                                                         |
| xml_etree_process    | 48.1 ms                                                         | 42.6 ms: 1.13x faster                                                        |
| json_loads           | 22.4 us                                                         | 21.0 us: 1.06x faster                                                        |
| xml_etree_generate   | 61.6 ms                                                         | 58.0 ms: 1.06x faster                                                        |
| unpickle_list        | 2.98 us                                                         | 2.85 us: 1.05x faster                                                        |
| unpickle             | 9.82 us                                                         | 10.0 us: 1.02x slower                                                        |
| pickle_list          | 3.22 us                                                         | 3.60 us: 1.12x slower                                                        |
| pickle_dict          | 18.2 us                                                         | 20.7 us: 1.13x slower                                                        |
| pickle               | 7.83 us                                                         | 9.05 us: 1.16x slower                                                        |
| Geometric mean       | (ref)                                                           | 1.12x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240523-pythonperf1_win32-x86-brandtbucher-justin_align-3.14.0a0-0081bcd |
|------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 24.3 ms: 1.06x slower                                                        |
| python_startup_no_site | 18.1 ms                                                         | 20.5 ms: 1.14x slower                                                        |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240523-pythonperf1_win32-x86-brandtbucher-justin_align-3.14.0a0-0081bcd |
|-----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.38 ms: 1.69x faster                                                        |
| django_template | 36.0 ms                                                         | 31.7 ms: 1.14x faster                                                        |
| genshi_text     | 21.0 ms                                                         | 21.4 ms: 1.02x slower                                                        |
| genshi_xml      | 46.6 ms                                                         | 50.5 ms: 1.08x slower                                                        |
| Geometric mean  | (ref)                                                           | 1.15x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240523-pythonperf1_win32-x86-brandtbucher-justin_align-3.14.0a0-0081bcd |
|--------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 137 us: 2.90x faster                                                         |
| pidigits                 | 502 ms                                                          | 198 ms: 2.53x faster                                                         |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 478 ms: 1.93x faster                                                         |
| logging_silent           | 97.9 ns                                                         | 55.0 ns: 1.78x faster                                                        |
| async_tree_io            | 940 ms                                                          | 545 ms: 1.73x faster                                                         |
| float                    | 69.6 ms                                                         | 40.9 ms: 1.70x faster                                                        |
| async_tree_none          | 394 ms                                                          | 232 ms: 1.70x faster                                                         |
| mako                     | 9.10 ms                                                         | 5.38 ms: 1.69x faster                                                        |
| spectral_norm            | 80.2 ms                                                         | 47.9 ms: 1.67x faster                                                        |
| async_tree_memoization   | 467 ms                                                          | 284 ms: 1.64x faster                                                         |
| crypto_pyaes             | 81.3 ms                                                         | 49.6 ms: 1.64x faster                                                        |
| comprehensions           | 17.7 us                                                         | 11.0 us: 1.61x faster                                                        |
| pylint                   | 384 ms                                                          | 241 ms: 1.59x faster                                                         |
| deltablue                | 4.04 ms                                                         | 2.55 ms: 1.58x faster                                                        |
| nbody                    | 79.1 ms                                                         | 51.8 ms: 1.53x faster                                                        |
| pyflate                  | 422 ms                                                          | 278 ms: 1.52x faster                                                         |
| scimark_monte_carlo      | 61.9 ms                                                         | 41.2 ms: 1.50x faster                                                        |
| raytrace                 | 303 ms                                                          | 202 ms: 1.50x faster                                                         |
| chaos                    | 74.4 ms                                                         | 49.8 ms: 1.49x faster                                                        |
| json_dumps               | 9.82 ms                                                         | 6.63 ms: 1.48x faster                                                        |
| fannkuch                 | 317 ms                                                          | 215 ms: 1.47x faster                                                         |
| sqlglot_parse            | 1.33 ms                                                         | 922 us: 1.44x faster                                                         |
| deepcopy_memo            | 29.6 us                                                         | 20.6 us: 1.43x faster                                                        |
| richards_super           | 49.9 ms                                                         | 35.5 ms: 1.41x faster                                                        |
| tomli_loads              | 1.91 sec                                                        | 1.37 sec: 1.40x faster                                                       |
| unpickle_pure_python     | 189 us                                                          | 137 us: 1.39x faster                                                         |
| hexiom                   | 6.13 ms                                                         | 4.45 ms: 1.38x faster                                                        |
| pickle_pure_python       | 280 us                                                          | 204 us: 1.37x faster                                                         |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.37 ms: 1.37x faster                                                        |
| generators               | 31.6 ms                                                         | 23.4 ms: 1.35x faster                                                        |
| go                       | 146 ms                                                          | 108 ms: 1.34x faster                                                         |
| sqlglot_transpile        | 1.58 ms                                                         | 1.19 ms: 1.33x faster                                                        |
| richards                 | 40.3 ms                                                         | 30.7 ms: 1.31x faster                                                        |
| pycparser                | 1.04 sec                                                        | 804 ms: 1.30x faster                                                         |
| scimark_fft              | 216 ms                                                          | 167 ms: 1.29x faster                                                         |
| nqueens                  | 87.1 ms                                                         | 67.5 ms: 1.29x faster                                                        |
| scimark_sor              | 115 ms                                                          | 89.4 ms: 1.29x faster                                                        |
| scimark_lu               | 89.8 ms                                                         | 70.6 ms: 1.27x faster                                                        |
| thrift                   | 902 us                                                          | 714 us: 1.26x faster                                                         |
| sqlite_synth             | 2.29 us                                                         | 1.85 us: 1.24x faster                                                        |
| pprint_safe_repr         | 658 ms                                                          | 542 ms: 1.21x faster                                                         |
| pprint_pformat           | 1.37 sec                                                        | 1.13 sec: 1.21x faster                                                       |
| regex_compile            | 117 ms                                                          | 96.3 ms: 1.21x faster                                                        |
| tornado_http             | 118 ms                                                          | 97.3 ms: 1.21x faster                                                        |
| xml_etree_iterparse      | 70.8 ms                                                         | 59.9 ms: 1.18x faster                                                        |
| xml_etree_parse          | 120 ms                                                          | 102 ms: 1.18x faster                                                         |
| asyncio_tcp              | 744 ms                                                          | 634 ms: 1.17x faster                                                         |
| mdp                      | 1.83 sec                                                        | 1.60 sec: 1.14x faster                                                       |
| django_template          | 36.0 ms                                                         | 31.7 ms: 1.14x faster                                                        |
| html5lib                 | 52.1 ms                                                         | 46.0 ms: 1.13x faster                                                        |
| xml_etree_process        | 48.1 ms                                                         | 42.6 ms: 1.13x faster                                                        |
| sympy_sum                | 122 ms                                                          | 108 ms: 1.13x faster                                                         |
| bench_thread_pool        | 1.12 ms                                                         | 1.01 ms: 1.11x faster                                                        |
| json                     | 4.76 ms                                                         | 4.30 ms: 1.11x faster                                                        |
| coroutines               | 17.9 ms                                                         | 16.2 ms: 1.10x faster                                                        |
| regex_dna                | 131 ms                                                          | 119 ms: 1.10x faster                                                         |
| meteor_contest           | 80.0 ms                                                         | 73.5 ms: 1.09x faster                                                        |
| sympy_str                | 229 ms                                                          | 212 ms: 1.08x faster                                                         |
| json_loads               | 22.4 us                                                         | 21.0 us: 1.06x faster                                                        |
| 2to3                     | 265 ms                                                          | 249 ms: 1.06x faster                                                         |
| sympy_integrate          | 16.6 ms                                                         | 15.7 ms: 1.06x faster                                                        |
| xml_etree_generate       | 61.6 ms                                                         | 58.0 ms: 1.06x faster                                                        |
| sqlglot_optimize         | 44.7 ms                                                         | 42.3 ms: 1.06x faster                                                        |
| unpickle_list            | 2.98 us                                                         | 2.85 us: 1.05x faster                                                        |
| sqlglot_normalize        | 230 ms                                                          | 221 ms: 1.04x faster                                                         |
| sympy_expand             | 391 ms                                                          | 376 ms: 1.04x faster                                                         |
| chameleon                | 6.42 ms                                                         | 6.18 ms: 1.04x faster                                                        |
| deepcopy                 | 310 us                                                          | 300 us: 1.03x faster                                                         |
| docutils                 | 1.95 sec                                                        | 1.90 sec: 1.02x faster                                                       |
| regex_v8                 | 15.8 ms                                                         | 15.7 ms: 1.01x faster                                                        |
| logging_format           | 7.91 us                                                         | 8.07 us: 1.02x slower                                                        |
| genshi_text              | 21.0 ms                                                         | 21.4 ms: 1.02x slower                                                        |
| unpickle                 | 9.82 us                                                         | 10.0 us: 1.02x slower                                                        |
| deepcopy_reduce          | 2.68 us                                                         | 2.75 us: 1.03x slower                                                        |
| logging_simple           | 7.29 us                                                         | 7.54 us: 1.03x slower                                                        |
| python_startup           | 22.9 ms                                                         | 24.3 ms: 1.06x slower                                                        |
| pathlib                  | 81.2 ms                                                         | 86.4 ms: 1.06x slower                                                        |
| coverage                 | 46.6 ms                                                         | 50.3 ms: 1.08x slower                                                        |
| genshi_xml               | 46.6 ms                                                         | 50.5 ms: 1.08x slower                                                        |
| create_gc_cycles         | 694 us                                                          | 764 us: 1.10x slower                                                         |
| pickle_list              | 3.22 us                                                         | 3.60 us: 1.12x slower                                                        |
| bench_mp_pool            | 66.4 ms                                                         | 74.8 ms: 1.13x slower                                                        |
| gc_traversal             | 1.28 ms                                                         | 1.45 ms: 1.13x slower                                                        |
| regex_effbot             | 1.66 ms                                                         | 1.88 ms: 1.13x slower                                                        |
| pickle_dict              | 18.2 us                                                         | 20.7 us: 1.13x slower                                                        |
| python_startup_no_site   | 18.1 ms                                                         | 20.5 ms: 1.14x slower                                                        |
| pickle                   | 7.83 us                                                         | 9.05 us: 1.16x slower                                                        |
| telco                    | 4.83 ms                                                         | 5.63 ms: 1.17x slower                                                        |
| async_generators         | 241 ms                                                          | 291 ms: 1.21x slower                                                         |
| Geometric mean           | (ref)                                                           | 1.22x faster                                                                 |

Benchmark hidden because not significant (2): asyncio_tcp_ssl, flaskblogging
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240523-3.14.0a0-0081bcd-JIT/bm-20240523-pythonperf1_win32-x86-brandtbucher-justin_align-3.14.0a0-0081bcd.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown