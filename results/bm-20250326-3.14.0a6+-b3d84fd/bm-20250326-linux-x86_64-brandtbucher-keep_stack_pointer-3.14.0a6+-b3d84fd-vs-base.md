# Results vs. base

- fork: brandtbucher
- ref: keep_stack_pointer
- machine: linux-x86_64
- commit hash: b3d84fd
- commit date: 2025-03-26
- overall geometric mean: 1.005x slower
- HPT reliability: 91.72%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250326-linux-x86_64-python-4b3d5b604210f68005ef-3.14.0a6+-4b3d5b6 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 256 ms                                                                 | 258 ms: 1.01x slower                                                       |
| docutils       | 2.58 sec                                                               | 2.63 sec: 1.02x slower                                                     |
| sphinx         | 1.00 sec                                                               | 1.03 sec: 1.02x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250326-linux-x86_64-python-4b3d5b604210f68005ef-3.14.0a6+-4b3d5b6 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 475 ms                                                                 | 469 ms: 1.01x faster                                                       |
| async_tree_cpu_io_mixed    | 491 ms                                                                 | 485 ms: 1.01x faster                                                       |
| async_generators           | 390 ms                                                                 | 395 ms: 1.01x slower                                                       |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (8): async_tree_io, asyncio_websockets, coroutines, async_tree_memoization, async_tree_none, async_tree_memoization_tg, async_tree_none_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250326-linux-x86_64-python-4b3d5b604210f68005ef-3.14.0a6+-4b3d5b6 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 98.6 ms                                                                | 97.6 ms: 1.01x faster                                                      |
| float          | 69.1 ms                                                                | 69.9 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250326-linux-x86_64-python-4b3d5b604210f68005ef-3.14.0a6+-4b3d5b6 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 126 ms                                                                 | 127 ms: 1.01x slower                                                       |
| regex_dna      | 220 ms                                                                 | 225 ms: 1.02x slower                                                       |
| regex_effbot   | 3.21 ms                                                                | 3.31 ms: 1.03x slower                                                      |
| regex_v8       | 22.5 ms                                                                | 23.8 ms: 1.06x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250326-linux-x86_64-python-4b3d5b604210f68005ef-3.14.0a6+-4b3d5b6 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.96 sec                                                               | 1.94 sec: 1.01x faster                                                     |
| xml_etree_parse      | 142 ms                                                                 | 141 ms: 1.01x faster                                                       |
| json_loads           | 30.0 us                                                                | 29.9 us: 1.01x faster                                                      |
| unpickle_pure_python | 216 us                                                                 | 217 us: 1.00x slower                                                       |
| xml_etree_process    | 59.0 ms                                                                | 59.3 ms: 1.00x slower                                                      |
| xml_etree_generate   | 84.5 ms                                                                | 84.9 ms: 1.01x slower                                                      |
| xml_etree_iterparse  | 98.7 ms                                                                | 99.4 ms: 1.01x slower                                                      |
| json_dumps           | 11.3 ms                                                                | 11.6 ms: 1.02x slower                                                      |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250326-linux-x86_64-python-4b3d5b604210f68005ef-3.14.0a6+-4b3d5b6 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 8.17 ms                                                                | 8.28 ms: 1.01x slower                                                      |
| python_startup         | 13.1 ms                                                                | 13.3 ms: 1.02x slower                                                      |
| Geometric mean         | (ref)                                                                  | 1.02x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250326-linux-x86_64-python-4b3d5b604210f68005ef-3.14.0a6+-4b3d5b6 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 21.3 ms                                                                | 21.1 ms: 1.01x faster                                                      |
| django_template | 31.6 ms                                                                | 31.3 ms: 1.01x faster                                                      |
| genshi_xml      | 48.7 ms                                                                | 48.5 ms: 1.00x faster                                                      |
| mako            | 11.1 ms                                                                | 11.2 ms: 1.01x slower                                                      |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20250326-linux-x86_64-python-4b3d5b604210f68005ef-3.14.0a6+-4b3d5b6 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| gc_traversal               | 5.01 ms                                                                | 4.79 ms: 1.05x faster                                                      |
| spectral_norm              | 100 ms                                                                 | 97.6 ms: 1.03x faster                                                      |
| logging_silent             | 100 ns                                                                 | 97.5 ns: 1.03x faster                                                      |
| pyflate                    | 462 ms                                                                 | 456 ms: 1.01x faster                                                       |
| async_tree_cpu_io_mixed_tg | 475 ms                                                                 | 469 ms: 1.01x faster                                                       |
| go                         | 116 ms                                                                 | 114 ms: 1.01x faster                                                       |
| async_tree_cpu_io_mixed    | 491 ms                                                                 | 485 ms: 1.01x faster                                                       |
| nbody                      | 98.6 ms                                                                | 97.6 ms: 1.01x faster                                                      |
| genshi_text                | 21.3 ms                                                                | 21.1 ms: 1.01x faster                                                      |
| json                       | 5.35 ms                                                                | 5.30 ms: 1.01x faster                                                      |
| django_template            | 31.6 ms                                                                | 31.3 ms: 1.01x faster                                                      |
| tomli_loads                | 1.96 sec                                                               | 1.94 sec: 1.01x faster                                                     |
| pprint_safe_repr           | 729 ms                                                                 | 723 ms: 1.01x faster                                                       |
| sqlglot_v2_normalize       | 106 ms                                                                 | 105 ms: 1.01x faster                                                       |
| deepcopy_memo              | 29.2 us                                                                | 29.0 us: 1.01x faster                                                      |
| hexiom                     | 6.32 ms                                                                | 6.27 ms: 1.01x faster                                                      |
| chaos                      | 58.6 ms                                                                | 58.2 ms: 1.01x faster                                                      |
| fannkuch                   | 428 ms                                                                 | 425 ms: 1.01x faster                                                       |
| xml_etree_parse            | 142 ms                                                                 | 141 ms: 1.01x faster                                                       |
| scimark_fft                | 351 ms                                                                 | 349 ms: 1.01x faster                                                       |
| logging_simple             | 5.54 us                                                                | 5.50 us: 1.01x faster                                                      |
| crypto_pyaes               | 73.5 ms                                                                | 73.1 ms: 1.01x faster                                                      |
| json_loads                 | 30.0 us                                                                | 29.9 us: 1.01x faster                                                      |
| genshi_xml                 | 48.7 ms                                                                | 48.5 ms: 1.00x faster                                                      |
| pprint_pformat             | 1.49 sec                                                               | 1.48 sec: 1.00x faster                                                     |
| bpe_tokeniser              | 4.61 sec                                                               | 4.59 sec: 1.00x faster                                                     |
| nqueens                    | 82.5 ms                                                                | 82.3 ms: 1.00x faster                                                      |
| create_gc_cycles           | 2.46 ms                                                                | 2.46 ms: 1.00x faster                                                      |
| deltablue                  | 3.14 ms                                                                | 3.15 ms: 1.00x slower                                                      |
| raytrace                   | 264 ms                                                                 | 265 ms: 1.00x slower                                                       |
| unpickle_pure_python       | 216 us                                                                 | 217 us: 1.00x slower                                                       |
| xml_etree_process          | 59.0 ms                                                                | 59.3 ms: 1.00x slower                                                      |
| xml_etree_generate         | 84.5 ms                                                                | 84.9 ms: 1.01x slower                                                      |
| sqlglot_v2_transpile       | 1.57 ms                                                                | 1.58 ms: 1.01x slower                                                      |
| regex_compile              | 126 ms                                                                 | 127 ms: 1.01x slower                                                       |
| meteor_contest             | 107 ms                                                                 | 107 ms: 1.01x slower                                                       |
| mako                       | 11.1 ms                                                                | 11.2 ms: 1.01x slower                                                      |
| xml_etree_iterparse        | 98.7 ms                                                                | 99.4 ms: 1.01x slower                                                      |
| 2to3                       | 256 ms                                                                 | 258 ms: 1.01x slower                                                       |
| deepcopy                   | 254 us                                                                 | 257 us: 1.01x slower                                                       |
| sympy_expand               | 455 ms                                                                 | 459 ms: 1.01x slower                                                       |
| mdp                        | 2.48 sec                                                               | 2.50 sec: 1.01x slower                                                     |
| comprehensions             | 16.8 us                                                                | 17.0 us: 1.01x slower                                                      |
| async_generators           | 390 ms                                                                 | 395 ms: 1.01x slower                                                       |
| float                      | 69.1 ms                                                                | 69.9 ms: 1.01x slower                                                      |
| thrift                     | 770 us                                                                 | 779 us: 1.01x slower                                                       |
| deepcopy_reduce            | 2.66 us                                                                | 2.69 us: 1.01x slower                                                      |
| scimark_lu                 | 114 ms                                                                 | 115 ms: 1.01x slower                                                       |
| python_startup_no_site     | 8.17 ms                                                                | 8.28 ms: 1.01x slower                                                      |
| richards                   | 43.2 ms                                                                | 43.9 ms: 1.02x slower                                                      |
| scimark_sparse_mat_mult    | 4.70 ms                                                                | 4.78 ms: 1.02x slower                                                      |
| python_startup             | 13.1 ms                                                                | 13.3 ms: 1.02x slower                                                      |
| json_dumps                 | 11.3 ms                                                                | 11.6 ms: 1.02x slower                                                      |
| sqlalchemy_declarative     | 130 ms                                                                 | 132 ms: 1.02x slower                                                       |
| docutils                   | 2.58 sec                                                               | 2.63 sec: 1.02x slower                                                     |
| sqlite_synth               | 2.75 us                                                                | 2.81 us: 1.02x slower                                                      |
| bench_thread_pool          | 870 us                                                                 | 889 us: 1.02x slower                                                       |
| sphinx                     | 1.00 sec                                                               | 1.03 sec: 1.02x slower                                                     |
| sympy_str                  | 266 ms                                                                 | 272 ms: 1.02x slower                                                       |
| regex_dna                  | 220 ms                                                                 | 225 ms: 1.02x slower                                                       |
| richards_super             | 49.4 ms                                                                | 50.6 ms: 1.02x slower                                                      |
| bench_mp_pool              | 83.1 ms                                                                | 85.3 ms: 1.03x slower                                                      |
| sympy_integrate            | 19.4 ms                                                                | 20.0 ms: 1.03x slower                                                      |
| regex_effbot               | 3.21 ms                                                                | 3.31 ms: 1.03x slower                                                      |
| many_optionals             | 947 us                                                                 | 982 us: 1.04x slower                                                       |
| sympy_sum                  | 148 ms                                                                 | 155 ms: 1.05x slower                                                       |
| regex_v8                   | 22.5 ms                                                                | 23.8 ms: 1.06x slower                                                      |
| dulwich_log                | 58.5 ms                                                                | 62.3 ms: 1.06x slower                                                      |
| sqlalchemy_imperative      | 16.7 ms                                                                | 18.4 ms: 1.10x slower                                                      |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (27): typing_runtime_protocols, async_tree_io, connected_components, html5lib, shortest_path, pathlib, pidigits, sqlglot_v2_optimize, k_core, telco, asyncio_websockets, subparsers, coroutines, async_tree_memoization, sqlglot_v2_parse, pickle_pure_python, async_tree_none, scimark_sor, generators, scimark_monte_carlo, logging_format, async_tree_memoization_tg, async_tree_none_tg, async_tree_io_tg, coverage, pycparser, pylint

- Geometric mean (including insignificant results): 1.005x slower

# HPT report

- Reliability score: 91.72% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x