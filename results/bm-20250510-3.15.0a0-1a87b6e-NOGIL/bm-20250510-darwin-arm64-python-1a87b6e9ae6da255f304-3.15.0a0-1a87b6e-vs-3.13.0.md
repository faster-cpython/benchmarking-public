# Results vs. 3.13.0

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: darwin-arm64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.050x slower
- HPT reliability: 99.78%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 210 ms: 1.18x slower                                                  |
| docutils       | 1.44 sec                                               | 1.52 sec: 1.05x slower                                                |
| sphinx         | 602 ms                                                 | 637 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.07x slower                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 187 ms: 1.54x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 339 ms: 1.47x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 347 ms: 1.47x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 330 ms: 1.45x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 358 ms: 1.42x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 151 ms: 1.31x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 211 ms: 1.27x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 171 ms: 1.24x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 397 ms: 1.13x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 421 ms: 1.09x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 157 ms: 1.07x faster                                                  |
| coroutines                       | 20.0 ms                                                | 18.9 ms: 1.06x faster                                                 |
| asyncio_websockets               | 242 ms                                                 | 237 ms: 1.02x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 377 ms: 1.01x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 380 ms: 1.10x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 171 ms: 1.24x slower                                                  |
| async_tree_eager                 | 69.9 ms                                                | 86.8 ms: 1.24x slower                                                 |
| async_tree_eager_tg              | 47.4 ms                                                | 130 ms: 2.74x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (1): async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 55.2 ms: 1.01x faster                                                 |
| pidigits       | 284 ms                                                 | 281 ms: 1.01x faster                                                  |
| nbody          | 73.6 ms                                                | 95.5 ms: 1.30x slower                                                 |
| Geometric mean | (ref)                                                  | 1.08x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.12 ms: 1.24x faster                                                 |
| regex_v8       | 17.0 ms                                                | 15.2 ms: 1.12x faster                                                 |
| regex_dna      | 149 ms                                                 | 135 ms: 1.10x faster                                                  |
| regex_compile  | 78.3 ms                                                | 95.9 ms: 1.23x slower                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_iterparse  | 74.2 ms                                                | 67.4 ms: 1.10x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 99.1 ms: 1.09x faster                                                 |
| tomli_loads          | 1.57 sec                                               | 1.63 sec: 1.04x slower                                                |
| xml_etree_generate   | 57.1 ms                                                | 63.7 ms: 1.12x slower                                                 |
| json_loads           | 17.0 us                                                | 19.2 us: 1.13x slower                                                 |
| unpickle_pure_python | 165 us                                                 | 190 us: 1.15x slower                                                  |
| xml_etree_process    | 41.3 ms                                                | 48.4 ms: 1.17x slower                                                 |
| pickle_pure_python   | 215 us                                                 | 274 us: 1.28x slower                                                  |
| json_dumps           | 6.47 ms                                                | 8.32 ms: 1.29x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.10x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 18.9 ms: 1.00x slower                                                 |
| python_startup_no_site | 13.7 ms                                                | 14.5 ms: 1.06x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 34.1 ms                                                | 39.3 ms: 1.15x slower                                                 |
| genshi_text     | 16.9 ms                                                | 19.9 ms: 1.18x slower                                                 |
| django_template | 20.5 ms                                                | 28.0 ms: 1.37x slower                                                 |
| mako            | 7.75 ms                                                | 11.6 ms: 1.50x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.29x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| gc_traversal                     | 2.94 ms                                                | 1.50 ms: 1.95x faster                                                 |
| mdp                              | 1.50 sec                                               | 930 ms: 1.61x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 187 ms: 1.54x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 339 ms: 1.47x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 347 ms: 1.47x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 330 ms: 1.45x faster                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 830 us: 1.44x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 358 ms: 1.42x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 151 ms: 1.31x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 211 ms: 1.27x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.12 ms: 1.24x faster                                                 |
| async_tree_none                  | 212 ms                                                 | 171 ms: 1.24x faster                                                  |
| deepcopy                         | 236 us                                                 | 202 us: 1.17x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 397 ms: 1.13x faster                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.38 us: 1.12x faster                                                 |
| regex_v8                         | 17.0 ms                                                | 15.2 ms: 1.12x faster                                                 |
| regex_dna                        | 149 ms                                                 | 135 ms: 1.10x faster                                                  |
| xml_etree_iterparse              | 74.2 ms                                                | 67.4 ms: 1.10x faster                                                 |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 421 ms: 1.09x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 99.1 ms: 1.09x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 157 ms: 1.07x faster                                                  |
| coroutines                       | 20.0 ms                                                | 18.9 ms: 1.06x faster                                                 |
| scimark_sor                      | 106 ms                                                 | 100 ms: 1.06x faster                                                  |
| go                               | 117 ms                                                 | 111 ms: 1.05x faster                                                  |
| deepcopy_memo                    | 27.4 us                                                | 26.7 us: 1.03x faster                                                 |
| asyncio_websockets               | 242 ms                                                 | 237 ms: 1.02x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 28.2 ms: 1.02x faster                                                 |
| float                            | 55.8 ms                                                | 55.2 ms: 1.01x faster                                                 |
| pidigits                         | 284 ms                                                 | 281 ms: 1.01x faster                                                  |
| python_startup                   | 18.8 ms                                                | 18.9 ms: 1.00x slower                                                 |
| bpe_tokeniser                    | 3.26 sec                                               | 3.28 sec: 1.01x slower                                                |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 377 ms: 1.01x slower                                                  |
| k_core                           | 1.61 sec                                               | 1.64 sec: 1.02x slower                                                |
| deepcopy_reduce                  | 2.09 us                                                | 2.14 us: 1.02x slower                                                 |
| pyflate                          | 352 ms                                                 | 363 ms: 1.03x slower                                                  |
| pathlib                          | 23.2 ms                                                | 24.0 ms: 1.03x slower                                                 |
| shortest_path                    | 345 ms                                                 | 357 ms: 1.03x slower                                                  |
| connected_components             | 319 ms                                                 | 331 ms: 1.04x slower                                                  |
| tomli_loads                      | 1.57 sec                                               | 1.63 sec: 1.04x slower                                                |
| json                             | 3.04 ms                                                | 3.18 ms: 1.04x slower                                                 |
| pycparser                        | 701 ms                                                 | 736 ms: 1.05x slower                                                  |
| docutils                         | 1.44 sec                                               | 1.52 sec: 1.05x slower                                                |
| spectral_norm                    | 76.5 ms                                                | 80.6 ms: 1.05x slower                                                 |
| sphinx                           | 602 ms                                                 | 637 ms: 1.06x slower                                                  |
| python_startup_no_site           | 13.7 ms                                                | 14.5 ms: 1.06x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 380 ms: 1.10x slower                                                  |
| telco                            | 4.84 ms                                                | 5.32 ms: 1.10x slower                                                 |
| sympy_integrate                  | 11.3 ms                                                | 12.4 ms: 1.10x slower                                                 |
| xml_etree_generate               | 57.1 ms                                                | 63.7 ms: 1.12x slower                                                 |
| scimark_fft                      | 200 ms                                                 | 224 ms: 1.12x slower                                                  |
| json_loads                       | 17.0 us                                                | 19.2 us: 1.13x slower                                                 |
| meteor_contest                   | 74.0 ms                                                | 83.6 ms: 1.13x slower                                                 |
| bench_mp_pool                    | 64.7 ms                                                | 73.3 ms: 1.13x slower                                                 |
| fannkuch                         | 279 ms                                                 | 317 ms: 1.14x slower                                                  |
| thrift                           | 466 us                                                 | 532 us: 1.14x slower                                                  |
| deltablue                        | 2.65 ms                                                | 3.03 ms: 1.14x slower                                                 |
| unpickle_pure_python             | 165 us                                                 | 190 us: 1.15x slower                                                  |
| richards                         | 36.2 ms                                                | 41.6 ms: 1.15x slower                                                 |
| pprint_pformat                   | 1.10 sec                                               | 1.27 sec: 1.15x slower                                                |
| genshi_xml                       | 34.1 ms                                                | 39.3 ms: 1.15x slower                                                 |
| pprint_safe_repr                 | 541 ms                                                 | 625 ms: 1.16x slower                                                  |
| xml_etree_process                | 41.3 ms                                                | 48.4 ms: 1.17x slower                                                 |
| 2to3                             | 179 ms                                                 | 210 ms: 1.18x slower                                                  |
| genshi_text                      | 16.9 ms                                                | 19.9 ms: 1.18x slower                                                 |
| sympy_sum                        | 75.1 ms                                                | 88.7 ms: 1.18x slower                                                 |
| sympy_str                        | 146 ms                                                 | 173 ms: 1.19x slower                                                  |
| hexiom                           | 4.87 ms                                                | 5.77 ms: 1.19x slower                                                 |
| richards_super                   | 39.2 ms                                                | 46.6 ms: 1.19x slower                                                 |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.55 ms: 1.19x slower                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 60.3 ms: 1.20x slower                                                 |
| nqueens                          | 61.8 ms                                                | 74.0 ms: 1.20x slower                                                 |
| crypto_pyaes                     | 55.3 ms                                                | 66.2 ms: 1.20x slower                                                 |
| sympy_expand                     | 248 ms                                                 | 297 ms: 1.20x slower                                                  |
| regex_compile                    | 78.3 ms                                                | 95.9 ms: 1.23x slower                                                 |
| chaos                            | 41.1 ms                                                | 50.4 ms: 1.23x slower                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 171 ms: 1.24x slower                                                  |
| async_tree_eager                 | 69.9 ms                                                | 86.8 ms: 1.24x slower                                                 |
| typing_runtime_protocols         | 101 us                                                 | 125 us: 1.24x slower                                                  |
| comprehensions                   | 12.0 us                                                | 15.0 us: 1.26x slower                                                 |
| raytrace                         | 181 ms                                                 | 228 ms: 1.26x slower                                                  |
| many_optionals                   | 409 us                                                 | 517 us: 1.26x slower                                                  |
| pickle_pure_python               | 215 us                                                 | 274 us: 1.28x slower                                                  |
| json_dumps                       | 6.47 ms                                                | 8.32 ms: 1.29x slower                                                 |
| scimark_lu                       | 75.9 ms                                                | 97.8 ms: 1.29x slower                                                 |
| nbody                            | 73.6 ms                                                | 95.5 ms: 1.30x slower                                                 |
| logging_format                   | 3.85 us                                                | 5.06 us: 1.31x slower                                                 |
| logging_simple                   | 3.56 us                                                | 4.68 us: 1.32x slower                                                 |
| django_template                  | 20.5 ms                                                | 28.0 ms: 1.37x slower                                                 |
| coverage                         | 46.2 ms                                                | 66.9 ms: 1.45x slower                                                 |
| mako                             | 7.75 ms                                                | 11.6 ms: 1.50x slower                                                 |
| bench_thread_pool                | 503 us                                                 | 760 us: 1.51x slower                                                  |
| subparsers                       | 9.44 ms                                                | 15.2 ms: 1.61x slower                                                 |
| async_tree_eager_tg              | 47.4 ms                                                | 130 ms: 2.74x slower                                                  |
| logging_silent                   | 71.0 ns                                                | 377 ns: 5.31x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.07x slower                                                          |

Benchmark hidden because not significant (4): html5lib, pylint, async_generators, generators
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250510-3.15.0a0-1a87b6e-NOGIL/bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.050x slower

# HPT report

- Reliability score: 99.78% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.27x