# Results vs. 3.13.0

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: darwin-arm64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.010x slower
- HPT reliability: 63.44%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 186 ms: 1.04x slower                                                  |
| docutils       | 1.44 sec                                               | 1.51 sec: 1.05x slower                                                |
| html5lib       | 36.7 ms                                                | 34.4 ms: 1.07x faster                                                 |
| sphinx         | 602 ms                                                 | 615 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 208 ms: 1.38x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 396 ms: 1.29x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 214 ms: 1.25x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 404 ms: 1.24x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 410 ms: 1.24x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 403 ms: 1.19x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 179 ms: 1.18x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 171 ms: 1.16x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 149 ms: 1.13x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 431 ms: 1.06x faster                                                  |
| coroutines                       | 20.0 ms                                                | 18.9 ms: 1.06x faster                                                 |
| async_generators                 | 294 ms                                                 | 277 ms: 1.06x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 424 ms: 1.06x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 367 ms: 1.02x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 76.6 ms: 1.10x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 398 ms: 1.15x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 181 ms: 1.31x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 141 ms: 2.97x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 56.7 ms: 1.02x slower                                                 |
| nbody          | 73.6 ms                                                | 85.7 ms: 1.16x slower                                                 |
| Geometric mean | (ref)                                                  | 1.06x slower                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.39 ms: 1.10x faster                                                 |
| regex_v8       | 17.0 ms                                                | 16.5 ms: 1.03x faster                                                 |
| regex_dna      | 149 ms                                                 | 147 ms: 1.02x faster                                                  |
| regex_compile  | 78.3 ms                                                | 81.2 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.43 sec: 1.10x faster                                                |
| xml_etree_parse      | 108 ms                                                 | 105 ms: 1.03x faster                                                  |
| json_loads           | 17.0 us                                                | 16.5 us: 1.03x faster                                                 |
| xml_etree_generate   | 57.1 ms                                                | 58.6 ms: 1.03x slower                                                 |
| xml_etree_process    | 41.3 ms                                                | 43.2 ms: 1.05x slower                                                 |
| json_dumps           | 6.47 ms                                                | 6.82 ms: 1.05x slower                                                 |
| unpickle_pure_python | 165 us                                                 | 177 us: 1.07x slower                                                  |
| pickle_pure_python   | 215 us                                                 | 241 us: 1.12x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                          |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 17.7 ms: 1.07x faster                                                 |
| python_startup_no_site | 13.7 ms                                                | 13.2 ms: 1.04x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 17.9 ms: 1.06x slower                                                 |
| genshi_xml      | 34.1 ms                                                | 36.4 ms: 1.07x slower                                                 |
| mako            | 7.75 ms                                                | 8.96 ms: 1.16x slower                                                 |
| django_template | 20.5 ms                                                | 24.8 ms: 1.21x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.12x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 819 ms: 1.83x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 208 ms: 1.38x faster                                                  |
| deepcopy                         | 236 us                                                 | 175 us: 1.35x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 396 ms: 1.29x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 214 ms: 1.25x faster                                                  |
| deepcopy_memo                    | 27.4 us                                                | 22.0 us: 1.25x faster                                                 |
| async_tree_io_tg                 | 500 ms                                                 | 404 ms: 1.24x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 410 ms: 1.24x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 403 ms: 1.19x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 179 ms: 1.18x faster                                                  |
| scimark_sor                      | 106 ms                                                 | 89.9 ms: 1.18x faster                                                 |
| go                               | 117 ms                                                 | 99.5 ms: 1.17x faster                                                 |
| async_tree_none_tg               | 198 ms                                                 | 171 ms: 1.16x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 149 ms: 1.13x faster                                                  |
| deepcopy_reduce                  | 2.09 us                                                | 1.89 us: 1.11x faster                                                 |
| regex_effbot                     | 2.63 ms                                                | 2.39 ms: 1.10x faster                                                 |
| k_core                           | 1.61 sec                                               | 1.47 sec: 1.10x faster                                                |
| tomli_loads                      | 1.57 sec                                               | 1.43 sec: 1.10x faster                                                |
| html5lib                         | 36.7 ms                                                | 34.4 ms: 1.07x faster                                                 |
| python_startup                   | 18.8 ms                                                | 17.7 ms: 1.07x faster                                                 |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 431 ms: 1.06x faster                                                  |
| pylint                           | 180 ms                                                 | 169 ms: 1.06x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 72.0 ms: 1.06x faster                                                 |
| coroutines                       | 20.0 ms                                                | 18.9 ms: 1.06x faster                                                 |
| async_generators                 | 294 ms                                                 | 277 ms: 1.06x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 424 ms: 1.06x faster                                                  |
| pyflate                          | 352 ms                                                 | 333 ms: 1.06x faster                                                  |
| shortest_path                    | 345 ms                                                 | 329 ms: 1.05x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 27.5 ms: 1.05x faster                                                 |
| connected_components             | 319 ms                                                 | 305 ms: 1.05x faster                                                  |
| python_startup_no_site           | 13.7 ms                                                | 13.2 ms: 1.04x faster                                                 |
| regex_v8                         | 17.0 ms                                                | 16.5 ms: 1.03x faster                                                 |
| json                             | 3.04 ms                                                | 2.94 ms: 1.03x faster                                                 |
| xml_etree_parse                  | 108 ms                                                 | 105 ms: 1.03x faster                                                  |
| json_loads                       | 17.0 us                                                | 16.5 us: 1.03x faster                                                 |
| telco                            | 4.84 ms                                                | 4.74 ms: 1.02x faster                                                 |
| regex_dna                        | 149 ms                                                 | 147 ms: 1.02x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 367 ms: 1.02x faster                                                  |
| generators                       | 31.9 ms                                                | 31.5 ms: 1.02x faster                                                 |
| pathlib                          | 23.2 ms                                                | 22.9 ms: 1.01x faster                                                 |
| bpe_tokeniser                    | 3.26 sec                                               | 3.23 sec: 1.01x faster                                                |
| sympy_integrate                  | 11.3 ms                                                | 11.2 ms: 1.01x faster                                                 |
| dask                             | 771 ms                                                 | 768 ms: 1.00x faster                                                  |
| meteor_contest                   | 74.0 ms                                                | 74.3 ms: 1.00x slower                                                 |
| scimark_fft                      | 200 ms                                                 | 202 ms: 1.01x slower                                                  |
| thrift                           | 466 us                                                 | 473 us: 1.01x slower                                                  |
| float                            | 55.8 ms                                                | 56.7 ms: 1.02x slower                                                 |
| sphinx                           | 602 ms                                                 | 615 ms: 1.02x slower                                                  |
| xml_etree_generate               | 57.1 ms                                                | 58.6 ms: 1.03x slower                                                 |
| deltablue                        | 2.65 ms                                                | 2.72 ms: 1.03x slower                                                 |
| richards                         | 36.2 ms                                                | 37.4 ms: 1.03x slower                                                 |
| regex_compile                    | 78.3 ms                                                | 81.2 ms: 1.04x slower                                                 |
| typing_runtime_protocols         | 101 us                                                 | 105 us: 1.04x slower                                                  |
| fannkuch                         | 279 ms                                                 | 290 ms: 1.04x slower                                                  |
| 2to3                             | 179 ms                                                 | 186 ms: 1.04x slower                                                  |
| xml_etree_process                | 41.3 ms                                                | 43.2 ms: 1.05x slower                                                 |
| hexiom                           | 4.87 ms                                                | 5.09 ms: 1.05x slower                                                 |
| docutils                         | 1.44 sec                                               | 1.51 sec: 1.05x slower                                                |
| sqlite_synth                     | 1.55 us                                                | 1.63 us: 1.05x slower                                                 |
| sympy_expand                     | 248 ms                                                 | 261 ms: 1.05x slower                                                  |
| json_dumps                       | 6.47 ms                                                | 6.82 ms: 1.05x slower                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 53.2 ms: 1.06x slower                                                 |
| sympy_str                        | 146 ms                                                 | 154 ms: 1.06x slower                                                  |
| genshi_text                      | 16.9 ms                                                | 17.9 ms: 1.06x slower                                                 |
| pycparser                        | 701 ms                                                 | 742 ms: 1.06x slower                                                  |
| richards_super                   | 39.2 ms                                                | 41.7 ms: 1.06x slower                                                 |
| sympy_sum                        | 75.1 ms                                                | 80.3 ms: 1.07x slower                                                 |
| genshi_xml                       | 34.1 ms                                                | 36.4 ms: 1.07x slower                                                 |
| unpickle_pure_python             | 165 us                                                 | 177 us: 1.07x slower                                                  |
| coverage                         | 46.2 ms                                                | 49.7 ms: 1.07x slower                                                 |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.21 ms: 1.08x slower                                                 |
| pprint_safe_repr                 | 541 ms                                                 | 586 ms: 1.08x slower                                                  |
| bench_mp_pool                    | 64.7 ms                                                | 70.2 ms: 1.08x slower                                                 |
| pprint_pformat                   | 1.10 sec                                               | 1.19 sec: 1.09x slower                                                |
| gc_traversal                     | 2.94 ms                                                | 3.19 ms: 1.09x slower                                                 |
| logging_silent                   | 71.0 ns                                                | 77.2 ns: 1.09x slower                                                 |
| logging_format                   | 3.85 us                                                | 4.21 us: 1.09x slower                                                 |
| async_tree_eager                 | 69.9 ms                                                | 76.6 ms: 1.10x slower                                                 |
| comprehensions                   | 12.0 us                                                | 13.1 us: 1.10x slower                                                 |
| crypto_pyaes                     | 55.3 ms                                                | 60.8 ms: 1.10x slower                                                 |
| logging_simple                   | 3.56 us                                                | 3.92 us: 1.10x slower                                                 |
| bench_thread_pool                | 503 us                                                 | 556 us: 1.11x slower                                                  |
| chaos                            | 41.1 ms                                                | 46.1 ms: 1.12x slower                                                 |
| pickle_pure_python               | 215 us                                                 | 241 us: 1.12x slower                                                  |
| scimark_lu                       | 75.9 ms                                                | 85.8 ms: 1.13x slower                                                 |
| nqueens                          | 61.8 ms                                                | 70.4 ms: 1.14x slower                                                 |
| create_gc_cycles                 | 1.19 ms                                                | 1.37 ms: 1.15x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 398 ms: 1.15x slower                                                  |
| mako                             | 7.75 ms                                                | 8.96 ms: 1.16x slower                                                 |
| raytrace                         | 181 ms                                                 | 210 ms: 1.16x slower                                                  |
| nbody                            | 73.6 ms                                                | 85.7 ms: 1.16x slower                                                 |
| django_template                  | 20.5 ms                                                | 24.8 ms: 1.21x slower                                                 |
| many_optionals                   | 409 us                                                 | 501 us: 1.23x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 181 ms: 1.31x slower                                                  |
| subparsers                       | 9.44 ms                                                | 15.1 ms: 1.60x slower                                                 |
| async_tree_eager_tg              | 47.4 ms                                                | 141 ms: 2.97x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (3): asyncio_websockets, pidigits, xml_etree_iterparse
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250712-3.15.0a0-47b01da/bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.010x slower

# HPT report

- Reliability score: 63.44% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.11x