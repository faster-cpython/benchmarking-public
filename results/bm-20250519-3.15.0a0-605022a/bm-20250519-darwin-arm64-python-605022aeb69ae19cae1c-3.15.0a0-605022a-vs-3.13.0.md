# Results vs. 3.13.0

- fork: python
- ref: 605022aeb69ae19cae1c
- machine: darwin-arm64
- commit hash: 605022a
- commit date: 2025-05-19
- overall geometric mean: 1.105x slower
- HPT reliability: 98.61%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-darwin-arm64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 193 ms: 1.08x slower                                                  |
| docutils       | 1.44 sec                                               | 1.57 sec: 1.08x slower                                                |
| html5lib       | 36.7 ms                                                | 35.2 ms: 1.04x faster                                                 |
| sphinx         | 602 ms                                                 | 637 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-darwin-arm64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 215 ms: 1.34x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 407 ms: 1.26x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 222 ms: 1.21x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 417 ms: 1.20x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 425 ms: 1.20x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 413 ms: 1.16x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 186 ms: 1.14x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 176 ms: 1.13x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 155 ms: 1.08x faster                                                  |
| async_generators                 | 294 ms                                                 | 274 ms: 1.07x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 426 ms: 1.05x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 440 ms: 1.04x faster                                                  |
| coroutines                       | 20.0 ms                                                | 19.7 ms: 1.02x faster                                                 |
| async_tree_eager                 | 69.9 ms                                                | 77.6 ms: 1.11x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 401 ms: 1.16x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 188 ms: 1.36x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 145 ms: 3.06x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (2): async_tree_eager_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-darwin-arm64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                                  |
| float          | 55.8 ms                                                | 58.9 ms: 1.06x slower                                                 |
| nbody          | 73.6 ms                                                | 91.7 ms: 1.25x slower                                                 |
| Geometric mean | (ref)                                                  | 1.10x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-darwin-arm64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.16 ms: 1.21x faster                                                 |
| regex_dna      | 149 ms                                                 | 137 ms: 1.08x faster                                                  |
| regex_v8       | 17.0 ms                                                | 15.8 ms: 1.08x faster                                                 |
| regex_compile  | 78.3 ms                                                | 86.7 ms: 1.11x slower                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-darwin-arm64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 105 ms: 1.03x faster                                                  |
| tomli_loads          | 1.57 sec                                               | 1.52 sec: 1.03x faster                                                |
| xml_etree_iterparse  | 74.2 ms                                                | 77.0 ms: 1.04x slower                                                 |
| json_loads           | 17.0 us                                                | 18.3 us: 1.07x slower                                                 |
| xml_etree_generate   | 57.1 ms                                                | 61.4 ms: 1.07x slower                                                 |
| json_dumps           | 6.47 ms                                                | 7.16 ms: 1.11x slower                                                 |
| xml_etree_process    | 41.3 ms                                                | 45.8 ms: 1.11x slower                                                 |
| unpickle_pure_python | 165 us                                                 | 189 us: 1.15x slower                                                  |
| pickle_pure_python   | 215 us                                                 | 250 us: 1.17x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.07x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-darwin-arm64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 18.9 ms: 1.00x slower                                                 |
| python_startup_no_site | 13.7 ms                                                | 14.4 ms: 1.05x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-darwin-arm64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 18.6 ms: 1.10x slower                                                 |
| genshi_xml      | 34.1 ms                                                | 37.6 ms: 1.10x slower                                                 |
| mako            | 7.75 ms                                                | 9.10 ms: 1.17x slower                                                 |
| django_template | 20.5 ms                                                | 26.6 ms: 1.30x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.17x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250519-darwin-arm64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 867 ms: 1.73x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 215 ms: 1.34x faster                                                  |
| deepcopy                         | 236 us                                                 | 187 us: 1.26x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 407 ms: 1.26x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.16 ms: 1.21x faster                                                 |
| async_tree_memoization           | 268 ms                                                 | 222 ms: 1.21x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 417 ms: 1.20x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 425 ms: 1.20x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 413 ms: 1.16x faster                                                  |
| deepcopy_memo                    | 27.4 us                                                | 23.8 us: 1.15x faster                                                 |
| async_tree_none                  | 212 ms                                                 | 186 ms: 1.14x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 176 ms: 1.13x faster                                                  |
| scimark_sor                      | 106 ms                                                 | 94.8 ms: 1.11x faster                                                 |
| go                               | 117 ms                                                 | 105 ms: 1.11x faster                                                  |
| regex_dna                        | 149 ms                                                 | 137 ms: 1.08x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 155 ms: 1.08x faster                                                  |
| regex_v8                         | 17.0 ms                                                | 15.8 ms: 1.08x faster                                                 |
| async_generators                 | 294 ms                                                 | 274 ms: 1.07x faster                                                  |
| deepcopy_reduce                  | 2.09 us                                                | 1.99 us: 1.05x faster                                                 |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 426 ms: 1.05x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 27.4 ms: 1.05x faster                                                 |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 440 ms: 1.04x faster                                                  |
| html5lib                         | 36.7 ms                                                | 35.2 ms: 1.04x faster                                                 |
| xml_etree_parse                  | 108 ms                                                 | 105 ms: 1.03x faster                                                  |
| tomli_loads                      | 1.57 sec                                               | 1.52 sec: 1.03x faster                                                |
| k_core                           | 1.61 sec                                               | 1.57 sec: 1.03x faster                                                |
| connected_components             | 319 ms                                                 | 313 ms: 1.02x faster                                                  |
| coroutines                       | 20.0 ms                                                | 19.7 ms: 1.02x faster                                                 |
| generators                       | 31.9 ms                                                | 31.5 ms: 1.02x faster                                                 |
| shortest_path                    | 345 ms                                                 | 341 ms: 1.01x faster                                                  |
| pyflate                          | 352 ms                                                 | 350 ms: 1.01x faster                                                  |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                                  |
| python_startup                   | 18.8 ms                                                | 18.9 ms: 1.00x slower                                                 |
| bpe_tokeniser                    | 3.26 sec                                               | 3.31 sec: 1.02x slower                                                |
| json                             | 3.04 ms                                                | 3.11 ms: 1.02x slower                                                 |
| sqlite_synth                     | 1.55 us                                                | 1.59 us: 1.03x slower                                                 |
| spectral_norm                    | 76.5 ms                                                | 78.5 ms: 1.03x slower                                                 |
| sympy_integrate                  | 11.3 ms                                                | 11.6 ms: 1.03x slower                                                 |
| xml_etree_iterparse              | 74.2 ms                                                | 77.0 ms: 1.04x slower                                                 |
| pathlib                          | 23.2 ms                                                | 24.2 ms: 1.04x slower                                                 |
| python_startup_no_site           | 13.7 ms                                                | 14.4 ms: 1.05x slower                                                 |
| scimark_fft                      | 200 ms                                                 | 209 ms: 1.05x slower                                                  |
| meteor_contest                   | 74.0 ms                                                | 77.8 ms: 1.05x slower                                                 |
| float                            | 55.8 ms                                                | 58.9 ms: 1.06x slower                                                 |
| sphinx                           | 602 ms                                                 | 637 ms: 1.06x slower                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 53.8 ms: 1.07x slower                                                 |
| json_loads                       | 17.0 us                                                | 18.3 us: 1.07x slower                                                 |
| xml_etree_generate               | 57.1 ms                                                | 61.4 ms: 1.07x slower                                                 |
| 2to3                             | 179 ms                                                 | 193 ms: 1.08x slower                                                  |
| fannkuch                         | 279 ms                                                 | 301 ms: 1.08x slower                                                  |
| bench_thread_pool                | 503 us                                                 | 544 us: 1.08x slower                                                  |
| deltablue                        | 2.65 ms                                                | 2.86 ms: 1.08x slower                                                 |
| pprint_pformat                   | 1.10 sec                                               | 1.19 sec: 1.08x slower                                                |
| docutils                         | 1.44 sec                                               | 1.57 sec: 1.08x slower                                                |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.24 ms: 1.09x slower                                                 |
| pprint_safe_repr                 | 541 ms                                                 | 588 ms: 1.09x slower                                                  |
| richards                         | 36.2 ms                                                | 39.4 ms: 1.09x slower                                                 |
| pycparser                        | 701 ms                                                 | 766 ms: 1.09x slower                                                  |
| sympy_expand                     | 248 ms                                                 | 271 ms: 1.09x slower                                                  |
| sympy_str                        | 146 ms                                                 | 160 ms: 1.10x slower                                                  |
| gc_traversal                     | 2.94 ms                                                | 3.22 ms: 1.10x slower                                                 |
| genshi_text                      | 16.9 ms                                                | 18.6 ms: 1.10x slower                                                 |
| sympy_sum                        | 75.1 ms                                                | 82.8 ms: 1.10x slower                                                 |
| bench_mp_pool                    | 64.7 ms                                                | 71.4 ms: 1.10x slower                                                 |
| genshi_xml                       | 34.1 ms                                                | 37.6 ms: 1.10x slower                                                 |
| json_dumps                       | 6.47 ms                                                | 7.16 ms: 1.11x slower                                                 |
| regex_compile                    | 78.3 ms                                                | 86.7 ms: 1.11x slower                                                 |
| xml_etree_process                | 41.3 ms                                                | 45.8 ms: 1.11x slower                                                 |
| async_tree_eager                 | 69.9 ms                                                | 77.6 ms: 1.11x slower                                                 |
| crypto_pyaes                     | 55.3 ms                                                | 61.4 ms: 1.11x slower                                                 |
| dask                             | 771 ms                                                 | 860 ms: 1.12x slower                                                  |
| typing_runtime_protocols         | 101 us                                                 | 112 us: 1.12x slower                                                  |
| richards_super                   | 39.2 ms                                                | 44.0 ms: 1.12x slower                                                 |
| hexiom                           | 4.87 ms                                                | 5.47 ms: 1.12x slower                                                 |
| scimark_lu                       | 75.9 ms                                                | 86.3 ms: 1.14x slower                                                 |
| chaos                            | 41.1 ms                                                | 46.9 ms: 1.14x slower                                                 |
| raytrace                         | 181 ms                                                 | 207 ms: 1.14x slower                                                  |
| unpickle_pure_python             | 165 us                                                 | 189 us: 1.15x slower                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 1.37 ms: 1.15x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 401 ms: 1.16x slower                                                  |
| pickle_pure_python               | 215 us                                                 | 250 us: 1.17x slower                                                  |
| mako                             | 7.75 ms                                                | 9.10 ms: 1.17x slower                                                 |
| logging_format                   | 3.85 us                                                | 4.54 us: 1.18x slower                                                 |
| logging_simple                   | 3.56 us                                                | 4.22 us: 1.19x slower                                                 |
| comprehensions                   | 12.0 us                                                | 14.6 us: 1.22x slower                                                 |
| nqueens                          | 61.8 ms                                                | 75.7 ms: 1.23x slower                                                 |
| nbody                            | 73.6 ms                                                | 91.7 ms: 1.25x slower                                                 |
| many_optionals                   | 409 us                                                 | 512 us: 1.25x slower                                                  |
| django_template                  | 20.5 ms                                                | 26.6 ms: 1.30x slower                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 188 ms: 1.36x slower                                                  |
| subparsers                       | 9.44 ms                                                | 15.2 ms: 1.61x slower                                                 |
| async_tree_eager_tg              | 47.4 ms                                                | 145 ms: 3.06x slower                                                  |
| logging_silent                   | 71.0 ns                                                | 344 ns: 4.85x slower                                                  |
| coverage                         | 46.2 ms                                                | 332 ms: 7.18x slower                                                  |
| thrift                           | 466 us                                                 | 43.9 ms: 94.25x slower                                                |
| Geometric mean                   | (ref)                                                  | 1.13x slower                                                          |

Benchmark hidden because not significant (4): pylint, telco, async_tree_eager_cpu_io_mixed, asyncio_websockets
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250519-3.15.0a0-605022a/bm-20250519-darwin-arm64-python-605022aeb69ae19cae1c-3.15.0a0-605022a.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.105x slower

# HPT report

- Reliability score: 98.61% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.11x