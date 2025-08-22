# Results vs. 3.10.4

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: windows-amd64
- commit hash: dc660a2
- commit date: 2025-08-22
- overall geometric mean: 1.349x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 215 ms: 1.14x faster                                                               |
| docutils       | 1.92 sec                                                    | 1.61 sec: 1.19x faster                                                             |
| html5lib       | 51.0 ms                                                     | 38.1 ms: 1.34x faster                                                              |
| Geometric mean | (ref)                                                       | 1.22x faster                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|-------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 385 ms: 2.88x faster                                                               |
| async_tree_memoization  | 526 ms                                                      | 203 ms: 2.60x faster                                                               |
| async_tree_none         | 435 ms                                                      | 171 ms: 2.55x faster                                                               |
| async_tree_cpu_io_mixed | 638 ms                                                      | 330 ms: 1.93x faster                                                               |
| Geometric mean          | (ref)                                                       | 2.47x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 42.6 ms: 1.67x faster                                                              |
| float          | 61.7 ms                                                     | 43.6 ms: 1.41x faster                                                              |
| pidigits       | 149 ms                                                      | 145 ms: 1.03x faster                                                               |
| Geometric mean | (ref)                                                       | 1.34x faster                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.3 ms: 1.35x faster                                                              |
| regex_dna      | 136 ms                                                      | 119 ms: 1.15x faster                                                               |
| regex_v8       | 15.4 ms                                                     | 14.0 ms: 1.10x faster                                                              |
| regex_effbot   | 1.66 ms                                                     | 1.54 ms: 1.08x faster                                                              |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 105 us: 1.74x faster                                                               |
| json_dumps           | 9.16 ms                                                     | 5.32 ms: 1.72x faster                                                              |
| tomli_loads          | 1.67 sec                                                    | 1.08 sec: 1.55x faster                                                             |
| pickle_pure_python   | 270 us                                                      | 203 us: 1.33x faster                                                               |
| xml_etree_process    | 44.5 ms                                                     | 35.0 ms: 1.27x faster                                                              |
| xml_etree_parse      | 96.8 ms                                                     | 83.1 ms: 1.16x faster                                                              |
| xml_etree_generate   | 55.5 ms                                                     | 48.8 ms: 1.14x faster                                                              |
| xml_etree_iterparse  | 65.0 ms                                                     | 60.7 ms: 1.07x faster                                                              |
| Geometric mean       | (ref)                                                       | 1.31x faster                                                                       |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.3 ms: 1.23x slower                                                              |
| python_startup_no_site | 15.5 ms                                                     | 19.3 ms: 1.24x slower                                                              |
| Geometric mean         | (ref)                                                       | 1.23x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.53 ms: 1.63x faster                                                              |
| genshi_text     | 19.8 ms                                                     | 15.6 ms: 1.27x faster                                                              |
| django_template | 28.9 ms                                                     | 24.1 ms: 1.20x faster                                                              |
| genshi_xml      | 41.0 ms                                                     | 35.2 ms: 1.17x faster                                                              |
| Geometric mean  | (ref)                                                       | 1.30x faster                                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|--------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 103 us: 3.27x faster                                                               |
| async_tree_io            | 1.11 sec                                                    | 385 ms: 2.88x faster                                                               |
| async_tree_memoization   | 526 ms                                                      | 203 ms: 2.60x faster                                                               |
| pathlib                  | 75.7 ms                                                     | 29.5 ms: 2.56x faster                                                              |
| async_tree_none          | 435 ms                                                      | 171 ms: 2.55x faster                                                               |
| mdp                      | 1.78 sec                                                    | 793 ms: 2.25x faster                                                               |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 330 ms: 1.93x faster                                                               |
| deltablue                | 4.19 ms                                                     | 2.26 ms: 1.85x faster                                                              |
| pylint                   | 350 ms                                                      | 193 ms: 1.81x faster                                                               |
| go                       | 139 ms                                                      | 77.1 ms: 1.80x faster                                                              |
| unpickle_pure_python     | 183 us                                                      | 105 us: 1.74x faster                                                               |
| json_dumps               | 9.16 ms                                                     | 5.32 ms: 1.72x faster                                                              |
| logging_silent           | 94.6 ns                                                     | 55.1 ns: 1.72x faster                                                              |
| richards_super           | 52.2 ms                                                     | 30.7 ms: 1.70x faster                                                              |
| nbody                    | 71.3 ms                                                     | 42.6 ms: 1.67x faster                                                              |
| generators               | 32.4 ms                                                     | 19.6 ms: 1.65x faster                                                              |
| mako                     | 9.03 ms                                                     | 5.53 ms: 1.63x faster                                                              |
| pyflate                  | 409 ms                                                      | 258 ms: 1.58x faster                                                               |
| raytrace                 | 273 ms                                                      | 173 ms: 1.58x faster                                                               |
| comprehensions           | 16.5 us                                                     | 10.4 us: 1.58x faster                                                              |
| richards                 | 42.4 ms                                                     | 27.0 ms: 1.57x faster                                                              |
| tomli_loads              | 1.67 sec                                                    | 1.08 sec: 1.55x faster                                                             |
| chaos                    | 61.7 ms                                                     | 40.3 ms: 1.53x faster                                                              |
| deepcopy_memo            | 28.8 us                                                     | 19.0 us: 1.52x faster                                                              |
| deepcopy                 | 255 us                                                      | 169 us: 1.51x faster                                                               |
| scimark_lu               | 85.8 ms                                                     | 58.8 ms: 1.46x faster                                                              |
| hexiom                   | 5.74 ms                                                     | 3.94 ms: 1.46x faster                                                              |
| crypto_pyaes             | 62.5 ms                                                     | 43.5 ms: 1.44x faster                                                              |
| pprint_safe_repr         | 592 ms                                                      | 412 ms: 1.44x faster                                                               |
| pprint_pformat           | 1.22 sec                                                    | 851 ms: 1.43x faster                                                               |
| float                    | 61.7 ms                                                     | 43.6 ms: 1.41x faster                                                              |
| scimark_monte_carlo      | 57.3 ms                                                     | 41.0 ms: 1.40x faster                                                              |
| scimark_sor              | 106 ms                                                      | 77.3 ms: 1.37x faster                                                              |
| pycparser                | 930 ms                                                      | 684 ms: 1.36x faster                                                               |
| regex_compile            | 106 ms                                                      | 78.3 ms: 1.35x faster                                                              |
| html5lib                 | 51.0 ms                                                     | 38.1 ms: 1.34x faster                                                              |
| pickle_pure_python       | 270 us                                                      | 203 us: 1.33x faster                                                               |
| scimark_fft              | 187 ms                                                      | 142 ms: 1.32x faster                                                               |
| thrift                   | 617 us                                                      | 478 us: 1.29x faster                                                               |
| dulwich_log              | 50.5 ms                                                     | 39.3 ms: 1.28x faster                                                              |
| xml_etree_process        | 44.5 ms                                                     | 35.0 ms: 1.27x faster                                                              |
| genshi_text              | 19.8 ms                                                     | 15.6 ms: 1.27x faster                                                              |
| sympy_sum                | 107 ms                                                      | 85.6 ms: 1.25x faster                                                              |
| sqlite_synth             | 1.91 us                                                     | 1.54 us: 1.24x faster                                                              |
| spectral_norm            | 77.3 ms                                                     | 62.7 ms: 1.23x faster                                                              |
| sympy_integrate          | 15.3 ms                                                     | 12.5 ms: 1.23x faster                                                              |
| fannkuch                 | 256 ms                                                      | 209 ms: 1.22x faster                                                               |
| deepcopy_reduce          | 2.20 us                                                     | 1.81 us: 1.22x faster                                                              |
| django_template          | 28.9 ms                                                     | 24.1 ms: 1.20x faster                                                              |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.28 ms: 1.19x faster                                                              |
| docutils                 | 1.92 sec                                                    | 1.61 sec: 1.19x faster                                                             |
| genshi_xml               | 41.0 ms                                                     | 35.2 ms: 1.17x faster                                                              |
| xml_etree_parse          | 96.8 ms                                                     | 83.1 ms: 1.16x faster                                                              |
| sympy_str                | 194 ms                                                      | 167 ms: 1.16x faster                                                               |
| regex_dna                | 136 ms                                                      | 119 ms: 1.15x faster                                                               |
| 2to3                     | 246 ms                                                      | 215 ms: 1.14x faster                                                               |
| nqueens                  | 66.6 ms                                                     | 58.4 ms: 1.14x faster                                                              |
| xml_etree_generate       | 55.5 ms                                                     | 48.8 ms: 1.14x faster                                                              |
| coroutines               | 16.0 ms                                                     | 14.3 ms: 1.12x faster                                                              |
| json                     | 3.14 ms                                                     | 2.82 ms: 1.11x faster                                                              |
| regex_v8                 | 15.4 ms                                                     | 14.0 ms: 1.10x faster                                                              |
| sympy_expand             | 314 ms                                                      | 287 ms: 1.10x faster                                                               |
| meteor_contest           | 75.9 ms                                                     | 69.8 ms: 1.09x faster                                                              |
| regex_effbot             | 1.66 ms                                                     | 1.54 ms: 1.08x faster                                                              |
| xml_etree_iterparse      | 65.0 ms                                                     | 60.7 ms: 1.07x faster                                                              |
| telco                    | 3.94 ms                                                     | 3.77 ms: 1.05x faster                                                              |
| logging_format           | 6.76 us                                                     | 6.48 us: 1.04x faster                                                              |
| logging_simple           | 6.22 us                                                     | 6.02 us: 1.03x faster                                                              |
| pidigits                 | 149 ms                                                      | 145 ms: 1.03x faster                                                               |
| async_generators         | 222 ms                                                      | 239 ms: 1.08x slower                                                               |
| python_startup           | 20.6 ms                                                     | 25.3 ms: 1.23x slower                                                              |
| python_startup_no_site   | 15.5 ms                                                     | 19.3 ms: 1.24x slower                                                              |
| coverage                 | 39.0 ms                                                     | 49.8 ms: 1.28x slower                                                              |
| gc_traversal             | 1.41 ms                                                     | 2.07 ms: 1.47x slower                                                              |
| create_gc_cycles         | 800 us                                                      | 1.29 ms: 1.61x slower                                                              |
| Geometric mean           | (ref)                                                       | 1.35x faster                                                                       |

Benchmark hidden because not significant (1): json_loads
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250822-3.15.0a0-dc660a2-JIT/bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.349x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: unknown