# Results vs. 3.10.4

- fork: python
- ref: 2a66dd33dfc0b845042d
- machine: windows-x86
- commit hash: 2a66dd3
- commit date: 2024-12-20
- overall geometric mean: 1.147x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 246 ms: 1.08x faster                                                            |
| docutils       | 1.95 sec                                                        | 1.79 sec: 1.09x faster                                                          |
| html5lib       | 52.1 ms                                                         | 44.1 ms: 1.18x faster                                                           |
| Geometric mean | (ref)                                                           | 1.12x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 443 ms: 2.12x faster                                                            |
| async_tree_cpu_io_mixed | 922 ms                                                          | 449 ms: 2.05x faster                                                            |
| async_tree_none         | 394 ms                                                          | 203 ms: 1.94x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 253 ms: 1.84x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.99x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 201 ms: 2.50x faster                                                            |
| float          | 69.6 ms                                                         | 59.0 ms: 1.18x faster                                                           |
| nbody          | 79.1 ms                                                         | 84.2 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                           | 1.40x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 103 ms: 1.13x faster                                                            |
| regex_dna      | 131 ms                                                          | 126 ms: 1.03x faster                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.64 ms: 1.01x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 15.9 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.91 sec                                                        | 1.64 sec: 1.16x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 107 ms: 1.12x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 174 us: 1.09x faster                                                            |
| json_dumps           | 9.82 ms                                                         | 9.08 ms: 1.08x faster                                                           |
| json_loads           | 22.4 us                                                         | 20.7 us: 1.08x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 65.6 ms: 1.08x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 268 us: 1.05x faster                                                            |
| xml_etree_process    | 48.1 ms                                                         | 48.6 ms: 1.01x slower                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 67.9 ms: 1.10x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.06x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.2 ms: 1.12x slower                                                           |
| python_startup         | 22.9 ms                                                         | 26.7 ms: 1.17x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.14x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.74 ms: 1.18x faster                                                           |
| django_template | 36.0 ms                                                         | 31.5 ms: 1.14x faster                                                           |
| genshi_xml      | 46.6 ms                                                         | 45.6 ms: 1.02x faster                                                           |
| genshi_text     | 21.0 ms                                                         | 21.3 ms: 1.01x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.08x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 141 us: 2.82x faster                                                            |
| pidigits                 | 502 ms                                                          | 201 ms: 2.50x faster                                                            |
| async_tree_io            | 940 ms                                                          | 443 ms: 2.12x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 449 ms: 2.05x faster                                                            |
| async_tree_none          | 394 ms                                                          | 203 ms: 1.94x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 253 ms: 1.84x faster                                                            |
| pylint                   | 384 ms                                                          | 216 ms: 1.77x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.58 ms: 1.57x faster                                                           |
| go                       | 146 ms                                                          | 97.0 ms: 1.50x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 69.3 ns: 1.41x faster                                                           |
| deepcopy                 | 310 us                                                          | 227 us: 1.37x faster                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 60.2 ms: 1.35x faster                                                           |
| chaos                    | 74.4 ms                                                         | 56.2 ms: 1.32x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 22.8 us: 1.30x faster                                                           |
| generators               | 31.6 ms                                                         | 24.4 ms: 1.29x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 1.04 ms: 1.28x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 70.9 ms: 1.27x faster                                                           |
| pycparser                | 1.04 sec                                                        | 830 ms: 1.25x faster                                                            |
| comprehensions           | 17.7 us                                                         | 14.2 us: 1.25x faster                                                           |
| pyflate                  | 422 ms                                                          | 339 ms: 1.24x faster                                                            |
| sqlglot_transpile        | 1.58 ms                                                         | 1.28 ms: 1.24x faster                                                           |
| raytrace                 | 303 ms                                                          | 245 ms: 1.24x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 5.03 ms: 1.22x faster                                                           |
| thrift                   | 902 us                                                          | 742 us: 1.22x faster                                                            |
| float                    | 69.6 ms                                                         | 59.0 ms: 1.18x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 44.1 ms: 1.18x faster                                                           |
| mako                     | 9.10 ms                                                         | 7.74 ms: 1.18x faster                                                           |
| richards_super           | 49.9 ms                                                         | 42.5 ms: 1.17x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.95 us: 1.17x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.64 sec: 1.16x faster                                                          |
| dulwich_log              | 58.5 ms                                                         | 50.4 ms: 1.16x faster                                                           |
| sympy_sum                | 122 ms                                                          | 106 ms: 1.16x faster                                                            |
| scimark_sor              | 115 ms                                                          | 100 ms: 1.15x faster                                                            |
| django_template          | 36.0 ms                                                         | 31.5 ms: 1.14x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 54.3 ms: 1.14x faster                                                           |
| json                     | 4.76 ms                                                         | 4.20 ms: 1.13x faster                                                           |
| regex_compile            | 117 ms                                                          | 103 ms: 1.13x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 70.7 ms: 1.13x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 107 ms: 1.12x faster                                                            |
| nqueens                  | 87.1 ms                                                         | 78.6 ms: 1.11x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.01 ms: 1.10x faster                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.45 us: 1.09x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 174 us: 1.09x faster                                                            |
| docutils                 | 1.95 sec                                                        | 1.79 sec: 1.09x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 9.08 ms: 1.08x faster                                                           |
| 2to3                     | 265 ms                                                          | 246 ms: 1.08x faster                                                            |
| json_loads               | 22.4 us                                                         | 20.7 us: 1.08x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 15.4 ms: 1.08x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 65.6 ms: 1.08x faster                                                           |
| richards                 | 40.3 ms                                                         | 37.4 ms: 1.08x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.02 ms: 1.07x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.70 sec: 1.07x faster                                                          |
| sympy_str                | 229 ms                                                          | 217 ms: 1.06x faster                                                            |
| fannkuch                 | 317 ms                                                          | 300 ms: 1.06x faster                                                            |
| sqlglot_optimize         | 44.7 ms                                                         | 42.4 ms: 1.06x faster                                                           |
| coroutines               | 17.9 ms                                                         | 17.1 ms: 1.05x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 268 us: 1.05x faster                                                            |
| sqlglot_normalize        | 230 ms                                                          | 221 ms: 1.04x faster                                                            |
| regex_dna                | 131 ms                                                          | 126 ms: 1.03x faster                                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.32 sec: 1.03x faster                                                          |
| sympy_expand             | 391 ms                                                          | 380 ms: 1.03x faster                                                            |
| genshi_xml               | 46.6 ms                                                         | 45.6 ms: 1.02x faster                                                           |
| pprint_safe_repr         | 658 ms                                                          | 646 ms: 1.02x faster                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.64 ms: 1.01x faster                                                           |
| meteor_contest           | 80.0 ms                                                         | 80.3 ms: 1.00x slower                                                           |
| xml_etree_process        | 48.1 ms                                                         | 48.6 ms: 1.01x slower                                                           |
| regex_v8                 | 15.8 ms                                                         | 15.9 ms: 1.01x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 21.3 ms: 1.01x slower                                                           |
| pathlib                  | 81.2 ms                                                         | 82.5 ms: 1.02x slower                                                           |
| scimark_fft              | 216 ms                                                          | 228 ms: 1.05x slower                                                            |
| logging_simple           | 7.29 us                                                         | 7.71 us: 1.06x slower                                                           |
| nbody                    | 79.1 ms                                                         | 84.2 ms: 1.06x slower                                                           |
| logging_format           | 7.91 us                                                         | 8.49 us: 1.07x slower                                                           |
| coverage                 | 46.6 ms                                                         | 51.1 ms: 1.10x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 67.9 ms: 1.10x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 20.2 ms: 1.12x slower                                                           |
| mypy2                    | 590 ms                                                          | 681 ms: 1.15x slower                                                            |
| python_startup           | 22.9 ms                                                         | 26.7 ms: 1.17x slower                                                           |
| async_generators         | 241 ms                                                          | 291 ms: 1.21x slower                                                            |
| telco                    | 4.83 ms                                                         | 6.71 ms: 1.39x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 92.6 ms: 1.40x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.83 ms: 1.43x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.07 ms: 1.54x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.14x faster                                                                    |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241220-3.14.0a3+-2a66dd3/bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.147x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: unknown