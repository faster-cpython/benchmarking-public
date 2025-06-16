# Results vs. 3.12.0

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: darwin-arm64
- commit hash: c41d531
- commit date: 2025-06-16
- overall geometric mean: 1.011x slower
- HPT reliability: 92.08%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250616-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 170 ms: 1.01x slower                                                            |
| html5lib       | 33.4 ms                                                | 31.7 ms: 1.05x faster                                                           |
| sphinx         | 613 ms                                                 | 580 ms: 1.06x faster                                                            |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                    |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250616-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 363 ms: 1.83x faster                                                            |
| async_tree_io_tg                 | 673 ms                                                 | 367 ms: 1.83x faster                                                            |
| async_tree_io                    | 672 ms                                                 | 379 ms: 1.77x faster                                                            |
| async_tree_memoization_tg        | 318 ms                                                 | 192 ms: 1.66x faster                                                            |
| async_tree_eager_io_tg           | 617 ms                                                 | 373 ms: 1.65x faster                                                            |
| async_tree_none_tg               | 255 ms                                                 | 156 ms: 1.63x faster                                                            |
| async_tree_none                  | 263 ms                                                 | 163 ms: 1.61x faster                                                            |
| async_tree_memoization           | 310 ms                                                 | 195 ms: 1.59x faster                                                            |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 410 ms: 1.29x faster                                                            |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 414 ms: 1.27x faster                                                            |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.20x faster                                                            |
| coroutines                       | 19.7 ms                                                | 16.9 ms: 1.16x faster                                                           |
| async_generators                 | 299 ms                                                 | 261 ms: 1.14x faster                                                            |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 357 ms: 1.05x faster                                                            |
| async_tree_eager                 | 65.8 ms                                                | 63.6 ms: 1.03x faster                                                           |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 388 ms: 1.12x slower                                                            |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 168 ms: 1.18x slower                                                            |
| async_tree_eager_tg              | 46.9 ms                                                | 129 ms: 2.75x slower                                                            |
| Geometric mean                   | (ref)                                                  | 1.23x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250616-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 49.9 ms: 1.08x faster                                                           |
| nbody          | 67.6 ms                                                | 74.2 ms: 1.10x slower                                                           |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250616-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 71.8 ms: 1.06x faster                                                           |
| regex_effbot   | 2.44 ms                                                | 2.37 ms: 1.03x faster                                                           |
| regex_dna      | 143 ms                                                 | 143 ms: 1.00x slower                                                            |
| regex_v8       | 15.1 ms                                                | 16.2 ms: 1.08x slower                                                           |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250616-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 100 ms: 1.08x faster                                                            |
| xml_etree_generate   | 55.4 ms                                                | 53.3 ms: 1.04x faster                                                           |
| json_loads           | 17.0 us                                                | 16.4 us: 1.04x faster                                                           |
| xml_etree_iterparse  | 75.5 ms                                                | 72.7 ms: 1.04x faster                                                           |
| xml_etree_process    | 38.9 ms                                                | 38.6 ms: 1.01x faster                                                           |
| json_dumps           | 6.19 ms                                                | 6.61 ms: 1.07x slower                                                           |
| unpickle_pure_python | 145 us                                                 | 158 us: 1.09x slower                                                            |
| pickle_pure_python   | 197 us                                                 | 217 us: 1.10x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250616-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 13.2 ms                                                | 13.3 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250616-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 14.7 ms                                                | 14.6 ms: 1.01x faster                                                           |
| genshi_xml      | 30.5 ms                                                | 30.9 ms: 1.01x slower                                                           |
| mako            | 7.44 ms                                                | 7.74 ms: 1.04x slower                                                           |
| django_template | 19.7 ms                                                | 21.9 ms: 1.11x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                                    |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250616-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 13.6 ms: 2.37x faster                                                           |
| mdp                              | 1.49 sec                                               | 759 ms: 1.97x faster                                                            |
| async_tree_eager_io              | 666 ms                                                 | 363 ms: 1.83x faster                                                            |
| async_tree_io_tg                 | 673 ms                                                 | 367 ms: 1.83x faster                                                            |
| async_tree_io                    | 672 ms                                                 | 379 ms: 1.77x faster                                                            |
| async_tree_memoization_tg        | 318 ms                                                 | 192 ms: 1.66x faster                                                            |
| async_tree_eager_io_tg           | 617 ms                                                 | 373 ms: 1.65x faster                                                            |
| async_tree_none_tg               | 255 ms                                                 | 156 ms: 1.63x faster                                                            |
| async_tree_none                  | 263 ms                                                 | 163 ms: 1.61x faster                                                            |
| async_tree_memoization           | 310 ms                                                 | 195 ms: 1.59x faster                                                            |
| deepcopy                         | 226 us                                                 | 157 us: 1.44x faster                                                            |
| deepcopy_memo                    | 26.0 us                                                | 19.4 us: 1.34x faster                                                           |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 410 ms: 1.29x faster                                                            |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 414 ms: 1.27x faster                                                            |
| generators                       | 29.4 ms                                                | 24.1 ms: 1.22x faster                                                           |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.20x faster                                                            |
| deepcopy_reduce                  | 2.01 us                                                | 1.69 us: 1.19x faster                                                           |
| k_core                           | 1.72 sec                                               | 1.47 sec: 1.17x faster                                                          |
| dulwich_log                      | 29.2 ms                                                | 25.0 ms: 1.17x faster                                                           |
| coroutines                       | 19.7 ms                                                | 16.9 ms: 1.16x faster                                                           |
| async_generators                 | 299 ms                                                 | 261 ms: 1.14x faster                                                            |
| raytrace                         | 204 ms                                                 | 180 ms: 1.13x faster                                                            |
| pylint                           | 182 ms                                                 | 161 ms: 1.13x faster                                                            |
| comprehensions                   | 14.0 us                                                | 12.4 us: 1.13x faster                                                           |
| go                               | 98.5 ms                                                | 87.5 ms: 1.13x faster                                                           |
| pathlib                          | 24.7 ms                                                | 22.4 ms: 1.10x faster                                                           |
| float                            | 54.1 ms                                                | 49.9 ms: 1.08x faster                                                           |
| xml_etree_parse                  | 108 ms                                                 | 100 ms: 1.08x faster                                                            |
| spectral_norm                    | 76.5 ms                                                | 71.0 ms: 1.08x faster                                                           |
| bpe_tokeniser                    | 3.28 sec                                               | 3.06 sec: 1.07x faster                                                          |
| sphinx                           | 613 ms                                                 | 580 ms: 1.06x faster                                                            |
| regex_compile                    | 75.9 ms                                                | 71.8 ms: 1.06x faster                                                           |
| html5lib                         | 33.4 ms                                                | 31.7 ms: 1.05x faster                                                           |
| chaos                            | 41.6 ms                                                | 39.7 ms: 1.05x faster                                                           |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 357 ms: 1.05x faster                                                            |
| xml_etree_generate               | 55.4 ms                                                | 53.3 ms: 1.04x faster                                                           |
| json_loads                       | 17.0 us                                                | 16.4 us: 1.04x faster                                                           |
| xml_etree_iterparse              | 75.5 ms                                                | 72.7 ms: 1.04x faster                                                           |
| async_tree_eager                 | 65.8 ms                                                | 63.6 ms: 1.03x faster                                                           |
| regex_effbot                     | 2.44 ms                                                | 2.37 ms: 1.03x faster                                                           |
| json                             | 3.00 ms                                                | 2.92 ms: 1.03x faster                                                           |
| sympy_sum                        | 76.2 ms                                                | 74.8 ms: 1.02x faster                                                           |
| sympy_str                        | 144 ms                                                 | 142 ms: 1.01x faster                                                            |
| dask                             | 779 ms                                                 | 769 ms: 1.01x faster                                                            |
| sympy_integrate                  | 11.1 ms                                                | 11.0 ms: 1.01x faster                                                           |
| xml_etree_process                | 38.9 ms                                                | 38.6 ms: 1.01x faster                                                           |
| genshi_text                      | 14.7 ms                                                | 14.6 ms: 1.01x faster                                                           |
| regex_dna                        | 143 ms                                                 | 143 ms: 1.00x slower                                                            |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.16 ms: 1.01x slower                                                           |
| python_startup_no_site           | 13.2 ms                                                | 13.3 ms: 1.01x slower                                                           |
| 2to3                             | 168 ms                                                 | 170 ms: 1.01x slower                                                            |
| deltablue                        | 2.57 ms                                                | 2.59 ms: 1.01x slower                                                           |
| scimark_fft                      | 194 ms                                                 | 196 ms: 1.01x slower                                                            |
| genshi_xml                       | 30.5 ms                                                | 30.9 ms: 1.01x slower                                                           |
| logging_simple                   | 3.60 us                                                | 3.67 us: 1.02x slower                                                           |
| logging_format                   | 3.90 us                                                | 3.97 us: 1.02x slower                                                           |
| nqueens                          | 59.5 ms                                                | 60.7 ms: 1.02x slower                                                           |
| pyflate                          | 311 ms                                                 | 318 ms: 1.02x slower                                                            |
| sympy_expand                     | 233 ms                                                 | 239 ms: 1.03x slower                                                            |
| scimark_sor                      | 85.8 ms                                                | 88.6 ms: 1.03x slower                                                           |
| connected_components             | 300 ms                                                 | 311 ms: 1.04x slower                                                            |
| sqlite_synth                     | 1.55 us                                                | 1.60 us: 1.04x slower                                                           |
| mako                             | 7.44 ms                                                | 7.74 ms: 1.04x slower                                                           |
| scimark_monte_carlo              | 44.5 ms                                                | 46.4 ms: 1.04x slower                                                           |
| meteor_contest                   | 69.1 ms                                                | 72.8 ms: 1.05x slower                                                           |
| hexiom                           | 4.38 ms                                                | 4.66 ms: 1.06x slower                                                           |
| json_dumps                       | 6.19 ms                                                | 6.61 ms: 1.07x slower                                                           |
| regex_v8                         | 15.1 ms                                                | 16.2 ms: 1.08x slower                                                           |
| fannkuch                         | 250 ms                                                 | 270 ms: 1.08x slower                                                            |
| gc_traversal                     | 2.95 ms                                                | 3.18 ms: 1.08x slower                                                           |
| unpickle_pure_python             | 145 us                                                 | 158 us: 1.09x slower                                                            |
| typing_runtime_protocols         | 91.5 us                                                | 100 us: 1.10x slower                                                            |
| crypto_pyaes                     | 51.4 ms                                                | 56.5 ms: 1.10x slower                                                           |
| nbody                            | 67.6 ms                                                | 74.2 ms: 1.10x slower                                                           |
| pickle_pure_python               | 197 us                                                 | 217 us: 1.10x slower                                                            |
| django_template                  | 19.7 ms                                                | 21.9 ms: 1.11x slower                                                           |
| scimark_lu                       | 73.5 ms                                                | 82.0 ms: 1.12x slower                                                           |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 388 ms: 1.12x slower                                                            |
| pprint_pformat                   | 986 ms                                                 | 1.14 sec: 1.16x slower                                                          |
| telco                            | 3.92 ms                                                | 4.54 ms: 1.16x slower                                                           |
| many_optionals                   | 403 us                                                 | 467 us: 1.16x slower                                                            |
| pprint_safe_repr                 | 483 ms                                                 | 562 ms: 1.16x slower                                                            |
| create_gc_cycles                 | 1.15 ms                                                | 1.35 ms: 1.18x slower                                                           |
| richards_super                   | 34.6 ms                                                | 40.9 ms: 1.18x slower                                                           |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 168 ms: 1.18x slower                                                            |
| richards                         | 30.6 ms                                                | 36.5 ms: 1.19x slower                                                           |
| async_tree_eager_tg              | 46.9 ms                                                | 129 ms: 2.75x slower                                                            |
| logging_silent                   | 72.5 ns                                                | 323 ns: 4.45x slower                                                            |
| coverage                         | 38.5 ms                                                | 290 ms: 7.53x slower                                                            |
| thrift                           | 468 us                                                 | 43.6 ms: 93.27x slower                                                          |
| Geometric mean                   | (ref)                                                  | 1.03x slower                                                                    |

Benchmark hidden because not significant (7): asyncio_websockets, docutils, python_startup, pidigits, tomli_loads, shortest_path, pycparser
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250616-3.15.0a0-c41d531/bm-20250616-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.011x slower

# HPT report

- Reliability score: 92.08% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.12x