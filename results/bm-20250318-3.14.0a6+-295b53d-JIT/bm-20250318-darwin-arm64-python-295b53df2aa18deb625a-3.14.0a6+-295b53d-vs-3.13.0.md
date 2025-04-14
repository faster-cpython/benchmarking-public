# Results vs. 3.13.0

- fork: python
- ref: 295b53df2aa18deb625a
- machine: darwin-arm64
- commit hash: 295b53d
- commit date: 2025-03-18
- overall geometric mean: 1.037x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-darwin-arm64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 171 ms: 1.04x faster                                                   |
| docutils       | 1.44 sec                                               | 1.49 sec: 1.03x slower                                                 |
| html5lib       | 36.7 ms                                                | 32.4 ms: 1.13x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-darwin-arm64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 203 ms: 1.42x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 378 ms: 1.35x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 206 ms: 1.30x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 393 ms: 1.29x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 388 ms: 1.29x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 169 ms: 1.25x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 388 ms: 1.23x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 162 ms: 1.22x faster                                                   |
| coroutines                       | 20.0 ms                                                | 17.3 ms: 1.16x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 148 ms: 1.13x faster                                                   |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 419 ms: 1.10x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 422 ms: 1.06x faster                                                   |
| async_tree_eager                 | 69.9 ms                                                | 66.3 ms: 1.05x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 363 ms: 1.03x faster                                                   |
| async_generators                 | 294 ms                                                 | 288 ms: 1.02x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 400 ms: 1.15x slower                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 182 ms: 1.32x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 135 ms: 2.85x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.06x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-darwin-arm64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 46.1 ms: 1.21x faster                                                  |
| nbody          | 73.6 ms                                                | 69.7 ms: 1.06x faster                                                  |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-darwin-arm64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.25 ms: 1.17x faster                                                  |
| regex_v8       | 17.0 ms                                                | 15.8 ms: 1.08x faster                                                  |
| regex_dna      | 149 ms                                                 | 140 ms: 1.06x faster                                                   |
| regex_compile  | 78.3 ms                                                | 74.0 ms: 1.06x faster                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-darwin-arm64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.27 sec: 1.23x faster                                                 |
| unpickle_pure_python | 165 us                                                 | 143 us: 1.16x faster                                                   |
| xml_etree_process    | 41.3 ms                                                | 36.9 ms: 1.12x faster                                                  |
| xml_etree_generate   | 57.1 ms                                                | 51.9 ms: 1.10x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 103 ms: 1.04x faster                                                   |
| xml_etree_iterparse  | 74.2 ms                                                | 73.1 ms: 1.02x faster                                                  |
| pickle_pure_python   | 215 us                                                 | 213 us: 1.01x faster                                                   |
| json_loads           | 17.0 us                                                | 18.0 us: 1.05x slower                                                  |
| json_dumps           | 6.47 ms                                                | 7.56 ms: 1.17x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-darwin-arm64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 17.6 ms: 1.07x faster                                                  |
| python_startup_no_site | 13.7 ms                                                | 13.3 ms: 1.03x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-darwin-arm64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.75 ms                                                | 6.72 ms: 1.15x faster                                                  |
| genshi_text     | 16.9 ms                                                | 15.4 ms: 1.10x faster                                                  |
| genshi_xml      | 34.1 ms                                                | 32.0 ms: 1.06x faster                                                  |
| django_template | 20.5 ms                                                | 22.6 ms: 1.11x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-darwin-arm64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy                         | 236 us                                                 | 163 us: 1.45x faster                                                   |
| async_tree_memoization_tg        | 288 ms                                                 | 203 ms: 1.42x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 378 ms: 1.35x faster                                                   |
| deepcopy_memo                    | 27.4 us                                                | 20.9 us: 1.31x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 206 ms: 1.30x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 393 ms: 1.29x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 388 ms: 1.29x faster                                                   |
| generators                       | 31.9 ms                                                | 25.0 ms: 1.28x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 169 ms: 1.25x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 388 ms: 1.23x faster                                                   |
| tomli_loads                      | 1.57 sec                                               | 1.27 sec: 1.23x faster                                                 |
| async_tree_none_tg               | 198 ms                                                 | 162 ms: 1.22x faster                                                   |
| deepcopy_reduce                  | 2.09 us                                                | 1.72 us: 1.21x faster                                                  |
| float                            | 55.8 ms                                                | 46.1 ms: 1.21x faster                                                  |
| scimark_sor                      | 106 ms                                                 | 89.1 ms: 1.19x faster                                                  |
| deltablue                        | 2.65 ms                                                | 2.24 ms: 1.18x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 65.3 ms: 1.17x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.25 ms: 1.17x faster                                                  |
| go                               | 117 ms                                                 | 100 ms: 1.16x faster                                                   |
| coroutines                       | 20.0 ms                                                | 17.3 ms: 1.16x faster                                                  |
| unpickle_pure_python             | 165 us                                                 | 143 us: 1.16x faster                                                   |
| richards                         | 36.2 ms                                                | 31.3 ms: 1.16x faster                                                  |
| mako                             | 7.75 ms                                                | 6.72 ms: 1.15x faster                                                  |
| html5lib                         | 36.7 ms                                                | 32.4 ms: 1.13x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 148 ms: 1.13x faster                                                   |
| xml_etree_process                | 41.3 ms                                                | 36.9 ms: 1.12x faster                                                  |
| richards_super                   | 39.2 ms                                                | 35.0 ms: 1.12x faster                                                  |
| xml_etree_generate               | 57.1 ms                                                | 51.9 ms: 1.10x faster                                                  |
| genshi_text                      | 16.9 ms                                                | 15.4 ms: 1.10x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 26.2 ms: 1.10x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 419 ms: 1.10x faster                                                   |
| pyflate                          | 352 ms                                                 | 323 ms: 1.09x faster                                                   |
| scimark_monte_carlo              | 50.4 ms                                                | 46.5 ms: 1.08x faster                                                  |
| regex_v8                         | 17.0 ms                                                | 15.8 ms: 1.08x faster                                                  |
| python_startup                   | 18.8 ms                                                | 17.6 ms: 1.07x faster                                                  |
| genshi_xml                       | 34.1 ms                                                | 32.0 ms: 1.06x faster                                                  |
| bpe_tokeniser                    | 3.26 sec                                               | 3.07 sec: 1.06x faster                                                 |
| bench_mp_pool                    | 64.7 ms                                                | 61.0 ms: 1.06x faster                                                  |
| regex_dna                        | 149 ms                                                 | 140 ms: 1.06x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 422 ms: 1.06x faster                                                   |
| pylint                           | 180 ms                                                 | 170 ms: 1.06x faster                                                   |
| regex_compile                    | 78.3 ms                                                | 74.0 ms: 1.06x faster                                                  |
| telco                            | 4.84 ms                                                | 4.58 ms: 1.06x faster                                                  |
| nbody                            | 73.6 ms                                                | 69.7 ms: 1.06x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 66.3 ms: 1.05x faster                                                  |
| connected_components             | 319 ms                                                 | 305 ms: 1.05x faster                                                   |
| xml_etree_parse                  | 108 ms                                                 | 103 ms: 1.04x faster                                                   |
| 2to3                             | 179 ms                                                 | 171 ms: 1.04x faster                                                   |
| k_core                           | 1.61 sec                                               | 1.55 sec: 1.04x faster                                                 |
| pprint_pformat                   | 1.10 sec                                               | 1.06 sec: 1.03x faster                                                 |
| scimark_fft                      | 200 ms                                                 | 193 ms: 1.03x faster                                                   |
| shortest_path                    | 345 ms                                                 | 335 ms: 1.03x faster                                                   |
| python_startup_no_site           | 13.7 ms                                                | 13.3 ms: 1.03x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 363 ms: 1.03x faster                                                   |
| pprint_safe_repr                 | 541 ms                                                 | 527 ms: 1.03x faster                                                   |
| async_generators                 | 294 ms                                                 | 288 ms: 1.02x faster                                                   |
| xml_etree_iterparse              | 74.2 ms                                                | 73.1 ms: 1.02x faster                                                  |
| typing_runtime_protocols         | 101 us                                                 | 99.2 us: 1.01x faster                                                  |
| thrift                           | 466 us                                                 | 461 us: 1.01x faster                                                   |
| mdp                              | 1.50 sec                                               | 1.49 sec: 1.01x faster                                                 |
| pickle_pure_python               | 215 us                                                 | 213 us: 1.01x faster                                                   |
| dask                             | 771 ms                                                 | 768 ms: 1.00x faster                                                   |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                                   |
| sqlite_synth                     | 1.55 us                                                | 1.56 us: 1.00x slower                                                  |
| bench_thread_pool                | 503 us                                                 | 507 us: 1.01x slower                                                   |
| logging_simple                   | 3.56 us                                                | 3.59 us: 1.01x slower                                                  |
| coverage                         | 46.2 ms                                                | 46.8 ms: 1.01x slower                                                  |
| sympy_str                        | 146 ms                                                 | 148 ms: 1.01x slower                                                   |
| sympy_expand                     | 248 ms                                                 | 251 ms: 1.02x slower                                                   |
| logging_format                   | 3.85 us                                                | 3.92 us: 1.02x slower                                                  |
| logging_silent                   | 71.0 ns                                                | 72.4 ns: 1.02x slower                                                  |
| pycparser                        | 701 ms                                                 | 715 ms: 1.02x slower                                                   |
| sympy_sum                        | 75.1 ms                                                | 76.9 ms: 1.02x slower                                                  |
| meteor_contest                   | 74.0 ms                                                | 76.0 ms: 1.03x slower                                                  |
| docutils                         | 1.44 sec                                               | 1.49 sec: 1.03x slower                                                 |
| hexiom                           | 4.87 ms                                                | 5.03 ms: 1.03x slower                                                  |
| pathlib                          | 23.2 ms                                                | 24.0 ms: 1.04x slower                                                  |
| json                             | 3.04 ms                                                | 3.15 ms: 1.04x slower                                                  |
| sqlalchemy_declarative           | 59.0 ms                                                | 61.4 ms: 1.04x slower                                                  |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.11 ms: 1.04x slower                                                  |
| scimark_lu                       | 75.9 ms                                                | 79.7 ms: 1.05x slower                                                  |
| fannkuch                         | 279 ms                                                 | 294 ms: 1.05x slower                                                   |
| sqlalchemy_imperative            | 6.69 ms                                                | 7.05 ms: 1.05x slower                                                  |
| json_loads                       | 17.0 us                                                | 18.0 us: 1.05x slower                                                  |
| comprehensions                   | 12.0 us                                                | 12.7 us: 1.06x slower                                                  |
| raytrace                         | 181 ms                                                 | 193 ms: 1.07x slower                                                   |
| sympy_integrate                  | 11.3 ms                                                | 12.0 ms: 1.07x slower                                                  |
| gc_traversal                     | 2.94 ms                                                | 3.13 ms: 1.07x slower                                                  |
| nqueens                          | 61.8 ms                                                | 66.0 ms: 1.07x slower                                                  |
| chaos                            | 41.1 ms                                                | 44.5 ms: 1.08x slower                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 1.30 ms: 1.09x slower                                                  |
| crypto_pyaes                     | 55.3 ms                                                | 60.7 ms: 1.10x slower                                                  |
| django_template                  | 20.5 ms                                                | 22.6 ms: 1.11x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 400 ms: 1.15x slower                                                   |
| many_optionals                   | 409 us                                                 | 473 us: 1.16x slower                                                   |
| json_dumps                       | 6.47 ms                                                | 7.56 ms: 1.17x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 182 ms: 1.32x slower                                                   |
| subparsers                       | 9.44 ms                                                | 12.8 ms: 1.36x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 135 ms: 2.85x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (2): sphinx, asyncio_websockets
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250318-3.14.0a6+-295b53d-JIT/bm-20250318-darwin-arm64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.037x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.10x