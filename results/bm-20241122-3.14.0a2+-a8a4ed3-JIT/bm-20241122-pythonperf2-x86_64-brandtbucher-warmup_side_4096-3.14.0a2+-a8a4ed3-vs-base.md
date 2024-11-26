# Results vs. base

- fork: brandtbucher
- ref: warmup_side_4096
- machine: linux-x86_64
- commit hash: a8a4ed3
- commit date: 2024-11-22
- overall geometric mean: 1.004x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241122-pythonperf2-x86_64-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-pythonperf2-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 296 ms                                                                       | 292 ms: 1.01x faster                                                           |
| docutils       | 3.09 sec                                                                     | 3.04 sec: 1.02x faster                                                         |
| html5lib       | 72.7 ms                                                                      | 72.1 ms: 1.01x faster                                                          |
| sphinx         | 1.19 sec                                                                     | 1.18 sec: 1.02x faster                                                         |
| Geometric mean | (ref)                                                                        | 1.01x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20241122-pythonperf2-x86_64-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-pythonperf2-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|--------------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_websockets | 390 ms                                                                       | 386 ms: 1.01x faster                                                           |
| coroutines         | 21.1 ms                                                                      | 21.5 ms: 1.02x slower                                                          |
| Geometric mean     | (ref)                                                                        | 1.00x faster                                                                   |

Benchmark hidden because not significant (9): async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_memoization, async_tree_io, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_none, async_generators, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241122-pythonperf2-x86_64-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-pythonperf2-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 81.2 ms                                                                      | 79.9 ms: 1.02x faster                                                          |
| pidigits       | 252 ms                                                                       | 251 ms: 1.00x faster                                                           |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                                   |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241122-pythonperf2-x86_64-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-pythonperf2-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 142 ms                                                                       | 143 ms: 1.01x slower                                                           |
| regex_effbot   | 3.29 ms                                                                      | 3.34 ms: 1.02x slower                                                          |
| regex_v8       | 24.9 ms                                                                      | 25.6 ms: 1.03x slower                                                          |
| regex_dna      | 242 ms                                                                       | 253 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                                        | 1.02x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark         | bm-20241122-pythonperf2-x86_64-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-pythonperf2-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|-------------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse   | 147 ms                                                                       | 144 ms: 1.02x faster                                                           |
| xml_etree_process | 58.1 ms                                                                      | 57.4 ms: 1.01x faster                                                          |
| json_loads        | 25.4 us                                                                      | 25.2 us: 1.01x faster                                                          |
| json_dumps        | 11.3 ms                                                                      | 11.4 ms: 1.01x slower                                                          |
| tomli_loads       | 2.15 sec                                                                     | 2.21 sec: 1.03x slower                                                         |
| Geometric mean    | (ref)                                                                        | 1.00x slower                                                                   |

