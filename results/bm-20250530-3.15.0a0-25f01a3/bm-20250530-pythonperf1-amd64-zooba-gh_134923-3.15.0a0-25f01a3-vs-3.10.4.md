# Results vs. 3.10.4

- fork: zooba
- ref: gh_134923
- machine: windows-amd64
- commit hash: 25f01a3
- commit date: 2025-05-30
- overall geometric mean: 1.165x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250530-pythonperf1-amd64-zooba-gh_134923-3.15.0a0-25f01a3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 222 ms: 1.11x faster                                           |
| docutils       | 1.92 sec                                                    | 1.61 sec: 1.19x faster                                         |
| html5lib       | 51.0 ms                                                     | 38.7 ms: 1.32x faster                                          |
| Geometric mean | (ref)                                                       | 1.20x faster                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250530-pythonperf1-amd64-zooba-gh_134923-3.15.0a0-25f01a3 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 395 ms: 2.80x faster                                           |
| async_tree_memoization  | 526 ms                                                      | 204 ms: 2.58x faster                                           |
| async_tree_none         | 435 ms                                                      | 170 ms: 2.57x faster                                           |
| async_tree_cpu_io_mixed | 638 ms                                                      | 329 ms: 1.94x faster                                           |
| Geometric mean          | (ref)                                                       | 2.45x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250530-pythonperf1-amd64-zooba-gh_134923-3.15.0a0-25f01a3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.8 ms: 1.38x faster                                          |
| nbody          | 71.3 ms                                                     | 62.6 ms: 1.14x faster                                          |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                           |
| Geometric mean | (ref)                                                       | 1.17x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250530-pythonperf1-amd64-zooba-gh_134923-3.15.0a0-25f01a3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.7 ms: 1.35x faster                                          |
| regex_dna      | 136 ms                                                      | 121 ms: 1.12x faster                                           |
| regex_v8       | 15.4 ms                                                     | 14.0 ms: 1.10x faster                                          |
| regex_effbot   | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                          |
| Geometric mean | (ref)                                                       | 1.15x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250530-pythonperf1-amd64-zooba-gh_134923-3.15.0a0-25f01a3 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.19 ms: 1.48x faster                                          |
| unpickle_pure_python | 183 us                                                      | 133 us: 1.37x faster                                           |
| pickle_pure_python   | 270 us                                                      | 215 us: 1.26x faster                                           |
| tomli_loads          | 1.67 sec                                                    | 1.33 sec: 1.26x faster                                         |
| xml_etree_process    | 44.5 ms                                                     | 38.8 ms: 1.15x faster                                          |
| xml_etree_parse      | 96.8 ms                                                     | 89.0 ms: 1.09x faster                                          |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.9 ms: 1.03x faster                                          |
| xml_etree_generate   | 55.5 ms                                                     | 55.9 ms: 1.01x slower                                          |
| json_loads           | 14.0 us                                                     | 15.0 us: 1.07x slower                                          |
| Geometric mean       | (ref)                                                       | 1.16x faster                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250530-pythonperf1-amd64-zooba-gh_134923-3.15.0a0-25f01a3 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.2 ms: 1.24x slower                                          |
| python_startup         | 20.6 ms                                                     | 25.9 ms: 1.26x slower                                          |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250530-pythonperf1-amd64-zooba-gh_134923-3.15.0a0-25f01a3 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.52 ms: 1.39x faster                                          |
| genshi_text     | 19.8 ms                                                     | 15.1 ms: 1.31x faster                                          |
| genshi_xml      | 41.0 ms                                                     | 33.6 ms: 1.22x faster                                          |
| django_template | 28.9 ms                                                     | 24.4 ms: 1.18x faster                                          |
| Geometric mean  | (ref)                                                       | 1.27x faster                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250530-pythonperf1-amd64-zooba-gh_134923-3.15.0a0-25f01a3 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 101 us: 3.33x faster                                           |
| async_tree_io            | 1.11 sec                                                    | 395 ms: 2.80x faster                                           |
| async_tree_memoization   | 526 ms                                                      | 204 ms: 2.58x faster                                           |
| async_tree_none          | 435 ms                                                      | 170 ms: 2.57x faster                                           |
| pathlib                  | 75.7 ms                                                     | 31.8 ms: 2.38x faster                                          |
| mdp                      | 1.78 sec                                                    | 788 ms: 2.26x faster                                           |
| deltablue                | 4.19 ms                                                     | 2.14 ms: 1.96x faster                                          |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 329 ms: 1.94x faster                                           |
| go                       | 139 ms                                                      | 74.2 ms: 1.87x faster                                          |
| pylint                   | 350 ms                                                      | 198 ms: 1.77x faster                                           |
| richards_super           | 52.2 ms                                                     | 30.5 ms: 1.71x faster                                          |
| generators               | 32.4 ms                                                     | 19.4 ms: 1.67x faster                                          |
| richards                 | 42.4 ms                                                     | 26.7 ms: 1.59x faster                                          |
| deepcopy_memo            | 28.8 us                                                     | 18.1 us: 1.59x faster                                          |
| chaos                    | 61.7 ms                                                     | 39.1 ms: 1.58x faster                                          |
| comprehensions           | 16.5 us                                                     | 10.5 us: 1.58x faster                                          |
| scimark_lu               | 85.8 ms                                                     | 57.7 ms: 1.49x faster                                          |
| deepcopy                 | 255 us                                                      | 172 us: 1.48x faster                                           |
| json_dumps               | 9.16 ms                                                     | 6.19 ms: 1.48x faster                                          |
| raytrace                 | 273 ms                                                      | 185 ms: 1.48x faster                                           |
| hexiom                   | 5.74 ms                                                     | 3.93 ms: 1.46x faster                                          |
| scimark_monte_carlo      | 57.3 ms                                                     | 39.2 ms: 1.46x faster                                          |
| pyflate                  | 409 ms                                                      | 284 ms: 1.44x faster                                           |
| scimark_sor              | 106 ms                                                      | 74.7 ms: 1.42x faster                                          |
| spectral_norm            | 77.3 ms                                                     | 55.7 ms: 1.39x faster                                          |
| mako                     | 9.03 ms                                                     | 6.52 ms: 1.39x faster                                          |
| float                    | 61.7 ms                                                     | 44.8 ms: 1.38x faster                                          |
| unpickle_pure_python     | 183 us                                                      | 133 us: 1.37x faster                                           |
| crypto_pyaes             | 62.5 ms                                                     | 46.1 ms: 1.36x faster                                          |
| regex_compile            | 106 ms                                                      | 78.7 ms: 1.35x faster                                          |
| pycparser                | 930 ms                                                      | 698 ms: 1.33x faster                                           |
| html5lib                 | 51.0 ms                                                     | 38.7 ms: 1.32x faster                                          |
| genshi_text              | 19.8 ms                                                     | 15.1 ms: 1.31x faster                                          |
| pickle_pure_python       | 270 us                                                      | 215 us: 1.26x faster                                           |
| tomli_loads              | 1.67 sec                                                    | 1.33 sec: 1.26x faster                                         |
| sympy_integrate          | 15.3 ms                                                     | 12.2 ms: 1.25x faster                                          |
| dulwich_log              | 50.5 ms                                                     | 40.9 ms: 1.23x faster                                          |
| sympy_sum                | 107 ms                                                      | 86.9 ms: 1.23x faster                                          |
| genshi_xml               | 41.0 ms                                                     | 33.6 ms: 1.22x faster                                          |
| sqlite_synth             | 1.91 us                                                     | 1.58 us: 1.21x faster                                          |
| docutils                 | 1.92 sec                                                    | 1.61 sec: 1.19x faster                                         |
| django_template          | 28.9 ms                                                     | 24.4 ms: 1.18x faster                                          |
| deepcopy_reduce          | 2.20 us                                                     | 1.87 us: 1.18x faster                                          |
| sympy_str                | 194 ms                                                      | 167 ms: 1.16x faster                                           |
| coroutines               | 16.0 ms                                                     | 13.8 ms: 1.16x faster                                          |
| xml_etree_process        | 44.5 ms                                                     | 38.8 ms: 1.15x faster                                          |
| nbody                    | 71.3 ms                                                     | 62.6 ms: 1.14x faster                                          |
| bench_thread_pool        | 958 us                                                      | 842 us: 1.14x faster                                           |
| regex_dna                | 136 ms                                                      | 121 ms: 1.12x faster                                           |
| 2to3                     | 246 ms                                                      | 222 ms: 1.11x faster                                           |
| regex_v8                 | 15.4 ms                                                     | 14.0 ms: 1.10x faster                                          |
| sympy_expand             | 314 ms                                                      | 288 ms: 1.09x faster                                           |
| nqueens                  | 66.6 ms                                                     | 61.2 ms: 1.09x faster                                          |
| xml_etree_parse          | 96.8 ms                                                     | 89.0 ms: 1.09x faster                                          |
| pprint_pformat           | 1.22 sec                                                    | 1.12 sec: 1.09x faster                                         |
| scimark_fft              | 187 ms                                                      | 174 ms: 1.08x faster                                           |
| meteor_contest           | 75.9 ms                                                     | 70.4 ms: 1.08x faster                                          |
| pprint_safe_repr         | 592 ms                                                      | 549 ms: 1.08x faster                                           |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.53 ms: 1.08x faster                                          |
| regex_effbot             | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                          |
| fannkuch                 | 256 ms                                                      | 247 ms: 1.04x faster                                           |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.9 ms: 1.03x faster                                          |
| logging_format           | 6.76 us                                                     | 6.69 us: 1.01x faster                                          |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                           |
| xml_etree_generate       | 55.5 ms                                                     | 55.9 ms: 1.01x slower                                          |
| async_generators         | 222 ms                                                      | 232 ms: 1.05x slower                                           |
| json_loads               | 14.0 us                                                     | 15.0 us: 1.07x slower                                          |
| telco                    | 3.94 ms                                                     | 4.55 ms: 1.15x slower                                          |
| python_startup_no_site   | 15.5 ms                                                     | 19.2 ms: 1.24x slower                                          |
| python_startup           | 20.6 ms                                                     | 25.9 ms: 1.26x slower                                          |
| gc_traversal             | 1.41 ms                                                     | 2.13 ms: 1.51x slower                                          |
| bench_mp_pool            | 62.0 ms                                                     | 94.1 ms: 1.52x slower                                          |
| create_gc_cycles         | 800 us                                                      | 1.31 ms: 1.64x slower                                          |
| logging_silent           | 94.6 ns                                                     | 317 ns: 3.35x slower                                           |
| coverage                 | 39.0 ms                                                     | 293 ms: 7.51x slower                                           |
| thrift                   | 617 us                                                      | 93.1 ms: 150.77x slower                                        |
| Geometric mean           | (ref)                                                       | 1.14x faster                                                   |

Benchmark hidden because not significant (2): logging_simple, json
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250530-3.15.0a0-25f01a3/bm-20250530-pythonperf1-amd64-zooba-gh_134923-3.15.0a0-25f01a3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.165x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown