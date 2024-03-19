# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_mprotect_cost
- machine: windows-x86
- commit hash: c8d6017
- commit date: 2024-03-18
- overall geometric mean: 1.07x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240318-pythonperf1_win32-x86-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 255 ms: 1.04x faster                                                                  |
| chameleon      | 6.42 ms                                                         | 5.84 ms: 1.10x faster                                                                 |
| docutils       | 1.95 sec                                                        | 1.81 sec: 1.08x faster                                                                |
| html5lib       | 52.1 ms                                                         | 44.9 ms: 1.16x faster                                                                 |
| tornado_http   | 118 ms                                                          | 95.9 ms: 1.23x faster                                                                 |
| Geometric mean | (ref)                                                           | 1.12x faster                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240318-pythonperf1_win32-x86-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 519 ms: 1.78x faster                                                                  |
| async_tree_io           | 940 ms                                                          | 616 ms: 1.53x faster                                                                  |
| async_tree_none         | 394 ms                                                          | 258 ms: 1.52x faster                                                                  |
| async_tree_memoization  | 467 ms                                                          | 320 ms: 1.46x faster                                                                  |
| Geometric mean          | (ref)                                                           | 1.57x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240318-pythonperf1_win32-x86-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 199 ms: 2.53x faster                                                                  |
| float          | 69.6 ms                                                         | 55.4 ms: 1.26x faster                                                                 |
| nbody          | 79.1 ms                                                         | 95.9 ms: 1.21x slower                                                                 |
| Geometric mean | (ref)                                                           | 1.38x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240318-pythonperf1_win32-x86-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 108 ms: 1.08x faster                                                                  |
| regex_dna      | 131 ms                                                          | 121 ms: 1.08x faster                                                                  |
| regex_v8       | 15.8 ms                                                         | 16.2 ms: 1.02x slower                                                                 |
| regex_effbot   | 1.66 ms                                                         | 1.89 ms: 1.14x slower                                                                 |
| Geometric mean | (ref)                                                           | 1.00x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240318-pythonperf1_win32-x86-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.07 ms: 1.39x faster                                                                 |
| pickle_pure_python   | 280 us                                                          | 209 us: 1.34x faster                                                                  |
| unpickle_pure_python | 189 us                                                          | 164 us: 1.15x faster                                                                  |
| tomli_loads          | 1.91 sec                                                        | 1.68 sec: 1.14x faster                                                                |
| json_loads           | 22.4 us                                                         | 19.8 us: 1.13x faster                                                                 |
| xml_etree_process    | 48.1 ms                                                         | 42.8 ms: 1.12x faster                                                                 |
| xml_etree_parse      | 120 ms                                                          | 108 ms: 1.11x faster                                                                  |
| xml_etree_iterparse  | 70.8 ms                                                         | 67.0 ms: 1.06x faster                                                                 |
| unpickle_list        | 2.98 us                                                         | 2.93 us: 1.02x faster                                                                 |
| xml_etree_generate   | 61.6 ms                                                         | 62.0 ms: 1.01x slower                                                                 |
| unpickle             | 9.82 us                                                         | 9.96 us: 1.01x slower                                                                 |
| pickle               | 7.83 us                                                         | 8.03 us: 1.03x slower                                                                 |
| pickle_list          | 3.22 us                                                         | 3.31 us: 1.03x slower                                                                 |
| pickle_dict          | 18.2 us                                                         | 19.8 us: 1.08x slower                                                                 |
| Geometric mean       | (ref)                                                           | 1.09x faster                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240318-pythonperf1_win32-x86-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 25.1 ms: 1.09x slower                                                                 |
| python_startup_no_site | 18.1 ms                                                         | 23.0 ms: 1.27x slower                                                                 |
| Geometric mean         | (ref)                                                           | 1.18x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240318-pythonperf1_win32-x86-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.00 ms: 1.30x faster                                                                 |
| django_template | 36.0 ms                                                         | 29.1 ms: 1.24x faster                                                                 |
| genshi_text     | 21.0 ms                                                         | 21.8 ms: 1.04x slower                                                                 |
| genshi_xml      | 46.6 ms                                                         | 48.5 ms: 1.04x slower                                                                 |
| Geometric mean  | (ref)                                                           | 1.10x faster                                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240318-pythonperf1_win32-x86-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 97.7 us: 4.05x faster                                                                 |
| pidigits                 | 502 ms                                                          | 199 ms: 2.53x faster                                                                  |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 519 ms: 1.78x faster                                                                  |
| pylint                   | 384 ms                                                          | 227 ms: 1.69x faster                                                                  |
| logging_silent           | 97.9 ns                                                         | 60.0 ns: 1.63x faster                                                                 |
| deltablue                | 4.04 ms                                                         | 2.49 ms: 1.62x faster                                                                 |
| async_tree_io            | 940 ms                                                          | 616 ms: 1.53x faster                                                                  |
| async_tree_none          | 394 ms                                                          | 258 ms: 1.52x faster                                                                  |
| async_tree_memoization   | 467 ms                                                          | 320 ms: 1.46x faster                                                                  |
| generators               | 31.6 ms                                                         | 22.2 ms: 1.42x faster                                                                 |
| json_dumps               | 9.82 ms                                                         | 7.07 ms: 1.39x faster                                                                 |
| sqlglot_parse            | 1.33 ms                                                         | 972 us: 1.37x faster                                                                  |
| pickle_pure_python       | 280 us                                                          | 209 us: 1.34x faster                                                                  |
| crypto_pyaes             | 81.3 ms                                                         | 61.3 ms: 1.33x faster                                                                 |
| richards_super           | 49.9 ms                                                         | 37.7 ms: 1.32x faster                                                                 |
| mako                     | 9.10 ms                                                         | 7.00 ms: 1.30x faster                                                                 |
| sqlglot_transpile        | 1.58 ms                                                         | 1.22 ms: 1.30x faster                                                                 |
| coroutines               | 17.9 ms                                                         | 14.0 ms: 1.28x faster                                                                 |
| float                    | 69.6 ms                                                         | 55.4 ms: 1.26x faster                                                                 |
| chaos                    | 74.4 ms                                                         | 60.1 ms: 1.24x faster                                                                 |
| pycparser                | 1.04 sec                                                        | 841 ms: 1.24x faster                                                                  |
| django_template          | 36.0 ms                                                         | 29.1 ms: 1.24x faster                                                                 |
| go                       | 146 ms                                                          | 118 ms: 1.23x faster                                                                  |
| tornado_http             | 118 ms                                                          | 95.9 ms: 1.23x faster                                                                 |
| comprehensions           | 17.7 us                                                         | 14.6 us: 1.21x faster                                                                 |
| deepcopy_memo            | 29.6 us                                                         | 24.4 us: 1.21x faster                                                                 |
| richards                 | 40.3 ms                                                         | 33.8 ms: 1.19x faster                                                                 |
| sqlite_synth             | 2.29 us                                                         | 1.94 us: 1.18x faster                                                                 |
| scimark_sor              | 115 ms                                                          | 97.7 ms: 1.18x faster                                                                 |
| asyncio_tcp              | 744 ms                                                          | 634 ms: 1.17x faster                                                                  |
| html5lib                 | 52.1 ms                                                         | 44.9 ms: 1.16x faster                                                                 |
| unpickle_pure_python     | 189 us                                                          | 164 us: 1.15x faster                                                                  |
| sympy_sum                | 122 ms                                                          | 107 ms: 1.14x faster                                                                  |
| json                     | 4.76 ms                                                         | 4.19 ms: 1.14x faster                                                                 |
| tomli_loads              | 1.91 sec                                                        | 1.68 sec: 1.14x faster                                                                |
| json_loads               | 22.4 us                                                         | 19.8 us: 1.13x faster                                                                 |
| raytrace                 | 303 ms                                                          | 269 ms: 1.13x faster                                                                  |
| pyflate                  | 422 ms                                                          | 375 ms: 1.12x faster                                                                  |
| xml_etree_process        | 48.1 ms                                                         | 42.8 ms: 1.12x faster                                                                 |
| spectral_norm            | 80.2 ms                                                         | 71.7 ms: 1.12x faster                                                                 |
| xml_etree_parse          | 120 ms                                                          | 108 ms: 1.11x faster                                                                  |
| deepcopy                 | 310 us                                                          | 281 us: 1.11x faster                                                                  |
| chameleon                | 6.42 ms                                                         | 5.84 ms: 1.10x faster                                                                 |
| bench_thread_pool        | 1.12 ms                                                         | 1.02 ms: 1.10x faster                                                                 |
| deepcopy_reduce          | 2.68 us                                                         | 2.45 us: 1.10x faster                                                                 |
| scimark_lu               | 89.8 ms                                                         | 82.1 ms: 1.09x faster                                                                 |
| sympy_str                | 229 ms                                                          | 211 ms: 1.09x faster                                                                  |
| sympy_integrate          | 16.6 ms                                                         | 15.3 ms: 1.09x faster                                                                 |
| regex_compile            | 117 ms                                                          | 108 ms: 1.08x faster                                                                  |
| regex_dna                | 131 ms                                                          | 121 ms: 1.08x faster                                                                  |
| docutils                 | 1.95 sec                                                        | 1.81 sec: 1.08x faster                                                                |
| xml_etree_iterparse      | 70.8 ms                                                         | 67.0 ms: 1.06x faster                                                                 |
| sympy_expand             | 391 ms                                                          | 370 ms: 1.06x faster                                                                  |
| mdp                      | 1.83 sec                                                        | 1.73 sec: 1.06x faster                                                                |
| create_gc_cycles         | 694 us                                                          | 662 us: 1.05x faster                                                                  |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.11 ms: 1.04x faster                                                                 |
| 2to3                     | 265 ms                                                          | 255 ms: 1.04x faster                                                                  |
| hexiom                   | 6.13 ms                                                         | 5.99 ms: 1.02x faster                                                                 |
| unpickle_list            | 2.98 us                                                         | 2.93 us: 1.02x faster                                                                 |
| sqlglot_normalize        | 230 ms                                                          | 226 ms: 1.02x faster                                                                  |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 16.8 sec: 1.01x faster                                                                |
| xml_etree_generate       | 61.6 ms                                                         | 62.0 ms: 1.01x slower                                                                 |
| unpickle                 | 9.82 us                                                         | 9.96 us: 1.01x slower                                                                 |
| scimark_monte_carlo      | 61.9 ms                                                         | 63.4 ms: 1.02x slower                                                                 |
| regex_v8                 | 15.8 ms                                                         | 16.2 ms: 1.02x slower                                                                 |
| pickle                   | 7.83 us                                                         | 8.03 us: 1.03x slower                                                                 |
| pickle_list              | 3.22 us                                                         | 3.31 us: 1.03x slower                                                                 |
| meteor_contest           | 80.0 ms                                                         | 82.7 ms: 1.03x slower                                                                 |
| genshi_text              | 21.0 ms                                                         | 21.8 ms: 1.04x slower                                                                 |
| genshi_xml               | 46.6 ms                                                         | 48.5 ms: 1.04x slower                                                                 |
| sqlglot_optimize         | 44.7 ms                                                         | 46.7 ms: 1.04x slower                                                                 |
| pathlib                  | 81.2 ms                                                         | 86.1 ms: 1.06x slower                                                                 |
| fannkuch                 | 317 ms                                                          | 342 ms: 1.08x slower                                                                  |
| nqueens                  | 87.1 ms                                                         | 94.1 ms: 1.08x slower                                                                 |
| pprint_pformat           | 1.37 sec                                                        | 1.48 sec: 1.08x slower                                                                |
| pickle_dict              | 18.2 us                                                         | 19.8 us: 1.08x slower                                                                 |
| logging_format           | 7.91 us                                                         | 8.62 us: 1.09x slower                                                                 |
| scimark_fft              | 216 ms                                                          | 236 ms: 1.09x slower                                                                  |
| gc_traversal             | 1.28 ms                                                         | 1.40 ms: 1.09x slower                                                                 |
| python_startup           | 22.9 ms                                                         | 25.1 ms: 1.09x slower                                                                 |
| logging_simple           | 7.29 us                                                         | 7.98 us: 1.10x slower                                                                 |
| bench_mp_pool            | 66.4 ms                                                         | 73.2 ms: 1.10x slower                                                                 |
| pprint_safe_repr         | 658 ms                                                          | 728 ms: 1.11x slower                                                                  |
| unpack_sequence          | 40.0 ns                                                         | 45.2 ns: 1.13x slower                                                                 |
| regex_effbot             | 1.66 ms                                                         | 1.89 ms: 1.14x slower                                                                 |
| nbody                    | 79.1 ms                                                         | 95.9 ms: 1.21x slower                                                                 |
| async_generators         | 241 ms                                                          | 300 ms: 1.24x slower                                                                  |
| python_startup_no_site   | 18.1 ms                                                         | 23.0 ms: 1.27x slower                                                                 |
| telco                    | 4.83 ms                                                         | 6.57 ms: 1.36x slower                                                                 |
| coverage                 | 46.6 ms                                                         | 501 ms: 10.76x slower                                                                 |
| thrift                   | 902 us                                                          | 10.8 ms: 11.92x slower                                                                |
| Geometric mean           | (ref)                                                           | 1.07x faster                                                                          |
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240318-3.13.0a5+-c8d6017-JIT/bm-20240318-pythonperf1_win32-x86-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.03x


# Memory

- memory change: unknown