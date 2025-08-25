# Results vs. 3.10.4

- fork: python
- ref: 6fcac09401e336b25833
- machine: windows-amd64
- commit hash: 6fcac09
- commit date: 2025-08-23
- overall geometric mean: 1.465x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.36x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 217 ms: 1.22x faster                                                             |
| docutils       | 1.95 sec                                                        | 1.59 sec: 1.22x faster                                                           |
| html5lib       | 52.1 ms                                                         | 37.5 ms: 1.39x faster                                                            |
| Geometric mean | (ref)                                                           | 1.28x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 327 ms: 2.82x faster                                                             |
| async_tree_io           | 940 ms                                                          | 389 ms: 2.42x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 201 ms: 2.33x faster                                                             |
| async_tree_none         | 394 ms                                                          | 173 ms: 2.28x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.45x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 143 ms: 3.50x faster                                                             |
| float          | 69.6 ms                                                         | 43.5 ms: 1.60x faster                                                            |
| nbody          | 79.1 ms                                                         | 64.0 ms: 1.24x faster                                                            |
| Geometric mean | (ref)                                                           | 1.91x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 78.7 ms: 1.48x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 13.8 ms: 1.14x faster                                                            |
| regex_dna      | 131 ms                                                          | 120 ms: 1.09x faster                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.57 ms: 1.06x faster                                                            |
| Geometric mean | (ref)                                                           | 1.18x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 5.34 ms: 1.84x faster                                                            |
| json_loads           | 22.4 us                                                         | 14.3 us: 1.56x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 134 us: 1.42x faster                                                             |
| xml_etree_parse      | 120 ms                                                          | 85.6 ms: 1.40x faster                                                            |
| tomli_loads          | 1.91 sec                                                        | 1.39 sec: 1.38x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 211 us: 1.33x faster                                                             |
| xml_etree_process    | 48.1 ms                                                         | 38.7 ms: 1.24x faster                                                            |
| unpickle             | 9.82 us                                                         | 8.53 us: 1.15x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 62.3 ms: 1.14x faster                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 56.4 ms: 1.09x faster                                                            |
| unpickle_list        | 2.98 us                                                         | 2.83 us: 1.05x faster                                                            |
| pickle_list          | 3.22 us                                                         | 3.28 us: 1.02x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 19.2 us: 1.05x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.23x faster                                                                     |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.3 ms: 1.07x slower                                                            |
| python_startup         | 22.9 ms                                                         | 25.1 ms: 1.09x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 24.4 ms: 1.48x faster                                                            |
| mako            | 9.10 ms                                                         | 6.56 ms: 1.39x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 15.2 ms: 1.38x faster                                                            |
| genshi_xml      | 46.6 ms                                                         | 34.0 ms: 1.37x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.40x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 1.25 sec: 13.58x faster                                                          |
| typing_runtime_protocols | 396 us                                                          | 104 us: 3.80x faster                                                             |
| pidigits                 | 502 ms                                                          | 143 ms: 3.50x faster                                                             |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 327 ms: 2.82x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 29.9 ms: 2.72x faster                                                            |
| async_tree_io            | 940 ms                                                          | 389 ms: 2.42x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 201 ms: 2.33x faster                                                             |
| mdp                      | 1.83 sec                                                        | 794 ms: 2.30x faster                                                             |
| async_tree_none          | 394 ms                                                          | 173 ms: 2.28x faster                                                             |
| pylint                   | 384 ms                                                          | 194 ms: 1.98x faster                                                             |
| asyncio_tcp              | 744 ms                                                          | 379 ms: 1.96x faster                                                             |
| go                       | 146 ms                                                          | 76.1 ms: 1.91x faster                                                            |
| chaos                    | 74.4 ms                                                         | 39.3 ms: 1.90x faster                                                            |
| thrift                   | 902 us                                                          | 488 us: 1.85x faster                                                             |
| json_dumps               | 9.82 ms                                                         | 5.34 ms: 1.84x faster                                                            |
| deepcopy                 | 310 us                                                          | 169 us: 1.84x faster                                                             |
| deltablue                | 4.04 ms                                                         | 2.23 ms: 1.81x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 54.6 ns: 1.79x faster                                                            |
| raytrace                 | 303 ms                                                          | 174 ms: 1.74x faster                                                             |
| crypto_pyaes             | 81.3 ms                                                         | 46.7 ms: 1.74x faster                                                            |
| generators               | 31.6 ms                                                         | 18.8 ms: 1.68x faster                                                            |
| richards_super           | 49.9 ms                                                         | 30.3 ms: 1.65x faster                                                            |
| comprehensions           | 17.7 us                                                         | 10.8 us: 1.64x faster                                                            |
| float                    | 69.6 ms                                                         | 43.5 ms: 1.60x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 56.4 ms: 1.59x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 39.0 ms: 1.59x faster                                                            |
| json                     | 4.76 ms                                                         | 3.00 ms: 1.59x faster                                                            |
| json_loads               | 22.4 us                                                         | 14.3 us: 1.56x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 19.3 us: 1.53x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 4.04 ms: 1.52x faster                                                            |
| richards                 | 40.3 ms                                                         | 26.6 ms: 1.51x faster                                                            |
| scimark_sor              | 115 ms                                                          | 76.3 ms: 1.51x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 39.0 ms: 1.50x faster                                                            |
| pycparser                | 1.04 sec                                                        | 701 ms: 1.49x faster                                                             |
| regex_compile            | 117 ms                                                          | 78.7 ms: 1.48x faster                                                            |
| django_template          | 36.0 ms                                                         | 24.4 ms: 1.48x faster                                                            |
| sqlite_synth             | 2.29 us                                                         | 1.55 us: 1.47x faster                                                            |
| pyflate                  | 422 ms                                                          | 288 ms: 1.47x faster                                                             |
| deepcopy_reduce          | 2.68 us                                                         | 1.84 us: 1.46x faster                                                            |
| sympy_sum                | 122 ms                                                          | 85.3 ms: 1.44x faster                                                            |
| nqueens                  | 87.1 ms                                                         | 60.8 ms: 1.43x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 134 us: 1.42x faster                                                             |
| xml_etree_parse          | 120 ms                                                          | 85.6 ms: 1.40x faster                                                            |
| pprint_pformat           | 1.37 sec                                                        | 981 ms: 1.40x faster                                                             |
| sympy_expand             | 391 ms                                                          | 281 ms: 1.39x faster                                                             |
| sympy_str                | 229 ms                                                          | 165 ms: 1.39x faster                                                             |
| html5lib                 | 52.1 ms                                                         | 37.5 ms: 1.39x faster                                                            |
| mako                     | 9.10 ms                                                         | 6.56 ms: 1.39x faster                                                            |
| genshi_text              | 21.0 ms                                                         | 15.2 ms: 1.38x faster                                                            |
| pprint_safe_repr         | 658 ms                                                          | 478 ms: 1.38x faster                                                             |
| tomli_loads              | 1.91 sec                                                        | 1.39 sec: 1.38x faster                                                           |
| genshi_xml               | 46.6 ms                                                         | 34.0 ms: 1.37x faster                                                            |
| sympy_integrate          | 16.6 ms                                                         | 12.3 ms: 1.35x faster                                                            |
| bench_thread_pool        | 1.12 ms                                                         | 839 us: 1.33x faster                                                             |
| pickle_pure_python       | 280 us                                                          | 211 us: 1.33x faster                                                             |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.51 ms: 1.29x faster                                                            |
| coroutines               | 17.9 ms                                                         | 14.0 ms: 1.28x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 63.1 ms: 1.27x faster                                                            |
| xml_etree_process        | 48.1 ms                                                         | 38.7 ms: 1.24x faster                                                            |
| nbody                    | 79.1 ms                                                         | 64.0 ms: 1.24x faster                                                            |
| docutils                 | 1.95 sec                                                        | 1.59 sec: 1.22x faster                                                           |
| logging_simple           | 7.29 us                                                         | 5.97 us: 1.22x faster                                                            |
| 2to3                     | 265 ms                                                          | 217 ms: 1.22x faster                                                             |
| logging_format           | 7.91 us                                                         | 6.48 us: 1.22x faster                                                            |
| fannkuch                 | 317 ms                                                          | 260 ms: 1.22x faster                                                             |
| scimark_fft              | 216 ms                                                          | 180 ms: 1.20x faster                                                             |
| telco                    | 4.83 ms                                                         | 4.13 ms: 1.17x faster                                                            |
| unpickle                 | 9.82 us                                                         | 8.53 us: 1.15x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 13.8 ms: 1.14x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 62.3 ms: 1.14x faster                                                            |
| meteor_contest           | 80.0 ms                                                         | 71.5 ms: 1.12x faster                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 56.4 ms: 1.09x faster                                                            |
| regex_dna                | 131 ms                                                          | 120 ms: 1.09x faster                                                             |
| async_generators         | 241 ms                                                          | 225 ms: 1.07x faster                                                             |
| unpack_sequence          | 40.0 ns                                                         | 37.9 ns: 1.06x faster                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.57 ms: 1.06x faster                                                            |
| unpickle_list            | 2.98 us                                                         | 2.83 us: 1.05x faster                                                            |
| pickle_list              | 3.22 us                                                         | 3.28 us: 1.02x slower                                                            |
| coverage                 | 46.6 ms                                                         | 48.9 ms: 1.05x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 19.2 us: 1.05x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 19.3 ms: 1.07x slower                                                            |
| python_startup           | 22.9 ms                                                         | 25.1 ms: 1.09x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 91.9 ms: 1.39x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 2.05 ms: 1.60x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.26 ms: 1.81x slower                                                            |
| Geometric mean           | (ref)                                                           | 1.46x faster                                                                     |

Benchmark hidden because not significant (1): pickle
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250823-3.15.0a0-6fcac09/bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.465x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.39x
- 95% likely to have a speedup of 1.38x
- 99% likely to have a speedup of 1.36x

# Memory
- memory change: unknown