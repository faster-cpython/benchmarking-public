# Results vs. 3.10.4

- fork: python
- ref: c6b1a073438d93d4e629
- machine: windows-amd64
- commit hash: c6b1a07
- commit date: 2025-03-29
- overall geometric mean: 1.489x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.35x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1-amd64-python-c6b1a073438d93d4e629-3.14.0a6+-c6b1a07 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 204 ms: 1.20x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.54 sec: 1.25x faster                                                      |
| html5lib       | 51.0 ms                                                     | 36.0 ms: 1.42x faster                                                       |
| Geometric mean | (ref)                                                       | 1.29x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1-amd64-python-c6b1a073438d93d4e629-3.14.0a6+-c6b1a07 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 349 ms: 3.18x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 190 ms: 2.78x faster                                                        |
| async_tree_none         | 435 ms                                                      | 158 ms: 2.75x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 312 ms: 2.05x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.65x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1-amd64-python-c6b1a073438d93d4e629-3.14.0a6+-c6b1a07 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 37.1 ms: 1.66x faster                                                       |
| nbody          | 71.3 ms                                                     | 47.7 ms: 1.50x faster                                                       |
| pidigits       | 149 ms                                                      | 145 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                       | 1.37x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1-amd64-python-c6b1a073438d93d4e629-3.14.0a6+-c6b1a07 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 69.1 ms: 1.53x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.3 ms: 1.16x faster                                                       |
| regex_dna      | 136 ms                                                      | 124 ms: 1.10x faster                                                        |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1-amd64-python-c6b1a073438d93d4e629-3.14.0a6+-c6b1a07 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 105 us: 1.74x faster                                                        |
| json_dumps           | 9.16 ms                                                     | 5.68 ms: 1.61x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 175 us: 1.54x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.09 sec: 1.53x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 33.5 ms: 1.33x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 47.6 ms: 1.17x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 88.2 ms: 1.10x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.0 ms: 1.07x faster                                                       |
| json_loads           | 14.0 us                                                     | 14.2 us: 1.01x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.32x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1-amd64-python-c6b1a073438d93d4e629-3.14.0a6+-c6b1a07 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 26.7 ms: 1.30x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 21.0 ms: 1.35x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.32x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1-amd64-python-c6b1a073438d93d4e629-3.14.0a6+-c6b1a07 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 19.8 ms                                                     | 12.0 ms: 1.66x faster                                                       |
| mako            | 9.03 ms                                                     | 5.78 ms: 1.56x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 28.7 ms: 1.43x faster                                                       |
| django_template | 28.9 ms                                                     | 20.4 ms: 1.42x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.51x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1-amd64-python-c6b1a073438d93d4e629-3.14.0a6+-c6b1a07 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 86.5 us: 3.89x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 349 ms: 3.18x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 190 ms: 2.78x faster                                                        |
| async_tree_none          | 435 ms                                                      | 158 ms: 2.75x faster                                                        |
| deltablue                | 4.19 ms                                                     | 1.59 ms: 2.63x faster                                                       |
| mdp                      | 1.78 sec                                                    | 684 ms: 2.60x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 30.6 ms: 2.47x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 41.8 ns: 2.27x faster                                                       |
| go                       | 139 ms                                                      | 62.2 ms: 2.23x faster                                                       |
| generators               | 32.4 ms                                                     | 15.0 ms: 2.16x faster                                                       |
| scimark_sor              | 106 ms                                                      | 49.2 ms: 2.16x faster                                                       |
| richards_super           | 52.2 ms                                                     | 25.4 ms: 2.06x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 14.0 us: 2.06x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 312 ms: 2.05x faster                                                        |
| scimark_lu               | 85.8 ms                                                     | 43.5 ms: 1.97x faster                                                       |
| chaos                    | 61.7 ms                                                     | 31.4 ms: 1.97x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 29.3 ms: 1.96x faster                                                       |
| raytrace                 | 273 ms                                                      | 140 ms: 1.95x faster                                                        |
| hexiom                   | 5.74 ms                                                     | 2.96 ms: 1.94x faster                                                       |
| comprehensions           | 16.5 us                                                     | 8.54 us: 1.93x faster                                                       |
| richards                 | 42.4 ms                                                     | 22.2 ms: 1.91x faster                                                       |
| pylint                   | 350 ms                                                      | 185 ms: 1.89x faster                                                        |
| spectral_norm            | 77.3 ms                                                     | 42.9 ms: 1.80x faster                                                       |
| deepcopy                 | 255 us                                                      | 142 us: 1.80x faster                                                        |
| pyflate                  | 409 ms                                                      | 230 ms: 1.78x faster                                                        |
| unpickle_pure_python     | 183 us                                                      | 105 us: 1.74x faster                                                        |
| float                    | 61.7 ms                                                     | 37.1 ms: 1.66x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 12.0 ms: 1.66x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 38.8 ms: 1.61x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 5.68 ms: 1.61x faster                                                       |
| mako                     | 9.03 ms                                                     | 5.78 ms: 1.56x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 175 us: 1.54x faster                                                        |
| regex_compile            | 106 ms                                                      | 69.1 ms: 1.53x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.09 sec: 1.53x faster                                                      |
| nbody                    | 71.3 ms                                                     | 47.7 ms: 1.50x faster                                                       |
| coroutines               | 16.0 ms                                                     | 10.9 ms: 1.47x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 834 ms: 1.46x faster                                                        |
| pprint_safe_repr         | 592 ms                                                      | 411 ms: 1.44x faster                                                        |
| pycparser                | 930 ms                                                      | 648 ms: 1.44x faster                                                        |
| genshi_xml               | 41.0 ms                                                     | 28.7 ms: 1.43x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.54 us: 1.43x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 36.0 ms: 1.42x faster                                                       |
| django_template          | 28.9 ms                                                     | 20.4 ms: 1.42x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 48.5 ms: 1.37x faster                                                       |
| sympy_sum                | 107 ms                                                      | 78.1 ms: 1.37x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 1.99 ms: 1.37x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 11.3 ms: 1.36x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 37.8 ms: 1.34x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 33.5 ms: 1.33x faster                                                       |
| sympy_str                | 194 ms                                                      | 148 ms: 1.31x faster                                                        |
| scimark_fft              | 187 ms                                                      | 144 ms: 1.30x faster                                                        |
| fannkuch                 | 256 ms                                                      | 197 ms: 1.30x faster                                                        |
| sqlite_synth             | 1.91 us                                                     | 1.48 us: 1.29x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.54 sec: 1.25x faster                                                      |
| sympy_expand             | 314 ms                                                      | 255 ms: 1.23x faster                                                        |
| 2to3                     | 246 ms                                                      | 204 ms: 1.20x faster                                                        |
| async_generators         | 222 ms                                                      | 188 ms: 1.18x faster                                                        |
| bench_thread_pool        | 958 us                                                      | 819 us: 1.17x faster                                                        |
| xml_etree_generate       | 55.5 ms                                                     | 47.6 ms: 1.17x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 13.3 ms: 1.16x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 66.6 ms: 1.14x faster                                                       |
| logging_format           | 6.76 us                                                     | 5.94 us: 1.14x faster                                                       |
| logging_simple           | 6.22 us                                                     | 5.60 us: 1.11x faster                                                       |
| json                     | 3.14 ms                                                     | 2.83 ms: 1.11x faster                                                       |
| regex_dna                | 136 ms                                                      | 124 ms: 1.10x faster                                                        |
| xml_etree_parse          | 96.8 ms                                                     | 88.2 ms: 1.10x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.0 ms: 1.07x faster                                                       |
| pidigits                 | 149 ms                                                      | 145 ms: 1.03x faster                                                        |
| coverage                 | 39.0 ms                                                     | 39.3 ms: 1.01x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.2 us: 1.01x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.23 ms: 1.07x slower                                                       |
| python_startup           | 20.6 ms                                                     | 26.7 ms: 1.30x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 21.0 ms: 1.35x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 88.7 ms: 1.43x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.34 ms: 1.68x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.74 ms: 1.95x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.48x faster                                                                |

Benchmark hidden because not significant (1): regex_effbot
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250329-3.14.0a6+-c6b1a07-CLANG/bm-20250329-pythonperf1-amd64-python-c6b1a073438d93d4e629-3.14.0a6+-c6b1a07.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.489x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.40x
- 95% likely to have a speedup of 1.38x
- 99% likely to have a speedup of 1.35x

# Memory
- memory change: unknown