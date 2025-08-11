# Results vs. 3.13.0

- fork: python
- ref: 046a4e39b3f8ac5cb13e
- machine: darwin-arm64
- commit hash: 046a4e3
- commit date: 2025-08-09
- overall geometric mean: 1.062x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 171 ms: 1.05x faster                                                  |
| docutils       | 1.44 sec                                               | 1.45 sec: 1.00x slower                                                |
| html5lib       | 36.7 ms                                                | 33.5 ms: 1.09x faster                                                 |
| sphinx         | 602 ms                                                 | 576 ms: 1.04x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 193 ms: 1.49x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 195 ms: 1.37x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 376 ms: 1.36x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 370 ms: 1.35x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 377 ms: 1.35x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 166 ms: 1.27x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 377 ms: 1.27x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 159 ms: 1.25x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 139 ms: 1.21x faster                                                  |
| coroutines                       | 20.0 ms                                                | 16.6 ms: 1.21x faster                                                 |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 419 ms: 1.10x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 64.4 ms: 1.09x faster                                                 |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 413 ms: 1.08x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 356 ms: 1.05x faster                                                  |
| async_generators                 | 294 ms                                                 | 285 ms: 1.03x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 388 ms: 1.12x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 171 ms: 1.24x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 133 ms: 2.80x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 51.1 ms: 1.09x faster                                                 |
| nbody          | 73.6 ms                                                | 72.4 ms: 1.02x faster                                                 |
| pidigits       | 284 ms                                                 | 285 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.13 ms: 1.24x faster                                                 |
| regex_v8       | 17.0 ms                                                | 15.5 ms: 1.10x faster                                                 |
| regex_dna      | 149 ms                                                 | 138 ms: 1.08x faster                                                  |
| regex_compile  | 78.3 ms                                                | 72.7 ms: 1.08x faster                                                 |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 165 us                                                 | 128 us: 1.29x faster                                                  |
| tomli_loads          | 1.57 sec                                               | 1.24 sec: 1.26x faster                                                |
| xml_etree_process    | 41.3 ms                                                | 34.6 ms: 1.19x faster                                                 |
| xml_etree_generate   | 57.1 ms                                                | 49.3 ms: 1.16x faster                                                 |
| json_dumps           | 6.47 ms                                                | 5.81 ms: 1.11x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 100 ms: 1.08x faster                                                  |
| xml_etree_iterparse  | 74.2 ms                                                | 71.1 ms: 1.04x faster                                                 |
| pickle_pure_python   | 215 us                                                 | 209 us: 1.03x faster                                                  |
| json_loads           | 17.0 us                                                | 17.5 us: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 18.0 ms: 1.04x faster                                                 |
| python_startup_no_site | 13.7 ms                                                | 13.6 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.75 ms                                                | 6.53 ms: 1.19x faster                                                 |
| genshi_text     | 16.9 ms                                                | 15.4 ms: 1.10x faster                                                 |
| genshi_xml      | 34.1 ms                                                | 33.0 ms: 1.03x faster                                                 |
| django_template | 20.5 ms                                                | 23.1 ms: 1.13x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 776 ms: 1.93x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 193 ms: 1.49x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 195 ms: 1.37x faster                                                  |
| deepcopy                         | 236 us                                                 | 173 us: 1.36x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 376 ms: 1.36x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 370 ms: 1.35x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 377 ms: 1.35x faster                                                  |
| go                               | 117 ms                                                 | 87.4 ms: 1.34x faster                                                 |
| generators                       | 31.9 ms                                                | 24.4 ms: 1.31x faster                                                 |
| unpickle_pure_python             | 165 us                                                 | 128 us: 1.29x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 166 ms: 1.27x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 377 ms: 1.27x faster                                                  |
| deepcopy_memo                    | 27.4 us                                                | 21.6 us: 1.27x faster                                                 |
| tomli_loads                      | 1.57 sec                                               | 1.24 sec: 1.26x faster                                                |
| async_tree_none_tg               | 198 ms                                                 | 159 ms: 1.25x faster                                                  |
| scimark_sor                      | 106 ms                                                 | 85.1 ms: 1.24x faster                                                 |
| regex_effbot                     | 2.63 ms                                                | 2.13 ms: 1.24x faster                                                 |
| pprint_pformat                   | 1.10 sec                                               | 901 ms: 1.22x faster                                                  |
| pyflate                          | 352 ms                                                 | 289 ms: 1.22x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 139 ms: 1.21x faster                                                  |
| pprint_safe_repr                 | 541 ms                                                 | 448 ms: 1.21x faster                                                  |
| coroutines                       | 20.0 ms                                                | 16.6 ms: 1.21x faster                                                 |
| xml_etree_process                | 41.3 ms                                                | 34.6 ms: 1.19x faster                                                 |
| spectral_norm                    | 76.5 ms                                                | 64.3 ms: 1.19x faster                                                 |
| mako                             | 7.75 ms                                                | 6.53 ms: 1.19x faster                                                 |
| deepcopy_reduce                  | 2.09 us                                                | 1.78 us: 1.18x faster                                                 |
| xml_etree_generate               | 57.1 ms                                                | 49.3 ms: 1.16x faster                                                 |
| dulwich_log                      | 28.7 ms                                                | 25.4 ms: 1.13x faster                                                 |
| fannkuch                         | 279 ms                                                 | 249 ms: 1.12x faster                                                  |
| json_dumps                       | 6.47 ms                                                | 5.81 ms: 1.11x faster                                                 |
| crypto_pyaes                     | 55.3 ms                                                | 49.7 ms: 1.11x faster                                                 |
| pylint                           | 180 ms                                                 | 162 ms: 1.11x faster                                                  |
| bpe_tokeniser                    | 3.26 sec                                               | 2.93 sec: 1.11x faster                                                |
| scimark_monte_carlo              | 50.4 ms                                                | 45.6 ms: 1.11x faster                                                 |
| regex_v8                         | 17.0 ms                                                | 15.5 ms: 1.10x faster                                                 |
| genshi_text                      | 16.9 ms                                                | 15.4 ms: 1.10x faster                                                 |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 419 ms: 1.10x faster                                                  |
| html5lib                         | 36.7 ms                                                | 33.5 ms: 1.09x faster                                                 |
| float                            | 55.8 ms                                                | 51.1 ms: 1.09x faster                                                 |
| async_tree_eager                 | 69.9 ms                                                | 64.4 ms: 1.09x faster                                                 |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 413 ms: 1.08x faster                                                  |
| telco                            | 4.84 ms                                                | 4.47 ms: 1.08x faster                                                 |
| xml_etree_parse                  | 108 ms                                                 | 100 ms: 1.08x faster                                                  |
| regex_dna                        | 149 ms                                                 | 138 ms: 1.08x faster                                                  |
| regex_compile                    | 78.3 ms                                                | 72.7 ms: 1.08x faster                                                 |
| richards                         | 36.2 ms                                                | 33.8 ms: 1.07x faster                                                 |
| logging_simple                   | 3.56 us                                                | 3.37 us: 1.06x faster                                                 |
| logging_format                   | 3.85 us                                                | 3.65 us: 1.05x faster                                                 |
| typing_runtime_protocols         | 101 us                                                 | 95.5 us: 1.05x faster                                                 |
| chaos                            | 41.1 ms                                                | 39.2 ms: 1.05x faster                                                 |
| comprehensions                   | 12.0 us                                                | 11.4 us: 1.05x faster                                                 |
| hexiom                           | 4.87 ms                                                | 4.65 ms: 1.05x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 356 ms: 1.05x faster                                                  |
| 2to3                             | 179 ms                                                 | 171 ms: 1.05x faster                                                  |
| richards_super                   | 39.2 ms                                                | 37.5 ms: 1.05x faster                                                 |
| xml_etree_iterparse              | 74.2 ms                                                | 71.1 ms: 1.04x faster                                                 |
| sphinx                           | 602 ms                                                 | 576 ms: 1.04x faster                                                  |
| python_startup                   | 18.8 ms                                                | 18.0 ms: 1.04x faster                                                 |
| deltablue                        | 2.65 ms                                                | 2.55 ms: 1.04x faster                                                 |
| sympy_integrate                  | 11.3 ms                                                | 10.9 ms: 1.03x faster                                                 |
| genshi_xml                       | 34.1 ms                                                | 33.0 ms: 1.03x faster                                                 |
| meteor_contest                   | 74.0 ms                                                | 71.7 ms: 1.03x faster                                                 |
| async_generators                 | 294 ms                                                 | 285 ms: 1.03x faster                                                  |
| scimark_fft                      | 200 ms                                                 | 194 ms: 1.03x faster                                                  |
| pickle_pure_python               | 215 us                                                 | 209 us: 1.03x faster                                                  |
| raytrace                         | 181 ms                                                 | 177 ms: 1.02x faster                                                  |
| thrift                           | 466 us                                                 | 457 us: 1.02x faster                                                  |
| nbody                            | 73.6 ms                                                | 72.4 ms: 1.02x faster                                                 |
| bench_thread_pool                | 503 us                                                 | 498 us: 1.01x faster                                                  |
| python_startup_no_site           | 13.7 ms                                                | 13.6 ms: 1.01x faster                                                 |
| pidigits                         | 284 ms                                                 | 285 ms: 1.00x slower                                                  |
| docutils                         | 1.44 sec                                               | 1.45 sec: 1.00x slower                                                |
| nqueens                          | 61.8 ms                                                | 62.2 ms: 1.01x slower                                                 |
| sympy_str                        | 146 ms                                                 | 147 ms: 1.01x slower                                                  |
| connected_components             | 319 ms                                                 | 322 ms: 1.01x slower                                                  |
| shortest_path                    | 345 ms                                                 | 350 ms: 1.01x slower                                                  |
| scimark_lu                       | 75.9 ms                                                | 77.1 ms: 1.02x slower                                                 |
| sqlite_synth                     | 1.55 us                                                | 1.58 us: 1.02x slower                                                 |
| sympy_sum                        | 75.1 ms                                                | 76.9 ms: 1.02x slower                                                 |
| json_loads                       | 17.0 us                                                | 17.5 us: 1.02x slower                                                 |
| dask                             | 771 ms                                                 | 797 ms: 1.03x slower                                                  |
| coverage                         | 46.2 ms                                                | 48.0 ms: 1.04x slower                                                 |
| logging_silent                   | 71.0 ns                                                | 75.2 ns: 1.06x slower                                                 |
| gc_traversal                     | 2.94 ms                                                | 3.20 ms: 1.09x slower                                                 |
| pathlib                          | 23.2 ms                                                | 25.8 ms: 1.11x slower                                                 |
| bench_mp_pool                    | 64.7 ms                                                | 72.0 ms: 1.11x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 388 ms: 1.12x slower                                                  |
| django_template                  | 20.5 ms                                                | 23.1 ms: 1.13x slower                                                 |
| create_gc_cycles                 | 1.19 ms                                                | 1.36 ms: 1.14x slower                                                 |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.42 ms: 1.15x slower                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 171 ms: 1.24x slower                                                  |
| many_optionals                   | 409 us                                                 | 598 us: 1.46x slower                                                  |
| subparsers                       | 9.44 ms                                                | 25.4 ms: 2.69x slower                                                 |
| async_tree_eager_tg              | 47.4 ms                                                | 133 ms: 2.80x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.06x faster                                                          |

Benchmark hidden because not significant (5): k_core, asyncio_websockets, sympy_expand, pycparser, json
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.062x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.13x