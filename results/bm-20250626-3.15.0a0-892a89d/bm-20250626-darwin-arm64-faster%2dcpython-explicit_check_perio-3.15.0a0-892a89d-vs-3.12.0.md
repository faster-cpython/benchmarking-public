# Results vs. 3.12.0

- fork: faster-cpython
- ref: explicit_check_perio
- machine: darwin-arm64
- commit hash: 892a89d
- commit date: 2025-06-26
- overall geometric mean: 1.018x slower
- HPT reliability: 98.05%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 187 ms: 1.11x slower                                                            |
| docutils       | 1.45 sec                                               | 1.52 sec: 1.05x slower                                                          |
| html5lib       | 33.4 ms                                                | 34.3 ms: 1.03x slower                                                           |
| sphinx         | 613 ms                                                 | 618 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                  | 1.05x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 398 ms: 1.67x faster                                                            |
| async_tree_io                    | 672 ms                                                 | 411 ms: 1.63x faster                                                            |
| async_tree_io_tg                 | 673 ms                                                 | 413 ms: 1.63x faster                                                            |
| async_tree_eager_io_tg           | 617 ms                                                 | 405 ms: 1.52x faster                                                            |
| async_tree_memoization_tg        | 318 ms                                                 | 209 ms: 1.52x faster                                                            |
| async_tree_none_tg               | 255 ms                                                 | 172 ms: 1.49x faster                                                            |
| async_tree_none                  | 263 ms                                                 | 179 ms: 1.47x faster                                                            |
| async_tree_memoization           | 310 ms                                                 | 216 ms: 1.44x faster                                                            |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 424 ms: 1.24x faster                                                            |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 433 ms: 1.21x faster                                                            |
| async_tree_eager_memoization     | 168 ms                                                 | 149 ms: 1.12x faster                                                            |
| async_generators                 | 299 ms                                                 | 274 ms: 1.09x faster                                                            |
| coroutines                       | 19.7 ms                                                | 18.8 ms: 1.05x faster                                                           |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 367 ms: 1.02x faster                                                            |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 398 ms: 1.15x slower                                                            |
| async_tree_eager                 | 65.8 ms                                                | 76.5 ms: 1.16x slower                                                           |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 181 ms: 1.27x slower                                                            |
| async_tree_eager_tg              | 46.9 ms                                                | 142 ms: 3.03x slower                                                            |
| Geometric mean                   | (ref)                                                  | 1.14x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 283 ms                                                 | 284 ms: 1.00x slower                                                            |
| float          | 54.1 ms                                                | 57.2 ms: 1.06x slower                                                           |
| nbody          | 67.6 ms                                                | 85.1 ms: 1.26x slower                                                           |
| Geometric mean | (ref)                                                  | 1.10x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.42 ms: 1.01x faster                                                           |
| regex_dna      | 143 ms                                                 | 145 ms: 1.01x slower                                                            |
| regex_compile  | 75.9 ms                                                | 81.4 ms: 1.07x slower                                                           |
| regex_v8       | 15.1 ms                                                | 16.6 ms: 1.10x slower                                                           |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 105 ms: 1.03x faster                                                            |
| json_loads           | 17.0 us                                                | 16.5 us: 1.03x faster                                                           |
| xml_etree_iterparse  | 75.5 ms                                                | 74.1 ms: 1.02x faster                                                           |
| tomli_loads          | 1.36 sec                                               | 1.43 sec: 1.06x slower                                                          |
| xml_etree_generate   | 55.4 ms                                                | 59.0 ms: 1.06x slower                                                           |
| json_dumps           | 6.19 ms                                                | 6.81 ms: 1.10x slower                                                           |
| xml_etree_process    | 38.9 ms                                                | 43.5 ms: 1.12x slower                                                           |
| pickle_pure_python   | 197 us                                                 | 243 us: 1.24x slower                                                            |
| unpickle_pure_python | 145 us                                                 | 180 us: 1.24x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.08x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 13.2 ms                                                | 13.3 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 30.5 ms                                                | 36.6 ms: 1.20x slower                                                           |
| genshi_text     | 14.7 ms                                                | 18.2 ms: 1.24x slower                                                           |
| mako            | 7.44 ms                                                | 9.33 ms: 1.25x slower                                                           |
| django_template | 19.7 ms                                                | 25.3 ms: 1.28x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.24x slower                                                                    |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 15.1 ms: 2.13x faster                                                           |
| mdp                              | 1.49 sec                                               | 823 ms: 1.81x faster                                                            |
| async_tree_eager_io              | 666 ms                                                 | 398 ms: 1.67x faster                                                            |
| async_tree_io                    | 672 ms                                                 | 411 ms: 1.63x faster                                                            |
| async_tree_io_tg                 | 673 ms                                                 | 413 ms: 1.63x faster                                                            |
| async_tree_eager_io_tg           | 617 ms                                                 | 405 ms: 1.52x faster                                                            |
| async_tree_memoization_tg        | 318 ms                                                 | 209 ms: 1.52x faster                                                            |
| async_tree_none_tg               | 255 ms                                                 | 172 ms: 1.49x faster                                                            |
| async_tree_none                  | 263 ms                                                 | 179 ms: 1.47x faster                                                            |
| async_tree_memoization           | 310 ms                                                 | 216 ms: 1.44x faster                                                            |
| deepcopy                         | 226 us                                                 | 177 us: 1.28x faster                                                            |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 424 ms: 1.24x faster                                                            |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 433 ms: 1.21x faster                                                            |
| deepcopy_memo                    | 26.0 us                                                | 22.0 us: 1.18x faster                                                           |
| k_core                           | 1.72 sec                                               | 1.47 sec: 1.17x faster                                                          |
| async_tree_eager_memoization     | 168 ms                                                 | 149 ms: 1.12x faster                                                            |
| pathlib                          | 24.7 ms                                                | 22.6 ms: 1.09x faster                                                           |
| async_generators                 | 299 ms                                                 | 274 ms: 1.09x faster                                                            |
| dulwich_log                      | 29.2 ms                                                | 27.5 ms: 1.06x faster                                                           |
| pylint                           | 182 ms                                                 | 171 ms: 1.06x faster                                                            |
| spectral_norm                    | 76.5 ms                                                | 72.5 ms: 1.05x faster                                                           |
| deepcopy_reduce                  | 2.01 us                                                | 1.91 us: 1.05x faster                                                           |
| comprehensions                   | 14.0 us                                                | 13.3 us: 1.05x faster                                                           |
| coroutines                       | 19.7 ms                                                | 18.8 ms: 1.05x faster                                                           |
| xml_etree_parse                  | 108 ms                                                 | 105 ms: 1.03x faster                                                            |
| json_loads                       | 17.0 us                                                | 16.5 us: 1.03x faster                                                           |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 367 ms: 1.02x faster                                                            |
| xml_etree_iterparse              | 75.5 ms                                                | 74.1 ms: 1.02x faster                                                           |
| json                             | 3.00 ms                                                | 2.95 ms: 1.02x faster                                                           |
| dask                             | 779 ms                                                 | 769 ms: 1.01x faster                                                            |
| regex_effbot                     | 2.44 ms                                                | 2.42 ms: 1.01x faster                                                           |
| bpe_tokeniser                    | 3.28 sec                                               | 3.27 sec: 1.00x faster                                                          |
| pidigits                         | 283 ms                                                 | 284 ms: 1.00x slower                                                            |
| python_startup_no_site           | 13.2 ms                                                | 13.3 ms: 1.01x slower                                                           |
| sphinx                           | 613 ms                                                 | 618 ms: 1.01x slower                                                            |
| thrift                           | 468 us                                                 | 472 us: 1.01x slower                                                            |
| go                               | 98.5 ms                                                | 99.7 ms: 1.01x slower                                                           |
| regex_dna                        | 143 ms                                                 | 145 ms: 1.01x slower                                                            |
| connected_components             | 300 ms                                                 | 305 ms: 1.02x slower                                                            |
| sympy_integrate                  | 11.1 ms                                                | 11.3 ms: 1.02x slower                                                           |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.22 ms: 1.02x slower                                                           |
| html5lib                         | 33.4 ms                                                | 34.3 ms: 1.03x slower                                                           |
| raytrace                         | 204 ms                                                 | 211 ms: 1.04x slower                                                            |
| scimark_fft                      | 194 ms                                                 | 203 ms: 1.04x slower                                                            |
| docutils                         | 1.45 sec                                               | 1.52 sec: 1.05x slower                                                          |
| sqlite_synth                     | 1.55 us                                                | 1.63 us: 1.05x slower                                                           |
| scimark_sor                      | 85.8 ms                                                | 90.4 ms: 1.05x slower                                                           |
| float                            | 54.1 ms                                                | 57.2 ms: 1.06x slower                                                           |
| tomli_loads                      | 1.36 sec                                               | 1.43 sec: 1.06x slower                                                          |
| xml_etree_generate               | 55.4 ms                                                | 59.0 ms: 1.06x slower                                                           |
| deltablue                        | 2.57 ms                                                | 2.73 ms: 1.07x slower                                                           |
| generators                       | 29.4 ms                                                | 31.5 ms: 1.07x slower                                                           |
| regex_compile                    | 75.9 ms                                                | 81.4 ms: 1.07x slower                                                           |
| sympy_sum                        | 76.2 ms                                                | 82.1 ms: 1.08x slower                                                           |
| sympy_str                        | 144 ms                                                 | 155 ms: 1.08x slower                                                            |
| gc_traversal                     | 2.95 ms                                                | 3.19 ms: 1.08x slower                                                           |
| pyflate                          | 311 ms                                                 | 339 ms: 1.09x slower                                                            |
| meteor_contest                   | 69.1 ms                                                | 75.3 ms: 1.09x slower                                                           |
| regex_v8                         | 15.1 ms                                                | 16.6 ms: 1.10x slower                                                           |
| json_dumps                       | 6.19 ms                                                | 6.81 ms: 1.10x slower                                                           |
| pycparser                        | 673 ms                                                 | 744 ms: 1.11x slower                                                            |
| 2to3                             | 168 ms                                                 | 187 ms: 1.11x slower                                                            |
| chaos                            | 41.6 ms                                                | 46.1 ms: 1.11x slower                                                           |
| xml_etree_process                | 38.9 ms                                                | 43.5 ms: 1.12x slower                                                           |
| sympy_expand                     | 233 ms                                                 | 263 ms: 1.13x slower                                                            |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 398 ms: 1.15x slower                                                            |
| typing_runtime_protocols         | 91.5 us                                                | 106 us: 1.16x slower                                                            |
| logging_format                   | 3.90 us                                                | 4.53 us: 1.16x slower                                                           |
| scimark_lu                       | 73.5 ms                                                | 85.3 ms: 1.16x slower                                                           |
| async_tree_eager                 | 65.8 ms                                                | 76.5 ms: 1.16x slower                                                           |
| logging_simple                   | 3.60 us                                                | 4.22 us: 1.17x slower                                                           |
| hexiom                           | 4.38 ms                                                | 5.14 ms: 1.17x slower                                                           |
| create_gc_cycles                 | 1.15 ms                                                | 1.36 ms: 1.18x slower                                                           |
| fannkuch                         | 250 ms                                                 | 296 ms: 1.18x slower                                                            |
| crypto_pyaes                     | 51.4 ms                                                | 61.3 ms: 1.19x slower                                                           |
| scimark_monte_carlo              | 44.5 ms                                                | 53.1 ms: 1.19x slower                                                           |
| nqueens                          | 59.5 ms                                                | 71.3 ms: 1.20x slower                                                           |
| genshi_xml                       | 30.5 ms                                                | 36.6 ms: 1.20x slower                                                           |
| richards_super                   | 34.6 ms                                                | 41.5 ms: 1.20x slower                                                           |
| telco                            | 3.92 ms                                                | 4.73 ms: 1.21x slower                                                           |
| richards                         | 30.6 ms                                                | 37.7 ms: 1.23x slower                                                           |
| pickle_pure_python               | 197 us                                                 | 243 us: 1.24x slower                                                            |
| unpickle_pure_python             | 145 us                                                 | 180 us: 1.24x slower                                                            |
| genshi_text                      | 14.7 ms                                                | 18.2 ms: 1.24x slower                                                           |
| many_optionals                   | 403 us                                                 | 503 us: 1.25x slower                                                            |
| mako                             | 7.44 ms                                                | 9.33 ms: 1.25x slower                                                           |
| nbody                            | 67.6 ms                                                | 85.1 ms: 1.26x slower                                                           |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 181 ms: 1.27x slower                                                            |
| coverage                         | 38.5 ms                                                | 49.1 ms: 1.28x slower                                                           |
| django_template                  | 19.7 ms                                                | 25.3 ms: 1.28x slower                                                           |
| pprint_pformat                   | 986 ms                                                 | 1.28 sec: 1.29x slower                                                          |
| pprint_safe_repr                 | 483 ms                                                 | 629 ms: 1.30x slower                                                            |
| async_tree_eager_tg              | 46.9 ms                                                | 142 ms: 3.03x slower                                                            |
| logging_silent                   | 72.5 ns                                                | 346 ns: 4.77x slower                                                            |
| Geometric mean                   | (ref)                                                  | 1.03x slower                                                                    |

Benchmark hidden because not significant (3): python_startup, asyncio_websockets, shortest_path
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250626-3.15.0a0-892a89d/bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.018x slower

# HPT report

- Reliability score: 98.05% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.12x