# Results vs. base

- fork: faster-cpython
- ref: fix_132508
- machine: linux-x86_64
- commit hash: b1b1252
- commit date: 2025-04-15
- overall geometric mean: 1.000x faster
- HPT reliability: 53.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250414-linux-x86_64-python-844596c09fc812a58ac1-3.14.0a7+-844596c | bm-20250415-linux-x86_64-faster%2dcpython-fix_132508-3.14.0a7+-b1b1252 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| docutils       | 2.59 sec                                                               | 2.60 sec: 1.00x slower                                                 |
| html5lib       | 60.9 ms                                                                | 59.6 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250414-linux-x86_64-python-844596c09fc812a58ac1-3.14.0a7+-844596c | bm-20250415-linux-x86_64-faster%2dcpython-fix_132508-3.14.0a7+-b1b1252 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 491 ms                                                                 | 479 ms: 1.03x faster                                                   |
| async_tree_cpu_io_mixed_tg | 486 ms                                                                 | 477 ms: 1.02x faster                                                   |
| coroutines                 | 24.1 ms                                                                | 24.2 ms: 1.00x slower                                                  |
| async_generators           | 388 ms                                                                 | 393 ms: 1.01x slower                                                   |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (7): async_tree_io, async_tree_none_tg, asyncio_websockets, async_tree_memoization, async_tree_none, async_tree_memoization_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250414-linux-x86_64-python-844596c09fc812a58ac1-3.14.0a7+-844596c | bm-20250415-linux-x86_64-faster%2dcpython-fix_132508-3.14.0a7+-b1b1252 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 191 ms                                                                 | 187 ms: 1.02x faster                                                   |
| nbody          | 98.0 ms                                                                | 96.6 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250414-linux-x86_64-python-844596c09fc812a58ac1-3.14.0a7+-844596c | bm-20250415-linux-x86_64-faster%2dcpython-fix_132508-3.14.0a7+-b1b1252 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 125 ms                                                                 | 125 ms: 1.01x faster                                                   |
| regex_v8       | 23.3 ms                                                                | 23.8 ms: 1.02x slower                                                  |
| regex_dna      | 204 ms                                                                 | 209 ms: 1.02x slower                                                   |
| regex_effbot   | 3.07 ms                                                                | 3.25 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250414-linux-x86_64-python-844596c09fc812a58ac1-3.14.0a7+-844596c | bm-20250415-linux-x86_64-faster%2dcpython-fix_132508-3.14.0a7+-b1b1252 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.98 sec                                                               | 1.95 sec: 1.02x faster                                                 |
| unpickle_pure_python | 216 us                                                                 | 215 us: 1.01x faster                                                   |
| xml_etree_parse      | 140 ms                                                                 | 141 ms: 1.01x slower                                                   |
| json_dumps           | 11.5 ms                                                                | 11.7 ms: 1.01x slower                                                  |
| pickle_pure_python   | 312 us                                                                 | 316 us: 1.01x slower                                                   |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (4): xml_etree_process, json_loads, xml_etree_iterparse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250414-linux-x86_64-python-844596c09fc812a58ac1-3.14.0a7+-844596c | bm-20250415-linux-x86_64-faster%2dcpython-fix_132508-3.14.0a7+-b1b1252 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                                | 13.3 ms: 1.01x slower                                                  |
| python_startup_no_site | 8.22 ms                                                                | 8.28 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250414-linux-x86_64-python-844596c09fc812a58ac1-3.14.0a7+-844596c | bm-20250415-linux-x86_64-faster%2dcpython-fix_132508-3.14.0a7+-b1b1252 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 20.8 ms                                                                | 20.6 ms: 1.01x faster                                                  |
| genshi_xml      | 48.6 ms                                                                | 49.3 ms: 1.01x slower                                                  |
| mako            | 11.1 ms                                                                | 11.3 ms: 1.02x slower                                                  |
| django_template | 31.4 ms                                                                | 32.2 ms: 1.02x slower                                                  |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20250414-linux-x86_64-python-844596c09fc812a58ac1-3.14.0a7+-844596c | bm-20250415-linux-x86_64-faster%2dcpython-fix_132508-3.14.0a7+-b1b1252 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| logging_silent             | 98.9 ns                                                                | 94.9 ns: 1.04x faster                                                  |
| gc_traversal               | 4.82 ms                                                                | 4.65 ms: 1.04x faster                                                  |
| scimark_sparse_mat_mult    | 4.99 ms                                                                | 4.85 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed    | 491 ms                                                                 | 479 ms: 1.03x faster                                                   |
| hexiom                     | 6.28 ms                                                                | 6.13 ms: 1.02x faster                                                  |
| html5lib                   | 60.9 ms                                                                | 59.6 ms: 1.02x faster                                                  |
| pyflate                    | 444 ms                                                                 | 434 ms: 1.02x faster                                                   |
| async_tree_cpu_io_mixed_tg | 486 ms                                                                 | 477 ms: 1.02x faster                                                   |
| pidigits                   | 191 ms                                                                 | 187 ms: 1.02x faster                                                   |
| json                       | 5.38 ms                                                                | 5.28 ms: 1.02x faster                                                  |
| meteor_contest             | 107 ms                                                                 | 105 ms: 1.02x faster                                                   |
| tomli_loads                | 1.98 sec                                                               | 1.95 sec: 1.02x faster                                                 |
| nbody                      | 98.0 ms                                                                | 96.6 ms: 1.01x faster                                                  |
| deltablue                  | 3.37 ms                                                                | 3.32 ms: 1.01x faster                                                  |
| go                         | 111 ms                                                                 | 110 ms: 1.01x faster                                                   |
| sqlglot_v2_parse           | 1.22 ms                                                                | 1.21 ms: 1.01x faster                                                  |
| pathlib                    | 17.1 ms                                                                | 16.9 ms: 1.01x faster                                                  |
| sqlglot_v2_transpile       | 1.53 ms                                                                | 1.52 ms: 1.01x faster                                                  |
| genshi_text                | 20.8 ms                                                                | 20.6 ms: 1.01x faster                                                  |
| scimark_sor                | 118 ms                                                                 | 117 ms: 1.01x faster                                                   |
| crypto_pyaes               | 74.1 ms                                                                | 73.5 ms: 1.01x faster                                                  |
| coverage                   | 88.1 ms                                                                | 87.4 ms: 1.01x faster                                                  |
| connected_components       | 451 ms                                                                 | 447 ms: 1.01x faster                                                   |
| pprint_safe_repr           | 708 ms                                                                 | 703 ms: 1.01x faster                                                   |
| spectral_norm              | 105 ms                                                                 | 104 ms: 1.01x faster                                                   |
| regex_compile              | 125 ms                                                                 | 125 ms: 1.01x faster                                                   |
| unpickle_pure_python       | 216 us                                                                 | 215 us: 1.01x faster                                                   |
| mdp                        | 1.21 sec                                                               | 1.20 sec: 1.00x faster                                                 |
| dulwich_log                | 60.0 ms                                                                | 59.8 ms: 1.00x faster                                                  |
| many_optionals             | 931 us                                                                 | 934 us: 1.00x slower                                                   |
| sqlglot_v2_optimize        | 51.9 ms                                                                | 52.0 ms: 1.00x slower                                                  |
| coroutines                 | 24.1 ms                                                                | 24.2 ms: 1.00x slower                                                  |
| sqlalchemy_declarative     | 133 ms                                                                 | 133 ms: 1.00x slower                                                   |
| sqlglot_v2_normalize       | 105 ms                                                                 | 105 ms: 1.00x slower                                                   |
| docutils                   | 2.59 sec                                                               | 2.60 sec: 1.00x slower                                                 |
| sympy_sum                  | 147 ms                                                                 | 148 ms: 1.01x slower                                                   |
| scimark_fft                | 354 ms                                                                 | 356 ms: 1.01x slower                                                   |
| chaos                      | 56.2 ms                                                                | 56.5 ms: 1.01x slower                                                  |
| python_startup             | 13.2 ms                                                                | 13.3 ms: 1.01x slower                                                  |
| python_startup_no_site     | 8.22 ms                                                                | 8.28 ms: 1.01x slower                                                  |
| xml_etree_parse            | 140 ms                                                                 | 141 ms: 1.01x slower                                                   |
| sqlalchemy_imperative      | 16.8 ms                                                                | 16.9 ms: 1.01x slower                                                  |
| fannkuch                   | 415 ms                                                                 | 419 ms: 1.01x slower                                                   |
| raytrace                   | 260 ms                                                                 | 262 ms: 1.01x slower                                                   |
| bench_mp_pool              | 82.0 ms                                                                | 82.9 ms: 1.01x slower                                                  |
| logging_format             | 6.07 us                                                                | 6.13 us: 1.01x slower                                                  |
| async_generators           | 388 ms                                                                 | 393 ms: 1.01x slower                                                   |
| json_dumps                 | 11.5 ms                                                                | 11.7 ms: 1.01x slower                                                  |
| pickle_pure_python         | 312 us                                                                 | 316 us: 1.01x slower                                                   |
| scimark_lu                 | 116 ms                                                                 | 117 ms: 1.01x slower                                                   |
| genshi_xml                 | 48.6 ms                                                                | 49.3 ms: 1.01x slower                                                  |
| deepcopy                   | 247 us                                                                 | 251 us: 1.01x slower                                                   |
| mako                       | 11.1 ms                                                                | 11.3 ms: 1.02x slower                                                  |
| regex_v8                   | 23.3 ms                                                                | 23.8 ms: 1.02x slower                                                  |
| nqueens                    | 80.2 ms                                                                | 81.9 ms: 1.02x slower                                                  |
| generators                 | 28.9 ms                                                                | 29.5 ms: 1.02x slower                                                  |
| django_template            | 31.4 ms                                                                | 32.2 ms: 1.02x slower                                                  |
| regex_dna                  | 204 ms                                                                 | 209 ms: 1.02x slower                                                   |
| pycparser                  | 1.13 sec                                                               | 1.16 sec: 1.02x slower                                                 |
| regex_effbot               | 3.07 ms                                                                | 3.25 ms: 1.06x slower                                                  |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (35): k_core, telco, shortest_path, scimark_monte_carlo, subparsers, richards, float, pylint, async_tree_io, richards_super, comprehensions, typing_runtime_protocols, xml_etree_process, async_tree_none_tg, deepcopy_memo, asyncio_websockets, create_gc_cycles, json_loads, async_tree_memoization, sympy_expand, sympy_integrate, bench_thread_pool, 2to3, xml_etree_iterparse, xml_etree_generate, deepcopy_reduce, bpe_tokeniser, pprint_pformat, logging_simple, async_tree_none, sympy_str, sqlite_synth, async_tree_memoization_tg, sphinx, async_tree_io_tg

- Geometric mean (including insignificant results): 1.000x faster

# HPT report

- Reliability score: 53.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x