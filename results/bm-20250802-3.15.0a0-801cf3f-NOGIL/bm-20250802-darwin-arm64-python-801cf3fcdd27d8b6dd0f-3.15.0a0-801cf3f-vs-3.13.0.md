# Results vs. 3.13.0

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: darwin-arm64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.037x faster
- HPT reliability: 92.08%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 184 ms: 1.03x slower                                                  |
| docutils       | 1.44 sec                                               | 1.39 sec: 1.04x faster                                                |
| html5lib       | 36.7 ms                                                | 32.4 ms: 1.13x faster                                                 |
| sphinx         | 602 ms                                                 | 580 ms: 1.04x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 166 ms: 1.73x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 305 ms: 1.68x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 302 ms: 1.65x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 290 ms: 1.65x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 319 ms: 1.59x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 135 ms: 1.47x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 184 ms: 1.46x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 153 ms: 1.38x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 138 ms: 1.22x faster                                                  |
| coroutines                       | 20.0 ms                                                | 16.8 ms: 1.19x faster                                                 |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 379 ms: 1.18x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 397 ms: 1.16x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 357 ms: 1.05x faster                                                  |
| async_generators                 | 294 ms                                                 | 284 ms: 1.03x faster                                                  |
| asyncio_websockets               | 242 ms                                                 | 238 ms: 1.02x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 360 ms: 1.04x slower                                                  |
| async_tree_eager                 | 69.9 ms                                                | 73.8 ms: 1.06x slower                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 148 ms: 1.08x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 115 ms: 2.42x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.19x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 46.9 ms: 1.19x faster                                                 |
| pidigits       | 284 ms                                                 | 277 ms: 1.02x faster                                                  |
| nbody          | 73.6 ms                                                | 87.0 ms: 1.18x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.23 ms: 1.18x faster                                                 |
| regex_v8       | 17.0 ms                                                | 14.8 ms: 1.15x faster                                                 |
| regex_dna      | 149 ms                                                 | 137 ms: 1.09x faster                                                  |
| regex_compile  | 78.3 ms                                                | 78.0 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_iterparse  | 74.2 ms                                                | 63.3 ms: 1.17x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 95.8 ms: 1.13x faster                                                 |
| tomli_loads          | 1.57 sec                                               | 1.52 sec: 1.03x faster                                                |
| unpickle_pure_python | 165 us                                                 | 163 us: 1.01x faster                                                  |
| pickle_pure_python   | 215 us                                                 | 222 us: 1.03x slower                                                  |
| json_dumps           | 6.47 ms                                                | 6.80 ms: 1.05x slower                                                 |
| json_loads           | 17.0 us                                                | 17.9 us: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 19.0 ms: 1.01x slower                                                 |
| python_startup_no_site | 13.7 ms                                                | 14.5 ms: 1.06x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 17.5 ms: 1.03x slower                                                 |
| genshi_xml      | 34.1 ms                                                | 36.2 ms: 1.06x slower                                                 |
| django_template | 20.5 ms                                                | 23.9 ms: 1.17x slower                                                 |
| mako            | 7.75 ms                                                | 10.4 ms: 1.34x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.15x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| gc_traversal                     | 2.94 ms                                                | 1.30 ms: 2.26x faster                                                 |
| mdp                              | 1.50 sec                                               | 835 ms: 1.79x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 166 ms: 1.73x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 305 ms: 1.68x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 302 ms: 1.65x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 290 ms: 1.65x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 319 ms: 1.59x faster                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 782 us: 1.52x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 135 ms: 1.47x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 184 ms: 1.46x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 153 ms: 1.38x faster                                                  |
| go                               | 117 ms                                                 | 89.3 ms: 1.31x faster                                                 |
| deepcopy                         | 236 us                                                 | 182 us: 1.29x faster                                                  |
| generators                       | 31.9 ms                                                | 25.0 ms: 1.28x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 138 ms: 1.22x faster                                                  |
| scimark_sor                      | 106 ms                                                 | 87.3 ms: 1.21x faster                                                 |
| deepcopy_memo                    | 27.4 us                                                | 22.6 us: 1.21x faster                                                 |
| coroutines                       | 20.0 ms                                                | 16.8 ms: 1.19x faster                                                 |
| float                            | 55.8 ms                                                | 46.9 ms: 1.19x faster                                                 |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 379 ms: 1.18x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.23 ms: 1.18x faster                                                 |
| xml_etree_iterparse              | 74.2 ms                                                | 63.3 ms: 1.17x faster                                                 |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 397 ms: 1.16x faster                                                  |
| regex_v8                         | 17.0 ms                                                | 14.8 ms: 1.15x faster                                                 |
| pyflate                          | 352 ms                                                 | 307 ms: 1.15x faster                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.37 us: 1.13x faster                                                 |
| html5lib                         | 36.7 ms                                                | 32.4 ms: 1.13x faster                                                 |
| xml_etree_parse                  | 108 ms                                                 | 95.8 ms: 1.13x faster                                                 |
| dulwich_log                      | 28.7 ms                                                | 25.8 ms: 1.11x faster                                                 |
| deepcopy_reduce                  | 2.09 us                                                | 1.90 us: 1.10x faster                                                 |
| regex_dna                        | 149 ms                                                 | 137 ms: 1.09x faster                                                  |
| pylint                           | 180 ms                                                 | 166 ms: 1.08x faster                                                  |
| deltablue                        | 2.65 ms                                                | 2.48 ms: 1.07x faster                                                 |
| bpe_tokeniser                    | 3.26 sec                                               | 3.05 sec: 1.07x faster                                                |
| spectral_norm                    | 76.5 ms                                                | 72.8 ms: 1.05x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 357 ms: 1.05x faster                                                  |
| sphinx                           | 602 ms                                                 | 580 ms: 1.04x faster                                                  |
| docutils                         | 1.44 sec                                               | 1.39 sec: 1.04x faster                                                |
| async_generators                 | 294 ms                                                 | 284 ms: 1.03x faster                                                  |
| tomli_loads                      | 1.57 sec                                               | 1.52 sec: 1.03x faster                                                |
| scimark_monte_carlo              | 50.4 ms                                                | 49.2 ms: 1.02x faster                                                 |
| pidigits                         | 284 ms                                                 | 277 ms: 1.02x faster                                                  |
| asyncio_websockets               | 242 ms                                                 | 238 ms: 1.02x faster                                                  |
| unpickle_pure_python             | 165 us                                                 | 163 us: 1.01x faster                                                  |
| pathlib                          | 23.2 ms                                                | 23.0 ms: 1.01x faster                                                 |
| pycparser                        | 701 ms                                                 | 694 ms: 1.01x faster                                                  |
| regex_compile                    | 78.3 ms                                                | 78.0 ms: 1.00x faster                                                 |
| richards                         | 36.2 ms                                                | 36.5 ms: 1.01x slower                                                 |
| scimark_fft                      | 200 ms                                                 | 202 ms: 1.01x slower                                                  |
| python_startup                   | 18.8 ms                                                | 19.0 ms: 1.01x slower                                                 |
| chaos                            | 41.1 ms                                                | 41.6 ms: 1.01x slower                                                 |
| connected_components             | 319 ms                                                 | 323 ms: 1.01x slower                                                  |
| shortest_path                    | 345 ms                                                 | 351 ms: 1.01x slower                                                  |
| sympy_integrate                  | 11.3 ms                                                | 11.5 ms: 1.02x slower                                                 |
| telco                            | 4.84 ms                                                | 4.96 ms: 1.03x slower                                                 |
| fannkuch                         | 279 ms                                                 | 287 ms: 1.03x slower                                                  |
| 2to3                             | 179 ms                                                 | 184 ms: 1.03x slower                                                  |
| pickle_pure_python               | 215 us                                                 | 222 us: 1.03x slower                                                  |
| genshi_text                      | 16.9 ms                                                | 17.5 ms: 1.03x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 360 ms: 1.04x slower                                                  |
| logging_simple                   | 3.56 us                                                | 3.70 us: 1.04x slower                                                 |
| nqueens                          | 61.8 ms                                                | 64.6 ms: 1.04x slower                                                 |
| dask                             | 771 ms                                                 | 807 ms: 1.05x slower                                                  |
| json_dumps                       | 6.47 ms                                                | 6.80 ms: 1.05x slower                                                 |
| richards_super                   | 39.2 ms                                                | 41.2 ms: 1.05x slower                                                 |
| raytrace                         | 181 ms                                                 | 191 ms: 1.05x slower                                                  |
| json_loads                       | 17.0 us                                                | 17.9 us: 1.05x slower                                                 |
| comprehensions                   | 12.0 us                                                | 12.6 us: 1.05x slower                                                 |
| crypto_pyaes                     | 55.3 ms                                                | 58.3 ms: 1.05x slower                                                 |
| async_tree_eager                 | 69.9 ms                                                | 73.8 ms: 1.06x slower                                                 |
| python_startup_no_site           | 13.7 ms                                                | 14.5 ms: 1.06x slower                                                 |
| genshi_xml                       | 34.1 ms                                                | 36.2 ms: 1.06x slower                                                 |
| pprint_pformat                   | 1.10 sec                                               | 1.17 sec: 1.07x slower                                                |
| logging_silent                   | 71.0 ns                                                | 75.7 ns: 1.07x slower                                                 |
| logging_format                   | 3.85 us                                                | 4.11 us: 1.07x slower                                                 |
| thrift                           | 466 us                                                 | 497 us: 1.07x slower                                                  |
| pprint_safe_repr                 | 541 ms                                                 | 578 ms: 1.07x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 148 ms: 1.08x slower                                                  |
| sympy_str                        | 146 ms                                                 | 157 ms: 1.08x slower                                                  |
| meteor_contest                   | 74.0 ms                                                | 80.8 ms: 1.09x slower                                                 |
| sympy_sum                        | 75.1 ms                                                | 82.4 ms: 1.10x slower                                                 |
| sympy_expand                     | 248 ms                                                 | 273 ms: 1.10x slower                                                  |
| scimark_lu                       | 75.9 ms                                                | 84.4 ms: 1.11x slower                                                 |
| typing_runtime_protocols         | 101 us                                                 | 113 us: 1.12x slower                                                  |
| bench_mp_pool                    | 64.7 ms                                                | 74.3 ms: 1.15x slower                                                 |
| django_template                  | 20.5 ms                                                | 23.9 ms: 1.17x slower                                                 |
| nbody                            | 73.6 ms                                                | 87.0 ms: 1.18x slower                                                 |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.57 ms: 1.20x slower                                                 |
| coverage                         | 46.2 ms                                                | 61.7 ms: 1.33x slower                                                 |
| mako                             | 7.75 ms                                                | 10.4 ms: 1.34x slower                                                 |
| many_optionals                   | 409 us                                                 | 606 us: 1.48x slower                                                  |
| bench_thread_pool                | 503 us                                                 | 756 us: 1.50x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 115 ms: 2.42x slower                                                  |
| subparsers                       | 9.44 ms                                                | 27.2 ms: 2.88x slower                                                 |
| Geometric mean                   | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (5): k_core, json, xml_etree_generate, hexiom, xml_etree_process
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250802-3.15.0a0-801cf3f-NOGIL/bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.037x faster

# HPT report

- Reliability score: 92.08% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.26x