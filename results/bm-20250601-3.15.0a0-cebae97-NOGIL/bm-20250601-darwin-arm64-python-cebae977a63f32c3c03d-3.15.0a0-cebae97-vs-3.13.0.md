# Results vs. 3.13.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: darwin-arm64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.070x slower
- HPT reliability: 99.82%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 203 ms: 1.14x slower                                                  |
| docutils       | 1.44 sec                                               | 1.60 sec: 1.11x slower                                                |
| html5lib       | 36.7 ms                                                | 35.1 ms: 1.04x faster                                                 |
| sphinx         | 602 ms                                                 | 682 ms: 1.13x slower                                                  |
| Geometric mean | (ref)                                                  | 1.08x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 181 ms: 1.59x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 333 ms: 1.53x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 327 ms: 1.53x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 319 ms: 1.50x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 345 ms: 1.47x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 147 ms: 1.35x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 200 ms: 1.34x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 165 ms: 1.28x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 149 ms: 1.13x faster                                                  |
| coroutines                       | 20.0 ms                                                | 18.1 ms: 1.11x faster                                                 |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 414 ms: 1.08x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 434 ms: 1.06x faster                                                  |
| asyncio_websockets               | 242 ms                                                 | 238 ms: 1.02x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 392 ms: 1.05x slower                                                  |
| async_generators                 | 294 ms                                                 | 313 ms: 1.07x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 399 ms: 1.15x slower                                                  |
| async_tree_eager                 | 69.9 ms                                                | 81.8 ms: 1.17x slower                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 165 ms: 1.20x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 128 ms: 2.71x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 49.3 ms: 1.13x faster                                                 |
| pidigits       | 284 ms                                                 | 281 ms: 1.01x faster                                                  |
| nbody          | 73.6 ms                                                | 92.7 ms: 1.26x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.20 ms: 1.20x faster                                                 |
| regex_dna      | 149 ms                                                 | 145 ms: 1.03x faster                                                  |
| regex_v8       | 17.0 ms                                                | 17.1 ms: 1.00x slower                                                 |
| regex_compile  | 78.3 ms                                                | 83.8 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_iterparse  | 74.2 ms                                                | 69.2 ms: 1.07x faster                                                 |
| unpickle_pure_python | 165 us                                                 | 169 us: 1.02x slower                                                  |
| xml_etree_parse      | 108 ms                                                 | 112 ms: 1.04x slower                                                  |
| pickle_pure_python   | 215 us                                                 | 238 us: 1.11x slower                                                  |
| xml_etree_process    | 41.3 ms                                                | 50.0 ms: 1.21x slower                                                 |
| xml_etree_generate   | 57.1 ms                                                | 72.5 ms: 1.27x slower                                                 |
| json_dumps           | 6.47 ms                                                | 8.38 ms: 1.30x slower                                                 |
| json_loads           | 17.0 us                                                | 24.4 us: 1.43x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.13x slower                                                          |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 20.3 ms: 1.08x slower                                                 |
| python_startup_no_site | 13.7 ms                                                | 15.5 ms: 1.13x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 18.3 ms: 1.08x slower                                                 |
| genshi_xml      | 34.1 ms                                                | 37.6 ms: 1.10x slower                                                 |
| django_template | 20.5 ms                                                | 28.2 ms: 1.38x slower                                                 |
| mako            | 7.75 ms                                                | 11.0 ms: 1.42x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.24x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| gc_traversal                     | 2.94 ms                                                | 1.43 ms: 2.05x faster                                                 |
| async_tree_memoization_tg        | 288 ms                                                 | 181 ms: 1.59x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 333 ms: 1.53x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 327 ms: 1.53x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 319 ms: 1.50x faster                                                  |
| mdp                              | 1.50 sec                                               | 1.00 sec: 1.49x faster                                                |
| async_tree_io                    | 508 ms                                                 | 345 ms: 1.47x faster                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 855 us: 1.39x faster                                                  |
| go                               | 117 ms                                                 | 85.0 ms: 1.37x faster                                                 |
| async_tree_none_tg               | 198 ms                                                 | 147 ms: 1.35x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 200 ms: 1.34x faster                                                  |
| generators                       | 31.9 ms                                                | 24.2 ms: 1.32x faster                                                 |
| async_tree_none                  | 212 ms                                                 | 165 ms: 1.28x faster                                                  |
| deepcopy_memo                    | 27.4 us                                                | 22.5 us: 1.22x faster                                                 |
| regex_effbot                     | 2.63 ms                                                | 2.20 ms: 1.20x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 149 ms: 1.13x faster                                                  |
| float                            | 55.8 ms                                                | 49.3 ms: 1.13x faster                                                 |
| deepcopy                         | 236 us                                                 | 213 us: 1.11x faster                                                  |
| coroutines                       | 20.0 ms                                                | 18.1 ms: 1.11x faster                                                 |
| pyflate                          | 352 ms                                                 | 323 ms: 1.09x faster                                                  |
| scimark_sor                      | 106 ms                                                 | 97.0 ms: 1.09x faster                                                 |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 414 ms: 1.08x faster                                                  |
| xml_etree_iterparse              | 74.2 ms                                                | 69.2 ms: 1.07x faster                                                 |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 434 ms: 1.06x faster                                                  |
| html5lib                         | 36.7 ms                                                | 35.1 ms: 1.04x faster                                                 |
| regex_dna                        | 149 ms                                                 | 145 ms: 1.03x faster                                                  |
| asyncio_websockets               | 242 ms                                                 | 238 ms: 1.02x faster                                                  |
| pidigits                         | 284 ms                                                 | 281 ms: 1.01x faster                                                  |
| regex_v8                         | 17.0 ms                                                | 17.1 ms: 1.00x slower                                                 |
| dulwich_log                      | 28.7 ms                                                | 28.9 ms: 1.01x slower                                                 |
| hexiom                           | 4.87 ms                                                | 4.96 ms: 1.02x slower                                                 |
| unpickle_pure_python             | 165 us                                                 | 169 us: 1.02x slower                                                  |
| xml_etree_parse                  | 108 ms                                                 | 112 ms: 1.04x slower                                                  |
| deltablue                        | 2.65 ms                                                | 2.74 ms: 1.04x slower                                                 |
| connected_components             | 319 ms                                                 | 334 ms: 1.05x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 392 ms: 1.05x slower                                                  |
| pycparser                        | 701 ms                                                 | 738 ms: 1.05x slower                                                  |
| pylint                           | 180 ms                                                 | 189 ms: 1.05x slower                                                  |
| shortest_path                    | 345 ms                                                 | 365 ms: 1.06x slower                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.64 us: 1.06x slower                                                 |
| async_generators                 | 294 ms                                                 | 313 ms: 1.07x slower                                                  |
| regex_compile                    | 78.3 ms                                                | 83.8 ms: 1.07x slower                                                 |
| python_startup                   | 18.8 ms                                                | 20.3 ms: 1.08x slower                                                 |
| genshi_text                      | 16.9 ms                                                | 18.3 ms: 1.08x slower                                                 |
| k_core                           | 1.61 sec                                               | 1.74 sec: 1.08x slower                                                |
| deepcopy_reduce                  | 2.09 us                                                | 2.27 us: 1.09x slower                                                 |
| genshi_xml                       | 34.1 ms                                                | 37.6 ms: 1.10x slower                                                 |
| pickle_pure_python               | 215 us                                                 | 238 us: 1.11x slower                                                  |
| docutils                         | 1.44 sec                                               | 1.60 sec: 1.11x slower                                                |
| pathlib                          | 23.2 ms                                                | 25.8 ms: 1.11x slower                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 56.2 ms: 1.11x slower                                                 |
| meteor_contest                   | 74.0 ms                                                | 83.0 ms: 1.12x slower                                                 |
| bpe_tokeniser                    | 3.26 sec                                               | 3.66 sec: 1.12x slower                                                |
| python_startup_no_site           | 13.7 ms                                                | 15.5 ms: 1.13x slower                                                 |
| richards                         | 36.2 ms                                                | 41.0 ms: 1.13x slower                                                 |
| sphinx                           | 602 ms                                                 | 682 ms: 1.13x slower                                                  |
| 2to3                             | 179 ms                                                 | 203 ms: 1.14x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 399 ms: 1.15x slower                                                  |
| sympy_integrate                  | 11.3 ms                                                | 13.0 ms: 1.15x slower                                                 |
| async_tree_eager                 | 69.9 ms                                                | 81.8 ms: 1.17x slower                                                 |
| nqueens                          | 61.8 ms                                                | 72.5 ms: 1.17x slower                                                 |
| spectral_norm                    | 76.5 ms                                                | 90.9 ms: 1.19x slower                                                 |
| richards_super                   | 39.2 ms                                                | 46.9 ms: 1.19x slower                                                 |
| chaos                            | 41.1 ms                                                | 49.1 ms: 1.20x slower                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 165 ms: 1.20x slower                                                  |
| xml_etree_process                | 41.3 ms                                                | 50.0 ms: 1.21x slower                                                 |
| bench_mp_pool                    | 64.7 ms                                                | 78.4 ms: 1.21x slower                                                 |
| logging_simple                   | 3.56 us                                                | 4.39 us: 1.23x slower                                                 |
| logging_format                   | 3.85 us                                                | 4.82 us: 1.25x slower                                                 |
| sympy_sum                        | 75.1 ms                                                | 94.1 ms: 1.25x slower                                                 |
| nbody                            | 73.6 ms                                                | 92.7 ms: 1.26x slower                                                 |
| sympy_str                        | 146 ms                                                 | 184 ms: 1.26x slower                                                  |
| pprint_safe_repr                 | 541 ms                                                 | 684 ms: 1.27x slower                                                  |
| pprint_pformat                   | 1.10 sec                                               | 1.39 sec: 1.27x slower                                                |
| xml_etree_generate               | 57.1 ms                                                | 72.5 ms: 1.27x slower                                                 |
| crypto_pyaes                     | 55.3 ms                                                | 70.4 ms: 1.27x slower                                                 |
| comprehensions                   | 12.0 us                                                | 15.4 us: 1.29x slower                                                 |
| fannkuch                         | 279 ms                                                 | 359 ms: 1.29x slower                                                  |
| telco                            | 4.84 ms                                                | 6.25 ms: 1.29x slower                                                 |
| json_dumps                       | 6.47 ms                                                | 8.38 ms: 1.30x slower                                                 |
| raytrace                         | 181 ms                                                 | 236 ms: 1.31x slower                                                  |
| sympy_expand                     | 248 ms                                                 | 325 ms: 1.31x slower                                                  |
| json                             | 3.04 ms                                                | 4.05 ms: 1.33x slower                                                 |
| many_optionals                   | 409 us                                                 | 549 us: 1.34x slower                                                  |
| scimark_lu                       | 75.9 ms                                                | 103 ms: 1.36x slower                                                  |
| thrift                           | 466 us                                                 | 636 us: 1.36x slower                                                  |
| django_template                  | 20.5 ms                                                | 28.2 ms: 1.38x slower                                                 |
| typing_runtime_protocols         | 101 us                                                 | 140 us: 1.39x slower                                                  |
| mako                             | 7.75 ms                                                | 11.0 ms: 1.42x slower                                                 |
| json_loads                       | 17.0 us                                                | 24.4 us: 1.43x slower                                                 |
| scimark_fft                      | 200 ms                                                 | 288 ms: 1.44x slower                                                  |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 4.54 ms: 1.52x slower                                                 |
| bench_thread_pool                | 503 us                                                 | 774 us: 1.54x slower                                                  |
| coverage                         | 46.2 ms                                                | 76.0 ms: 1.64x slower                                                 |
| subparsers                       | 9.44 ms                                                | 17.0 ms: 1.80x slower                                                 |
| async_tree_eager_tg              | 47.4 ms                                                | 128 ms: 2.71x slower                                                  |
| logging_silent                   | 71.0 ns                                                | 450 ns: 6.33x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.09x slower                                                          |

Benchmark hidden because not significant (1): tomli_loads
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250601-3.15.0a0-cebae97-NOGIL/bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.070x slower

# HPT report

- Reliability score: 99.82% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.26x