Benchmark hidden because not significant (4): xml_etree_generate, xml_etree_iterparse, unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241122-pythonperf2-x86_64-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-pythonperf2-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|-----------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.45 ms                                                                      | 9.42 ms: 1.00x faster                                                          |
| genshi_xml      | 62.0 ms                                                                      | 63.7 ms: 1.03x slower                                                          |
| django_template | 39.2 ms                                                                      | 40.8 ms: 1.04x slower                                                          |
| genshi_text     | 28.1 ms                                                                      | 29.4 ms: 1.04x slower                                                          |
| Geometric mean  | (ref)                                                                        | 1.03x slower                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20241122-pythonperf2-x86_64-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-pythonperf2-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|--------------------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| scimark_sor              | 109 ms                                                                       | 102 ms: 1.07x faster                                                           |
| logging_silent           | 98.0 ns                                                                      | 93.6 ns: 1.05x faster                                                          |
| scimark_fft              | 316 ms                                                                       | 303 ms: 1.04x faster                                                           |
| coverage                 | 82.9 ms                                                                      | 79.6 ms: 1.04x faster                                                          |
| scimark_sparse_mat_mult  | 5.06 ms                                                                      | 4.87 ms: 1.04x faster                                                          |
| scimark_lu               | 98.2 ms                                                                      | 94.5 ms: 1.04x faster                                                          |
| scimark_monte_carlo      | 69.8 ms                                                                      | 67.4 ms: 1.04x faster                                                          |
| bpe_tokeniser            | 5.00 sec                                                                     | 4.85 sec: 1.03x faster                                                         |
| pylint                   | 332 ms                                                                       | 323 ms: 1.03x faster                                                           |
| fannkuch                 | 395 ms                                                                       | 384 ms: 1.03x faster                                                           |
| richards                 | 44.9 ms                                                                      | 43.8 ms: 1.02x faster                                                          |
| sqlglot_parse            | 1.52 ms                                                                      | 1.48 ms: 1.02x faster                                                          |
| sqlglot_transpile        | 1.92 ms                                                                      | 1.87 ms: 1.02x faster                                                          |
| sqlglot_normalize        | 129 ms                                                                       | 126 ms: 1.02x faster                                                           |
| hexiom                   | 7.28 ms                                                                      | 7.12 ms: 1.02x faster                                                          |
| crypto_pyaes             | 74.6 ms                                                                      | 72.9 ms: 1.02x faster                                                          |
| pprint_safe_repr         | 815 ms                                                                       | 798 ms: 1.02x faster                                                           |
| comprehensions           | 20.0 us                                                                      | 19.6 us: 1.02x faster                                                          |
| connected_components     | 410 ms                                                                       | 402 ms: 1.02x faster                                                           |
| xml_etree_parse          | 147 ms                                                                       | 144 ms: 1.02x faster                                                           |
| docutils                 | 3.09 sec                                                                     | 3.04 sec: 1.02x faster                                                         |
| float                    | 81.2 ms                                                                      | 79.9 ms: 1.02x faster                                                          |
| deepcopy_memo            | 29.6 us                                                                      | 29.1 us: 1.02x faster                                                          |
| chaos                    | 67.4 ms                                                                      | 66.3 ms: 1.02x faster                                                          |
| sphinx                   | 1.19 sec                                                                     | 1.18 sec: 1.02x faster                                                         |
| raytrace                 | 327 ms                                                                       | 322 ms: 1.02x faster                                                           |
| sqlglot_optimize         | 63.9 ms                                                                      | 63.0 ms: 1.01x faster                                                          |
| 2to3                     | 296 ms                                                                       | 292 ms: 1.01x faster                                                           |
| xml_etree_process        | 58.1 ms                                                                      | 57.4 ms: 1.01x faster                                                          |
| richards_super           | 50.6 ms                                                                      | 50.1 ms: 1.01x faster                                                          |
| shortest_path            | 441 ms                                                                       | 436 ms: 1.01x faster                                                           |
| sympy_integrate          | 24.7 ms                                                                      | 24.4 ms: 1.01x faster                                                          |
| asyncio_websockets       | 390 ms                                                                       | 386 ms: 1.01x faster                                                           |
| sqlite_synth             | 2.83 us                                                                      | 2.80 us: 1.01x faster                                                          |
| html5lib                 | 72.7 ms                                                                      | 72.1 ms: 1.01x faster                                                          |
| deepcopy                 | 313 us                                                                       | 310 us: 1.01x faster                                                           |
| sqlalchemy_declarative   | 147 ms                                                                       | 146 ms: 1.01x faster                                                           |
| deltablue                | 3.28 ms                                                                      | 3.26 ms: 1.01x faster                                                          |
| pyflate                  | 480 ms                                                                       | 477 ms: 1.01x faster                                                           |
| pathlib                  | 16.6 ms                                                                      | 16.5 ms: 1.01x faster                                                          |
| json_loads               | 25.4 us                                                                      | 25.2 us: 1.01x faster                                                          |
| sympy_sum                | 162 ms                                                                       | 161 ms: 1.00x faster                                                           |
| mako                     | 9.45 ms                                                                      | 9.42 ms: 1.00x faster                                                          |
| pidigits                 | 252 ms                                                                       | 251 ms: 1.00x faster                                                           |
| gc_traversal             | 5.80 ms                                                                      | 5.82 ms: 1.00x slower                                                          |
| json                     | 5.13 ms                                                                      | 5.16 ms: 1.00x slower                                                          |
| nqueens                  | 101 ms                                                                       | 102 ms: 1.00x slower                                                           |
| deepcopy_reduce          | 3.01 us                                                                      | 3.03 us: 1.01x slower                                                          |
| sympy_expand             | 528 ms                                                                       | 531 ms: 1.01x slower                                                           |
| json_dumps               | 11.3 ms                                                                      | 11.4 ms: 1.01x slower                                                          |
| logging_format           | 7.29 us                                                                      | 7.36 us: 1.01x slower                                                          |
| regex_compile            | 142 ms                                                                       | 143 ms: 1.01x slower                                                           |
| meteor_contest           | 130 ms                                                                       | 131 ms: 1.01x slower                                                           |
| mdp                      | 2.58 sec                                                                     | 2.62 sec: 1.01x slower                                                         |
| regex_effbot             | 3.29 ms                                                                      | 3.34 ms: 1.02x slower                                                          |
| typing_runtime_protocols | 183 us                                                                       | 186 us: 1.02x slower                                                           |
| coroutines               | 21.1 ms                                                                      | 21.5 ms: 1.02x slower                                                          |
| logging_simple           | 6.65 us                                                                      | 6.77 us: 1.02x slower                                                          |
| genshi_xml               | 62.0 ms                                                                      | 63.7 ms: 1.03x slower                                                          |
| regex_v8                 | 24.9 ms                                                                      | 25.6 ms: 1.03x slower                                                          |
| tomli_loads              | 2.15 sec                                                                     | 2.21 sec: 1.03x slower                                                         |
| dulwich_log              | 65.3 ms                                                                      | 67.8 ms: 1.04x slower                                                          |
| django_template          | 39.2 ms                                                                      | 40.8 ms: 1.04x slower                                                          |
| genshi_text              | 28.1 ms                                                                      | 29.4 ms: 1.04x slower                                                          |
| regex_dna                | 242 ms                                                                       | 253 ms: 1.05x slower                                                           |
| generators               | 39.9 ms                                                                      | 42.9 ms: 1.07x slower                                                          |
| Geometric mean           | (ref)                                                                        | 1.00x faster                                                                   |

Benchmark hidden because not significant (31): spectral_norm, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_memoization, async_tree_io, k_core, telco, bench_thread_pool, xml_etree_generate, async_tree_cpu_io_mixed, async_tree_none_tg, pycparser, sympy_str, async_tree_none, go, djangocms, subparsers, python_startup, python_startup_no_site, sqlalchemy_imperative, xml_etree_iterparse, thrift, async_generators, many_optionals, unpickle_pure_python, create_gc_cycles, async_tree_io_tg, pprint_pformat, nbody, pickle_pure_python, bench_mp_pool

- Geometric mean (including insignificant results): 1.004x faster
# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x