# Results vs. base

- fork: python
- ref: f6cc7c8bd01d8468af70
- machine: darwin-arm64
- commit hash: f6cc7c8
- commit date: 2024-10-26
- overall geometric mean: 1.046x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json | results/bm-20241026-3.14.0a1+-f6cc7c8-JIT/bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 160 ms                                                                                                            | 184 ms: 1.15x slower                                                                                                  |
| docutils       | 1.40 sec                                                                                                          | 1.57 sec: 1.12x slower                                                                                                |
| html5lib       | 30.1 ms                                                                                                           | 32.6 ms: 1.08x slower                                                                                                 |
| sphinx         | 576 ms                                                                                                            | 665 ms: 1.15x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.12x slower                                                                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json | results/bm-20241026-3.14.0a1+-f6cc7c8-JIT/bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json |
|----------------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| coroutines                       | 16.5 ms                                                                                                           | 16.6 ms: 1.00x slower                                                                                                 |
| async_tree_io_tg                 | 611 ms                                                                                                            | 613 ms: 1.00x slower                                                                                                  |
| async_tree_eager_cpu_io_mixed_tg | 335 ms                                                                                                            | 336 ms: 1.00x slower                                                                                                  |
| async_tree_none                  | 199 ms                                                                                                            | 201 ms: 1.01x slower                                                                                                  |
| async_tree_eager_cpu_io_mixed    | 359 ms                                                                                                            | 363 ms: 1.01x slower                                                                                                  |
| async_tree_eager_io_tg           | 704 ms                                                                                                            | 715 ms: 1.02x slower                                                                                                  |
| async_tree_eager_tg              | 42.3 ms                                                                                                           | 43.1 ms: 1.02x slower                                                                                                 |
| async_tree_eager_memoization     | 150 ms                                                                                                            | 154 ms: 1.03x slower                                                                                                  |
| async_tree_eager                 | 61.1 ms                                                                                                           | 64.5 ms: 1.06x slower                                                                                                 |
| async_generators                 | 277 ms                                                                                                            | 295 ms: 1.07x slower                                                                                                  |
| Geometric mean                   | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (9): async_tree_memoization, async_tree_none_tg, async_tree_memoization_tg, asyncio_websockets, async_tree_io, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_eager_memoization_tg, async_tree_eager_io

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json | results/bm-20241026-3.14.0a1+-f6cc7c8-JIT/bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| float          | 49.8 ms                                                                                                           | 48.7 ms: 1.02x faster                                                                                                 |
| nbody          | 66.0 ms                                                                                                           | 65.9 ms: 1.00x faster                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.01x faster                                                                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json | results/bm-20241026-3.14.0a1+-f6cc7c8-JIT/bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 142 ms                                                                                                            | 143 ms: 1.00x slower                                                                                                  |
| regex_v8       | 16.6 ms                                                                                                           | 16.8 ms: 1.01x slower                                                                                                 |
| regex_effbot   | 2.45 ms                                                                                                           | 2.48 ms: 1.02x slower                                                                                                 |
| regex_compile  | 68.1 ms                                                                                                           | 75.3 ms: 1.11x slower                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.03x slower                                                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json | results/bm-20241026-3.14.0a1+-f6cc7c8-JIT/bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.49 sec                                                                                                          | 1.26 sec: 1.19x faster                                                                                                |
| xml_etree_process    | 37.2 ms                                                                                                           | 34.8 ms: 1.07x faster                                                                                                 |
| unpickle_pure_python | 142 us                                                                                                            | 134 us: 1.06x faster                                                                                                  |
| xml_etree_generate   | 52.3 ms                                                                                                           | 49.6 ms: 1.05x faster                                                                                                 |
| xml_etree_iterparse  | 74.6 ms                                                                                                           | 72.8 ms: 1.02x faster                                                                                                 |
| pickle_pure_python   | 183 us                                                                                                            | 179 us: 1.02x faster                                                                                                  |
| json_dumps           | 7.18 ms                                                                                                           | 7.13 ms: 1.01x faster                                                                                                 |
| Geometric mean       | (ref)                                                                                                             | 1.05x faster                                                                                                          |

