# Results vs. 3.10.4

- fork: faster-cpython
- ref: jit_trampoline
- machine: windows-amd64
- commit hash: 14080cb
- commit date: 2025-08-19
- overall geometric mean: 1.321x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250819-pythonperf1-amd64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 219 ms: 1.12x faster                                                           |
| docutils       | 1.92 sec                                                    | 1.66 sec: 1.16x faster                                                         |
| html5lib       | 51.0 ms                                                     | 38.9 ms: 1.31x faster                                                          |
| Geometric mean | (ref)                                                       | 1.19x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250819-pythonperf1-amd64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|-------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 393 ms: 2.82x faster                                                           |
| async_tree_memoization  | 526 ms                                                      | 204 ms: 2.58x faster                                                           |
| async_tree_none         | 435 ms                                                      | 173 ms: 2.52x faster                                                           |
| async_tree_cpu_io_mixed | 638 ms                                                      | 331 ms: 1.92x faster                                                           |
| Geometric mean          | (ref)                                                       | 2.44x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250819-pythonperf1-amd64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.6 ms: 1.41x faster                                                          |
| nbody          | 71.3 ms                                                     | 58.0 ms: 1.23x faster                                                          |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                       | 1.21x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250819-pythonperf1-amd64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 79.2 ms: 1.34x faster                                                          |
| regex_dna      | 136 ms                                                      | 118 ms: 1.15x faster                                                           |
| regex_v8       | 15.4 ms                                                     | 13.9 ms: 1.11x faster                                                          |
| regex_effbot   | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                          |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250819-pythonperf1-amd64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 105 us: 1.75x faster                                                           |
| json_dumps           | 9.16 ms                                                     | 5.34 ms: 1.72x faster                                                          |
| tomli_loads          | 1.67 sec                                                    | 1.12 sec: 1.49x faster                                                         |
| pickle_pure_python   | 270 us                                                      | 205 us: 1.31x faster                                                           |
| xml_etree_process    | 44.5 ms                                                     | 36.2 ms: 1.23x faster                                                          |
| xml_etree_parse      | 96.8 ms                                                     | 88.6 ms: 1.09x faster                                                          |
| xml_etree_generate   | 55.5 ms                                                     | 50.9 ms: 1.09x faster                                                          |
| Geometric mean       | (ref)                                                       | 1.27x faster                                                                   |

