# Results vs. 3.12.0

- fork: faster-cpython
- ref: use_ob_flags_for_gc
- machine: darwin-arm64
- commit hash: 53e0c51
- commit date: 2025-07-10
- overall geometric mean: 1.017x slower
- HPT reliability: 97.13%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250710-darwin-arm64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-53e0c51 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 188 ms: 1.12x slower                                                           |
| docutils       | 1.45 sec                                               | 1.52 sec: 1.04x slower                                                         |
| html5lib       | 33.4 ms                                                | 34.4 ms: 1.03x slower                                                          |
| sphinx         | 613 ms                                                 | 620 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                  | 1.05x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250710-darwin-arm64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-53e0c51 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 389 ms: 1.71x faster                                                           |
| async_tree_io                    | 672 ms                                                 | 404 ms: 1.66x faster                                                           |
| async_tree_io_tg                 | 673 ms                                                 | 407 ms: 1.65x faster                                                           |
| async_tree_eager_io_tg           | 617 ms                                                 | 394 ms: 1.57x faster                                                           |
| async_tree_memoization_tg        | 318 ms                                                 | 205 ms: 1.55x faster                                                           |
| async_tree_none_tg               | 255 ms                                                 | 172 ms: 1.49x faster                                                           |
| async_tree_none                  | 263 ms                                                 | 180 ms: 1.46x faster                                                           |
| async_tree_memoization           | 310 ms                                                 | 214 ms: 1.45x faster                                                           |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 421 ms: 1.25x faster                                                           |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 432 ms: 1.22x faster                                                           |
| async_tree_eager_memoization     | 168 ms                                                 | 150 ms: 1.11x faster                                                           |
| async_generators                 | 299 ms                                                 | 278 ms: 1.07x faster                                                           |
| coroutines                       | 19.7 ms                                                | 19.1 ms: 1.03x faster                                                          |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 368 ms: 1.02x faster                                                           |
| async_tree_eager                 | 65.8 ms                                                | 73.5 ms: 1.12x slower                                                          |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 398 ms: 1.15x slower                                                           |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 181 ms: 1.27x slower                                                           |
| async_tree_eager_tg              | 46.9 ms                                                | 142 ms: 3.03x slower                                                           |
| Geometric mean                   | (ref)                                                  | 1.15x faster                                                                   |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250710-darwin-arm64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-53e0c51 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 283 ms                                                 | 286 ms: 1.01x slower                                                           |
| float          | 54.1 ms                                                | 59.9 ms: 1.11x slower                                                          |
| nbody          | 67.6 ms                                                | 86.6 ms: 1.28x slower                                                          |
| Geometric mean | (ref)                                                  | 1.13x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250710-darwin-arm64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-53e0c51 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.36 ms: 1.03x faster                                                          |
| regex_dna      | 143 ms                                                 | 144 ms: 1.01x slower                                                           |
| regex_compile  | 75.9 ms                                                | 82.2 ms: 1.08x slower                                                          |
| regex_v8       | 15.1 ms                                                | 16.3 ms: 1.08x slower                                                          |
| Geometric mean | (ref)                                                  | 1.03x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250710-darwin-arm64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-53e0c51 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 98.7 ms: 1.09x faster                                                          |
| xml_etree_iterparse  | 75.5 ms                                                | 73.5 ms: 1.03x faster                                                          |
| json_loads           | 17.0 us                                                | 16.7 us: 1.02x faster                                                          |
| xml_etree_generate   | 55.4 ms                                                | 58.9 ms: 1.06x slower                                                          |
| tomli_loads          | 1.36 sec                                               | 1.45 sec: 1.07x slower                                                         |
| json_dumps           | 6.19 ms                                                | 6.94 ms: 1.12x slower                                                          |
| xml_etree_process    | 38.9 ms                                                | 43.9 ms: 1.13x slower                                                          |
| pickle_pure_python   | 197 us                                                 | 243 us: 1.23x slower                                                           |
| unpickle_pure_python | 145 us                                                 | 182 us: 1.25x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.08x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250710-darwin-arm64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-53e0c51 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 16.7 ms: 1.06x faster                                                          |
| python_startup_no_site | 13.2 ms                                                | 12.4 ms: 1.06x faster                                                          |
| Geometric mean         | (ref)                                                  | 1.06x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250710-darwin-arm64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-53e0c51 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 30.5 ms                                                | 36.7 ms: 1.20x slower                                                          |
| genshi_text     | 14.7 ms                                                | 17.9 ms: 1.22x slower                                                          |
| mako            | 7.44 ms                                                | 9.16 ms: 1.23x slower                                                          |
| django_template | 19.7 ms                                                | 25.1 ms: 1.27x slower                                                          |
| Geometric mean  | (ref)                                                  | 1.23x slower                                                                   |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250710-darwin-arm64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-53e0c51 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 14.9 ms: 2.16x faster                                                          |
| mdp                              | 1.49 sec                                               | 836 ms: 1.79x faster                                                           |
| async_tree_eager_io              | 666 ms                                                 | 389 ms: 1.71x faster                                                           |
| async_tree_io                    | 672 ms                                                 | 404 ms: 1.66x faster                                                           |
| async_tree_io_tg                 | 673 ms                                                 | 407 ms: 1.65x faster                                                           |
| async_tree_eager_io_tg           | 617 ms                                                 | 394 ms: 1.57x faster                                                           |
| async_tree_memoization_tg        | 318 ms                                                 | 205 ms: 1.55x faster                                                           |
| async_tree_none_tg               | 255 ms                                                 | 172 ms: 1.49x faster                                                           |
| async_tree_none                  | 263 ms                                                 | 180 ms: 1.46x faster                                                           |
| async_tree_memoization           | 310 ms                                                 | 214 ms: 1.45x faster                                                           |
| deepcopy                         | 226 us                                                 | 177 us: 1.28x faster                                                           |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 421 ms: 1.25x faster                                                           |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 432 ms: 1.22x faster                                                           |
| deepcopy_memo                    | 26.0 us                                                | 22.0 us: 1.18x faster                                                          |
| k_core                           | 1.72 sec                                               | 1.47 sec: 1.17x faster                                                         |
| async_tree_eager_memoization     | 168 ms                                                 | 150 ms: 1.11x faster                                                           |
| xml_etree_parse                  | 108 ms                                                 | 98.7 ms: 1.09x faster                                                          |
| pylint                           | 182 ms                                                 | 169 ms: 1.08x faster                                                           |
| async_generators                 | 299 ms                                                 | 278 ms: 1.07x faster                                                           |
| python_startup                   | 17.8 ms                                                | 16.7 ms: 1.06x faster                                                          |
| pathlib                          | 24.7 ms                                                | 23.3 ms: 1.06x faster                                                          |
| python_startup_no_site           | 13.2 ms                                                | 12.4 ms: 1.06x faster                                                          |
| deepcopy_reduce                  | 2.01 us                                                | 1.90 us: 1.06x faster                                                          |
| comprehensions                   | 14.0 us                                                | 13.3 us: 1.05x faster                                                          |
| spectral_norm                    | 76.5 ms                                                | 73.3 ms: 1.04x faster                                                          |
| regex_effbot                     | 2.44 ms                                                | 2.36 ms: 1.03x faster                                                          |
| coroutines                       | 19.7 ms                                                | 19.1 ms: 1.03x faster                                                          |
| xml_etree_iterparse              | 75.5 ms                                                | 73.5 ms: 1.03x faster                                                          |
| json_loads                       | 17.0 us                                                | 16.7 us: 1.02x faster                                                          |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 368 ms: 1.02x faster                                                           |
| dask                             | 779 ms                                                 | 770 ms: 1.01x faster                                                           |
| bpe_tokeniser                    | 3.28 sec                                               | 3.28 sec: 1.00x faster                                                         |
| regex_dna                        | 143 ms                                                 | 144 ms: 1.01x slower                                                           |
| pidigits                         | 283 ms                                                 | 286 ms: 1.01x slower                                                           |
| sphinx                           | 613 ms                                                 | 620 ms: 1.01x slower                                                           |
| go                               | 98.5 ms                                                | 100 ms: 1.02x slower                                                           |
| dulwich_log                      | 29.2 ms                                                | 29.7 ms: 1.02x slower                                                          |
| thrift                           | 468 us                                                 | 478 us: 1.02x slower                                                           |
| connected_components             | 300 ms                                                 | 307 ms: 1.02x slower                                                           |
| html5lib                         | 33.4 ms                                                | 34.4 ms: 1.03x slower                                                          |
| sympy_integrate                  | 11.1 ms                                                | 11.5 ms: 1.04x slower                                                          |
| docutils                         | 1.45 sec                                               | 1.52 sec: 1.04x slower                                                         |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.31 ms: 1.05x slower                                                          |
| raytrace                         | 204 ms                                                 | 215 ms: 1.06x slower                                                           |
| gc_traversal                     | 2.95 ms                                                | 3.11 ms: 1.06x slower                                                          |
| scimark_fft                      | 194 ms                                                 | 205 ms: 1.06x slower                                                           |
| logging_format                   | 3.90 us                                                | 4.14 us: 1.06x slower                                                          |
| xml_etree_generate               | 55.4 ms                                                | 58.9 ms: 1.06x slower                                                          |
| logging_simple                   | 3.60 us                                                | 3.84 us: 1.07x slower                                                          |
| tomli_loads                      | 1.36 sec                                               | 1.45 sec: 1.07x slower                                                         |
| sqlite_synth                     | 1.55 us                                                | 1.65 us: 1.07x slower                                                          |
| logging_silent                   | 72.5 ns                                                | 77.7 ns: 1.07x slower                                                          |
| scimark_sor                      | 85.8 ms                                                | 92.2 ms: 1.07x slower                                                          |
| sympy_sum                        | 76.2 ms                                                | 82.3 ms: 1.08x slower                                                          |
| regex_compile                    | 75.9 ms                                                | 82.2 ms: 1.08x slower                                                          |
| regex_v8                         | 15.1 ms                                                | 16.3 ms: 1.08x slower                                                          |
| meteor_contest                   | 69.1 ms                                                | 74.9 ms: 1.08x slower                                                          |
| generators                       | 29.4 ms                                                | 31.9 ms: 1.09x slower                                                          |
| pyflate                          | 311 ms                                                 | 338 ms: 1.09x slower                                                           |
| deltablue                        | 2.57 ms                                                | 2.81 ms: 1.10x slower                                                          |
| sympy_str                        | 144 ms                                                 | 158 ms: 1.10x slower                                                           |
| create_gc_cycles                 | 1.15 ms                                                | 1.27 ms: 1.10x slower                                                          |
| float                            | 54.1 ms                                                | 59.9 ms: 1.11x slower                                                          |
| pycparser                        | 673 ms                                                 | 748 ms: 1.11x slower                                                           |
| 2to3                             | 168 ms                                                 | 188 ms: 1.12x slower                                                           |
| async_tree_eager                 | 65.8 ms                                                | 73.5 ms: 1.12x slower                                                          |
| json_dumps                       | 6.19 ms                                                | 6.94 ms: 1.12x slower                                                          |
| xml_etree_process                | 38.9 ms                                                | 43.9 ms: 1.13x slower                                                          |
| chaos                            | 41.6 ms                                                | 47.6 ms: 1.14x slower                                                          |
| sympy_expand                     | 233 ms                                                 | 267 ms: 1.15x slower                                                           |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 398 ms: 1.15x slower                                                           |
| scimark_lu                       | 73.5 ms                                                | 85.3 ms: 1.16x slower                                                          |
| hexiom                           | 4.38 ms                                                | 5.10 ms: 1.17x slower                                                          |
| typing_runtime_protocols         | 91.5 us                                                | 107 us: 1.17x slower                                                           |
| crypto_pyaes                     | 51.4 ms                                                | 60.8 ms: 1.18x slower                                                          |
| nqueens                          | 59.5 ms                                                | 71.6 ms: 1.20x slower                                                          |
| scimark_monte_carlo              | 44.5 ms                                                | 53.5 ms: 1.20x slower                                                          |
| genshi_xml                       | 30.5 ms                                                | 36.7 ms: 1.20x slower                                                          |
| genshi_text                      | 14.7 ms                                                | 17.9 ms: 1.22x slower                                                          |
| pprint_pformat                   | 986 ms                                                 | 1.21 sec: 1.22x slower                                                         |
| pprint_safe_repr                 | 483 ms                                                 | 594 ms: 1.23x slower                                                           |
| mako                             | 7.44 ms                                                | 9.16 ms: 1.23x slower                                                          |
| pickle_pure_python               | 197 us                                                 | 243 us: 1.23x slower                                                           |
| richards                         | 30.6 ms                                                | 37.8 ms: 1.24x slower                                                          |
| many_optionals                   | 403 us                                                 | 500 us: 1.24x slower                                                           |
| telco                            | 3.92 ms                                                | 4.89 ms: 1.25x slower                                                          |
| richards_super                   | 34.6 ms                                                | 43.4 ms: 1.25x slower                                                          |
| unpickle_pure_python             | 145 us                                                 | 182 us: 1.25x slower                                                           |
| django_template                  | 19.7 ms                                                | 25.1 ms: 1.27x slower                                                          |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 181 ms: 1.27x slower                                                           |
| nbody                            | 67.6 ms                                                | 86.6 ms: 1.28x slower                                                          |
| coverage                         | 38.5 ms                                                | 49.6 ms: 1.29x slower                                                          |
| fannkuch                         | 250 ms                                                 | 327 ms: 1.31x slower                                                           |
| async_tree_eager_tg              | 46.9 ms                                                | 142 ms: 3.03x slower                                                           |
| Geometric mean                   | (ref)                                                  | 1.02x slower                                                                   |

Benchmark hidden because not significant (3): json, shortest_path, asyncio_websockets
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250710-3.15.0a0-53e0c51/bm-20250710-darwin-arm64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-53e0c51.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.017x slower

# HPT report

- Reliability score: 97.13% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.13x