# Results vs. base

- fork: iritkatriel
- ref: list_subscr
- machine: linux-x86_64
- commit hash: 638a892
- commit date: 2025-04-29
- overall geometric mean: 1.001x slower
- HPT reliability: 92.67%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250430-linux-x86_64-python-42b0b0667e67ff444a03-3.14.0a7+-42b0b06 | bm-20250429-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-638a892 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 252 ms                                                                 | 254 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                       |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250430-linux-x86_64-python-42b0b0667e67ff444a03-3.14.0a7+-42b0b06 | bm-20250429-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-638a892 |
|----------------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_eager_cpu_io_mixed    | 389 ms                                                                 | 381 ms: 1.02x faster                                               |
| async_tree_eager_cpu_io_mixed_tg | 466 ms                                                                 | 459 ms: 1.02x faster                                               |
| async_tree_cpu_io_mixed          | 497 ms                                                                 | 492 ms: 1.01x faster                                               |
| async_tree_cpu_io_mixed_tg       | 493 ms                                                                 | 487 ms: 1.01x faster                                               |
| async_tree_eager                 | 103 ms                                                                 | 103 ms: 1.01x faster                                               |
| async_tree_memoization_tg        | 309 ms                                                                 | 311 ms: 1.01x slower                                               |
| async_tree_io                    | 591 ms                                                                 | 597 ms: 1.01x slower                                               |
| async_tree_memoization           | 312 ms                                                                 | 315 ms: 1.01x slower                                               |
| async_tree_none                  | 260 ms                                                                 | 263 ms: 1.01x slower                                               |
| async_tree_eager_memoization_tg  | 282 ms                                                                 | 285 ms: 1.01x slower                                               |
| Geometric mean                   | (ref)                                                                  | 1.00x faster                                                       |