Benchmark hidden because not significant (2): xml_etree_iterparse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250819-pythonperf1-amd64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.0 ms: 1.23x slower                                                          |
| python_startup         | 20.6 ms                                                     | 25.8 ms: 1.25x slower                                                          |
| Geometric mean         | (ref)                                                       | 1.24x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250819-pythonperf1-amd64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.34 ms: 1.69x faster                                                          |
| genshi_text     | 19.8 ms                                                     | 15.7 ms: 1.26x faster                                                          |
| django_template | 28.9 ms                                                     | 24.2 ms: 1.19x faster                                                          |
| genshi_xml      | 41.0 ms                                                     | 35.4 ms: 1.16x faster                                                          |
| Geometric mean  | (ref)                                                       | 1.31x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250819-pythonperf1-amd64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 102 us: 3.29x faster                                                           |
| async_tree_io            | 1.11 sec                                                    | 393 ms: 2.82x faster                                                           |
| pathlib                  | 75.7 ms                                                     | 29.3 ms: 2.58x faster                                                          |
| async_tree_memoization   | 526 ms                                                      | 204 ms: 2.58x faster                                                           |
| async_tree_none          | 435 ms                                                      | 173 ms: 2.52x faster                                                           |
| mdp                      | 1.78 sec                                                    | 802 ms: 2.22x faster                                                           |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 331 ms: 1.92x faster                                                           |
| deltablue                | 4.19 ms                                                     | 2.22 ms: 1.88x faster                                                          |
| go                       | 139 ms                                                      | 77.8 ms: 1.79x faster                                                          |
| pylint                   | 350 ms                                                      | 198 ms: 1.77x faster                                                           |
| unpickle_pure_python     | 183 us                                                      | 105 us: 1.75x faster                                                           |
| logging_silent           | 94.6 ns                                                     | 54.3 ns: 1.74x faster                                                          |
| json_dumps               | 9.16 ms                                                     | 5.34 ms: 1.72x faster                                                          |
| mako                     | 9.03 ms                                                     | 5.34 ms: 1.69x faster                                                          |
| richards_super           | 52.2 ms                                                     | 31.3 ms: 1.67x faster                                                          |
| generators               | 32.4 ms                                                     | 19.5 ms: 1.66x faster                                                          |
| deepcopy_memo            | 28.8 us                                                     | 18.0 us: 1.60x faster                                                          |
| pyflate                  | 409 ms                                                      | 261 ms: 1.57x faster                                                           |
| comprehensions           | 16.5 us                                                     | 10.5 us: 1.57x faster                                                          |
| richards                 | 42.4 ms                                                     | 27.9 ms: 1.52x faster                                                          |
| chaos                    | 61.7 ms                                                     | 40.7 ms: 1.52x faster                                                          |
| raytrace                 | 273 ms                                                      | 183 ms: 1.50x faster                                                           |
| deepcopy                 | 255 us                                                      | 171 us: 1.49x faster                                                           |
| tomli_loads              | 1.67 sec                                                    | 1.12 sec: 1.49x faster                                                         |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.2 ms: 1.43x faster                                                          |
| float                    | 61.7 ms                                                     | 43.6 ms: 1.41x faster                                                          |
| hexiom                   | 5.74 ms                                                     | 4.06 ms: 1.41x faster                                                          |
| scimark_lu               | 85.8 ms                                                     | 61.1 ms: 1.40x faster                                                          |
| scimark_sor              | 106 ms                                                      | 76.9 ms: 1.38x faster                                                          |
| crypto_pyaes             | 62.5 ms                                                     | 45.5 ms: 1.38x faster                                                          |
| pprint_pformat           | 1.22 sec                                                    | 890 ms: 1.37x faster                                                           |
| pprint_safe_repr         | 592 ms                                                      | 440 ms: 1.34x faster                                                           |
| regex_compile            | 106 ms                                                      | 79.2 ms: 1.34x faster                                                          |
| pycparser                | 930 ms                                                      | 708 ms: 1.31x faster                                                           |
| pickle_pure_python       | 270 us                                                      | 205 us: 1.31x faster                                                           |
| html5lib                 | 51.0 ms                                                     | 38.9 ms: 1.31x faster                                                          |
| genshi_text              | 19.8 ms                                                     | 15.7 ms: 1.26x faster                                                          |
| dulwich_log              | 50.5 ms                                                     | 40.4 ms: 1.25x faster                                                          |
| sqlite_synth             | 1.91 us                                                     | 1.54 us: 1.24x faster                                                          |
| thrift                   | 617 us                                                      | 501 us: 1.23x faster                                                           |
| nbody                    | 71.3 ms                                                     | 58.0 ms: 1.23x faster                                                          |
| sympy_sum                | 107 ms                                                      | 87.2 ms: 1.23x faster                                                          |
| xml_etree_process        | 44.5 ms                                                     | 36.2 ms: 1.23x faster                                                          |
| scimark_fft              | 187 ms                                                      | 153 ms: 1.22x faster                                                           |
| fannkuch                 | 256 ms                                                      | 210 ms: 1.22x faster                                                           |
| sympy_integrate          | 15.3 ms                                                     | 12.8 ms: 1.20x faster                                                          |
| django_template          | 28.9 ms                                                     | 24.2 ms: 1.19x faster                                                          |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.29 ms: 1.19x faster                                                          |
| spectral_norm            | 77.3 ms                                                     | 65.3 ms: 1.18x faster                                                          |
| deepcopy_reduce          | 2.20 us                                                     | 1.87 us: 1.18x faster                                                          |
| genshi_xml               | 41.0 ms                                                     | 35.4 ms: 1.16x faster                                                          |
| docutils                 | 1.92 sec                                                    | 1.66 sec: 1.16x faster                                                         |
| regex_dna                | 136 ms                                                      | 118 ms: 1.15x faster                                                           |
| sympy_str                | 194 ms                                                      | 170 ms: 1.14x faster                                                           |
| 2to3                     | 246 ms                                                      | 219 ms: 1.12x faster                                                           |
| regex_v8                 | 15.4 ms                                                     | 13.9 ms: 1.11x faster                                                          |
| coroutines               | 16.0 ms                                                     | 14.5 ms: 1.10x faster                                                          |
| nqueens                  | 66.6 ms                                                     | 60.8 ms: 1.10x faster                                                          |
| xml_etree_parse          | 96.8 ms                                                     | 88.6 ms: 1.09x faster                                                          |
| xml_etree_generate       | 55.5 ms                                                     | 50.9 ms: 1.09x faster                                                          |
| meteor_contest           | 75.9 ms                                                     | 71.4 ms: 1.06x faster                                                          |
| regex_effbot             | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                          |
| sympy_expand             | 314 ms                                                      | 298 ms: 1.05x faster                                                           |
| logging_format           | 6.76 us                                                     | 6.45 us: 1.05x faster                                                          |
| json                     | 3.14 ms                                                     | 3.00 ms: 1.04x faster                                                          |
| logging_simple           | 6.22 us                                                     | 5.97 us: 1.04x faster                                                          |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                                           |
| telco                    | 3.94 ms                                                     | 4.06 ms: 1.03x slower                                                          |
| async_generators         | 222 ms                                                      | 247 ms: 1.11x slower                                                           |
| python_startup_no_site   | 15.5 ms                                                     | 19.0 ms: 1.23x slower                                                          |
| python_startup           | 20.6 ms                                                     | 25.8 ms: 1.25x slower                                                          |
| coverage                 | 39.0 ms                                                     | 50.0 ms: 1.28x slower                                                          |
| gc_traversal             | 1.41 ms                                                     | 2.10 ms: 1.49x slower                                                          |
| create_gc_cycles         | 800 us                                                      | 1.27 ms: 1.58x slower                                                          |
| Geometric mean           | (ref)                                                       | 1.32x faster                                                                   |

Benchmark hidden because not significant (2): xml_etree_iterparse, json_loads
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250819-3.15.0a0-14080cb-JIT/bm-20250819-pythonperf1-amd64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.321x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: unknown