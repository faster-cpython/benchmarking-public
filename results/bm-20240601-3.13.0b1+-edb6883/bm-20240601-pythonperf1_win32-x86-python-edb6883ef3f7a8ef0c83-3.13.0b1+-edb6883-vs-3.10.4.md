# Results vs. 3.10.4

- fork: python
- ref: edb6883ef3f7a8ef0c83
- machine: windows-x86
- commit hash: edb6883
- commit date: 2024-06-01
- overall geometric mean: 1.15x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240601-pythonperf1_win32-x86-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 233 ms: 1.14x faster                                                            |
| chameleon      | 6.42 ms                                                         | 5.73 ms: 1.12x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.81 sec: 1.08x faster                                                          |
| html5lib       | 52.1 ms                                                         | 44.7 ms: 1.16x faster                                                           |
| tornado_http   | 118 ms                                                          | 93.8 ms: 1.25x faster                                                           |
| Geometric mean | (ref)                                                           | 1.15x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240601-pythonperf1_win32-x86-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 473 ms: 1.95x faster                                                            |
| async_tree_io           | 940 ms                                                          | 534 ms: 1.76x faster                                                            |
| async_tree_none         | 394 ms                                                          | 227 ms: 1.73x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 274 ms: 1.70x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.78x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240601-pythonperf1_win32-x86-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 199 ms: 2.53x faster                                                            |
| float          | 69.6 ms                                                         | 53.1 ms: 1.31x faster                                                           |
| nbody          | 79.1 ms                                                         | 77.3 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                           | 1.50x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240601-pythonperf1_win32-x86-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 99.0 ms: 1.18x faster                                                           |
| regex_dna      | 131 ms                                                          | 122 ms: 1.07x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 15.9 ms: 1.01x slower                                                           |
| regex_effbot   | 1.66 ms                                                         | 1.91 ms: 1.15x slower                                                           |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240601-pythonperf1_win32-x86-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.99 ms: 1.41x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 215 us: 1.30x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 147 us: 1.29x faster                                                            |
| tomli_loads          | 1.91 sec                                                        | 1.60 sec: 1.19x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 101 ms: 1.19x faster                                                            |
| xml_etree_process    | 48.1 ms                                                         | 41.4 ms: 1.16x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 63.1 ms: 1.12x faster                                                           |
| unpickle_list        | 2.98 us                                                         | 2.73 us: 1.09x faster                                                           |
| json_loads           | 22.4 us                                                         | 20.7 us: 1.08x faster                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 58.6 ms: 1.05x faster                                                           |
| pickle               | 7.83 us                                                         | 7.99 us: 1.02x slower                                                           |
| unpickle             | 9.82 us                                                         | 10.2 us: 1.03x slower                                                           |
| pickle_dict          | 18.2 us                                                         | 20.4 us: 1.12x slower                                                           |
| pickle_list          | 3.22 us                                                         | 3.63 us: 1.13x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.11x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240601-pythonperf1_win32-x86-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 22.8 ms: 1.01x faster                                                           |
| python_startup_no_site | 18.1 ms                                                         | 18.6 ms: 1.03x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.01x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240601-pythonperf1_win32-x86-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 6.83 ms: 1.33x faster                                                           |
| django_template | 36.0 ms                                                         | 30.1 ms: 1.20x faster                                                           |
| genshi_text     | 21.0 ms                                                         | 19.5 ms: 1.08x faster                                                           |
| genshi_xml      | 46.6 ms                                                         | 43.5 ms: 1.07x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.16x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240601-pythonperf1_win32-x86-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 131 us: 3.01x faster                                                            |
| pidigits                 | 502 ms                                                          | 199 ms: 2.53x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 473 ms: 1.95x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.19 ms: 1.84x faster                                                           |
| pylint                   | 384 ms                                                          | 217 ms: 1.77x faster                                                            |
| async_tree_io            | 940 ms                                                          | 534 ms: 1.76x faster                                                            |
| async_tree_none          | 394 ms                                                          | 227 ms: 1.73x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 274 ms: 1.70x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 57.9 ns: 1.69x faster                                                           |
| raytrace                 | 303 ms                                                          | 189 ms: 1.60x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 59.4 ms: 1.51x faster                                                           |
| comprehensions           | 17.7 us                                                         | 11.8 us: 1.51x faster                                                           |
| chaos                    | 74.4 ms                                                         | 49.5 ms: 1.50x faster                                                           |
| generators               | 31.6 ms                                                         | 21.3 ms: 1.48x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 55.8 ms: 1.46x faster                                                           |
| go                       | 146 ms                                                          | 102 ms: 1.43x faster                                                            |
| richards_super           | 49.9 ms                                                         | 35.0 ms: 1.43x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 934 us: 1.42x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 4.35 ms: 1.41x faster                                                           |
| scimark_sor              | 115 ms                                                          | 81.7 ms: 1.41x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 6.99 ms: 1.41x faster                                                           |
| pyflate                  | 422 ms                                                          | 310 ms: 1.36x faster                                                            |
| sqlglot_transpile        | 1.58 ms                                                         | 1.17 ms: 1.35x faster                                                           |
| pycparser                | 1.04 sec                                                        | 775 ms: 1.34x faster                                                            |
| mako                     | 9.10 ms                                                         | 6.83 ms: 1.33x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 47.1 ms: 1.31x faster                                                           |
| float                    | 69.6 ms                                                         | 53.1 ms: 1.31x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 66.7 ms: 1.31x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 215 us: 1.30x faster                                                            |
| richards                 | 40.3 ms                                                         | 31.0 ms: 1.30x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 147 us: 1.29x faster                                                            |
| tornado_http             | 118 ms                                                          | 93.8 ms: 1.25x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 24.2 us: 1.22x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 66.0 ms: 1.22x faster                                                           |
| django_template          | 36.0 ms                                                         | 30.1 ms: 1.20x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.60 sec: 1.19x faster                                                          |
| xml_etree_parse          | 120 ms                                                          | 101 ms: 1.19x faster                                                            |
| sqlite_synth             | 2.29 us                                                         | 1.94 us: 1.18x faster                                                           |
| sympy_sum                | 122 ms                                                          | 104 ms: 1.18x faster                                                            |
| regex_compile            | 117 ms                                                          | 99.0 ms: 1.18x faster                                                           |
| coroutines               | 17.9 ms                                                         | 15.3 ms: 1.17x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 44.7 ms: 1.16x faster                                                           |
| xml_etree_process        | 48.1 ms                                                         | 41.4 ms: 1.16x faster                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.18 sec: 1.16x faster                                                          |
| sympy_integrate          | 16.6 ms                                                         | 14.5 ms: 1.15x faster                                                           |
| json                     | 4.76 ms                                                         | 4.16 ms: 1.15x faster                                                           |
| pprint_safe_repr         | 658 ms                                                          | 576 ms: 1.14x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.84 ms: 1.14x faster                                                           |
| 2to3                     | 265 ms                                                          | 233 ms: 1.14x faster                                                            |
| bench_thread_pool        | 1.12 ms                                                         | 984 us: 1.14x faster                                                            |
| fannkuch                 | 317 ms                                                          | 281 ms: 1.13x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 63.1 ms: 1.12x faster                                                           |
| chameleon                | 6.42 ms                                                         | 5.73 ms: 1.12x faster                                                           |
| deepcopy                 | 310 us                                                          | 277 us: 1.12x faster                                                            |
| mdp                      | 1.83 sec                                                        | 1.64 sec: 1.11x faster                                                          |
| sympy_str                | 229 ms                                                          | 207 ms: 1.11x faster                                                            |
| asyncio_tcp              | 744 ms                                                          | 674 ms: 1.10x faster                                                            |
| sqlglot_optimize         | 44.7 ms                                                         | 40.8 ms: 1.09x faster                                                           |
| unpickle_list            | 2.98 us                                                         | 2.73 us: 1.09x faster                                                           |
| sqlglot_normalize        | 230 ms                                                          | 211 ms: 1.09x faster                                                            |
| meteor_contest           | 80.0 ms                                                         | 73.7 ms: 1.09x faster                                                           |
| json_loads               | 22.4 us                                                         | 20.7 us: 1.08x faster                                                           |
| scimark_fft              | 216 ms                                                          | 201 ms: 1.08x faster                                                            |
| docutils                 | 1.95 sec                                                        | 1.81 sec: 1.08x faster                                                          |
| genshi_text              | 21.0 ms                                                         | 19.5 ms: 1.08x faster                                                           |
| sympy_expand             | 391 ms                                                          | 364 ms: 1.07x faster                                                            |
| regex_dna                | 131 ms                                                          | 122 ms: 1.07x faster                                                            |
| genshi_xml               | 46.6 ms                                                         | 43.5 ms: 1.07x faster                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.55 us: 1.05x faster                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 58.6 ms: 1.05x faster                                                           |
| nbody                    | 79.1 ms                                                         | 77.3 ms: 1.02x faster                                                           |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 16.8 sec: 1.01x faster                                                          |
| python_startup           | 22.9 ms                                                         | 22.8 ms: 1.01x faster                                                           |
| flaskblogging            | 2.03 sec                                                        | 2.03 sec: 1.00x slower                                                          |
| regex_v8                 | 15.8 ms                                                         | 15.9 ms: 1.01x slower                                                           |
| logging_format           | 7.91 us                                                         | 8.05 us: 1.02x slower                                                           |
| pickle                   | 7.83 us                                                         | 7.99 us: 1.02x slower                                                           |
| logging_simple           | 7.29 us                                                         | 7.47 us: 1.02x slower                                                           |
| pathlib                  | 81.2 ms                                                         | 83.3 ms: 1.03x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 18.6 ms: 1.03x slower                                                           |
| unpickle                 | 9.82 us                                                         | 10.2 us: 1.03x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 69.7 ms: 1.05x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 748 us: 1.08x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 20.4 us: 1.12x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.43 ms: 1.12x slower                                                           |
| pickle_list              | 3.22 us                                                         | 3.63 us: 1.13x slower                                                           |
| async_generators         | 241 ms                                                          | 273 ms: 1.13x slower                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.91 ms: 1.15x slower                                                           |
| telco                    | 4.83 ms                                                         | 5.96 ms: 1.23x slower                                                           |
| coverage                 | 46.6 ms                                                         | 307 ms: 6.59x slower                                                            |
| thrift                   | 902 us                                                          | 9.88 ms: 10.95x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.15x faster                                                                    |
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240601-3.13.0b1+-edb6883/bm-20240601-pythonperf1_win32-x86-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown