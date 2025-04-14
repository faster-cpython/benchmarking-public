# Results vs. base

- fork: iritkatriel
- ref: dicts
- machine: linux-x86_64
- commit hash: bf2d1dd
- commit date: 2025-04-10
- overall geometric mean: 1.007x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250407-linux-x86_64-python-f0dcb29d3affbbe1ec25-3.14.0a6+-f0dcb29 | bm-20250410-linux-x86_64-iritkatriel-dicts-3.14.0a6+-bf2d1dd |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 249 ms: 1.01x faster                                         |
| docutils       | 2.58 sec                                                               | 2.59 sec: 1.01x slower                                       |
| html5lib       | 60.5 ms                                                                | 61.3 ms: 1.01x slower                                        |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                 |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250407-linux-x86_64-python-f0dcb29d3affbbe1ec25-3.14.0a6+-f0dcb29 | bm-20250410-linux-x86_64-iritkatriel-dicts-3.14.0a6+-bf2d1dd |
|-------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| coroutines              | 24.4 ms                                                                | 23.1 ms: 1.06x faster                                        |
| async_tree_cpu_io_mixed | 478 ms                                                                 | 474 ms: 1.01x faster                                         |
| async_tree_memoization  | 310 ms                                                                 | 308 ms: 1.01x faster                                         |
| async_generators        | 388 ms                                                                 | 394 ms: 1.02x slower                                         |
| Geometric mean          | (ref)                                                                  | 1.01x faster                                                 |

Benchmark hidden because not significant (7): async_tree_io, async_tree_none, asyncio_websockets, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250407-linux-x86_64-python-f0dcb29d3affbbe1ec25-3.14.0a6+-f0dcb29 | bm-20250410-linux-x86_64-iritkatriel-dicts-3.14.0a6+-bf2d1dd |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 67.5 ms                                                                | 66.5 ms: 1.01x faster                                        |
| nbody          | 93.2 ms                                                                | 92.5 ms: 1.01x faster                                        |
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x slower                                         |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250407-linux-x86_64-python-f0dcb29d3affbbe1ec25-3.14.0a6+-f0dcb29 | bm-20250410-linux-x86_64-iritkatriel-dicts-3.14.0a6+-bf2d1dd |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 124 ms                                                                 | 123 ms: 1.01x faster                                         |
| regex_dna      | 214 ms                                                                 | 216 ms: 1.01x slower                                         |
| regex_effbot   | 3.26 ms                                                                | 3.38 ms: 1.04x slower                                        |
| regex_v8       | 21.6 ms                                                                | 22.6 ms: 1.05x slower                                        |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250407-linux-x86_64-python-f0dcb29d3affbbe1ec25-3.14.0a6+-f0dcb29 | bm-20250410-linux-x86_64-iritkatriel-dicts-3.14.0a6+-bf2d1dd |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| xml_etree_process    | 58.6 ms                                                                | 58.0 ms: 1.01x faster                                        |
| xml_etree_generate   | 84.3 ms                                                                | 83.5 ms: 1.01x faster                                        |
| unpickle_pure_python | 215 us                                                                 | 214 us: 1.01x faster                                         |
| pickle_pure_python   | 313 us                                                                 | 311 us: 1.01x faster                                         |
| xml_etree_parse      | 140 ms                                                                 | 141 ms: 1.01x slower                                         |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                 |

