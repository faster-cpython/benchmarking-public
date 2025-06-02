# Results vs. 3.13.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: darwin-arm64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.202x faster
- HPT reliability: 97.25%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 226 ms: 1.27x slower                                                  |
| docutils       | 1.44 sec                                               | 1.67 sec: 1.16x slower                                                |
| html5lib       | 36.7 ms                                                | 33.4 ms: 1.10x faster                                                 |
| sphinx         | 602 ms                                                 | 659 ms: 1.10x slower                                                  |
| Geometric mean | (ref)                                                  | 1.10x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 205 ms: 1.40x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 394 ms: 1.30x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 208 ms: 1.29x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 395 ms: 1.27x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 406 ms: 1.25x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 175 ms: 1.21x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 405 ms: 1.18x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 169 ms: 1.18x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 151 ms: 1.11x faster                                                  |
| coroutines                       | 20.0 ms                                                | 18.4 ms: 1.09x faster                                                 |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 454 ms: 1.01x faster                                                  |
| asyncio_websockets               | 242 ms                                                 | 243 ms: 1.00x slower                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 450 ms: 1.01x slower                                                  |
| async_tree_eager                 | 69.9 ms                                                | 73.6 ms: 1.05x slower                                                 |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 395 ms: 1.06x slower                                                  |
| async_generators                 | 294 ms                                                 | 331 ms: 1.13x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 430 ms: 1.24x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 184 ms: 1.34x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 142 ms: 3.01x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 49.2 ms: 1.13x faster                                                 |
| pidigits       | 284 ms                                                 | 284 ms: 1.00x slower                                                  |
| nbody          | 73.6 ms                                                | 77.9 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.21 ms: 1.19x faster                                                 |
| regex_compile  | 78.3 ms                                                | 68.1 ms: 1.15x faster                                                 |
| regex_dna      | 149 ms                                                 | 145 ms: 1.03x faster                                                  |
| regex_v8       | 17.0 ms                                                | 17.4 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 165 us                                                 | 151 us: 1.09x faster                                                  |
| tomli_loads          | 1.57 sec                                               | 1.44 sec: 1.09x faster                                                |
| pickle_pure_python   | 215 us                                                 | 221 us: 1.03x slower                                                  |
| xml_etree_parse      | 108 ms                                                 | 112 ms: 1.04x slower                                                  |
| xml_etree_process    | 41.3 ms                                                | 43.1 ms: 1.04x slower                                                 |
| xml_etree_iterparse  | 74.2 ms                                                | 77.5 ms: 1.04x slower                                                 |
| xml_etree_generate   | 57.1 ms                                                | 63.9 ms: 1.12x slower                                                 |
| json_dumps           | 6.47 ms                                                | 8.02 ms: 1.24x slower                                                 |
| json_loads           | 17.0 us                                                | 22.6 us: 1.33x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.07x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 17.8 ms: 1.06x faster                                                 |
| python_startup_no_site | 13.7 ms                                                | 13.2 ms: 1.04x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 15.9 ms: 1.07x faster                                                 |
| genshi_xml      | 34.1 ms                                                | 33.7 ms: 1.01x faster                                                 |
| mako            | 7.75 ms                                                | 8.24 ms: 1.06x slower                                                 |
| django_template | 20.5 ms                                                | 25.8 ms: 1.26x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.06x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pprint_pformat                   | 1.10 sec                                               | 1.01 us: 1087257.37x faster                                           |
| pprint_safe_repr                 | 541 ms                                                 | 590 ns: 915420.12x faster                                             |
| mdp                              | 1.50 sec                                               | 891 ms: 1.68x faster                                                  |
| go                               | 117 ms                                                 | 79.7 ms: 1.46x faster                                                 |
| deepcopy_memo                    | 27.4 us                                                | 19.5 us: 1.40x faster                                                 |
| async_tree_memoization_tg        | 288 ms                                                 | 205 ms: 1.40x faster                                                  |
| generators                       | 31.9 ms                                                | 23.4 ms: 1.37x faster                                                 |
| async_tree_eager_io              | 511 ms                                                 | 394 ms: 1.30x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 208 ms: 1.29x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 395 ms: 1.27x faster                                                  |
| deepcopy                         | 236 us                                                 | 187 us: 1.26x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 406 ms: 1.25x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 175 ms: 1.21x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.21 ms: 1.19x faster                                                 |
| scimark_sor                      | 106 ms                                                 | 89.3 ms: 1.18x faster                                                 |
| async_tree_eager_io_tg           | 479 ms                                                 | 405 ms: 1.18x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 169 ms: 1.18x faster                                                  |
| regex_compile                    | 78.3 ms                                                | 68.1 ms: 1.15x faster                                                 |
| float                            | 55.8 ms                                                | 49.2 ms: 1.13x faster                                                 |
| pyflate                          | 352 ms                                                 | 311 ms: 1.13x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 151 ms: 1.11x faster                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 45.8 ms: 1.10x faster                                                 |
| html5lib                         | 36.7 ms                                                | 33.4 ms: 1.10x faster                                                 |
| unpickle_pure_python             | 165 us                                                 | 151 us: 1.09x faster                                                  |
| tomli_loads                      | 1.57 sec                                               | 1.44 sec: 1.09x faster                                                |
| coroutines                       | 20.0 ms                                                | 18.4 ms: 1.09x faster                                                 |
| genshi_text                      | 16.9 ms                                                | 15.9 ms: 1.07x faster                                                 |
| python_startup                   | 18.8 ms                                                | 17.8 ms: 1.06x faster                                                 |
| deepcopy_reduce                  | 2.09 us                                                | 1.99 us: 1.05x faster                                                 |
| dulwich_log                      | 28.7 ms                                                | 27.5 ms: 1.04x faster                                                 |
| python_startup_no_site           | 13.7 ms                                                | 13.2 ms: 1.04x faster                                                 |
| hexiom                           | 4.87 ms                                                | 4.69 ms: 1.04x faster                                                 |
| regex_dna                        | 149 ms                                                 | 145 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 454 ms: 1.01x faster                                                  |
| genshi_xml                       | 34.1 ms                                                | 33.7 ms: 1.01x faster                                                 |
| pidigits                         | 284 ms                                                 | 284 ms: 1.00x slower                                                  |
| asyncio_websockets               | 242 ms                                                 | 243 ms: 1.00x slower                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 450 ms: 1.01x slower                                                  |
| richards                         | 36.2 ms                                                | 36.4 ms: 1.01x slower                                                 |
| deltablue                        | 2.65 ms                                                | 2.68 ms: 1.01x slower                                                 |
| regex_v8                         | 17.0 ms                                                | 17.4 ms: 1.02x slower                                                 |
| shortest_path                    | 345 ms                                                 | 355 ms: 1.03x slower                                                  |
| connected_components             | 319 ms                                                 | 328 ms: 1.03x slower                                                  |
| pickle_pure_python               | 215 us                                                 | 221 us: 1.03x slower                                                  |
| xml_etree_parse                  | 108 ms                                                 | 112 ms: 1.04x slower                                                  |
| k_core                           | 1.61 sec                                               | 1.68 sec: 1.04x slower                                                |
| xml_etree_process                | 41.3 ms                                                | 43.1 ms: 1.04x slower                                                 |
| xml_etree_iterparse              | 74.2 ms                                                | 77.5 ms: 1.04x slower                                                 |
| richards_super                   | 39.2 ms                                                | 41.0 ms: 1.04x slower                                                 |
| async_tree_eager                 | 69.9 ms                                                | 73.6 ms: 1.05x slower                                                 |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 395 ms: 1.06x slower                                                  |
| nbody                            | 73.6 ms                                                | 77.9 ms: 1.06x slower                                                 |
| spectral_norm                    | 76.5 ms                                                | 81.0 ms: 1.06x slower                                                 |
| mako                             | 7.75 ms                                                | 8.24 ms: 1.06x slower                                                 |
| sympy_integrate                  | 11.3 ms                                                | 12.1 ms: 1.07x slower                                                 |
| bench_thread_pool                | 503 us                                                 | 545 us: 1.08x slower                                                  |
| pathlib                          | 23.2 ms                                                | 25.2 ms: 1.09x slower                                                 |
| sphinx                           | 602 ms                                                 | 659 ms: 1.10x slower                                                  |
| chaos                            | 41.1 ms                                                | 45.1 ms: 1.10x slower                                                 |
| gc_traversal                     | 2.94 ms                                                | 3.23 ms: 1.10x slower                                                 |
| dask                             | 771 ms                                                 | 853 ms: 1.11x slower                                                  |
| meteor_contest                   | 74.0 ms                                                | 81.8 ms: 1.11x slower                                                 |
| crypto_pyaes                     | 55.3 ms                                                | 61.2 ms: 1.11x slower                                                 |
| nqueens                          | 61.8 ms                                                | 68.7 ms: 1.11x slower                                                 |
| xml_etree_generate               | 57.1 ms                                                | 63.9 ms: 1.12x slower                                                 |
| comprehensions                   | 12.0 us                                                | 13.5 us: 1.13x slower                                                 |
| async_generators                 | 294 ms                                                 | 331 ms: 1.13x slower                                                  |
| pycparser                        | 701 ms                                                 | 791 ms: 1.13x slower                                                  |
| logging_format                   | 3.85 us                                                | 4.38 us: 1.14x slower                                                 |
| logging_simple                   | 3.56 us                                                | 4.04 us: 1.14x slower                                                 |
| sympy_sum                        | 75.1 ms                                                | 86.0 ms: 1.15x slower                                                 |
| sympy_str                        | 146 ms                                                 | 167 ms: 1.15x slower                                                  |
| telco                            | 4.84 ms                                                | 5.56 ms: 1.15x slower                                                 |
| scimark_lu                       | 75.9 ms                                                | 87.3 ms: 1.15x slower                                                 |
| bpe_tokeniser                    | 3.26 sec                                               | 3.76 sec: 1.15x slower                                                |
| bench_mp_pool                    | 64.7 ms                                                | 74.8 ms: 1.16x slower                                                 |
| docutils                         | 1.44 sec                                               | 1.67 sec: 1.16x slower                                                |
| raytrace                         | 181 ms                                                 | 211 ms: 1.17x slower                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 1.40 ms: 1.17x slower                                                 |
| sympy_expand                     | 248 ms                                                 | 292 ms: 1.18x slower                                                  |
| typing_runtime_protocols         | 101 us                                                 | 123 us: 1.23x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 430 ms: 1.24x slower                                                  |
| scimark_fft                      | 200 ms                                                 | 248 ms: 1.24x slower                                                  |
| json_dumps                       | 6.47 ms                                                | 8.02 ms: 1.24x slower                                                 |
| sqlite_synth                     | 1.55 us                                                | 1.94 us: 1.25x slower                                                 |
| django_template                  | 20.5 ms                                                | 25.8 ms: 1.26x slower                                                 |
| json                             | 3.04 ms                                                | 3.84 ms: 1.26x slower                                                 |
| 2to3                             | 179 ms                                                 | 226 ms: 1.27x slower                                                  |
| fannkuch                         | 279 ms                                                 | 358 ms: 1.28x slower                                                  |
| many_optionals                   | 409 us                                                 | 535 us: 1.31x slower                                                  |
| json_loads                       | 17.0 us                                                | 22.6 us: 1.33x slower                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 184 ms: 1.34x slower                                                  |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 4.21 ms: 1.41x slower                                                 |
| subparsers                       | 9.44 ms                                                | 16.0 ms: 1.70x slower                                                 |
| async_tree_eager_tg              | 47.4 ms                                                | 142 ms: 3.01x slower                                                  |
| logging_silent                   | 71.0 ns                                                | 411 ns: 5.79x slower                                                  |
| coverage                         | 46.2 ms                                                | 308 ms: 6.66x slower                                                  |
| thrift                           | 466 us                                                 | 44.3 ms: 94.97x slower                                                |
| Geometric mean                   | (ref)                                                  | 1.18x faster                                                          |

Benchmark hidden because not significant (1): pylint
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.202x faster

# HPT report

- Reliability score: 97.25% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.08x