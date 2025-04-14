# Results vs. 3.13.0

- fork: python
- ref: v3.14.0a5
- machine: darwin-arm64
- commit hash: 3ae9101
- commit date: 2025-02-11
- overall geometric mean: 1.025x faster
- HPT reliability: 99.57%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-darwin-arm64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 176 ms: 1.02x faster                                       |
| docutils       | 1.44 sec                                               | 1.51 sec: 1.05x slower                                     |
| html5lib       | 36.7 ms                                                | 33.1 ms: 1.11x faster                                      |
| Geometric mean | (ref)                                                  | 1.02x faster                                               |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-darwin-arm64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 208 ms: 1.38x faster                                       |
| async_tree_eager_io              | 511 ms                                                 | 394 ms: 1.30x faster                                       |
| async_tree_io_tg                 | 500 ms                                                 | 391 ms: 1.28x faster                                       |
| async_tree_memoization           | 268 ms                                                 | 211 ms: 1.27x faster                                       |
| async_tree_io                    | 508 ms                                                 | 407 ms: 1.25x faster                                       |
| async_tree_none                  | 212 ms                                                 | 173 ms: 1.22x faster                                       |
| async_tree_eager_io_tg           | 479 ms                                                 | 397 ms: 1.21x faster                                       |
| async_tree_none_tg               | 198 ms                                                 | 167 ms: 1.19x faster                                       |
| coroutines                       | 20.0 ms                                                | 17.9 ms: 1.12x faster                                      |
| async_tree_eager_memoization     | 168 ms                                                 | 151 ms: 1.11x faster                                       |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 426 ms: 1.08x faster                                       |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 429 ms: 1.04x faster                                       |
| async_generators                 | 294 ms                                                 | 283 ms: 1.04x faster                                       |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 369 ms: 1.01x faster                                       |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 401 ms: 1.15x slower                                       |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 187 ms: 1.36x slower                                       |
| async_tree_eager_tg              | 47.4 ms                                                | 141 ms: 2.97x slower                                       |
| Geometric mean                   | (ref)                                                  | 1.04x faster                                               |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_eager

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-darwin-arm64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 73.6 ms                                                | 65.0 ms: 1.13x faster                                      |
| float          | 55.8 ms                                                | 52.6 ms: 1.06x faster                                      |
| Geometric mean | (ref)                                                  | 1.06x faster                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-darwin-arm64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.24 ms: 1.17x faster                                      |
| regex_compile  | 78.3 ms                                                | 73.5 ms: 1.07x faster                                      |
| regex_dna      | 149 ms                                                 | 140 ms: 1.06x faster                                       |
| regex_v8       | 17.0 ms                                                | 16.9 ms: 1.01x faster                                      |
| Geometric mean | (ref)                                                  | 1.08x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-darwin-arm64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| unpickle_pure_python | 165 us                                                 | 134 us: 1.23x faster                                       |
| tomli_loads          | 1.57 sec                                               | 1.29 sec: 1.22x faster                                     |
| xml_etree_generate   | 57.1 ms                                                | 50.6 ms: 1.13x faster                                      |
| xml_etree_process    | 41.3 ms                                                | 36.7 ms: 1.13x faster                                      |
| xml_etree_parse      | 108 ms                                                 | 101 ms: 1.07x faster                                       |
| xml_etree_iterparse  | 74.2 ms                                                | 70.7 ms: 1.05x faster                                      |
| pickle_pure_python   | 215 us                                                 | 210 us: 1.02x faster                                       |
| json_loads           | 17.0 us                                                | 17.9 us: 1.05x slower                                      |
| json_dumps           | 6.47 ms                                                | 7.53 ms: 1.16x slower                                      |
| Geometric mean       | (ref)                                                  | 1.07x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-darwin-arm64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 17.5 ms: 1.08x faster                                      |
| python_startup_no_site | 13.7 ms                                                | 12.8 ms: 1.07x faster                                      |
| Geometric mean         | (ref)                                                  | 1.08x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-darwin-arm64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 7.75 ms                                                | 6.49 ms: 1.19x faster                                      |
| genshi_text     | 16.9 ms                                                | 15.8 ms: 1.07x faster                                      |
| genshi_xml      | 34.1 ms                                                | 33.3 ms: 1.02x faster                                      |
| django_template | 20.5 ms                                                | 23.9 ms: 1.17x slower                                      |
| Geometric mean  | (ref)                                                  | 1.03x faster                                               |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-darwin-arm64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| deepcopy                         | 236 us                                                 | 168 us: 1.41x faster                                       |
| async_tree_memoization_tg        | 288 ms                                                 | 208 ms: 1.38x faster                                       |
| async_tree_eager_io              | 511 ms                                                 | 394 ms: 1.30x faster                                       |
| deepcopy_memo                    | 27.4 us                                                | 21.2 us: 1.29x faster                                      |
| async_tree_io_tg                 | 500 ms                                                 | 391 ms: 1.28x faster                                       |
| async_tree_memoization           | 268 ms                                                 | 211 ms: 1.27x faster                                       |
| async_tree_io                    | 508 ms                                                 | 407 ms: 1.25x faster                                       |
| go                               | 117 ms                                                 | 94.2 ms: 1.24x faster                                      |
| unpickle_pure_python             | 165 us                                                 | 134 us: 1.23x faster                                       |
| async_tree_none                  | 212 ms                                                 | 173 ms: 1.22x faster                                       |
| tomli_loads                      | 1.57 sec                                               | 1.29 sec: 1.22x faster                                     |
| async_tree_eager_io_tg           | 479 ms                                                 | 397 ms: 1.21x faster                                       |
| mako                             | 7.75 ms                                                | 6.49 ms: 1.19x faster                                      |
| async_tree_none_tg               | 198 ms                                                 | 167 ms: 1.19x faster                                       |
| deepcopy_reduce                  | 2.09 us                                                | 1.77 us: 1.18x faster                                      |
| regex_effbot                     | 2.63 ms                                                | 2.24 ms: 1.17x faster                                      |
| scimark_fft                      | 200 ms                                                 | 172 ms: 1.16x faster                                       |
| pyflate                          | 352 ms                                                 | 303 ms: 1.16x faster                                       |
| scimark_sor                      | 106 ms                                                 | 92.3 ms: 1.15x faster                                      |
| spectral_norm                    | 76.5 ms                                                | 66.9 ms: 1.14x faster                                      |
| nbody                            | 73.6 ms                                                | 65.0 ms: 1.13x faster                                      |
| bpe_tokeniser                    | 3.26 sec                                               | 2.88 sec: 1.13x faster                                     |
| xml_etree_generate               | 57.1 ms                                                | 50.6 ms: 1.13x faster                                      |
| xml_etree_process                | 41.3 ms                                                | 36.7 ms: 1.13x faster                                      |
| generators                       | 31.9 ms                                                | 28.5 ms: 1.12x faster                                      |
| coroutines                       | 20.0 ms                                                | 17.9 ms: 1.12x faster                                      |
| async_tree_eager_memoization     | 168 ms                                                 | 151 ms: 1.11x faster                                       |
| html5lib                         | 36.7 ms                                                | 33.1 ms: 1.11x faster                                      |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 426 ms: 1.08x faster                                       |
| telco                            | 4.84 ms                                                | 4.49 ms: 1.08x faster                                      |
| python_startup                   | 18.8 ms                                                | 17.5 ms: 1.08x faster                                      |
| python_startup_no_site           | 13.7 ms                                                | 12.8 ms: 1.07x faster                                      |
| bench_mp_pool                    | 64.7 ms                                                | 60.3 ms: 1.07x faster                                      |
| genshi_text                      | 16.9 ms                                                | 15.8 ms: 1.07x faster                                      |
| connected_components             | 319 ms                                                 | 299 ms: 1.07x faster                                       |
| xml_etree_parse                  | 108 ms                                                 | 101 ms: 1.07x faster                                       |
| regex_compile                    | 78.3 ms                                                | 73.5 ms: 1.07x faster                                      |
| regex_dna                        | 149 ms                                                 | 140 ms: 1.06x faster                                       |
| float                            | 55.8 ms                                                | 52.6 ms: 1.06x faster                                      |
| pylint                           | 180 ms                                                 | 170 ms: 1.06x faster                                       |
| k_core                           | 1.61 sec                                               | 1.53 sec: 1.05x faster                                     |
| shortest_path                    | 345 ms                                                 | 329 ms: 1.05x faster                                       |
| xml_etree_iterparse              | 74.2 ms                                                | 70.7 ms: 1.05x faster                                      |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 429 ms: 1.04x faster                                       |
| pprint_pformat                   | 1.10 sec                                               | 1.06 sec: 1.04x faster                                     |
| pprint_safe_repr                 | 541 ms                                                 | 519 ms: 1.04x faster                                       |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 2.87 ms: 1.04x faster                                      |
| async_generators                 | 294 ms                                                 | 283 ms: 1.04x faster                                       |
| fannkuch                         | 279 ms                                                 | 272 ms: 1.03x faster                                       |
| crypto_pyaes                     | 55.3 ms                                                | 53.9 ms: 1.02x faster                                      |
| pickle_pure_python               | 215 us                                                 | 210 us: 1.02x faster                                       |
| genshi_xml                       | 34.1 ms                                                | 33.3 ms: 1.02x faster                                      |
| scimark_monte_carlo              | 50.4 ms                                                | 49.4 ms: 1.02x faster                                      |
| 2to3                             | 179 ms                                                 | 176 ms: 1.02x faster                                       |
| json                             | 3.04 ms                                                | 3.01 ms: 1.01x faster                                      |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 369 ms: 1.01x faster                                       |
| thrift                           | 466 us                                                 | 461 us: 1.01x faster                                       |
| regex_v8                         | 17.0 ms                                                | 16.9 ms: 1.01x faster                                      |
| dask                             | 771 ms                                                 | 768 ms: 1.01x faster                                       |
| sqlite_synth                     | 1.55 us                                                | 1.55 us: 1.00x faster                                      |
| typing_runtime_protocols         | 101 us                                                 | 102 us: 1.01x slower                                       |
| logging_simple                   | 3.56 us                                                | 3.60 us: 1.01x slower                                      |
| logging_format                   | 3.85 us                                                | 3.91 us: 1.01x slower                                      |
| meteor_contest                   | 74.0 ms                                                | 75.0 ms: 1.01x slower                                      |
| pycparser                        | 701 ms                                                 | 713 ms: 1.02x slower                                       |
| hexiom                           | 4.87 ms                                                | 4.97 ms: 1.02x slower                                      |
| sqlglot_transpile                | 1.04 ms                                                | 1.06 ms: 1.03x slower                                      |
| sqlglot_optimize                 | 34.7 ms                                                | 35.6 ms: 1.03x slower                                      |
| coverage                         | 46.2 ms                                                | 47.5 ms: 1.03x slower                                      |
| bench_thread_pool                | 503 us                                                 | 518 us: 1.03x slower                                       |
| dulwich_log                      | 28.7 ms                                                | 29.6 ms: 1.03x slower                                      |
| sympy_expand                     | 248 ms                                                 | 256 ms: 1.03x slower                                       |
| sympy_str                        | 146 ms                                                 | 151 ms: 1.03x slower                                       |
| nqueens                          | 61.8 ms                                                | 64.0 ms: 1.04x slower                                      |
| sqlglot_parse                    | 852 us                                                 | 887 us: 1.04x slower                                       |
| richards                         | 36.2 ms                                                | 37.7 ms: 1.04x slower                                      |
| sqlglot_normalize                | 188 ms                                                 | 196 ms: 1.04x slower                                       |
| sympy_sum                        | 75.1 ms                                                | 78.4 ms: 1.04x slower                                      |
| sqlalchemy_declarative           | 59.0 ms                                                | 61.7 ms: 1.05x slower                                      |
| deltablue                        | 2.65 ms                                                | 2.77 ms: 1.05x slower                                      |
| docutils                         | 1.44 sec                                               | 1.51 sec: 1.05x slower                                     |
| json_loads                       | 17.0 us                                                | 17.9 us: 1.05x slower                                      |
| mdp                              | 1.50 sec                                               | 1.58 sec: 1.05x slower                                     |
| gc_traversal                     | 2.94 ms                                                | 3.11 ms: 1.06x slower                                      |
| sqlalchemy_imperative            | 6.69 ms                                                | 7.10 ms: 1.06x slower                                      |
| richards_super                   | 39.2 ms                                                | 41.7 ms: 1.06x slower                                      |
| logging_silent                   | 71.0 ns                                                | 75.6 ns: 1.07x slower                                      |
| chaos                            | 41.1 ms                                                | 43.8 ms: 1.07x slower                                      |
| sympy_integrate                  | 11.3 ms                                                | 12.1 ms: 1.07x slower                                      |
| create_gc_cycles                 | 1.19 ms                                                | 1.28 ms: 1.08x slower                                      |
| comprehensions                   | 12.0 us                                                | 13.0 us: 1.09x slower                                      |
| scimark_lu                       | 75.9 ms                                                | 83.0 ms: 1.09x slower                                      |
| raytrace                         | 181 ms                                                 | 199 ms: 1.10x slower                                       |
| many_optionals                   | 409 us                                                 | 470 us: 1.15x slower                                       |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 401 ms: 1.15x slower                                       |
| json_dumps                       | 6.47 ms                                                | 7.53 ms: 1.16x slower                                      |
| django_template                  | 20.5 ms                                                | 23.9 ms: 1.17x slower                                      |
| subparsers                       | 9.44 ms                                                | 12.5 ms: 1.32x slower                                      |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 187 ms: 1.36x slower                                       |
| async_tree_eager_tg              | 47.4 ms                                                | 141 ms: 2.97x slower                                       |
| Geometric mean                   | (ref)                                                  | 1.03x faster                                               |

Benchmark hidden because not significant (5): sphinx, asyncio_websockets, async_tree_eager, pidigits, pathlib
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.025x faster

# HPT report

- Reliability score: 99.57% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x