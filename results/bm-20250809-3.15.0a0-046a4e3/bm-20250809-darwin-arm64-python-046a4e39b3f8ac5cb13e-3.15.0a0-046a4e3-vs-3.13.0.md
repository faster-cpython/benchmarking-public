# Results vs. 3.13.0

- fork: python
- ref: 046a4e39b3f8ac5cb13e
- machine: darwin-arm64
- commit hash: 046a4e3
- commit date: 2025-08-09
- overall geometric mean: 1.049x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 171 ms: 1.05x faster                                                  |
| docutils       | 1.44 sec                                               | 1.44 sec: 1.01x faster                                                |
| html5lib       | 36.7 ms                                                | 33.0 ms: 1.11x faster                                                 |
| sphinx         | 602 ms                                                 | 576 ms: 1.04x faster                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 193 ms: 1.49x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 197 ms: 1.36x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 376 ms: 1.36x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 370 ms: 1.35x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 382 ms: 1.33x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 376 ms: 1.27x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 168 ms: 1.26x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 160 ms: 1.24x faster                                                  |
| coroutines                       | 20.0 ms                                                | 16.4 ms: 1.22x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 139 ms: 1.21x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 420 ms: 1.09x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 413 ms: 1.08x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 65.1 ms: 1.08x faster                                                 |
| async_generators                 | 294 ms                                                 | 279 ms: 1.05x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 357 ms: 1.05x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 387 ms: 1.12x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 171 ms: 1.24x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 133 ms: 2.81x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 50.6 ms: 1.10x faster                                                 |
| nbody          | 73.6 ms                                                | 81.3 ms: 1.10x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.15 ms: 1.23x faster                                                 |
| regex_v8       | 17.0 ms                                                | 15.3 ms: 1.11x faster                                                 |
| regex_dna      | 149 ms                                                 | 138 ms: 1.08x faster                                                  |
| regex_compile  | 78.3 ms                                                | 73.1 ms: 1.07x faster                                                 |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 6.47 ms                                                | 5.77 ms: 1.12x faster                                                 |
| tomli_loads          | 1.57 sec                                               | 1.44 sec: 1.08x faster                                                |
| xml_etree_parse      | 108 ms                                                 | 101 ms: 1.06x faster                                                  |
| unpickle_pure_python | 165 us                                                 | 158 us: 1.04x faster                                                  |
| xml_etree_iterparse  | 74.2 ms                                                | 71.2 ms: 1.04x faster                                                 |
| xml_etree_process    | 41.3 ms                                                | 39.7 ms: 1.04x faster                                                 |
| xml_etree_generate   | 57.1 ms                                                | 55.6 ms: 1.03x faster                                                 |
| pickle_pure_python   | 215 us                                                 | 219 us: 1.02x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 17.6 ms: 1.07x faster                                                 |
| python_startup_no_site | 13.7 ms                                                | 13.3 ms: 1.03x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 15.2 ms: 1.11x faster                                                 |
| genshi_xml      | 34.1 ms                                                | 32.7 ms: 1.04x faster                                                 |
| mako            | 7.75 ms                                                | 7.95 ms: 1.03x slower                                                 |
| django_template | 20.5 ms                                                | 23.0 ms: 1.12x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 776 ms: 1.93x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 193 ms: 1.49x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 197 ms: 1.36x faster                                                  |
| deepcopy                         | 236 us                                                 | 173 us: 1.36x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 376 ms: 1.36x faster                                                  |
| go                               | 117 ms                                                 | 86.1 ms: 1.36x faster                                                 |
| async_tree_io_tg                 | 500 ms                                                 | 370 ms: 1.35x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 382 ms: 1.33x faster                                                  |
| generators                       | 31.9 ms                                                | 24.3 ms: 1.32x faster                                                 |
| async_tree_eager_io_tg           | 479 ms                                                 | 376 ms: 1.27x faster                                                  |
| deepcopy_memo                    | 27.4 us                                                | 21.7 us: 1.26x faster                                                 |
| async_tree_none                  | 212 ms                                                 | 168 ms: 1.26x faster                                                  |
| scimark_sor                      | 106 ms                                                 | 85.1 ms: 1.24x faster                                                 |
| async_tree_none_tg               | 198 ms                                                 | 160 ms: 1.24x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.15 ms: 1.23x faster                                                 |
| coroutines                       | 20.0 ms                                                | 16.4 ms: 1.22x faster                                                 |
| spectral_norm                    | 76.5 ms                                                | 62.8 ms: 1.22x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 139 ms: 1.21x faster                                                  |
| deepcopy_reduce                  | 2.09 us                                                | 1.77 us: 1.18x faster                                                 |
| pyflate                          | 352 ms                                                 | 306 ms: 1.15x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 25.0 ms: 1.15x faster                                                 |
| json_dumps                       | 6.47 ms                                                | 5.77 ms: 1.12x faster                                                 |
| pylint                           | 180 ms                                                 | 161 ms: 1.12x faster                                                  |
| genshi_text                      | 16.9 ms                                                | 15.2 ms: 1.11x faster                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 45.3 ms: 1.11x faster                                                 |
| html5lib                         | 36.7 ms                                                | 33.0 ms: 1.11x faster                                                 |
| regex_v8                         | 17.0 ms                                                | 15.3 ms: 1.11x faster                                                 |
| float                            | 55.8 ms                                                | 50.6 ms: 1.10x faster                                                 |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 420 ms: 1.09x faster                                                  |
| tomli_loads                      | 1.57 sec                                               | 1.44 sec: 1.08x faster                                                |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 413 ms: 1.08x faster                                                  |
| deltablue                        | 2.65 ms                                                | 2.44 ms: 1.08x faster                                                 |
| regex_dna                        | 149 ms                                                 | 138 ms: 1.08x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 65.1 ms: 1.08x faster                                                 |
| richards                         | 36.2 ms                                                | 33.8 ms: 1.07x faster                                                 |
| regex_compile                    | 78.3 ms                                                | 73.1 ms: 1.07x faster                                                 |
| python_startup                   | 18.8 ms                                                | 17.6 ms: 1.07x faster                                                 |
| xml_etree_parse                  | 108 ms                                                 | 101 ms: 1.06x faster                                                  |
| logging_format                   | 3.85 us                                                | 3.63 us: 1.06x faster                                                 |
| scimark_fft                      | 200 ms                                                 | 188 ms: 1.06x faster                                                  |
| logging_simple                   | 3.56 us                                                | 3.36 us: 1.06x faster                                                 |
| telco                            | 4.84 ms                                                | 4.58 ms: 1.06x faster                                                 |
| k_core                           | 1.61 sec                                               | 1.53 sec: 1.05x faster                                                |
| typing_runtime_protocols         | 101 us                                                 | 95.7 us: 1.05x faster                                                 |
| async_generators                 | 294 ms                                                 | 279 ms: 1.05x faster                                                  |
| crypto_pyaes                     | 55.3 ms                                                | 52.7 ms: 1.05x faster                                                 |
| hexiom                           | 4.87 ms                                                | 4.64 ms: 1.05x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 357 ms: 1.05x faster                                                  |
| chaos                            | 41.1 ms                                                | 39.3 ms: 1.05x faster                                                 |
| 2to3                             | 179 ms                                                 | 171 ms: 1.05x faster                                                  |
| sphinx                           | 602 ms                                                 | 576 ms: 1.04x faster                                                  |
| sympy_integrate                  | 11.3 ms                                                | 10.8 ms: 1.04x faster                                                 |
| unpickle_pure_python             | 165 us                                                 | 158 us: 1.04x faster                                                  |
| xml_etree_iterparse              | 74.2 ms                                                | 71.2 ms: 1.04x faster                                                 |
| xml_etree_process                | 41.3 ms                                                | 39.7 ms: 1.04x faster                                                 |
| connected_components             | 319 ms                                                 | 306 ms: 1.04x faster                                                  |
| genshi_xml                       | 34.1 ms                                                | 32.7 ms: 1.04x faster                                                 |
| richards_super                   | 39.2 ms                                                | 37.8 ms: 1.04x faster                                                 |
| python_startup_no_site           | 13.7 ms                                                | 13.3 ms: 1.03x faster                                                 |
| shortest_path                    | 345 ms                                                 | 336 ms: 1.03x faster                                                  |
| xml_etree_generate               | 57.1 ms                                                | 55.6 ms: 1.03x faster                                                 |
| thrift                           | 466 us                                                 | 455 us: 1.02x faster                                                  |
| bpe_tokeniser                    | 3.26 sec                                               | 3.19 sec: 1.02x faster                                                |
| raytrace                         | 181 ms                                                 | 178 ms: 1.02x faster                                                  |
| comprehensions                   | 12.0 us                                                | 11.7 us: 1.02x faster                                                 |
| json                             | 3.04 ms                                                | 2.99 ms: 1.02x faster                                                 |
| pycparser                        | 701 ms                                                 | 694 ms: 1.01x faster                                                  |
| nqueens                          | 61.8 ms                                                | 61.4 ms: 1.01x faster                                                 |
| docutils                         | 1.44 sec                                               | 1.44 sec: 1.01x faster                                                |
| pprint_pformat                   | 1.10 sec                                               | 1.10 sec: 1.00x faster                                                |
| sympy_expand                     | 248 ms                                                 | 247 ms: 1.00x faster                                                  |
| coverage                         | 46.2 ms                                                | 46.4 ms: 1.00x slower                                                 |
| pickle_pure_python               | 215 us                                                 | 219 us: 1.02x slower                                                  |
| mako                             | 7.75 ms                                                | 7.95 ms: 1.03x slower                                                 |
| sympy_sum                        | 75.1 ms                                                | 77.2 ms: 1.03x slower                                                 |
| dask                             | 771 ms                                                 | 795 ms: 1.03x slower                                                  |
| pathlib                          | 23.2 ms                                                | 24.2 ms: 1.04x slower                                                 |
| fannkuch                         | 279 ms                                                 | 293 ms: 1.05x slower                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.64 us: 1.05x slower                                                 |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.14 ms: 1.05x slower                                                 |
| logging_silent                   | 71.0 ns                                                | 75.2 ns: 1.06x slower                                                 |
| gc_traversal                     | 2.94 ms                                                | 3.21 ms: 1.09x slower                                                 |
| bench_mp_pool                    | 64.7 ms                                                | 71.0 ms: 1.10x slower                                                 |
| nbody                            | 73.6 ms                                                | 81.3 ms: 1.10x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 387 ms: 1.12x slower                                                  |
| django_template                  | 20.5 ms                                                | 23.0 ms: 1.12x slower                                                 |
| create_gc_cycles                 | 1.19 ms                                                | 1.36 ms: 1.14x slower                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 171 ms: 1.24x slower                                                  |
| many_optionals                   | 409 us                                                 | 593 us: 1.45x slower                                                  |
| subparsers                       | 9.44 ms                                                | 25.3 ms: 2.68x slower                                                 |
| async_tree_eager_tg              | 47.4 ms                                                | 133 ms: 2.81x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (8): bench_thread_pool, pprint_safe_repr, asyncio_websockets, scimark_lu, pidigits, meteor_contest, json_loads, sympy_str
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.049x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.11x