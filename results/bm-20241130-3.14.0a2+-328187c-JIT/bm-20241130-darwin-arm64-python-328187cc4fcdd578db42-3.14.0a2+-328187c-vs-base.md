# Results vs. base

- fork: python
- ref: 328187cc4fcdd578db42
- machine: darwin-arm64
- commit hash: 328187c
- commit date: 2024-11-30
- overall geometric mean: 1.015x slower
- HPT reliability: 99.35%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20241130-3.14.0a2+-328187c/bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json | results/bm-20241130-3.14.0a2+-328187c-JIT/bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 169 ms                                                                                                            | 203 ms: 1.20x slower                                                                                                  |
| docutils       | 1.44 sec                                                                                                          | 1.52 sec: 1.05x slower                                                                                                |
| html5lib       | 31.3 ms                                                                                                           | 33.3 ms: 1.06x slower                                                                                                 |
| sphinx         | 592 ms                                                                                                            | 630 ms: 1.06x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.09x slower                                                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | results/bm-20241130-3.14.0a2+-328187c/bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json | results/bm-20241130-3.14.0a2+-328187c-JIT/bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json |
|----------------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| async_tree_io                    | 611 ms                                                                                                            | 609 ms: 1.00x faster                                                                                                  |
| async_tree_eager_cpu_io_mixed_tg | 342 ms                                                                                                            | 345 ms: 1.01x slower                                                                                                  |
| async_tree_eager_cpu_io_mixed    | 360 ms                                                                                                            | 365 ms: 1.01x slower                                                                                                  |
| async_tree_eager_memoization_tg  | 131 ms                                                                                                            | 133 ms: 1.02x slower                                                                                                  |
| async_tree_eager_tg              | 44.5 ms                                                                                                           | 45.4 ms: 1.02x slower                                                                                                 |
| async_tree_eager_memoization     | 160 ms                                                                                                            | 165 ms: 1.03x slower                                                                                                  |
| async_generators                 | 287 ms                                                                                                            | 304 ms: 1.06x slower                                                                                                  |
| async_tree_eager                 | 63.8 ms                                                                                                           | 67.9 ms: 1.06x slower                                                                                                 |
| Geometric mean                   | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (11): async_tree_io_tg, async_tree_none_tg, coroutines, async_tree_memoization, async_tree_eager_io_tg, async_tree_eager_io, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20241130-3.14.0a2+-328187c/bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json | results/bm-20241130-3.14.0a2+-328187c-JIT/bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| float          | 53.3 ms                                                                                                           | 48.9 ms: 1.09x faster                                                                                                 |
| nbody          | 68.6 ms                                                                                                           | 63.5 ms: 1.08x faster                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.06x faster                                                                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20241130-3.14.0a2+-328187c/bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json | results/bm-20241130-3.14.0a2+-328187c-JIT/bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 2.08 ms                                                                                                           | 2.01 ms: 1.03x faster                                                                                                 |
| regex_compile  | 72.1 ms                                                                                                           | 71.9 ms: 1.00x faster                                                                                                 |
| regex_v8       | 15.9 ms                                                                                                           | 16.0 ms: 1.00x slower                                                                                                 |
| regex_dna      | 134 ms                                                                                                            | 135 ms: 1.01x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.01x faster                                                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20241130-3.14.0a2+-328187c/bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json | results/bm-20241130-3.14.0a2+-328187c-JIT/bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 154 us                                                                                                            | 126 us: 1.23x faster                                                                                                  |
| tomli_loads          | 1.53 sec                                                                                                          | 1.26 sec: 1.21x faster                                                                                                |
| xml_etree_process    | 39.2 ms                                                                                                           | 35.7 ms: 1.10x faster                                                                                                 |
| xml_etree_generate   | 54.3 ms                                                                                                           | 50.7 ms: 1.07x faster                                                                                                 |
| pickle_pure_python   | 207 us                                                                                                            | 195 us: 1.06x faster                                                                                                  |
| xml_etree_iterparse  | 76.9 ms                                                                                                           | 74.5 ms: 1.03x faster                                                                                                 |
| json_dumps           | 7.28 ms                                                                                                           | 7.21 ms: 1.01x faster                                                                                                 |
| Geometric mean       | (ref)                                                                                                             | 1.08x faster                                                                                                          |

