# Results vs. 3.13.0

- fork: python
- ref: 009e7b36981fd07f7cca
- machine: darwin-arm64
- commit hash: 009e7b3
- commit date: 2025-05-18
- overall geometric mean: 1.061x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 158 ms: 1.13x faster                                                  |
| docutils       | 1.44 sec                                               | 1.40 sec: 1.03x faster                                                |
| html5lib       | 36.7 ms                                                | 29.4 ms: 1.25x faster                                                 |
| sphinx         | 602 ms                                                 | 559 ms: 1.08x faster                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 182 ms: 1.58x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 335 ms: 1.52x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 340 ms: 1.49x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 180 ms: 1.49x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 342 ms: 1.46x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 152 ms: 1.40x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 347 ms: 1.38x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 145 ms: 1.37x faster                                                  |
| coroutines                       | 20.0 ms                                                | 15.3 ms: 1.31x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 133 ms: 1.26x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 57.3 ms: 1.22x faster                                                 |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 408 ms: 1.13x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 402 ms: 1.11x faster                                                  |
| async_generators                 | 294 ms                                                 | 266 ms: 1.11x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 350 ms: 1.06x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 381 ms: 1.10x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 159 ms: 1.16x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 120 ms: 2.53x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.17x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 43.9 ms: 1.27x faster                                                 |
| pidigits       | 284 ms                                                 | 280 ms: 1.01x faster                                                  |
| nbody          | 73.6 ms                                                | 73.8 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 78.3 ms                                                | 61.6 ms: 1.27x faster                                                 |
| regex_effbot   | 2.63 ms                                                | 2.20 ms: 1.19x faster                                                 |
| regex_v8       | 17.0 ms                                                | 15.5 ms: 1.10x faster                                                 |
| regex_dna      | 149 ms                                                 | 141 ms: 1.06x faster                                                  |
| Geometric mean | (ref)                                                  | 1.15x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.20 sec: 1.30x faster                                                |
| unpickle_pure_python | 165 us                                                 | 129 us: 1.28x faster                                                  |
| pickle_pure_python   | 215 us                                                 | 188 us: 1.14x faster                                                  |
| xml_etree_process    | 41.3 ms                                                | 39.4 ms: 1.05x faster                                                 |
| xml_etree_generate   | 57.1 ms                                                | 55.6 ms: 1.03x faster                                                 |
| xml_etree_iterparse  | 74.2 ms                                                | 72.9 ms: 1.02x faster                                                 |
| json_dumps           | 6.47 ms                                                | 6.36 ms: 1.02x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 107 ms: 1.01x faster                                                  |
| json_loads           | 17.0 us                                                | 18.4 us: 1.08x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 18.3 ms: 1.03x faster                                                 |
| python_startup_no_site | 13.7 ms                                                | 13.9 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 12.8 ms: 1.32x faster                                                 |
| genshi_xml      | 34.1 ms                                                | 27.1 ms: 1.26x faster                                                 |
| mako            | 7.75 ms                                                | 7.22 ms: 1.07x faster                                                 |
| django_template | 20.5 ms                                                | 19.7 ms: 1.04x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.17x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 709 ms: 2.11x faster                                                  |
| generators                       | 31.9 ms                                                | 18.9 ms: 1.69x faster                                                 |
| deepcopy_memo                    | 27.4 us                                                | 16.4 us: 1.67x faster                                                 |
| go                               | 117 ms                                                 | 71.2 ms: 1.64x faster                                                 |
| deepcopy                         | 236 us                                                 | 145 us: 1.63x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 182 ms: 1.58x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 335 ms: 1.52x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 340 ms: 1.49x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 180 ms: 1.49x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 342 ms: 1.46x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 152 ms: 1.40x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 347 ms: 1.38x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 145 ms: 1.37x faster                                                  |
| scimark_sor                      | 106 ms                                                 | 77.9 ms: 1.36x faster                                                 |
| genshi_text                      | 16.9 ms                                                | 12.8 ms: 1.32x faster                                                 |
| deepcopy_reduce                  | 2.09 us                                                | 1.59 us: 1.32x faster                                                 |
| coroutines                       | 20.0 ms                                                | 15.3 ms: 1.31x faster                                                 |
| tomli_loads                      | 1.57 sec                                               | 1.20 sec: 1.30x faster                                                |
| deltablue                        | 2.65 ms                                                | 2.04 ms: 1.29x faster                                                 |
| hexiom                           | 4.87 ms                                                | 3.79 ms: 1.28x faster                                                 |
| unpickle_pure_python             | 165 us                                                 | 129 us: 1.28x faster                                                  |
| regex_compile                    | 78.3 ms                                                | 61.6 ms: 1.27x faster                                                 |
| float                            | 55.8 ms                                                | 43.9 ms: 1.27x faster                                                 |
| pyflate                          | 352 ms                                                 | 277 ms: 1.27x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 133 ms: 1.26x faster                                                  |
| genshi_xml                       | 34.1 ms                                                | 27.1 ms: 1.26x faster                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 40.4 ms: 1.25x faster                                                 |
| html5lib                         | 36.7 ms                                                | 29.4 ms: 1.25x faster                                                 |
| richards                         | 36.2 ms                                                | 29.5 ms: 1.23x faster                                                 |
| async_tree_eager                 | 69.9 ms                                                | 57.3 ms: 1.22x faster                                                 |
| pprint_pformat                   | 1.10 sec                                               | 907 ms: 1.21x faster                                                  |
| pprint_safe_repr                 | 541 ms                                                 | 447 ms: 1.21x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 23.8 ms: 1.21x faster                                                 |
| regex_effbot                     | 2.63 ms                                                | 2.20 ms: 1.19x faster                                                 |
| richards_super                   | 39.2 ms                                                | 33.2 ms: 1.18x faster                                                 |
| pylint                           | 180 ms                                                 | 153 ms: 1.18x faster                                                  |
| chaos                            | 41.1 ms                                                | 35.6 ms: 1.15x faster                                                 |
| nqueens                          | 61.8 ms                                                | 54.0 ms: 1.15x faster                                                 |
| pickle_pure_python               | 215 us                                                 | 188 us: 1.14x faster                                                  |
| comprehensions                   | 12.0 us                                                | 10.6 us: 1.13x faster                                                 |
| 2to3                             | 179 ms                                                 | 158 ms: 1.13x faster                                                  |
| raytrace                         | 181 ms                                                 | 161 ms: 1.13x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 408 ms: 1.13x faster                                                  |
| bpe_tokeniser                    | 3.26 sec                                               | 2.89 sec: 1.13x faster                                                |
| sympy_expand                     | 248 ms                                                 | 222 ms: 1.12x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 402 ms: 1.11x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 68.6 ms: 1.11x faster                                                 |
| pycparser                        | 701 ms                                                 | 629 ms: 1.11x faster                                                  |
| sympy_integrate                  | 11.3 ms                                                | 10.2 ms: 1.11x faster                                                 |
| crypto_pyaes                     | 55.3 ms                                                | 49.9 ms: 1.11x faster                                                 |
| sympy_str                        | 146 ms                                                 | 131 ms: 1.11x faster                                                  |
| async_generators                 | 294 ms                                                 | 266 ms: 1.11x faster                                                  |
| regex_v8                         | 17.0 ms                                                | 15.5 ms: 1.10x faster                                                 |
| typing_runtime_protocols         | 101 us                                                 | 91.7 us: 1.10x faster                                                 |
| fannkuch                         | 279 ms                                                 | 254 ms: 1.10x faster                                                  |
| scimark_lu                       | 75.9 ms                                                | 69.7 ms: 1.09x faster                                                 |
| logging_simple                   | 3.56 us                                                | 3.27 us: 1.09x faster                                                 |
| sympy_sum                        | 75.1 ms                                                | 69.7 ms: 1.08x faster                                                 |
| sphinx                           | 602 ms                                                 | 559 ms: 1.08x faster                                                  |
| logging_format                   | 3.85 us                                                | 3.58 us: 1.08x faster                                                 |
| mako                             | 7.75 ms                                                | 7.22 ms: 1.07x faster                                                 |
| bench_thread_pool                | 503 us                                                 | 471 us: 1.07x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 350 ms: 1.06x faster                                                  |
| telco                            | 4.84 ms                                                | 4.56 ms: 1.06x faster                                                 |
| regex_dna                        | 149 ms                                                 | 141 ms: 1.06x faster                                                  |
| k_core                           | 1.61 sec                                               | 1.53 sec: 1.06x faster                                                |
| connected_components             | 319 ms                                                 | 302 ms: 1.06x faster                                                  |
| shortest_path                    | 345 ms                                                 | 327 ms: 1.06x faster                                                  |
| xml_etree_process                | 41.3 ms                                                | 39.4 ms: 1.05x faster                                                 |
| django_template                  | 20.5 ms                                                | 19.7 ms: 1.04x faster                                                 |
| meteor_contest                   | 74.0 ms                                                | 71.0 ms: 1.04x faster                                                 |
| docutils                         | 1.44 sec                                               | 1.40 sec: 1.03x faster                                                |
| python_startup                   | 18.8 ms                                                | 18.3 ms: 1.03x faster                                                 |
| xml_etree_generate               | 57.1 ms                                                | 55.6 ms: 1.03x faster                                                 |
| xml_etree_iterparse              | 74.2 ms                                                | 72.9 ms: 1.02x faster                                                 |
| json_dumps                       | 6.47 ms                                                | 6.36 ms: 1.02x faster                                                 |
| pidigits                         | 284 ms                                                 | 280 ms: 1.01x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 107 ms: 1.01x faster                                                  |
| nbody                            | 73.6 ms                                                | 73.8 ms: 1.00x slower                                                 |
| sqlite_synth                     | 1.55 us                                                | 1.57 us: 1.01x slower                                                 |
| python_startup_no_site           | 13.7 ms                                                | 13.9 ms: 1.01x slower                                                 |
| dask                             | 771 ms                                                 | 799 ms: 1.04x slower                                                  |
| scimark_fft                      | 200 ms                                                 | 207 ms: 1.04x slower                                                  |
| pathlib                          | 23.2 ms                                                | 24.1 ms: 1.04x slower                                                 |
| many_optionals                   | 409 us                                                 | 439 us: 1.07x slower                                                  |
| bench_mp_pool                    | 64.7 ms                                                | 69.6 ms: 1.08x slower                                                 |
| json_loads                       | 17.0 us                                                | 18.4 us: 1.08x slower                                                 |
| gc_traversal                     | 2.94 ms                                                | 3.18 ms: 1.08x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 381 ms: 1.10x slower                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 1.34 ms: 1.12x slower                                                 |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.37 ms: 1.13x slower                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 159 ms: 1.16x slower                                                  |
| subparsers                       | 9.44 ms                                                | 12.9 ms: 1.36x slower                                                 |
| async_tree_eager_tg              | 47.4 ms                                                | 120 ms: 2.53x slower                                                  |
| logging_silent                   | 71.0 ns                                                | 302 ns: 4.26x slower                                                  |
| coverage                         | 46.2 ms                                                | 258 ms: 5.59x slower                                                  |
| thrift                           | 466 us                                                 | 43.1 ms: 92.56x slower                                                |
| Geometric mean                   | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (2): asyncio_websockets, json
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250518-3.15.0a0-009e7b3-CLANG/bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.061x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.11x