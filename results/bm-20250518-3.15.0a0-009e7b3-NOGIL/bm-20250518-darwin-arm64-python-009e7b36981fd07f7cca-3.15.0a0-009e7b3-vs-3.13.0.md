# Results vs. 3.13.0

- fork: python
- ref: 009e7b36981fd07f7cca
- machine: darwin-arm64
- commit hash: 009e7b3
- commit date: 2025-05-18
- overall geometric mean: 1.051x slower
- HPT reliability: 99.67%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 205 ms: 1.15x slower                                                  |
| docutils       | 1.44 sec                                               | 1.53 sec: 1.06x slower                                                |
| html5lib       | 36.7 ms                                                | 35.2 ms: 1.04x faster                                                 |
| sphinx         | 602 ms                                                 | 648 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg                 | 500 ms                                                 | 336 ms: 1.49x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 343 ms: 1.49x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 326 ms: 1.47x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 362 ms: 1.40x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 149 ms: 1.33x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 205 ms: 1.31x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 173 ms: 1.22x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 243 ms: 1.18x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 415 ms: 1.11x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 154 ms: 1.09x faster                                                  |
| coroutines                       | 20.0 ms                                                | 18.9 ms: 1.06x faster                                                 |
| asyncio_websockets               | 242 ms                                                 | 237 ms: 1.02x faster                                                  |
| async_generators                 | 294 ms                                                 | 291 ms: 1.01x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 453 ms: 1.01x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 378 ms: 1.09x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 169 ms: 1.22x slower                                                  |
| async_tree_eager                 | 69.9 ms                                                | 91.6 ms: 1.31x slower                                                 |
| async_tree_eager_tg              | 47.4 ms                                                | 129 ms: 2.73x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.06x faster                                                          |

