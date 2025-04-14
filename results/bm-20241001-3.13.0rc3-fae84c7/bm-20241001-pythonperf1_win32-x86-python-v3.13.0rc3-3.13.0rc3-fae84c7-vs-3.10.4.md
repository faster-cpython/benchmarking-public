# Results vs. 3.10.4

- fork: python
- ref: v3.13.0rc3
- machine: windows-x86
- commit hash: fae84c7
- commit date: 2024-10-01
- overall geometric mean: 1.135x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 243 ms: 1.09x faster                                                  |
| chameleon      | 6.42 ms                                                         | 5.98 ms: 1.07x faster                                                 |
| docutils       | 1.95 sec                                                        | 1.77 sec: 1.10x faster                                                |
| html5lib       | 52.1 ms                                                         | 45.6 ms: 1.14x faster                                                 |
| tornado_http   | 118 ms                                                          | 102 ms: 1.15x faster                                                  |
| Geometric mean | (ref)                                                           | 1.11x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|-------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 473 ms: 1.95x faster                                                  |
| async_tree_io           | 940 ms                                                          | 508 ms: 1.85x faster                                                  |
| async_tree_none         | 394 ms                                                          | 231 ms: 1.70x faster                                                  |
| async_tree_memoization  | 467 ms                                                          | 281 ms: 1.66x faster                                                  |
| Geometric mean          | (ref)                                                           | 1.79x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 200 ms: 2.52x faster                                                  |
| float          | 69.6 ms                                                         | 55.2 ms: 1.26x faster                                                 |
| nbody          | 79.1 ms                                                         | 78.0 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                           | 1.48x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 99.5 ms: 1.17x faster                                                 |
| regex_dna      | 131 ms                                                          | 119 ms: 1.10x faster                                                  |
| regex_effbot   | 1.66 ms                                                         | 1.90 ms: 1.15x slower                                                 |
| Geometric mean | (ref)                                                           | 1.03x faster                                                          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.48 ms: 1.31x faster                                                 |
| pickle_pure_python   | 280 us                                                          | 231 us: 1.21x faster                                                  |
| unpickle_pure_python | 189 us                                                          | 157 us: 1.21x faster                                                  |
| xml_etree_parse      | 120 ms                                                          | 103 ms: 1.17x faster                                                  |
| tomli_loads          | 1.91 sec                                                        | 1.67 sec: 1.15x faster                                                |
| xml_etree_iterparse  | 70.8 ms                                                         | 62.2 ms: 1.14x faster                                                 |
| xml_etree_process    | 48.1 ms                                                         | 44.3 ms: 1.09x faster                                                 |
| json_loads           | 22.4 us                                                         | 20.6 us: 1.09x faster                                                 |
| unpickle_list        | 2.98 us                                                         | 2.78 us: 1.07x faster                                                 |
| pickle               | 7.83 us                                                         | 7.79 us: 1.01x faster                                                 |
| xml_etree_generate   | 61.6 ms                                                         | 62.6 ms: 1.02x slower                                                 |
| pickle_list          | 3.22 us                                                         | 3.32 us: 1.03x slower                                                 |
| unpickle             | 9.82 us                                                         | 10.3 us: 1.05x slower                                                 |
| pickle_dict          | 18.2 us                                                         | 20.3 us: 1.11x slower                                                 |
| Geometric mean       | (ref)                                                           | 1.08x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 24.7 ms: 1.08x slower                                                 |
| python_startup_no_site | 18.1 ms                                                         | 20.6 ms: 1.14x slower                                                 |
| Geometric mean         | (ref)                                                           | 1.11x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.06 ms: 1.29x faster                                                 |
| django_template | 36.0 ms                                                         | 29.3 ms: 1.23x faster                                                 |
| genshi_xml      | 46.6 ms                                                         | 45.1 ms: 1.03x faster                                                 |
| genshi_text     | 21.0 ms                                                         | 20.9 ms: 1.01x faster                                                 |
| Geometric mean  | (ref)                                                           | 1.13x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|--------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 137 us: 2.89x faster                                                  |
| pidigits                 | 502 ms                                                          | 200 ms: 2.52x faster                                                  |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 473 ms: 1.95x faster                                                  |
| async_tree_io            | 940 ms                                                          | 508 ms: 1.85x faster                                                  |
| deltablue                | 4.04 ms                                                         | 2.27 ms: 1.77x faster                                                 |
| pylint                   | 384 ms                                                          | 222 ms: 1.73x faster                                                  |
| async_tree_none          | 394 ms                                                          | 231 ms: 1.70x faster                                                  |
| async_tree_memoization   | 467 ms                                                          | 281 ms: 1.66x faster                                                  |
| logging_silent           | 97.9 ns                                                         | 59.5 ns: 1.65x faster                                                 |
| raytrace                 | 303 ms                                                          | 191 ms: 1.58x faster                                                  |
| chaos                    | 74.4 ms                                                         | 48.3 ms: 1.54x faster                                                 |
| generators               | 31.6 ms                                                         | 21.5 ms: 1.47x faster                                                 |
| scimark_lu               | 89.8 ms                                                         | 62.1 ms: 1.44x faster                                                 |
| comprehensions           | 17.7 us                                                         | 12.4 us: 1.43x faster                                                 |
| crypto_pyaes             | 81.3 ms                                                         | 57.5 ms: 1.41x faster                                                 |
| sqlglot_parse            | 1.33 ms                                                         | 956 us: 1.39x faster                                                  |
| go                       | 146 ms                                                          | 105 ms: 1.38x faster                                                  |
| hexiom                   | 6.13 ms                                                         | 4.50 ms: 1.36x faster                                                 |
| richards_super           | 49.9 ms                                                         | 37.0 ms: 1.35x faster                                                 |
| pyflate                  | 422 ms                                                          | 313 ms: 1.35x faster                                                  |
| sqlglot_transpile        | 1.58 ms                                                         | 1.19 ms: 1.33x faster                                                 |
| json_dumps               | 9.82 ms                                                         | 7.48 ms: 1.31x faster                                                 |
| scimark_sor              | 115 ms                                                          | 88.0 ms: 1.31x faster                                                 |
| scimark_monte_carlo      | 61.9 ms                                                         | 47.9 ms: 1.29x faster                                                 |
| mako                     | 9.10 ms                                                         | 7.06 ms: 1.29x faster                                                 |
| pycparser                | 1.04 sec                                                        | 810 ms: 1.29x faster                                                  |
| float                    | 69.6 ms                                                         | 55.2 ms: 1.26x faster                                                 |
| nqueens                  | 87.1 ms                                                         | 69.1 ms: 1.26x faster                                                 |
| django_template          | 36.0 ms                                                         | 29.3 ms: 1.23x faster                                                 |
| pickle_pure_python       | 280 us                                                          | 231 us: 1.21x faster                                                  |
| unpickle_pure_python     | 189 us                                                          | 157 us: 1.21x faster                                                  |
| richards                 | 40.3 ms                                                         | 33.5 ms: 1.20x faster                                                 |
| dulwich_log              | 58.5 ms                                                         | 49.0 ms: 1.19x faster                                                 |
| regex_compile            | 117 ms                                                          | 99.5 ms: 1.17x faster                                                 |
| xml_etree_parse          | 120 ms                                                          | 103 ms: 1.17x faster                                                  |
| sqlite_synth             | 2.29 us                                                         | 1.98 us: 1.16x faster                                                 |
| sympy_sum                | 122 ms                                                          | 106 ms: 1.16x faster                                                  |
| deepcopy_memo            | 29.6 us                                                         | 25.7 us: 1.15x faster                                                 |
| tornado_http             | 118 ms                                                          | 102 ms: 1.15x faster                                                  |
| coroutines               | 17.9 ms                                                         | 15.6 ms: 1.15x faster                                                 |
| tomli_loads              | 1.91 sec                                                        | 1.67 sec: 1.15x faster                                                |
| html5lib                 | 52.1 ms                                                         | 45.6 ms: 1.14x faster                                                 |
| xml_etree_iterparse      | 70.8 ms                                                         | 62.2 ms: 1.14x faster                                                 |
| bench_thread_pool        | 1.12 ms                                                         | 989 us: 1.13x faster                                                  |
| fannkuch                 | 317 ms                                                          | 282 ms: 1.12x faster                                                  |
| json                     | 4.76 ms                                                         | 4.25 ms: 1.12x faster                                                 |
| sympy_integrate          | 16.6 ms                                                         | 14.9 ms: 1.12x faster                                                 |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.90 ms: 1.12x faster                                                 |
| mdp                      | 1.83 sec                                                        | 1.64 sec: 1.11x faster                                                |
| sqlglot_normalize        | 230 ms                                                          | 209 ms: 1.10x faster                                                  |
| sqlglot_optimize         | 44.7 ms                                                         | 40.5 ms: 1.10x faster                                                 |
| docutils                 | 1.95 sec                                                        | 1.77 sec: 1.10x faster                                                |
| regex_dna                | 131 ms                                                          | 119 ms: 1.10x faster                                                  |
| spectral_norm            | 80.2 ms                                                         | 73.1 ms: 1.10x faster                                                 |
| 2to3                     | 265 ms                                                          | 243 ms: 1.09x faster                                                  |
| pprint_pformat           | 1.37 sec                                                        | 1.25 sec: 1.09x faster                                                |
| xml_etree_process        | 48.1 ms                                                         | 44.3 ms: 1.09x faster                                                 |
| json_loads               | 22.4 us                                                         | 20.6 us: 1.09x faster                                                 |
| sympy_str                | 229 ms                                                          | 212 ms: 1.08x faster                                                  |
| pprint_safe_repr         | 658 ms                                                          | 610 ms: 1.08x faster                                                  |
| unpickle_list            | 2.98 us                                                         | 2.78 us: 1.07x faster                                                 |
| chameleon                | 6.42 ms                                                         | 5.98 ms: 1.07x faster                                                 |
| deepcopy                 | 310 us                                                          | 291 us: 1.07x faster                                                  |
| scimark_fft              | 216 ms                                                          | 205 ms: 1.05x faster                                                  |
| sympy_expand             | 391 ms                                                          | 371 ms: 1.05x faster                                                  |
| meteor_contest           | 80.0 ms                                                         | 76.3 ms: 1.05x faster                                                 |
| genshi_xml               | 46.6 ms                                                         | 45.1 ms: 1.03x faster                                                 |
| nbody                    | 79.1 ms                                                         | 78.0 ms: 1.01x faster                                                 |
| genshi_text              | 21.0 ms                                                         | 20.9 ms: 1.01x faster                                                 |
| pickle                   | 7.83 us                                                         | 7.79 us: 1.01x faster                                                 |
| flaskblogging            | 2.03 sec                                                        | 2.03 sec: 1.00x slower                                                |
| deepcopy_reduce          | 2.68 us                                                         | 2.72 us: 1.01x slower                                                 |
| xml_etree_generate       | 61.6 ms                                                         | 62.6 ms: 1.02x slower                                                 |
| pickle_list              | 3.22 us                                                         | 3.32 us: 1.03x slower                                                 |
| logging_format           | 7.91 us                                                         | 8.31 us: 1.05x slower                                                 |
| unpickle                 | 9.82 us                                                         | 10.3 us: 1.05x slower                                                 |
| logging_simple           | 7.29 us                                                         | 7.68 us: 1.05x slower                                                 |
| python_startup           | 22.9 ms                                                         | 24.7 ms: 1.08x slower                                                 |
| unpack_sequence          | 40.0 ns                                                         | 43.5 ns: 1.09x slower                                                 |
| pathlib                  | 81.2 ms                                                         | 88.3 ms: 1.09x slower                                                 |
| async_generators         | 241 ms                                                          | 263 ms: 1.09x slower                                                  |
| pickle_dict              | 18.2 us                                                         | 20.3 us: 1.11x slower                                                 |
| gc_traversal             | 1.28 ms                                                         | 1.45 ms: 1.13x slower                                                 |
| python_startup_no_site   | 18.1 ms                                                         | 20.6 ms: 1.14x slower                                                 |
| regex_effbot             | 1.66 ms                                                         | 1.90 ms: 1.15x slower                                                 |
| bench_mp_pool            | 66.4 ms                                                         | 76.8 ms: 1.16x slower                                                 |
| telco                    | 4.83 ms                                                         | 6.35 ms: 1.32x slower                                                 |
| coverage                 | 46.6 ms                                                         | 324 ms: 6.95x slower                                                  |
| thrift                   | 902 us                                                          | 10.1 ms: 11.21x slower                                                |
| Geometric mean           | (ref)                                                           | 1.12x faster                                                          |

Benchmark hidden because not significant (4): asyncio_tcp, asyncio_tcp_ssl, regex_v8, create_gc_cycles
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20241001-3.13.0rc3-fae84c7/bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.135x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown