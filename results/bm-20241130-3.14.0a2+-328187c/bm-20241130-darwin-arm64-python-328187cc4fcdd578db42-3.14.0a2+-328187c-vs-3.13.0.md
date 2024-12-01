# Results vs. 3.13.0

- fork: python
- ref: 328187cc4fcdd578db42
- machine: darwin-arm64
- commit hash: 328187c
- commit date: 2024-11-30
- overall geometric mean: 1.041x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 169 ms: 1.11x faster                                                   |
| html5lib       | 36.6 ms                                                | 31.3 ms: 1.17x faster                                                  |
| sphinx         | 603 ms                                                 | 592 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 256 ms: 1.13x faster                                                   |
| coroutines                       | 19.8 ms                                                | 17.6 ms: 1.12x faster                                                  |
| async_tree_eager                 | 70.1 ms                                                | 63.8 ms: 1.10x faster                                                  |
| async_tree_eager_tg              | 47.8 ms                                                | 44.5 ms: 1.07x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 253 ms: 1.06x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 160 ms: 1.05x faster                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 131 ms: 1.05x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 360 ms: 1.03x faster                                                   |
| async_generators                 | 295 ms                                                 | 287 ms: 1.03x faster                                                   |
| async_tree_none                  | 215 ms                                                 | 211 ms: 1.02x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 342 ms: 1.01x faster                                                   |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 472 ms: 1.03x slower                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 476 ms: 1.06x slower                                                   |
| async_tree_io                    | 507 ms                                                 | 611 ms: 1.21x slower                                                   |
| async_tree_io_tg                 | 497 ms                                                 | 608 ms: 1.22x slower                                                   |
| async_tree_eager_io              | 514 ms                                                 | 715 ms: 1.39x slower                                                   |
| async_tree_eager_io_tg           | 477 ms                                                 | 706 ms: 1.48x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.03x slower                                                           |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 74.0 ms                                                | 68.6 ms: 1.08x faster                                                  |
| float          | 56.0 ms                                                | 53.3 ms: 1.05x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.08 ms: 1.26x faster                                                  |
| regex_dna      | 149 ms                                                 | 134 ms: 1.11x faster                                                   |
| regex_compile  | 78.6 ms                                                | 72.1 ms: 1.09x faster                                                  |
| regex_v8       | 17.0 ms                                                | 15.9 ms: 1.07x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 164 us                                                 | 154 us: 1.07x faster                                                   |
| xml_etree_generate   | 57.0 ms                                                | 54.3 ms: 1.05x faster                                                  |
| xml_etree_process    | 41.0 ms                                                | 39.2 ms: 1.04x faster                                                  |
| pickle_pure_python   | 214 us                                                 | 207 us: 1.04x faster                                                   |
| tomli_loads          | 1.57 sec                                               | 1.53 sec: 1.02x faster                                                 |
| json_loads           | 17.0 us                                                | 16.6 us: 1.02x faster                                                  |
| xml_etree_parse      | 107 ms                                                 | 109 ms: 1.02x slower                                                   |
| xml_etree_iterparse  | 73.6 ms                                                | 76.9 ms: 1.05x slower                                                  |
| json_dumps           | 6.52 ms                                                | 7.28 ms: 1.12x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 14.5 ms                                                | 15.5 ms: 1.07x slower                                                  |
| python_startup         | 18.9 ms                                                | 20.3 ms: 1.07x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 14.4 ms: 1.17x faster                                                  |
| genshi_xml      | 34.4 ms                                                | 31.0 ms: 1.11x faster                                                  |
| mako            | 7.68 ms                                                | 7.13 ms: 1.08x faster                                                  |
| django_template | 22.2 ms                                                | 20.8 ms: 1.07x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy                         | 237 us                                                 | 152 us: 1.56x faster                                                   |
| deepcopy_memo                    | 27.4 us                                                | 18.2 us: 1.50x faster                                                  |
| generators                       | 31.5 ms                                                | 22.5 ms: 1.40x faster                                                  |
| go                               | 115 ms                                                 | 87.6 ms: 1.31x faster                                                  |
| deepcopy_reduce                  | 2.07 us                                                | 1.59 us: 1.30x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.08 ms: 1.26x faster                                                  |
| pylint                           | 180 ms                                                 | 152 ms: 1.19x faster                                                   |
| genshi_text                      | 16.9 ms                                                | 14.4 ms: 1.17x faster                                                  |
| html5lib                         | 36.6 ms                                                | 31.3 ms: 1.17x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 256 ms: 1.13x faster                                                   |
| coroutines                       | 19.8 ms                                                | 17.6 ms: 1.12x faster                                                  |
| regex_dna                        | 149 ms                                                 | 134 ms: 1.11x faster                                                   |
| genshi_xml                       | 34.4 ms                                                | 31.0 ms: 1.11x faster                                                  |
| 2to3                             | 187 ms                                                 | 169 ms: 1.11x faster                                                   |
| pprint_safe_repr                 | 533 ms                                                 | 484 ms: 1.10x faster                                                   |
| pprint_pformat                   | 1.08 sec                                               | 984 ms: 1.10x faster                                                   |
| async_tree_eager                 | 70.1 ms                                                | 63.8 ms: 1.10x faster                                                  |
| logging_simple                   | 3.60 us                                                | 3.29 us: 1.10x faster                                                  |
| regex_compile                    | 78.6 ms                                                | 72.1 ms: 1.09x faster                                                  |
| deltablue                        | 2.68 ms                                                | 2.47 ms: 1.08x faster                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 46.5 ms: 1.08x faster                                                  |
| logging_format                   | 3.89 us                                                | 3.59 us: 1.08x faster                                                  |
| nbody                            | 74.0 ms                                                | 68.6 ms: 1.08x faster                                                  |
| thrift                           | 466 us                                                 | 433 us: 1.08x faster                                                   |
| mako                             | 7.68 ms                                                | 7.13 ms: 1.08x faster                                                  |
| async_tree_eager_tg              | 47.8 ms                                                | 44.5 ms: 1.07x faster                                                  |
| pycparser                        | 705 ms                                                 | 658 ms: 1.07x faster                                                   |
| hexiom                           | 4.86 ms                                                | 4.55 ms: 1.07x faster                                                  |
| regex_v8                         | 17.0 ms                                                | 15.9 ms: 1.07x faster                                                  |
| django_template                  | 22.2 ms                                                | 20.8 ms: 1.07x faster                                                  |
| unpickle_pure_python             | 164 us                                                 | 154 us: 1.07x faster                                                   |
| bench_thread_pool                | 505 us                                                 | 475 us: 1.06x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 253 ms: 1.06x faster                                                   |
| sqlglot_optimize                 | 34.9 ms                                                | 33.0 ms: 1.06x faster                                                  |
| scimark_lu                       | 76.7 ms                                                | 72.4 ms: 1.06x faster                                                  |
| nqueens                          | 62.5 ms                                                | 59.1 ms: 1.06x faster                                                  |
| sqlglot_parse                    | 856 us                                                 | 808 us: 1.06x faster                                                   |
| json                             | 3.03 ms                                                | 2.87 ms: 1.06x faster                                                  |
| raytrace                         | 181 ms                                                 | 171 ms: 1.06x faster                                                   |
| richards_super                   | 39.1 ms                                                | 37.0 ms: 1.06x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 160 ms: 1.05x faster                                                   |
| fannkuch                         | 284 ms                                                 | 269 ms: 1.05x faster                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 131 ms: 1.05x faster                                                   |
| float                            | 56.0 ms                                                | 53.3 ms: 1.05x faster                                                  |
| xml_etree_generate               | 57.0 ms                                                | 54.3 ms: 1.05x faster                                                  |
| richards                         | 35.2 ms                                                | 33.5 ms: 1.05x faster                                                  |
| spectral_norm                    | 76.3 ms                                                | 72.7 ms: 1.05x faster                                                  |
| scimark_sor                      | 105 ms                                                 | 101 ms: 1.05x faster                                                   |
| sqlglot_normalize                | 189 ms                                                 | 181 ms: 1.05x faster                                                   |
| chaos                            | 41.2 ms                                                | 39.4 ms: 1.05x faster                                                  |
| xml_etree_process                | 41.0 ms                                                | 39.2 ms: 1.04x faster                                                  |
| sympy_expand                     | 246 ms                                                 | 236 ms: 1.04x faster                                                   |
| coverage                         | 46.0 ms                                                | 44.2 ms: 1.04x faster                                                  |
| sqlglot_transpile                | 1.02 ms                                                | 983 us: 1.04x faster                                                   |
| telco                            | 4.76 ms                                                | 4.58 ms: 1.04x faster                                                  |
| pyflate                          | 351 ms                                                 | 338 ms: 1.04x faster                                                   |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.44 ms: 1.04x faster                                                  |
| pathlib                          | 23.4 ms                                                | 22.5 ms: 1.04x faster                                                  |
| pickle_pure_python               | 214 us                                                 | 207 us: 1.04x faster                                                   |
| sympy_str                        | 145 ms                                                 | 140 ms: 1.04x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 360 ms: 1.03x faster                                                   |
| sympy_sum                        | 75.4 ms                                                | 73.0 ms: 1.03x faster                                                  |
| scimark_fft                      | 201 ms                                                 | 195 ms: 1.03x faster                                                   |
| typing_runtime_protocols         | 101 us                                                 | 98.2 us: 1.03x faster                                                  |
| async_generators                 | 295 ms                                                 | 287 ms: 1.03x faster                                                   |
| tomli_loads                      | 1.57 sec                                               | 1.53 sec: 1.02x faster                                                 |
| json_loads                       | 17.0 us                                                | 16.6 us: 1.02x faster                                                  |
| async_tree_none                  | 215 ms                                                 | 211 ms: 1.02x faster                                                   |
| meteor_contest                   | 74.0 ms                                                | 72.4 ms: 1.02x faster                                                  |
| bpe_tokeniser                    | 3.25 sec                                               | 3.18 sec: 1.02x faster                                                 |
| sphinx                           | 603 ms                                                 | 592 ms: 1.02x faster                                                   |
| dulwich_log                      | 28.5 ms                                                | 28.1 ms: 1.02x faster                                                  |
| bench_mp_pool                    | 62.5 ms                                                | 61.7 ms: 1.01x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 342 ms: 1.01x faster                                                   |
| shortest_path                    | 347 ms                                                 | 345 ms: 1.01x faster                                                   |
| sqlalchemy_declarative           | 58.9 ms                                                | 58.6 ms: 1.00x faster                                                  |
| connected_components             | 319 ms                                                 | 320 ms: 1.00x slower                                                   |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 3.03 ms: 1.01x slower                                                  |
| gc_traversal                     | 2.91 ms                                                | 2.95 ms: 1.01x slower                                                  |
| sympy_integrate                  | 11.3 ms                                                | 11.5 ms: 1.02x slower                                                  |
| xml_etree_parse                  | 107 ms                                                 | 109 ms: 1.02x slower                                                   |
| mdp                              | 1.49 sec                                               | 1.52 sec: 1.02x slower                                                 |
| comprehensions                   | 12.3 us                                                | 12.5 us: 1.02x slower                                                  |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 472 ms: 1.03x slower                                                   |
| xml_etree_iterparse              | 73.6 ms                                                | 76.9 ms: 1.05x slower                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 476 ms: 1.06x slower                                                   |
| python_startup_no_site           | 14.5 ms                                                | 15.5 ms: 1.07x slower                                                  |
| python_startup                   | 18.9 ms                                                | 20.3 ms: 1.07x slower                                                  |
| create_gc_cycles                 | 1.17 ms                                                | 1.30 ms: 1.11x slower                                                  |
| json_dumps                       | 6.52 ms                                                | 7.28 ms: 1.12x slower                                                  |
| k_core                           | 1.61 sec                                               | 1.92 sec: 1.20x slower                                                 |
| async_tree_io                    | 507 ms                                                 | 611 ms: 1.21x slower                                                   |
| async_tree_io_tg                 | 497 ms                                                 | 608 ms: 1.22x slower                                                   |
| async_tree_eager_io              | 514 ms                                                 | 715 ms: 1.39x slower                                                   |
| async_tree_eager_io_tg           | 477 ms                                                 | 706 ms: 1.48x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (6): asyncio_websockets, pidigits, crypto_pyaes, logging_silent, docutils, async_tree_none_tg
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, gevent_hub, mypy2, tornado_http
Ignored benchmarks (3) of results/bm-20241130-3.14.0a2+-328187c/bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json: many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.041x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.02x