# Results vs. 3.13.0

- fork: python
- ref: fba5dded6df3c2b19435
- machine: darwin-arm64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.063x slower
- HPT reliability: 99.63%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 202 ms: 1.13x slower                                                  |
| docutils       | 1.44 sec                                               | 1.59 sec: 1.10x slower                                                |
| html5lib       | 36.7 ms                                                | 34.3 ms: 1.07x faster                                                 |
| sphinx         | 602 ms                                                 | 678 ms: 1.13x slower                                                  |
| Geometric mean | (ref)                                                  | 1.07x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 180 ms: 1.60x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 332 ms: 1.54x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 327 ms: 1.53x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 317 ms: 1.51x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 343 ms: 1.48x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 146 ms: 1.36x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 198 ms: 1.35x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 164 ms: 1.29x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 148 ms: 1.14x faster                                                  |
| coroutines                       | 20.0 ms                                                | 18.0 ms: 1.11x faster                                                 |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 413 ms: 1.08x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 432 ms: 1.06x faster                                                  |
| asyncio_websockets               | 242 ms                                                 | 238 ms: 1.02x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 391 ms: 1.05x slower                                                  |
| async_generators                 | 294 ms                                                 | 324 ms: 1.10x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 397 ms: 1.14x slower                                                  |
| async_tree_eager                 | 69.9 ms                                                | 81.9 ms: 1.17x slower                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 163 ms: 1.18x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 127 ms: 2.68x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 48.6 ms: 1.15x faster                                                 |
| pidigits       | 284 ms                                                 | 281 ms: 1.01x faster                                                  |
| nbody          | 73.6 ms                                                | 93.1 ms: 1.27x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.22 ms: 1.18x faster                                                 |
| regex_dna      | 149 ms                                                 | 145 ms: 1.03x faster                                                  |
| regex_v8       | 17.0 ms                                                | 17.1 ms: 1.00x slower                                                 |
| regex_compile  | 78.3 ms                                                | 83.7 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_iterparse  | 74.2 ms                                                | 69.2 ms: 1.07x faster                                                 |
| tomli_loads          | 1.57 sec                                               | 1.55 sec: 1.01x faster                                                |
| unpickle_pure_python | 165 us                                                 | 169 us: 1.02x slower                                                  |
| xml_etree_parse      | 108 ms                                                 | 111 ms: 1.03x slower                                                  |
| pickle_pure_python   | 215 us                                                 | 237 us: 1.10x slower                                                  |
| xml_etree_process    | 41.3 ms                                                | 50.0 ms: 1.21x slower                                                 |
| xml_etree_generate   | 57.1 ms                                                | 72.5 ms: 1.27x slower                                                 |
| json_dumps           | 6.47 ms                                                | 8.33 ms: 1.29x slower                                                 |
| json_loads           | 17.0 us                                                | 24.5 us: 1.44x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.13x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 20.5 ms: 1.09x slower                                                 |
| python_startup_no_site | 13.7 ms                                                | 15.5 ms: 1.13x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 18.4 ms: 1.09x slower                                                 |
| genshi_xml      | 34.1 ms                                                | 39.3 ms: 1.15x slower                                                 |
| django_template | 20.5 ms                                                | 28.4 ms: 1.39x slower                                                 |
| mako            | 7.75 ms                                                | 10.8 ms: 1.40x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.25x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| gc_traversal                     | 2.94 ms                                                | 1.41 ms: 2.08x faster                                                 |
| async_tree_memoization_tg        | 288 ms                                                 | 180 ms: 1.60x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 332 ms: 1.54x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 327 ms: 1.53x faster                                                  |
| mdp                              | 1.50 sec                                               | 993 ms: 1.51x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 317 ms: 1.51x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 343 ms: 1.48x faster                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 859 us: 1.39x faster                                                  |
| go                               | 117 ms                                                 | 84.2 ms: 1.39x faster                                                 |
| async_tree_none_tg               | 198 ms                                                 | 146 ms: 1.36x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 198 ms: 1.35x faster                                                  |
| generators                       | 31.9 ms                                                | 24.0 ms: 1.33x faster                                                 |
| async_tree_none                  | 212 ms                                                 | 164 ms: 1.29x faster                                                  |
| deepcopy_memo                    | 27.4 us                                                | 22.1 us: 1.24x faster                                                 |
| regex_effbot                     | 2.63 ms                                                | 2.22 ms: 1.18x faster                                                 |
| float                            | 55.8 ms                                                | 48.6 ms: 1.15x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 148 ms: 1.14x faster                                                  |
| pyflate                          | 352 ms                                                 | 316 ms: 1.11x faster                                                  |
| coroutines                       | 20.0 ms                                                | 18.0 ms: 1.11x faster                                                 |
| deepcopy                         | 236 us                                                 | 213 us: 1.11x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 413 ms: 1.08x faster                                                  |
| xml_etree_iterparse              | 74.2 ms                                                | 69.2 ms: 1.07x faster                                                 |
| html5lib                         | 36.7 ms                                                | 34.3 ms: 1.07x faster                                                 |
| scimark_sor                      | 106 ms                                                 | 99.3 ms: 1.06x faster                                                 |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 432 ms: 1.06x faster                                                  |
| regex_dna                        | 149 ms                                                 | 145 ms: 1.03x faster                                                  |
| asyncio_websockets               | 242 ms                                                 | 238 ms: 1.02x faster                                                  |
| tomli_loads                      | 1.57 sec                                               | 1.55 sec: 1.01x faster                                                |
| pidigits                         | 284 ms                                                 | 281 ms: 1.01x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 28.6 ms: 1.01x faster                                                 |
| regex_v8                         | 17.0 ms                                                | 17.1 ms: 1.00x slower                                                 |
| connected_components             | 319 ms                                                 | 320 ms: 1.00x slower                                                  |
| deltablue                        | 2.65 ms                                                | 2.70 ms: 1.02x slower                                                 |
| unpickle_pure_python             | 165 us                                                 | 169 us: 1.02x slower                                                  |
| dask                             | 771 ms                                                 | 787 ms: 1.02x slower                                                  |
| hexiom                           | 4.87 ms                                                | 4.99 ms: 1.03x slower                                                 |
| k_core                           | 1.61 sec                                               | 1.65 sec: 1.03x slower                                                |
| xml_etree_parse                  | 108 ms                                                 | 111 ms: 1.03x slower                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.62 us: 1.04x slower                                                 |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 391 ms: 1.05x slower                                                  |
| pylint                           | 180 ms                                                 | 189 ms: 1.05x slower                                                  |
| pathlib                          | 23.2 ms                                                | 24.5 ms: 1.05x slower                                                 |
| pycparser                        | 701 ms                                                 | 739 ms: 1.05x slower                                                  |
| regex_compile                    | 78.3 ms                                                | 83.7 ms: 1.07x slower                                                 |
| deepcopy_reduce                  | 2.09 us                                                | 2.27 us: 1.08x slower                                                 |
| genshi_text                      | 16.9 ms                                                | 18.4 ms: 1.09x slower                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 54.9 ms: 1.09x slower                                                 |
| python_startup                   | 18.8 ms                                                | 20.5 ms: 1.09x slower                                                 |
| docutils                         | 1.44 sec                                               | 1.59 sec: 1.10x slower                                                |
| async_generators                 | 294 ms                                                 | 324 ms: 1.10x slower                                                  |
| pickle_pure_python               | 215 us                                                 | 237 us: 1.10x slower                                                  |
| bpe_tokeniser                    | 3.26 sec                                               | 3.61 sec: 1.11x slower                                                |
| richards                         | 36.2 ms                                                | 40.4 ms: 1.12x slower                                                 |
| meteor_contest                   | 74.0 ms                                                | 82.8 ms: 1.12x slower                                                 |
| sphinx                           | 602 ms                                                 | 678 ms: 1.13x slower                                                  |
| 2to3                             | 179 ms                                                 | 202 ms: 1.13x slower                                                  |
| python_startup_no_site           | 13.7 ms                                                | 15.5 ms: 1.13x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 397 ms: 1.14x slower                                                  |
| sympy_integrate                  | 11.3 ms                                                | 13.0 ms: 1.15x slower                                                 |
| genshi_xml                       | 34.1 ms                                                | 39.3 ms: 1.15x slower                                                 |
| nqueens                          | 61.8 ms                                                | 71.7 ms: 1.16x slower                                                 |
| spectral_norm                    | 76.5 ms                                                | 89.6 ms: 1.17x slower                                                 |
| async_tree_eager                 | 69.9 ms                                                | 81.9 ms: 1.17x slower                                                 |
| chaos                            | 41.1 ms                                                | 48.2 ms: 1.17x slower                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 163 ms: 1.18x slower                                                  |
| richards_super                   | 39.2 ms                                                | 46.4 ms: 1.18x slower                                                 |
| bench_mp_pool                    | 64.7 ms                                                | 77.6 ms: 1.20x slower                                                 |
| xml_etree_process                | 41.3 ms                                                | 50.0 ms: 1.21x slower                                                 |
| logging_simple                   | 3.56 us                                                | 4.40 us: 1.24x slower                                                 |
| sympy_sum                        | 75.1 ms                                                | 93.1 ms: 1.24x slower                                                 |
| fannkuch                         | 279 ms                                                 | 348 ms: 1.25x slower                                                  |
| logging_format                   | 3.85 us                                                | 4.84 us: 1.26x slower                                                 |
| sympy_str                        | 146 ms                                                 | 184 ms: 1.26x slower                                                  |
| nbody                            | 73.6 ms                                                | 93.1 ms: 1.27x slower                                                 |
| pprint_safe_repr                 | 541 ms                                                 | 684 ms: 1.27x slower                                                  |
| pprint_pformat                   | 1.10 sec                                               | 1.39 sec: 1.27x slower                                                |
| telco                            | 4.84 ms                                                | 6.14 ms: 1.27x slower                                                 |
| xml_etree_generate               | 57.1 ms                                                | 72.5 ms: 1.27x slower                                                 |
| crypto_pyaes                     | 55.3 ms                                                | 70.3 ms: 1.27x slower                                                 |
| comprehensions                   | 12.0 us                                                | 15.3 us: 1.28x slower                                                 |
| json_dumps                       | 6.47 ms                                                | 8.33 ms: 1.29x slower                                                 |
| raytrace                         | 181 ms                                                 | 235 ms: 1.30x slower                                                  |
| sympy_expand                     | 248 ms                                                 | 325 ms: 1.31x slower                                                  |
| scimark_lu                       | 75.9 ms                                                | 99.9 ms: 1.32x slower                                                 |
| json                             | 3.04 ms                                                | 4.04 ms: 1.33x slower                                                 |
| many_optionals                   | 409 us                                                 | 546 us: 1.34x slower                                                  |
| thrift                           | 466 us                                                 | 635 us: 1.36x slower                                                  |
| django_template                  | 20.5 ms                                                | 28.4 ms: 1.39x slower                                                 |
| typing_runtime_protocols         | 101 us                                                 | 140 us: 1.39x slower                                                  |
| mako                             | 7.75 ms                                                | 10.8 ms: 1.40x slower                                                 |
| scimark_fft                      | 200 ms                                                 | 280 ms: 1.40x slower                                                  |
| json_loads                       | 17.0 us                                                | 24.5 us: 1.44x slower                                                 |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 4.50 ms: 1.51x slower                                                 |
| bench_thread_pool                | 503 us                                                 | 780 us: 1.55x slower                                                  |
| coverage                         | 46.2 ms                                                | 75.3 ms: 1.63x slower                                                 |
| subparsers                       | 9.44 ms                                                | 17.0 ms: 1.80x slower                                                 |
| async_tree_eager_tg              | 47.4 ms                                                | 127 ms: 2.68x slower                                                  |
| logging_silent                   | 71.0 ns                                                | 442 ns: 6.23x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.09x slower                                                          |

Benchmark hidden because not significant (1): shortest_path
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250617-3.15.0a0-fba5dde-NOGIL/bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.063x slower

# HPT report

- Reliability score: 99.63% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.26x