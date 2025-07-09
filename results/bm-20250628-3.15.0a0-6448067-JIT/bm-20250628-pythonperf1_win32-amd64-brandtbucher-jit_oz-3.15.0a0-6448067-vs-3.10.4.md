# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_oz
- machine: windows-amd64
- commit hash: 6448067
- commit date: 2025-06-28
- overall geometric mean: 1.472x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.36x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1_win32-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 218 ms: 1.22x faster                                                     |
| docutils       | 1.95 sec                                                        | 1.64 sec: 1.19x faster                                                   |
| html5lib       | 52.1 ms                                                         | 38.4 ms: 1.36x faster                                                    |
| Geometric mean | (ref)                                                           | 1.25x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1_win32-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 329 ms: 2.80x faster                                                     |
| async_tree_io           | 940 ms                                                          | 391 ms: 2.41x faster                                                     |
| async_tree_none         | 394 ms                                                          | 170 ms: 2.32x faster                                                     |
| async_tree_memoization  | 467 ms                                                          | 204 ms: 2.29x faster                                                     |
| Geometric mean          | (ref)                                                           | 2.45x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1_win32-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 147 ms: 3.43x faster                                                     |
| float          | 69.6 ms                                                         | 43.4 ms: 1.60x faster                                                    |
| nbody          | 79.1 ms                                                         | 52.1 ms: 1.52x faster                                                    |
| Geometric mean | (ref)                                                           | 2.03x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1_win32-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 78.6 ms: 1.48x faster                                                    |
| regex_dna      | 131 ms                                                          | 121 ms: 1.08x faster                                                     |
| regex_v8       | 15.8 ms                                                         | 14.6 ms: 1.08x faster                                                    |
| regex_effbot   | 1.66 ms                                                         | 1.56 ms: 1.07x faster                                                    |
| Geometric mean | (ref)                                                           | 1.17x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1_win32-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 189 us                                                          | 111 us: 1.70x faster                                                     |
| json_dumps           | 9.82 ms                                                         | 6.16 ms: 1.60x faster                                                    |
| json_loads           | 22.4 us                                                         | 14.3 us: 1.57x faster                                                    |
| tomli_loads          | 1.91 sec                                                        | 1.23 sec: 1.56x faster                                                   |
| xml_etree_parse      | 120 ms                                                          | 88.0 ms: 1.36x faster                                                    |
| pickle_pure_python   | 280 us                                                          | 206 us: 1.36x faster                                                     |
| xml_etree_process    | 48.1 ms                                                         | 35.6 ms: 1.35x faster                                                    |
| xml_etree_generate   | 61.6 ms                                                         | 49.9 ms: 1.24x faster                                                    |
| xml_etree_iterparse  | 70.8 ms                                                         | 61.6 ms: 1.15x faster                                                    |
| Geometric mean       | (ref)                                                           | 1.42x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1_win32-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.1 ms: 1.06x slower                                                    |
| python_startup         | 22.9 ms                                                         | 26.1 ms: 1.14x slower                                                    |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1_win32-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.41 ms: 1.68x faster                                                    |
| django_template | 36.0 ms                                                         | 24.0 ms: 1.50x faster                                                    |
| genshi_text     | 21.0 ms                                                         | 15.6 ms: 1.34x faster                                                    |
| genshi_xml      | 46.6 ms                                                         | 34.9 ms: 1.34x faster                                                    |
| Geometric mean  | (ref)                                                           | 1.46x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1_win32-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 105 us: 3.76x faster                                                     |
| pidigits                 | 502 ms                                                          | 147 ms: 3.43x faster                                                     |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 329 ms: 2.80x faster                                                     |
| pathlib                  | 81.2 ms                                                         | 29.1 ms: 2.79x faster                                                    |
| async_tree_io            | 940 ms                                                          | 391 ms: 2.41x faster                                                     |
| async_tree_none          | 394 ms                                                          | 170 ms: 2.32x faster                                                     |
| async_tree_memoization   | 467 ms                                                          | 204 ms: 2.29x faster                                                     |
| mdp                      | 1.83 sec                                                        | 803 ms: 2.27x faster                                                     |
| pylint                   | 384 ms                                                          | 198 ms: 1.94x faster                                                     |
| go                       | 146 ms                                                          | 77.5 ms: 1.88x faster                                                    |
| deepcopy                 | 310 us                                                          | 169 us: 1.84x faster                                                     |
| deltablue                | 4.04 ms                                                         | 2.21 ms: 1.83x faster                                                    |
| chaos                    | 74.4 ms                                                         | 40.7 ms: 1.83x faster                                                    |
| logging_silent           | 97.9 ns                                                         | 54.8 ns: 1.79x faster                                                    |
| thrift                   | 902 us                                                          | 508 us: 1.78x faster                                                     |
| crypto_pyaes             | 81.3 ms                                                         | 46.9 ms: 1.73x faster                                                    |
| unpickle_pure_python     | 189 us                                                          | 111 us: 1.70x faster                                                     |
| raytrace                 | 303 ms                                                          | 178 ms: 1.70x faster                                                     |
| mako                     | 9.10 ms                                                         | 5.41 ms: 1.68x faster                                                    |
| deepcopy_memo            | 29.6 us                                                         | 17.8 us: 1.66x faster                                                    |
| pyflate                  | 422 ms                                                          | 257 ms: 1.64x faster                                                     |
| richards_super           | 49.9 ms                                                         | 30.4 ms: 1.64x faster                                                    |
| generators               | 31.6 ms                                                         | 19.4 ms: 1.62x faster                                                    |
| comprehensions           | 17.7 us                                                         | 11.0 us: 1.61x faster                                                    |
| float                    | 69.6 ms                                                         | 43.4 ms: 1.60x faster                                                    |
| json_dumps               | 9.82 ms                                                         | 6.16 ms: 1.60x faster                                                    |
| scimark_monte_carlo      | 61.9 ms                                                         | 39.2 ms: 1.58x faster                                                    |
| json_loads               | 22.4 us                                                         | 14.3 us: 1.57x faster                                                    |
| tomli_loads              | 1.91 sec                                                        | 1.23 sec: 1.56x faster                                                   |
| nbody                    | 79.1 ms                                                         | 52.1 ms: 1.52x faster                                                    |
| scimark_sor              | 115 ms                                                          | 75.8 ms: 1.52x faster                                                    |
| scimark_lu               | 89.8 ms                                                         | 59.6 ms: 1.50x faster                                                    |
| django_template          | 36.0 ms                                                         | 24.0 ms: 1.50x faster                                                    |
| json                     | 4.76 ms                                                         | 3.19 ms: 1.49x faster                                                    |
| richards                 | 40.3 ms                                                         | 27.0 ms: 1.49x faster                                                    |
| regex_compile            | 117 ms                                                          | 78.6 ms: 1.48x faster                                                    |
| pycparser                | 1.04 sec                                                        | 702 ms: 1.48x faster                                                     |
| sqlite_synth             | 2.29 us                                                         | 1.55 us: 1.48x faster                                                    |
| hexiom                   | 6.13 ms                                                         | 4.17 ms: 1.47x faster                                                    |
| deepcopy_reduce          | 2.68 us                                                         | 1.84 us: 1.46x faster                                                    |
| dulwich_log              | 58.5 ms                                                         | 40.3 ms: 1.45x faster                                                    |
| pprint_pformat           | 1.37 sec                                                        | 956 ms: 1.43x faster                                                     |
| pprint_safe_repr         | 658 ms                                                          | 464 ms: 1.42x faster                                                     |
| sympy_sum                | 122 ms                                                          | 86.6 ms: 1.41x faster                                                    |
| nqueens                  | 87.1 ms                                                         | 61.8 ms: 1.41x faster                                                    |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.31 ms: 1.41x faster                                                    |
| xml_etree_parse          | 120 ms                                                          | 88.0 ms: 1.36x faster                                                    |
| pickle_pure_python       | 280 us                                                          | 206 us: 1.36x faster                                                     |
| scimark_fft              | 216 ms                                                          | 159 ms: 1.36x faster                                                     |
| html5lib                 | 52.1 ms                                                         | 38.4 ms: 1.36x faster                                                    |
| xml_etree_process        | 48.1 ms                                                         | 35.6 ms: 1.35x faster                                                    |
| sympy_str                | 229 ms                                                          | 170 ms: 1.35x faster                                                     |
| genshi_text              | 21.0 ms                                                         | 15.6 ms: 1.34x faster                                                    |
| genshi_xml               | 46.6 ms                                                         | 34.9 ms: 1.34x faster                                                    |
| sympy_expand             | 391 ms                                                          | 295 ms: 1.33x faster                                                     |
| sympy_integrate          | 16.6 ms                                                         | 12.7 ms: 1.31x faster                                                    |
| fannkuch                 | 317 ms                                                          | 247 ms: 1.29x faster                                                     |
| spectral_norm            | 80.2 ms                                                         | 63.4 ms: 1.26x faster                                                    |
| coroutines               | 17.9 ms                                                         | 14.4 ms: 1.24x faster                                                    |
| xml_etree_generate       | 61.6 ms                                                         | 49.9 ms: 1.24x faster                                                    |
| 2to3                     | 265 ms                                                          | 218 ms: 1.22x faster                                                     |
| logging_format           | 7.91 us                                                         | 6.62 us: 1.19x faster                                                    |
| docutils                 | 1.95 sec                                                        | 1.64 sec: 1.19x faster                                                   |
| logging_simple           | 7.29 us                                                         | 6.15 us: 1.18x faster                                                    |
| xml_etree_iterparse      | 70.8 ms                                                         | 61.6 ms: 1.15x faster                                                    |
| telco                    | 4.83 ms                                                         | 4.31 ms: 1.12x faster                                                    |
| meteor_contest           | 80.0 ms                                                         | 71.5 ms: 1.12x faster                                                    |
| regex_dna                | 131 ms                                                          | 121 ms: 1.08x faster                                                     |
| regex_v8                 | 15.8 ms                                                         | 14.6 ms: 1.08x faster                                                    |
| regex_effbot             | 1.66 ms                                                         | 1.56 ms: 1.07x faster                                                    |
| async_generators         | 241 ms                                                          | 246 ms: 1.02x slower                                                     |
| python_startup_no_site   | 18.1 ms                                                         | 19.1 ms: 1.06x slower                                                    |
| coverage                 | 46.6 ms                                                         | 50.3 ms: 1.08x slower                                                    |
| python_startup           | 22.9 ms                                                         | 26.1 ms: 1.14x slower                                                    |
| gc_traversal             | 1.28 ms                                                         | 2.10 ms: 1.64x slower                                                    |
| create_gc_cycles         | 694 us                                                          | 1.30 ms: 1.87x slower                                                    |
| Geometric mean           | (ref)                                                           | 1.47x faster                                                             |
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250628-3.15.0a0-6448067-JIT/bm-20250628-pythonperf1_win32-amd64-brandtbucher-jit_oz-3.15.0a0-6448067.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.472x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.41x
- 95% likely to have a speedup of 1.39x
- 99% likely to have a speedup of 1.36x

# Memory
- memory change: unknown