# Results vs. 3.10.4

- fork: python
- ref: 0cafa97932c6574734bb
- machine: windows-x86
- commit hash: 0cafa97
- commit date: 2025-01-04
- overall geometric mean: 1.071x faster
- HPT reliability: 93.20%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| docutils       | 1.95 sec                                                        | 1.94 sec: 1.01x faster                                                          |
| html5lib       | 52.1 ms                                                         | 48.1 ms: 1.08x faster                                                           |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                    |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 471 ms: 2.00x faster                                                            |
| async_tree_cpu_io_mixed | 922 ms                                                          | 471 ms: 1.96x faster                                                            |
| async_tree_none         | 394 ms                                                          | 226 ms: 1.74x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 275 ms: 1.70x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.85x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 200 ms: 2.51x faster                                                            |
| float          | 69.6 ms                                                         | 51.9 ms: 1.34x faster                                                           |
| nbody          | 79.1 ms                                                         | 97.0 ms: 1.23x slower                                                           |
| Geometric mean | (ref)                                                           | 1.40x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 117 ms: 1.11x faster                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.54 ms: 1.08x faster                                                           |
| regex_compile  | 117 ms                                                          | 112 ms: 1.04x faster                                                            |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 120 ms                                                          | 107 ms: 1.12x faster                                                            |
| json_dumps           | 9.82 ms                                                         | 8.92 ms: 1.10x faster                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.76 sec: 1.09x faster                                                          |
| xml_etree_iterparse  | 70.8 ms                                                         | 65.9 ms: 1.07x faster                                                           |
| json_loads           | 22.4 us                                                         | 21.6 us: 1.04x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 291 us: 1.04x slower                                                            |
| unpickle_pure_python | 189 us                                                          | 200 us: 1.06x slower                                                            |
| xml_etree_process    | 48.1 ms                                                         | 53.3 ms: 1.11x slower                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 72.7 ms: 1.18x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.00x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.6 ms: 1.08x slower                                                           |
| python_startup         | 22.9 ms                                                         | 26.1 ms: 1.14x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.11x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.45 ms: 1.22x faster                                                           |
| django_template | 36.0 ms                                                         | 36.8 ms: 1.02x slower                                                           |
| genshi_xml      | 46.6 ms                                                         | 54.7 ms: 1.17x slower                                                           |
| genshi_text     | 21.0 ms                                                         | 25.0 ms: 1.19x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.04x slower                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits                 | 502 ms                                                          | 200 ms: 2.51x faster                                                            |
| typing_runtime_protocols | 396 us                                                          | 164 us: 2.42x faster                                                            |
| sqlglot_normalize        | 230 ms                                                          | 106 ms: 2.17x faster                                                            |
| async_tree_io            | 940 ms                                                          | 471 ms: 2.00x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 471 ms: 1.96x faster                                                            |
| async_tree_none          | 394 ms                                                          | 226 ms: 1.74x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 275 ms: 1.70x faster                                                            |
| pylint                   | 384 ms                                                          | 234 ms: 1.64x faster                                                            |
| float                    | 69.6 ms                                                         | 51.9 ms: 1.34x faster                                                           |
| deltablue                | 4.04 ms                                                         | 3.17 ms: 1.27x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 70.8 ms: 1.27x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 23.5 us: 1.26x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 78.5 ns: 1.25x faster                                                           |
| mako                     | 9.10 ms                                                         | 7.45 ms: 1.22x faster                                                           |
| scimark_sor              | 115 ms                                                          | 95.2 ms: 1.21x faster                                                           |
| go                       | 146 ms                                                          | 122 ms: 1.20x faster                                                            |
| thrift                   | 902 us                                                          | 757 us: 1.19x faster                                                            |
| sqlite_synth             | 2.29 us                                                         | 1.93 us: 1.19x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 1.12 ms: 1.18x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 69.3 ms: 1.17x faster                                                           |
| dulwich_log              | 58.5 ms                                                         | 50.6 ms: 1.16x faster                                                           |
| deepcopy                 | 310 us                                                          | 271 us: 1.15x faster                                                            |
| sqlglot_transpile        | 1.58 ms                                                         | 1.39 ms: 1.14x faster                                                           |
| pyflate                  | 422 ms                                                          | 374 ms: 1.13x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 107 ms: 1.12x faster                                                            |
| chaos                    | 74.4 ms                                                         | 66.4 ms: 1.12x faster                                                           |
| pycparser                | 1.04 sec                                                        | 931 ms: 1.12x faster                                                            |
| regex_dna                | 131 ms                                                          | 117 ms: 1.11x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 8.92 ms: 1.10x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 73.4 ms: 1.09x faster                                                           |
| richards_super           | 49.9 ms                                                         | 45.8 ms: 1.09x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.76 sec: 1.09x faster                                                          |
| coroutines               | 17.9 ms                                                         | 16.6 ms: 1.08x faster                                                           |
| regex_effbot             | 1.66 ms                                                         | 1.54 ms: 1.08x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 48.1 ms: 1.08x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 65.9 ms: 1.07x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.05 ms: 1.07x faster                                                           |
| sympy_sum                | 122 ms                                                          | 115 ms: 1.07x faster                                                            |
| json                     | 4.76 ms                                                         | 4.46 ms: 1.07x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.04 ms: 1.07x faster                                                           |
| raytrace                 | 303 ms                                                          | 289 ms: 1.05x faster                                                            |
| regex_compile            | 117 ms                                                          | 112 ms: 1.04x faster                                                            |
| json_loads               | 22.4 us                                                         | 21.6 us: 1.04x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 61.2 ms: 1.01x faster                                                           |
| docutils                 | 1.95 sec                                                        | 1.94 sec: 1.01x faster                                                          |
| mdp                      | 1.83 sec                                                        | 1.82 sec: 1.00x faster                                                          |
| richards                 | 40.3 ms                                                         | 40.8 ms: 1.01x slower                                                           |
| pathlib                  | 81.2 ms                                                         | 82.7 ms: 1.02x slower                                                           |
| django_template          | 36.0 ms                                                         | 36.8 ms: 1.02x slower                                                           |
| sympy_str                | 229 ms                                                          | 234 ms: 1.02x slower                                                            |
| sympy_expand             | 391 ms                                                          | 406 ms: 1.04x slower                                                            |
| sympy_integrate          | 16.6 ms                                                         | 17.3 ms: 1.04x slower                                                           |
| pickle_pure_python       | 280 us                                                          | 291 us: 1.04x slower                                                            |
| comprehensions           | 17.7 us                                                         | 18.5 us: 1.04x slower                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.80 us: 1.04x slower                                                           |
| unpickle_pure_python     | 189 us                                                          | 200 us: 1.06x slower                                                            |
| fannkuch                 | 317 ms                                                          | 337 ms: 1.06x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 19.6 ms: 1.08x slower                                                           |
| meteor_contest           | 80.0 ms                                                         | 87.4 ms: 1.09x slower                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.50 sec: 1.09x slower                                                          |
| scimark_fft              | 216 ms                                                          | 239 ms: 1.11x slower                                                            |
| pprint_safe_repr         | 658 ms                                                          | 729 ms: 1.11x slower                                                            |
| xml_etree_process        | 48.1 ms                                                         | 53.3 ms: 1.11x slower                                                           |
| nqueens                  | 87.1 ms                                                         | 97.3 ms: 1.12x slower                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 50.4 ms: 1.13x slower                                                           |
| coverage                 | 46.6 ms                                                         | 52.5 ms: 1.13x slower                                                           |
| python_startup           | 22.9 ms                                                         | 26.1 ms: 1.14x slower                                                           |
| hexiom                   | 6.13 ms                                                         | 7.02 ms: 1.14x slower                                                           |
| logging_format           | 7.91 us                                                         | 9.10 us: 1.15x slower                                                           |
| logging_simple           | 7.29 us                                                         | 8.50 us: 1.17x slower                                                           |
| genshi_xml               | 46.6 ms                                                         | 54.7 ms: 1.17x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 72.7 ms: 1.18x slower                                                           |
| generators               | 31.6 ms                                                         | 37.4 ms: 1.19x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 25.0 ms: 1.19x slower                                                           |
| nbody                    | 79.1 ms                                                         | 97.0 ms: 1.23x slower                                                           |
| mypy2                    | 590 ms                                                          | 727 ms: 1.23x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 87.4 ms: 1.32x slower                                                           |
| async_generators         | 241 ms                                                          | 329 ms: 1.36x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 1.81 ms: 1.42x slower                                                           |
| telco                    | 4.83 ms                                                         | 7.01 ms: 1.45x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.05 ms: 1.51x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.07x faster                                                                    |

Benchmark hidden because not significant (2): 2to3, regex_v8
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250104-3.14.0a3+-0cafa97-JIT/bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.071x faster

# HPT report

- Reliability score: 93.20% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown