# Results vs. base

- fork: brandtbucher
- ref: jit_share_optimizati
- machine: linux-x86_64
- commit hash: 7d42f99
- commit date: 2025-04-21
- overall geometric mean: 1.001x slower
- HPT reliability: 95.70%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250421-linux-x86_64-python-09b624b80f54e1f97812-3.14.0a7+-09b624b | bm-20250421-linux-x86_64-brandtbucher-jit_share_optimizati-3.14.0a7+-7d42f99 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| docutils       | 2.67 sec                                                               | 2.68 sec: 1.00x slower                                                       |
| html5lib       | 60.3 ms                                                                | 62.1 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250421-linux-x86_64-python-09b624b80f54e1f97812-3.14.0a7+-09b624b | bm-20250421-linux-x86_64-brandtbucher-jit_share_optimizati-3.14.0a7+-7d42f99 |
|----------------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_eager_io_tg           | 612 ms                                                                 | 616 ms: 1.01x slower                                                         |
| async_tree_none_tg               | 250 ms                                                                 | 252 ms: 1.01x slower                                                         |
| async_tree_memoization           | 313 ms                                                                 | 316 ms: 1.01x slower                                                         |
| coroutines                       | 24.2 ms                                                                | 24.6 ms: 1.02x slower                                                        |
| async_tree_cpu_io_mixed          | 487 ms                                                                 | 496 ms: 1.02x slower                                                         |
| async_tree_memoization_tg        | 315 ms                                                                 | 321 ms: 1.02x slower                                                         |
| async_tree_eager_cpu_io_mixed_tg | 449 ms                                                                 | 458 ms: 1.02x slower                                                         |
| async_tree_cpu_io_mixed_tg       | 476 ms                                                                 | 487 ms: 1.02x slower                                                         |
| async_tree_eager_cpu_io_mixed    | 378 ms                                                                 | 387 ms: 1.03x slower                                                         |
| Geometric mean                   | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (10): async_tree_eager_memoization_tg, async_tree_none, async_tree_eager_tg, async_generators, asyncio_websockets, async_tree_eager_memoization, async_tree_io, async_tree_io_tg, async_tree_eager, async_tree_eager_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250421-linux-x86_64-python-09b624b80f54e1f97812-3.14.0a7+-09b624b | bm-20250421-linux-x86_64-brandtbucher-jit_share_optimizati-3.14.0a7+-7d42f99 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 195 ms                                                                 | 187 ms: 1.04x faster                                                         |
| nbody          | 88.8 ms                                                                | 86.7 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                                 |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250421-linux-x86_64-python-09b624b80f54e1f97812-3.14.0a7+-09b624b | bm-20250421-linux-x86_64-brandtbucher-jit_share_optimizati-3.14.0a7+-7d42f99 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.17 ms                                                                | 3.12 ms: 1.02x faster                                                        |
| regex_dna      | 202 ms                                                                 | 199 ms: 1.01x faster                                                         |
| regex_compile  | 126 ms                                                                 | 125 ms: 1.01x faster                                                         |
| regex_v8       | 23.2 ms                                                                | 23.4 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250421-linux-x86_64-python-09b624b80f54e1f97812-3.14.0a7+-09b624b | bm-20250421-linux-x86_64-brandtbucher-jit_share_optimizati-3.14.0a7+-7d42f99 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_loads           | 30.2 us                                                                | 29.8 us: 1.01x faster                                                        |
| pickle_pure_python   | 320 us                                                                 | 317 us: 1.01x faster                                                         |
| unpickle_pure_python | 209 us                                                                 | 207 us: 1.01x faster                                                         |
| xml_etree_iterparse  | 98.4 ms                                                                | 98.1 ms: 1.00x faster                                                        |
| xml_etree_generate   | 80.5 ms                                                                | 81.1 ms: 1.01x slower                                                        |
| xml_etree_process    | 56.3 ms                                                                | 56.8 ms: 1.01x slower                                                        |
| json_dumps           | 11.5 ms                                                                | 11.7 ms: 1.01x slower                                                        |
| tomli_loads          | 1.83 sec                                                               | 1.87 sec: 1.02x slower                                                       |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250421-linux-x86_64-python-09b624b80f54e1f97812-3.14.0a7+-09b624b | bm-20250421-linux-x86_64-brandtbucher-jit_share_optimizati-3.14.0a7+-7d42f99 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.21 ms                                                                | 8.25 ms: 1.01x slower                                                        |
| python_startup         | 13.2 ms                                                                | 13.3 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250421-linux-x86_64-python-09b624b80f54e1f97812-3.14.0a7+-09b624b | bm-20250421-linux-x86_64-brandtbucher-jit_share_optimizati-3.14.0a7+-7d42f99 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 31.6 ms                                                                | 32.0 ms: 1.01x slower                                                        |
| genshi_xml      | 49.3 ms                                                                | 50.1 ms: 1.02x slower                                                        |
| genshi_text     | 20.8 ms                                                                | 21.4 ms: 1.03x slower                                                        |
| mako            | 11.0 ms                                                                | 11.4 ms: 1.03x slower                                                        |
| Geometric mean  | (ref)                                                                  | 1.02x slower                                                                 |

All benchmarks:
===============

| Benchmark                        | bm-20250421-linux-x86_64-python-09b624b80f54e1f97812-3.14.0a7+-09b624b | bm-20250421-linux-x86_64-brandtbucher-jit_share_optimizati-3.14.0a7+-7d42f99 |
|----------------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| richards                         | 36.3 ms                                                                | 33.0 ms: 1.10x faster                                                        |
| richards_super                   | 41.3 ms                                                                | 38.2 ms: 1.08x faster                                                        |
| pidigits                         | 195 ms                                                                 | 187 ms: 1.04x faster                                                         |
| generators                       | 30.9 ms                                                                | 29.8 ms: 1.04x faster                                                        |
| logging_silent                   | 98.0 ns                                                                | 94.5 ns: 1.04x faster                                                        |
| nbody                            | 88.8 ms                                                                | 86.7 ms: 1.03x faster                                                        |
| pprint_safe_repr                 | 731 ms                                                                 | 718 ms: 1.02x faster                                                         |
| spectral_norm                    | 103 ms                                                                 | 101 ms: 1.02x faster                                                         |
| deepcopy_reduce                  | 2.67 us                                                                | 2.63 us: 1.02x faster                                                        |
| regex_effbot                     | 3.17 ms                                                                | 3.12 ms: 1.02x faster                                                        |
| regex_dna                        | 202 ms                                                                 | 199 ms: 1.01x faster                                                         |
| fannkuch                         | 424 ms                                                                 | 418 ms: 1.01x faster                                                         |
| bpe_tokeniser                    | 4.43 sec                                                               | 4.38 sec: 1.01x faster                                                       |
| json_loads                       | 30.2 us                                                                | 29.8 us: 1.01x faster                                                        |
| scimark_sor                      | 118 ms                                                                 | 117 ms: 1.01x faster                                                         |
| shortest_path                    | 496 ms                                                                 | 490 ms: 1.01x faster                                                         |
| chaos                            | 58.3 ms                                                                | 57.7 ms: 1.01x faster                                                        |
| telco                            | 7.77 ms                                                                | 7.69 ms: 1.01x faster                                                        |
| pickle_pure_python               | 320 us                                                                 | 317 us: 1.01x faster                                                         |
| unpickle_pure_python             | 209 us                                                                 | 207 us: 1.01x faster                                                         |
| crypto_pyaes                     | 74.5 ms                                                                | 73.9 ms: 1.01x faster                                                        |
| raytrace                         | 268 ms                                                                 | 266 ms: 1.01x faster                                                         |
| go                               | 126 ms                                                                 | 125 ms: 1.01x faster                                                         |
| regex_compile                    | 126 ms                                                                 | 125 ms: 1.01x faster                                                         |
| deltablue                        | 3.06 ms                                                                | 3.04 ms: 1.01x faster                                                        |
| meteor_contest                   | 110 ms                                                                 | 109 ms: 1.01x faster                                                         |
| xml_etree_iterparse              | 98.4 ms                                                                | 98.1 ms: 1.00x faster                                                        |
| docutils                         | 2.67 sec                                                               | 2.68 sec: 1.00x slower                                                       |
| sqlglot_v2_transpile             | 1.57 ms                                                                | 1.57 ms: 1.00x slower                                                        |
| python_startup_no_site           | 8.21 ms                                                                | 8.25 ms: 1.01x slower                                                        |
| python_startup                   | 13.2 ms                                                                | 13.3 ms: 1.01x slower                                                        |
| sqlite_synth                     | 2.77 us                                                                | 2.78 us: 1.01x slower                                                        |
| logging_format                   | 6.15 us                                                                | 6.19 us: 1.01x slower                                                        |
| async_tree_eager_io_tg           | 612 ms                                                                 | 616 ms: 1.01x slower                                                         |
| bench_mp_pool                    | 81.3 ms                                                                | 81.8 ms: 1.01x slower                                                        |
| bench_thread_pool                | 891 us                                                                 | 897 us: 1.01x slower                                                         |
| logging_simple                   | 5.60 us                                                                | 5.64 us: 1.01x slower                                                        |
| many_optionals                   | 950 us                                                                 | 957 us: 1.01x slower                                                         |
| xml_etree_generate               | 80.5 ms                                                                | 81.1 ms: 1.01x slower                                                        |
| sympy_integrate                  | 19.3 ms                                                                | 19.5 ms: 1.01x slower                                                        |
| async_tree_none_tg               | 250 ms                                                                 | 252 ms: 1.01x slower                                                         |
| sqlalchemy_imperative            | 17.3 ms                                                                | 17.4 ms: 1.01x slower                                                        |
| sqlalchemy_declarative           | 133 ms                                                                 | 135 ms: 1.01x slower                                                         |
| sympy_expand                     | 466 ms                                                                 | 470 ms: 1.01x slower                                                         |
| regex_v8                         | 23.2 ms                                                                | 23.4 ms: 1.01x slower                                                        |
| async_tree_memoization           | 313 ms                                                                 | 316 ms: 1.01x slower                                                         |
| xml_etree_process                | 56.3 ms                                                                | 56.8 ms: 1.01x slower                                                        |
| deepcopy                         | 251 us                                                                 | 254 us: 1.01x slower                                                         |
| django_template                  | 31.6 ms                                                                | 32.0 ms: 1.01x slower                                                        |
| json_dumps                       | 11.5 ms                                                                | 11.7 ms: 1.01x slower                                                        |
| coroutines                       | 24.2 ms                                                                | 24.6 ms: 1.02x slower                                                        |
| genshi_xml                       | 49.3 ms                                                                | 50.1 ms: 1.02x slower                                                        |
| async_tree_cpu_io_mixed          | 487 ms                                                                 | 496 ms: 1.02x slower                                                         |
| sympy_sum                        | 147 ms                                                                 | 150 ms: 1.02x slower                                                         |
| async_tree_memoization_tg        | 315 ms                                                                 | 321 ms: 1.02x slower                                                         |
| async_tree_eager_cpu_io_mixed_tg | 449 ms                                                                 | 458 ms: 1.02x slower                                                         |
| sympy_str                        | 269 ms                                                                 | 275 ms: 1.02x slower                                                         |
| tomli_loads                      | 1.83 sec                                                               | 1.87 sec: 1.02x slower                                                       |
| mdp                              | 1.21 sec                                                               | 1.24 sec: 1.02x slower                                                       |
| async_tree_cpu_io_mixed_tg       | 476 ms                                                                 | 487 ms: 1.02x slower                                                         |
| sqlglot_v2_normalize             | 107 ms                                                                 | 110 ms: 1.02x slower                                                         |
| pathlib                          | 16.8 ms                                                                | 17.2 ms: 1.02x slower                                                        |
| nqueens                          | 81.8 ms                                                                | 83.8 ms: 1.02x slower                                                        |
| genshi_text                      | 20.8 ms                                                                | 21.4 ms: 1.03x slower                                                        |
| async_tree_eager_cpu_io_mixed    | 378 ms                                                                 | 387 ms: 1.03x slower                                                         |
| html5lib                         | 60.3 ms                                                                | 62.1 ms: 1.03x slower                                                        |
| mako                             | 11.0 ms                                                                | 11.4 ms: 1.03x slower                                                        |
| hexiom                           | 6.57 ms                                                                | 6.81 ms: 1.04x slower                                                        |
| sqlglot_v2_optimize              | 53.2 ms                                                                | 55.3 ms: 1.04x slower                                                        |
| comprehensions                   | 18.4 us                                                                | 19.2 us: 1.05x slower                                                        |
| Geometric mean                   | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (33): json, pprint_pformat, async_tree_eager_memoization_tg, float, scimark_monte_carlo, async_tree_none, async_tree_eager_tg, xml_etree_parse, dulwich_log, subparsers, typing_runtime_protocols, deepcopy_memo, create_gc_cycles, pyflate, async_generators, gc_traversal, 2to3, asyncio_websockets, async_tree_eager_memoization, async_tree_io, scimark_fft, connected_components, sqlglot_v2_parse, coverage, scimark_sparse_mat_mult, k_core, scimark_lu, sphinx, async_tree_io_tg, async_tree_eager, async_tree_eager_io, pylint, pycparser

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 95.70% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x