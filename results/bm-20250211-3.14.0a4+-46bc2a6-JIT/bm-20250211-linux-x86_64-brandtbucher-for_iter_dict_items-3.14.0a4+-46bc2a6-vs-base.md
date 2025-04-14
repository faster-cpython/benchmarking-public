# Results vs. base

- fork: brandtbucher
- ref: for_iter_dict_items
- machine: linux-x86_64
- commit hash: 46bc2a6
- commit date: 2025-02-11
- overall geometric mean: 1.001x slower
- HPT reliability: 61.49%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250209-linux-x86_64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-46bc2a6 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 258 ms                                                                 | 258 ms: 1.00x faster                                                        |
| html5lib       | 60.8 ms                                                                | 61.8 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20250209-linux-x86_64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-46bc2a6 |
|------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| coroutines       | 23.6 ms                                                                | 22.7 ms: 1.04x faster                                                       |
| async_tree_io_tg | 632 ms                                                                 | 613 ms: 1.03x faster                                                        |
| Geometric mean   | (ref)                                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (9): async_tree_io, async_tree_memoization_tg, async_tree_none, async_tree_memoization, async_tree_none_tg, asyncio_websockets, async_generators, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250209-linux-x86_64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-46bc2a6 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 70.8 ms                                                                | 69.1 ms: 1.02x faster                                                       |
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x slower                                                        |
| nbody          | 95.5 ms                                                                | 96.8 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250209-linux-x86_64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-46bc2a6 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                                | 23.8 ms: 1.00x faster                                                       |
| regex_dna      | 206 ms                                                                 | 207 ms: 1.01x slower                                                        |
| regex_effbot   | 3.18 ms                                                                | 3.20 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250209-linux-x86_64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-46bc2a6 |
|---------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads         | 1.85 sec                                                               | 1.82 sec: 1.01x faster                                                      |
| xml_etree_iterparse | 95.4 ms                                                                | 95.9 ms: 1.00x slower                                                       |
| xml_etree_parse     | 137 ms                                                                 | 139 ms: 1.01x slower                                                        |
| Geometric mean      | (ref)                                                                  | 1.00x faster                                                                |

