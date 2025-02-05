# Results vs. base

- fork: brandtbucher
- ref: no_generators_alt_al
- machine: linux-x86_64
- commit hash: c28475f
- commit date: 2025-02-04
- overall geometric mean: 1.004x faster
- HPT reliability: 52.02%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-c28475f |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 261 ms                                                                 | 258 ms: 1.01x faster                                                         |
| docutils       | 2.67 sec                                                               | 2.69 sec: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-c28475f |
|------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_generators | 411 ms                                                                 | 405 ms: 1.01x faster                                                         |
| coroutines       | 23.0 ms                                                                | 23.9 ms: 1.04x slower                                                        |
| Geometric mean   | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (9): async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_none_tg, async_tree_io, async_tree_memoization, async_tree_none, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-c28475f |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-c28475f |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 130 ms                                                                 | 128 ms: 1.01x faster                                                         |
| regex_dna      | 211 ms                                                                 | 212 ms: 1.00x slower                                                         |
| regex_effbot   | 3.18 ms                                                                | 3.31 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-c28475f |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 200 us                                                                 | 201 us: 1.00x slower                                                         |
| xml_etree_generate   | 78.0 ms                                                                | 78.6 ms: 1.01x slower                                                        |
| xml_etree_parse      | 138 ms                                                                 | 139 ms: 1.01x slower                                                         |
| xml_etree_process    | 54.6 ms                                                                | 55.3 ms: 1.01x slower                                                        |
| json_dumps           | 11.1 ms                                                                | 11.3 ms: 1.01x slower                                                        |
| json_loads           | 28.9 us                                                                | 29.4 us: 1.02x slower                                                        |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (3): pickle_pure_python, xml_etree_iterparse, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-c28475f |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 12.9 ms                                                                | 12.8 ms: 1.00x faster                                                        |
| python_startup_no_site | 7.06 ms                                                                | 7.07 ms: 1.00x slower                                                        |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-c28475f |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml     | 57.7 ms                                                                | 49.2 ms: 1.17x faster                                                        |
| genshi_text    | 23.0 ms                                                                | 21.4 ms: 1.08x faster                                                        |
| mako           | 10.3 ms                                                                | 10.1 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                                  | 1.06x faster                                                                 |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-c28475f |
|--------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators               | 37.5 ms                                                                | 28.9 ms: 1.30x faster                                                        |
| genshi_xml               | 57.7 ms                                                                | 49.2 ms: 1.17x faster                                                        |
| genshi_text              | 23.0 ms                                                                | 21.4 ms: 1.08x faster                                                        |
| pyflate                  | 463 ms                                                                 | 448 ms: 1.03x faster                                                         |
| scimark_monte_carlo      | 63.9 ms                                                                | 62.6 ms: 1.02x faster                                                        |
| dulwich_log              | 66.8 ms                                                                | 65.6 ms: 1.02x faster                                                        |
| crypto_pyaes             | 71.3 ms                                                                | 70.0 ms: 1.02x faster                                                        |
| mako                     | 10.3 ms                                                                | 10.1 ms: 1.02x faster                                                        |
| go                       | 128 ms                                                                 | 126 ms: 1.02x faster                                                         |
| scimark_fft              | 314 ms                                                                 | 309 ms: 1.02x faster                                                         |
| sqlglot_normalize        | 108 ms                                                                 | 106 ms: 1.02x faster                                                         |
| regex_compile            | 130 ms                                                                 | 128 ms: 1.01x faster                                                         |
| async_generators         | 411 ms                                                                 | 405 ms: 1.01x faster                                                         |
| subparsers               | 20.7 ms                                                                | 20.5 ms: 1.01x faster                                                        |
| 2to3                     | 261 ms                                                                 | 258 ms: 1.01x faster                                                         |
| fannkuch                 | 392 ms                                                                 | 388 ms: 1.01x faster                                                         |
| sqlglot_optimize         | 54.1 ms                                                                | 53.6 ms: 1.01x faster                                                        |
| hexiom                   | 7.46 ms                                                                | 7.39 ms: 1.01x faster                                                        |
| scimark_sor              | 114 ms                                                                 | 113 ms: 1.01x faster                                                         |
| bench_thread_pool        | 894 us                                                                 | 887 us: 1.01x faster                                                         |
| typing_runtime_protocols | 165 us                                                                 | 164 us: 1.01x faster                                                         |
| connected_components     | 440 ms                                                                 | 437 ms: 1.01x faster                                                         |
| shortest_path            | 481 ms                                                                 | 478 ms: 1.01x faster                                                         |
| thrift                   | 771 us                                                                 | 766 us: 1.01x faster                                                         |
| sqlalchemy_declarative   | 131 ms                                                                 | 130 ms: 1.01x faster                                                         |
| pidigits                 | 186 ms                                                                 | 186 ms: 1.00x faster                                                         |
| meteor_contest           | 108 ms                                                                 | 108 ms: 1.00x faster                                                         |
| python_startup           | 12.9 ms                                                                | 12.8 ms: 1.00x faster                                                        |
| python_startup_no_site   | 7.06 ms                                                                | 7.07 ms: 1.00x slower                                                        |
| regex_dna                | 211 ms                                                                 | 212 ms: 1.00x slower                                                         |
| sympy_expand             | 470 ms                                                                 | 472 ms: 1.00x slower                                                         |
| unpickle_pure_python     | 200 us                                                                 | 201 us: 1.00x slower                                                         |
| docutils                 | 2.67 sec                                                               | 2.69 sec: 1.01x slower                                                       |
| sqlglot_parse            | 1.28 ms                                                                | 1.28 ms: 1.01x slower                                                        |
| mdp                      | 2.54 sec                                                               | 2.56 sec: 1.01x slower                                                       |
| deltablue                | 3.49 ms                                                                | 3.52 ms: 1.01x slower                                                        |
| xml_etree_generate       | 78.0 ms                                                                | 78.6 ms: 1.01x slower                                                        |
| pathlib                  | 16.1 ms                                                                | 16.2 ms: 1.01x slower                                                        |
| create_gc_cycles         | 2.45 ms                                                                | 2.47 ms: 1.01x slower                                                        |
| coverage                 | 89.7 ms                                                                | 90.6 ms: 1.01x slower                                                        |
| scimark_lu               | 113 ms                                                                 | 114 ms: 1.01x slower                                                         |
| spectral_norm            | 95.6 ms                                                                | 96.5 ms: 1.01x slower                                                        |
| sqlglot_transpile        | 1.58 ms                                                                | 1.60 ms: 1.01x slower                                                        |
| xml_etree_parse          | 138 ms                                                                 | 139 ms: 1.01x slower                                                         |
| deepcopy_memo            | 30.2 us                                                                | 30.6 us: 1.01x slower                                                        |
| pprint_safe_repr         | 728 ms                                                                 | 738 ms: 1.01x slower                                                         |
| xml_etree_process        | 54.6 ms                                                                | 55.3 ms: 1.01x slower                                                        |
| json_dumps               | 11.1 ms                                                                | 11.3 ms: 1.01x slower                                                        |
| deepcopy_reduce          | 2.73 us                                                                | 2.78 us: 1.02x slower                                                        |
| json_loads               | 28.9 us                                                                | 29.4 us: 1.02x slower                                                        |
| deepcopy                 | 265 us                                                                 | 270 us: 1.02x slower                                                         |
| logging_format           | 6.17 us                                                                | 6.35 us: 1.03x slower                                                        |
| logging_silent           | 108 ns                                                                 | 111 ns: 1.03x slower                                                         |
| coroutines               | 23.0 ms                                                                | 23.9 ms: 1.04x slower                                                        |
| logging_simple           | 5.63 us                                                                | 5.85 us: 1.04x slower                                                        |
| regex_effbot             | 3.18 ms                                                                | 3.31 ms: 1.04x slower                                                        |
| gc_traversal             | 4.77 ms                                                                | 5.04 ms: 1.06x slower                                                        |
| Geometric mean           | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (39): pylint, raytrace, scimark_sparse_mat_mult, sphinx, pickle_pure_python, chaos, bench_mp_pool, comprehensions, sqlalchemy_imperative, many_optionals, regex_v8, k_core, xml_etree_iterparse, async_tree_cpu_io_mixed_tg, sympy_str, pprint_pformat, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_none_tg, float, async_tree_io, sqlite_synth, sympy_sum, nbody, html5lib, bpe_tokeniser, nqueens, tomli_loads, sympy_integrate, async_tree_memoization, django_template, async_tree_none, richards, async_tree_io_tg, richards_super, telco, json, pycparser

- Geometric mean (including insignificant results): 1.004x faster

# HPT report

- Reliability score: 52.02% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x