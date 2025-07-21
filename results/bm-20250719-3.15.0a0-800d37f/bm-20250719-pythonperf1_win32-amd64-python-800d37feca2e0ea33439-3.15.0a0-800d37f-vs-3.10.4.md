# Results vs. 3.10.4

- fork: python
- ref: 800d37feca2e0ea33439
- machine: windows-amd64
- commit hash: 800d37f
- commit date: 2025-07-19
- overall geometric mean: 1.435x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.33x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 221 ms: 1.20x faster                                                             |
| docutils       | 1.95 sec                                                        | 1.62 sec: 1.20x faster                                                           |
| html5lib       | 52.1 ms                                                         | 39.4 ms: 1.32x faster                                                            |
| Geometric mean | (ref)                                                           | 1.24x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 328 ms: 2.82x faster                                                             |
| async_tree_io           | 940 ms                                                          | 393 ms: 2.39x faster                                                             |
| async_tree_none         | 394 ms                                                          | 170 ms: 2.31x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 205 ms: 2.28x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.44x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 146 ms: 3.43x faster                                                             |
| float          | 69.6 ms                                                         | 43.4 ms: 1.60x faster                                                            |
| nbody          | 79.1 ms                                                         | 64.2 ms: 1.23x faster                                                            |
| Geometric mean | (ref)                                                           | 1.89x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 79.9 ms: 1.46x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 14.3 ms: 1.10x faster                                                            |
| regex_dna      | 131 ms                                                          | 120 ms: 1.09x faster                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.57 ms: 1.06x faster                                                            |
| Geometric mean | (ref)                                                           | 1.17x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_loads           | 22.4 us                                                         | 14.1 us: 1.59x faster                                                            |
| json_dumps           | 9.82 ms                                                         | 6.31 ms: 1.56x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 135 us: 1.40x faster                                                             |
| xml_etree_parse      | 120 ms                                                          | 86.8 ms: 1.38x faster                                                            |
| tomli_loads          | 1.91 sec                                                        | 1.41 sec: 1.36x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 213 us: 1.32x faster                                                             |
| xml_etree_process    | 48.1 ms                                                         | 38.5 ms: 1.25x faster                                                            |
| unpickle             | 9.82 us                                                         | 8.42 us: 1.17x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 63.1 ms: 1.12x faster                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 55.9 ms: 1.10x faster                                                            |
| unpickle_list        | 2.98 us                                                         | 2.86 us: 1.04x faster                                                            |
| pickle               | 7.83 us                                                         | 8.26 us: 1.05x slower                                                            |
| pickle_list          | 3.22 us                                                         | 3.39 us: 1.06x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 19.9 us: 1.09x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.20x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.3 ms: 1.07x slower                                                            |
| python_startup         | 22.9 ms                                                         | 25.8 ms: 1.12x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 24.6 ms: 1.47x faster                                                            |
| mako            | 9.10 ms                                                         | 6.53 ms: 1.40x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 15.1 ms: 1.39x faster                                                            |
| genshi_xml      | 46.6 ms                                                         | 34.0 ms: 1.37x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.40x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 1.29 sec: 13.20x faster                                                          |
| typing_runtime_protocols | 396 us                                                          | 105 us: 3.76x faster                                                             |
| pidigits                 | 502 ms                                                          | 146 ms: 3.43x faster                                                             |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 328 ms: 2.82x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 30.5 ms: 2.66x faster                                                            |
| async_tree_io            | 940 ms                                                          | 393 ms: 2.39x faster                                                             |
| async_tree_none          | 394 ms                                                          | 170 ms: 2.31x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 205 ms: 2.28x faster                                                             |
| mdp                      | 1.83 sec                                                        | 804 ms: 2.27x faster                                                             |
| pylint                   | 384 ms                                                          | 196 ms: 1.96x faster                                                             |
| go                       | 146 ms                                                          | 77.1 ms: 1.89x faster                                                            |
| asyncio_tcp              | 744 ms                                                          | 398 ms: 1.87x faster                                                             |
| deltablue                | 4.04 ms                                                         | 2.21 ms: 1.82x faster                                                            |
| chaos                    | 74.4 ms                                                         | 41.0 ms: 1.81x faster                                                            |
| deepcopy                 | 310 us                                                          | 171 us: 1.81x faster                                                             |
| thrift                   | 902 us                                                          | 505 us: 1.79x faster                                                             |
| logging_silent           | 97.9 ns                                                         | 55.6 ns: 1.76x faster                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 48.4 ms: 1.68x faster                                                            |
| comprehensions           | 17.7 us                                                         | 10.7 us: 1.66x faster                                                            |
| json                     | 4.76 ms                                                         | 2.88 ms: 1.66x faster                                                            |
| raytrace                 | 303 ms                                                          | 184 ms: 1.64x faster                                                             |
| generators               | 31.6 ms                                                         | 19.3 ms: 1.64x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 18.3 us: 1.62x faster                                                            |
| float                    | 69.6 ms                                                         | 43.4 ms: 1.60x faster                                                            |
| json_loads               | 22.4 us                                                         | 14.1 us: 1.59x faster                                                            |
| richards_super           | 49.9 ms                                                         | 31.9 ms: 1.56x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 6.31 ms: 1.56x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 40.4 ms: 1.53x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 58.6 ms: 1.53x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 4.08 ms: 1.50x faster                                                            |
| django_template          | 36.0 ms                                                         | 24.6 ms: 1.47x faster                                                            |
| regex_compile            | 117 ms                                                          | 79.9 ms: 1.46x faster                                                            |
| pycparser                | 1.04 sec                                                        | 714 ms: 1.46x faster                                                             |
| pyflate                  | 422 ms                                                          | 289 ms: 1.46x faster                                                             |
| deepcopy_reduce          | 2.68 us                                                         | 1.85 us: 1.45x faster                                                            |
| scimark_sor              | 115 ms                                                          | 79.2 ms: 1.45x faster                                                            |
| sqlite_synth             | 2.29 us                                                         | 1.58 us: 1.45x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 40.4 ms: 1.45x faster                                                            |
| richards                 | 40.3 ms                                                         | 27.8 ms: 1.45x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 135 us: 1.40x faster                                                             |
| nqueens                  | 87.1 ms                                                         | 62.2 ms: 1.40x faster                                                            |
| sympy_sum                | 122 ms                                                          | 87.8 ms: 1.40x faster                                                            |
| mako                     | 9.10 ms                                                         | 6.53 ms: 1.40x faster                                                            |
| genshi_text              | 21.0 ms                                                         | 15.1 ms: 1.39x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 86.8 ms: 1.38x faster                                                            |
| genshi_xml               | 46.6 ms                                                         | 34.0 ms: 1.37x faster                                                            |
| tomli_loads              | 1.91 sec                                                        | 1.41 sec: 1.36x faster                                                           |
| sympy_str                | 229 ms                                                          | 169 ms: 1.35x faster                                                             |
| sympy_expand             | 391 ms                                                          | 289 ms: 1.35x faster                                                             |
| sympy_integrate          | 16.6 ms                                                         | 12.4 ms: 1.34x faster                                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.02 sec: 1.34x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 39.4 ms: 1.32x faster                                                            |
| bench_thread_pool        | 1.12 ms                                                         | 849 us: 1.32x faster                                                             |
| pickle_pure_python       | 280 us                                                          | 213 us: 1.32x faster                                                             |
| pprint_safe_repr         | 658 ms                                                          | 508 ms: 1.30x faster                                                             |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.50 ms: 1.30x faster                                                            |
| xml_etree_process        | 48.1 ms                                                         | 38.5 ms: 1.25x faster                                                            |
| coroutines               | 17.9 ms                                                         | 14.4 ms: 1.25x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 64.5 ms: 1.24x faster                                                            |
| nbody                    | 79.1 ms                                                         | 64.2 ms: 1.23x faster                                                            |
| unpack_sequence          | 40.0 ns                                                         | 32.6 ns: 1.23x faster                                                            |
| 2to3                     | 265 ms                                                          | 221 ms: 1.20x faster                                                             |
| docutils                 | 1.95 sec                                                        | 1.62 sec: 1.20x faster                                                           |
| fannkuch                 | 317 ms                                                          | 269 ms: 1.18x faster                                                             |
| logging_format           | 7.91 us                                                         | 6.75 us: 1.17x faster                                                            |
| unpickle                 | 9.82 us                                                         | 8.42 us: 1.17x faster                                                            |
| logging_simple           | 7.29 us                                                         | 6.29 us: 1.16x faster                                                            |
| scimark_fft              | 216 ms                                                          | 189 ms: 1.14x faster                                                             |
| xml_etree_iterparse      | 70.8 ms                                                         | 63.1 ms: 1.12x faster                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 55.9 ms: 1.10x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 14.3 ms: 1.10x faster                                                            |
| meteor_contest           | 80.0 ms                                                         | 72.6 ms: 1.10x faster                                                            |
| regex_dna                | 131 ms                                                          | 120 ms: 1.09x faster                                                             |
| regex_effbot             | 1.66 ms                                                         | 1.57 ms: 1.06x faster                                                            |
| telco                    | 4.83 ms                                                         | 4.60 ms: 1.05x faster                                                            |
| unpickle_list            | 2.98 us                                                         | 2.86 us: 1.04x faster                                                            |
| async_generators         | 241 ms                                                          | 233 ms: 1.03x faster                                                             |
| pickle                   | 7.83 us                                                         | 8.26 us: 1.05x slower                                                            |
| pickle_list              | 3.22 us                                                         | 3.39 us: 1.06x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 19.3 ms: 1.07x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 19.9 us: 1.09x slower                                                            |
| coverage                 | 46.6 ms                                                         | 51.8 ms: 1.11x slower                                                            |
| python_startup           | 22.9 ms                                                         | 25.8 ms: 1.12x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 94.2 ms: 1.42x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 2.11 ms: 1.65x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.30 ms: 1.88x slower                                                            |
| Geometric mean           | (ref)                                                           | 1.43x faster                                                                     |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250719-3.15.0a0-800d37f/bm-20250719-pythonperf1_win32-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.435x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.35x
- 95% likely to have a speedup of 1.35x
- 99% likely to have a speedup of 1.33x

# Memory
- memory change: unknown