Benchmark hidden because not significant (6): unpickle_pure_python, xml_etree_process, xml_etree_generate, json_loads, pickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250209-linux-x86_64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-46bc2a6 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.05 ms                                                                | 7.04 ms: 1.00x faster                                                       |
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                                       |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250209-linux-x86_64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-46bc2a6 |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.88 ms                                                                | 10.0 ms: 1.02x slower                                                       |
| django_template | 31.8 ms                                                                | 32.5 ms: 1.02x slower                                                       |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                                |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20250209-linux-x86_64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-46bc2a6 |
|--------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| logging_format           | 6.33 us                                                                | 6.00 us: 1.05x faster                                                       |
| logging_simple           | 5.69 us                                                                | 5.47 us: 1.04x faster                                                       |
| coroutines               | 23.6 ms                                                                | 22.7 ms: 1.04x faster                                                       |
| spectral_norm            | 94.4 ms                                                                | 90.9 ms: 1.04x faster                                                       |
| async_tree_io_tg         | 632 ms                                                                 | 613 ms: 1.03x faster                                                        |
| float                    | 70.8 ms                                                                | 69.1 ms: 1.02x faster                                                       |
| nqueens                  | 90.7 ms                                                                | 89.2 ms: 1.02x faster                                                       |
| richards_super           | 50.9 ms                                                                | 50.1 ms: 1.02x faster                                                       |
| tomli_loads              | 1.85 sec                                                               | 1.82 sec: 1.01x faster                                                      |
| thrift                   | 773 us                                                                 | 763 us: 1.01x faster                                                        |
| json                     | 5.20 ms                                                                | 5.14 ms: 1.01x faster                                                       |
| scimark_lu               | 115 ms                                                                 | 113 ms: 1.01x faster                                                        |
| pyflate                  | 444 ms                                                                 | 441 ms: 1.01x faster                                                        |
| logging_silent           | 106 ns                                                                 | 106 ns: 1.01x faster                                                        |
| richards                 | 44.4 ms                                                                | 44.1 ms: 1.01x faster                                                       |
| many_optionals           | 957 us                                                                 | 953 us: 1.00x faster                                                        |
| chaos                    | 58.6 ms                                                                | 58.3 ms: 1.00x faster                                                       |
| shortest_path            | 482 ms                                                                 | 481 ms: 1.00x faster                                                        |
| connected_components     | 439 ms                                                                 | 437 ms: 1.00x faster                                                        |
| 2to3                     | 258 ms                                                                 | 258 ms: 1.00x faster                                                        |
| regex_v8                 | 23.8 ms                                                                | 23.8 ms: 1.00x faster                                                       |
| mdp                      | 2.57 sec                                                               | 2.56 sec: 1.00x faster                                                      |
| python_startup_no_site   | 7.05 ms                                                                | 7.04 ms: 1.00x faster                                                       |
| python_startup           | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                                       |
| pidigits                 | 186 ms                                                                 | 186 ms: 1.00x slower                                                        |
| sqlalchemy_declarative   | 130 ms                                                                 | 131 ms: 1.00x slower                                                        |
| meteor_contest           | 107 ms                                                                 | 108 ms: 1.00x slower                                                        |
| sympy_integrate          | 20.2 ms                                                                | 20.3 ms: 1.00x slower                                                       |
| xml_etree_iterparse      | 95.4 ms                                                                | 95.9 ms: 1.00x slower                                                       |
| regex_dna                | 206 ms                                                                 | 207 ms: 1.01x slower                                                        |
| regex_effbot             | 3.18 ms                                                                | 3.20 ms: 1.01x slower                                                       |
| sqlite_synth             | 2.70 us                                                                | 2.72 us: 1.01x slower                                                       |
| raytrace                 | 274 ms                                                                 | 277 ms: 1.01x slower                                                        |
| deltablue                | 3.34 ms                                                                | 3.38 ms: 1.01x slower                                                       |
| hexiom                   | 6.84 ms                                                                | 6.93 ms: 1.01x slower                                                       |
| xml_etree_parse          | 137 ms                                                                 | 139 ms: 1.01x slower                                                        |
| typing_runtime_protocols | 161 us                                                                 | 163 us: 1.01x slower                                                        |
| nbody                    | 95.5 ms                                                                | 96.8 ms: 1.01x slower                                                       |
| scimark_sparse_mat_mult  | 4.46 ms                                                                | 4.52 ms: 1.01x slower                                                       |
| deepcopy                 | 257 us                                                                 | 260 us: 1.01x slower                                                        |
| html5lib                 | 60.8 ms                                                                | 61.8 ms: 1.02x slower                                                       |
| mako                     | 9.88 ms                                                                | 10.0 ms: 1.02x slower                                                       |
| go                       | 129 ms                                                                 | 131 ms: 1.02x slower                                                        |
| sympy_str                | 275 ms                                                                 | 280 ms: 1.02x slower                                                        |
| sqlglot_transpile        | 1.58 ms                                                                | 1.61 ms: 1.02x slower                                                       |
| django_template          | 31.8 ms                                                                | 32.5 ms: 1.02x slower                                                       |
| gc_traversal             | 4.80 ms                                                                | 4.94 ms: 1.03x slower                                                       |
| sympy_expand             | 468 ms                                                                 | 481 ms: 1.03x slower                                                        |
| sqlglot_parse            | 1.28 ms                                                                | 1.31 ms: 1.03x slower                                                       |
| deepcopy_reduce          | 2.66 us                                                                | 2.74 us: 1.03x slower                                                       |
| deepcopy_memo            | 29.9 us                                                                | 30.8 us: 1.03x slower                                                       |
| sqlglot_normalize        | 106 ms                                                                 | 109 ms: 1.03x slower                                                        |
| sqlglot_optimize         | 53.4 ms                                                                | 55.2 ms: 1.03x slower                                                       |
| sympy_sum                | 151 ms                                                                 | 156 ms: 1.04x slower                                                        |
| Geometric mean           | (ref)                                                                  | 1.00x slower                                                                |

Benchmark hidden because not significant (42): unpickle_pure_python, async_tree_io, async_tree_memoization_tg, pprint_pformat, async_tree_none, crypto_pyaes, generators, async_tree_memoization, subparsers, async_tree_none_tg, scimark_fft, xml_etree_process, pylint, bench_thread_pool, xml_etree_generate, asyncio_websockets, dulwich_log, coverage, bpe_tokeniser, comprehensions, regex_compile, genshi_text, pycparser, create_gc_cycles, sphinx, async_generators, pathlib, scimark_sor, docutils, async_tree_cpu_io_mixed, bench_mp_pool, fannkuch, genshi_xml, json_loads, async_tree_cpu_io_mixed_tg, scimark_monte_carlo, sqlalchemy_imperative, pickle_pure_python, telco, json_dumps, pprint_safe_repr, k_core

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 61.49% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x