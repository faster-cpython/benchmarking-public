# Results vs. 3.10.4

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: windows-amd64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.291x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 228 ms: 1.17x faster                                                             |
| docutils       | 1.95 sec                                                        | 2.85 sec: 1.46x slower                                                           |
| html5lib       | 52.1 ms                                                         | 40.1 ms: 1.30x faster                                                            |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 333 ms: 2.77x faster                                                             |
| async_tree_io           | 940 ms                                                          | 353 ms: 2.67x faster                                                             |
| async_tree_none         | 394 ms                                                          | 169 ms: 2.33x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 212 ms: 2.20x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.48x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 136 ms: 3.71x faster                                                             |
| float          | 69.6 ms                                                         | 46.8 ms: 1.49x faster                                                            |
| nbody          | 79.1 ms                                                         | 84.9 ms: 1.07x slower                                                            |
| Geometric mean | (ref)                                                           | 1.73x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_v8       | 15.8 ms                                                         | 12.8 ms: 1.23x faster                                                            |
| regex_compile  | 117 ms                                                          | 95.3 ms: 1.22x faster                                                            |
| regex_dna      | 131 ms                                                          | 112 ms: 1.17x faster                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.50 ms: 1.11x faster                                                            |
| Geometric mean | (ref)                                                           | 1.18x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.62 ms: 1.48x faster                                                            |
| json_loads           | 22.4 us                                                         | 16.1 us: 1.39x faster                                                            |
| xml_etree_parse      | 120 ms                                                          | 90.0 ms: 1.33x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 154 us: 1.23x faster                                                             |
| xml_etree_iterparse  | 70.8 ms                                                         | 58.4 ms: 1.21x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 234 us: 1.20x faster                                                             |
| xml_etree_process    | 48.1 ms                                                         | 44.3 ms: 1.09x faster                                                            |
| pickle_list          | 3.22 us                                                         | 3.08 us: 1.04x faster                                                            |
| unpickle_list        | 2.98 us                                                         | 3.00 us: 1.01x slower                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 62.6 ms: 1.02x slower                                                            |
| unpickle             | 9.82 us                                                         | 10.1 us: 1.03x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 20.0 us: 1.10x slower                                                            |
| tomli_loads          | 1.91 sec                                                        | 2.64 sec: 1.38x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.09x faster                                                                     |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.5 ms: 1.08x slower                                                            |
| python_startup         | 22.9 ms                                                         | 26.0 ms: 1.14x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.11x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 27.3 ms: 1.32x faster                                                            |
| genshi_xml      | 46.6 ms                                                         | 39.4 ms: 1.18x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 19.1 ms: 1.10x faster                                                            |
| mako            | 9.10 ms                                                         | 9.84 ms: 1.08x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.12x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 2.19 sec: 7.76x faster                                                           |
| pidigits                 | 502 ms                                                          | 136 ms: 3.71x faster                                                             |
| typing_runtime_protocols | 396 us                                                          | 130 us: 3.03x faster                                                             |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 333 ms: 2.77x faster                                                             |
| async_tree_io            | 940 ms                                                          | 353 ms: 2.67x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 30.5 ms: 2.66x faster                                                            |
| async_tree_none          | 394 ms                                                          | 169 ms: 2.33x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 212 ms: 2.20x faster                                                             |
| pylint                   | 384 ms                                                          | 212 ms: 1.81x faster                                                             |
| sqlite_synth             | 2.29 us                                                         | 1.36 us: 1.68x faster                                                            |
| mdp                      | 1.83 sec                                                        | 1.11 sec: 1.64x faster                                                           |
| asyncio_tcp              | 744 ms                                                          | 457 ms: 1.63x faster                                                             |
| deltablue                | 4.04 ms                                                         | 2.48 ms: 1.63x faster                                                            |
| chaos                    | 74.4 ms                                                         | 46.3 ms: 1.61x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 61.7 ns: 1.59x faster                                                            |
| thrift                   | 902 us                                                          | 577 us: 1.56x faster                                                             |
| go                       | 146 ms                                                          | 93.9 ms: 1.55x faster                                                            |
| deepcopy                 | 310 us                                                          | 200 us: 1.55x faster                                                             |
| json                     | 4.76 ms                                                         | 3.19 ms: 1.49x faster                                                            |
| float                    | 69.6 ms                                                         | 46.8 ms: 1.49x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 6.62 ms: 1.48x faster                                                            |
| comprehensions           | 17.7 us                                                         | 12.0 us: 1.48x faster                                                            |
| pycparser                | 1.04 sec                                                        | 710 ms: 1.47x faster                                                             |
| crypto_pyaes             | 81.3 ms                                                         | 56.5 ms: 1.44x faster                                                            |
| raytrace                 | 303 ms                                                          | 211 ms: 1.43x faster                                                             |
| generators               | 31.6 ms                                                         | 22.5 ms: 1.41x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 21.2 us: 1.40x faster                                                            |
| json_loads               | 22.4 us                                                         | 16.1 us: 1.39x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 42.3 ms: 1.38x faster                                                            |
| pyflate                  | 422 ms                                                          | 312 ms: 1.35x faster                                                             |
| scimark_sor              | 115 ms                                                          | 85.9 ms: 1.34x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 90.0 ms: 1.33x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 4.65 ms: 1.32x faster                                                            |
| django_template          | 36.0 ms                                                         | 27.3 ms: 1.32x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 68.3 ms: 1.31x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 40.1 ms: 1.30x faster                                                            |
| coroutines               | 17.9 ms                                                         | 14.0 ms: 1.28x faster                                                            |
| richards_super           | 49.9 ms                                                         | 39.3 ms: 1.27x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 49.0 ms: 1.26x faster                                                            |
| sympy_sum                | 122 ms                                                          | 97.3 ms: 1.26x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 2.15 us: 1.25x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 12.8 ms: 1.23x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 154 us: 1.23x faster                                                             |
| regex_compile            | 117 ms                                                          | 95.3 ms: 1.22x faster                                                            |
| sympy_str                | 229 ms                                                          | 187 ms: 1.22x faster                                                             |
| xml_etree_iterparse      | 70.8 ms                                                         | 58.4 ms: 1.21x faster                                                            |
| sympy_expand             | 391 ms                                                          | 323 ms: 1.21x faster                                                             |
| pickle_pure_python       | 280 us                                                          | 234 us: 1.20x faster                                                             |
| richards                 | 40.3 ms                                                         | 33.7 ms: 1.20x faster                                                            |
| nqueens                  | 87.1 ms                                                         | 72.9 ms: 1.20x faster                                                            |
| genshi_xml               | 46.6 ms                                                         | 39.4 ms: 1.18x faster                                                            |
| sympy_integrate          | 16.6 ms                                                         | 14.1 ms: 1.18x faster                                                            |
| pprint_safe_repr         | 658 ms                                                          | 563 ms: 1.17x faster                                                             |
| regex_dna                | 131 ms                                                          | 112 ms: 1.17x faster                                                             |
| 2to3                     | 265 ms                                                          | 228 ms: 1.17x faster                                                             |
| regex_effbot             | 1.66 ms                                                         | 1.50 ms: 1.11x faster                                                            |
| genshi_text              | 21.0 ms                                                         | 19.1 ms: 1.10x faster                                                            |
| logging_format           | 7.91 us                                                         | 7.22 us: 1.10x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 73.7 ms: 1.09x faster                                                            |
| xml_etree_process        | 48.1 ms                                                         | 44.3 ms: 1.09x faster                                                            |
| logging_simple           | 7.29 us                                                         | 6.74 us: 1.08x faster                                                            |
| fannkuch                 | 317 ms                                                          | 296 ms: 1.07x faster                                                             |
| gc_traversal             | 1.28 ms                                                         | 1.21 ms: 1.06x faster                                                            |
| pickle_list              | 3.22 us                                                         | 3.08 us: 1.04x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.12 ms: 1.04x faster                                                            |
| bench_thread_pool        | 1.12 ms                                                         | 1.09 ms: 1.03x faster                                                            |
| scimark_fft              | 216 ms                                                          | 214 ms: 1.01x faster                                                             |
| unpickle_list            | 2.98 us                                                         | 3.00 us: 1.01x slower                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 62.6 ms: 1.02x slower                                                            |
| unpack_sequence          | 40.0 ns                                                         | 40.9 ns: 1.02x slower                                                            |
| unpickle                 | 9.82 us                                                         | 10.1 us: 1.03x slower                                                            |
| nbody                    | 79.1 ms                                                         | 84.9 ms: 1.07x slower                                                            |
| meteor_contest           | 80.0 ms                                                         | 86.4 ms: 1.08x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 19.5 ms: 1.08x slower                                                            |
| mako                     | 9.10 ms                                                         | 9.84 ms: 1.08x slower                                                            |
| async_generators         | 241 ms                                                          | 264 ms: 1.10x slower                                                             |
| pickle_dict              | 18.2 us                                                         | 20.0 us: 1.10x slower                                                            |
| telco                    | 4.83 ms                                                         | 5.43 ms: 1.12x slower                                                            |
| python_startup           | 22.9 ms                                                         | 26.0 ms: 1.14x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 79.3 ms: 1.20x slower                                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.68 sec: 1.23x slower                                                           |
| tomli_loads              | 1.91 sec                                                        | 2.64 sec: 1.38x slower                                                           |
| docutils                 | 1.95 sec                                                        | 2.85 sec: 1.46x slower                                                           |
| coverage                 | 46.6 ms                                                         | 68.2 ms: 1.46x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.03 ms: 1.48x slower                                                            |
| Geometric mean           | (ref)                                                           | 1.29x faster                                                                     |

Benchmark hidden because not significant (1): pickle
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250712-3.15.0a0-47b01da-NOGIL/bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.291x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: unknown