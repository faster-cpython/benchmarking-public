# Results vs. 3.10.4

- fork: python
- ref: 5b941e57c71d7d0ab983
- machine: windows-x86
- commit hash: 5b941e5
- commit date: 2024-05-11
- overall geometric mean: 1.20x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 234 ms: 1.13x faster                                                           |
| chameleon      | 6.42 ms                                                         | 5.83 ms: 1.10x faster                                                          |
| docutils       | 1.95 sec                                                        | 1.81 sec: 1.07x faster                                                         |
| html5lib       | 52.1 ms                                                         | 44.8 ms: 1.16x faster                                                          |
| tornado_http   | 118 ms                                                          | 94.6 ms: 1.24x faster                                                          |
| Geometric mean | (ref)                                                           | 1.14x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 470 ms: 1.96x faster                                                           |
| async_tree_io           | 940 ms                                                          | 538 ms: 1.75x faster                                                           |
| async_tree_none         | 394 ms                                                          | 228 ms: 1.72x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 277 ms: 1.69x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.78x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 199 ms: 2.52x faster                                                           |
| float          | 69.6 ms                                                         | 52.0 ms: 1.34x faster                                                          |
| nbody          | 79.1 ms                                                         | 75.0 ms: 1.06x faster                                                          |
| Geometric mean | (ref)                                                           | 1.53x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 97.3 ms: 1.20x faster                                                          |
| regex_dna      | 131 ms                                                          | 120 ms: 1.09x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 16.2 ms: 1.03x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.92 ms: 1.16x slower                                                          |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.79 ms: 1.45x faster                                                          |
| pickle_pure_python   | 280 us                                                          | 212 us: 1.32x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 147 us: 1.29x faster                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.63 sec: 1.17x faster                                                         |
| xml_etree_process    | 48.1 ms                                                         | 41.7 ms: 1.16x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 105 ms: 1.15x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 63.9 ms: 1.11x faster                                                          |
| json_loads           | 22.4 us                                                         | 20.3 us: 1.10x faster                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 58.1 ms: 1.06x faster                                                          |
| unpickle_list        | 2.98 us                                                         | 3.00 us: 1.01x slower                                                          |
| pickle               | 7.83 us                                                         | 7.92 us: 1.01x slower                                                          |
| unpickle             | 9.82 us                                                         | 9.98 us: 1.02x slower                                                          |
| pickle_list          | 3.22 us                                                         | 3.45 us: 1.07x slower                                                          |
| pickle_dict          | 18.2 us                                                         | 20.6 us: 1.13x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.10x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 22.1 ms: 1.04x faster                                                          |
| python_startup_no_site | 18.1 ms                                                         | 18.4 ms: 1.02x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.01x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 6.85 ms: 1.33x faster                                                          |
| django_template | 36.0 ms                                                         | 30.1 ms: 1.20x faster                                                          |
| genshi_text     | 21.0 ms                                                         | 20.1 ms: 1.05x faster                                                          |
| genshi_xml      | 46.6 ms                                                         | 45.1 ms: 1.03x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.15x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 133 us: 2.98x faster                                                           |
| pidigits                 | 502 ms                                                          | 199 ms: 2.52x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 470 ms: 1.96x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.20 ms: 1.83x faster                                                          |
| pylint                   | 384 ms                                                          | 219 ms: 1.75x faster                                                           |
| async_tree_io            | 940 ms                                                          | 538 ms: 1.75x faster                                                           |
| async_tree_none          | 394 ms                                                          | 228 ms: 1.72x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 277 ms: 1.69x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 58.2 ns: 1.68x faster                                                          |
| raytrace                 | 303 ms                                                          | 184 ms: 1.64x faster                                                           |
| chaos                    | 74.4 ms                                                         | 47.3 ms: 1.57x faster                                                          |
| scimark_lu               | 89.8 ms                                                         | 59.9 ms: 1.50x faster                                                          |
| comprehensions           | 17.7 us                                                         | 11.9 us: 1.49x faster                                                          |
| generators               | 31.6 ms                                                         | 21.3 ms: 1.48x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 55.4 ms: 1.47x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 6.79 ms: 1.45x faster                                                          |
| hexiom                   | 6.13 ms                                                         | 4.28 ms: 1.43x faster                                                          |
| go                       | 146 ms                                                          | 102 ms: 1.42x faster                                                           |
| richards_super           | 49.9 ms                                                         | 35.1 ms: 1.42x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 958 us: 1.39x faster                                                           |
| pyflate                  | 422 ms                                                          | 304 ms: 1.39x faster                                                           |
| float                    | 69.6 ms                                                         | 52.0 ms: 1.34x faster                                                          |
| scimark_sor              | 115 ms                                                          | 86.2 ms: 1.34x faster                                                          |
| pycparser                | 1.04 sec                                                        | 782 ms: 1.33x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.19 ms: 1.33x faster                                                          |
| mako                     | 9.10 ms                                                         | 6.85 ms: 1.33x faster                                                          |
| pickle_pure_python       | 280 us                                                          | 212 us: 1.32x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 46.9 ms: 1.32x faster                                                          |
| richards                 | 40.3 ms                                                         | 31.2 ms: 1.29x faster                                                          |
| unpickle_pure_python     | 189 us                                                          | 147 us: 1.29x faster                                                           |
| thrift                   | 902 us                                                          | 706 us: 1.28x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 68.2 ms: 1.28x faster                                                          |
| deepcopy_memo            | 29.6 us                                                         | 23.5 us: 1.26x faster                                                          |
| tornado_http             | 118 ms                                                          | 94.6 ms: 1.24x faster                                                          |
| regex_compile            | 117 ms                                                          | 97.3 ms: 1.20x faster                                                          |
| django_template          | 36.0 ms                                                         | 30.1 ms: 1.20x faster                                                          |
| fannkuch                 | 317 ms                                                          | 266 ms: 1.19x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 67.9 ms: 1.18x faster                                                          |
| sqlite_synth             | 2.29 us                                                         | 1.94 us: 1.18x faster                                                          |
| sympy_sum                | 122 ms                                                          | 104 ms: 1.17x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.63 sec: 1.17x faster                                                         |
| html5lib                 | 52.1 ms                                                         | 44.8 ms: 1.16x faster                                                          |
| xml_etree_process        | 48.1 ms                                                         | 41.7 ms: 1.16x faster                                                          |
| sympy_integrate          | 16.6 ms                                                         | 14.4 ms: 1.15x faster                                                          |
| json                     | 4.76 ms                                                         | 4.15 ms: 1.15x faster                                                          |
| xml_etree_parse          | 120 ms                                                          | 105 ms: 1.15x faster                                                           |
| 2to3                     | 265 ms                                                          | 234 ms: 1.13x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.87 ms: 1.13x faster                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 1000 us: 1.12x faster                                                          |
| deepcopy                 | 310 us                                                          | 277 us: 1.12x faster                                                           |
| coroutines               | 17.9 ms                                                         | 16.1 ms: 1.11x faster                                                          |
| mdp                      | 1.83 sec                                                        | 1.64 sec: 1.11x faster                                                         |
| sympy_str                | 229 ms                                                          | 206 ms: 1.11x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 63.9 ms: 1.11x faster                                                          |
| json_loads               | 22.4 us                                                         | 20.3 us: 1.10x faster                                                          |
| pprint_pformat           | 1.37 sec                                                        | 1.24 sec: 1.10x faster                                                         |
| chameleon                | 6.42 ms                                                         | 5.83 ms: 1.10x faster                                                          |
| sqlglot_normalize        | 230 ms                                                          | 211 ms: 1.09x faster                                                           |
| pprint_safe_repr         | 658 ms                                                          | 604 ms: 1.09x faster                                                           |
| regex_dna                | 131 ms                                                          | 120 ms: 1.09x faster                                                           |
| docutils                 | 1.95 sec                                                        | 1.81 sec: 1.07x faster                                                         |
| sympy_expand             | 391 ms                                                          | 364 ms: 1.07x faster                                                           |
| asyncio_tcp              | 744 ms                                                          | 694 ms: 1.07x faster                                                           |
| meteor_contest           | 80.0 ms                                                         | 74.8 ms: 1.07x faster                                                          |
| sqlglot_optimize         | 44.7 ms                                                         | 41.9 ms: 1.07x faster                                                          |
| xml_etree_generate       | 61.6 ms                                                         | 58.1 ms: 1.06x faster                                                          |
| nbody                    | 79.1 ms                                                         | 75.0 ms: 1.06x faster                                                          |
| scimark_fft              | 216 ms                                                          | 206 ms: 1.05x faster                                                           |
| genshi_text              | 21.0 ms                                                         | 20.1 ms: 1.05x faster                                                          |
| python_startup           | 22.9 ms                                                         | 22.1 ms: 1.04x faster                                                          |
| genshi_xml               | 46.6 ms                                                         | 45.1 ms: 1.03x faster                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.67 us: 1.01x faster                                                          |
| flaskblogging            | 2.03 sec                                                        | 2.03 sec: 1.00x slower                                                         |
| unpickle_list            | 2.98 us                                                         | 3.00 us: 1.01x slower                                                          |
| pickle                   | 7.83 us                                                         | 7.92 us: 1.01x slower                                                          |
| unpickle                 | 9.82 us                                                         | 9.98 us: 1.02x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 18.4 ms: 1.02x slower                                                          |
| logging_simple           | 7.29 us                                                         | 7.44 us: 1.02x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.08 us: 1.02x slower                                                          |
| regex_v8                 | 15.8 ms                                                         | 16.2 ms: 1.03x slower                                                          |
| coverage                 | 46.6 ms                                                         | 48.7 ms: 1.05x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 70.6 ms: 1.06x slower                                                          |
| pickle_list              | 3.22 us                                                         | 3.45 us: 1.07x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 745 us: 1.07x slower                                                           |
| pathlib                  | 81.2 ms                                                         | 88.5 ms: 1.09x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.43 ms: 1.12x slower                                                          |
| pickle_dict              | 18.2 us                                                         | 20.6 us: 1.13x slower                                                          |
| async_generators         | 241 ms                                                          | 279 ms: 1.16x slower                                                           |
| regex_effbot             | 1.66 ms                                                         | 1.92 ms: 1.16x slower                                                          |
| telco                    | 4.83 ms                                                         | 5.78 ms: 1.20x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.20x faster                                                                   |

Benchmark hidden because not significant (1): asyncio_tcp_ssl
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240511-3.14.0a0-5b941e5/bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown