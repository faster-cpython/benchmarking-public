# Results vs. 3.10.4

- fork: brandtbucher
- ref: main
- machine: windows-x86
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.21x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 258 ms: 1.03x faster                                                 |
| docutils       | 1.95 sec                                                        | 2.01 sec: 1.03x slower                                               |
| html5lib       | 52.1 ms                                                         | 46.6 ms: 1.12x faster                                                |
| tornado_http   | 118 ms                                                          | 99.4 ms: 1.18x faster                                                |
| Geometric mean | (ref)                                                           | 1.07x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75 |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 475 ms: 1.94x faster                                                 |
| async_tree_none         | 394 ms                                                          | 216 ms: 1.82x faster                                                 |
| async_tree_io           | 940 ms                                                          | 536 ms: 1.75x faster                                                 |
| async_tree_memoization  | 467 ms                                                          | 272 ms: 1.72x faster                                                 |
| Geometric mean          | (ref)                                                           | 1.81x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 198 ms: 2.54x faster                                                 |
| nbody          | 79.1 ms                                                         | 49.5 ms: 1.60x faster                                                |
| float          | 69.6 ms                                                         | 44.1 ms: 1.58x faster                                                |
| Geometric mean | (ref)                                                           | 1.86x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 103 ms: 1.14x faster                                                 |
| regex_dna      | 131 ms                                                          | 121 ms: 1.08x faster                                                 |
| regex_v8       | 15.8 ms                                                         | 15.8 ms: 1.00x slower                                                |
| regex_effbot   | 1.66 ms                                                         | 1.95 ms: 1.17x slower                                                |
| Geometric mean | (ref)                                                           | 1.01x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.06 ms: 1.39x faster                                                |
| tomli_loads          | 1.91 sec                                                        | 1.54 sec: 1.24x faster                                               |
| xml_etree_process    | 48.1 ms                                                         | 39.6 ms: 1.21x faster                                                |
| pickle_pure_python   | 280 us                                                          | 236 us: 1.19x faster                                                 |
| unpickle_pure_python | 189 us                                                          | 162 us: 1.17x faster                                                 |
| xml_etree_parse      | 120 ms                                                          | 104 ms: 1.15x faster                                                 |
| xml_etree_generate   | 61.6 ms                                                         | 53.6 ms: 1.15x faster                                                |
| xml_etree_iterparse  | 70.8 ms                                                         | 61.9 ms: 1.15x faster                                                |
| unpickle_list        | 2.98 us                                                         | 2.70 us: 1.11x faster                                                |
| json_loads           | 22.4 us                                                         | 20.9 us: 1.07x faster                                                |
| pickle_list          | 3.22 us                                                         | 3.32 us: 1.03x slower                                                |
| pickle               | 7.83 us                                                         | 8.12 us: 1.04x slower                                                |
| unpickle             | 9.82 us                                                         | 10.4 us: 1.06x slower                                                |
| pickle_dict          | 18.2 us                                                         | 19.7 us: 1.08x slower                                                |
| Geometric mean       | (ref)                                                           | 1.11x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 24.3 ms: 1.06x slower                                                |
| python_startup_no_site | 18.1 ms                                                         | 20.1 ms: 1.12x slower                                                |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.52 ms: 1.65x faster                                                |
| django_template | 36.0 ms                                                         | 33.4 ms: 1.08x faster                                                |
| genshi_text     | 21.0 ms                                                         | 23.6 ms: 1.13x slower                                                |
| genshi_xml      | 46.6 ms                                                         | 55.9 ms: 1.20x slower                                                |
| Geometric mean  | (ref)                                                           | 1.07x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 144 us: 2.74x faster                                                 |
| pidigits                 | 502 ms                                                          | 198 ms: 2.54x faster                                                 |
| sqlglot_normalize        | 230 ms                                                          | 102 ms: 2.26x faster                                                 |
| deepcopy_memo            | 29.6 us                                                         | 15.1 us: 1.96x faster                                                |
| deltablue                | 4.04 ms                                                         | 2.07 ms: 1.95x faster                                                |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 475 ms: 1.94x faster                                                 |
| async_tree_none          | 394 ms                                                          | 216 ms: 1.82x faster                                                 |
| async_tree_io            | 940 ms                                                          | 536 ms: 1.75x faster                                                 |
| spectral_norm            | 80.2 ms                                                         | 46.1 ms: 1.74x faster                                                |
| async_tree_memoization   | 467 ms                                                          | 272 ms: 1.72x faster                                                 |
| scimark_sor              | 115 ms                                                          | 67.4 ms: 1.71x faster                                                |
| crypto_pyaes             | 81.3 ms                                                         | 48.6 ms: 1.67x faster                                                |
| logging_silent           | 97.9 ns                                                         | 58.5 ns: 1.67x faster                                                |
| mako                     | 9.10 ms                                                         | 5.52 ms: 1.65x faster                                                |
| nbody                    | 79.1 ms                                                         | 49.5 ms: 1.60x faster                                                |
| float                    | 69.6 ms                                                         | 44.1 ms: 1.58x faster                                                |
| pyflate                  | 422 ms                                                          | 279 ms: 1.51x faster                                                 |
| scimark_lu               | 89.8 ms                                                         | 59.7 ms: 1.50x faster                                                |
| comprehensions           | 17.7 us                                                         | 11.9 us: 1.50x faster                                                |
| go                       | 146 ms                                                          | 99.3 ms: 1.47x faster                                                |
| pylint                   | 384 ms                                                          | 268 ms: 1.43x faster                                                 |
| json_dumps               | 9.82 ms                                                         | 7.06 ms: 1.39x faster                                                |
| richards_super           | 49.9 ms                                                         | 35.9 ms: 1.39x faster                                                |
| chaos                    | 74.4 ms                                                         | 55.1 ms: 1.35x faster                                                |
| generators               | 31.6 ms                                                         | 23.7 ms: 1.33x faster                                                |
| fannkuch                 | 317 ms                                                          | 243 ms: 1.31x faster                                                 |
| deepcopy                 | 310 us                                                          | 238 us: 1.30x faster                                                 |
| pycparser                | 1.04 sec                                                        | 819 ms: 1.27x faster                                                 |
| sqlglot_parse            | 1.33 ms                                                         | 1.06 ms: 1.26x faster                                                |
| scimark_fft              | 216 ms                                                          | 173 ms: 1.25x faster                                                 |
| hexiom                   | 6.13 ms                                                         | 4.91 ms: 1.25x faster                                                |
| tomli_loads              | 1.91 sec                                                        | 1.54 sec: 1.24x faster                                               |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.62 ms: 1.24x faster                                                |
| richards                 | 40.3 ms                                                         | 32.9 ms: 1.22x faster                                                |
| scimark_monte_carlo      | 61.9 ms                                                         | 50.6 ms: 1.22x faster                                                |
| raytrace                 | 303 ms                                                          | 248 ms: 1.22x faster                                                 |
| dulwich_log              | 58.5 ms                                                         | 48.1 ms: 1.22x faster                                                |
| xml_etree_process        | 48.1 ms                                                         | 39.6 ms: 1.21x faster                                                |
| sqlite_synth             | 2.29 us                                                         | 1.89 us: 1.21x faster                                                |
| asyncio_tcp              | 744 ms                                                          | 620 ms: 1.20x faster                                                 |
| pickle_pure_python       | 280 us                                                          | 236 us: 1.19x faster                                                 |
| thrift                   | 902 us                                                          | 762 us: 1.18x faster                                                 |
| tornado_http             | 118 ms                                                          | 99.4 ms: 1.18x faster                                                |
| json                     | 4.76 ms                                                         | 4.06 ms: 1.17x faster                                                |
| unpickle_pure_python     | 189 us                                                          | 162 us: 1.17x faster                                                 |
| sqlglot_transpile        | 1.58 ms                                                         | 1.35 ms: 1.17x faster                                                |
| xml_etree_parse          | 120 ms                                                          | 104 ms: 1.15x faster                                                 |
| xml_etree_generate       | 61.6 ms                                                         | 53.6 ms: 1.15x faster                                                |
| xml_etree_iterparse      | 70.8 ms                                                         | 61.9 ms: 1.15x faster                                                |
| regex_compile            | 117 ms                                                          | 103 ms: 1.14x faster                                                 |
| html5lib                 | 52.1 ms                                                         | 46.6 ms: 1.12x faster                                                |
| bench_thread_pool        | 1.12 ms                                                         | 1.00 ms: 1.12x faster                                                |
| nqueens                  | 87.1 ms                                                         | 78.2 ms: 1.11x faster                                                |
| pprint_safe_repr         | 658 ms                                                          | 595 ms: 1.11x faster                                                 |
| unpickle_list            | 2.98 us                                                         | 2.70 us: 1.11x faster                                                |
| mdp                      | 1.83 sec                                                        | 1.66 sec: 1.10x faster                                               |
| pprint_pformat           | 1.37 sec                                                        | 1.26 sec: 1.09x faster                                               |
| meteor_contest           | 80.0 ms                                                         | 74.2 ms: 1.08x faster                                                |
| regex_dna                | 131 ms                                                          | 121 ms: 1.08x faster                                                 |
| django_template          | 36.0 ms                                                         | 33.4 ms: 1.08x faster                                                |
| sympy_sum                | 122 ms                                                          | 114 ms: 1.08x faster                                                 |
| json_loads               | 22.4 us                                                         | 20.9 us: 1.07x faster                                                |
| deepcopy_reduce          | 2.68 us                                                         | 2.51 us: 1.07x faster                                                |
| 2to3                     | 265 ms                                                          | 258 ms: 1.03x faster                                                 |
| sympy_str                | 229 ms                                                          | 223 ms: 1.03x faster                                                 |
| regex_v8                 | 15.8 ms                                                         | 15.8 ms: 1.00x slower                                                |
| sympy_integrate          | 16.6 ms                                                         | 16.8 ms: 1.01x slower                                                |
| sympy_expand             | 391 ms                                                          | 399 ms: 1.02x slower                                                 |
| pathlib                  | 81.2 ms                                                         | 83.5 ms: 1.03x slower                                                |
| docutils                 | 1.95 sec                                                        | 2.01 sec: 1.03x slower                                               |
| pickle_list              | 3.22 us                                                         | 3.32 us: 1.03x slower                                                |
| pickle                   | 7.83 us                                                         | 8.12 us: 1.04x slower                                                |
| unpack_sequence          | 40.0 ns                                                         | 41.8 ns: 1.04x slower                                                |
| unpickle                 | 9.82 us                                                         | 10.4 us: 1.06x slower                                                |
| python_startup           | 22.9 ms                                                         | 24.3 ms: 1.06x slower                                                |
| sqlglot_optimize         | 44.7 ms                                                         | 47.7 ms: 1.07x slower                                                |
| logging_simple           | 7.29 us                                                         | 7.80 us: 1.07x slower                                                |
| create_gc_cycles         | 694 us                                                          | 742 us: 1.07x slower                                                 |
| coroutines               | 17.9 ms                                                         | 19.2 ms: 1.07x slower                                                |
| logging_format           | 7.91 us                                                         | 8.51 us: 1.08x slower                                                |
| pickle_dict              | 18.2 us                                                         | 19.7 us: 1.08x slower                                                |
| coverage                 | 46.6 ms                                                         | 51.6 ms: 1.11x slower                                                |
| python_startup_no_site   | 18.1 ms                                                         | 20.1 ms: 1.12x slower                                                |
| gc_traversal             | 1.28 ms                                                         | 1.44 ms: 1.12x slower                                                |
| genshi_text              | 21.0 ms                                                         | 23.6 ms: 1.13x slower                                                |
| bench_mp_pool            | 66.4 ms                                                         | 75.9 ms: 1.14x slower                                                |
| regex_effbot             | 1.66 ms                                                         | 1.95 ms: 1.17x slower                                                |
| telco                    | 4.83 ms                                                         | 5.68 ms: 1.18x slower                                                |
| genshi_xml               | 46.6 ms                                                         | 55.9 ms: 1.20x slower                                                |
| async_generators         | 241 ms                                                          | 327 ms: 1.36x slower                                                 |
| Geometric mean           | (ref)                                                           | 1.21x faster                                                         |

Benchmark hidden because not significant (1): asyncio_tcp_ssl
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240924-3.14.0a0-e256a75-JIT/bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown