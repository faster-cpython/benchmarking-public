# Results vs. base

- fork: brandtbucher
- ref: warmup_side_4096
- machine: darwin-arm64
- commit hash: a8a4ed3
- commit date: 2024-11-22
- overall geometric mean: 1.003x faster
- HPT reliability: 99.78%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241122-darwin-arm64-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-darwin-arm64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 173 ms                                                                 | 170 ms: 1.02x faster                                                     |
| docutils       | 1.52 sec                                                               | 1.49 sec: 1.02x faster                                                   |
| sphinx         | 633 ms                                                                 | 618 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                             |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20241122-darwin-arm64-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-darwin-arm64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|-------------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_eager_cpu_io_mixed | 363 ms                                                                 | 362 ms: 1.00x faster                                                     |
| async_tree_eager              | 65.7 ms                                                                | 66.7 ms: 1.01x slower                                                    |
| Geometric mean                | (ref)                                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (17): async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_io_tg, async_tree_eager_io, async_tree_none, async_tree_cpu_io_mixed, async_tree_eager_io_tg, coroutines, async_tree_none_tg, async_tree_eager_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_memoization_tg, async_tree_io, asyncio_websockets, async_tree_memoization, async_tree_eager_memoization, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241122-darwin-arm64-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-darwin-arm64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 63.2 ms                                                                | 63.5 ms: 1.00x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                             |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241122-darwin-arm64-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-darwin-arm64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 71.8 ms                                                                | 70.4 ms: 1.02x faster                                                    |
| regex_effbot   | 2.03 ms                                                                | 2.02 ms: 1.00x faster                                                    |
| regex_dna      | 135 ms                                                                 | 135 ms: 1.00x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241122-darwin-arm64-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-darwin-arm64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 109 ms                                                                 | 108 ms: 1.01x faster                                                     |
| json_dumps           | 7.18 ms                                                                | 7.13 ms: 1.01x faster                                                    |
| unpickle_pure_python | 123 us                                                                 | 122 us: 1.00x faster                                                     |
| xml_etree_generate   | 49.7 ms                                                                | 49.9 ms: 1.00x slower                                                    |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (5): xml_etree_iterparse, pickle_pure_python, xml_etree_process, tomli_loads, json_loads

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241122-darwin-arm64-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-darwin-arm64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 22.5 ms                                                                | 23.1 ms: 1.03x slower                                                    |
| genshi_xml      | 38.6 ms                                                                | 40.2 ms: 1.04x slower                                                    |
| genshi_text     | 15.8 ms                                                                | 17.4 ms: 1.10x slower                                                    |
| Geometric mean  | (ref)                                                                  | 1.04x slower                                                             |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                     | bm-20241122-darwin-arm64-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-darwin-arm64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|-------------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                           | 1.75 sec                                                               | 1.60 sec: 1.09x faster                                                   |
| fannkuch                      | 279 ms                                                                 | 266 ms: 1.05x faster                                                     |
| comprehensions                | 13.9 us                                                                | 13.5 us: 1.03x faster                                                    |
| sympy_integrate               | 12.0 ms                                                                | 11.7 ms: 1.03x faster                                                    |
| sqlglot_transpile             | 1.06 ms                                                                | 1.03 ms: 1.03x faster                                                    |
| pylint                        | 161 ms                                                                 | 156 ms: 1.03x faster                                                     |
| bpe_tokeniser                 | 3.06 sec                                                               | 2.98 sec: 1.03x faster                                                   |
| sphinx                        | 633 ms                                                                 | 618 ms: 1.02x faster                                                     |
| sympy_sum                     | 76.1 ms                                                                | 74.4 ms: 1.02x faster                                                    |
| sqlglot_parse                 | 882 us                                                                 | 862 us: 1.02x faster                                                     |
| scimark_sparse_mat_mult       | 3.12 ms                                                                | 3.05 ms: 1.02x faster                                                    |
| 2to3                          | 173 ms                                                                 | 170 ms: 1.02x faster                                                     |
| docutils                      | 1.52 sec                                                               | 1.49 sec: 1.02x faster                                                   |
| sqlglot_normalize             | 189 ms                                                                 | 186 ms: 1.02x faster                                                     |
| sqlglot_optimize              | 34.9 ms                                                                | 34.3 ms: 1.02x faster                                                    |
| regex_compile                 | 71.8 ms                                                                | 70.4 ms: 1.02x faster                                                    |
| pathlib                       | 23.0 ms                                                                | 22.6 ms: 1.02x faster                                                    |
| sympy_expand                  | 248 ms                                                                 | 243 ms: 1.02x faster                                                     |
| sympy_str                     | 146 ms                                                                 | 144 ms: 1.02x faster                                                     |
| deltablue                     | 2.61 ms                                                                | 2.56 ms: 1.02x faster                                                    |
| deepcopy_reduce               | 1.58 us                                                                | 1.56 us: 1.01x faster                                                    |
| xml_etree_parse               | 109 ms                                                                 | 108 ms: 1.01x faster                                                     |
| shortest_path                 | 330 ms                                                                 | 326 ms: 1.01x faster                                                     |
| json                          | 2.92 ms                                                                | 2.88 ms: 1.01x faster                                                    |
| sqlalchemy_declarative        | 59.7 ms                                                                | 59.0 ms: 1.01x faster                                                    |
| sqlalchemy_imperative         | 6.67 ms                                                                | 6.60 ms: 1.01x faster                                                    |
| connected_components          | 299 ms                                                                 | 297 ms: 1.01x faster                                                     |
| thrift                        | 444 us                                                                 | 440 us: 1.01x faster                                                     |
| json_dumps                    | 7.18 ms                                                                | 7.13 ms: 1.01x faster                                                    |
| deepcopy_memo                 | 17.7 us                                                                | 17.5 us: 1.01x faster                                                    |
| hexiom                        | 4.91 ms                                                                | 4.87 ms: 1.01x faster                                                    |
| nqueens                       | 62.1 ms                                                                | 61.7 ms: 1.01x faster                                                    |
| deepcopy                      | 158 us                                                                 | 157 us: 1.01x faster                                                     |
| gc_traversal                  | 2.97 ms                                                                | 2.96 ms: 1.01x faster                                                    |
| pyflate                       | 324 ms                                                                 | 323 ms: 1.00x faster                                                     |
| go                            | 101 ms                                                                 | 100 ms: 1.00x faster                                                     |
| regex_effbot                  | 2.03 ms                                                                | 2.02 ms: 1.00x faster                                                    |
| unpickle_pure_python          | 123 us                                                                 | 122 us: 1.00x faster                                                     |
| scimark_lu                    | 68.8 ms                                                                | 68.5 ms: 1.00x faster                                                    |
| scimark_sor                   | 87.3 ms                                                                | 87.0 ms: 1.00x faster                                                    |
| logging_silent                | 76.1 ns                                                                | 75.9 ns: 1.00x faster                                                    |
| raytrace                      | 183 ms                                                                 | 182 ms: 1.00x faster                                                     |
| async_tree_eager_cpu_io_mixed | 363 ms                                                                 | 362 ms: 1.00x faster                                                     |
| scimark_monte_carlo           | 45.1 ms                                                                | 45.0 ms: 1.00x faster                                                    |
| regex_dna                     | 135 ms                                                                 | 135 ms: 1.00x slower                                                     |
| chaos                         | 43.4 ms                                                                | 43.6 ms: 1.00x slower                                                    |
| meteor_contest                | 73.0 ms                                                                | 73.2 ms: 1.00x slower                                                    |
| bench_thread_pool             | 488 us                                                                 | 489 us: 1.00x slower                                                     |
| xml_etree_generate            | 49.7 ms                                                                | 49.9 ms: 1.00x slower                                                    |
| nbody                         | 63.2 ms                                                                | 63.5 ms: 1.00x slower                                                    |
| pycparser                     | 672 ms                                                                 | 677 ms: 1.01x slower                                                     |
| generators                    | 26.9 ms                                                                | 27.1 ms: 1.01x slower                                                    |
| pprint_pformat                | 978 ms                                                                 | 990 ms: 1.01x slower                                                     |
| async_tree_eager              | 65.7 ms                                                                | 66.7 ms: 1.01x slower                                                    |
| richards                      | 33.5 ms                                                                | 34.2 ms: 1.02x slower                                                    |
| coverage                      | 44.6 ms                                                                | 45.5 ms: 1.02x slower                                                    |
| richards_super                | 37.3 ms                                                                | 38.1 ms: 1.02x slower                                                    |
| logging_format                | 3.66 us                                                                | 3.75 us: 1.02x slower                                                    |
| django_template               | 22.5 ms                                                                | 23.1 ms: 1.03x slower                                                    |
| logging_simple                | 3.36 us                                                                | 3.46 us: 1.03x slower                                                    |
| genshi_xml                    | 38.6 ms                                                                | 40.2 ms: 1.04x slower                                                    |
| pprint_safe_repr              | 473 ms                                                                 | 492 ms: 1.04x slower                                                     |
| genshi_text                   | 15.8 ms                                                                | 17.4 ms: 1.10x slower                                                    |
| Geometric mean                | (ref)                                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (41): async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, xml_etree_iterparse, async_tree_io_tg, async_tree_eager_io, async_tree_none, k_core, dulwich_log, python_startup_no_site, html5lib, async_tree_cpu_io_mixed, subparsers, async_tree_eager_io_tg, coroutines, async_tree_none_tg, async_tree_eager_tg, spectral_norm, create_gc_cycles, pickle_pure_python, regex_v8, async_tree_eager_cpu_io_mixed_tg, scimark_fft, pidigits, typing_runtime_protocols, xml_etree_process, async_tree_eager_memoization_tg, async_tree_io, asyncio_websockets, sqlite_synth, mako, python_startup, crypto_pyaes, async_tree_memoization, bench_mp_pool, async_tree_eager_memoization, telco, async_generators, tomli_loads, float, json_loads, many_optionals

- Geometric mean (including insignificant results): 1.003x faster
# HPT report

- Reliability score: 99.78% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x