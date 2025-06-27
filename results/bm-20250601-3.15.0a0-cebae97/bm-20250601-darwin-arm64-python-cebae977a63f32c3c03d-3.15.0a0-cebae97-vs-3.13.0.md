# Results vs. 3.13.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: darwin-arm64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.056x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 170 ms: 1.05x faster                                                  |
| docutils       | 1.44 sec                                               | 1.46 sec: 1.01x slower                                                |
| html5lib       | 36.7 ms                                                | 31.6 ms: 1.16x faster                                                 |
| sphinx         | 602 ms                                                 | 585 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 192 ms: 1.49x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 365 ms: 1.40x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 195 ms: 1.37x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 380 ms: 1.34x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 375 ms: 1.34x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 164 ms: 1.29x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 374 ms: 1.28x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 157 ms: 1.26x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.20x faster                                                  |
| coroutines                       | 20.0 ms                                                | 17.0 ms: 1.18x faster                                                 |
| async_generators                 | 294 ms                                                 | 263 ms: 1.12x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 414 ms: 1.11x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 63.9 ms: 1.09x faster                                                 |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 411 ms: 1.09x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 357 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 389 ms: 1.12x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 168 ms: 1.22x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 129 ms: 2.73x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.10x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 49.5 ms: 1.13x faster                                                 |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                                  |
| nbody          | 73.6 ms                                                | 75.1 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.37 ms: 1.11x faster                                                 |
| regex_compile  | 78.3 ms                                                | 72.0 ms: 1.09x faster                                                 |
| regex_v8       | 17.0 ms                                                | 16.1 ms: 1.05x faster                                                 |
| regex_dna      | 149 ms                                                 | 143 ms: 1.04x faster                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.36 sec: 1.16x faster                                                |
| xml_etree_generate   | 57.1 ms                                                | 53.6 ms: 1.06x faster                                                 |
| xml_etree_process    | 41.3 ms                                                | 38.9 ms: 1.06x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 103 ms: 1.05x faster                                                  |
| json_loads           | 17.0 us                                                | 16.4 us: 1.04x faster                                                 |
| unpickle_pure_python | 165 us                                                 | 161 us: 1.03x faster                                                  |
| xml_etree_iterparse  | 74.2 ms                                                | 72.8 ms: 1.02x faster                                                 |
| pickle_pure_python   | 215 us                                                 | 219 us: 1.02x slower                                                  |
| json_dumps           | 6.47 ms                                                | 6.61 ms: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 18.1 ms: 1.04x faster                                                 |
| python_startup_no_site | 13.7 ms                                                | 13.5 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 14.7 ms: 1.15x faster                                                 |
| genshi_xml      | 34.1 ms                                                | 31.2 ms: 1.09x faster                                                 |
| mako            | 7.75 ms                                                | 7.81 ms: 1.01x slower                                                 |
| django_template | 20.5 ms                                                | 22.0 ms: 1.07x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 761 ms: 1.97x faster                                                  |
| deepcopy                         | 236 us                                                 | 156 us: 1.52x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 192 ms: 1.49x faster                                                  |
| deepcopy_memo                    | 27.4 us                                                | 19.3 us: 1.42x faster                                                 |
| async_tree_eager_io              | 511 ms                                                 | 365 ms: 1.40x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 195 ms: 1.37x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 380 ms: 1.34x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 375 ms: 1.34x faster                                                  |
| go                               | 117 ms                                                 | 87.5 ms: 1.33x faster                                                 |
| generators                       | 31.9 ms                                                | 24.0 ms: 1.33x faster                                                 |
| async_tree_none                  | 212 ms                                                 | 164 ms: 1.29x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 374 ms: 1.28x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 157 ms: 1.26x faster                                                  |
| deepcopy_reduce                  | 2.09 us                                                | 1.68 us: 1.25x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.20x faster                                                  |
| scimark_sor                      | 106 ms                                                 | 88.4 ms: 1.20x faster                                                 |
| coroutines                       | 20.0 ms                                                | 17.0 ms: 1.18x faster                                                 |
| html5lib                         | 36.7 ms                                                | 31.6 ms: 1.16x faster                                                 |
| dulwich_log                      | 28.7 ms                                                | 24.9 ms: 1.16x faster                                                 |
| tomli_loads                      | 1.57 sec                                               | 1.36 sec: 1.16x faster                                                |
| genshi_text                      | 16.9 ms                                                | 14.7 ms: 1.15x faster                                                 |
| float                            | 55.8 ms                                                | 49.5 ms: 1.13x faster                                                 |
| async_generators                 | 294 ms                                                 | 263 ms: 1.12x faster                                                  |
| pylint                           | 180 ms                                                 | 162 ms: 1.11x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 414 ms: 1.11x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.37 ms: 1.11x faster                                                 |
| pyflate                          | 352 ms                                                 | 319 ms: 1.10x faster                                                  |
| k_core                           | 1.61 sec                                               | 1.47 sec: 1.10x faster                                                |
| async_tree_eager                 | 69.9 ms                                                | 63.9 ms: 1.09x faster                                                 |
| genshi_xml                       | 34.1 ms                                                | 31.2 ms: 1.09x faster                                                 |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 411 ms: 1.09x faster                                                  |
| regex_compile                    | 78.3 ms                                                | 72.0 ms: 1.09x faster                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 46.6 ms: 1.08x faster                                                 |
| spectral_norm                    | 76.5 ms                                                | 70.9 ms: 1.08x faster                                                 |
| telco                            | 4.84 ms                                                | 4.50 ms: 1.08x faster                                                 |
| xml_etree_generate               | 57.1 ms                                                | 53.6 ms: 1.06x faster                                                 |
| xml_etree_process                | 41.3 ms                                                | 38.9 ms: 1.06x faster                                                 |
| json                             | 3.04 ms                                                | 2.87 ms: 1.06x faster                                                 |
| bpe_tokeniser                    | 3.26 sec                                               | 3.09 sec: 1.06x faster                                                |
| regex_v8                         | 17.0 ms                                                | 16.1 ms: 1.05x faster                                                 |
| shortest_path                    | 345 ms                                                 | 329 ms: 1.05x faster                                                  |
| 2to3                             | 179 ms                                                 | 170 ms: 1.05x faster                                                  |
| thrift                           | 466 us                                                 | 444 us: 1.05x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 103 ms: 1.05x faster                                                  |
| fannkuch                         | 279 ms                                                 | 267 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 357 ms: 1.04x faster                                                  |
| regex_dna                        | 149 ms                                                 | 143 ms: 1.04x faster                                                  |
| typing_runtime_protocols         | 101 us                                                 | 96.7 us: 1.04x faster                                                 |
| connected_components             | 319 ms                                                 | 307 ms: 1.04x faster                                                  |
| python_startup                   | 18.8 ms                                                | 18.1 ms: 1.04x faster                                                 |
| json_loads                       | 17.0 us                                                | 16.4 us: 1.04x faster                                                 |
| hexiom                           | 4.87 ms                                                | 4.69 ms: 1.04x faster                                                 |
| sphinx                           | 602 ms                                                 | 585 ms: 1.03x faster                                                  |
| pycparser                        | 701 ms                                                 | 682 ms: 1.03x faster                                                  |
| deltablue                        | 2.65 ms                                                | 2.58 ms: 1.03x faster                                                 |
| sympy_expand                     | 248 ms                                                 | 241 ms: 1.03x faster                                                  |
| unpickle_pure_python             | 165 us                                                 | 161 us: 1.03x faster                                                  |
| chaos                            | 41.1 ms                                                | 40.2 ms: 1.02x faster                                                 |
| sympy_integrate                  | 11.3 ms                                                | 11.1 ms: 1.02x faster                                                 |
| xml_etree_iterparse              | 74.2 ms                                                | 72.8 ms: 1.02x faster                                                 |
| scimark_fft                      | 200 ms                                                 | 196 ms: 1.02x faster                                                  |
| sympy_str                        | 146 ms                                                 | 143 ms: 1.02x faster                                                  |
| python_startup_no_site           | 13.7 ms                                                | 13.5 ms: 1.01x faster                                                 |
| richards                         | 36.2 ms                                                | 35.8 ms: 1.01x faster                                                 |
| dask                             | 771 ms                                                 | 766 ms: 1.01x faster                                                  |
| raytrace                         | 181 ms                                                 | 180 ms: 1.00x faster                                                  |
| meteor_contest                   | 74.0 ms                                                | 73.7 ms: 1.00x faster                                                 |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                                  |
| comprehensions                   | 12.0 us                                                | 12.0 us: 1.00x slower                                                 |
| sympy_sum                        | 75.1 ms                                                | 75.6 ms: 1.01x slower                                                 |
| docutils                         | 1.44 sec                                               | 1.46 sec: 1.01x slower                                                |
| mako                             | 7.75 ms                                                | 7.81 ms: 1.01x slower                                                 |
| nbody                            | 73.6 ms                                                | 75.1 ms: 1.02x slower                                                 |
| pickle_pure_python               | 215 us                                                 | 219 us: 1.02x slower                                                  |
| json_dumps                       | 6.47 ms                                                | 6.61 ms: 1.02x slower                                                 |
| sqlite_synth                     | 1.55 us                                                | 1.59 us: 1.03x slower                                                 |
| pprint_pformat                   | 1.10 sec                                               | 1.13 sec: 1.03x slower                                                |
| richards_super                   | 39.2 ms                                                | 40.2 ms: 1.03x slower                                                 |
| logging_simple                   | 3.56 us                                                | 3.66 us: 1.03x slower                                                 |
| logging_format                   | 3.85 us                                                | 3.97 us: 1.03x slower                                                 |
| crypto_pyaes                     | 55.3 ms                                                | 57.1 ms: 1.03x slower                                                 |
| pprint_safe_repr                 | 541 ms                                                 | 558 ms: 1.03x slower                                                  |
| pathlib                          | 23.2 ms                                                | 24.1 ms: 1.04x slower                                                 |
| coverage                         | 46.2 ms                                                | 48.1 ms: 1.04x slower                                                 |
| django_template                  | 20.5 ms                                                | 22.0 ms: 1.07x slower                                                 |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.23 ms: 1.08x slower                                                 |
| gc_traversal                     | 2.94 ms                                                | 3.19 ms: 1.09x slower                                                 |
| scimark_lu                       | 75.9 ms                                                | 83.3 ms: 1.10x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 389 ms: 1.12x slower                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 1.35 ms: 1.13x slower                                                 |
| many_optionals                   | 409 us                                                 | 466 us: 1.14x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 168 ms: 1.22x slower                                                  |
| subparsers                       | 9.44 ms                                                | 13.7 ms: 1.45x slower                                                 |
| async_tree_eager_tg              | 47.4 ms                                                | 129 ms: 2.73x slower                                                  |
| logging_silent                   | 71.0 ns                                                | 331 ns: 4.66x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (2): asyncio_websockets, nqueens
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250601-3.15.0a0-cebae97/bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.056x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.11x