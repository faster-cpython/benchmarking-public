# Results vs. base

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: darwin-arm64
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.008x slower
- HPT reliability: 92.14%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json | results/bm-20241214-3.14.0a2+-0ac40ac-JIT/bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 169 ms                                                                                                            | 198 ms: 1.17x slower                                                                                                  |
| docutils       | 1.42 sec                                                                                                          | 1.46 sec: 1.03x slower                                                                                                |
| html5lib       | 31.6 ms                                                                                                           | 33.5 ms: 1.06x slower                                                                                                 |
| sphinx         | 573 ms                                                                                                            | 597 ms: 1.04x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.08x slower                                                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json | results/bm-20241214-3.14.0a2+-0ac40ac-JIT/bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json |
|----------------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg                 | 380 ms                                                                                                            | 360 ms: 1.06x faster                                                                                                  |
| async_tree_eager_io_tg           | 388 ms                                                                                                            | 377 ms: 1.03x faster                                                                                                  |
| async_tree_none_tg               | 157 ms                                                                                                            | 154 ms: 1.02x faster                                                                                                  |
| async_tree_eager_io              | 377 ms                                                                                                            | 371 ms: 1.02x faster                                                                                                  |
| async_tree_io                    | 381 ms                                                                                                            | 376 ms: 1.01x faster                                                                                                  |
| async_tree_memoization           | 206 ms                                                                                                            | 204 ms: 1.01x faster                                                                                                  |
| coroutines                       | 17.4 ms                                                                                                           | 17.3 ms: 1.01x faster                                                                                                 |
| async_tree_memoization_tg        | 194 ms                                                                                                            | 193 ms: 1.01x faster                                                                                                  |
| async_tree_eager_cpu_io_mixed_tg | 342 ms                                                                                                            | 344 ms: 1.00x slower                                                                                                  |
| async_tree_cpu_io_mixed_tg       | 421 ms                                                                                                            | 423 ms: 1.01x slower                                                                                                  |
| async_tree_eager_cpu_io_mixed    | 364 ms                                                                                                            | 368 ms: 1.01x slower                                                                                                  |
| async_tree_eager_memoization_tg  | 126 ms                                                                                                            | 128 ms: 1.02x slower                                                                                                  |
| async_tree_eager_memoization     | 145 ms                                                                                                            | 150 ms: 1.03x slower                                                                                                  |
| async_tree_eager                 | 64.2 ms                                                                                                           | 67.3 ms: 1.05x slower                                                                                                 |
| async_generators                 | 283 ms                                                                                                            | 300 ms: 1.06x slower                                                                                                  |
| Geometric mean                   | (ref)                                                                                                             | 1.00x slower                                                                                                          |

Benchmark hidden because not significant (4): async_tree_none, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_eager_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json | results/bm-20241214-3.14.0a2+-0ac40ac-JIT/bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| nbody          | 68.4 ms                                                                                                           | 63.5 ms: 1.08x faster                                                                                                 |
| float          | 51.4 ms                                                                                                           | 47.9 ms: 1.07x faster                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.05x faster                                                                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json | results/bm-20241214-3.14.0a2+-0ac40ac-JIT/bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 70.7 ms                                                                                                           | 69.5 ms: 1.02x faster                                                                                                 |
| regex_effbot   | 2.03 ms                                                                                                           | 2.01 ms: 1.01x faster                                                                                                 |
| regex_v8       | 15.7 ms                                                                                                           | 15.9 ms: 1.02x slower                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.00x faster                                                                                                          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json | results/bm-20241214-3.14.0a2+-0ac40ac-JIT/bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 153 us                                                                                                            | 125 us: 1.23x faster                                                                                                  |
| tomli_loads          | 1.46 sec                                                                                                          | 1.22 sec: 1.20x faster                                                                                                |
| xml_etree_process    | 39.3 ms                                                                                                           | 35.0 ms: 1.12x faster                                                                                                 |
| xml_etree_generate   | 53.5 ms                                                                                                           | 49.2 ms: 1.09x faster                                                                                                 |
| pickle_pure_python   | 208 us                                                                                                            | 195 us: 1.07x faster                                                                                                  |
| xml_etree_iterparse  | 72.7 ms                                                                                                           | 70.4 ms: 1.03x faster                                                                                                 |
| json_dumps           | 7.35 ms                                                                                                           | 7.21 ms: 1.02x faster                                                                                                 |
| json_loads           | 16.6 us                                                                                                           | 16.5 us: 1.00x faster                                                                                                 |
| Geometric mean       | (ref)                                                                                                             | 1.08x faster                                                                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json | results/bm-20241214-3.14.0a2+-0ac40ac-JIT/bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| python_startup | 21.4 ms                                                                                                           | 21.6 ms: 1.01x slower                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json | results/bm-20241214-3.14.0a2+-0ac40ac-JIT/bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.93 ms                                                                                                           | 6.26 ms: 1.11x faster                                                                                                 |
| django_template | 21.2 ms                                                                                                           | 22.7 ms: 1.07x slower                                                                                                 |
| genshi_text     | 14.8 ms                                                                                                           | 17.3 ms: 1.17x slower                                                                                                 |
| genshi_xml      | 31.5 ms                                                                                                           | 40.9 ms: 1.30x slower                                                                                                 |
| Geometric mean  | (ref)                                                                                                             | 1.10x slower                                                                                                          |

