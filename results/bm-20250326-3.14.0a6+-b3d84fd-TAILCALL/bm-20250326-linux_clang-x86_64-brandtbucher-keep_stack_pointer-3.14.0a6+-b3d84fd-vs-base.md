# Results vs. base

- fork: brandtbucher
- ref: keep_stack_pointer
- machine: linux-x86_64
- commit hash: b3d84fd
- commit date: 2025-03-26
- overall geometric mean: 1.007x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250326-linux-x86_64-python-4b3d5b604210f68005ef-3.14.0a6+-4b3d5b6 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 252 ms                                                                 | 248 ms: 1.02x faster                                                       |
| docutils       | 2.59 sec                                                               | 2.55 sec: 1.01x faster                                                     |
| html5lib       | 59.4 ms                                                                | 57.7 ms: 1.03x faster                                                      |
| sphinx         | 996 ms                                                                 | 978 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250326-linux-x86_64-python-4b3d5b604210f68005ef-3.14.0a6+-4b3d5b6 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_generators           | 384 ms                                                                 | 383 ms: 1.00x faster                                                       |
| async_tree_cpu_io_mixed_tg | 471 ms                                                                 | 479 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                                 | 497 ms: 1.02x slower                                                       |
| coroutines                 | 21.4 ms                                                                | 22.0 ms: 1.03x slower                                                      |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (7): async_tree_io_tg, async_tree_io, async_tree_none, async_tree_none_tg, async_tree_memoization_tg, async_tree_memoization, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250326-linux-x86_64-python-4b3d5b604210f68005ef-3.14.0a6+-4b3d5b6 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 90.8 ms                                                                | 81.2 ms: 1.12x faster                                                      |
| float          | 69.6 ms                                                                | 68.1 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                                  | 1.05x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250326-linux-x86_64-python-4b3d5b604210f68005ef-3.14.0a6+-4b3d5b6 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 194 ms                                                                 | 183 ms: 1.06x faster                                                       |
| regex_effbot   | 3.24 ms                                                                | 3.07 ms: 1.05x faster                                                      |
| regex_v8       | 24.1 ms                                                                | 23.0 ms: 1.05x faster                                                      |
| regex_compile  | 126 ms                                                                 | 125 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                  | 1.04x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250326-linux-x86_64-python-4b3d5b604210f68005ef-3.14.0a6+-4b3d5b6 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 218 us                                                                 | 214 us: 1.02x faster                                                       |
| tomli_loads          | 1.90 sec                                                               | 1.87 sec: 1.01x faster                                                     |
| pickle_pure_python   | 307 us                                                                 | 304 us: 1.01x faster                                                       |
| xml_etree_process    | 59.4 ms                                                                | 58.9 ms: 1.01x faster                                                      |
| xml_etree_iterparse  | 102 ms                                                                 | 101 ms: 1.00x faster                                                       |
| xml_etree_parse      | 156 ms                                                                 | 158 ms: 1.01x slower                                                       |
| json_dumps           | 12.3 ms                                                                | 12.4 ms: 1.01x slower                                                      |
| json_loads           | 28.6 us                                                                | 29.0 us: 1.01x slower                                                      |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250326-linux-x86_64-python-4b3d5b604210f68005ef-3.14.0a6+-4b3d5b6 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 12.9 ms                                                                | 12.9 ms: 1.00x slower                                                      |
| python_startup_no_site | 8.10 ms                                                                | 8.12 ms: 1.00x slower                                                      |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250326-linux-x86_64-python-4b3d5b604210f68005ef-3.14.0a6+-4b3d5b6 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 11.8 ms                                                                | 11.6 ms: 1.02x faster                                                      |
| genshi_xml      | 47.4 ms                                                                | 46.9 ms: 1.01x faster                                                      |
| genshi_text     | 20.5 ms                                                                | 20.4 ms: 1.01x faster                                                      |
| django_template | 30.9 ms                                                                | 30.7 ms: 1.01x faster                                                      |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20250326-linux-x86_64-python-4b3d5b604210f68005ef-3.14.0a6+-4b3d5b6 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody                      | 90.8 ms                                                                | 81.2 ms: 1.12x faster                                                      |
| regex_dna                  | 194 ms                                                                 | 183 ms: 1.06x faster                                                       |
| regex_effbot               | 3.24 ms                                                                | 3.07 ms: 1.05x faster                                                      |
| regex_v8                   | 24.1 ms                                                                | 23.0 ms: 1.05x faster                                                      |
| go                         | 113 ms                                                                 | 109 ms: 1.04x faster                                                       |
| hexiom                     | 5.92 ms                                                                | 5.74 ms: 1.03x faster                                                      |
| html5lib                   | 59.4 ms                                                                | 57.7 ms: 1.03x faster                                                      |
| deltablue                  | 3.01 ms                                                                | 2.93 ms: 1.03x faster                                                      |
| comprehensions             | 16.1 us                                                                | 15.6 us: 1.03x faster                                                      |
| crypto_pyaes               | 72.9 ms                                                                | 71.0 ms: 1.03x faster                                                      |
| raytrace                   | 257 ms                                                                 | 250 ms: 1.03x faster                                                       |
| gc_traversal               | 5.09 ms                                                                | 4.96 ms: 1.02x faster                                                      |
| mako                       | 11.8 ms                                                                | 11.6 ms: 1.02x faster                                                      |
| float                      | 69.6 ms                                                                | 68.1 ms: 1.02x faster                                                      |
| pycparser                  | 1.13 sec                                                               | 1.11 sec: 1.02x faster                                                     |
| meteor_contest             | 110 ms                                                                 | 108 ms: 1.02x faster                                                       |
| pyflate                    | 419 ms                                                                 | 411 ms: 1.02x faster                                                       |
| bpe_tokeniser              | 4.47 sec                                                               | 4.38 sec: 1.02x faster                                                     |
| sphinx                     | 996 ms                                                                 | 978 ms: 1.02x faster                                                       |
| unpickle_pure_python       | 218 us                                                                 | 214 us: 1.02x faster                                                       |
| 2to3                       | 252 ms                                                                 | 248 ms: 1.02x faster                                                       |
| docutils                   | 2.59 sec                                                               | 2.55 sec: 1.01x faster                                                     |
| telco                      | 7.55 ms                                                                | 7.45 ms: 1.01x faster                                                      |
| pprint_pformat             | 1.53 sec                                                               | 1.51 sec: 1.01x faster                                                     |
| tomli_loads                | 1.90 sec                                                               | 1.87 sec: 1.01x faster                                                     |
| pprint_safe_repr           | 747 ms                                                                 | 738 ms: 1.01x faster                                                       |
| regex_compile              | 126 ms                                                                 | 125 ms: 1.01x faster                                                       |
| generators                 | 28.0 ms                                                                | 27.7 ms: 1.01x faster                                                      |
| scimark_sor                | 109 ms                                                                 | 108 ms: 1.01x faster                                                       |
| pickle_pure_python         | 307 us                                                                 | 304 us: 1.01x faster                                                       |
| genshi_xml                 | 47.4 ms                                                                | 46.9 ms: 1.01x faster                                                      |
| coverage                   | 81.7 ms                                                                | 81.0 ms: 1.01x faster                                                      |
| nqueens                    | 78.1 ms                                                                | 77.4 ms: 1.01x faster                                                      |
| sqlglot_v2_normalize       | 105 ms                                                                 | 104 ms: 1.01x faster                                                       |
| sqlglot_v2_optimize        | 52.6 ms                                                                | 52.2 ms: 1.01x faster                                                      |
| chaos                      | 54.6 ms                                                                | 54.1 ms: 1.01x faster                                                      |
| logging_format             | 6.03 us                                                                | 5.98 us: 1.01x faster                                                      |
| genshi_text                | 20.5 ms                                                                | 20.4 ms: 1.01x faster                                                      |
| xml_etree_process          | 59.4 ms                                                                | 58.9 ms: 1.01x faster                                                      |
| typing_runtime_protocols   | 155 us                                                                 | 154 us: 1.01x faster                                                       |
| django_template            | 30.9 ms                                                                | 30.7 ms: 1.01x faster                                                      |
| bench_thread_pool          | 840 us                                                                 | 834 us: 1.01x faster                                                       |
| dulwich_log                | 57.8 ms                                                                | 57.4 ms: 1.01x faster                                                      |
| fannkuch                   | 409 ms                                                                 | 407 ms: 1.01x faster                                                       |
| sqlglot_v2_transpile       | 1.52 ms                                                                | 1.52 ms: 1.01x faster                                                      |
| sqlglot_v2_parse           | 1.22 ms                                                                | 1.21 ms: 1.00x faster                                                      |
| async_generators           | 384 ms                                                                 | 383 ms: 1.00x faster                                                       |
| many_optionals             | 937 us                                                                 | 933 us: 1.00x faster                                                       |
| sympy_str                  | 263 ms                                                                 | 262 ms: 1.00x faster                                                       |
| xml_etree_iterparse        | 102 ms                                                                 | 101 ms: 1.00x faster                                                       |
| python_startup             | 12.9 ms                                                                | 12.9 ms: 1.00x slower                                                      |
| python_startup_no_site     | 8.10 ms                                                                | 8.12 ms: 1.00x slower                                                      |
| create_gc_cycles           | 2.54 ms                                                                | 2.55 ms: 1.00x slower                                                      |
| deepcopy_memo              | 28.8 us                                                                | 28.9 us: 1.01x slower                                                      |
| xml_etree_parse            | 156 ms                                                                 | 158 ms: 1.01x slower                                                       |
| logging_silent             | 88.1 ns                                                                | 89.0 ns: 1.01x slower                                                      |
| json_dumps                 | 12.3 ms                                                                | 12.4 ms: 1.01x slower                                                      |
| json_loads                 | 28.6 us                                                                | 29.0 us: 1.01x slower                                                      |
| json                       | 5.22 ms                                                                | 5.29 ms: 1.01x slower                                                      |
| mdp                        | 2.68 sec                                                               | 2.72 sec: 1.01x slower                                                     |
| async_tree_cpu_io_mixed_tg | 471 ms                                                                 | 479 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                                 | 497 ms: 1.02x slower                                                       |
| scimark_lu                 | 105 ms                                                                 | 107 ms: 1.02x slower                                                       |
| coroutines                 | 21.4 ms                                                                | 22.0 ms: 1.03x slower                                                      |
| scimark_fft                | 290 ms                                                                 | 301 ms: 1.04x slower                                                       |
| scimark_sparse_mat_mult    | 3.90 ms                                                                | 4.30 ms: 1.10x slower                                                      |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (30): async_tree_io_tg, async_tree_io, async_tree_none, logging_simple, bench_mp_pool, deepcopy_reduce, sympy_expand, xml_etree_generate, async_tree_none_tg, pylint, async_tree_memoization_tg, deepcopy, k_core, richards_super, subparsers, sqlalchemy_imperative, scimark_monte_carlo, pathlib, pidigits, sympy_integrate, async_tree_memoization, shortest_path, sqlalchemy_declarative, asyncio_websockets, sympy_sum, spectral_norm, connected_components, richards, thrift, sqlite_synth

- Geometric mean (including insignificant results): 1.007x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x