# Results vs. 3.13.0

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: darwin-arm64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.058x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 171 ms: 1.04x faster                                                  |
| docutils       | 1.44 sec                                               | 1.46 sec: 1.01x slower                                                |
| html5lib       | 36.7 ms                                                | 33.6 ms: 1.09x faster                                                 |
| sphinx         | 602 ms                                                 | 579 ms: 1.04x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 193 ms: 1.49x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 366 ms: 1.39x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 370 ms: 1.35x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 380 ms: 1.34x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 204 ms: 1.32x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 376 ms: 1.27x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 170 ms: 1.24x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 165 ms: 1.20x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.20x faster                                                  |
| coroutines                       | 20.0 ms                                                | 17.0 ms: 1.18x faster                                                 |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 415 ms: 1.11x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 415 ms: 1.08x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 65.4 ms: 1.07x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 358 ms: 1.04x faster                                                  |
| async_generators                 | 294 ms                                                 | 288 ms: 1.02x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 390 ms: 1.12x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 166 ms: 1.20x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 129 ms: 2.73x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 51.6 ms: 1.08x faster                                                 |
| nbody          | 73.6 ms                                                | 71.7 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.14 ms: 1.23x faster                                                 |
| regex_v8       | 17.0 ms                                                | 15.3 ms: 1.11x faster                                                 |
| regex_dna      | 149 ms                                                 | 138 ms: 1.08x faster                                                  |
| regex_compile  | 78.3 ms                                                | 73.6 ms: 1.06x faster                                                 |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 165 us                                                 | 129 us: 1.28x faster                                                  |
| tomli_loads          | 1.57 sec                                               | 1.24 sec: 1.26x faster                                                |
| xml_etree_process    | 41.3 ms                                                | 34.9 ms: 1.18x faster                                                 |
| xml_etree_generate   | 57.1 ms                                                | 49.4 ms: 1.15x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 99.1 ms: 1.09x faster                                                 |
| xml_etree_iterparse  | 74.2 ms                                                | 70.8 ms: 1.05x faster                                                 |
| json_dumps           | 6.47 ms                                                | 6.28 ms: 1.03x faster                                                 |
| pickle_pure_python   | 215 us                                                 | 210 us: 1.02x faster                                                  |
| json_loads           | 17.0 us                                                | 17.4 us: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 17.0 ms: 1.10x faster                                                 |
| python_startup_no_site | 13.7 ms                                                | 12.9 ms: 1.06x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.75 ms                                                | 6.46 ms: 1.20x faster                                                 |
| genshi_text     | 16.9 ms                                                | 15.3 ms: 1.10x faster                                                 |
| genshi_xml      | 34.1 ms                                                | 33.3 ms: 1.02x faster                                                 |
| django_template | 20.5 ms                                                | 23.4 ms: 1.14x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 774 ms: 1.94x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 193 ms: 1.49x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 366 ms: 1.39x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 370 ms: 1.35x faster                                                  |
| deepcopy                         | 236 us                                                 | 175 us: 1.35x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 380 ms: 1.34x faster                                                  |
| go                               | 117 ms                                                 | 88.2 ms: 1.32x faster                                                 |
| async_tree_memoization           | 268 ms                                                 | 204 ms: 1.32x faster                                                  |
| generators                       | 31.9 ms                                                | 24.4 ms: 1.31x faster                                                 |
| unpickle_pure_python             | 165 us                                                 | 129 us: 1.28x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 376 ms: 1.27x faster                                                  |
| tomli_loads                      | 1.57 sec                                               | 1.24 sec: 1.26x faster                                                |
| async_tree_none                  | 212 ms                                                 | 170 ms: 1.24x faster                                                  |
| deepcopy_memo                    | 27.4 us                                                | 22.3 us: 1.23x faster                                                 |
| regex_effbot                     | 2.63 ms                                                | 2.14 ms: 1.23x faster                                                 |
| scimark_sor                      | 106 ms                                                 | 86.2 ms: 1.23x faster                                                 |
| spectral_norm                    | 76.5 ms                                                | 63.5 ms: 1.20x faster                                                 |
| pprint_pformat                   | 1.10 sec                                               | 916 ms: 1.20x faster                                                  |
| pyflate                          | 352 ms                                                 | 293 ms: 1.20x faster                                                  |
| mako                             | 7.75 ms                                                | 6.46 ms: 1.20x faster                                                 |
| async_tree_none_tg               | 198 ms                                                 | 165 ms: 1.20x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.20x faster                                                  |
| xml_etree_process                | 41.3 ms                                                | 34.9 ms: 1.18x faster                                                 |
| pprint_safe_repr                 | 541 ms                                                 | 457 ms: 1.18x faster                                                  |
| coroutines                       | 20.0 ms                                                | 17.0 ms: 1.18x faster                                                 |
| deepcopy_reduce                  | 2.09 us                                                | 1.79 us: 1.17x faster                                                 |
| xml_etree_generate               | 57.1 ms                                                | 49.4 ms: 1.15x faster                                                 |
| fannkuch                         | 279 ms                                                 | 246 ms: 1.13x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 25.7 ms: 1.12x faster                                                 |
| bpe_tokeniser                    | 3.26 sec                                               | 2.92 sec: 1.12x faster                                                |
| regex_v8                         | 17.0 ms                                                | 15.3 ms: 1.11x faster                                                 |
| pylint                           | 180 ms                                                 | 162 ms: 1.11x faster                                                  |
| crypto_pyaes                     | 55.3 ms                                                | 49.9 ms: 1.11x faster                                                 |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 415 ms: 1.11x faster                                                  |
| genshi_text                      | 16.9 ms                                                | 15.3 ms: 1.10x faster                                                 |
| python_startup                   | 18.8 ms                                                | 17.0 ms: 1.10x faster                                                 |
| telco                            | 4.84 ms                                                | 4.40 ms: 1.10x faster                                                 |
| html5lib                         | 36.7 ms                                                | 33.6 ms: 1.09x faster                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 46.3 ms: 1.09x faster                                                 |
| xml_etree_parse                  | 108 ms                                                 | 99.1 ms: 1.09x faster                                                 |
| float                            | 55.8 ms                                                | 51.6 ms: 1.08x faster                                                 |
| regex_dna                        | 149 ms                                                 | 138 ms: 1.08x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 415 ms: 1.08x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 65.4 ms: 1.07x faster                                                 |
| python_startup_no_site           | 13.7 ms                                                | 12.9 ms: 1.06x faster                                                 |
| regex_compile                    | 78.3 ms                                                | 73.6 ms: 1.06x faster                                                 |
| typing_runtime_protocols         | 101 us                                                 | 94.7 us: 1.06x faster                                                 |
| richards                         | 36.2 ms                                                | 34.3 ms: 1.06x faster                                                 |
| comprehensions                   | 12.0 us                                                | 11.4 us: 1.05x faster                                                 |
| xml_etree_iterparse              | 74.2 ms                                                | 70.8 ms: 1.05x faster                                                 |
| 2to3                             | 179 ms                                                 | 171 ms: 1.04x faster                                                  |
| logging_format                   | 3.85 us                                                | 3.70 us: 1.04x faster                                                 |
| scimark_fft                      | 200 ms                                                 | 192 ms: 1.04x faster                                                  |
| hexiom                           | 4.87 ms                                                | 4.67 ms: 1.04x faster                                                 |
| deltablue                        | 2.65 ms                                                | 2.54 ms: 1.04x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 358 ms: 1.04x faster                                                  |
| chaos                            | 41.1 ms                                                | 39.5 ms: 1.04x faster                                                 |
| logging_simple                   | 3.56 us                                                | 3.42 us: 1.04x faster                                                 |
| sphinx                           | 602 ms                                                 | 579 ms: 1.04x faster                                                  |
| richards_super                   | 39.2 ms                                                | 38.0 ms: 1.03x faster                                                 |
| json_dumps                       | 6.47 ms                                                | 6.28 ms: 1.03x faster                                                 |
| sympy_integrate                  | 11.3 ms                                                | 11.0 ms: 1.03x faster                                                 |
| nbody                            | 73.6 ms                                                | 71.7 ms: 1.03x faster                                                 |
| pickle_pure_python               | 215 us                                                 | 210 us: 1.02x faster                                                  |
| genshi_xml                       | 34.1 ms                                                | 33.3 ms: 1.02x faster                                                 |
| async_generators                 | 294 ms                                                 | 288 ms: 1.02x faster                                                  |
| meteor_contest                   | 74.0 ms                                                | 72.7 ms: 1.02x faster                                                 |
| thrift                           | 466 us                                                 | 459 us: 1.01x faster                                                  |
| sympy_expand                     | 248 ms                                                 | 249 ms: 1.01x slower                                                  |
| connected_components             | 319 ms                                                 | 321 ms: 1.01x slower                                                  |
| sympy_str                        | 146 ms                                                 | 147 ms: 1.01x slower                                                  |
| docutils                         | 1.44 sec                                               | 1.46 sec: 1.01x slower                                                |
| shortest_path                    | 345 ms                                                 | 350 ms: 1.01x slower                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.59 us: 1.02x slower                                                 |
| json_loads                       | 17.0 us                                                | 17.4 us: 1.02x slower                                                 |
| sympy_sum                        | 75.1 ms                                                | 77.4 ms: 1.03x slower                                                 |
| dask                             | 771 ms                                                 | 797 ms: 1.03x slower                                                  |
| coverage                         | 46.2 ms                                                | 48.2 ms: 1.04x slower                                                 |
| pycparser                        | 701 ms                                                 | 736 ms: 1.05x slower                                                  |
| pathlib                          | 23.2 ms                                                | 24.5 ms: 1.05x slower                                                 |
| gc_traversal                     | 2.94 ms                                                | 3.18 ms: 1.08x slower                                                 |
| bench_mp_pool                    | 64.7 ms                                                | 70.2 ms: 1.08x slower                                                 |
| logging_silent                   | 71.0 ns                                                | 77.0 ns: 1.09x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 390 ms: 1.12x slower                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 1.35 ms: 1.13x slower                                                 |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.39 ms: 1.14x slower                                                 |
| django_template                  | 20.5 ms                                                | 23.4 ms: 1.14x slower                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 166 ms: 1.20x slower                                                  |
| many_optionals                   | 409 us                                                 | 600 us: 1.47x slower                                                  |
| subparsers                       | 9.44 ms                                                | 25.6 ms: 2.71x slower                                                 |
| async_tree_eager_tg              | 47.4 ms                                                | 129 ms: 2.73x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.06x faster                                                          |

Benchmark hidden because not significant (8): k_core, raytrace, pidigits, bench_thread_pool, asyncio_websockets, scimark_lu, json, nqueens
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250802-3.15.0a0-801cf3f-JIT/bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.058x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.13x