Benchmark hidden because not significant (1): async_tree_eager_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 53.8 ms: 1.04x faster                                                 |
| pidigits       | 284 ms                                                 | 280 ms: 1.01x faster                                                  |
| nbody          | 73.6 ms                                                | 95.3 ms: 1.29x slower                                                 |
| Geometric mean | (ref)                                                  | 1.07x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.11 ms: 1.25x faster                                                 |
| regex_v8       | 17.0 ms                                                | 15.1 ms: 1.13x faster                                                 |
| regex_dna      | 149 ms                                                 | 136 ms: 1.09x faster                                                  |
| regex_compile  | 78.3 ms                                                | 95.8 ms: 1.22x slower                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_iterparse  | 74.2 ms                                                | 66.7 ms: 1.11x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 97.6 ms: 1.11x faster                                                 |
| tomli_loads          | 1.57 sec                                               | 1.64 sec: 1.05x slower                                                |
| xml_etree_generate   | 57.1 ms                                                | 63.4 ms: 1.11x slower                                                 |
| json_loads           | 17.0 us                                                | 19.1 us: 1.12x slower                                                 |
| json_dumps           | 6.47 ms                                                | 7.27 ms: 1.12x slower                                                 |
| unpickle_pure_python | 165 us                                                 | 190 us: 1.15x slower                                                  |
| xml_etree_process    | 41.3 ms                                                | 48.2 ms: 1.17x slower                                                 |
| pickle_pure_python   | 215 us                                                 | 272 us: 1.27x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.08x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 19.8 ms: 1.05x slower                                                 |
| python_startup_no_site | 13.7 ms                                                | 15.3 ms: 1.11x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 34.1 ms                                                | 38.8 ms: 1.14x slower                                                 |
| genshi_text     | 16.9 ms                                                | 19.4 ms: 1.15x slower                                                 |
| django_template | 20.5 ms                                                | 29.0 ms: 1.42x slower                                                 |
| mako            | 7.75 ms                                                | 11.6 ms: 1.50x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.29x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| gc_traversal                     | 2.94 ms                                                | 1.49 ms: 1.97x faster                                                 |
| mdp                              | 1.50 sec                                               | 905 ms: 1.66x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 336 ms: 1.49x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 343 ms: 1.49x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 326 ms: 1.47x faster                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 824 us: 1.45x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 362 ms: 1.40x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 149 ms: 1.33x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 205 ms: 1.31x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.11 ms: 1.25x faster                                                 |
| async_tree_none                  | 212 ms                                                 | 173 ms: 1.22x faster                                                  |
| deepcopy                         | 236 us                                                 | 200 us: 1.18x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 243 ms: 1.18x faster                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.37 us: 1.14x faster                                                 |
| regex_v8                         | 17.0 ms                                                | 15.1 ms: 1.13x faster                                                 |
| xml_etree_iterparse              | 74.2 ms                                                | 66.7 ms: 1.11x faster                                                 |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 415 ms: 1.11x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 97.6 ms: 1.11x faster                                                 |
| regex_dna                        | 149 ms                                                 | 136 ms: 1.09x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 154 ms: 1.09x faster                                                  |
| deepcopy_memo                    | 27.4 us                                                | 25.6 us: 1.07x faster                                                 |
| coroutines                       | 20.0 ms                                                | 18.9 ms: 1.06x faster                                                 |
| go                               | 117 ms                                                 | 111 ms: 1.05x faster                                                  |
| html5lib                         | 36.7 ms                                                | 35.2 ms: 1.04x faster                                                 |
| scimark_sor                      | 106 ms                                                 | 102 ms: 1.04x faster                                                  |
| float                            | 55.8 ms                                                | 53.8 ms: 1.04x faster                                                 |
| dulwich_log                      | 28.7 ms                                                | 28.0 ms: 1.03x faster                                                 |
| asyncio_websockets               | 242 ms                                                 | 237 ms: 1.02x faster                                                  |
| pidigits                         | 284 ms                                                 | 280 ms: 1.01x faster                                                  |
| async_generators                 | 294 ms                                                 | 291 ms: 1.01x faster                                                  |
| bpe_tokeniser                    | 3.26 sec                                               | 3.27 sec: 1.00x slower                                                |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 453 ms: 1.01x slower                                                  |
| deepcopy_reduce                  | 2.09 us                                                | 2.15 us: 1.03x slower                                                 |
| pyflate                          | 352 ms                                                 | 364 ms: 1.03x slower                                                  |
| shortest_path                    | 345 ms                                                 | 359 ms: 1.04x slower                                                  |
| connected_components             | 319 ms                                                 | 333 ms: 1.04x slower                                                  |
| json                             | 3.04 ms                                                | 3.18 ms: 1.04x slower                                                 |
| tomli_loads                      | 1.57 sec                                               | 1.64 sec: 1.05x slower                                                |
| pycparser                        | 701 ms                                                 | 734 ms: 1.05x slower                                                  |
| python_startup                   | 18.8 ms                                                | 19.8 ms: 1.05x slower                                                 |
| docutils                         | 1.44 sec                                               | 1.53 sec: 1.06x slower                                                |
| spectral_norm                    | 76.5 ms                                                | 81.0 ms: 1.06x slower                                                 |
| sphinx                           | 602 ms                                                 | 648 ms: 1.08x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 378 ms: 1.09x slower                                                  |
| sympy_integrate                  | 11.3 ms                                                | 12.3 ms: 1.09x slower                                                 |
| pathlib                          | 23.2 ms                                                | 25.4 ms: 1.09x slower                                                 |
| telco                            | 4.84 ms                                                | 5.33 ms: 1.10x slower                                                 |
| xml_etree_generate               | 57.1 ms                                                | 63.4 ms: 1.11x slower                                                 |
| python_startup_no_site           | 13.7 ms                                                | 15.3 ms: 1.11x slower                                                 |
| json_loads                       | 17.0 us                                                | 19.1 us: 1.12x slower                                                 |
| json_dumps                       | 6.47 ms                                                | 7.27 ms: 1.12x slower                                                 |
| thrift                           | 466 us                                                 | 524 us: 1.12x slower                                                  |
| meteor_contest                   | 74.0 ms                                                | 83.4 ms: 1.13x slower                                                 |
| fannkuch                         | 279 ms                                                 | 315 ms: 1.13x slower                                                  |
| deltablue                        | 2.65 ms                                                | 3.01 ms: 1.14x slower                                                 |
| genshi_xml                       | 34.1 ms                                                | 38.8 ms: 1.14x slower                                                 |
| bench_mp_pool                    | 64.7 ms                                                | 73.8 ms: 1.14x slower                                                 |
| genshi_text                      | 16.9 ms                                                | 19.4 ms: 1.15x slower                                                 |
| richards                         | 36.2 ms                                                | 41.5 ms: 1.15x slower                                                 |
| scimark_fft                      | 200 ms                                                 | 229 ms: 1.15x slower                                                  |
| pprint_safe_repr                 | 541 ms                                                 | 621 ms: 1.15x slower                                                  |
| pprint_pformat                   | 1.10 sec                                               | 1.26 sec: 1.15x slower                                                |
| unpickle_pure_python             | 165 us                                                 | 190 us: 1.15x slower                                                  |
| 2to3                             | 179 ms                                                 | 205 ms: 1.15x slower                                                  |
| xml_etree_process                | 41.3 ms                                                | 48.2 ms: 1.17x slower                                                 |
| hexiom                           | 4.87 ms                                                | 5.72 ms: 1.18x slower                                                 |
| sympy_sum                        | 75.1 ms                                                | 88.3 ms: 1.18x slower                                                 |
| sympy_str                        | 146 ms                                                 | 172 ms: 1.18x slower                                                  |
| nqueens                          | 61.8 ms                                                | 73.6 ms: 1.19x slower                                                 |
| crypto_pyaes                     | 55.3 ms                                                | 66.1 ms: 1.19x slower                                                 |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.57 ms: 1.20x slower                                                 |
| sympy_expand                     | 248 ms                                                 | 297 ms: 1.20x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 169 ms: 1.22x slower                                                  |
| regex_compile                    | 78.3 ms                                                | 95.8 ms: 1.22x slower                                                 |
| richards_super                   | 39.2 ms                                                | 48.2 ms: 1.23x slower                                                 |
| typing_runtime_protocols         | 101 us                                                 | 124 us: 1.23x slower                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 62.5 ms: 1.24x slower                                                 |
| comprehensions                   | 12.0 us                                                | 14.9 us: 1.25x slower                                                 |
| chaos                            | 41.1 ms                                                | 51.3 ms: 1.25x slower                                                 |
| raytrace                         | 181 ms                                                 | 228 ms: 1.26x slower                                                  |
| many_optionals                   | 409 us                                                 | 518 us: 1.27x slower                                                  |
| pickle_pure_python               | 215 us                                                 | 272 us: 1.27x slower                                                  |
| scimark_lu                       | 75.9 ms                                                | 98.2 ms: 1.29x slower                                                 |
| nbody                            | 73.6 ms                                                | 95.3 ms: 1.29x slower                                                 |
| async_tree_eager                 | 69.9 ms                                                | 91.6 ms: 1.31x slower                                                 |
| logging_format                   | 3.85 us                                                | 5.11 us: 1.33x slower                                                 |
| logging_simple                   | 3.56 us                                                | 4.72 us: 1.33x slower                                                 |
| django_template                  | 20.5 ms                                                | 29.0 ms: 1.42x slower                                                 |
| coverage                         | 46.2 ms                                                | 66.6 ms: 1.44x slower                                                 |
| mako                             | 7.75 ms                                                | 11.6 ms: 1.50x slower                                                 |
| bench_thread_pool                | 503 us                                                 | 762 us: 1.51x slower                                                  |
| subparsers                       | 9.44 ms                                                | 15.7 ms: 1.67x slower                                                 |
| async_tree_eager_tg              | 47.4 ms                                                | 129 ms: 2.73x slower                                                  |
| logging_silent                   | 71.0 ns                                                | 373 ns: 5.26x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.08x slower                                                          |

Benchmark hidden because not significant (4): pylint, generators, async_tree_eager_cpu_io_mixed, k_core
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250518-3.15.0a0-009e7b3-NOGIL/bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.051x slower

# HPT report

- Reliability score: 99.67% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.27x