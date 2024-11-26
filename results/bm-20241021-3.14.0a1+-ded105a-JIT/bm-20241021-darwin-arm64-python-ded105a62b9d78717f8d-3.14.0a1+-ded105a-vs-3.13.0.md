# Results vs. 3.13.0

- fork: python
- ref: ded105a62b9d78717f8d
- machine: darwin-arm64
- commit hash: ded105a
- commit date: 2024-10-21
- overall geometric mean: 1.040x faster
- HPT reliability: 99.75%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 182 ms: 1.03x faster                                                   |
| docutils       | 1.44 sec                                               | 1.55 sec: 1.08x slower                                                 |
| html5lib       | 36.6 ms                                                | 32.1 ms: 1.14x faster                                                  |
| sphinx         | 603 ms                                                 | 661 ms: 1.10x slower                                                   |
| Geometric mean | (ref)                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 235 ms: 1.23x faster                                                   |
| coroutines                       | 19.8 ms                                                | 16.4 ms: 1.20x faster                                                  |
| async_tree_eager_tg              | 47.8 ms                                                | 43.0 ms: 1.11x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 153 ms: 1.10x faster                                                   |
| async_tree_eager                 | 70.1 ms                                                | 63.9 ms: 1.10x faster                                                  |
| async_tree_none                  | 215 ms                                                 | 199 ms: 1.08x faster                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 130 ms: 1.06x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 337 ms: 1.03x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 364 ms: 1.02x faster                                                   |
| async_generators                 | 295 ms                                                 | 292 ms: 1.01x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 469 ms: 1.05x slower                                                   |
| async_tree_none_tg               | 198 ms                                                 | 213 ms: 1.07x slower                                                   |
| async_tree_io                    | 507 ms                                                 | 581 ms: 1.15x slower                                                   |
| async_tree_io_tg                 | 497 ms                                                 | 609 ms: 1.23x slower                                                   |
| async_tree_eager_io              | 514 ms                                                 | 676 ms: 1.32x slower                                                   |
| async_tree_eager_io_tg           | 477 ms                                                 | 714 ms: 1.50x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (3): async_tree_memoization, async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 56.0 ms                                                | 48.2 ms: 1.16x faster                                                  |
| nbody          | 74.0 ms                                                | 65.7 ms: 1.13x faster                                                  |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 78.6 ms                                                | 74.5 ms: 1.06x faster                                                  |
| regex_effbot   | 2.63 ms                                                | 2.50 ms: 1.05x faster                                                  |
| regex_dna      | 149 ms                                                 | 143 ms: 1.05x faster                                                   |
| regex_v8       | 17.0 ms                                                | 16.8 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.25 sec: 1.26x faster                                                 |
| unpickle_pure_python | 164 us                                                 | 133 us: 1.24x faster                                                   |
| pickle_pure_python   | 214 us                                                 | 179 us: 1.20x faster                                                   |
| xml_etree_process    | 41.0 ms                                                | 34.6 ms: 1.19x faster                                                  |
| xml_etree_generate   | 57.0 ms                                                | 50.4 ms: 1.13x faster                                                  |
| xml_etree_iterparse  | 73.6 ms                                                | 72.2 ms: 1.02x faster                                                  |
| json_loads           | 17.0 us                                                | 16.7 us: 1.02x faster                                                  |
| json_dumps           | 6.52 ms                                                | 7.15 ms: 1.10x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 18.9 ms                                                | 19.1 ms: 1.01x slower                                                  |
| python_startup_no_site | 14.5 ms                                                | 15.1 ms: 1.04x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.49 ms: 1.18x faster                                                  |
| genshi_text     | 16.9 ms                                                | 16.6 ms: 1.02x faster                                                  |
| django_template | 22.2 ms                                                | 22.7 ms: 1.02x slower                                                  |
| genshi_xml      | 34.4 ms                                                | 41.7 ms: 1.21x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy_memo                    | 27.4 us                                                | 16.8 us: 1.63x faster                                                  |
| deepcopy                         | 237 us                                                 | 153 us: 1.55x faster                                                   |
| deepcopy_reduce                  | 2.07 us                                                | 1.54 us: 1.34x faster                                                  |
| tomli_loads                      | 1.57 sec                                               | 1.25 sec: 1.26x faster                                                 |
| generators                       | 31.5 ms                                                | 25.5 ms: 1.24x faster                                                  |
| unpickle_pure_python             | 164 us                                                 | 133 us: 1.24x faster                                                   |
| scimark_sor                      | 105 ms                                                 | 85.9 ms: 1.23x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 235 ms: 1.23x faster                                                   |
| coroutines                       | 19.8 ms                                                | 16.4 ms: 1.20x faster                                                  |
| pickle_pure_python               | 214 us                                                 | 179 us: 1.20x faster                                                   |
| xml_etree_process                | 41.0 ms                                                | 34.6 ms: 1.19x faster                                                  |
| mako                             | 7.68 ms                                                | 6.49 ms: 1.18x faster                                                  |
| go                               | 115 ms                                                 | 98.5 ms: 1.17x faster                                                  |
| scimark_lu                       | 76.7 ms                                                | 65.7 ms: 1.17x faster                                                  |
| float                            | 56.0 ms                                                | 48.2 ms: 1.16x faster                                                  |
| logging_simple                   | 3.60 us                                                | 3.11 us: 1.16x faster                                                  |
| logging_format                   | 3.89 us                                                | 3.39 us: 1.15x faster                                                  |
| html5lib                         | 36.6 ms                                                | 32.1 ms: 1.14x faster                                                  |
| xml_etree_generate               | 57.0 ms                                                | 50.4 ms: 1.13x faster                                                  |
| nbody                            | 74.0 ms                                                | 65.7 ms: 1.13x faster                                                  |
| deltablue                        | 2.68 ms                                                | 2.39 ms: 1.12x faster                                                  |
| async_tree_eager_tg              | 47.8 ms                                                | 43.0 ms: 1.11x faster                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 45.5 ms: 1.11x faster                                                  |
| fannkuch                         | 284 ms                                                 | 257 ms: 1.10x faster                                                   |
| thrift                           | 466 us                                                 | 422 us: 1.10x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 153 ms: 1.10x faster                                                   |
| async_tree_eager                 | 70.1 ms                                                | 63.9 ms: 1.10x faster                                                  |
| spectral_norm                    | 76.3 ms                                                | 69.5 ms: 1.10x faster                                                  |
| pyflate                          | 351 ms                                                 | 324 ms: 1.08x faster                                                   |
| async_tree_none                  | 215 ms                                                 | 199 ms: 1.08x faster                                                   |
| pprint_pformat                   | 1.08 sec                                               | 1.00 sec: 1.08x faster                                                 |
| richards                         | 35.2 ms                                                | 32.9 ms: 1.07x faster                                                  |
| raytrace                         | 181 ms                                                 | 169 ms: 1.07x faster                                                   |
| bpe_tokeniser                    | 3.25 sec                                               | 3.05 sec: 1.07x faster                                                 |
| richards_super                   | 39.1 ms                                                | 36.7 ms: 1.06x faster                                                  |
| pprint_safe_repr                 | 533 ms                                                 | 501 ms: 1.06x faster                                                   |
| nqueens                          | 62.5 ms                                                | 58.9 ms: 1.06x faster                                                  |
| bench_thread_pool                | 505 us                                                 | 475 us: 1.06x faster                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 130 ms: 1.06x faster                                                   |
| regex_compile                    | 78.6 ms                                                | 74.5 ms: 1.06x faster                                                  |
| json                             | 3.03 ms                                                | 2.88 ms: 1.05x faster                                                  |
| scimark_fft                      | 201 ms                                                 | 191 ms: 1.05x faster                                                   |
| regex_effbot                     | 2.63 ms                                                | 2.50 ms: 1.05x faster                                                  |
| telco                            | 4.76 ms                                                | 4.56 ms: 1.05x faster                                                  |
| regex_dna                        | 149 ms                                                 | 143 ms: 1.05x faster                                                   |
| coverage                         | 46.0 ms                                                | 44.1 ms: 1.04x faster                                                  |
| pycparser                        | 705 ms                                                 | 677 ms: 1.04x faster                                                   |
| pathlib                          | 23.4 ms                                                | 22.5 ms: 1.04x faster                                                  |
| typing_runtime_protocols         | 101 us                                                 | 97.5 us: 1.04x faster                                                  |
| 2to3                             | 187 ms                                                 | 182 ms: 1.03x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 337 ms: 1.03x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 364 ms: 1.02x faster                                                   |
| sqlglot_normalize                | 189 ms                                                 | 185 ms: 1.02x faster                                                   |
| xml_etree_iterparse              | 73.6 ms                                                | 72.2 ms: 1.02x faster                                                  |
| genshi_text                      | 16.9 ms                                                | 16.6 ms: 1.02x faster                                                  |
| json_loads                       | 17.0 us                                                | 16.7 us: 1.02x faster                                                  |
| regex_v8                         | 17.0 ms                                                | 16.8 ms: 1.01x faster                                                  |
| bench_mp_pool                    | 62.5 ms                                                | 61.8 ms: 1.01x faster                                                  |
| async_generators                 | 295 ms                                                 | 292 ms: 1.01x faster                                                   |
| crypto_pyaes                     | 54.2 ms                                                | 53.9 ms: 1.01x faster                                                  |
| logging_silent                   | 70.1 ns                                                | 69.9 ns: 1.00x faster                                                  |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                                   |
| chaos                            | 41.2 ms                                                | 41.3 ms: 1.00x slower                                                  |
| sqlglot_parse                    | 856 us                                                 | 862 us: 1.01x slower                                                   |
| gc_traversal                     | 2.91 ms                                                | 2.94 ms: 1.01x slower                                                  |
| python_startup                   | 18.9 ms                                                | 19.1 ms: 1.01x slower                                                  |
| meteor_contest                   | 74.0 ms                                                | 75.1 ms: 1.02x slower                                                  |
| dulwich_log                      | 28.5 ms                                                | 29.0 ms: 1.02x slower                                                  |
| django_template                  | 22.2 ms                                                | 22.7 ms: 1.02x slower                                                  |
| hexiom                           | 4.86 ms                                                | 4.99 ms: 1.03x slower                                                  |
| sqlglot_transpile                | 1.02 ms                                                | 1.05 ms: 1.03x slower                                                  |
| sympy_str                        | 145 ms                                                 | 150 ms: 1.03x slower                                                   |
| mdp                              | 1.49 sec                                               | 1.55 sec: 1.04x slower                                                 |
| python_startup_no_site           | 14.5 ms                                                | 15.1 ms: 1.04x slower                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 469 ms: 1.05x slower                                                   |
| sympy_sum                        | 75.4 ms                                                | 79.6 ms: 1.06x slower                                                  |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 3.16 ms: 1.06x slower                                                  |
| sqlglot_optimize                 | 34.9 ms                                                | 37.0 ms: 1.06x slower                                                  |
| comprehensions                   | 12.3 us                                                | 13.1 us: 1.07x slower                                                  |
| async_tree_none_tg               | 198 ms                                                 | 213 ms: 1.07x slower                                                   |
| docutils                         | 1.44 sec                                               | 1.55 sec: 1.08x slower                                                 |
| json_dumps                       | 6.52 ms                                                | 7.15 ms: 1.10x slower                                                  |
| sphinx                           | 603 ms                                                 | 661 ms: 1.10x slower                                                   |
| sympy_integrate                  | 11.3 ms                                                | 12.5 ms: 1.11x slower                                                  |
| create_gc_cycles                 | 1.17 ms                                                | 1.31 ms: 1.12x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 581 ms: 1.15x slower                                                   |
| genshi_xml                       | 34.4 ms                                                | 41.7 ms: 1.21x slower                                                  |
| async_tree_io_tg                 | 497 ms                                                 | 609 ms: 1.23x slower                                                   |
| async_tree_eager_io              | 514 ms                                                 | 676 ms: 1.32x slower                                                   |
| async_tree_eager_io_tg           | 477 ms                                                 | 714 ms: 1.50x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (7): tornado_http, async_tree_memoization, pylint, xml_etree_parse, async_tree_cpu_io_mixed, asyncio_websockets, sympy_expand
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dask, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.040x faster
# HPT report

- Reliability score: 99.75% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.10x