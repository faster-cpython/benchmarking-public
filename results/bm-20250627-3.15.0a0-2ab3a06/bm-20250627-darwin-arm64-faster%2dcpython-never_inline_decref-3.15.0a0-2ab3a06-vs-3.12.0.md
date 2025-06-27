# Results vs. 3.12.0

- fork: faster-cpython
- ref: never_inline_decref
- machine: darwin-arm64
- commit hash: 2ab3a06
- commit date: 2025-06-27
- overall geometric mean: 1.023x slower
- HPT reliability: 99.48%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-darwin-arm64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 191 ms: 1.13x slower                                                           |
| docutils       | 1.45 sec                                               | 1.53 sec: 1.06x slower                                                         |
| html5lib       | 33.4 ms                                                | 36.4 ms: 1.09x slower                                                          |
| Geometric mean | (ref)                                                  | 1.07x slower                                                                   |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-darwin-arm64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 393 ms: 1.69x faster                                                           |
| async_tree_io_tg                 | 673 ms                                                 | 408 ms: 1.65x faster                                                           |
| async_tree_io                    | 672 ms                                                 | 412 ms: 1.63x faster                                                           |
| async_tree_eager_io_tg           | 617 ms                                                 | 404 ms: 1.53x faster                                                           |
| async_tree_memoization_tg        | 318 ms                                                 | 209 ms: 1.52x faster                                                           |
| async_tree_none_tg               | 255 ms                                                 | 173 ms: 1.48x faster                                                           |
| async_tree_none                  | 263 ms                                                 | 180 ms: 1.47x faster                                                           |
| async_tree_memoization           | 310 ms                                                 | 218 ms: 1.42x faster                                                           |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 425 ms: 1.24x faster                                                           |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 438 ms: 1.20x faster                                                           |
| async_tree_eager_memoization     | 168 ms                                                 | 152 ms: 1.10x faster                                                           |
| async_generators                 | 299 ms                                                 | 285 ms: 1.05x faster                                                           |
| coroutines                       | 19.7 ms                                                | 19.0 ms: 1.04x faster                                                          |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 372 ms: 1.00x faster                                                           |
| async_tree_eager                 | 65.8 ms                                                | 73.7 ms: 1.12x slower                                                          |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 403 ms: 1.16x slower                                                           |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 183 ms: 1.29x slower                                                           |
| async_tree_eager_tg              | 46.9 ms                                                | 144 ms: 3.06x slower                                                           |
| Geometric mean                   | (ref)                                                  | 1.14x faster                                                                   |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-darwin-arm64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 283 ms                                                 | 284 ms: 1.00x slower                                                           |
| float          | 54.1 ms                                                | 58.2 ms: 1.08x slower                                                          |
| nbody          | 67.6 ms                                                | 85.4 ms: 1.26x slower                                                          |
| Geometric mean | (ref)                                                  | 1.11x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-darwin-arm64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.35 ms: 1.04x faster                                                          |
| regex_dna      | 143 ms                                                 | 139 ms: 1.03x faster                                                           |
| regex_v8       | 15.1 ms                                                | 15.9 ms: 1.05x slower                                                          |
| regex_compile  | 75.9 ms                                                | 81.8 ms: 1.08x slower                                                          |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-darwin-arm64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_loads           | 17.0 us                                                | 17.1 us: 1.00x slower                                                          |
| xml_etree_iterparse  | 75.5 ms                                                | 76.2 ms: 1.01x slower                                                          |
| xml_etree_parse      | 108 ms                                                 | 110 ms: 1.02x slower                                                           |
| tomli_loads          | 1.36 sec                                               | 1.45 sec: 1.07x slower                                                         |
| xml_etree_generate   | 55.4 ms                                                | 62.1 ms: 1.12x slower                                                          |
| json_dumps           | 6.19 ms                                                | 7.12 ms: 1.15x slower                                                          |
| xml_etree_process    | 38.9 ms                                                | 45.3 ms: 1.17x slower                                                          |
| unpickle_pure_python | 145 us                                                 | 177 us: 1.22x slower                                                           |
| pickle_pure_python   | 197 us                                                 | 241 us: 1.22x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.11x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-darwin-arm64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 18.1 ms: 1.02x slower                                                          |
| python_startup_no_site | 13.2 ms                                                | 13.6 ms: 1.03x slower                                                          |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-darwin-arm64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 30.5 ms                                                | 37.5 ms: 1.23x slower                                                          |
| mako            | 7.44 ms                                                | 9.21 ms: 1.24x slower                                                          |
| django_template | 19.7 ms                                                | 25.0 ms: 1.27x slower                                                          |
| genshi_text     | 14.7 ms                                                | 18.8 ms: 1.28x slower                                                          |
| Geometric mean  | (ref)                                                  | 1.25x slower                                                                   |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-darwin-arm64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 14.8 ms: 2.17x faster                                                          |
| mdp                              | 1.49 sec                                               | 848 ms: 1.76x faster                                                           |
| async_tree_eager_io              | 666 ms                                                 | 393 ms: 1.69x faster                                                           |
| async_tree_io_tg                 | 673 ms                                                 | 408 ms: 1.65x faster                                                           |
| async_tree_io                    | 672 ms                                                 | 412 ms: 1.63x faster                                                           |
| async_tree_eager_io_tg           | 617 ms                                                 | 404 ms: 1.53x faster                                                           |
| async_tree_memoization_tg        | 318 ms                                                 | 209 ms: 1.52x faster                                                           |
| async_tree_none_tg               | 255 ms                                                 | 173 ms: 1.48x faster                                                           |
| async_tree_none                  | 263 ms                                                 | 180 ms: 1.47x faster                                                           |
| async_tree_memoization           | 310 ms                                                 | 218 ms: 1.42x faster                                                           |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 425 ms: 1.24x faster                                                           |
| deepcopy                         | 226 us                                                 | 187 us: 1.21x faster                                                           |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 438 ms: 1.20x faster                                                           |
| k_core                           | 1.72 sec                                               | 1.48 sec: 1.16x faster                                                         |
| deepcopy_memo                    | 26.0 us                                                | 22.8 us: 1.14x faster                                                          |
| async_tree_eager_memoization     | 168 ms                                                 | 152 ms: 1.10x faster                                                           |
| dulwich_log                      | 29.2 ms                                                | 26.6 ms: 1.10x faster                                                          |
| pylint                           | 182 ms                                                 | 168 ms: 1.08x faster                                                           |
| comprehensions                   | 14.0 us                                                | 13.2 us: 1.06x faster                                                          |
| spectral_norm                    | 76.5 ms                                                | 72.7 ms: 1.05x faster                                                          |
| deepcopy_reduce                  | 2.01 us                                                | 1.92 us: 1.05x faster                                                          |
| async_generators                 | 299 ms                                                 | 285 ms: 1.05x faster                                                           |
| regex_effbot                     | 2.44 ms                                                | 2.35 ms: 1.04x faster                                                          |
| coroutines                       | 19.7 ms                                                | 19.0 ms: 1.04x faster                                                          |
| regex_dna                        | 143 ms                                                 | 139 ms: 1.03x faster                                                           |
| dask                             | 779 ms                                                 | 768 ms: 1.01x faster                                                           |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 372 ms: 1.00x faster                                                           |
| pidigits                         | 283 ms                                                 | 284 ms: 1.00x slower                                                           |
| json_loads                       | 17.0 us                                                | 17.1 us: 1.00x slower                                                          |
| thrift                           | 468 us                                                 | 470 us: 1.00x slower                                                           |
| connected_components             | 300 ms                                                 | 302 ms: 1.01x slower                                                           |
| bpe_tokeniser                    | 3.28 sec                                               | 3.30 sec: 1.01x slower                                                         |
| xml_etree_iterparse              | 75.5 ms                                                | 76.2 ms: 1.01x slower                                                          |
| raytrace                         | 204 ms                                                 | 206 ms: 1.01x slower                                                           |
| xml_etree_parse                  | 108 ms                                                 | 110 ms: 1.02x slower                                                           |
| python_startup                   | 17.8 ms                                                | 18.1 ms: 1.02x slower                                                          |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.20 ms: 1.02x slower                                                          |
| sympy_integrate                  | 11.1 ms                                                | 11.3 ms: 1.02x slower                                                          |
| python_startup_no_site           | 13.2 ms                                                | 13.6 ms: 1.03x slower                                                          |
| scimark_fft                      | 194 ms                                                 | 202 ms: 1.04x slower                                                           |
| sqlite_synth                     | 1.55 us                                                | 1.62 us: 1.05x slower                                                          |
| regex_v8                         | 15.1 ms                                                | 15.9 ms: 1.05x slower                                                          |
| scimark_sor                      | 85.8 ms                                                | 90.3 ms: 1.05x slower                                                          |
| docutils                         | 1.45 sec                                               | 1.53 sec: 1.06x slower                                                         |
| logging_format                   | 3.90 us                                                | 4.12 us: 1.06x slower                                                          |
| logging_simple                   | 3.60 us                                                | 3.82 us: 1.06x slower                                                          |
| tomli_loads                      | 1.36 sec                                               | 1.45 sec: 1.07x slower                                                         |
| go                               | 98.5 ms                                                | 106 ms: 1.07x slower                                                           |
| float                            | 54.1 ms                                                | 58.2 ms: 1.08x slower                                                          |
| sympy_sum                        | 76.2 ms                                                | 82.1 ms: 1.08x slower                                                          |
| regex_compile                    | 75.9 ms                                                | 81.8 ms: 1.08x slower                                                          |
| generators                       | 29.4 ms                                                | 31.7 ms: 1.08x slower                                                          |
| gc_traversal                     | 2.95 ms                                                | 3.19 ms: 1.08x slower                                                          |
| logging_silent                   | 72.5 ns                                                | 78.7 ns: 1.08x slower                                                          |
| html5lib                         | 33.4 ms                                                | 36.4 ms: 1.09x slower                                                          |
| sympy_str                        | 144 ms                                                 | 157 ms: 1.09x slower                                                           |
| deltablue                        | 2.57 ms                                                | 2.81 ms: 1.10x slower                                                          |
| chaos                            | 41.6 ms                                                | 45.7 ms: 1.10x slower                                                          |
| pycparser                        | 673 ms                                                 | 743 ms: 1.10x slower                                                           |
| meteor_contest                   | 69.1 ms                                                | 77.2 ms: 1.12x slower                                                          |
| async_tree_eager                 | 65.8 ms                                                | 73.7 ms: 1.12x slower                                                          |
| xml_etree_generate               | 55.4 ms                                                | 62.1 ms: 1.12x slower                                                          |
| 2to3                             | 168 ms                                                 | 191 ms: 1.13x slower                                                           |
| sympy_expand                     | 233 ms                                                 | 266 ms: 1.14x slower                                                           |
| pyflate                          | 311 ms                                                 | 357 ms: 1.15x slower                                                           |
| json_dumps                       | 6.19 ms                                                | 7.12 ms: 1.15x slower                                                          |
| typing_runtime_protocols         | 91.5 us                                                | 105 us: 1.15x slower                                                           |
| pprint_pformat                   | 986 ms                                                 | 1.14 sec: 1.16x slower                                                         |
| pprint_safe_repr                 | 483 ms                                                 | 561 ms: 1.16x slower                                                           |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 403 ms: 1.16x slower                                                           |
| xml_etree_process                | 38.9 ms                                                | 45.3 ms: 1.17x slower                                                          |
| create_gc_cycles                 | 1.15 ms                                                | 1.35 ms: 1.17x slower                                                          |
| hexiom                           | 4.38 ms                                                | 5.14 ms: 1.17x slower                                                          |
| scimark_lu                       | 73.5 ms                                                | 86.5 ms: 1.18x slower                                                          |
| crypto_pyaes                     | 51.4 ms                                                | 60.9 ms: 1.18x slower                                                          |
| scimark_monte_carlo              | 44.5 ms                                                | 53.0 ms: 1.19x slower                                                          |
| richards_super                   | 34.6 ms                                                | 42.0 ms: 1.21x slower                                                          |
| unpickle_pure_python             | 145 us                                                 | 177 us: 1.22x slower                                                           |
| richards                         | 30.6 ms                                                | 37.3 ms: 1.22x slower                                                          |
| many_optionals                   | 403 us                                                 | 493 us: 1.22x slower                                                           |
| pickle_pure_python               | 197 us                                                 | 241 us: 1.22x slower                                                           |
| genshi_xml                       | 30.5 ms                                                | 37.5 ms: 1.23x slower                                                          |
| mako                             | 7.44 ms                                                | 9.21 ms: 1.24x slower                                                          |
| nqueens                          | 59.5 ms                                                | 74.3 ms: 1.25x slower                                                          |
| nbody                            | 67.6 ms                                                | 85.4 ms: 1.26x slower                                                          |
| django_template                  | 19.7 ms                                                | 25.0 ms: 1.27x slower                                                          |
| genshi_text                      | 14.7 ms                                                | 18.8 ms: 1.28x slower                                                          |
| fannkuch                         | 250 ms                                                 | 321 ms: 1.28x slower                                                           |
| telco                            | 3.92 ms                                                | 5.04 ms: 1.28x slower                                                          |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 183 ms: 1.29x slower                                                           |
| coverage                         | 38.5 ms                                                | 53.2 ms: 1.38x slower                                                          |
| async_tree_eager_tg              | 46.9 ms                                                | 144 ms: 3.06x slower                                                           |
| Geometric mean                   | (ref)                                                  | 1.02x slower                                                                   |

Benchmark hidden because not significant (5): shortest_path, json, asyncio_websockets, pathlib, sphinx
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250627-3.15.0a0-2ab3a06/bm-20250627-darwin-arm64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.023x slower

# HPT report

- Reliability score: 99.48% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.12x