Benchmark hidden because not significant (2): json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json | results/bm-20241026-3.14.0a1+-f6cc7c8-JIT/bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 18.9 ms                                                                                                           | 18.8 ms: 1.00x faster                                                                                                 |
| python_startup_no_site | 14.3 ms                                                                                                           | 14.4 ms: 1.01x slower                                                                                                 |
| Geometric mean         | (ref)                                                                                                             | 1.00x slower                                                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json | results/bm-20241026-3.14.0a1+-f6cc7c8-JIT/bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.97 ms                                                                                                           | 6.44 ms: 1.08x faster                                                                                                 |
| django_template | 19.9 ms                                                                                                           | 22.9 ms: 1.15x slower                                                                                                 |
| genshi_text     | 13.8 ms                                                                                                           | 16.8 ms: 1.22x slower                                                                                                 |
| genshi_xml      | 30.1 ms                                                                                                           | 42.4 ms: 1.41x slower                                                                                                 |
| Geometric mean  | (ref)                                                                                                             | 1.16x slower                                                                                                          |

All benchmarks:
===============

| Benchmark                        | results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json | results/bm-20241026-3.14.0a1+-f6cc7c8-JIT/bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json |
|----------------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| tomli_loads                      | 1.49 sec                                                                                                          | 1.26 sec: 1.19x faster                                                                                                |
| scimark_sor                      | 96.1 ms                                                                                                           | 87.0 ms: 1.10x faster                                                                                                 |
| mako                             | 6.97 ms                                                                                                           | 6.44 ms: 1.08x faster                                                                                                 |
| xml_etree_process                | 37.2 ms                                                                                                           | 34.8 ms: 1.07x faster                                                                                                 |
| unpickle_pure_python             | 142 us                                                                                                            | 134 us: 1.06x faster                                                                                                  |
| xml_etree_generate               | 52.3 ms                                                                                                           | 49.6 ms: 1.05x faster                                                                                                 |
| telco                            | 4.59 ms                                                                                                           | 4.45 ms: 1.03x faster                                                                                                 |
| xml_etree_iterparse              | 74.6 ms                                                                                                           | 72.8 ms: 1.02x faster                                                                                                 |
| float                            | 49.8 ms                                                                                                           | 48.7 ms: 1.02x faster                                                                                                 |
| pickle_pure_python               | 183 us                                                                                                            | 179 us: 1.02x faster                                                                                                  |
| bpe_tokeniser                    | 3.11 sec                                                                                                          | 3.05 sec: 1.02x faster                                                                                                |
| scimark_lu                       | 67.0 ms                                                                                                           | 65.8 ms: 1.02x faster                                                                                                 |
| fannkuch                         | 267 ms                                                                                                            | 263 ms: 1.02x faster                                                                                                  |
| json                             | 2.90 ms                                                                                                           | 2.86 ms: 1.01x faster                                                                                                 |
| json_dumps                       | 7.18 ms                                                                                                           | 7.13 ms: 1.01x faster                                                                                                 |
| scimark_fft                      | 192 ms                                                                                                            | 190 ms: 1.01x faster                                                                                                  |
| python_startup                   | 18.9 ms                                                                                                           | 18.8 ms: 1.00x faster                                                                                                 |
| nbody                            | 66.0 ms                                                                                                           | 65.9 ms: 1.00x faster                                                                                                 |
| regex_dna                        | 142 ms                                                                                                            | 143 ms: 1.00x slower                                                                                                  |
| coverage                         | 43.7 ms                                                                                                           | 43.9 ms: 1.00x slower                                                                                                 |
| gc_traversal                     | 2.93 ms                                                                                                           | 2.94 ms: 1.00x slower                                                                                                 |
| coroutines                       | 16.5 ms                                                                                                           | 16.6 ms: 1.00x slower                                                                                                 |
| async_tree_io_tg                 | 611 ms                                                                                                            | 613 ms: 1.00x slower                                                                                                  |
| async_tree_eager_cpu_io_mixed_tg | 335 ms                                                                                                            | 336 ms: 1.00x slower                                                                                                  |
| deepcopy_memo                    | 17.0 us                                                                                                           | 17.1 us: 1.01x slower                                                                                                 |
| create_gc_cycles                 | 1.31 ms                                                                                                           | 1.32 ms: 1.01x slower                                                                                                 |
| deepcopy_reduce                  | 1.54 us                                                                                                           | 1.55 us: 1.01x slower                                                                                                 |
| python_startup_no_site           | 14.3 ms                                                                                                           | 14.4 ms: 1.01x slower                                                                                                 |
| regex_v8                         | 16.6 ms                                                                                                           | 16.8 ms: 1.01x slower                                                                                                 |
| async_tree_none                  | 199 ms                                                                                                            | 201 ms: 1.01x slower                                                                                                  |
| async_tree_eager_cpu_io_mixed    | 359 ms                                                                                                            | 363 ms: 1.01x slower                                                                                                  |
| async_tree_eager_io_tg           | 704 ms                                                                                                            | 715 ms: 1.02x slower                                                                                                  |
| thrift                           | 419 us                                                                                                            | 426 us: 1.02x slower                                                                                                  |
| regex_effbot                     | 2.45 ms                                                                                                           | 2.48 ms: 1.02x slower                                                                                                 |
| pathlib                          | 22.0 ms                                                                                                           | 22.4 ms: 1.02x slower                                                                                                 |
| pyflate                          | 326 ms                                                                                                            | 332 ms: 1.02x slower                                                                                                  |
| async_tree_eager_tg              | 42.3 ms                                                                                                           | 43.1 ms: 1.02x slower                                                                                                 |
| async_tree_eager_memoization     | 150 ms                                                                                                            | 154 ms: 1.03x slower                                                                                                  |
| scimark_monte_carlo              | 44.2 ms                                                                                                           | 45.8 ms: 1.04x slower                                                                                                 |
| sqlalchemy_imperative            | 6.36 ms                                                                                                           | 6.59 ms: 1.04x slower                                                                                                 |
| bench_mp_pool                    | 59.9 ms                                                                                                           | 62.2 ms: 1.04x slower                                                                                                 |
| bench_thread_pool                | 453 us                                                                                                            | 474 us: 1.05x slower                                                                                                  |
| logging_format                   | 3.31 us                                                                                                           | 3.46 us: 1.05x slower                                                                                                 |
| logging_simple                   | 3.03 us                                                                                                           | 3.18 us: 1.05x slower                                                                                                 |
| mdp                              | 1.48 sec                                                                                                          | 1.56 sec: 1.05x slower                                                                                                |
| async_tree_eager                 | 61.1 ms                                                                                                           | 64.5 ms: 1.06x slower                                                                                                 |
| crypto_pyaes                     | 51.7 ms                                                                                                           | 54.6 ms: 1.06x slower                                                                                                 |
| typing_runtime_protocols         | 93.0 us                                                                                                           | 98.5 us: 1.06x slower                                                                                                 |
| dulwich_log                      | 27.6 ms                                                                                                           | 29.3 ms: 1.06x slower                                                                                                 |
| meteor_contest                   | 70.6 ms                                                                                                           | 75.2 ms: 1.06x slower                                                                                                 |
| async_generators                 | 277 ms                                                                                                            | 295 ms: 1.07x slower                                                                                                  |
| deepcopy                         | 145 us                                                                                                            | 155 us: 1.07x slower                                                                                                  |
| nqueens                          | 54.8 ms                                                                                                           | 58.8 ms: 1.07x slower                                                                                                 |
| deltablue                        | 2.24 ms                                                                                                           | 2.41 ms: 1.08x slower                                                                                                 |
| html5lib                         | 30.1 ms                                                                                                           | 32.6 ms: 1.08x slower                                                                                                 |
| pycparser                        | 635 ms                                                                                                            | 689 ms: 1.08x slower                                                                                                  |
| pprint_pformat                   | 935 ms                                                                                                            | 1.02 sec: 1.09x slower                                                                                                |
| richards_super                   | 34.6 ms                                                                                                           | 37.8 ms: 1.09x slower                                                                                                 |
| richards                         | 31.1 ms                                                                                                           | 34.0 ms: 1.09x slower                                                                                                 |
| pprint_safe_repr                 | 459 ms                                                                                                            | 502 ms: 1.09x slower                                                                                                  |
| sympy_expand                     | 226 ms                                                                                                            | 249 ms: 1.10x slower                                                                                                  |
| sqlalchemy_declarative           | 56.0 ms                                                                                                           | 61.8 ms: 1.10x slower                                                                                                 |
| regex_compile                    | 68.1 ms                                                                                                           | 75.3 ms: 1.11x slower                                                                                                 |
| docutils                         | 1.40 sec                                                                                                          | 1.57 sec: 1.12x slower                                                                                                |
| sqlglot_normalize                | 166 ms                                                                                                            | 187 ms: 1.12x slower                                                                                                  |
| raytrace                         | 154 ms                                                                                                            | 173 ms: 1.12x slower                                                                                                  |
| scimark_sparse_mat_mult          | 2.82 ms                                                                                                           | 3.18 ms: 1.13x slower                                                                                                 |
| sympy_str                        | 134 ms                                                                                                            | 152 ms: 1.13x slower                                                                                                  |
| chaos                            | 36.8 ms                                                                                                           | 41.9 ms: 1.14x slower                                                                                                 |
| sympy_integrate                  | 11.0 ms                                                                                                           | 12.6 ms: 1.15x slower                                                                                                 |
| sympy_sum                        | 69.8 ms                                                                                                           | 80.2 ms: 1.15x slower                                                                                                 |
| 2to3                             | 160 ms                                                                                                            | 184 ms: 1.15x slower                                                                                                  |
| django_template                  | 19.9 ms                                                                                                           | 22.9 ms: 1.15x slower                                                                                                 |
| sphinx                           | 576 ms                                                                                                            | 665 ms: 1.15x slower                                                                                                  |
| logging_silent                   | 60.9 ns                                                                                                           | 70.9 ns: 1.16x slower                                                                                                 |
| comprehensions                   | 11.4 us                                                                                                           | 13.3 us: 1.17x slower                                                                                                 |
| sqlglot_parse                    | 746 us                                                                                                            | 880 us: 1.18x slower                                                                                                  |
| sqlglot_transpile                | 902 us                                                                                                            | 1.07 ms: 1.18x slower                                                                                                 |
| go                               | 82.4 ms                                                                                                           | 98.8 ms: 1.20x slower                                                                                                 |
| pylint                           | 179 ms                                                                                                            | 215 ms: 1.20x slower                                                                                                  |
| hexiom                           | 4.13 ms                                                                                                           | 5.00 ms: 1.21x slower                                                                                                 |
| sqlglot_optimize                 | 31.1 ms                                                                                                           | 37.7 ms: 1.21x slower                                                                                                 |
| genshi_text                      | 13.8 ms                                                                                                           | 16.8 ms: 1.22x slower                                                                                                 |
| generators                       | 20.1 ms                                                                                                           | 25.3 ms: 1.26x slower                                                                                                 |
| genshi_xml                       | 30.1 ms                                                                                                           | 42.4 ms: 1.41x slower                                                                                                 |
| Geometric mean                   | (ref)                                                                                                             | 1.05x slower                                                                                                          |

Benchmark hidden because not significant (14): async_tree_memoization, async_tree_none_tg, async_tree_memoization_tg, asyncio_websockets, async_tree_io, json_loads, xml_etree_parse, pidigits, spectral_norm, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_eager_memoization_tg, async_tree_eager_io, tornado_http

- Geometric mean (including insignificant results): 1.046x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.08x