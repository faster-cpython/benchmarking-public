# Results vs. 3.10.4

- fork: faster-cpython
- ref: never_inline_decref
- machine: windows-amd64
- commit hash: 2ab3a06
- commit date: 2025-06-27
- overall geometric mean: 1.273x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-pythonperf1-amd64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 222 ms: 1.11x faster                                                                |
| docutils       | 1.92 sec                                                    | 1.63 sec: 1.17x faster                                                              |
| html5lib       | 51.0 ms                                                     | 39.0 ms: 1.31x faster                                                               |
| Geometric mean | (ref)                                                       | 1.19x faster                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-pythonperf1-amd64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|-------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 399 ms: 2.78x faster                                                                |
| async_tree_none         | 435 ms                                                      | 173 ms: 2.52x faster                                                                |
| async_tree_memoization  | 526 ms                                                      | 209 ms: 2.51x faster                                                                |
| async_tree_cpu_io_mixed | 638 ms                                                      | 326 ms: 1.95x faster                                                                |
| Geometric mean          | (ref)                                                       | 2.42x faster                                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-pythonperf1-amd64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.9 ms: 1.41x faster                                                               |
| nbody          | 71.3 ms                                                     | 65.2 ms: 1.09x faster                                                               |
| pidigits       | 149 ms                                                      | 146 ms: 1.02x faster                                                                |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-pythonperf1-amd64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 81.8 ms: 1.30x faster                                                               |
| regex_dna      | 136 ms                                                      | 119 ms: 1.15x faster                                                                |
| regex_v8       | 15.4 ms                                                     | 13.7 ms: 1.12x faster                                                               |
| regex_effbot   | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                               |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-pythonperf1-amd64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.43 ms: 1.43x faster                                                               |
| unpickle_pure_python | 183 us                                                      | 135 us: 1.36x faster                                                                |
| pickle_pure_python   | 270 us                                                      | 211 us: 1.28x faster                                                                |
| tomli_loads          | 1.67 sec                                                    | 1.44 sec: 1.16x faster                                                              |
| xml_etree_process    | 44.5 ms                                                     | 39.4 ms: 1.13x faster                                                               |
| xml_etree_parse      | 96.8 ms                                                     | 92.1 ms: 1.05x faster                                                               |
| json_loads           | 14.0 us                                                     | 14.3 us: 1.02x slower                                                               |
| xml_etree_generate   | 55.5 ms                                                     | 56.5 ms: 1.02x slower                                                               |
| Geometric mean       | (ref)                                                       | 1.14x faster                                                                        |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-pythonperf1-amd64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.5 ms: 1.24x slower                                                               |
| python_startup_no_site | 15.5 ms                                                     | 19.4 ms: 1.25x slower                                                               |
| Geometric mean         | (ref)                                                       | 1.24x slower                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-pythonperf1-amd64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.76 ms: 1.34x faster                                                               |
| genshi_text     | 19.8 ms                                                     | 15.3 ms: 1.30x faster                                                               |
| django_template | 28.9 ms                                                     | 23.6 ms: 1.23x faster                                                               |
| genshi_xml      | 41.0 ms                                                     | 34.0 ms: 1.21x faster                                                               |
| Geometric mean  | (ref)                                                       | 1.27x faster                                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-pythonperf1-amd64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|--------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 102 us: 3.30x faster                                                                |
| async_tree_io            | 1.11 sec                                                    | 399 ms: 2.78x faster                                                                |
| async_tree_none          | 435 ms                                                      | 173 ms: 2.52x faster                                                                |
| async_tree_memoization   | 526 ms                                                      | 209 ms: 2.51x faster                                                                |
| pathlib                  | 75.7 ms                                                     | 31.8 ms: 2.38x faster                                                               |
| mdp                      | 1.78 sec                                                    | 807 ms: 2.21x faster                                                                |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 326 ms: 1.95x faster                                                                |
| deltablue                | 4.19 ms                                                     | 2.20 ms: 1.90x faster                                                               |
| go                       | 139 ms                                                      | 76.5 ms: 1.82x faster                                                               |
| pylint                   | 350 ms                                                      | 198 ms: 1.77x faster                                                                |
| logging_silent           | 94.6 ns                                                     | 55.2 ns: 1.72x faster                                                               |
| richards_super           | 52.2 ms                                                     | 30.5 ms: 1.71x faster                                                               |
| generators               | 32.4 ms                                                     | 19.6 ms: 1.65x faster                                                               |
| deepcopy_memo            | 28.8 us                                                     | 17.9 us: 1.61x faster                                                               |
| richards                 | 42.4 ms                                                     | 26.8 ms: 1.58x faster                                                               |
| raytrace                 | 273 ms                                                      | 177 ms: 1.55x faster                                                                |
| chaos                    | 61.7 ms                                                     | 40.4 ms: 1.53x faster                                                               |
| scimark_lu               | 85.8 ms                                                     | 57.1 ms: 1.50x faster                                                               |
| deepcopy                 | 255 us                                                      | 172 us: 1.49x faster                                                                |
| comprehensions           | 16.5 us                                                     | 11.1 us: 1.49x faster                                                               |
| json_dumps               | 9.16 ms                                                     | 6.43 ms: 1.43x faster                                                               |
| float                    | 61.7 ms                                                     | 43.9 ms: 1.41x faster                                                               |
| scimark_monte_carlo      | 57.3 ms                                                     | 41.0 ms: 1.40x faster                                                               |
| pyflate                  | 409 ms                                                      | 294 ms: 1.39x faster                                                                |
| scimark_sor              | 106 ms                                                      | 76.5 ms: 1.39x faster                                                               |
| hexiom                   | 5.74 ms                                                     | 4.18 ms: 1.38x faster                                                               |
| unpickle_pure_python     | 183 us                                                      | 135 us: 1.36x faster                                                                |
| mako                     | 9.03 ms                                                     | 6.76 ms: 1.34x faster                                                               |
| pycparser                | 930 ms                                                      | 706 ms: 1.32x faster                                                                |
| html5lib                 | 51.0 ms                                                     | 39.0 ms: 1.31x faster                                                               |
| crypto_pyaes             | 62.5 ms                                                     | 47.9 ms: 1.30x faster                                                               |
| genshi_text              | 19.8 ms                                                     | 15.3 ms: 1.30x faster                                                               |
| regex_compile            | 106 ms                                                      | 81.8 ms: 1.30x faster                                                               |
| pickle_pure_python       | 270 us                                                      | 211 us: 1.28x faster                                                                |
| thrift                   | 617 us                                                      | 498 us: 1.24x faster                                                                |
| dulwich_log              | 50.5 ms                                                     | 41.1 ms: 1.23x faster                                                               |
| django_template          | 28.9 ms                                                     | 23.6 ms: 1.23x faster                                                               |
| sympy_integrate          | 15.3 ms                                                     | 12.5 ms: 1.23x faster                                                               |
| sympy_sum                | 107 ms                                                      | 87.8 ms: 1.22x faster                                                               |
| sqlite_synth             | 1.91 us                                                     | 1.58 us: 1.21x faster                                                               |
| genshi_xml               | 41.0 ms                                                     | 34.0 ms: 1.21x faster                                                               |
| spectral_norm            | 77.3 ms                                                     | 64.3 ms: 1.20x faster                                                               |
| pprint_pformat           | 1.22 sec                                                    | 1.03 sec: 1.18x faster                                                              |
| deepcopy_reduce          | 2.20 us                                                     | 1.87 us: 1.18x faster                                                               |
| docutils                 | 1.92 sec                                                    | 1.63 sec: 1.17x faster                                                              |
| pprint_safe_repr         | 592 ms                                                      | 509 ms: 1.16x faster                                                                |
| tomli_loads              | 1.67 sec                                                    | 1.44 sec: 1.16x faster                                                              |
| sympy_str                | 194 ms                                                      | 169 ms: 1.15x faster                                                                |
| regex_dna                | 136 ms                                                      | 119 ms: 1.15x faster                                                                |
| xml_etree_process        | 44.5 ms                                                     | 39.4 ms: 1.13x faster                                                               |
| regex_v8                 | 15.4 ms                                                     | 13.7 ms: 1.12x faster                                                               |
| 2to3                     | 246 ms                                                      | 222 ms: 1.11x faster                                                                |
| nbody                    | 71.3 ms                                                     | 65.2 ms: 1.09x faster                                                               |
| sympy_expand             | 314 ms                                                      | 290 ms: 1.08x faster                                                                |
| coroutines               | 16.0 ms                                                     | 14.8 ms: 1.08x faster                                                               |
| regex_effbot             | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                               |
| nqueens                  | 66.6 ms                                                     | 63.0 ms: 1.06x faster                                                               |
| xml_etree_parse          | 96.8 ms                                                     | 92.1 ms: 1.05x faster                                                               |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.62 ms: 1.04x faster                                                               |
| meteor_contest           | 75.9 ms                                                     | 73.9 ms: 1.03x faster                                                               |
| pidigits                 | 149 ms                                                      | 146 ms: 1.02x faster                                                                |
| logging_format           | 6.76 us                                                     | 6.67 us: 1.01x faster                                                               |
| scimark_fft              | 187 ms                                                      | 185 ms: 1.01x faster                                                                |
| json                     | 3.14 ms                                                     | 3.11 ms: 1.01x faster                                                               |
| json_loads               | 14.0 us                                                     | 14.3 us: 1.02x slower                                                               |
| xml_etree_generate       | 55.5 ms                                                     | 56.5 ms: 1.02x slower                                                               |
| fannkuch                 | 256 ms                                                      | 261 ms: 1.02x slower                                                                |
| async_generators         | 222 ms                                                      | 243 ms: 1.10x slower                                                                |
| telco                    | 3.94 ms                                                     | 4.73 ms: 1.20x slower                                                               |
| python_startup           | 20.6 ms                                                     | 25.5 ms: 1.24x slower                                                               |
| python_startup_no_site   | 15.5 ms                                                     | 19.4 ms: 1.25x slower                                                               |
| coverage                 | 39.0 ms                                                     | 52.3 ms: 1.34x slower                                                               |
| gc_traversal             | 1.41 ms                                                     | 2.18 ms: 1.54x slower                                                               |
| create_gc_cycles         | 800 us                                                      | 1.33 ms: 1.66x slower                                                               |
| Geometric mean           | (ref)                                                       | 1.28x faster                                                                        |

Benchmark hidden because not significant (2): logging_simple, xml_etree_iterparse
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250627-3.15.0a0-2ab3a06/bm-20250627-pythonperf1-amd64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.273x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: unknown