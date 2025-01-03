# Results vs. 3.13.0

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 4c14f03
- commit date: 2025-01-03
- overall geometric mean: 1.118x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250103-darwin-arm64-python-main-3.14.0a3+-4c14f03 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 181 ms                                                 | 188 ms: 1.04x slower                                   |
| docutils       | 1.44 sec                                               | 1.47 sec: 1.02x slower                                 |
| html5lib       | 36.6 ms                                                | 29.3 ms: 1.25x faster                                  |
| sphinx         | 600 ms                                                 | 565 ms: 1.06x faster                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250103-darwin-arm64-python-main-3.14.0a3+-4c14f03 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_memoization_tg        | 289 ms                                                 | 191 ms: 1.52x faster                                   |
| async_tree_eager_io              | 514 ms                                                 | 362 ms: 1.42x faster                                   |
| async_tree_io_tg                 | 499 ms                                                 | 355 ms: 1.41x faster                                   |
| async_tree_io                    | 510 ms                                                 | 368 ms: 1.39x faster                                   |
| async_tree_none_tg               | 199 ms                                                 | 148 ms: 1.34x faster                                   |
| async_tree_memoization           | 268 ms                                                 | 201 ms: 1.34x faster                                   |
| async_tree_none                  | 212 ms                                                 | 161 ms: 1.32x faster                                   |
| async_tree_eager_io_tg           | 481 ms                                                 | 370 ms: 1.30x faster                                   |
| coroutines                       | 19.8 ms                                                | 16.0 ms: 1.23x faster                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 141 ms: 1.19x faster                                   |
| async_tree_eager                 | 69.9 ms                                                | 61.7 ms: 1.13x faster                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 124 ms: 1.11x faster                                   |
| async_tree_eager_tg              | 48.0 ms                                                | 43.2 ms: 1.11x faster                                  |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 414 ms: 1.11x faster                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 412 ms: 1.09x faster                                   |
| async_generators                 | 292 ms                                                 | 276 ms: 1.06x faster                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 359 ms: 1.04x faster                                   |
| async_tree_eager_cpu_io_mixed_tg | 346 ms                                                 | 339 ms: 1.02x faster                                   |
| Geometric mean                   | (ref)                                                  | 1.21x faster                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250103-darwin-arm64-python-main-3.14.0a3+-4c14f03 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 56.3 ms                                                | 46.3 ms: 1.22x faster                                  |
| nbody          | 73.9 ms                                                | 67.8 ms: 1.09x faster                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250103-darwin-arm64-python-main-3.14.0a3+-4c14f03 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 2.62 ms                                                | 2.06 ms: 1.27x faster                                  |
| regex_compile  | 78.6 ms                                                | 67.4 ms: 1.17x faster                                  |
| regex_v8       | 17.0 ms                                                | 15.7 ms: 1.08x faster                                  |
| regex_dna      | 148 ms                                                 | 138 ms: 1.07x faster                                   |
| Geometric mean | (ref)                                                  | 1.14x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250103-darwin-arm64-python-main-3.14.0a3+-4c14f03 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| tomli_loads          | 1.56 sec                                               | 1.21 sec: 1.29x faster                                 |
| unpickle_pure_python | 164 us                                                 | 137 us: 1.20x faster                                   |
| xml_etree_generate   | 57.0 ms                                                | 52.5 ms: 1.09x faster                                  |
| pickle_pure_python   | 214 us                                                 | 197 us: 1.09x faster                                   |
| xml_etree_process    | 41.0 ms                                                | 38.0 ms: 1.08x faster                                  |
| xml_etree_parse      | 107 ms                                                 | 102 ms: 1.05x faster                                   |
| xml_etree_iterparse  | 74.1 ms                                                | 70.9 ms: 1.05x faster                                  |
| json_loads           | 17.0 us                                                | 16.3 us: 1.04x faster                                  |
| json_dumps           | 6.51 ms                                                | 7.30 ms: 1.12x slower                                  |
| Geometric mean       | (ref)                                                  | 1.08x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250103-darwin-arm64-python-main-3.14.0a3+-4c14f03 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 15.8 ms                                                | 12.8 ms: 1.23x faster                                  |
| python_startup         | 20.6 ms                                                | 17.5 ms: 1.18x faster                                  |
| Geometric mean         | (ref)                                                  | 1.21x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250103-darwin-arm64-python-main-3.14.0a3+-4c14f03 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 13.5 ms: 1.25x faster                                  |
| genshi_xml      | 34.1 ms                                                | 28.3 ms: 1.21x faster                                  |
| mako            | 7.70 ms                                                | 7.13 ms: 1.08x faster                                  |
| django_template | 20.5 ms                                                | 21.0 ms: 1.02x slower                                  |
| Geometric mean  | (ref)                                                  | 1.12x faster                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250103-darwin-arm64-python-main-3.14.0a3+-4c14f03 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deepcopy                         | 234 us                                                 | 150 us: 1.56x faster                                   |
| async_tree_memoization_tg        | 289 ms                                                 | 191 ms: 1.52x faster                                   |
| deepcopy_memo                    | 27.3 us                                                | 18.0 us: 1.51x faster                                  |
| go                               | 115 ms                                                 | 78.2 ms: 1.47x faster                                  |
| async_tree_eager_io              | 514 ms                                                 | 362 ms: 1.42x faster                                   |
| async_tree_io_tg                 | 499 ms                                                 | 355 ms: 1.41x faster                                   |
| generators                       | 31.5 ms                                                | 22.4 ms: 1.40x faster                                  |
| async_tree_io                    | 510 ms                                                 | 368 ms: 1.39x faster                                   |
| async_tree_none_tg               | 199 ms                                                 | 148 ms: 1.34x faster                                   |
| scimark_sor                      | 106 ms                                                 | 78.7 ms: 1.34x faster                                  |
| deepcopy_reduce                  | 2.08 us                                                | 1.56 us: 1.34x faster                                  |
| async_tree_memoization           | 268 ms                                                 | 201 ms: 1.34x faster                                   |
| async_tree_none                  | 212 ms                                                 | 161 ms: 1.32x faster                                   |
| async_tree_eager_io_tg           | 481 ms                                                 | 370 ms: 1.30x faster                                   |
| tomli_loads                      | 1.56 sec                                               | 1.21 sec: 1.29x faster                                 |
| regex_effbot                     | 2.62 ms                                                | 2.06 ms: 1.27x faster                                  |
| genshi_text                      | 16.9 ms                                                | 13.5 ms: 1.25x faster                                  |
| html5lib                         | 36.6 ms                                                | 29.3 ms: 1.25x faster                                  |
| coroutines                       | 19.8 ms                                                | 16.0 ms: 1.23x faster                                  |
| python_startup_no_site           | 15.8 ms                                                | 12.8 ms: 1.23x faster                                  |
| spectral_norm                    | 76.3 ms                                                | 61.8 ms: 1.23x faster                                  |
| float                            | 56.3 ms                                                | 46.3 ms: 1.22x faster                                  |
| pyflate                          | 355 ms                                                 | 293 ms: 1.21x faster                                   |
| scimark_monte_carlo              | 50.6 ms                                                | 41.9 ms: 1.21x faster                                  |
| genshi_xml                       | 34.1 ms                                                | 28.3 ms: 1.21x faster                                  |
| unpickle_pure_python             | 164 us                                                 | 137 us: 1.20x faster                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 141 ms: 1.19x faster                                   |
| pprint_pformat                   | 1.10 sec                                               | 926 ms: 1.19x faster                                   |
| python_startup                   | 20.6 ms                                                | 17.5 ms: 1.18x faster                                  |
| pprint_safe_repr                 | 535 ms                                                 | 458 ms: 1.17x faster                                   |
| regex_compile                    | 78.6 ms                                                | 67.4 ms: 1.17x faster                                  |
| scimark_fft                      | 200 ms                                                 | 172 ms: 1.16x faster                                   |
| hexiom                           | 4.83 ms                                                | 4.17 ms: 1.16x faster                                  |
| fannkuch                         | 285 ms                                                 | 248 ms: 1.15x faster                                   |
| deltablue                        | 2.67 ms                                                | 2.35 ms: 1.14x faster                                  |
| logging_simple                   | 3.59 us                                                | 3.17 us: 1.13x faster                                  |
| async_tree_eager                 | 69.9 ms                                                | 61.7 ms: 1.13x faster                                  |
| sqlglot_parse                    | 859 us                                                 | 763 us: 1.13x faster                                   |
| scimark_sparse_mat_mult          | 3.00 ms                                                | 2.67 ms: 1.12x faster                                  |
| pylint                           | 179 ms                                                 | 160 ms: 1.12x faster                                   |
| logging_format                   | 3.90 us                                                | 3.49 us: 1.12x faster                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 124 ms: 1.11x faster                                   |
| richards_super                   | 39.2 ms                                                | 35.2 ms: 1.11x faster                                  |
| richards                         | 35.2 ms                                                | 31.6 ms: 1.11x faster                                  |
| async_tree_eager_tg              | 48.0 ms                                                | 43.2 ms: 1.11x faster                                  |
| pycparser                        | 708 ms                                                 | 637 ms: 1.11x faster                                   |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 414 ms: 1.11x faster                                   |
| sqlglot_transpile                | 1.03 ms                                                | 928 us: 1.11x faster                                   |
| nqueens                          | 61.8 ms                                                | 56.0 ms: 1.10x faster                                  |
| bpe_tokeniser                    | 3.25 sec                                               | 2.97 sec: 1.09x faster                                 |
| nbody                            | 73.9 ms                                                | 67.8 ms: 1.09x faster                                  |
| bench_mp_pool                    | 64.9 ms                                                | 59.6 ms: 1.09x faster                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 412 ms: 1.09x faster                                   |
| xml_etree_generate               | 57.0 ms                                                | 52.5 ms: 1.09x faster                                  |
| pickle_pure_python               | 214 us                                                 | 197 us: 1.09x faster                                   |
| chaos                            | 41.3 ms                                                | 38.0 ms: 1.09x faster                                  |
| k_core                           | 1.62 sec                                               | 1.49 sec: 1.08x faster                                 |
| mako                             | 7.70 ms                                                | 7.13 ms: 1.08x faster                                  |
| xml_etree_process                | 41.0 ms                                                | 38.0 ms: 1.08x faster                                  |
| regex_v8                         | 17.0 ms                                                | 15.7 ms: 1.08x faster                                  |
| bench_thread_pool                | 508 us                                                 | 472 us: 1.08x faster                                   |
| logging_silent                   | 70.1 ns                                                | 65.2 ns: 1.07x faster                                  |
| regex_dna                        | 148 ms                                                 | 138 ms: 1.07x faster                                   |
| shortest_path                    | 349 ms                                                 | 326 ms: 1.07x faster                                   |
| connected_components             | 320 ms                                                 | 300 ms: 1.07x faster                                   |
| sqlglot_optimize                 | 34.8 ms                                                | 32.5 ms: 1.07x faster                                  |
| typing_runtime_protocols         | 103 us                                                 | 96.1 us: 1.07x faster                                  |
| raytrace                         | 181 ms                                                 | 170 ms: 1.06x faster                                   |
| sphinx                           | 600 ms                                                 | 565 ms: 1.06x faster                                   |
| json                             | 3.06 ms                                                | 2.88 ms: 1.06x faster                                  |
| scimark_lu                       | 76.7 ms                                                | 72.2 ms: 1.06x faster                                  |
| thrift                           | 465 us                                                 | 439 us: 1.06x faster                                   |
| async_generators                 | 292 ms                                                 | 276 ms: 1.06x faster                                   |
| telco                            | 4.79 ms                                                | 4.55 ms: 1.05x faster                                  |
| sympy_expand                     | 247 ms                                                 | 235 ms: 1.05x faster                                   |
| xml_etree_parse                  | 107 ms                                                 | 102 ms: 1.05x faster                                   |
| sqlglot_normalize                | 188 ms                                                 | 179 ms: 1.05x faster                                   |
| dulwich_log                      | 28.6 ms                                                | 27.3 ms: 1.05x faster                                  |
| meteor_contest                   | 75.1 ms                                                | 71.9 ms: 1.05x faster                                  |
| xml_etree_iterparse              | 74.1 ms                                                | 70.9 ms: 1.05x faster                                  |
| json_loads                       | 17.0 us                                                | 16.3 us: 1.04x faster                                  |
| sqlalchemy_imperative            | 6.68 ms                                                | 6.42 ms: 1.04x faster                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 359 ms: 1.04x faster                                   |
| pathlib                          | 23.3 ms                                                | 22.7 ms: 1.02x faster                                  |
| crypto_pyaes                     | 54.4 ms                                                | 53.2 ms: 1.02x faster                                  |
| async_tree_eager_cpu_io_mixed_tg | 346 ms                                                 | 339 ms: 1.02x faster                                   |
| sympy_str                        | 145 ms                                                 | 142 ms: 1.02x faster                                   |
| sqlalchemy_declarative           | 59.1 ms                                                | 58.2 ms: 1.01x faster                                  |
| coverage                         | 45.5 ms                                                | 45.0 ms: 1.01x faster                                  |
| mdp                              | 1.50 sec                                               | 1.49 sec: 1.01x faster                                 |
| sqlite_synth                     | 1.56 us                                                | 1.55 us: 1.01x faster                                  |
| docutils                         | 1.44 sec                                               | 1.47 sec: 1.02x slower                                 |
| django_template                  | 20.5 ms                                                | 21.0 ms: 1.02x slower                                  |
| 2to3                             | 181 ms                                                 | 188 ms: 1.04x slower                                   |
| comprehensions                   | 12.0 us                                                | 12.5 us: 1.04x slower                                  |
| gc_traversal                     | 2.93 ms                                                | 3.10 ms: 1.06x slower                                  |
| create_gc_cycles                 | 1.20 ms                                                | 1.29 ms: 1.07x slower                                  |
| json_dumps                       | 6.51 ms                                                | 7.30 ms: 1.12x slower                                  |
| subparsers                       | 9.50 ms                                                | 11.9 ms: 1.25x slower                                  |
| many_optionals                   | 324 us                                                 | 441 us: 1.36x slower                                   |
| Geometric mean                   | (ref)                                                  | 1.12x faster                                           |

Benchmark hidden because not significant (4): asyncio_websockets, sympy_integrate, pidigits, sympy_sum
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20250103-3.14.0a3+-4c14f03/bm-20250103-darwin-arm64-python-main-3.14.0a3+-4c14f03.json: mypy2

- Geometric mean (including insignificant results): 1.118x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.03x