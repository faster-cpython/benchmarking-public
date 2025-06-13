# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: pylong_compactadd
- machine: windows-amd64
- commit hash: 4019a15
- commit date: 2025-06-14
- overall geometric mean: 1.168x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1-amd64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 222 ms: 1.11x faster                                                              |
| docutils       | 1.92 sec                                                    | 1.63 sec: 1.18x faster                                                            |
| html5lib       | 51.0 ms                                                     | 38.6 ms: 1.32x faster                                                             |
| Geometric mean | (ref)                                                       | 1.20x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1-amd64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 397 ms: 2.80x faster                                                              |
| async_tree_memoization  | 526 ms                                                      | 204 ms: 2.58x faster                                                              |
| async_tree_none         | 435 ms                                                      | 170 ms: 2.56x faster                                                              |
| async_tree_cpu_io_mixed | 638 ms                                                      | 327 ms: 1.95x faster                                                              |
| Geometric mean          | (ref)                                                       | 2.45x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1-amd64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.7 ms: 1.41x faster                                                             |
| nbody          | 71.3 ms                                                     | 62.0 ms: 1.15x faster                                                             |
| pidigits       | 149 ms                                                      | 145 ms: 1.03x faster                                                              |
| Geometric mean | (ref)                                                       | 1.19x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1-amd64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 79.3 ms: 1.34x faster                                                             |
| regex_dna      | 136 ms                                                      | 122 ms: 1.12x faster                                                              |
| regex_v8       | 15.4 ms                                                     | 14.0 ms: 1.10x faster                                                             |
| regex_effbot   | 1.66 ms                                                     | 1.51 ms: 1.09x faster                                                             |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1-amd64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.36 ms: 1.44x faster                                                             |
| unpickle_pure_python | 183 us                                                      | 131 us: 1.40x faster                                                              |
| pickle_pure_python   | 270 us                                                      | 208 us: 1.29x faster                                                              |
| tomli_loads          | 1.67 sec                                                    | 1.37 sec: 1.22x faster                                                            |
| xml_etree_process    | 44.5 ms                                                     | 39.2 ms: 1.13x faster                                                             |
| xml_etree_parse      | 96.8 ms                                                     | 87.9 ms: 1.10x faster                                                             |
| Geometric mean       | (ref)                                                       | 1.17x faster                                                                      |