Benchmark hidden because not significant (4): tomli_loads, json_loads, xml_etree_iterparse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250407-linux-x86_64-python-f0dcb29d3affbbe1ec25-3.14.0a6+-f0dcb29 | bm-20250410-linux-x86_64-iritkatriel-dicts-3.14.0a6+-bf2d1dd |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 8.21 ms                                                                | 8.18 ms: 1.00x faster                                        |
| python_startup         | 13.2 ms                                                                | 13.2 ms: 1.00x faster                                        |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250407-linux-x86_64-python-f0dcb29d3affbbe1ec25-3.14.0a6+-f0dcb29 | bm-20250410-linux-x86_64-iritkatriel-dicts-3.14.0a6+-bf2d1dd |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 31.9 ms                                                                | 31.2 ms: 1.02x faster                                        |
| mako            | 11.2 ms                                                                | 11.0 ms: 1.02x faster                                        |
| genshi_xml      | 49.8 ms                                                                | 49.1 ms: 1.01x faster                                        |
| genshi_text     | 20.7 ms                                                                | 21.4 ms: 1.03x slower                                        |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20250407-linux-x86_64-python-f0dcb29d3affbbe1ec25-3.14.0a6+-f0dcb29 | bm-20250410-linux-x86_64-iritkatriel-dicts-3.14.0a6+-bf2d1dd |
|--------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------:|
| logging_silent           | 97.3 ns                                                                | 90.8 ns: 1.07x faster                                        |
| coroutines               | 24.4 ms                                                                | 23.1 ms: 1.06x faster                                        |
| scimark_monte_carlo      | 66.8 ms                                                                | 63.3 ms: 1.06x faster                                        |
| go                       | 111 ms                                                                 | 106 ms: 1.05x faster                                         |
| scimark_sor              | 120 ms                                                                 | 114 ms: 1.05x faster                                         |
| bpe_tokeniser            | 4.54 sec                                                               | 4.37 sec: 1.04x faster                                       |
| scimark_sparse_mat_mult  | 4.77 ms                                                                | 4.61 ms: 1.03x faster                                        |
| comprehensions           | 16.9 us                                                                | 16.4 us: 1.03x faster                                        |
| deltablue                | 3.37 ms                                                                | 3.26 ms: 1.03x faster                                        |
| pyflate                  | 442 ms                                                                 | 430 ms: 1.03x faster                                         |
| mdp                      | 1.24 sec                                                               | 1.21 sec: 1.03x faster                                       |
| nqueens                  | 81.4 ms                                                                | 79.5 ms: 1.02x faster                                        |
| django_template          | 31.9 ms                                                                | 31.2 ms: 1.02x faster                                        |
| sympy_sum                | 150 ms                                                                 | 146 ms: 1.02x faster                                         |
| sympy_str                | 268 ms                                                                 | 263 ms: 1.02x faster                                         |
| spectral_norm            | 101 ms                                                                 | 98.8 ms: 1.02x faster                                        |
| sympy_expand             | 458 ms                                                                 | 448 ms: 1.02x faster                                         |
| richards                 | 43.1 ms                                                                | 42.2 ms: 1.02x faster                                        |
| fannkuch                 | 411 ms                                                                 | 403 ms: 1.02x faster                                         |
| raytrace                 | 260 ms                                                                 | 255 ms: 1.02x faster                                         |
| coverage                 | 86.3 ms                                                                | 84.7 ms: 1.02x faster                                        |
| hexiom                   | 6.14 ms                                                                | 6.03 ms: 1.02x faster                                        |
| crypto_pyaes             | 72.9 ms                                                                | 71.6 ms: 1.02x faster                                        |
| mako                     | 11.2 ms                                                                | 11.0 ms: 1.02x faster                                        |
| chaos                    | 55.8 ms                                                                | 54.9 ms: 1.02x faster                                        |
| sympy_integrate          | 19.1 ms                                                                | 18.8 ms: 1.02x faster                                        |
| richards_super           | 49.1 ms                                                                | 48.4 ms: 1.01x faster                                        |
| float                    | 67.5 ms                                                                | 66.5 ms: 1.01x faster                                        |
| meteor_contest           | 106 ms                                                                 | 105 ms: 1.01x faster                                         |
| genshi_xml               | 49.8 ms                                                                | 49.1 ms: 1.01x faster                                        |
| sqlglot_v2_parse         | 1.23 ms                                                                | 1.21 ms: 1.01x faster                                        |
| scimark_fft              | 342 ms                                                                 | 338 ms: 1.01x faster                                         |
| xml_etree_process        | 58.6 ms                                                                | 58.0 ms: 1.01x faster                                        |
| sqlglot_v2_transpile     | 1.53 ms                                                                | 1.52 ms: 1.01x faster                                        |
| sqlite_synth             | 2.81 us                                                                | 2.78 us: 1.01x faster                                        |
| xml_etree_generate       | 84.3 ms                                                                | 83.5 ms: 1.01x faster                                        |
| logging_format           | 6.08 us                                                                | 6.03 us: 1.01x faster                                        |
| async_tree_cpu_io_mixed  | 478 ms                                                                 | 474 ms: 1.01x faster                                         |
| unpickle_pure_python     | 215 us                                                                 | 214 us: 1.01x faster                                         |
| nbody                    | 93.2 ms                                                                | 92.5 ms: 1.01x faster                                        |
| async_tree_memoization   | 310 ms                                                                 | 308 ms: 1.01x faster                                         |
| 2to3                     | 251 ms                                                                 | 249 ms: 1.01x faster                                         |
| pickle_pure_python       | 313 us                                                                 | 311 us: 1.01x faster                                         |
| pprint_pformat           | 1.47 sec                                                               | 1.46 sec: 1.01x faster                                       |
| bench_thread_pool        | 879 us                                                                 | 874 us: 1.01x faster                                         |
| regex_compile            | 124 ms                                                                 | 123 ms: 1.01x faster                                         |
| pprint_safe_repr         | 718 ms                                                                 | 714 ms: 1.01x faster                                         |
| deepcopy_memo            | 28.8 us                                                                | 28.6 us: 1.01x faster                                        |
| sqlglot_v2_normalize     | 105 ms                                                                 | 104 ms: 1.01x faster                                         |
| sqlalchemy_declarative   | 131 ms                                                                 | 131 ms: 1.00x faster                                         |
| deepcopy                 | 247 us                                                                 | 246 us: 1.00x faster                                         |
| python_startup_no_site   | 8.21 ms                                                                | 8.18 ms: 1.00x faster                                        |
| sqlglot_v2_optimize      | 51.9 ms                                                                | 51.7 ms: 1.00x faster                                        |
| python_startup           | 13.2 ms                                                                | 13.2 ms: 1.00x faster                                        |
| pidigits                 | 186 ms                                                                 | 186 ms: 1.00x slower                                         |
| shortest_path            | 489 ms                                                                 | 491 ms: 1.01x slower                                         |
| docutils                 | 2.58 sec                                                               | 2.59 sec: 1.01x slower                                       |
| xml_etree_parse          | 140 ms                                                                 | 141 ms: 1.01x slower                                         |
| regex_dna                | 214 ms                                                                 | 216 ms: 1.01x slower                                         |
| html5lib                 | 60.5 ms                                                                | 61.3 ms: 1.01x slower                                        |
| async_generators         | 388 ms                                                                 | 394 ms: 1.02x slower                                         |
| typing_runtime_protocols | 164 us                                                                 | 167 us: 1.02x slower                                         |
| generators               | 29.5 ms                                                                | 30.3 ms: 1.02x slower                                        |
| pathlib                  | 16.5 ms                                                                | 16.9 ms: 1.02x slower                                        |
| json                     | 5.37 ms                                                                | 5.52 ms: 1.03x slower                                        |
| genshi_text              | 20.7 ms                                                                | 21.4 ms: 1.03x slower                                        |
| regex_effbot             | 3.26 ms                                                                | 3.38 ms: 1.04x slower                                        |
| regex_v8                 | 21.6 ms                                                                | 22.6 ms: 1.05x slower                                        |
| gc_traversal             | 4.73 ms                                                                | 4.96 ms: 1.05x slower                                        |
| Geometric mean           | (ref)                                                                  | 1.01x faster                                                 |

Benchmark hidden because not significant (26): k_core, deepcopy_reduce, connected_components, async_tree_io, telco, async_tree_none, pylint, asyncio_websockets, sqlalchemy_imperative, scimark_lu, tomli_loads, create_gc_cycles, json_loads, async_tree_memoization_tg, dulwich_log, many_optionals, bench_mp_pool, async_tree_cpu_io_mixed_tg, xml_etree_iterparse, json_dumps, logging_simple, async_tree_io_tg, async_tree_none_tg, subparsers, sphinx, pycparser

- Geometric mean (including insignificant results): 1.007x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x