Benchmark hidden because not significant (9): async_tree_eager_memoization, asyncio_websockets, async_tree_eager_io, coroutines, async_tree_none_tg, async_generators, async_tree_eager_io_tg, async_tree_eager_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250430-linux-x86_64-python-42b0b0667e67ff444a03-3.14.0a7+-42b0b06 | bm-20250429-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-638a892 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| pidigits       | 199 ms                                                                 | 188 ms: 1.06x faster                                               |
| nbody          | 98.0 ms                                                                | 96.3 ms: 1.02x faster                                              |
| float          | 68.6 ms                                                                | 69.2 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250430-linux-x86_64-python-42b0b0667e67ff444a03-3.14.0a7+-42b0b06 | bm-20250429-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-638a892 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 3.17 ms                                                                | 3.14 ms: 1.01x faster                                              |
| regex_compile  | 125 ms                                                                 | 126 ms: 1.01x slower                                               |
| regex_dna      | 208 ms                                                                 | 209 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                       |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250430-linux-x86_64-python-42b0b0667e67ff444a03-3.14.0a7+-42b0b06 | bm-20250429-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-638a892 |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| xml_etree_process    | 60.8 ms                                                                | 60.5 ms: 1.00x faster                                              |
| unpickle_pure_python | 218 us                                                                 | 219 us: 1.00x slower                                               |
| json_loads           | 29.8 us                                                                | 30.0 us: 1.01x slower                                              |
| xml_etree_parse      | 142 ms                                                                 | 143 ms: 1.01x slower                                               |
| tomli_loads          | 1.96 sec                                                               | 1.98 sec: 1.01x slower                                             |
| xml_etree_iterparse  | 99.5 ms                                                                | 100 ms: 1.01x slower                                               |
| xml_etree_generate   | 86.2 ms                                                                | 87.6 ms: 1.02x slower                                              |
| pickle_pure_python   | 313 us                                                                 | 319 us: 1.02x slower                                               |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                       |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250430-linux-x86_64-python-42b0b0667e67ff444a03-3.14.0a7+-42b0b06 | bm-20250429-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-638a892 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 13.1 ms                                                                | 13.0 ms: 1.00x faster                                              |
| python_startup_no_site | 6.88 ms                                                                | 6.87 ms: 1.00x faster                                              |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250430-linux-x86_64-python-42b0b0667e67ff444a03-3.14.0a7+-42b0b06 | bm-20250429-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-638a892 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text    | 21.5 ms                                                                | 21.1 ms: 1.02x faster                                              |
| mako           | 11.8 ms                                                                | 11.7 ms: 1.01x faster                                              |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                       |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                        | bm-20250430-linux-x86_64-python-42b0b0667e67ff444a03-3.14.0a7+-42b0b06 | bm-20250429-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-638a892 |
|----------------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| pidigits                         | 199 ms                                                                 | 188 ms: 1.06x faster                                               |
| gc_traversal                     | 5.00 ms                                                                | 4.85 ms: 1.03x faster                                              |
| async_tree_eager_cpu_io_mixed    | 389 ms                                                                 | 381 ms: 1.02x faster                                               |
| genshi_text                      | 21.5 ms                                                                | 21.1 ms: 1.02x faster                                              |
| nbody                            | 98.0 ms                                                                | 96.3 ms: 1.02x faster                                              |
| async_tree_eager_cpu_io_mixed_tg | 466 ms                                                                 | 459 ms: 1.02x faster                                               |
| async_tree_cpu_io_mixed          | 497 ms                                                                 | 492 ms: 1.01x faster                                               |
| typing_runtime_protocols         | 169 us                                                                 | 167 us: 1.01x faster                                               |
| scimark_fft                      | 360 ms                                                                 | 356 ms: 1.01x faster                                               |
| async_tree_cpu_io_mixed_tg       | 493 ms                                                                 | 487 ms: 1.01x faster                                               |
| regex_effbot                     | 3.17 ms                                                                | 3.14 ms: 1.01x faster                                              |
| mako                             | 11.8 ms                                                                | 11.7 ms: 1.01x faster                                              |
| async_tree_eager                 | 103 ms                                                                 | 103 ms: 1.01x faster                                               |
| raytrace                         | 264 ms                                                                 | 261 ms: 1.01x faster                                               |
| shortest_path                    | 492 ms                                                                 | 487 ms: 1.01x faster                                               |
| fannkuch                         | 411 ms                                                                 | 408 ms: 1.01x faster                                               |
| logging_format                   | 6.15 us                                                                | 6.11 us: 1.01x faster                                              |
| sympy_str                        | 268 ms                                                                 | 266 ms: 1.01x faster                                               |
| create_gc_cycles                 | 2.49 ms                                                                | 2.48 ms: 1.01x faster                                              |
| richards                         | 43.7 ms                                                                | 43.4 ms: 1.01x faster                                              |
| meteor_contest                   | 106 ms                                                                 | 106 ms: 1.01x faster                                               |
| xml_etree_process                | 60.8 ms                                                                | 60.5 ms: 1.00x faster                                              |
| go                               | 112 ms                                                                 | 112 ms: 1.00x faster                                               |
| python_startup                   | 13.1 ms                                                                | 13.0 ms: 1.00x faster                                              |
| python_startup_no_site           | 6.88 ms                                                                | 6.87 ms: 1.00x faster                                              |
| sqlglot_v2_optimize              | 52.2 ms                                                                | 52.3 ms: 1.00x slower                                              |
| unpickle_pure_python             | 218 us                                                                 | 219 us: 1.00x slower                                               |
| sqlalchemy_declarative           | 131 ms                                                                 | 132 ms: 1.00x slower                                               |
| mdp                              | 1.22 sec                                                               | 1.23 sec: 1.00x slower                                             |
| comprehensions                   | 16.6 us                                                                | 16.7 us: 1.00x slower                                              |
| regex_compile                    | 125 ms                                                                 | 126 ms: 1.01x slower                                               |
| scimark_sor                      | 119 ms                                                                 | 119 ms: 1.01x slower                                               |
| json_loads                       | 29.8 us                                                                | 30.0 us: 1.01x slower                                              |
| regex_dna                        | 208 ms                                                                 | 209 ms: 1.01x slower                                               |
| bpe_tokeniser                    | 4.47 sec                                                               | 4.50 sec: 1.01x slower                                             |
| sqlalchemy_imperative            | 17.1 ms                                                                | 17.3 ms: 1.01x slower                                              |
| pprint_pformat                   | 1.46 sec                                                               | 1.47 sec: 1.01x slower                                             |
| async_tree_memoization_tg        | 309 ms                                                                 | 311 ms: 1.01x slower                                               |
| xml_etree_parse                  | 142 ms                                                                 | 143 ms: 1.01x slower                                               |
| scimark_monte_carlo              | 66.3 ms                                                                | 66.8 ms: 1.01x slower                                              |
| scimark_lu                       | 116 ms                                                                 | 117 ms: 1.01x slower                                               |
| tomli_loads                      | 1.96 sec                                                               | 1.98 sec: 1.01x slower                                             |
| xml_etree_iterparse              | 99.5 ms                                                                | 100 ms: 1.01x slower                                               |
| async_tree_io                    | 591 ms                                                                 | 597 ms: 1.01x slower                                               |
| float                            | 68.6 ms                                                                | 69.2 ms: 1.01x slower                                              |
| chaos                            | 56.3 ms                                                                | 56.9 ms: 1.01x slower                                              |
| 2to3                             | 252 ms                                                                 | 254 ms: 1.01x slower                                               |
| async_tree_memoization           | 312 ms                                                                 | 315 ms: 1.01x slower                                               |
| async_tree_none                  | 260 ms                                                                 | 263 ms: 1.01x slower                                               |
| subparsers                       | 20.9 ms                                                                | 21.1 ms: 1.01x slower                                              |
| async_tree_eager_memoization_tg  | 282 ms                                                                 | 285 ms: 1.01x slower                                               |
| generators                       | 29.2 ms                                                                | 29.6 ms: 1.01x slower                                              |
| pycparser                        | 1.15 sec                                                               | 1.17 sec: 1.01x slower                                             |
| crypto_pyaes                     | 72.5 ms                                                                | 73.6 ms: 1.01x slower                                              |
| xml_etree_generate               | 86.2 ms                                                                | 87.6 ms: 1.02x slower                                              |
| spectral_norm                    | 103 ms                                                                 | 104 ms: 1.02x slower                                               |
| pprint_safe_repr                 | 711 ms                                                                 | 723 ms: 1.02x slower                                               |
| sqlite_synth                     | 2.83 us                                                                | 2.88 us: 1.02x slower                                              |
| pickle_pure_python               | 313 us                                                                 | 319 us: 1.02x slower                                               |
| pathlib                          | 16.7 ms                                                                | 17.0 ms: 1.02x slower                                              |
| deepcopy_reduce                  | 2.67 us                                                                | 2.72 us: 1.02x slower                                              |
| deepcopy                         | 253 us                                                                 | 258 us: 1.02x slower                                               |
| hexiom                           | 6.17 ms                                                                | 6.30 ms: 1.02x slower                                              |
| scimark_sparse_mat_mult          | 5.04 ms                                                                | 5.16 ms: 1.02x slower                                              |
| logging_silent                   | 95.1 ns                                                                | 98.2 ns: 1.03x slower                                              |
| Geometric mean                   | (ref)                                                                  | 1.00x slower                                                       |

Benchmark hidden because not significant (38): async_tree_eager_memoization, k_core, django_template, deepcopy_memo, sqlglot_v2_normalize, pyflate, logging_simple, coverage, connected_components, asyncio_websockets, json_dumps, async_tree_eager_io, sympy_integrate, telco, coroutines, sqlglot_v2_parse, sqlglot_v2_transpile, sympy_expand, nqueens, async_tree_none_tg, pylint, docutils, richards_super, regex_v8, bench_thread_pool, deltablue, dulwich_log, many_optionals, bench_mp_pool, async_generators, genshi_xml, async_tree_eager_io_tg, sympy_sum, html5lib, sphinx, async_tree_eager_tg, json, async_tree_io_tg

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 92.67% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x