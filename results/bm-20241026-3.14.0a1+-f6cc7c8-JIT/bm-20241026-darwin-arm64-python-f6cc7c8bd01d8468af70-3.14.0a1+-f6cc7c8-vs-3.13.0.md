# Results vs. 3.13.0

- fork: python
- ref: f6cc7c8bd01d8468af70
- machine: darwin-arm64
- commit hash: f6cc7c8
- commit date: 2024-10-26
- overall geometric mean: 1.033x faster
- HPT reliability: 99.43%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 184 ms: 1.02x faster                                                   |
| docutils       | 1.44 sec                                               | 1.57 sec: 1.09x slower                                                 |
| html5lib       | 36.6 ms                                                | 32.6 ms: 1.12x faster                                                  |
| sphinx         | 603 ms                                                 | 665 ms: 1.10x slower                                                   |
| Geometric mean | (ref)                                                  | 1.02x slower                                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 235 ms: 1.22x faster                                                   |
| coroutines                       | 19.8 ms                                                | 16.6 ms: 1.19x faster                                                  |
| async_tree_eager_tg              | 47.8 ms                                                | 43.1 ms: 1.11x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 154 ms: 1.09x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 245 ms: 1.09x faster                                                   |
| async_tree_eager                 | 70.1 ms                                                | 64.5 ms: 1.09x faster                                                  |
| async_tree_none                  | 215 ms                                                 | 201 ms: 1.07x faster                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 131 ms: 1.05x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 336 ms: 1.03x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 363 ms: 1.03x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 472 ms: 1.05x slower                                                   |
| async_tree_none_tg               | 198 ms                                                 | 214 ms: 1.08x slower                                                   |
| async_tree_io                    | 507 ms                                                 | 582 ms: 1.15x slower                                                   |
| async_tree_io_tg                 | 497 ms                                                 | 613 ms: 1.23x slower                                                   |
| async_tree_eager_io              | 514 ms                                                 | 671 ms: 1.30x slower                                                   |
| async_tree_eager_io_tg           | 477 ms                                                 | 715 ms: 1.50x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (3): asyncio_websockets, async_tree_cpu_io_mixed, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 56.0 ms                                                | 48.7 ms: 1.15x faster                                                  |
| nbody          | 74.0 ms                                                | 65.9 ms: 1.12x faster                                                  |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.48 ms: 1.06x faster                                                  |
| regex_dna      | 149 ms                                                 | 143 ms: 1.05x faster                                                   |
| regex_compile  | 78.6 ms                                                | 75.3 ms: 1.04x faster                                                  |
| regex_v8       | 17.0 ms                                                | 16.8 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.26 sec: 1.25x faster                                                 |
| unpickle_pure_python | 164 us                                                 | 134 us: 1.22x faster                                                   |
| pickle_pure_python   | 214 us                                                 | 179 us: 1.20x faster                                                   |
| xml_etree_process    | 41.0 ms                                                | 34.8 ms: 1.18x faster                                                  |
| xml_etree_generate   | 57.0 ms                                                | 49.6 ms: 1.15x faster                                                  |
| json_loads           | 17.0 us                                                | 16.6 us: 1.02x faster                                                  |
| xml_etree_iterparse  | 73.6 ms                                                | 72.8 ms: 1.01x faster                                                  |
| json_dumps           | 6.52 ms                                                | 7.13 ms: 1.09x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup | 18.9 ms                                                | 18.8 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.44 ms: 1.19x faster                                                  |
| django_template | 22.2 ms                                                | 22.9 ms: 1.03x slower                                                  |
| genshi_xml      | 34.4 ms                                                | 42.4 ms: 1.23x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                           |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy_memo                    | 27.4 us                                                | 17.1 us: 1.60x faster                                                  |
| deepcopy                         | 237 us                                                 | 155 us: 1.53x faster                                                   |
| deepcopy_reduce                  | 2.07 us                                                | 1.55 us: 1.34x faster                                                  |
| generators                       | 31.5 ms                                                | 25.3 ms: 1.25x faster                                                  |
| tomli_loads                      | 1.57 sec                                               | 1.26 sec: 1.25x faster                                                 |
| async_tree_memoization_tg        | 288 ms                                                 | 235 ms: 1.22x faster                                                   |
| unpickle_pure_python             | 164 us                                                 | 134 us: 1.22x faster                                                   |
| scimark_sor                      | 105 ms                                                 | 87.0 ms: 1.21x faster                                                  |
| pickle_pure_python               | 214 us                                                 | 179 us: 1.20x faster                                                   |
| mako                             | 7.68 ms                                                | 6.44 ms: 1.19x faster                                                  |
| coroutines                       | 19.8 ms                                                | 16.6 ms: 1.19x faster                                                  |
| xml_etree_process                | 41.0 ms                                                | 34.8 ms: 1.18x faster                                                  |
| scimark_lu                       | 76.7 ms                                                | 65.8 ms: 1.17x faster                                                  |
| go                               | 115 ms                                                 | 98.8 ms: 1.16x faster                                                  |
| float                            | 56.0 ms                                                | 48.7 ms: 1.15x faster                                                  |
| xml_etree_generate               | 57.0 ms                                                | 49.6 ms: 1.15x faster                                                  |
| logging_simple                   | 3.60 us                                                | 3.18 us: 1.14x faster                                                  |
| logging_format                   | 3.89 us                                                | 3.46 us: 1.13x faster                                                  |
| nbody                            | 74.0 ms                                                | 65.9 ms: 1.12x faster                                                  |
| html5lib                         | 36.6 ms                                                | 32.6 ms: 1.12x faster                                                  |
| deltablue                        | 2.68 ms                                                | 2.41 ms: 1.11x faster                                                  |
| async_tree_eager_tg              | 47.8 ms                                                | 43.1 ms: 1.11x faster                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 45.8 ms: 1.10x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 154 ms: 1.09x faster                                                   |
| thrift                           | 466 us                                                 | 426 us: 1.09x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 245 ms: 1.09x faster                                                   |
| spectral_norm                    | 76.3 ms                                                | 70.1 ms: 1.09x faster                                                  |
| async_tree_eager                 | 70.1 ms                                                | 64.5 ms: 1.09x faster                                                  |
| fannkuch                         | 284 ms                                                 | 263 ms: 1.08x faster                                                   |
| async_tree_none                  | 215 ms                                                 | 201 ms: 1.07x faster                                                   |
| telco                            | 4.76 ms                                                | 4.45 ms: 1.07x faster                                                  |
| pprint_pformat                   | 1.08 sec                                               | 1.02 sec: 1.07x faster                                                 |
| bpe_tokeniser                    | 3.25 sec                                               | 3.05 sec: 1.07x faster                                                 |
| bench_thread_pool                | 505 us                                                 | 474 us: 1.06x faster                                                   |
| nqueens                          | 62.5 ms                                                | 58.8 ms: 1.06x faster                                                  |
| pprint_safe_repr                 | 533 ms                                                 | 502 ms: 1.06x faster                                                   |
| json                             | 3.03 ms                                                | 2.86 ms: 1.06x faster                                                  |
| pyflate                          | 351 ms                                                 | 332 ms: 1.06x faster                                                   |
| regex_effbot                     | 2.63 ms                                                | 2.48 ms: 1.06x faster                                                  |
| scimark_fft                      | 201 ms                                                 | 190 ms: 1.05x faster                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 131 ms: 1.05x faster                                                   |
| coverage                         | 46.0 ms                                                | 43.9 ms: 1.05x faster                                                  |
| raytrace                         | 181 ms                                                 | 173 ms: 1.05x faster                                                   |
| regex_dna                        | 149 ms                                                 | 143 ms: 1.05x faster                                                   |
| regex_compile                    | 78.6 ms                                                | 75.3 ms: 1.04x faster                                                  |
| pathlib                          | 23.4 ms                                                | 22.4 ms: 1.04x faster                                                  |
| richards_super                   | 39.1 ms                                                | 37.8 ms: 1.03x faster                                                  |
| richards                         | 35.2 ms                                                | 34.0 ms: 1.03x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 336 ms: 1.03x faster                                                   |
| typing_runtime_protocols         | 101 us                                                 | 98.5 us: 1.03x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 363 ms: 1.03x faster                                                   |
| json_loads                       | 17.0 us                                                | 16.6 us: 1.02x faster                                                  |
| pycparser                        | 705 ms                                                 | 689 ms: 1.02x faster                                                   |
| 2to3                             | 187 ms                                                 | 184 ms: 1.02x faster                                                   |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.59 ms: 1.01x faster                                                  |
| regex_v8                         | 17.0 ms                                                | 16.8 ms: 1.01x faster                                                  |
| sqlglot_normalize                | 189 ms                                                 | 187 ms: 1.01x faster                                                   |
| xml_etree_iterparse              | 73.6 ms                                                | 72.8 ms: 1.01x faster                                                  |
| bench_mp_pool                    | 62.5 ms                                                | 62.2 ms: 1.01x faster                                                  |
| python_startup                   | 18.9 ms                                                | 18.8 ms: 1.01x faster                                                  |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                                   |
| crypto_pyaes                     | 54.2 ms                                                | 54.6 ms: 1.01x slower                                                  |
| gc_traversal                     | 2.91 ms                                                | 2.94 ms: 1.01x slower                                                  |
| sympy_expand                     | 246 ms                                                 | 249 ms: 1.01x slower                                                   |
| logging_silent                   | 70.1 ns                                                | 70.9 ns: 1.01x slower                                                  |
| chaos                            | 41.2 ms                                                | 41.9 ms: 1.02x slower                                                  |
| meteor_contest                   | 74.0 ms                                                | 75.2 ms: 1.02x slower                                                  |
| dulwich_log                      | 28.5 ms                                                | 29.3 ms: 1.03x slower                                                  |
| hexiom                           | 4.86 ms                                                | 5.00 ms: 1.03x slower                                                  |
| sqlglot_parse                    | 856 us                                                 | 880 us: 1.03x slower                                                   |
| django_template                  | 22.2 ms                                                | 22.9 ms: 1.03x slower                                                  |
| mdp                              | 1.49 sec                                               | 1.56 sec: 1.04x slower                                                 |
| sympy_str                        | 145 ms                                                 | 152 ms: 1.04x slower                                                   |
| sqlglot_transpile                | 1.02 ms                                                | 1.07 ms: 1.04x slower                                                  |
| sqlalchemy_declarative           | 58.9 ms                                                | 61.8 ms: 1.05x slower                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 472 ms: 1.05x slower                                                   |
| sympy_sum                        | 75.4 ms                                                | 80.2 ms: 1.06x slower                                                  |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 3.18 ms: 1.06x slower                                                  |
| sqlglot_optimize                 | 34.9 ms                                                | 37.7 ms: 1.08x slower                                                  |
| async_tree_none_tg               | 198 ms                                                 | 214 ms: 1.08x slower                                                   |
| comprehensions                   | 12.3 us                                                | 13.3 us: 1.09x slower                                                  |
| docutils                         | 1.44 sec                                               | 1.57 sec: 1.09x slower                                                 |
| json_dumps                       | 6.52 ms                                                | 7.13 ms: 1.09x slower                                                  |
| sphinx                           | 603 ms                                                 | 665 ms: 1.10x slower                                                   |
| sympy_integrate                  | 11.3 ms                                                | 12.6 ms: 1.12x slower                                                  |
| create_gc_cycles                 | 1.17 ms                                                | 1.32 ms: 1.13x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 582 ms: 1.15x slower                                                   |
| pylint                           | 180 ms                                                 | 215 ms: 1.20x slower                                                   |
| genshi_xml                       | 34.4 ms                                                | 42.4 ms: 1.23x slower                                                  |
| async_tree_io_tg                 | 497 ms                                                 | 613 ms: 1.23x slower                                                   |
| async_tree_eager_io              | 514 ms                                                 | 671 ms: 1.30x slower                                                   |
| async_tree_eager_io_tg           | 477 ms                                                 | 715 ms: 1.50x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (7): python_startup_no_site, genshi_text, asyncio_websockets, async_tree_cpu_io_mixed, async_generators, xml_etree_parse, tornado_http
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dask, gevent_hub, k_core, mypy2, shortest_path

- Geometric mean (including insignificant results): 1.033x faster
# HPT report

- Reliability score: 99.43% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.10x