All benchmarks:
===============

| Benchmark                        | results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json | results/bm-20241214-3.14.0a2+-0ac40ac-JIT/bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json |
|----------------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python             | 153 us                                                                                                            | 125 us: 1.23x faster                                                                                                  |
| mypy2                            | 644 ms                                                                                                            | 529 ms: 1.22x faster                                                                                                  |
| tomli_loads                      | 1.46 sec                                                                                                          | 1.22 sec: 1.20x faster                                                                                                |
| scimark_sor                      | 95.6 ms                                                                                                           | 82.2 ms: 1.16x faster                                                                                                 |
| xml_etree_process                | 39.3 ms                                                                                                           | 35.0 ms: 1.12x faster                                                                                                 |
| mako                             | 6.93 ms                                                                                                           | 6.26 ms: 1.11x faster                                                                                                 |
| xml_etree_generate               | 53.5 ms                                                                                                           | 49.2 ms: 1.09x faster                                                                                                 |
| connected_components             | 319 ms                                                                                                            | 296 ms: 1.08x faster                                                                                                  |
| nbody                            | 68.4 ms                                                                                                           | 63.5 ms: 1.08x faster                                                                                                 |
| float                            | 51.4 ms                                                                                                           | 47.9 ms: 1.07x faster                                                                                                 |
| pickle_pure_python               | 208 us                                                                                                            | 195 us: 1.07x faster                                                                                                  |
| bpe_tokeniser                    | 3.12 sec                                                                                                          | 2.94 sec: 1.06x faster                                                                                                |
| scimark_lu                       | 73.6 ms                                                                                                           | 69.3 ms: 1.06x faster                                                                                                 |
| deepcopy_memo                    | 18.1 us                                                                                                           | 17.2 us: 1.06x faster                                                                                                 |
| async_tree_io_tg                 | 380 ms                                                                                                            | 360 ms: 1.06x faster                                                                                                  |
| shortest_path                    | 344 ms                                                                                                            | 327 ms: 1.05x faster                                                                                                  |
| xml_etree_iterparse              | 72.7 ms                                                                                                           | 70.4 ms: 1.03x faster                                                                                                 |
| telco                            | 4.60 ms                                                                                                           | 4.46 ms: 1.03x faster                                                                                                 |
| async_tree_eager_io_tg           | 388 ms                                                                                                            | 377 ms: 1.03x faster                                                                                                  |
| pyflate                          | 327 ms                                                                                                            | 318 ms: 1.03x faster                                                                                                  |
| k_core                           | 1.55 sec                                                                                                          | 1.51 sec: 1.03x faster                                                                                                |
| scimark_monte_carlo              | 46.1 ms                                                                                                           | 45.2 ms: 1.02x faster                                                                                                 |
| async_tree_none_tg               | 157 ms                                                                                                            | 154 ms: 1.02x faster                                                                                                  |
| json_dumps                       | 7.35 ms                                                                                                           | 7.21 ms: 1.02x faster                                                                                                 |
| async_tree_eager_io              | 377 ms                                                                                                            | 371 ms: 1.02x faster                                                                                                  |
| deepcopy_reduce                  | 1.61 us                                                                                                           | 1.58 us: 1.02x faster                                                                                                 |
| regex_compile                    | 70.7 ms                                                                                                           | 69.5 ms: 1.02x faster                                                                                                 |
| async_tree_io                    | 381 ms                                                                                                            | 376 ms: 1.01x faster                                                                                                  |
| scimark_fft                      | 174 ms                                                                                                            | 171 ms: 1.01x faster                                                                                                  |
| crypto_pyaes                     | 54.5 ms                                                                                                           | 53.8 ms: 1.01x faster                                                                                                 |
| regex_effbot                     | 2.03 ms                                                                                                           | 2.01 ms: 1.01x faster                                                                                                 |
| async_tree_memoization           | 206 ms                                                                                                            | 204 ms: 1.01x faster                                                                                                  |
| coroutines                       | 17.4 ms                                                                                                           | 17.3 ms: 1.01x faster                                                                                                 |
| async_tree_memoization_tg        | 194 ms                                                                                                            | 193 ms: 1.01x faster                                                                                                  |
| json_loads                       | 16.6 us                                                                                                           | 16.5 us: 1.00x faster                                                                                                 |
| coverage                         | 44.2 ms                                                                                                           | 44.1 ms: 1.00x faster                                                                                                 |
| async_tree_eager_cpu_io_mixed_tg | 342 ms                                                                                                            | 344 ms: 1.00x slower                                                                                                  |
| spectral_norm                    | 61.8 ms                                                                                                           | 62.0 ms: 1.00x slower                                                                                                 |
| sqlalchemy_declarative           | 58.7 ms                                                                                                           | 58.9 ms: 1.00x slower                                                                                                 |
| fannkuch                         | 266 ms                                                                                                            | 267 ms: 1.00x slower                                                                                                  |
| pathlib                          | 22.4 ms                                                                                                           | 22.5 ms: 1.01x slower                                                                                                 |
| async_tree_cpu_io_mixed_tg       | 421 ms                                                                                                            | 423 ms: 1.01x slower                                                                                                  |
| meteor_contest                   | 72.3 ms                                                                                                           | 72.9 ms: 1.01x slower                                                                                                 |
| async_tree_eager_cpu_io_mixed    | 364 ms                                                                                                            | 368 ms: 1.01x slower                                                                                                  |
| python_startup                   | 21.4 ms                                                                                                           | 21.6 ms: 1.01x slower                                                                                                 |
| thrift                           | 436 us                                                                                                            | 443 us: 1.01x slower                                                                                                  |
| sqlite_synth                     | 1.53 us                                                                                                           | 1.55 us: 1.02x slower                                                                                                 |
| async_tree_eager_memoization_tg  | 126 ms                                                                                                            | 128 ms: 1.02x slower                                                                                                  |
| create_gc_cycles                 | 1.27 ms                                                                                                           | 1.29 ms: 1.02x slower                                                                                                 |
| regex_v8                         | 15.7 ms                                                                                                           | 15.9 ms: 1.02x slower                                                                                                 |
| typing_runtime_protocols         | 98.6 us                                                                                                           | 100 us: 1.02x slower                                                                                                  |
| sympy_integrate                  | 11.5 ms                                                                                                           | 11.8 ms: 1.02x slower                                                                                                 |
| sqlalchemy_imperative            | 6.49 ms                                                                                                           | 6.62 ms: 1.02x slower                                                                                                 |
| sympy_sum                        | 73.9 ms                                                                                                           | 75.6 ms: 1.02x slower                                                                                                 |
| pycparser                        | 658 ms                                                                                                            | 675 ms: 1.03x slower                                                                                                  |
| sympy_expand                     | 237 ms                                                                                                            | 244 ms: 1.03x slower                                                                                                  |
| sympy_str                        | 141 ms                                                                                                            | 146 ms: 1.03x slower                                                                                                  |
| pylint                           | 161 ms                                                                                                            | 166 ms: 1.03x slower                                                                                                  |
| pprint_safe_repr                 | 485 ms                                                                                                            | 500 ms: 1.03x slower                                                                                                  |
| docutils                         | 1.42 sec                                                                                                          | 1.46 sec: 1.03x slower                                                                                                |
| async_tree_eager_memoization     | 145 ms                                                                                                            | 150 ms: 1.03x slower                                                                                                  |
| pprint_pformat                   | 986 ms                                                                                                            | 1.02 sec: 1.03x slower                                                                                                |
| mdp                              | 1.52 sec                                                                                                          | 1.57 sec: 1.03x slower                                                                                                |
| dulwich_log                      | 27.8 ms                                                                                                           | 28.8 ms: 1.04x slower                                                                                                 |
| deepcopy                         | 151 us                                                                                                            | 157 us: 1.04x slower                                                                                                  |
| deltablue                        | 2.47 ms                                                                                                           | 2.56 ms: 1.04x slower                                                                                                 |
| bench_thread_pool                | 483 us                                                                                                            | 502 us: 1.04x slower                                                                                                  |
| sphinx                           | 573 ms                                                                                                            | 597 ms: 1.04x slower                                                                                                  |
| richards                         | 33.4 ms                                                                                                           | 35.0 ms: 1.05x slower                                                                                                 |
| async_tree_eager                 | 64.2 ms                                                                                                           | 67.3 ms: 1.05x slower                                                                                                 |
| logging_format                   | 3.57 us                                                                                                           | 3.74 us: 1.05x slower                                                                                                 |
| sqlglot_optimize                 | 32.7 ms                                                                                                           | 34.3 ms: 1.05x slower                                                                                                 |
| sqlglot_normalize                | 179 ms                                                                                                            | 188 ms: 1.05x slower                                                                                                  |
| richards_super                   | 36.9 ms                                                                                                           | 38.8 ms: 1.05x slower                                                                                                 |
| many_optionals                   | 360 us                                                                                                            | 379 us: 1.05x slower                                                                                                  |
| logging_simple                   | 3.26 us                                                                                                           | 3.44 us: 1.06x slower                                                                                                 |
| async_generators                 | 283 ms                                                                                                            | 300 ms: 1.06x slower                                                                                                  |
| nqueens                          | 58.2 ms                                                                                                           | 61.7 ms: 1.06x slower                                                                                                 |
| html5lib                         | 31.6 ms                                                                                                           | 33.5 ms: 1.06x slower                                                                                                 |
| sqlglot_transpile                | 971 us                                                                                                            | 1.04 ms: 1.07x slower                                                                                                 |
| django_template                  | 21.2 ms                                                                                                           | 22.7 ms: 1.07x slower                                                                                                 |
| sqlglot_parse                    | 800 us                                                                                                            | 856 us: 1.07x slower                                                                                                  |
| scimark_sparse_mat_mult          | 2.72 ms                                                                                                           | 2.94 ms: 1.08x slower                                                                                                 |
| raytrace                         | 170 ms                                                                                                            | 185 ms: 1.08x slower                                                                                                  |
| chaos                            | 39.0 ms                                                                                                           | 42.4 ms: 1.09x slower                                                                                                 |
| logging_silent                   | 69.3 ns                                                                                                           | 75.6 ns: 1.09x slower                                                                                                 |
| hexiom                           | 4.54 ms                                                                                                           | 4.96 ms: 1.09x slower                                                                                                 |
| comprehensions                   | 12.5 us                                                                                                           | 13.9 us: 1.11x slower                                                                                                 |
| go                               | 86.9 ms                                                                                                           | 100 ms: 1.16x slower                                                                                                  |
| genshi_text                      | 14.8 ms                                                                                                           | 17.3 ms: 1.17x slower                                                                                                 |
| 2to3                             | 169 ms                                                                                                            | 198 ms: 1.17x slower                                                                                                  |
| generators                       | 22.8 ms                                                                                                           | 27.3 ms: 1.20x slower                                                                                                 |
| genshi_xml                       | 31.5 ms                                                                                                           | 40.9 ms: 1.30x slower                                                                                                 |
| Geometric mean                   | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (12): async_tree_none, json, async_tree_cpu_io_mixed, bench_mp_pool, regex_dna, gc_traversal, pidigits, asyncio_websockets, async_tree_eager_tg, python_startup_no_site, subparsers, xml_etree_parse

- Geometric mean (including insignificant results): 1.008x slower

# HPT report

- Reliability score: 92.14% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x