# Results vs. 3.13.0

- fork: python
- ref: d3d94e0ed715829d9bf9
- machine: darwin-arm64
- commit hash: d3d94e0
- commit date: 2025-08-30
- overall geometric mean: 1.064x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 187 ms: 1.05x slower                                                  |
| html5lib       | 36.7 ms                                                | 33.2 ms: 1.10x faster                                                 |
| sphinx         | 602 ms                                                 | 576 ms: 1.04x faster                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 193 ms: 1.49x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 364 ms: 1.40x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 195 ms: 1.37x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 367 ms: 1.36x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 378 ms: 1.34x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 373 ms: 1.28x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 158 ms: 1.26x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 170 ms: 1.24x faster                                                  |
| coroutines                       | 20.0 ms                                                | 16.5 ms: 1.21x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 141 ms: 1.19x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 417 ms: 1.10x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 413 ms: 1.08x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 65.0 ms: 1.08x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 363 ms: 1.03x faster                                                  |
| async_generators                 | 294 ms                                                 | 286 ms: 1.03x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 390 ms: 1.12x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 169 ms: 1.22x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 130 ms: 2.74x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 50.6 ms: 1.10x faster                                                 |
| nbody          | 73.6 ms                                                | 71.7 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.14 ms: 1.23x faster                                                 |
| regex_v8       | 17.0 ms                                                | 15.3 ms: 1.11x faster                                                 |
| regex_dna      | 149 ms                                                 | 138 ms: 1.08x faster                                                  |
| regex_compile  | 78.3 ms                                                | 72.7 ms: 1.08x faster                                                 |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 165 us                                                 | 129 us: 1.28x faster                                                  |
| tomli_loads          | 1.57 sec                                               | 1.25 sec: 1.26x faster                                                |
| xml_etree_process    | 41.3 ms                                                | 34.7 ms: 1.19x faster                                                 |
| xml_etree_generate   | 57.1 ms                                                | 49.4 ms: 1.16x faster                                                 |
| json_dumps           | 6.47 ms                                                | 5.77 ms: 1.12x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 101 ms: 1.07x faster                                                  |
| pickle_pure_python   | 215 us                                                 | 206 us: 1.04x faster                                                  |
| xml_etree_iterparse  | 74.2 ms                                                | 71.9 ms: 1.03x faster                                                 |
| json_loads           | 17.0 us                                                | 17.4 us: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 18.9 ms: 1.01x slower                                                 |
| python_startup_no_site | 13.7 ms                                                | 14.4 ms: 1.05x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.75 ms                                                | 6.50 ms: 1.19x faster                                                 |
| genshi_text     | 16.9 ms                                                | 15.5 ms: 1.09x faster                                                 |
| genshi_xml      | 34.1 ms                                                | 33.3 ms: 1.02x faster                                                 |
| django_template | 20.5 ms                                                | 23.3 ms: 1.14x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 779 ms: 1.93x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 193 ms: 1.49x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 364 ms: 1.40x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 195 ms: 1.37x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 367 ms: 1.36x faster                                                  |
| deepcopy                         | 236 us                                                 | 174 us: 1.35x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 378 ms: 1.34x faster                                                  |
| go                               | 117 ms                                                 | 87.6 ms: 1.33x faster                                                 |
| generators                       | 31.9 ms                                                | 24.7 ms: 1.29x faster                                                 |
| unpickle_pure_python             | 165 us                                                 | 129 us: 1.28x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 373 ms: 1.28x faster                                                  |
| scimark_sor                      | 106 ms                                                 | 83.7 ms: 1.26x faster                                                 |
| deepcopy_memo                    | 27.4 us                                                | 21.8 us: 1.26x faster                                                 |
| async_tree_none_tg               | 198 ms                                                 | 158 ms: 1.26x faster                                                  |
| tomli_loads                      | 1.57 sec                                               | 1.25 sec: 1.26x faster                                                |
| async_tree_none                  | 212 ms                                                 | 170 ms: 1.24x faster                                                  |
| pyflate                          | 352 ms                                                 | 285 ms: 1.23x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.14 ms: 1.23x faster                                                 |
| telco                            | 4.84 ms                                                | 3.95 ms: 1.23x faster                                                 |
| pprint_pformat                   | 1.10 sec                                               | 900 ms: 1.22x faster                                                  |
| coroutines                       | 20.0 ms                                                | 16.5 ms: 1.21x faster                                                 |
| pprint_safe_repr                 | 541 ms                                                 | 449 ms: 1.20x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 63.8 ms: 1.20x faster                                                 |
| mako                             | 7.75 ms                                                | 6.50 ms: 1.19x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 141 ms: 1.19x faster                                                  |
| xml_etree_process                | 41.3 ms                                                | 34.7 ms: 1.19x faster                                                 |
| deepcopy_reduce                  | 2.09 us                                                | 1.80 us: 1.17x faster                                                 |
| xml_etree_generate               | 57.1 ms                                                | 49.4 ms: 1.16x faster                                                 |
| dulwich_log                      | 28.7 ms                                                | 25.3 ms: 1.14x faster                                                 |
| json_dumps                       | 6.47 ms                                                | 5.77 ms: 1.12x faster                                                 |
| fannkuch                         | 279 ms                                                 | 249 ms: 1.12x faster                                                  |
| bpe_tokeniser                    | 3.26 sec                                               | 2.92 sec: 1.12x faster                                                |
| crypto_pyaes                     | 55.3 ms                                                | 49.6 ms: 1.12x faster                                                 |
| pylint                           | 180 ms                                                 | 161 ms: 1.11x faster                                                  |
| regex_v8                         | 17.0 ms                                                | 15.3 ms: 1.11x faster                                                 |
| html5lib                         | 36.7 ms                                                | 33.2 ms: 1.10x faster                                                 |
| float                            | 55.8 ms                                                | 50.6 ms: 1.10x faster                                                 |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 417 ms: 1.10x faster                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 46.2 ms: 1.09x faster                                                 |
| genshi_text                      | 16.9 ms                                                | 15.5 ms: 1.09x faster                                                 |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 413 ms: 1.08x faster                                                  |
| regex_dna                        | 149 ms                                                 | 138 ms: 1.08x faster                                                  |
| richards                         | 36.2 ms                                                | 33.5 ms: 1.08x faster                                                 |
| regex_compile                    | 78.3 ms                                                | 72.7 ms: 1.08x faster                                                 |
| async_tree_eager                 | 69.9 ms                                                | 65.0 ms: 1.08x faster                                                 |
| logging_format                   | 3.85 us                                                | 3.58 us: 1.07x faster                                                 |
| logging_simple                   | 3.56 us                                                | 3.31 us: 1.07x faster                                                 |
| xml_etree_parse                  | 108 ms                                                 | 101 ms: 1.07x faster                                                  |
| chaos                            | 41.1 ms                                                | 38.9 ms: 1.06x faster                                                 |
| hexiom                           | 4.87 ms                                                | 4.61 ms: 1.06x faster                                                 |
| comprehensions                   | 12.0 us                                                | 11.4 us: 1.05x faster                                                 |
| richards_super                   | 39.2 ms                                                | 37.4 ms: 1.05x faster                                                 |
| deltablue                        | 2.65 ms                                                | 2.53 ms: 1.05x faster                                                 |
| sphinx                           | 602 ms                                                 | 576 ms: 1.04x faster                                                  |
| typing_runtime_protocols         | 101 us                                                 | 96.5 us: 1.04x faster                                                 |
| pickle_pure_python               | 215 us                                                 | 206 us: 1.04x faster                                                  |
| scimark_fft                      | 200 ms                                                 | 192 ms: 1.04x faster                                                  |
| sympy_integrate                  | 11.3 ms                                                | 10.9 ms: 1.04x faster                                                 |
| raytrace                         | 181 ms                                                 | 175 ms: 1.03x faster                                                  |
| xml_etree_iterparse              | 74.2 ms                                                | 71.9 ms: 1.03x faster                                                 |
| nbody                            | 73.6 ms                                                | 71.7 ms: 1.03x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 363 ms: 1.03x faster                                                  |
| async_generators                 | 294 ms                                                 | 286 ms: 1.03x faster                                                  |
| genshi_xml                       | 34.1 ms                                                | 33.3 ms: 1.02x faster                                                 |
| bench_thread_pool                | 503 us                                                 | 493 us: 1.02x faster                                                  |
| meteor_contest                   | 74.0 ms                                                | 72.7 ms: 1.02x faster                                                 |
| thrift                           | 466 us                                                 | 458 us: 1.02x faster                                                  |
| scimark_lu                       | 75.9 ms                                                | 75.6 ms: 1.00x faster                                                 |
| sqlite_synth                     | 1.55 us                                                | 1.57 us: 1.01x slower                                                 |
| python_startup                   | 18.8 ms                                                | 18.9 ms: 1.01x slower                                                 |
| nqueens                          | 61.8 ms                                                | 62.3 ms: 1.01x slower                                                 |
| connected_components             | 319 ms                                                 | 322 ms: 1.01x slower                                                  |
| shortest_path                    | 345 ms                                                 | 351 ms: 1.02x slower                                                  |
| dask                             | 771 ms                                                 | 785 ms: 1.02x slower                                                  |
| sympy_sum                        | 75.1 ms                                                | 76.7 ms: 1.02x slower                                                 |
| json_loads                       | 17.0 us                                                | 17.4 us: 1.02x slower                                                 |
| coverage                         | 46.2 ms                                                | 47.5 ms: 1.03x slower                                                 |
| logging_silent                   | 71.0 ns                                                | 73.3 ns: 1.03x slower                                                 |
| 2to3                             | 179 ms                                                 | 187 ms: 1.05x slower                                                  |
| python_startup_no_site           | 13.7 ms                                                | 14.4 ms: 1.05x slower                                                 |
| gc_traversal                     | 2.94 ms                                                | 3.17 ms: 1.08x slower                                                 |
| bench_mp_pool                    | 64.7 ms                                                | 71.7 ms: 1.11x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 390 ms: 1.12x slower                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 1.34 ms: 1.13x slower                                                 |
| django_template                  | 20.5 ms                                                | 23.3 ms: 1.14x slower                                                 |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.41 ms: 1.14x slower                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 169 ms: 1.22x slower                                                  |
| many_optionals                   | 409 us                                                 | 615 us: 1.51x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 130 ms: 2.74x slower                                                  |
| subparsers                       | 9.44 ms                                                | 26.3 ms: 2.79x slower                                                 |
| Geometric mean                   | (ref)                                                  | 1.06x faster                                                          |

Benchmark hidden because not significant (9): k_core, pycparser, sympy_str, pathlib, docutils, pidigits, sympy_expand, asyncio_websockets, json
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250830-3.15.0a0-d3d94e0-JIT/bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.064x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.13x