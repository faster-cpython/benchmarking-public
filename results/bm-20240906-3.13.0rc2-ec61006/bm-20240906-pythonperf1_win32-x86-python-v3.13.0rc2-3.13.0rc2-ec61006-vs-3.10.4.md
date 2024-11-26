# Results vs. 3.10.4

- fork: python
- ref: v3.13.0rc2
- machine: windows-x86
- commit hash: ec61006
- commit date: 2024-09-06
- overall geometric mean: 1.132x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 245 ms: 1.08x faster                                                  |
| chameleon      | 6.42 ms                                                         | 5.83 ms: 1.10x faster                                                 |
| docutils       | 1.95 sec                                                        | 1.85 sec: 1.05x faster                                                |
| html5lib       | 52.1 ms                                                         | 45.7 ms: 1.14x faster                                                 |
| tornado_http   | 118 ms                                                          | 104 ms: 1.13x faster                                                  |
| Geometric mean | (ref)                                                           | 1.10x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|-------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 475 ms: 1.94x faster                                                  |
| async_tree_io           | 940 ms                                                          | 537 ms: 1.75x faster                                                  |
| async_tree_none         | 394 ms                                                          | 230 ms: 1.71x faster                                                  |
| async_tree_memoization  | 467 ms                                                          | 279 ms: 1.68x faster                                                  |
| Geometric mean          | (ref)                                                           | 1.77x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 199 ms: 2.52x faster                                                  |
| float          | 69.6 ms                                                         | 53.5 ms: 1.30x faster                                                 |
| Geometric mean | (ref)                                                           | 1.48x faster                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 101 ms: 1.15x faster                                                  |
| regex_dna      | 131 ms                                                          | 119 ms: 1.09x faster                                                  |
| regex_v8       | 15.8 ms                                                         | 15.9 ms: 1.01x slower                                                 |
| regex_effbot   | 1.66 ms                                                         | 1.88 ms: 1.13x slower                                                 |
| Geometric mean | (ref)                                                           | 1.02x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.03 ms: 1.40x faster                                                 |
| pickle_pure_python   | 280 us                                                          | 228 us: 1.23x faster                                                  |
| unpickle_pure_python | 189 us                                                          | 155 us: 1.22x faster                                                  |
| tomli_loads          | 1.91 sec                                                        | 1.65 sec: 1.16x faster                                                |
| xml_etree_parse      | 120 ms                                                          | 107 ms: 1.13x faster                                                  |
| json_loads           | 22.4 us                                                         | 20.6 us: 1.09x faster                                                 |
| xml_etree_iterparse  | 70.8 ms                                                         | 65.3 ms: 1.08x faster                                                 |
| xml_etree_process    | 48.1 ms                                                         | 44.9 ms: 1.07x faster                                                 |
| unpickle_list        | 2.98 us                                                         | 2.92 us: 1.02x faster                                                 |
| pickle_list          | 3.22 us                                                         | 3.15 us: 1.02x faster                                                 |
| xml_etree_generate   | 61.6 ms                                                         | 62.2 ms: 1.01x slower                                                 |
| unpickle             | 9.82 us                                                         | 10.0 us: 1.02x slower                                                 |
| pickle               | 7.83 us                                                         | 8.01 us: 1.02x slower                                                 |
| pickle_dict          | 18.2 us                                                         | 20.4 us: 1.12x slower                                                 |
| Geometric mean       | (ref)                                                           | 1.08x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 24.2 ms: 1.05x slower                                                 |
| python_startup_no_site | 18.1 ms                                                         | 19.9 ms: 1.10x slower                                                 |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.08 ms: 1.29x faster                                                 |
| django_template | 36.0 ms                                                         | 31.1 ms: 1.16x faster                                                 |
| genshi_text     | 21.0 ms                                                         | 19.8 ms: 1.06x faster                                                 |
| genshi_xml      | 46.6 ms                                                         | 43.9 ms: 1.06x faster                                                 |
| Geometric mean  | (ref)                                                           | 1.14x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|--------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 139 us: 2.86x faster                                                  |
| pidigits                 | 502 ms                                                          | 199 ms: 2.52x faster                                                  |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 475 ms: 1.94x faster                                                  |
| pylint                   | 384 ms                                                          | 210 ms: 1.83x faster                                                  |
| async_tree_io            | 940 ms                                                          | 537 ms: 1.75x faster                                                  |
| deltablue                | 4.04 ms                                                         | 2.34 ms: 1.72x faster                                                 |
| async_tree_none          | 394 ms                                                          | 230 ms: 1.71x faster                                                  |
| async_tree_memoization   | 467 ms                                                          | 279 ms: 1.68x faster                                                  |
| logging_silent           | 97.9 ns                                                         | 60.1 ns: 1.63x faster                                                 |
| raytrace                 | 303 ms                                                          | 193 ms: 1.57x faster                                                  |
| chaos                    | 74.4 ms                                                         | 48.9 ms: 1.52x faster                                                 |
| crypto_pyaes             | 81.3 ms                                                         | 55.4 ms: 1.47x faster                                                 |
| generators               | 31.6 ms                                                         | 21.8 ms: 1.45x faster                                                 |
| scimark_lu               | 89.8 ms                                                         | 62.0 ms: 1.45x faster                                                 |
| comprehensions           | 17.7 us                                                         | 12.5 us: 1.42x faster                                                 |
| json_dumps               | 9.82 ms                                                         | 7.03 ms: 1.40x faster                                                 |
| go                       | 146 ms                                                          | 108 ms: 1.35x faster                                                  |
| sqlglot_parse            | 1.33 ms                                                         | 989 us: 1.34x faster                                                  |
| hexiom                   | 6.13 ms                                                         | 4.58 ms: 1.34x faster                                                 |
| richards_super           | 49.9 ms                                                         | 37.7 ms: 1.32x faster                                                 |
| pyflate                  | 422 ms                                                          | 319 ms: 1.32x faster                                                  |
| scimark_sor              | 115 ms                                                          | 87.5 ms: 1.32x faster                                                 |
| pycparser                | 1.04 sec                                                        | 798 ms: 1.31x faster                                                  |
| sqlglot_transpile        | 1.58 ms                                                         | 1.22 ms: 1.30x faster                                                 |
| float                    | 69.6 ms                                                         | 53.5 ms: 1.30x faster                                                 |
| mako                     | 9.10 ms                                                         | 7.08 ms: 1.29x faster                                                 |
| scimark_monte_carlo      | 61.9 ms                                                         | 49.2 ms: 1.26x faster                                                 |
| nqueens                  | 87.1 ms                                                         | 69.5 ms: 1.25x faster                                                 |
| pickle_pure_python       | 280 us                                                          | 228 us: 1.23x faster                                                  |
| unpickle_pure_python     | 189 us                                                          | 155 us: 1.22x faster                                                  |
| richards                 | 40.3 ms                                                         | 33.3 ms: 1.21x faster                                                 |
| dulwich_log              | 58.5 ms                                                         | 49.2 ms: 1.19x faster                                                 |
| deepcopy_memo            | 29.6 us                                                         | 24.9 us: 1.19x faster                                                 |
| django_template          | 36.0 ms                                                         | 31.1 ms: 1.16x faster                                                 |
| tomli_loads              | 1.91 sec                                                        | 1.65 sec: 1.16x faster                                                |
| sqlite_synth             | 2.29 us                                                         | 1.98 us: 1.16x faster                                                 |
| regex_compile            | 117 ms                                                          | 101 ms: 1.15x faster                                                  |
| sympy_sum                | 122 ms                                                          | 106 ms: 1.15x faster                                                  |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.82 ms: 1.15x faster                                                 |
| spectral_norm            | 80.2 ms                                                         | 70.3 ms: 1.14x faster                                                 |
| html5lib                 | 52.1 ms                                                         | 45.7 ms: 1.14x faster                                                 |
| tornado_http             | 118 ms                                                          | 104 ms: 1.13x faster                                                  |
| xml_etree_parse          | 120 ms                                                          | 107 ms: 1.13x faster                                                  |
| coroutines               | 17.9 ms                                                         | 16.0 ms: 1.12x faster                                                 |
| sympy_integrate          | 16.6 ms                                                         | 14.9 ms: 1.12x faster                                                 |
| json                     | 4.76 ms                                                         | 4.27 ms: 1.12x faster                                                 |
| fannkuch                 | 317 ms                                                          | 286 ms: 1.11x faster                                                  |
| bench_thread_pool        | 1.12 ms                                                         | 1.01 ms: 1.11x faster                                                 |
| mdp                      | 1.83 sec                                                        | 1.65 sec: 1.10x faster                                                |
| chameleon                | 6.42 ms                                                         | 5.83 ms: 1.10x faster                                                 |
| sqlglot_optimize         | 44.7 ms                                                         | 40.6 ms: 1.10x faster                                                 |
| pprint_pformat           | 1.37 sec                                                        | 1.25 sec: 1.10x faster                                                |
| sqlglot_normalize        | 230 ms                                                          | 210 ms: 1.10x faster                                                  |
| regex_dna                | 131 ms                                                          | 119 ms: 1.09x faster                                                  |
| json_loads               | 22.4 us                                                         | 20.6 us: 1.09x faster                                                 |
| sympy_str                | 229 ms                                                          | 211 ms: 1.09x faster                                                  |
| xml_etree_iterparse      | 70.8 ms                                                         | 65.3 ms: 1.08x faster                                                 |
| pprint_safe_repr         | 658 ms                                                          | 608 ms: 1.08x faster                                                  |
| 2to3                     | 265 ms                                                          | 245 ms: 1.08x faster                                                  |
| deepcopy                 | 310 us                                                          | 288 us: 1.07x faster                                                  |
| xml_etree_process        | 48.1 ms                                                         | 44.9 ms: 1.07x faster                                                 |
| genshi_text              | 21.0 ms                                                         | 19.8 ms: 1.06x faster                                                 |
| genshi_xml               | 46.6 ms                                                         | 43.9 ms: 1.06x faster                                                 |
| sympy_expand             | 391 ms                                                          | 368 ms: 1.06x faster                                                  |
| scimark_fft              | 216 ms                                                          | 204 ms: 1.06x faster                                                  |
| meteor_contest           | 80.0 ms                                                         | 75.8 ms: 1.06x faster                                                 |
| docutils                 | 1.95 sec                                                        | 1.85 sec: 1.05x faster                                                |
| asyncio_tcp              | 744 ms                                                          | 717 ms: 1.04x faster                                                  |
| unpickle_list            | 2.98 us                                                         | 2.92 us: 1.02x faster                                                 |
| pickle_list              | 3.22 us                                                         | 3.15 us: 1.02x faster                                                 |
| flaskblogging            | 2.03 sec                                                        | 2.04 sec: 1.01x slower                                                |
| deepcopy_reduce          | 2.68 us                                                         | 2.70 us: 1.01x slower                                                 |
| regex_v8                 | 15.8 ms                                                         | 15.9 ms: 1.01x slower                                                 |
| xml_etree_generate       | 61.6 ms                                                         | 62.2 ms: 1.01x slower                                                 |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.2 sec: 1.01x slower                                                |
| unpickle                 | 9.82 us                                                         | 10.0 us: 1.02x slower                                                 |
| pickle                   | 7.83 us                                                         | 8.01 us: 1.02x slower                                                 |
| python_startup           | 22.9 ms                                                         | 24.2 ms: 1.05x slower                                                 |
| logging_simple           | 7.29 us                                                         | 7.79 us: 1.07x slower                                                 |
| unpack_sequence          | 40.0 ns                                                         | 42.8 ns: 1.07x slower                                                 |
| logging_format           | 7.91 us                                                         | 8.48 us: 1.07x slower                                                 |
| create_gc_cycles         | 694 us                                                          | 751 us: 1.08x slower                                                  |
| pathlib                  | 81.2 ms                                                         | 88.7 ms: 1.09x slower                                                 |
| bench_mp_pool            | 66.4 ms                                                         | 73.1 ms: 1.10x slower                                                 |
| python_startup_no_site   | 18.1 ms                                                         | 19.9 ms: 1.10x slower                                                 |
| pickle_dict              | 18.2 us                                                         | 20.4 us: 1.12x slower                                                 |
| gc_traversal             | 1.28 ms                                                         | 1.44 ms: 1.13x slower                                                 |
| regex_effbot             | 1.66 ms                                                         | 1.88 ms: 1.13x slower                                                 |
| async_generators         | 241 ms                                                          | 278 ms: 1.15x slower                                                  |
| telco                    | 4.83 ms                                                         | 6.56 ms: 1.36x slower                                                 |
| coverage                 | 46.6 ms                                                         | 324 ms: 6.97x slower                                                  |
| thrift                   | 902 us                                                          | 10.1 ms: 11.23x slower                                                |
| Geometric mean           | (ref)                                                           | 1.12x faster                                                          |

Benchmark hidden because not significant (1): nbody
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240906-3.13.0rc2-ec61006/bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.132x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown