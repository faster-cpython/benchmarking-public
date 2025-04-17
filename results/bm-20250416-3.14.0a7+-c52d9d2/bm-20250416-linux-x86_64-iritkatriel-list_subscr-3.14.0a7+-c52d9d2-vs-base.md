# Results vs. base

- fork: iritkatriel
- ref: list_subscr
- machine: linux-x86_64
- commit hash: c52d9d2
- commit date: 2025-04-16
- overall geometric mean: 1.000x faster
- HPT reliability: 78.57%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250416-linux-x86_64-python-62ff86fa55c903a8362a-3.14.0a7+-62ff86f | bm-20250416-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-c52d9d2 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 252 ms                                                                 | 250 ms: 1.01x faster                                               |
| docutils       | 2.61 sec                                                               | 2.61 sec: 1.00x faster                                             |
| html5lib       | 61.0 ms                                                                | 61.8 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                       |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250416-linux-x86_64-python-62ff86fa55c903a8362a-3.14.0a7+-62ff86f | bm-20250416-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-c52d9d2 |
|----------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_generators           | 398 ms                                                                 | 396 ms: 1.00x faster                                               |
| coroutines                 | 24.2 ms                                                                | 24.4 ms: 1.01x slower                                              |
| async_tree_cpu_io_mixed_tg | 477 ms                                                                 | 490 ms: 1.03x slower                                               |
| async_tree_cpu_io_mixed    | 480 ms                                                                 | 497 ms: 1.03x slower                                               |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                       |

Benchmark hidden because not significant (7): async_tree_none, async_tree_io_tg, asyncio_websockets, async_tree_io, async_tree_memoization_tg, async_tree_memoization, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250416-linux-x86_64-python-62ff86fa55c903a8362a-3.14.0a7+-62ff86f | bm-20250416-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-c52d9d2 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 69.1 ms                                                                | 68.2 ms: 1.01x faster                                              |
| pidigits       | 190 ms                                                                 | 191 ms: 1.01x slower                                               |
| nbody          | 93.7 ms                                                                | 95.4 ms: 1.02x slower                                              |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250416-linux-x86_64-python-62ff86fa55c903a8362a-3.14.0a7+-62ff86f | bm-20250416-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-c52d9d2 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 3.29 ms                                                                | 3.24 ms: 1.01x faster                                              |
| regex_compile  | 126 ms                                                                 | 125 ms: 1.00x faster                                               |
| regex_v8       | 22.9 ms                                                                | 23.2 ms: 1.01x slower                                              |
| regex_dna      | 206 ms                                                                 | 210 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250416-linux-x86_64-python-62ff86fa55c903a8362a-3.14.0a7+-62ff86f | bm-20250416-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-c52d9d2 |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| xml_etree_generate   | 86.2 ms                                                                | 84.5 ms: 1.02x faster                                              |
| xml_etree_process    | 59.7 ms                                                                | 58.5 ms: 1.02x faster                                              |
| pickle_pure_python   | 318 us                                                                 | 315 us: 1.01x faster                                               |
| unpickle_pure_python | 219 us                                                                 | 217 us: 1.01x faster                                               |
| xml_etree_iterparse  | 99.0 ms                                                                | 98.3 ms: 1.01x faster                                              |
| json_dumps           | 11.5 ms                                                                | 11.5 ms: 1.00x slower                                              |
| json_loads           | 29.7 us                                                                | 30.1 us: 1.01x slower                                              |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                       |

