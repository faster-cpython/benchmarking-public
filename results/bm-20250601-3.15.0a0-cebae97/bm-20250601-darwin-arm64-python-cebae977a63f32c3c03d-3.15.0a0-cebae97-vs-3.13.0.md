# Results vs. 3.13.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: darwin-arm64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.087x slower
- HPT reliability: 97.02%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 221 ms: 1.24x slower                                                  |
| docutils       | 1.44 sec                                               | 1.59 sec: 1.10x slower                                                |
| html5lib       | 36.7 ms                                                | 33.3 ms: 1.10x faster                                                 |
| sphinx         | 602 ms                                                 | 651 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.07x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 203 ms: 1.41x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 205 ms: 1.30x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 394 ms: 1.30x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 389 ms: 1.29x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 402 ms: 1.26x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 174 ms: 1.22x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 400 ms: 1.20x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 167 ms: 1.19x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 148 ms: 1.14x faster                                                  |
| coroutines                       | 20.0 ms                                                | 18.1 ms: 1.11x faster                                                 |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 454 ms: 1.01x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 70.4 ms: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 391 ms: 1.05x slower                                                  |
| async_generators                 | 294 ms                                                 | 316 ms: 1.08x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 427 ms: 1.23x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 182 ms: 1.32x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 141 ms: 2.97x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 51.2 ms: 1.09x faster                                                 |
| pidigits       | 284 ms                                                 | 284 ms: 1.00x slower                                                  |
| nbody          | 73.6 ms                                                | 77.6 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.19 ms: 1.20x faster                                                 |
| regex_compile  | 78.3 ms                                                | 74.3 ms: 1.05x faster                                                 |
| regex_dna      | 149 ms                                                 | 145 ms: 1.03x faster                                                  |
| regex_v8       | 17.0 ms                                                | 17.3 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.40 sec: 1.12x faster                                                |
| unpickle_pure_python | 165 us                                                 | 156 us: 1.06x faster                                                  |
| xml_etree_iterparse  | 74.2 ms                                                | 76.7 ms: 1.03x slower                                                 |
| pickle_pure_python   | 215 us                                                 | 222 us: 1.04x slower                                                  |
| xml_etree_parse      | 108 ms                                                 | 112 ms: 1.04x slower                                                  |
| xml_etree_process    | 41.3 ms                                                | 43.9 ms: 1.06x slower                                                 |
| xml_etree_generate   | 57.1 ms                                                | 65.1 ms: 1.14x slower                                                 |
| json_dumps           | 6.47 ms                                                | 8.07 ms: 1.25x slower                                                 |
| json_loads           | 17.0 us                                                | 22.6 us: 1.33x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.07x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup | 18.8 ms                                                | 18.2 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 15.6 ms: 1.08x faster                                                 |
| genshi_xml      | 34.1 ms                                                | 33.1 ms: 1.03x faster                                                 |
| mako            | 7.75 ms                                                | 8.23 ms: 1.06x slower                                                 |
| django_template | 20.5 ms                                                | 25.3 ms: 1.24x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 880 ms: 1.70x faster                                                  |
| go                               | 117 ms                                                 | 77.4 ms: 1.51x faster                                                 |
| deepcopy_memo                    | 27.4 us                                                | 19.3 us: 1.42x faster                                                 |
| async_tree_memoization_tg        | 288 ms                                                 | 203 ms: 1.41x faster                                                  |
| generators                       | 31.9 ms                                                | 23.0 ms: 1.39x faster                                                 |
| async_tree_memoization           | 268 ms                                                 | 205 ms: 1.30x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 394 ms: 1.30x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 389 ms: 1.29x faster                                                  |
| deepcopy                         | 236 us                                                 | 185 us: 1.28x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 402 ms: 1.26x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 174 ms: 1.22x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.19 ms: 1.20x faster                                                 |
| async_tree_eager_io_tg           | 479 ms                                                 | 400 ms: 1.20x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 167 ms: 1.19x faster                                                  |
| scimark_sor                      | 106 ms                                                 | 89.9 ms: 1.18x faster                                                 |
| pyflate                          | 352 ms                                                 | 306 ms: 1.15x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 148 ms: 1.14x faster                                                  |
| tomli_loads                      | 1.57 sec                                               | 1.40 sec: 1.12x faster                                                |
| coroutines                       | 20.0 ms                                                | 18.1 ms: 1.11x faster                                                 |
| html5lib                         | 36.7 ms                                                | 33.3 ms: 1.10x faster                                                 |
| float                            | 55.8 ms                                                | 51.2 ms: 1.09x faster                                                 |
| genshi_text                      | 16.9 ms                                                | 15.6 ms: 1.08x faster                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 46.7 ms: 1.08x faster                                                 |
| dulwich_log                      | 28.7 ms                                                | 27.1 ms: 1.06x faster                                                 |
| hexiom                           | 4.87 ms                                                | 4.60 ms: 1.06x faster                                                 |
| unpickle_pure_python             | 165 us                                                 | 156 us: 1.06x faster                                                  |
| regex_compile                    | 78.3 ms                                                | 74.3 ms: 1.05x faster                                                 |
| deepcopy_reduce                  | 2.09 us                                                | 2.00 us: 1.05x faster                                                 |
| python_startup                   | 18.8 ms                                                | 18.2 ms: 1.03x faster                                                 |
| genshi_xml                       | 34.1 ms                                                | 33.1 ms: 1.03x faster                                                 |
| regex_dna                        | 149 ms                                                 | 145 ms: 1.03x faster                                                  |
| connected_components             | 319 ms                                                 | 312 ms: 1.02x faster                                                  |
| deltablue                        | 2.65 ms                                                | 2.60 ms: 1.02x faster                                                 |
| shortest_path                    | 345 ms                                                 | 341 ms: 1.01x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 454 ms: 1.01x faster                                                  |
| comprehensions                   | 12.0 us                                                | 11.9 us: 1.01x faster                                                 |
| pidigits                         | 284 ms                                                 | 284 ms: 1.00x slower                                                  |
| async_tree_eager                 | 69.9 ms                                                | 70.4 ms: 1.01x slower                                                 |
| regex_v8                         | 17.0 ms                                                | 17.3 ms: 1.02x slower                                                 |
| meteor_contest                   | 74.0 ms                                                | 75.9 ms: 1.03x slower                                                 |
| richards_super                   | 39.2 ms                                                | 40.5 ms: 1.03x slower                                                 |
| xml_etree_iterparse              | 74.2 ms                                                | 76.7 ms: 1.03x slower                                                 |
| pickle_pure_python               | 215 us                                                 | 222 us: 1.04x slower                                                  |
| spectral_norm                    | 76.5 ms                                                | 79.2 ms: 1.04x slower                                                 |
| sympy_integrate                  | 11.3 ms                                                | 11.7 ms: 1.04x slower                                                 |
| xml_etree_parse                  | 108 ms                                                 | 112 ms: 1.04x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 391 ms: 1.05x slower                                                  |
| nbody                            | 73.6 ms                                                | 77.6 ms: 1.05x slower                                                 |
| pycparser                        | 701 ms                                                 | 744 ms: 1.06x slower                                                  |
| xml_etree_process                | 41.3 ms                                                | 43.9 ms: 1.06x slower                                                 |
| mako                             | 7.75 ms                                                | 8.23 ms: 1.06x slower                                                 |
| bench_thread_pool                | 503 us                                                 | 535 us: 1.06x slower                                                  |
| chaos                            | 41.1 ms                                                | 43.8 ms: 1.07x slower                                                 |
| async_generators                 | 294 ms                                                 | 316 ms: 1.08x slower                                                  |
| sphinx                           | 602 ms                                                 | 651 ms: 1.08x slower                                                  |
| pprint_pformat                   | 1.10 sec                                               | 1.19 sec: 1.08x slower                                                |
| pprint_safe_repr                 | 541 ms                                                 | 587 ms: 1.09x slower                                                  |
| crypto_pyaes                     | 55.3 ms                                                | 60.3 ms: 1.09x slower                                                 |
| pathlib                          | 23.2 ms                                                | 25.3 ms: 1.09x slower                                                 |
| nqueens                          | 61.8 ms                                                | 67.8 ms: 1.10x slower                                                 |
| gc_traversal                     | 2.94 ms                                                | 3.23 ms: 1.10x slower                                                 |
| docutils                         | 1.44 sec                                               | 1.59 sec: 1.10x slower                                                |
| dask                             | 771 ms                                                 | 857 ms: 1.11x slower                                                  |
| logging_simple                   | 3.56 us                                                | 3.97 us: 1.12x slower                                                 |
| sympy_str                        | 146 ms                                                 | 163 ms: 1.12x slower                                                  |
| logging_format                   | 3.85 us                                                | 4.33 us: 1.12x slower                                                 |
| bpe_tokeniser                    | 3.26 sec                                               | 3.67 sec: 1.13x slower                                                |
| fannkuch                         | 279 ms                                                 | 314 ms: 1.13x slower                                                  |
| scimark_lu                       | 75.9 ms                                                | 85.9 ms: 1.13x slower                                                 |
| sympy_sum                        | 75.1 ms                                                | 85.1 ms: 1.13x slower                                                 |
| xml_etree_generate               | 57.1 ms                                                | 65.1 ms: 1.14x slower                                                 |
| telco                            | 4.84 ms                                                | 5.55 ms: 1.15x slower                                                 |
| sympy_expand                     | 248 ms                                                 | 285 ms: 1.15x slower                                                  |
| bench_mp_pool                    | 64.7 ms                                                | 74.8 ms: 1.16x slower                                                 |
| raytrace                         | 181 ms                                                 | 210 ms: 1.16x slower                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 1.40 ms: 1.17x slower                                                 |
| typing_runtime_protocols         | 101 us                                                 | 119 us: 1.18x slower                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.90 us: 1.22x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 427 ms: 1.23x slower                                                  |
| 2to3                             | 179 ms                                                 | 221 ms: 1.24x slower                                                  |
| django_template                  | 20.5 ms                                                | 25.3 ms: 1.24x slower                                                 |
| json_dumps                       | 6.47 ms                                                | 8.07 ms: 1.25x slower                                                 |
| json                             | 3.04 ms                                                | 3.83 ms: 1.26x slower                                                 |
| many_optionals                   | 409 us                                                 | 523 us: 1.28x slower                                                  |
| scimark_fft                      | 200 ms                                                 | 263 ms: 1.32x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 182 ms: 1.32x slower                                                  |
| json_loads                       | 17.0 us                                                | 22.6 us: 1.33x slower                                                 |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 4.03 ms: 1.35x slower                                                 |
| subparsers                       | 9.44 ms                                                | 16.0 ms: 1.70x slower                                                 |
| async_tree_eager_tg              | 47.4 ms                                                | 141 ms: 2.97x slower                                                  |
| logging_silent                   | 71.0 ns                                                | 420 ns: 5.91x slower                                                  |
| coverage                         | 46.2 ms                                                | 302 ms: 6.53x slower                                                  |
| thrift                           | 466 us                                                 | 44.2 ms: 94.93x slower                                                |
| Geometric mean                   | (ref)                                                  | 1.11x slower                                                          |

Benchmark hidden because not significant (6): pylint, python_startup_no_site, richards, asyncio_websockets, async_tree_cpu_io_mixed_tg, k_core
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250601-3.15.0a0-cebae97/bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.087x slower

# HPT report

- Reliability score: 97.02% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.08x