Benchmark hidden because not significant (3): xml_etree_iterparse, xml_etree_generate, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1-amd64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.3 ms: 1.24x slower                                                             |
| python_startup         | 20.6 ms                                                     | 26.2 ms: 1.27x slower                                                             |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1-amd64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.54 ms: 1.38x faster                                                             |
| genshi_text     | 19.8 ms                                                     | 15.1 ms: 1.31x faster                                                             |
| genshi_xml      | 41.0 ms                                                     | 33.7 ms: 1.22x faster                                                             |
| django_template | 28.9 ms                                                     | 23.9 ms: 1.21x faster                                                             |
| Geometric mean  | (ref)                                                       | 1.28x faster                                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1-amd64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 101 us: 3.32x faster                                                              |
| async_tree_io            | 1.11 sec                                                    | 397 ms: 2.80x faster                                                              |
| async_tree_memoization   | 526 ms                                                      | 204 ms: 2.58x faster                                                              |
| async_tree_none          | 435 ms                                                      | 170 ms: 2.56x faster                                                              |
| pathlib                  | 75.7 ms                                                     | 31.5 ms: 2.40x faster                                                             |
| mdp                      | 1.78 sec                                                    | 795 ms: 2.24x faster                                                              |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 327 ms: 1.95x faster                                                              |
| deltablue                | 4.19 ms                                                     | 2.19 ms: 1.91x faster                                                             |
| go                       | 139 ms                                                      | 75.8 ms: 1.83x faster                                                             |
| pylint                   | 350 ms                                                      | 199 ms: 1.76x faster                                                              |
| richards_super           | 52.2 ms                                                     | 30.5 ms: 1.71x faster                                                             |
| generators               | 32.4 ms                                                     | 19.3 ms: 1.68x faster                                                             |
| richards                 | 42.4 ms                                                     | 27.1 ms: 1.57x faster                                                             |
| comprehensions           | 16.5 us                                                     | 10.6 us: 1.55x faster                                                             |
| chaos                    | 61.7 ms                                                     | 40.2 ms: 1.54x faster                                                             |
| raytrace                 | 273 ms                                                      | 182 ms: 1.50x faster                                                              |
| deepcopy                 | 255 us                                                      | 171 us: 1.49x faster                                                              |
| scimark_lu               | 85.8 ms                                                     | 58.1 ms: 1.48x faster                                                             |
| deepcopy_memo            | 28.8 us                                                     | 19.5 us: 1.48x faster                                                             |
| pyflate                  | 409 ms                                                      | 280 ms: 1.46x faster                                                              |
| scimark_monte_carlo      | 57.3 ms                                                     | 39.4 ms: 1.45x faster                                                             |
| json_dumps               | 9.16 ms                                                     | 6.36 ms: 1.44x faster                                                             |
| hexiom                   | 5.74 ms                                                     | 4.03 ms: 1.42x faster                                                             |
| float                    | 61.7 ms                                                     | 43.7 ms: 1.41x faster                                                             |
| scimark_sor              | 106 ms                                                      | 75.5 ms: 1.41x faster                                                             |
| unpickle_pure_python     | 183 us                                                      | 131 us: 1.40x faster                                                              |
| mako                     | 9.03 ms                                                     | 6.54 ms: 1.38x faster                                                             |
| regex_compile            | 106 ms                                                      | 79.3 ms: 1.34x faster                                                             |
| crypto_pyaes             | 62.5 ms                                                     | 47.0 ms: 1.33x faster                                                             |
| html5lib                 | 51.0 ms                                                     | 38.6 ms: 1.32x faster                                                             |
| genshi_text              | 19.8 ms                                                     | 15.1 ms: 1.31x faster                                                             |
| pickle_pure_python       | 270 us                                                      | 208 us: 1.29x faster                                                              |
| pycparser                | 930 ms                                                      | 725 ms: 1.28x faster                                                              |
| spectral_norm            | 77.3 ms                                                     | 61.6 ms: 1.25x faster                                                             |
| sympy_integrate          | 15.3 ms                                                     | 12.4 ms: 1.23x faster                                                             |
| dulwich_log              | 50.5 ms                                                     | 41.2 ms: 1.22x faster                                                             |
| tomli_loads              | 1.67 sec                                                    | 1.37 sec: 1.22x faster                                                            |
| sympy_sum                | 107 ms                                                      | 87.7 ms: 1.22x faster                                                             |
| genshi_xml               | 41.0 ms                                                     | 33.7 ms: 1.22x faster                                                             |
| deepcopy_reduce          | 2.20 us                                                     | 1.81 us: 1.22x faster                                                             |
| django_template          | 28.9 ms                                                     | 23.9 ms: 1.21x faster                                                             |
| sqlite_synth             | 1.91 us                                                     | 1.58 us: 1.21x faster                                                             |
| docutils                 | 1.92 sec                                                    | 1.63 sec: 1.18x faster                                                            |
| sympy_str                | 194 ms                                                      | 168 ms: 1.16x faster                                                              |
| nbody                    | 71.3 ms                                                     | 62.0 ms: 1.15x faster                                                             |
| coroutines               | 16.0 ms                                                     | 14.1 ms: 1.14x faster                                                             |
| xml_etree_process        | 44.5 ms                                                     | 39.2 ms: 1.13x faster                                                             |
| regex_dna                | 136 ms                                                      | 122 ms: 1.12x faster                                                              |
| pprint_pformat           | 1.22 sec                                                    | 1.10 sec: 1.11x faster                                                            |
| 2to3                     | 246 ms                                                      | 222 ms: 1.11x faster                                                              |
| nqueens                  | 66.6 ms                                                     | 60.2 ms: 1.11x faster                                                             |
| pprint_safe_repr         | 592 ms                                                      | 537 ms: 1.10x faster                                                              |
| xml_etree_parse          | 96.8 ms                                                     | 87.9 ms: 1.10x faster                                                             |
| regex_v8                 | 15.4 ms                                                     | 14.0 ms: 1.10x faster                                                             |
| regex_effbot             | 1.66 ms                                                     | 1.51 ms: 1.09x faster                                                             |
| sympy_expand             | 314 ms                                                      | 290 ms: 1.08x faster                                                              |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.55 ms: 1.07x faster                                                             |
| scimark_fft              | 187 ms                                                      | 176 ms: 1.06x faster                                                              |
| meteor_contest           | 75.9 ms                                                     | 72.5 ms: 1.05x faster                                                             |
| json                     | 3.14 ms                                                     | 3.01 ms: 1.04x faster                                                             |
| pidigits                 | 149 ms                                                      | 145 ms: 1.03x faster                                                              |
| fannkuch                 | 256 ms                                                      | 258 ms: 1.01x slower                                                              |
| logging_format           | 6.76 us                                                     | 6.92 us: 1.02x slower                                                             |
| logging_simple           | 6.22 us                                                     | 6.40 us: 1.03x slower                                                             |
| async_generators         | 222 ms                                                      | 231 ms: 1.04x slower                                                              |
| telco                    | 3.94 ms                                                     | 4.49 ms: 1.14x slower                                                             |
| python_startup_no_site   | 15.5 ms                                                     | 19.3 ms: 1.24x slower                                                             |
| python_startup           | 20.6 ms                                                     | 26.2 ms: 1.27x slower                                                             |
| gc_traversal             | 1.41 ms                                                     | 2.16 ms: 1.53x slower                                                             |
| create_gc_cycles         | 800 us                                                      | 1.34 ms: 1.67x slower                                                             |
| logging_silent           | 94.6 ns                                                     | 321 ns: 3.40x slower                                                              |
| coverage                 | 39.0 ms                                                     | 294 ms: 7.53x slower                                                              |
| thrift                   | 617 us                                                      | 98.7 ms: 159.81x slower                                                           |
| Geometric mean           | (ref)                                                       | 1.15x faster                                                                      |

Benchmark hidden because not significant (3): xml_etree_iterparse, xml_etree_generate, json_loads
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250614-3.15.0a0-4019a15/bm-20250614-pythonperf1-amd64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.168x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown