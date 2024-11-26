# Results vs. 3.10.4

- fork: brandtbucher
- ref: warmup_side_4096
- machine: windows-x86
- commit hash: a8a4ed3
- commit date: 2024-11-22
- overall geometric mean: 1.054x faster
- HPT reliability: 80.63%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241122-pythonperf1_win32-x86-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 260 ms: 1.02x faster                                                              |
| html5lib       | 52.1 ms                                                         | 49.2 ms: 1.06x faster                                                             |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                      |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241122-pythonperf1_win32-x86-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|-------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 500 ms: 1.84x faster                                                              |
| async_tree_io           | 940 ms                                                          | 567 ms: 1.66x faster                                                              |
| async_tree_none         | 394 ms                                                          | 240 ms: 1.64x faster                                                              |
| async_tree_memoization  | 467 ms                                                          | 301 ms: 1.55x faster                                                              |
| Geometric mean          | (ref)                                                           | 1.67x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241122-pythonperf1_win32-x86-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 203 ms: 2.48x faster                                                              |
| float          | 69.6 ms                                                         | 56.3 ms: 1.24x faster                                                             |
| nbody          | 79.1 ms                                                         | 94.9 ms: 1.20x slower                                                             |
| Geometric mean | (ref)                                                           | 1.37x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241122-pythonperf1_win32-x86-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 113 ms: 1.16x faster                                                              |
| regex_effbot   | 1.66 ms                                                         | 1.55 ms: 1.07x faster                                                             |
| regex_compile  | 117 ms                                                          | 113 ms: 1.03x faster                                                              |
| regex_v8       | 15.8 ms                                                         | 15.6 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241122-pythonperf1_win32-x86-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 9.01 ms: 1.09x faster                                                             |
| xml_etree_parse      | 120 ms                                                          | 113 ms: 1.06x faster                                                              |
| json_loads           | 22.4 us                                                         | 21.3 us: 1.05x faster                                                             |
| xml_etree_iterparse  | 70.8 ms                                                         | 68.3 ms: 1.04x faster                                                             |
| tomli_loads          | 1.91 sec                                                        | 1.84 sec: 1.04x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 296 us: 1.06x slower                                                              |
| unpickle_pure_python | 189 us                                                          | 207 us: 1.10x slower                                                              |
| xml_etree_process    | 48.1 ms                                                         | 53.7 ms: 1.11x slower                                                             |
| xml_etree_generate   | 61.6 ms                                                         | 72.7 ms: 1.18x slower                                                             |
| Geometric mean       | (ref)                                                           | 1.02x slower                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241122-pythonperf1_win32-x86-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.5 ms: 1.08x slower                                                             |
| python_startup         | 22.9 ms                                                         | 25.7 ms: 1.12x slower                                                             |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241122-pythonperf1_win32-x86-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.39 ms: 1.23x faster                                                             |
| django_template | 36.0 ms                                                         | 37.0 ms: 1.03x slower                                                             |
| genshi_xml      | 46.6 ms                                                         | 57.2 ms: 1.23x slower                                                             |
| genshi_text     | 21.0 ms                                                         | 25.9 ms: 1.23x slower                                                             |
| Geometric mean  | (ref)                                                           | 1.06x slower                                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241122-pythonperf1_win32-x86-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|--------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pidigits                 | 502 ms                                                          | 203 ms: 2.48x faster                                                              |
| typing_runtime_protocols | 396 us                                                          | 169 us: 2.35x faster                                                              |
| sqlglot_normalize        | 230 ms                                                          | 108 ms: 2.14x faster                                                              |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 500 ms: 1.84x faster                                                              |
| pylint                   | 384 ms                                                          | 228 ms: 1.68x faster                                                              |
| async_tree_io            | 940 ms                                                          | 567 ms: 1.66x faster                                                              |
| async_tree_none          | 394 ms                                                          | 240 ms: 1.64x faster                                                              |
| async_tree_memoization   | 467 ms                                                          | 301 ms: 1.55x faster                                                              |
| deltablue                | 4.04 ms                                                         | 3.21 ms: 1.26x faster                                                             |
| float                    | 69.6 ms                                                         | 56.3 ms: 1.24x faster                                                             |
| mako                     | 9.10 ms                                                         | 7.39 ms: 1.23x faster                                                             |
| deepcopy_memo            | 29.6 us                                                         | 24.0 us: 1.23x faster                                                             |
| crypto_pyaes             | 81.3 ms                                                         | 66.7 ms: 1.22x faster                                                             |
| scimark_lu               | 89.8 ms                                                         | 74.0 ms: 1.21x faster                                                             |
| go                       | 146 ms                                                          | 121 ms: 1.21x faster                                                              |
| sqlite_synth             | 2.29 us                                                         | 1.94 us: 1.18x faster                                                             |
| dulwich_log              | 58.5 ms                                                         | 49.8 ms: 1.17x faster                                                             |
| regex_dna                | 131 ms                                                          | 113 ms: 1.16x faster                                                              |
| sqlglot_parse            | 1.33 ms                                                         | 1.15 ms: 1.16x faster                                                             |
| thrift                   | 902 us                                                          | 786 us: 1.15x faster                                                              |
| chaos                    | 74.4 ms                                                         | 65.7 ms: 1.13x faster                                                             |
| pycparser                | 1.04 sec                                                        | 931 ms: 1.12x faster                                                              |
| sqlglot_transpile        | 1.58 ms                                                         | 1.42 ms: 1.12x faster                                                             |
| deepcopy                 | 310 us                                                          | 278 us: 1.11x faster                                                              |
| logging_silent           | 97.9 ns                                                         | 87.9 ns: 1.11x faster                                                             |
| json_dumps               | 9.82 ms                                                         | 9.01 ms: 1.09x faster                                                             |
| coroutines               | 17.9 ms                                                         | 16.5 ms: 1.08x faster                                                             |
| bench_thread_pool        | 1.12 ms                                                         | 1.03 ms: 1.08x faster                                                             |
| scimark_sor              | 115 ms                                                          | 106 ms: 1.08x faster                                                              |
| regex_effbot             | 1.66 ms                                                         | 1.55 ms: 1.07x faster                                                             |
| xml_etree_parse          | 120 ms                                                          | 113 ms: 1.06x faster                                                              |
| sympy_sum                | 122 ms                                                          | 115 ms: 1.06x faster                                                              |
| html5lib                 | 52.1 ms                                                         | 49.2 ms: 1.06x faster                                                             |
| json_loads               | 22.4 us                                                         | 21.3 us: 1.05x faster                                                             |
| richards_super           | 49.9 ms                                                         | 47.4 ms: 1.05x faster                                                             |
| xml_etree_iterparse      | 70.8 ms                                                         | 68.3 ms: 1.04x faster                                                             |
| tomli_loads              | 1.91 sec                                                        | 1.84 sec: 1.04x faster                                                            |
| pyflate                  | 422 ms                                                          | 408 ms: 1.03x faster                                                              |
| regex_compile            | 117 ms                                                          | 113 ms: 1.03x faster                                                              |
| 2to3                     | 265 ms                                                          | 260 ms: 1.02x faster                                                              |
| regex_v8                 | 15.8 ms                                                         | 15.6 ms: 1.01x faster                                                             |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.21 ms: 1.01x faster                                                             |
| mdp                      | 1.83 sec                                                        | 1.85 sec: 1.01x slower                                                            |
| sympy_str                | 229 ms                                                          | 233 ms: 1.02x slower                                                              |
| pathlib                  | 81.2 ms                                                         | 83.4 ms: 1.03x slower                                                             |
| django_template          | 36.0 ms                                                         | 37.0 ms: 1.03x slower                                                             |
| sympy_expand             | 391 ms                                                          | 403 ms: 1.03x slower                                                              |
| richards                 | 40.3 ms                                                         | 41.6 ms: 1.03x slower                                                             |
| scimark_monte_carlo      | 61.9 ms                                                         | 64.1 ms: 1.04x slower                                                             |
| comprehensions           | 17.7 us                                                         | 18.4 us: 1.04x slower                                                             |
| fannkuch                 | 317 ms                                                          | 330 ms: 1.04x slower                                                              |
| spectral_norm            | 80.2 ms                                                         | 83.5 ms: 1.04x slower                                                             |
| sympy_integrate          | 16.6 ms                                                         | 17.5 ms: 1.05x slower                                                             |
| pickle_pure_python       | 280 us                                                          | 296 us: 1.06x slower                                                              |
| deepcopy_reduce          | 2.68 us                                                         | 2.86 us: 1.07x slower                                                             |
| python_startup_no_site   | 18.1 ms                                                         | 19.5 ms: 1.08x slower                                                             |
| unpickle_pure_python     | 189 us                                                          | 207 us: 1.10x slower                                                              |
| pprint_pformat           | 1.37 sec                                                        | 1.51 sec: 1.10x slower                                                            |
| meteor_contest           | 80.0 ms                                                         | 88.3 ms: 1.10x slower                                                             |
| pprint_safe_repr         | 658 ms                                                          | 731 ms: 1.11x slower                                                              |
| xml_etree_process        | 48.1 ms                                                         | 53.7 ms: 1.11x slower                                                             |
| python_startup           | 22.9 ms                                                         | 25.7 ms: 1.12x slower                                                             |
| nqueens                  | 87.1 ms                                                         | 98.9 ms: 1.14x slower                                                             |
| sqlglot_optimize         | 44.7 ms                                                         | 50.8 ms: 1.14x slower                                                             |
| logging_format           | 7.91 us                                                         | 9.01 us: 1.14x slower                                                             |
| hexiom                   | 6.13 ms                                                         | 7.00 ms: 1.14x slower                                                             |
| logging_simple           | 7.29 us                                                         | 8.40 us: 1.15x slower                                                             |
| scimark_fft              | 216 ms                                                          | 250 ms: 1.16x slower                                                              |
| generators               | 31.6 ms                                                         | 36.7 ms: 1.16x slower                                                             |
| xml_etree_generate       | 61.6 ms                                                         | 72.7 ms: 1.18x slower                                                             |
| coverage                 | 46.6 ms                                                         | 55.0 ms: 1.18x slower                                                             |
| nbody                    | 79.1 ms                                                         | 94.9 ms: 1.20x slower                                                             |
| genshi_xml               | 46.6 ms                                                         | 57.2 ms: 1.23x slower                                                             |
| genshi_text              | 21.0 ms                                                         | 25.9 ms: 1.23x slower                                                             |
| bench_mp_pool            | 66.4 ms                                                         | 87.2 ms: 1.31x slower                                                             |
| async_generators         | 241 ms                                                          | 319 ms: 1.32x slower                                                              |
| gc_traversal             | 1.28 ms                                                         | 1.70 ms: 1.33x slower                                                             |
| telco                    | 4.83 ms                                                         | 7.17 ms: 1.48x slower                                                             |
| create_gc_cycles         | 694 us                                                          | 1.15 ms: 1.65x slower                                                             |
| Geometric mean           | (ref)                                                           | 1.05x faster                                                                      |

Benchmark hidden because not significant (3): json, raytrace, docutils
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241122-3.14.0a2+-a8a4ed3-JIT/bm-20241122-pythonperf1_win32-x86-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.054x faster
# HPT report

- Reliability score: 80.63% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown