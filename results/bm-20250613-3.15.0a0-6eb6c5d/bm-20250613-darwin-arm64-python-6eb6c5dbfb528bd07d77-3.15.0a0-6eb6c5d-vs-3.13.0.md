# Results vs. 3.13.0

- fork: python
- ref: 6eb6c5dbfb528bd07d77
- machine: darwin-arm64
- commit hash: 6eb6c5d
- commit date: 2025-06-13
- overall geometric mean: 1.079x slower
- HPT reliability: 82.81%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-darwin-arm64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 186 ms: 1.04x slower                                                  |
| docutils       | 1.44 sec                                               | 1.51 sec: 1.05x slower                                                |
| html5lib       | 36.7 ms                                                | 34.2 ms: 1.07x faster                                                 |
| sphinx         | 602 ms                                                 | 614 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-darwin-arm64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 207 ms: 1.39x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 393 ms: 1.30x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 215 ms: 1.25x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 405 ms: 1.24x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 413 ms: 1.23x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 403 ms: 1.19x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 170 ms: 1.16x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 183 ms: 1.16x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 151 ms: 1.11x faster                                                  |
| async_generators                 | 294 ms                                                 | 273 ms: 1.07x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 433 ms: 1.06x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 422 ms: 1.06x faster                                                  |
| coroutines                       | 20.0 ms                                                | 19.3 ms: 1.04x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 368 ms: 1.01x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 73.0 ms: 1.04x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 400 ms: 1.15x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 183 ms: 1.33x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 143 ms: 3.03x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-darwin-arm64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 57.7 ms: 1.03x slower                                                 |
| nbody          | 73.6 ms                                                | 84.7 ms: 1.15x slower                                                 |
| Geometric mean | (ref)                                                  | 1.06x slower                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-darwin-arm64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.34 ms: 1.12x faster                                                 |
| regex_v8       | 17.0 ms                                                | 16.1 ms: 1.05x faster                                                 |
| regex_dna      | 149 ms                                                 | 143 ms: 1.04x faster                                                  |
| regex_compile  | 78.3 ms                                                | 81.4 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-darwin-arm64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.45 sec: 1.08x faster                                                |
| xml_etree_parse      | 108 ms                                                 | 104 ms: 1.04x faster                                                  |
| json_loads           | 17.0 us                                                | 16.6 us: 1.03x faster                                                 |
| xml_etree_generate   | 57.1 ms                                                | 58.1 ms: 1.02x slower                                                 |
| xml_etree_process    | 41.3 ms                                                | 43.0 ms: 1.04x slower                                                 |
| json_dumps           | 6.47 ms                                                | 6.83 ms: 1.06x slower                                                 |
| unpickle_pure_python | 165 us                                                 | 177 us: 1.07x slower                                                  |
| pickle_pure_python   | 215 us                                                 | 241 us: 1.12x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                          |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-darwin-arm64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 17.5 ms: 1.07x faster                                                 |
| python_startup_no_site | 13.7 ms                                                | 13.1 ms: 1.05x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-darwin-arm64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 17.6 ms: 1.04x slower                                                 |
| genshi_xml      | 34.1 ms                                                | 36.5 ms: 1.07x slower                                                 |
| mako            | 7.75 ms                                                | 9.19 ms: 1.19x slower                                                 |
| django_template | 20.5 ms                                                | 25.1 ms: 1.23x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.13x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-darwin-arm64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 829 ms: 1.81x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 207 ms: 1.39x faster                                                  |
| deepcopy                         | 236 us                                                 | 175 us: 1.35x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 393 ms: 1.30x faster                                                  |
| deepcopy_memo                    | 27.4 us                                                | 21.8 us: 1.25x faster                                                 |
| async_tree_memoization           | 268 ms                                                 | 215 ms: 1.25x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 405 ms: 1.24x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 413 ms: 1.23x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 403 ms: 1.19x faster                                                  |
| scimark_sor                      | 106 ms                                                 | 90.9 ms: 1.16x faster                                                 |
| async_tree_none_tg               | 198 ms                                                 | 170 ms: 1.16x faster                                                  |
| go                               | 117 ms                                                 | 100 ms: 1.16x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 183 ms: 1.16x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.34 ms: 1.12x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 151 ms: 1.11x faster                                                  |
| k_core                           | 1.61 sec                                               | 1.46 sec: 1.10x faster                                                |
| deepcopy_reduce                  | 2.09 us                                                | 1.90 us: 1.10x faster                                                 |
| tomli_loads                      | 1.57 sec                                               | 1.45 sec: 1.08x faster                                                |
| python_startup                   | 18.8 ms                                                | 17.5 ms: 1.07x faster                                                 |
| async_generators                 | 294 ms                                                 | 273 ms: 1.07x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 26.8 ms: 1.07x faster                                                 |
| html5lib                         | 36.7 ms                                                | 34.2 ms: 1.07x faster                                                 |
| pylint                           | 180 ms                                                 | 168 ms: 1.07x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 433 ms: 1.06x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 422 ms: 1.06x faster                                                  |
| shortest_path                    | 345 ms                                                 | 328 ms: 1.05x faster                                                  |
| regex_v8                         | 17.0 ms                                                | 16.1 ms: 1.05x faster                                                 |
| python_startup_no_site           | 13.7 ms                                                | 13.1 ms: 1.05x faster                                                 |
| pyflate                          | 352 ms                                                 | 336 ms: 1.05x faster                                                  |
| regex_dna                        | 149 ms                                                 | 143 ms: 1.04x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 104 ms: 1.04x faster                                                  |
| coroutines                       | 20.0 ms                                                | 19.3 ms: 1.04x faster                                                 |
| connected_components             | 319 ms                                                 | 308 ms: 1.04x faster                                                  |
| json                             | 3.04 ms                                                | 2.94 ms: 1.04x faster                                                 |
| json_loads                       | 17.0 us                                                | 16.6 us: 1.03x faster                                                 |
| spectral_norm                    | 76.5 ms                                                | 74.9 ms: 1.02x faster                                                 |
| generators                       | 31.9 ms                                                | 31.5 ms: 1.01x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 368 ms: 1.01x faster                                                  |
| telco                            | 4.84 ms                                                | 4.80 ms: 1.01x faster                                                 |
| sympy_integrate                  | 11.3 ms                                                | 11.4 ms: 1.00x slower                                                 |
| bpe_tokeniser                    | 3.26 sec                                               | 3.28 sec: 1.01x slower                                                |
| meteor_contest                   | 74.0 ms                                                | 74.5 ms: 1.01x slower                                                 |
| xml_etree_generate               | 57.1 ms                                                | 58.1 ms: 1.02x slower                                                 |
| sphinx                           | 602 ms                                                 | 614 ms: 1.02x slower                                                  |
| scimark_fft                      | 200 ms                                                 | 206 ms: 1.03x slower                                                  |
| float                            | 55.8 ms                                                | 57.7 ms: 1.03x slower                                                 |
| richards                         | 36.2 ms                                                | 37.4 ms: 1.03x slower                                                 |
| sqlite_synth                     | 1.55 us                                                | 1.61 us: 1.04x slower                                                 |
| regex_compile                    | 78.3 ms                                                | 81.4 ms: 1.04x slower                                                 |
| xml_etree_process                | 41.3 ms                                                | 43.0 ms: 1.04x slower                                                 |
| 2to3                             | 179 ms                                                 | 186 ms: 1.04x slower                                                  |
| genshi_text                      | 16.9 ms                                                | 17.6 ms: 1.04x slower                                                 |
| async_tree_eager                 | 69.9 ms                                                | 73.0 ms: 1.04x slower                                                 |
| docutils                         | 1.44 sec                                               | 1.51 sec: 1.05x slower                                                |
| scimark_monte_carlo              | 50.4 ms                                                | 52.8 ms: 1.05x slower                                                 |
| hexiom                           | 4.87 ms                                                | 5.10 ms: 1.05x slower                                                 |
| sympy_expand                     | 248 ms                                                 | 261 ms: 1.05x slower                                                  |
| json_dumps                       | 6.47 ms                                                | 6.83 ms: 1.06x slower                                                 |
| pycparser                        | 701 ms                                                 | 741 ms: 1.06x slower                                                  |
| sympy_str                        | 146 ms                                                 | 154 ms: 1.06x slower                                                  |
| deltablue                        | 2.65 ms                                                | 2.81 ms: 1.06x slower                                                 |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.17 ms: 1.06x slower                                                 |
| pathlib                          | 23.2 ms                                                | 24.7 ms: 1.06x slower                                                 |
| richards_super                   | 39.2 ms                                                | 41.9 ms: 1.07x slower                                                 |
| genshi_xml                       | 34.1 ms                                                | 36.5 ms: 1.07x slower                                                 |
| unpickle_pure_python             | 165 us                                                 | 177 us: 1.07x slower                                                  |
| sympy_sum                        | 75.1 ms                                                | 81.3 ms: 1.08x slower                                                 |
| gc_traversal                     | 2.94 ms                                                | 3.19 ms: 1.09x slower                                                 |
| typing_runtime_protocols         | 101 us                                                 | 110 us: 1.10x slower                                                  |
| comprehensions                   | 12.0 us                                                | 13.1 us: 1.10x slower                                                 |
| scimark_lu                       | 75.9 ms                                                | 84.3 ms: 1.11x slower                                                 |
| crypto_pyaes                     | 55.3 ms                                                | 61.4 ms: 1.11x slower                                                 |
| fannkuch                         | 279 ms                                                 | 310 ms: 1.11x slower                                                  |
| pickle_pure_python               | 215 us                                                 | 241 us: 1.12x slower                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 1.35 ms: 1.13x slower                                                 |
| nbody                            | 73.6 ms                                                | 84.7 ms: 1.15x slower                                                 |
| nqueens                          | 61.8 ms                                                | 71.2 ms: 1.15x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 400 ms: 1.15x slower                                                  |
| pprint_pformat                   | 1.10 sec                                               | 1.27 sec: 1.15x slower                                                |
| logging_format                   | 3.85 us                                                | 4.44 us: 1.15x slower                                                 |
| pprint_safe_repr                 | 541 ms                                                 | 623 ms: 1.15x slower                                                  |
| raytrace                         | 181 ms                                                 | 212 ms: 1.17x slower                                                  |
| logging_simple                   | 3.56 us                                                | 4.19 us: 1.18x slower                                                 |
| chaos                            | 41.1 ms                                                | 48.4 ms: 1.18x slower                                                 |
| mako                             | 7.75 ms                                                | 9.19 ms: 1.19x slower                                                 |
| many_optionals                   | 409 us                                                 | 494 us: 1.21x slower                                                  |
| django_template                  | 20.5 ms                                                | 25.1 ms: 1.23x slower                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 183 ms: 1.33x slower                                                  |
| subparsers                       | 9.44 ms                                                | 14.9 ms: 1.58x slower                                                 |
| async_tree_eager_tg              | 47.4 ms                                                | 143 ms: 3.03x slower                                                  |
| logging_silent                   | 71.0 ns                                                | 347 ns: 4.89x slower                                                  |
| coverage                         | 46.2 ms                                                | 335 ms: 7.25x slower                                                  |
| thrift                           | 466 us                                                 | 43.9 ms: 94.31x slower                                                |
| Geometric mean                   | (ref)                                                  | 1.10x slower                                                          |

Benchmark hidden because not significant (4): dask, pidigits, asyncio_websockets, xml_etree_iterparse
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250613-3.15.0a0-6eb6c5d/bm-20250613-darwin-arm64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.079x slower

# HPT report

- Reliability score: 82.81% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.11x