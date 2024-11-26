# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_frame_pointer
- machine: darwin-arm64
- commit hash: b1f0a4e
- commit date: 2024-11-14
- overall geometric mean: 1.005x slower
- HPT reliability: 67.81%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-darwin-arm64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 193 ms: 1.03x slower                                                         |
| docutils       | 1.44 sec                                               | 1.61 sec: 1.12x slower                                                       |
| html5lib       | 36.6 ms                                                | 33.5 ms: 1.09x faster                                                        |
| sphinx         | 603 ms                                                 | 681 ms: 1.13x slower                                                         |
| Geometric mean | (ref)                                                  | 1.05x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-darwin-arm64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 241 ms: 1.19x faster                                                         |
| coroutines                       | 19.8 ms                                                | 17.6 ms: 1.12x faster                                                        |
| async_tree_eager_memoization     | 168 ms                                                 | 160 ms: 1.05x faster                                                         |
| async_tree_eager_tg              | 47.8 ms                                                | 45.6 ms: 1.05x faster                                                        |
| async_tree_memoization           | 268 ms                                                 | 257 ms: 1.04x faster                                                         |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 133 ms: 1.03x faster                                                         |
| async_tree_none                  | 215 ms                                                 | 212 ms: 1.02x faster                                                         |
| async_tree_eager                 | 70.1 ms                                                | 69.3 ms: 1.01x faster                                                        |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 343 ms: 1.01x faster                                                         |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 370 ms: 1.01x faster                                                         |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 473 ms: 1.03x slower                                                         |
| async_generators                 | 295 ms                                                 | 307 ms: 1.04x slower                                                         |
| async_tree_none_tg               | 198 ms                                                 | 208 ms: 1.05x slower                                                         |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 480 ms: 1.07x slower                                                         |
| async_tree_io                    | 507 ms                                                 | 596 ms: 1.18x slower                                                         |
| async_tree_io_tg                 | 497 ms                                                 | 628 ms: 1.26x slower                                                         |
| async_tree_eager_io              | 514 ms                                                 | 684 ms: 1.33x slower                                                         |
| async_tree_eager_io_tg           | 477 ms                                                 | 729 ms: 1.53x slower                                                         |
| Geometric mean                   | (ref)                                                  | 1.04x slower                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-darwin-arm64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 56.0 ms                                                | 51.2 ms: 1.09x faster                                                        |
| nbody          | 74.0 ms                                                | 72.8 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-darwin-arm64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.33 ms: 1.13x faster                                                        |
| regex_v8       | 17.0 ms                                                | 16.0 ms: 1.06x faster                                                        |
| regex_dna      | 149 ms                                                 | 141 ms: 1.06x faster                                                         |
| regex_compile  | 78.6 ms                                                | 79.1 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-darwin-arm64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.30 sec: 1.20x faster                                                       |
| xml_etree_process    | 41.0 ms                                                | 36.6 ms: 1.12x faster                                                        |
| unpickle_pure_python | 164 us                                                 | 148 us: 1.11x faster                                                         |
| xml_etree_generate   | 57.0 ms                                                | 51.4 ms: 1.11x faster                                                        |
| pickle_pure_python   | 214 us                                                 | 201 us: 1.07x faster                                                         |
| json_loads           | 17.0 us                                                | 16.7 us: 1.02x faster                                                        |
| xml_etree_parse      | 107 ms                                                 | 105 ms: 1.02x faster                                                         |
| xml_etree_iterparse  | 73.6 ms                                                | 74.1 ms: 1.01x slower                                                        |
| json_dumps           | 6.52 ms                                                | 7.27 ms: 1.11x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-darwin-arm64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 14.5 ms                                                | 15.0 ms: 1.04x slower                                                        |
| python_startup         | 18.9 ms                                                | 19.7 ms: 1.04x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.04x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-darwin-arm64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.61 ms: 1.16x faster                                                        |
| genshi_text     | 16.9 ms                                                | 17.2 ms: 1.02x slower                                                        |
| django_template | 22.2 ms                                                | 23.8 ms: 1.07x slower                                                        |
| genshi_xml      | 34.4 ms                                                | 42.0 ms: 1.22x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                                 |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-darwin-arm64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy                         | 237 us                                                 | 163 us: 1.46x faster                                                         |
| deepcopy_memo                    | 27.4 us                                                | 19.2 us: 1.43x faster                                                        |
| deepcopy_reduce                  | 2.07 us                                                | 1.60 us: 1.29x faster                                                        |
| tomli_loads                      | 1.57 sec                                               | 1.30 sec: 1.20x faster                                                       |
| async_tree_memoization_tg        | 288 ms                                                 | 241 ms: 1.19x faster                                                         |
| mako                             | 7.68 ms                                                | 6.61 ms: 1.16x faster                                                        |
| regex_effbot                     | 2.63 ms                                                | 2.33 ms: 1.13x faster                                                        |
| coroutines                       | 19.8 ms                                                | 17.6 ms: 1.12x faster                                                        |
| xml_etree_process                | 41.0 ms                                                | 36.6 ms: 1.12x faster                                                        |
| unpickle_pure_python             | 164 us                                                 | 148 us: 1.11x faster                                                         |
| xml_etree_generate               | 57.0 ms                                                | 51.4 ms: 1.11x faster                                                        |
| generators                       | 31.5 ms                                                | 28.6 ms: 1.10x faster                                                        |
| float                            | 56.0 ms                                                | 51.2 ms: 1.09x faster                                                        |
| scimark_sor                      | 105 ms                                                 | 96.4 ms: 1.09x faster                                                        |
| html5lib                         | 36.6 ms                                                | 33.5 ms: 1.09x faster                                                        |
| go                               | 115 ms                                                 | 106 ms: 1.09x faster                                                         |
| fannkuch                         | 284 ms                                                 | 264 ms: 1.08x faster                                                         |
| pickle_pure_python               | 214 us                                                 | 201 us: 1.07x faster                                                         |
| regex_v8                         | 17.0 ms                                                | 16.0 ms: 1.06x faster                                                        |
| regex_dna                        | 149 ms                                                 | 141 ms: 1.06x faster                                                         |
| logging_simple                   | 3.60 us                                                | 3.41 us: 1.06x faster                                                        |
| thrift                           | 466 us                                                 | 442 us: 1.05x faster                                                         |
| bpe_tokeniser                    | 3.25 sec                                               | 3.08 sec: 1.05x faster                                                       |
| async_tree_eager_memoization     | 168 ms                                                 | 160 ms: 1.05x faster                                                         |
| connected_components             | 319 ms                                                 | 303 ms: 1.05x faster                                                         |
| pprint_safe_repr                 | 533 ms                                                 | 507 ms: 1.05x faster                                                         |
| json                             | 3.03 ms                                                | 2.88 ms: 1.05x faster                                                        |
| scimark_monte_carlo              | 50.4 ms                                                | 48.0 ms: 1.05x faster                                                        |
| async_tree_eager_tg              | 47.8 ms                                                | 45.6 ms: 1.05x faster                                                        |
| logging_format                   | 3.89 us                                                | 3.72 us: 1.05x faster                                                        |
| pprint_pformat                   | 1.08 sec                                               | 1.04 sec: 1.05x faster                                                       |
| async_tree_memoization           | 268 ms                                                 | 257 ms: 1.04x faster                                                         |
| shortest_path                    | 347 ms                                                 | 333 ms: 1.04x faster                                                         |
| scimark_lu                       | 76.7 ms                                                | 73.7 ms: 1.04x faster                                                        |
| coverage                         | 46.0 ms                                                | 44.3 ms: 1.04x faster                                                        |
| pathlib                          | 23.4 ms                                                | 22.5 ms: 1.04x faster                                                        |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 133 ms: 1.03x faster                                                         |
| telco                            | 4.76 ms                                                | 4.65 ms: 1.02x faster                                                        |
| scimark_fft                      | 201 ms                                                 | 196 ms: 1.02x faster                                                         |
| nbody                            | 74.0 ms                                                | 72.8 ms: 1.02x faster                                                        |
| json_loads                       | 17.0 us                                                | 16.7 us: 1.02x faster                                                        |
| async_tree_none                  | 215 ms                                                 | 212 ms: 1.02x faster                                                         |
| xml_etree_parse                  | 107 ms                                                 | 105 ms: 1.02x faster                                                         |
| richards_super                   | 39.1 ms                                                | 38.5 ms: 1.01x faster                                                        |
| spectral_norm                    | 76.3 ms                                                | 75.2 ms: 1.01x faster                                                        |
| richards                         | 35.2 ms                                                | 34.8 ms: 1.01x faster                                                        |
| pyflate                          | 351 ms                                                 | 347 ms: 1.01x faster                                                         |
| async_tree_eager                 | 70.1 ms                                                | 69.3 ms: 1.01x faster                                                        |
| bench_thread_pool                | 505 us                                                 | 499 us: 1.01x faster                                                         |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 343 ms: 1.01x faster                                                         |
| pycparser                        | 705 ms                                                 | 700 ms: 1.01x faster                                                         |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 370 ms: 1.01x faster                                                         |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.72 ms: 1.00x slower                                                        |
| regex_compile                    | 78.6 ms                                                | 79.1 ms: 1.01x slower                                                        |
| xml_etree_iterparse              | 73.6 ms                                                | 74.1 ms: 1.01x slower                                                        |
| gc_traversal                     | 2.91 ms                                                | 2.93 ms: 1.01x slower                                                        |
| typing_runtime_protocols         | 101 us                                                 | 102 us: 1.01x slower                                                         |
| nqueens                          | 62.5 ms                                                | 63.4 ms: 1.01x slower                                                        |
| genshi_text                      | 16.9 ms                                                | 17.2 ms: 1.02x slower                                                        |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 473 ms: 1.03x slower                                                         |
| dulwich_log                      | 28.5 ms                                                | 29.4 ms: 1.03x slower                                                        |
| 2to3                             | 187 ms                                                 | 193 ms: 1.03x slower                                                         |
| python_startup_no_site           | 14.5 ms                                                | 15.0 ms: 1.04x slower                                                        |
| crypto_pyaes                     | 54.2 ms                                                | 56.3 ms: 1.04x slower                                                        |
| meteor_contest                   | 74.0 ms                                                | 76.9 ms: 1.04x slower                                                        |
| async_generators                 | 295 ms                                                 | 307 ms: 1.04x slower                                                         |
| bench_mp_pool                    | 62.5 ms                                                | 65.2 ms: 1.04x slower                                                        |
| python_startup                   | 18.9 ms                                                | 19.7 ms: 1.04x slower                                                        |
| sqlglot_normalize                | 189 ms                                                 | 197 ms: 1.04x slower                                                         |
| deltablue                        | 2.68 ms                                                | 2.79 ms: 1.04x slower                                                        |
| async_tree_none_tg               | 198 ms                                                 | 208 ms: 1.05x slower                                                         |
| sympy_expand                     | 246 ms                                                 | 259 ms: 1.05x slower                                                         |
| sqlglot_parse                    | 856 us                                                 | 903 us: 1.05x slower                                                         |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 3.17 ms: 1.06x slower                                                        |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 480 ms: 1.07x slower                                                         |
| django_template                  | 22.2 ms                                                | 23.8 ms: 1.07x slower                                                        |
| raytrace                         | 181 ms                                                 | 195 ms: 1.08x slower                                                         |
| mdp                              | 1.49 sec                                               | 1.61 sec: 1.08x slower                                                       |
| sqlglot_transpile                | 1.02 ms                                                | 1.11 ms: 1.08x slower                                                        |
| sqlalchemy_declarative           | 58.9 ms                                                | 63.7 ms: 1.08x slower                                                        |
| sympy_str                        | 145 ms                                                 | 158 ms: 1.09x slower                                                         |
| sympy_sum                        | 75.4 ms                                                | 82.5 ms: 1.10x slower                                                        |
| chaos                            | 41.2 ms                                                | 45.2 ms: 1.10x slower                                                        |
| json_dumps                       | 6.52 ms                                                | 7.27 ms: 1.11x slower                                                        |
| sqlglot_optimize                 | 34.9 ms                                                | 39.0 ms: 1.12x slower                                                        |
| docutils                         | 1.44 sec                                               | 1.61 sec: 1.12x slower                                                       |
| sphinx                           | 603 ms                                                 | 681 ms: 1.13x slower                                                         |
| create_gc_cycles                 | 1.17 ms                                                | 1.33 ms: 1.13x slower                                                        |
| hexiom                           | 4.86 ms                                                | 5.60 ms: 1.15x slower                                                        |
| sympy_integrate                  | 11.3 ms                                                | 13.2 ms: 1.17x slower                                                        |
| async_tree_io                    | 507 ms                                                 | 596 ms: 1.18x slower                                                         |
| comprehensions                   | 12.3 us                                                | 14.4 us: 1.18x slower                                                        |
| logging_silent                   | 70.1 ns                                                | 85.0 ns: 1.21x slower                                                        |
| genshi_xml                       | 34.4 ms                                                | 42.0 ms: 1.22x slower                                                        |
| async_tree_io_tg                 | 497 ms                                                 | 628 ms: 1.26x slower                                                         |
| async_tree_eager_io              | 514 ms                                                 | 684 ms: 1.33x slower                                                         |
| k_core                           | 1.61 sec                                               | 2.25 sec: 1.40x slower                                                       |
| async_tree_eager_io_tg           | 477 ms                                                 | 729 ms: 1.53x slower                                                         |
| Geometric mean                   | (ref)                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (3): pidigits, asyncio_websockets, pylint
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, gevent_hub, mypy2, tornado_http
Ignored benchmarks (3) of results/bm-20241114-3.14.0a1+-b1f0a4e-JIT/bm-20241114-darwin-arm64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e.json: many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.005x slower
# HPT report

- Reliability score: 67.81% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.10x