Benchmark hidden because not significant (2): json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20241130-3.14.0a2+-328187c/bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json | results/bm-20241130-3.14.0a2+-328187c-JIT/bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                                                                           | 20.5 ms: 1.01x slower                                                                                                 |
| python_startup_no_site | 15.5 ms                                                                                                           | 15.7 ms: 1.01x slower                                                                                                 |
| Geometric mean         | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20241130-3.14.0a2+-328187c/bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json | results/bm-20241130-3.14.0a2+-328187c-JIT/bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako            | 7.13 ms                                                                                                           | 6.24 ms: 1.14x faster                                                                                                 |
| django_template | 20.8 ms                                                                                                           | 23.0 ms: 1.10x slower                                                                                                 |
| genshi_text     | 14.4 ms                                                                                                           | 16.8 ms: 1.16x slower                                                                                                 |
| genshi_xml      | 31.0 ms                                                                                                           | 39.3 ms: 1.26x slower                                                                                                 |
| Geometric mean  | (ref)                                                                                                             | 1.09x slower                                                                                                          |

All benchmarks:
===============

| Benchmark                        | results/bm-20241130-3.14.0a2+-328187c/bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json | results/bm-20241130-3.14.0a2+-328187c-JIT/bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json |
|----------------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python             | 154 us                                                                                                            | 126 us: 1.23x faster                                                                                                  |
| tomli_loads                      | 1.53 sec                                                                                                          | 1.26 sec: 1.21x faster                                                                                                |
| scimark_sor                      | 101 ms                                                                                                            | 87.8 ms: 1.15x faster                                                                                                 |
| mako                             | 7.13 ms                                                                                                           | 6.24 ms: 1.14x faster                                                                                                 |
| xml_etree_process                | 39.2 ms                                                                                                           | 35.7 ms: 1.10x faster                                                                                                 |
| float                            | 53.3 ms                                                                                                           | 48.9 ms: 1.09x faster                                                                                                 |
| nbody                            | 68.6 ms                                                                                                           | 63.5 ms: 1.08x faster                                                                                                 |
| xml_etree_generate               | 54.3 ms                                                                                                           | 50.7 ms: 1.07x faster                                                                                                 |
| connected_components             | 320 ms                                                                                                            | 301 ms: 1.06x faster                                                                                                  |
| pickle_pure_python               | 207 us                                                                                                            | 195 us: 1.06x faster                                                                                                  |
| scimark_fft                      | 195 ms                                                                                                            | 186 ms: 1.05x faster                                                                                                  |
| shortest_path                    | 345 ms                                                                                                            | 330 ms: 1.04x faster                                                                                                  |
| bpe_tokeniser                    | 3.18 sec                                                                                                          | 3.05 sec: 1.04x faster                                                                                                |
| scimark_lu                       | 72.4 ms                                                                                                           | 69.3 ms: 1.04x faster                                                                                                 |
| spectral_norm                    | 72.7 ms                                                                                                           | 69.6 ms: 1.04x faster                                                                                                 |
| deepcopy_memo                    | 18.2 us                                                                                                           | 17.5 us: 1.04x faster                                                                                                 |
| regex_effbot                     | 2.08 ms                                                                                                           | 2.01 ms: 1.03x faster                                                                                                 |
| xml_etree_iterparse              | 76.9 ms                                                                                                           | 74.5 ms: 1.03x faster                                                                                                 |
| pyflate                          | 338 ms                                                                                                            | 327 ms: 1.03x faster                                                                                                  |
| scimark_monte_carlo              | 46.5 ms                                                                                                           | 45.3 ms: 1.03x faster                                                                                                 |
| deepcopy_reduce                  | 1.59 us                                                                                                           | 1.58 us: 1.01x faster                                                                                                 |
| json_dumps                       | 7.28 ms                                                                                                           | 7.21 ms: 1.01x faster                                                                                                 |
| telco                            | 4.58 ms                                                                                                           | 4.54 ms: 1.01x faster                                                                                                 |
| async_tree_io                    | 611 ms                                                                                                            | 609 ms: 1.00x faster                                                                                                  |
| pprint_safe_repr                 | 484 ms                                                                                                            | 482 ms: 1.00x faster                                                                                                  |
| regex_compile                    | 72.1 ms                                                                                                           | 71.9 ms: 1.00x faster                                                                                                 |
| pprint_pformat                   | 984 ms                                                                                                            | 982 ms: 1.00x faster                                                                                                  |
| bench_mp_pool                    | 61.7 ms                                                                                                           | 61.9 ms: 1.00x slower                                                                                                 |
| regex_v8                         | 15.9 ms                                                                                                           | 16.0 ms: 1.00x slower                                                                                                 |
| pathlib                          | 22.5 ms                                                                                                           | 22.7 ms: 1.01x slower                                                                                                 |
| regex_dna                        | 134 ms                                                                                                            | 135 ms: 1.01x slower                                                                                                  |
| async_tree_eager_cpu_io_mixed_tg | 342 ms                                                                                                            | 345 ms: 1.01x slower                                                                                                  |
| typing_runtime_protocols         | 98.2 us                                                                                                           | 99.1 us: 1.01x slower                                                                                                 |
| crypto_pyaes                     | 54.3 ms                                                                                                           | 54.8 ms: 1.01x slower                                                                                                 |
| create_gc_cycles                 | 1.30 ms                                                                                                           | 1.32 ms: 1.01x slower                                                                                                 |
| python_startup                   | 20.3 ms                                                                                                           | 20.5 ms: 1.01x slower                                                                                                 |
| python_startup_no_site           | 15.5 ms                                                                                                           | 15.7 ms: 1.01x slower                                                                                                 |
| meteor_contest                   | 72.4 ms                                                                                                           | 73.3 ms: 1.01x slower                                                                                                 |
| scimark_sparse_mat_mult          | 3.03 ms                                                                                                           | 3.07 ms: 1.01x slower                                                                                                 |
| async_tree_eager_cpu_io_mixed    | 360 ms                                                                                                            | 365 ms: 1.01x slower                                                                                                  |
| sqlite_synth                     | 1.54 us                                                                                                           | 1.56 us: 1.01x slower                                                                                                 |
| coverage                         | 44.2 ms                                                                                                           | 44.9 ms: 1.02x slower                                                                                                 |
| async_tree_eager_memoization_tg  | 131 ms                                                                                                            | 133 ms: 1.02x slower                                                                                                  |
| subparsers                       | 12.2 ms                                                                                                           | 12.4 ms: 1.02x slower                                                                                                 |
| sqlalchemy_declarative           | 58.6 ms                                                                                                           | 59.6 ms: 1.02x slower                                                                                                 |
| richards                         | 33.5 ms                                                                                                           | 34.2 ms: 1.02x slower                                                                                                 |
| async_tree_eager_tg              | 44.5 ms                                                                                                           | 45.4 ms: 1.02x slower                                                                                                 |
| thrift                           | 433 us                                                                                                            | 442 us: 1.02x slower                                                                                                  |
| async_tree_eager_memoization     | 160 ms                                                                                                            | 165 ms: 1.03x slower                                                                                                  |
| logging_simple                   | 3.29 us                                                                                                           | 3.40 us: 1.03x slower                                                                                                 |
| logging_format                   | 3.59 us                                                                                                           | 3.72 us: 1.03x slower                                                                                                 |
| pycparser                        | 658 ms                                                                                                            | 681 ms: 1.04x slower                                                                                                  |
| bench_thread_pool                | 475 us                                                                                                            | 492 us: 1.04x slower                                                                                                  |
| richards_super                   | 37.0 ms                                                                                                           | 38.4 ms: 1.04x slower                                                                                                 |
| sqlalchemy_imperative            | 6.44 ms                                                                                                           | 6.69 ms: 1.04x slower                                                                                                 |
| mdp                              | 1.52 sec                                                                                                          | 1.59 sec: 1.04x slower                                                                                                |
| sympy_str                        | 140 ms                                                                                                            | 147 ms: 1.05x slower                                                                                                  |
| sympy_expand                     | 236 ms                                                                                                            | 248 ms: 1.05x slower                                                                                                  |
| sympy_sum                        | 73.0 ms                                                                                                           | 76.9 ms: 1.05x slower                                                                                                 |
| fannkuch                         | 269 ms                                                                                                            | 284 ms: 1.05x slower                                                                                                  |
| sympy_integrate                  | 11.5 ms                                                                                                           | 12.1 ms: 1.05x slower                                                                                                 |
| docutils                         | 1.44 sec                                                                                                          | 1.52 sec: 1.05x slower                                                                                                |
| async_generators                 | 287 ms                                                                                                            | 304 ms: 1.06x slower                                                                                                  |
| deltablue                        | 2.47 ms                                                                                                           | 2.61 ms: 1.06x slower                                                                                                 |
| deepcopy                         | 152 us                                                                                                            | 161 us: 1.06x slower                                                                                                  |
| nqueens                          | 59.1 ms                                                                                                           | 62.6 ms: 1.06x slower                                                                                                 |
| pylint                           | 152 ms                                                                                                            | 161 ms: 1.06x slower                                                                                                  |
| async_tree_eager                 | 63.8 ms                                                                                                           | 67.9 ms: 1.06x slower                                                                                                 |
| html5lib                         | 31.3 ms                                                                                                           | 33.3 ms: 1.06x slower                                                                                                 |
| sphinx                           | 592 ms                                                                                                            | 630 ms: 1.06x slower                                                                                                  |
| dulwich_log                      | 28.1 ms                                                                                                           | 29.9 ms: 1.07x slower                                                                                                 |
| sqlglot_optimize                 | 33.0 ms                                                                                                           | 35.3 ms: 1.07x slower                                                                                                 |
| raytrace                         | 171 ms                                                                                                            | 183 ms: 1.07x slower                                                                                                  |
| many_optionals                   | 361 us                                                                                                            | 387 us: 1.07x slower                                                                                                  |
| sqlglot_transpile                | 983 us                                                                                                            | 1.06 ms: 1.08x slower                                                                                                 |
| sqlglot_parse                    | 808 us                                                                                                            | 880 us: 1.09x slower                                                                                                  |
| logging_silent                   | 70.3 ns                                                                                                           | 76.5 ns: 1.09x slower                                                                                                 |
| comprehensions                   | 12.5 us                                                                                                           | 13.7 us: 1.09x slower                                                                                                 |
| hexiom                           | 4.55 ms                                                                                                           | 4.97 ms: 1.09x slower                                                                                                 |
| sqlglot_normalize                | 181 ms                                                                                                            | 197 ms: 1.09x slower                                                                                                  |
| chaos                            | 39.4 ms                                                                                                           | 43.4 ms: 1.10x slower                                                                                                 |
| django_template                  | 20.8 ms                                                                                                           | 23.0 ms: 1.10x slower                                                                                                 |
| go                               | 87.6 ms                                                                                                           | 101 ms: 1.15x slower                                                                                                  |
| genshi_text                      | 14.4 ms                                                                                                           | 16.8 ms: 1.16x slower                                                                                                 |
| generators                       | 22.5 ms                                                                                                           | 26.8 ms: 1.19x slower                                                                                                 |
| 2to3                             | 169 ms                                                                                                            | 203 ms: 1.20x slower                                                                                                  |
| genshi_xml                       | 31.0 ms                                                                                                           | 39.3 ms: 1.26x slower                                                                                                 |
| Geometric mean                   | (ref)                                                                                                             | 1.02x slower                                                                                                          |

Benchmark hidden because not significant (17): k_core, async_tree_io_tg, async_tree_none_tg, json, coroutines, async_tree_memoization, async_tree_eager_io_tg, async_tree_eager_io, json_loads, pidigits, asyncio_websockets, async_tree_cpu_io_mixed_tg, gc_traversal, async_tree_memoization_tg, xml_etree_parse, async_tree_cpu_io_mixed, async_tree_none

- Geometric mean (including insignificant results): 1.015x slower

# HPT report

- Reliability score: 99.35% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.03x