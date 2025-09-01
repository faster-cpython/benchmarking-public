# Results vs. 3.13.0

- fork: python
- ref: d3d94e0ed715829d9bf9
- machine: darwin-arm64
- commit hash: d3d94e0
- commit date: 2025-08-30
- overall geometric mean: 1.054x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 170 ms: 1.05x faster                                                  |
| docutils       | 1.44 sec                                               | 1.43 sec: 1.01x faster                                                |
| html5lib       | 36.7 ms                                                | 32.5 ms: 1.13x faster                                                 |
| sphinx         | 602 ms                                                 | 573 ms: 1.05x faster                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 194 ms: 1.48x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 370 ms: 1.38x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 197 ms: 1.36x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 376 ms: 1.33x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 385 ms: 1.32x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 377 ms: 1.27x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 160 ms: 1.24x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 172 ms: 1.23x faster                                                  |
| coroutines                       | 20.0 ms                                                | 16.3 ms: 1.23x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 142 ms: 1.19x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 420 ms: 1.09x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 414 ms: 1.08x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 65.9 ms: 1.06x faster                                                 |
| async_generators                 | 294 ms                                                 | 279 ms: 1.05x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 360 ms: 1.03x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 391 ms: 1.13x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 170 ms: 1.23x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 131 ms: 2.77x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 49.1 ms: 1.14x faster                                                 |
| nbody          | 73.6 ms                                                | 80.0 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.13 ms: 1.23x faster                                                 |
| regex_v8       | 17.0 ms                                                | 15.6 ms: 1.09x faster                                                 |
| regex_dna      | 149 ms                                                 | 137 ms: 1.08x faster                                                  |
| regex_compile  | 78.3 ms                                                | 72.4 ms: 1.08x faster                                                 |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 6.47 ms                                                | 5.67 ms: 1.14x faster                                                 |
| tomli_loads          | 1.57 sec                                               | 1.41 sec: 1.11x faster                                                |
| unpickle_pure_python | 165 us                                                 | 155 us: 1.06x faster                                                  |
| xml_etree_process    | 41.3 ms                                                | 39.5 ms: 1.05x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 103 ms: 1.05x faster                                                  |
| xml_etree_generate   | 57.1 ms                                                | 55.6 ms: 1.03x faster                                                 |
| xml_etree_iterparse  | 74.2 ms                                                | 72.3 ms: 1.03x faster                                                 |
| pickle_pure_python   | 215 us                                                 | 216 us: 1.01x slower                                                  |
| json_loads           | 17.0 us                                                | 17.4 us: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 13.7 ms                                                | 14.3 ms: 1.04x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                          |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 14.9 ms: 1.14x faster                                                 |
| genshi_xml      | 34.1 ms                                                | 32.6 ms: 1.04x faster                                                 |
| mako            | 7.75 ms                                                | 8.04 ms: 1.04x slower                                                 |
| django_template | 20.5 ms                                                | 23.0 ms: 1.13x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 772 ms: 1.94x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 194 ms: 1.48x faster                                                  |
| go                               | 117 ms                                                 | 84.0 ms: 1.39x faster                                                 |
| deepcopy                         | 236 us                                                 | 171 us: 1.38x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 370 ms: 1.38x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 197 ms: 1.36x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 376 ms: 1.33x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 385 ms: 1.32x faster                                                  |
| generators                       | 31.9 ms                                                | 24.4 ms: 1.31x faster                                                 |
| deepcopy_memo                    | 27.4 us                                                | 21.2 us: 1.29x faster                                                 |
| scimark_sor                      | 106 ms                                                 | 83.1 ms: 1.27x faster                                                 |
| async_tree_eager_io_tg           | 479 ms                                                 | 377 ms: 1.27x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 160 ms: 1.24x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.13 ms: 1.23x faster                                                 |
| async_tree_none                  | 212 ms                                                 | 172 ms: 1.23x faster                                                  |
| coroutines                       | 20.0 ms                                                | 16.3 ms: 1.23x faster                                                 |
| spectral_norm                    | 76.5 ms                                                | 62.8 ms: 1.22x faster                                                 |
| deepcopy_reduce                  | 2.09 us                                                | 1.76 us: 1.19x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 142 ms: 1.19x faster                                                  |
| pyflate                          | 352 ms                                                 | 301 ms: 1.17x faster                                                  |
| telco                            | 4.84 ms                                                | 4.16 ms: 1.16x faster                                                 |
| dulwich_log                      | 28.7 ms                                                | 25.2 ms: 1.14x faster                                                 |
| json_dumps                       | 6.47 ms                                                | 5.67 ms: 1.14x faster                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 44.4 ms: 1.14x faster                                                 |
| genshi_text                      | 16.9 ms                                                | 14.9 ms: 1.14x faster                                                 |
| float                            | 55.8 ms                                                | 49.1 ms: 1.14x faster                                                 |
| html5lib                         | 36.7 ms                                                | 32.5 ms: 1.13x faster                                                 |
| pylint                           | 180 ms                                                 | 161 ms: 1.12x faster                                                  |
| tomli_loads                      | 1.57 sec                                               | 1.41 sec: 1.11x faster                                                |
| deltablue                        | 2.65 ms                                                | 2.42 ms: 1.10x faster                                                 |
| regex_v8                         | 17.0 ms                                                | 15.6 ms: 1.09x faster                                                 |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 420 ms: 1.09x faster                                                  |
| logging_simple                   | 3.56 us                                                | 3.26 us: 1.09x faster                                                 |
| richards                         | 36.2 ms                                                | 33.2 ms: 1.09x faster                                                 |
| logging_format                   | 3.85 us                                                | 3.55 us: 1.08x faster                                                 |
| regex_dna                        | 149 ms                                                 | 137 ms: 1.08x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 414 ms: 1.08x faster                                                  |
| regex_compile                    | 78.3 ms                                                | 72.4 ms: 1.08x faster                                                 |
| hexiom                           | 4.87 ms                                                | 4.53 ms: 1.07x faster                                                 |
| crypto_pyaes                     | 55.3 ms                                                | 51.6 ms: 1.07x faster                                                 |
| scimark_fft                      | 200 ms                                                 | 187 ms: 1.07x faster                                                  |
| unpickle_pure_python             | 165 us                                                 | 155 us: 1.06x faster                                                  |
| k_core                           | 1.61 sec                                               | 1.52 sec: 1.06x faster                                                |
| async_tree_eager                 | 69.9 ms                                                | 65.9 ms: 1.06x faster                                                 |
| chaos                            | 41.1 ms                                                | 38.8 ms: 1.06x faster                                                 |
| richards_super                   | 39.2 ms                                                | 37.2 ms: 1.05x faster                                                 |
| async_generators                 | 294 ms                                                 | 279 ms: 1.05x faster                                                  |
| 2to3                             | 179 ms                                                 | 170 ms: 1.05x faster                                                  |
| sphinx                           | 602 ms                                                 | 573 ms: 1.05x faster                                                  |
| sympy_integrate                  | 11.3 ms                                                | 10.8 ms: 1.05x faster                                                 |
| xml_etree_process                | 41.3 ms                                                | 39.5 ms: 1.05x faster                                                 |
| xml_etree_parse                  | 108 ms                                                 | 103 ms: 1.05x faster                                                  |
| genshi_xml                       | 34.1 ms                                                | 32.6 ms: 1.04x faster                                                 |
| connected_components             | 319 ms                                                 | 306 ms: 1.04x faster                                                  |
| bpe_tokeniser                    | 3.26 sec                                               | 3.14 sec: 1.04x faster                                                |
| typing_runtime_protocols         | 101 us                                                 | 97.1 us: 1.04x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 360 ms: 1.03x faster                                                  |
| shortest_path                    | 345 ms                                                 | 334 ms: 1.03x faster                                                  |
| scimark_lu                       | 75.9 ms                                                | 73.8 ms: 1.03x faster                                                 |
| xml_etree_generate               | 57.1 ms                                                | 55.6 ms: 1.03x faster                                                 |
| xml_etree_iterparse              | 74.2 ms                                                | 72.3 ms: 1.03x faster                                                 |
| raytrace                         | 181 ms                                                 | 177 ms: 1.02x faster                                                  |
| pycparser                        | 701 ms                                                 | 687 ms: 1.02x faster                                                  |
| bench_thread_pool                | 503 us                                                 | 493 us: 1.02x faster                                                  |
| comprehensions                   | 12.0 us                                                | 11.7 us: 1.02x faster                                                 |
| thrift                           | 466 us                                                 | 458 us: 1.02x faster                                                  |
| nqueens                          | 61.8 ms                                                | 61.0 ms: 1.01x faster                                                 |
| fannkuch                         | 279 ms                                                 | 276 ms: 1.01x faster                                                  |
| meteor_contest                   | 74.0 ms                                                | 73.4 ms: 1.01x faster                                                 |
| sympy_expand                     | 248 ms                                                 | 246 ms: 1.01x faster                                                  |
| docutils                         | 1.44 sec                                               | 1.43 sec: 1.01x faster                                                |
| pprint_pformat                   | 1.10 sec                                               | 1.11 sec: 1.00x slower                                                |
| pickle_pure_python               | 215 us                                                 | 216 us: 1.01x slower                                                  |
| pprint_safe_repr                 | 541 ms                                                 | 546 ms: 1.01x slower                                                  |
| logging_silent                   | 71.0 ns                                                | 71.9 ns: 1.01x slower                                                 |
| dask                             | 771 ms                                                 | 786 ms: 1.02x slower                                                  |
| json_loads                       | 17.0 us                                                | 17.4 us: 1.02x slower                                                 |
| sympy_sum                        | 75.1 ms                                                | 77.1 ms: 1.03x slower                                                 |
| coverage                         | 46.2 ms                                                | 47.8 ms: 1.03x slower                                                 |
| sqlite_synth                     | 1.55 us                                                | 1.61 us: 1.04x slower                                                 |
| mako                             | 7.75 ms                                                | 8.04 ms: 1.04x slower                                                 |
| python_startup_no_site           | 13.7 ms                                                | 14.3 ms: 1.04x slower                                                 |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.12 ms: 1.05x slower                                                 |
| gc_traversal                     | 2.94 ms                                                | 3.16 ms: 1.08x slower                                                 |
| nbody                            | 73.6 ms                                                | 80.0 ms: 1.09x slower                                                 |
| bench_mp_pool                    | 64.7 ms                                                | 71.4 ms: 1.10x slower                                                 |
| django_template                  | 20.5 ms                                                | 23.0 ms: 1.13x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 391 ms: 1.13x slower                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 1.34 ms: 1.13x slower                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 170 ms: 1.23x slower                                                  |
| many_optionals                   | 409 us                                                 | 594 us: 1.45x slower                                                  |
| subparsers                       | 9.44 ms                                                | 25.4 ms: 2.69x slower                                                 |
| async_tree_eager_tg              | 47.4 ms                                                | 131 ms: 2.77x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (6): pathlib, json, python_startup, pidigits, asyncio_websockets, sympy_str
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250830-3.15.0a0-d3d94e0/bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.054x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.12x