# Results vs. 3.13.0

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: darwin-arm64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.049x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 173 ms: 1.03x faster                                                  |
| docutils       | 1.44 sec                                               | 1.45 sec: 1.01x slower                                                |
| html5lib       | 36.7 ms                                                | 33.1 ms: 1.11x faster                                                 |
| sphinx         | 602 ms                                                 | 582 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 193 ms: 1.49x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 366 ms: 1.39x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 196 ms: 1.37x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 382 ms: 1.33x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 383 ms: 1.31x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 375 ms: 1.28x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 167 ms: 1.27x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 159 ms: 1.24x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 139 ms: 1.21x faster                                                  |
| coroutines                       | 20.0 ms                                                | 16.6 ms: 1.21x faster                                                 |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 419 ms: 1.10x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 413 ms: 1.08x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 64.9 ms: 1.08x faster                                                 |
| async_generators                 | 294 ms                                                 | 275 ms: 1.07x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 357 ms: 1.05x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 387 ms: 1.11x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 171 ms: 1.24x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 131 ms: 2.76x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 50.1 ms: 1.11x faster                                                 |
| pidigits       | 284 ms                                                 | 284 ms: 1.00x slower                                                  |
| nbody          | 73.6 ms                                                | 80.0 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.15 ms: 1.22x faster                                                 |
| regex_v8       | 17.0 ms                                                | 15.5 ms: 1.10x faster                                                 |
| regex_dna      | 149 ms                                                 | 139 ms: 1.07x faster                                                  |
| regex_compile  | 78.3 ms                                                | 74.0 ms: 1.06x faster                                                 |
| Geometric mean | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 165 us                                                 | 156 us: 1.06x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 103 ms: 1.05x faster                                                  |
| xml_etree_process    | 41.3 ms                                                | 39.7 ms: 1.04x faster                                                 |
| tomli_loads          | 1.57 sec                                               | 1.51 sec: 1.04x faster                                                |
| xml_etree_iterparse  | 74.2 ms                                                | 71.8 ms: 1.03x faster                                                 |
| xml_etree_generate   | 57.1 ms                                                | 56.0 ms: 1.02x faster                                                 |
| pickle_pure_python   | 215 us                                                 | 216 us: 1.00x slower                                                  |
| json_dumps           | 6.47 ms                                                | 6.63 ms: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 16.9 ms: 1.11x faster                                                 |
| python_startup_no_site | 13.7 ms                                                | 12.7 ms: 1.08x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 15.4 ms: 1.10x faster                                                 |
| genshi_xml      | 34.1 ms                                                | 33.0 ms: 1.03x faster                                                 |
| mako            | 7.75 ms                                                | 8.09 ms: 1.04x slower                                                 |
| django_template | 20.5 ms                                                | 22.8 ms: 1.11x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 774 ms: 1.94x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 193 ms: 1.49x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 366 ms: 1.39x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 196 ms: 1.37x faster                                                  |
| go                               | 117 ms                                                 | 85.7 ms: 1.36x faster                                                 |
| deepcopy                         | 236 us                                                 | 173 us: 1.36x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 382 ms: 1.33x faster                                                  |
| generators                       | 31.9 ms                                                | 24.1 ms: 1.32x faster                                                 |
| async_tree_io_tg                 | 500 ms                                                 | 383 ms: 1.31x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 375 ms: 1.28x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 167 ms: 1.27x faster                                                  |
| scimark_sor                      | 106 ms                                                 | 84.3 ms: 1.25x faster                                                 |
| deepcopy_memo                    | 27.4 us                                                | 21.9 us: 1.25x faster                                                 |
| async_tree_none_tg               | 198 ms                                                 | 159 ms: 1.24x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 62.6 ms: 1.22x faster                                                 |
| regex_effbot                     | 2.63 ms                                                | 2.15 ms: 1.22x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 139 ms: 1.21x faster                                                  |
| coroutines                       | 20.0 ms                                                | 16.6 ms: 1.21x faster                                                 |
| deepcopy_reduce                  | 2.09 us                                                | 1.78 us: 1.18x faster                                                 |
| pyflate                          | 352 ms                                                 | 306 ms: 1.15x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 25.2 ms: 1.14x faster                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 45.2 ms: 1.12x faster                                                 |
| float                            | 55.8 ms                                                | 50.1 ms: 1.11x faster                                                 |
| python_startup                   | 18.8 ms                                                | 16.9 ms: 1.11x faster                                                 |
| deltablue                        | 2.65 ms                                                | 2.39 ms: 1.11x faster                                                 |
| html5lib                         | 36.7 ms                                                | 33.1 ms: 1.11x faster                                                 |
| pylint                           | 180 ms                                                 | 162 ms: 1.11x faster                                                  |
| genshi_text                      | 16.9 ms                                                | 15.4 ms: 1.10x faster                                                 |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 419 ms: 1.10x faster                                                  |
| regex_v8                         | 17.0 ms                                                | 15.5 ms: 1.10x faster                                                 |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 413 ms: 1.08x faster                                                  |
| python_startup_no_site           | 13.7 ms                                                | 12.7 ms: 1.08x faster                                                 |
| async_tree_eager                 | 69.9 ms                                                | 64.9 ms: 1.08x faster                                                 |
| richards                         | 36.2 ms                                                | 33.6 ms: 1.08x faster                                                 |
| regex_dna                        | 149 ms                                                 | 139 ms: 1.07x faster                                                  |
| logging_simple                   | 3.56 us                                                | 3.34 us: 1.07x faster                                                 |
| scimark_fft                      | 200 ms                                                 | 187 ms: 1.07x faster                                                  |
| async_generators                 | 294 ms                                                 | 275 ms: 1.07x faster                                                  |
| hexiom                           | 4.87 ms                                                | 4.58 ms: 1.06x faster                                                 |
| crypto_pyaes                     | 55.3 ms                                                | 52.1 ms: 1.06x faster                                                 |
| chaos                            | 41.1 ms                                                | 38.7 ms: 1.06x faster                                                 |
| regex_compile                    | 78.3 ms                                                | 74.0 ms: 1.06x faster                                                 |
| unpickle_pure_python             | 165 us                                                 | 156 us: 1.06x faster                                                  |
| logging_format                   | 3.85 us                                                | 3.64 us: 1.06x faster                                                 |
| k_core                           | 1.61 sec                                               | 1.53 sec: 1.05x faster                                                |
| telco                            | 4.84 ms                                                | 4.60 ms: 1.05x faster                                                 |
| xml_etree_parse                  | 108 ms                                                 | 103 ms: 1.05x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 357 ms: 1.05x faster                                                  |
| thrift                           | 466 us                                                 | 447 us: 1.04x faster                                                  |
| sympy_integrate                  | 11.3 ms                                                | 10.9 ms: 1.04x faster                                                 |
| connected_components             | 319 ms                                                 | 306 ms: 1.04x faster                                                  |
| typing_runtime_protocols         | 101 us                                                 | 96.8 us: 1.04x faster                                                 |
| richards_super                   | 39.2 ms                                                | 37.7 ms: 1.04x faster                                                 |
| xml_etree_process                | 41.3 ms                                                | 39.7 ms: 1.04x faster                                                 |
| raytrace                         | 181 ms                                                 | 175 ms: 1.04x faster                                                  |
| bpe_tokeniser                    | 3.26 sec                                               | 3.14 sec: 1.04x faster                                                |
| tomli_loads                      | 1.57 sec                                               | 1.51 sec: 1.04x faster                                                |
| sphinx                           | 602 ms                                                 | 582 ms: 1.03x faster                                                  |
| xml_etree_iterparse              | 74.2 ms                                                | 71.8 ms: 1.03x faster                                                 |
| 2to3                             | 179 ms                                                 | 173 ms: 1.03x faster                                                  |
| genshi_xml                       | 34.1 ms                                                | 33.0 ms: 1.03x faster                                                 |
| shortest_path                    | 345 ms                                                 | 337 ms: 1.03x faster                                                  |
| pprint_safe_repr                 | 541 ms                                                 | 529 ms: 1.02x faster                                                  |
| pprint_pformat                   | 1.10 sec                                               | 1.08 sec: 1.02x faster                                                |
| xml_etree_generate               | 57.1 ms                                                | 56.0 ms: 1.02x faster                                                 |
| json                             | 3.04 ms                                                | 2.99 ms: 1.02x faster                                                 |
| pycparser                        | 701 ms                                                 | 692 ms: 1.01x faster                                                  |
| nqueens                          | 61.8 ms                                                | 61.5 ms: 1.00x faster                                                 |
| comprehensions                   | 12.0 us                                                | 11.9 us: 1.00x faster                                                 |
| pidigits                         | 284 ms                                                 | 284 ms: 1.00x slower                                                  |
| bench_thread_pool                | 503 us                                                 | 505 us: 1.00x slower                                                  |
| pickle_pure_python               | 215 us                                                 | 216 us: 1.00x slower                                                  |
| scimark_lu                       | 75.9 ms                                                | 76.4 ms: 1.01x slower                                                 |
| docutils                         | 1.44 sec                                               | 1.45 sec: 1.01x slower                                                |
| logging_silent                   | 71.0 ns                                                | 71.5 ns: 1.01x slower                                                 |
| sympy_str                        | 146 ms                                                 | 147 ms: 1.01x slower                                                  |
| meteor_contest                   | 74.0 ms                                                | 75.0 ms: 1.01x slower                                                 |
| sqlite_synth                     | 1.55 us                                                | 1.59 us: 1.02x slower                                                 |
| json_dumps                       | 6.47 ms                                                | 6.63 ms: 1.02x slower                                                 |
| fannkuch                         | 279 ms                                                 | 286 ms: 1.03x slower                                                  |
| sympy_sum                        | 75.1 ms                                                | 77.6 ms: 1.03x slower                                                 |
| dask                             | 771 ms                                                 | 797 ms: 1.03x slower                                                  |
| pathlib                          | 23.2 ms                                                | 24.1 ms: 1.04x slower                                                 |
| mako                             | 7.75 ms                                                | 8.09 ms: 1.04x slower                                                 |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.12 ms: 1.05x slower                                                 |
| bench_mp_pool                    | 64.7 ms                                                | 69.6 ms: 1.08x slower                                                 |
| gc_traversal                     | 2.94 ms                                                | 3.17 ms: 1.08x slower                                                 |
| nbody                            | 73.6 ms                                                | 80.0 ms: 1.09x slower                                                 |
| django_template                  | 20.5 ms                                                | 22.8 ms: 1.11x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 387 ms: 1.11x slower                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 1.35 ms: 1.13x slower                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 171 ms: 1.24x slower                                                  |
| many_optionals                   | 409 us                                                 | 591 us: 1.45x slower                                                  |
| subparsers                       | 9.44 ms                                                | 25.5 ms: 2.70x slower                                                 |
| async_tree_eager_tg              | 47.4 ms                                                | 131 ms: 2.76x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (4): coverage, sympy_expand, json_loads, asyncio_websockets
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.049x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.11x