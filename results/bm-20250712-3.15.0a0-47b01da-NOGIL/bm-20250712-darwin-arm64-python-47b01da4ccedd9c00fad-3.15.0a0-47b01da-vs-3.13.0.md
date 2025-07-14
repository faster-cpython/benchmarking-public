# Results vs. 3.13.0

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: darwin-arm64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.061x slower
- HPT reliability: 99.76%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 210 ms: 1.18x slower                                                  |
| docutils       | 1.44 sec                                               | 1.54 sec: 1.06x slower                                                |
| html5lib       | 36.7 ms                                                | 35.2 ms: 1.04x faster                                                 |
| sphinx         | 602 ms                                                 | 641 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 191 ms: 1.51x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 347 ms: 1.47x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 342 ms: 1.46x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 333 ms: 1.44x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 366 ms: 1.39x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 152 ms: 1.30x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 209 ms: 1.28x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 177 ms: 1.19x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 399 ms: 1.12x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 418 ms: 1.10x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 156 ms: 1.08x faster                                                  |
| asyncio_websockets               | 242 ms                                                 | 238 ms: 1.02x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 374 ms: 1.00x slower                                                  |
| async_generators                 | 294 ms                                                 | 298 ms: 1.01x slower                                                  |
| coroutines                       | 20.0 ms                                                | 20.3 ms: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 384 ms: 1.11x slower                                                  |
| async_tree_eager                 | 69.9 ms                                                | 88.7 ms: 1.27x slower                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 175 ms: 1.27x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 132 ms: 2.79x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 53.5 ms: 1.04x faster                                                 |
| pidigits       | 284 ms                                                 | 281 ms: 1.01x faster                                                  |
| nbody          | 73.6 ms                                                | 98.8 ms: 1.34x slower                                                 |
| Geometric mean | (ref)                                                  | 1.08x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.12 ms: 1.24x faster                                                 |
| regex_v8       | 17.0 ms                                                | 15.0 ms: 1.13x faster                                                 |
| regex_dna      | 149 ms                                                 | 133 ms: 1.12x faster                                                  |
| regex_compile  | 78.3 ms                                                | 93.2 ms: 1.19x slower                                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_iterparse  | 74.2 ms                                                | 68.7 ms: 1.08x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 103 ms: 1.05x faster                                                  |
| json_loads           | 17.0 us                                                | 17.8 us: 1.04x slower                                                 |
| json_dumps           | 6.47 ms                                                | 7.21 ms: 1.11x slower                                                 |
| tomli_loads          | 1.57 sec                                               | 1.76 sec: 1.13x slower                                                |
| xml_etree_generate   | 57.1 ms                                                | 65.2 ms: 1.14x slower                                                 |
| xml_etree_process    | 41.3 ms                                                | 49.1 ms: 1.19x slower                                                 |
| unpickle_pure_python | 165 us                                                 | 201 us: 1.22x slower                                                  |
| pickle_pure_python   | 215 us                                                 | 265 us: 1.24x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.10x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 19.7 ms: 1.05x slower                                                 |
| python_startup_no_site | 13.7 ms                                                | 15.0 ms: 1.09x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 34.1 ms                                                | 40.6 ms: 1.19x slower                                                 |
| genshi_text     | 16.9 ms                                                | 20.6 ms: 1.22x slower                                                 |
| django_template | 20.5 ms                                                | 29.3 ms: 1.43x slower                                                 |
| mako            | 7.75 ms                                                | 11.7 ms: 1.51x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.33x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| gc_traversal                     | 2.94 ms                                                | 1.46 ms: 2.00x faster                                                 |
| mdp                              | 1.50 sec                                               | 942 ms: 1.59x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 191 ms: 1.51x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 347 ms: 1.47x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 342 ms: 1.46x faster                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 821 us: 1.45x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 333 ms: 1.44x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 366 ms: 1.39x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 152 ms: 1.30x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 209 ms: 1.28x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.12 ms: 1.24x faster                                                 |
| async_tree_none                  | 212 ms                                                 | 177 ms: 1.19x faster                                                  |
| deepcopy                         | 236 us                                                 | 207 us: 1.14x faster                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.37 us: 1.14x faster                                                 |
| regex_v8                         | 17.0 ms                                                | 15.0 ms: 1.13x faster                                                 |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 399 ms: 1.12x faster                                                  |
| regex_dna                        | 149 ms                                                 | 133 ms: 1.12x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 418 ms: 1.10x faster                                                  |
| xml_etree_iterparse              | 74.2 ms                                                | 68.7 ms: 1.08x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 156 ms: 1.08x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 103 ms: 1.05x faster                                                  |
| float                            | 55.8 ms                                                | 53.5 ms: 1.04x faster                                                 |
| html5lib                         | 36.7 ms                                                | 35.2 ms: 1.04x faster                                                 |
| k_core                           | 1.61 sec                                               | 1.55 sec: 1.04x faster                                                |
| asyncio_websockets               | 242 ms                                                 | 238 ms: 1.02x faster                                                  |
| scimark_sor                      | 106 ms                                                 | 104 ms: 1.01x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 28.4 ms: 1.01x faster                                                 |
| pidigits                         | 284 ms                                                 | 281 ms: 1.01x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 374 ms: 1.00x slower                                                  |
| deepcopy_reduce                  | 2.09 us                                                | 2.10 us: 1.00x slower                                                 |
| connected_components             | 319 ms                                                 | 320 ms: 1.01x slower                                                  |
| dask                             | 771 ms                                                 | 780 ms: 1.01x slower                                                  |
| async_generators                 | 294 ms                                                 | 298 ms: 1.01x slower                                                  |
| coroutines                       | 20.0 ms                                                | 20.3 ms: 1.01x slower                                                 |
| deepcopy_memo                    | 27.4 us                                                | 28.2 us: 1.03x slower                                                 |
| bpe_tokeniser                    | 3.26 sec                                               | 3.36 sec: 1.03x slower                                                |
| json_loads                       | 17.0 us                                                | 17.8 us: 1.04x slower                                                 |
| pycparser                        | 701 ms                                                 | 733 ms: 1.05x slower                                                  |
| python_startup                   | 18.8 ms                                                | 19.7 ms: 1.05x slower                                                 |
| pyflate                          | 352 ms                                                 | 371 ms: 1.05x slower                                                  |
| docutils                         | 1.44 sec                                               | 1.54 sec: 1.06x slower                                                |
| sphinx                           | 602 ms                                                 | 641 ms: 1.07x slower                                                  |
| telco                            | 4.84 ms                                                | 5.25 ms: 1.09x slower                                                 |
| python_startup_no_site           | 13.7 ms                                                | 15.0 ms: 1.09x slower                                                 |
| sympy_integrate                  | 11.3 ms                                                | 12.5 ms: 1.10x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 384 ms: 1.11x slower                                                  |
| json_dumps                       | 6.47 ms                                                | 7.21 ms: 1.11x slower                                                 |
| tomli_loads                      | 1.57 sec                                               | 1.76 sec: 1.13x slower                                                |
| thrift                           | 466 us                                                 | 527 us: 1.13x slower                                                  |
| spectral_norm                    | 76.5 ms                                                | 86.6 ms: 1.13x slower                                                 |
| bench_mp_pool                    | 64.7 ms                                                | 73.5 ms: 1.14x slower                                                 |
| meteor_contest                   | 74.0 ms                                                | 84.5 ms: 1.14x slower                                                 |
| xml_etree_generate               | 57.1 ms                                                | 65.2 ms: 1.14x slower                                                 |
| richards                         | 36.2 ms                                                | 41.3 ms: 1.14x slower                                                 |
| deltablue                        | 2.65 ms                                                | 3.06 ms: 1.15x slower                                                 |
| pprint_safe_repr                 | 541 ms                                                 | 625 ms: 1.16x slower                                                  |
| pprint_pformat                   | 1.10 sec                                               | 1.28 sec: 1.16x slower                                                |
| scimark_fft                      | 200 ms                                                 | 232 ms: 1.16x slower                                                  |
| sympy_sum                        | 75.1 ms                                                | 87.9 ms: 1.17x slower                                                 |
| 2to3                             | 179 ms                                                 | 210 ms: 1.18x slower                                                  |
| sympy_str                        | 146 ms                                                 | 172 ms: 1.18x slower                                                  |
| xml_etree_process                | 41.3 ms                                                | 49.1 ms: 1.19x slower                                                 |
| logging_silent                   | 71.0 ns                                                | 84.4 ns: 1.19x slower                                                 |
| regex_compile                    | 78.3 ms                                                | 93.2 ms: 1.19x slower                                                 |
| genshi_xml                       | 34.1 ms                                                | 40.6 ms: 1.19x slower                                                 |
| comprehensions                   | 12.0 us                                                | 14.3 us: 1.19x slower                                                 |
| sympy_expand                     | 248 ms                                                 | 296 ms: 1.19x slower                                                  |
| fannkuch                         | 279 ms                                                 | 333 ms: 1.20x slower                                                  |
| typing_runtime_protocols         | 101 us                                                 | 122 us: 1.21x slower                                                  |
| genshi_text                      | 16.9 ms                                                | 20.6 ms: 1.22x slower                                                 |
| unpickle_pure_python             | 165 us                                                 | 201 us: 1.22x slower                                                  |
| hexiom                           | 4.87 ms                                                | 5.95 ms: 1.22x slower                                                 |
| richards_super                   | 39.2 ms                                                | 48.2 ms: 1.23x slower                                                 |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.67 ms: 1.23x slower                                                 |
| pickle_pure_python               | 215 us                                                 | 265 us: 1.24x slower                                                  |
| crypto_pyaes                     | 55.3 ms                                                | 68.4 ms: 1.24x slower                                                 |
| chaos                            | 41.1 ms                                                | 51.3 ms: 1.25x slower                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 63.7 ms: 1.26x slower                                                 |
| logging_simple                   | 3.56 us                                                | 4.50 us: 1.26x slower                                                 |
| raytrace                         | 181 ms                                                 | 230 ms: 1.27x slower                                                  |
| async_tree_eager                 | 69.9 ms                                                | 88.7 ms: 1.27x slower                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 175 ms: 1.27x slower                                                  |
| logging_format                   | 3.85 us                                                | 4.91 us: 1.27x slower                                                 |
| many_optionals                   | 409 us                                                 | 525 us: 1.29x slower                                                  |
| nqueens                          | 61.8 ms                                                | 82.1 ms: 1.33x slower                                                 |
| nbody                            | 73.6 ms                                                | 98.8 ms: 1.34x slower                                                 |
| scimark_lu                       | 75.9 ms                                                | 106 ms: 1.39x slower                                                  |
| django_template                  | 20.5 ms                                                | 29.3 ms: 1.43x slower                                                 |
| coverage                         | 46.2 ms                                                | 66.7 ms: 1.44x slower                                                 |
| mako                             | 7.75 ms                                                | 11.7 ms: 1.51x slower                                                 |
| bench_thread_pool                | 503 us                                                 | 776 us: 1.54x slower                                                  |
| subparsers                       | 9.44 ms                                                | 15.9 ms: 1.69x slower                                                 |
| async_tree_eager_tg              | 47.4 ms                                                | 132 ms: 2.79x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.07x slower                                                          |

Benchmark hidden because not significant (6): pylint, generators, go, json, shortest_path, pathlib
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250712-3.15.0a0-47b01da-NOGIL/bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.061x slower

# HPT report

- Reliability score: 99.76% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.25x