Benchmark hidden because not significant (2): xml_etree_parse, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250416-linux-x86_64-python-62ff86fa55c903a8362a-3.14.0a7+-62ff86f | bm-20250416-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-c52d9d2 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 8.22 ms                                                                | 8.22 ms: 1.00x faster                                              |
| python_startup         | 13.2 ms                                                                | 13.2 ms: 1.00x faster                                              |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250416-linux-x86_64-python-62ff86fa55c903a8362a-3.14.0a7+-62ff86f | bm-20250416-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-c52d9d2 |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 11.5 ms                                                                | 11.2 ms: 1.02x faster                                              |
| genshi_text     | 21.1 ms                                                                | 20.7 ms: 1.02x faster                                              |
| genshi_xml      | 49.1 ms                                                                | 48.7 ms: 1.01x faster                                              |
| django_template | 31.7 ms                                                                | 32.0 ms: 1.01x slower                                              |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20250416-linux-x86_64-python-62ff86fa55c903a8362a-3.14.0a7+-62ff86f | bm-20250416-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-c52d9d2 |
|----------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| gc_traversal               | 5.03 ms                                                                | 4.80 ms: 1.05x faster                                              |
| logging_silent             | 102 ns                                                                 | 98.8 ns: 1.03x faster                                              |
| fannkuch                   | 416 ms                                                                 | 405 ms: 1.03x faster                                               |
| generators                 | 30.6 ms                                                                | 29.9 ms: 1.02x faster                                              |
| mako                       | 11.5 ms                                                                | 11.2 ms: 1.02x faster                                              |
| genshi_text                | 21.1 ms                                                                | 20.7 ms: 1.02x faster                                              |
| xml_etree_generate         | 86.2 ms                                                                | 84.5 ms: 1.02x faster                                              |
| xml_etree_process          | 59.7 ms                                                                | 58.5 ms: 1.02x faster                                              |
| deepcopy_reduce            | 2.69 us                                                                | 2.64 us: 1.02x faster                                              |
| sqlglot_v2_transpile       | 1.56 ms                                                                | 1.53 ms: 1.01x faster                                              |
| regex_effbot               | 3.29 ms                                                                | 3.24 ms: 1.01x faster                                              |
| float                      | 69.1 ms                                                                | 68.2 ms: 1.01x faster                                              |
| sqlglot_v2_parse           | 1.24 ms                                                                | 1.23 ms: 1.01x faster                                              |
| coverage                   | 88.4 ms                                                                | 87.5 ms: 1.01x faster                                              |
| richards_super             | 49.3 ms                                                                | 48.8 ms: 1.01x faster                                              |
| genshi_xml                 | 49.1 ms                                                                | 48.7 ms: 1.01x faster                                              |
| subparsers                 | 20.8 ms                                                                | 20.6 ms: 1.01x faster                                              |
| pprint_safe_repr           | 714 ms                                                                 | 707 ms: 1.01x faster                                               |
| meteor_contest             | 106 ms                                                                 | 105 ms: 1.01x faster                                               |
| pickle_pure_python         | 318 us                                                                 | 315 us: 1.01x faster                                               |
| unpickle_pure_python       | 219 us                                                                 | 217 us: 1.01x faster                                               |
| deepcopy                   | 250 us                                                                 | 248 us: 1.01x faster                                               |
| hexiom                     | 6.22 ms                                                                | 6.17 ms: 1.01x faster                                              |
| raytrace                   | 263 ms                                                                 | 261 ms: 1.01x faster                                               |
| comprehensions             | 16.7 us                                                                | 16.6 us: 1.01x faster                                              |
| xml_etree_iterparse        | 99.0 ms                                                                | 98.3 ms: 1.01x faster                                              |
| 2to3                       | 252 ms                                                                 | 250 ms: 1.01x faster                                               |
| mdp                        | 1.22 sec                                                               | 1.22 sec: 1.00x faster                                             |
| bpe_tokeniser              | 4.60 sec                                                               | 4.58 sec: 1.00x faster                                             |
| pprint_pformat             | 1.45 sec                                                               | 1.44 sec: 1.00x faster                                             |
| richards                   | 42.9 ms                                                                | 42.8 ms: 1.00x faster                                              |
| async_generators           | 398 ms                                                                 | 396 ms: 1.00x faster                                               |
| deltablue                  | 3.40 ms                                                                | 3.39 ms: 1.00x faster                                              |
| docutils                   | 2.61 sec                                                               | 2.61 sec: 1.00x faster                                             |
| regex_compile              | 126 ms                                                                 | 125 ms: 1.00x faster                                               |
| scimark_sparse_mat_mult    | 4.88 ms                                                                | 4.88 ms: 1.00x faster                                              |
| python_startup_no_site     | 8.22 ms                                                                | 8.22 ms: 1.00x faster                                              |
| python_startup             | 13.2 ms                                                                | 13.2 ms: 1.00x faster                                              |
| many_optionals             | 929 us                                                                 | 931 us: 1.00x slower                                               |
| json_dumps                 | 11.5 ms                                                                | 11.5 ms: 1.00x slower                                              |
| deepcopy_memo              | 28.6 us                                                                | 28.7 us: 1.01x slower                                              |
| pidigits                   | 190 ms                                                                 | 191 ms: 1.01x slower                                               |
| chaos                      | 55.6 ms                                                                | 56.0 ms: 1.01x slower                                              |
| scimark_monte_carlo        | 66.3 ms                                                                | 66.8 ms: 1.01x slower                                              |
| logging_simple             | 5.41 us                                                                | 5.45 us: 1.01x slower                                              |
| crypto_pyaes               | 72.7 ms                                                                | 73.3 ms: 1.01x slower                                              |
| connected_components       | 450 ms                                                                 | 454 ms: 1.01x slower                                               |
| django_template            | 31.7 ms                                                                | 32.0 ms: 1.01x slower                                              |
| coroutines                 | 24.2 ms                                                                | 24.4 ms: 1.01x slower                                              |
| regex_v8                   | 22.9 ms                                                                | 23.2 ms: 1.01x slower                                              |
| scimark_sor                | 118 ms                                                                 | 119 ms: 1.01x slower                                               |
| html5lib                   | 61.0 ms                                                                | 61.8 ms: 1.01x slower                                              |
| scimark_fft                | 355 ms                                                                 | 360 ms: 1.01x slower                                               |
| json_loads                 | 29.7 us                                                                | 30.1 us: 1.01x slower                                              |
| go                         | 111 ms                                                                 | 112 ms: 1.01x slower                                               |
| logging_format             | 5.95 us                                                                | 6.04 us: 1.02x slower                                              |
| regex_dna                  | 206 ms                                                                 | 210 ms: 1.02x slower                                               |
| nbody                      | 93.7 ms                                                                | 95.4 ms: 1.02x slower                                              |
| typing_runtime_protocols   | 164 us                                                                 | 167 us: 1.02x slower                                               |
| pathlib                    | 16.6 ms                                                                | 17.0 ms: 1.02x slower                                              |
| async_tree_cpu_io_mixed_tg | 477 ms                                                                 | 490 ms: 1.03x slower                                               |
| async_tree_cpu_io_mixed    | 480 ms                                                                 | 497 ms: 1.03x slower                                               |
| pyflate                    | 435 ms                                                                 | 453 ms: 1.04x slower                                               |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                       |

Benchmark hidden because not significant (32): pycparser, nqueens, async_tree_none, sympy_sum, shortest_path, sympy_expand, bench_mp_pool, sqlglot_v2_normalize, scimark_lu, sqlite_synth, sphinx, create_gc_cycles, dulwich_log, k_core, sqlglot_v2_optimize, xml_etree_parse, bench_thread_pool, pylint, async_tree_io_tg, sympy_integrate, asyncio_websockets, async_tree_io, sympy_str, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, async_tree_memoization_tg, telco, async_tree_memoization, json, spectral_norm, async_tree_none_tg

- Geometric mean (including insignificant results): 1.000x faster

# HPT report

- Reliability score: 78.57% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x