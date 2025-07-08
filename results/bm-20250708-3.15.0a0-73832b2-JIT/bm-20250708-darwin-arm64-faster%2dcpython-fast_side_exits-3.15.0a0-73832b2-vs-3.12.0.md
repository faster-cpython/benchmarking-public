# Results vs. 3.12.0

- fork: faster-cpython
- ref: fast_side_exits
- machine: darwin-arm64
- commit hash: 73832b2
- commit date: 2025-07-08
- overall geometric mean: 1.061x faster
- HPT reliability: 96.11%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-darwin-arm64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 171 ms: 1.02x slower                                                       |
| html5lib       | 33.4 ms                                                | 31.6 ms: 1.05x faster                                                      |
| sphinx         | 613 ms                                                 | 583 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                  | 1.02x faster                                                               |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-darwin-arm64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 361 ms: 1.84x faster                                                       |
| async_tree_io                    | 672 ms                                                 | 372 ms: 1.80x faster                                                       |
| async_tree_io_tg                 | 673 ms                                                 | 378 ms: 1.78x faster                                                       |
| async_tree_eager_io_tg           | 617 ms                                                 | 372 ms: 1.66x faster                                                       |
| async_tree_memoization_tg        | 318 ms                                                 | 192 ms: 1.66x faster                                                       |
| async_tree_none_tg               | 255 ms                                                 | 156 ms: 1.64x faster                                                       |
| async_tree_none                  | 263 ms                                                 | 162 ms: 1.62x faster                                                       |
| async_tree_memoization           | 310 ms                                                 | 193 ms: 1.61x faster                                                       |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 411 ms: 1.29x faster                                                       |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 414 ms: 1.27x faster                                                       |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.20x faster                                                       |
| coroutines                       | 19.7 ms                                                | 17.1 ms: 1.15x faster                                                      |
| async_generators                 | 299 ms                                                 | 283 ms: 1.06x faster                                                       |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 358 ms: 1.04x faster                                                       |
| async_tree_eager                 | 65.8 ms                                                | 63.6 ms: 1.03x faster                                                      |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 390 ms: 1.12x slower                                                       |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 168 ms: 1.19x slower                                                       |
| async_tree_eager_tg              | 46.9 ms                                                | 129 ms: 2.74x slower                                                       |
| Geometric mean                   | (ref)                                                  | 1.23x faster                                                               |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-darwin-arm64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 49.8 ms: 1.09x faster                                                      |
| pidigits       | 283 ms                                                 | 284 ms: 1.00x slower                                                       |
| nbody          | 67.6 ms                                                | 75.6 ms: 1.12x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-darwin-arm64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 71.3 ms: 1.07x faster                                                      |
| regex_effbot   | 2.44 ms                                                | 2.34 ms: 1.04x faster                                                      |
| regex_dna      | 143 ms                                                 | 138 ms: 1.03x faster                                                       |
| regex_v8       | 15.1 ms                                                | 15.6 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-darwin-arm64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                               | 1.24 sec: 1.10x faster                                                     |
| xml_etree_generate   | 55.4 ms                                                | 50.8 ms: 1.09x faster                                                      |
| xml_etree_process    | 38.9 ms                                                | 35.7 ms: 1.09x faster                                                      |
| unpickle_pure_python | 145 us                                                 | 135 us: 1.08x faster                                                       |
| xml_etree_parse      | 108 ms                                                 | 102 ms: 1.06x faster                                                       |
| xml_etree_iterparse  | 75.5 ms                                                | 72.3 ms: 1.04x faster                                                      |
| json_loads           | 17.0 us                                                | 16.4 us: 1.04x faster                                                      |
| json_dumps           | 6.19 ms                                                | 6.55 ms: 1.06x slower                                                      |
| pickle_pure_python   | 197 us                                                 | 210 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-darwin-arm64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 18.9 ms: 1.06x slower                                                      |
| python_startup_no_site | 13.2 ms                                                | 14.4 ms: 1.09x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-darwin-arm64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.44 ms                                                | 6.92 ms: 1.08x faster                                                      |
| genshi_text     | 14.7 ms                                                | 14.9 ms: 1.01x slower                                                      |
| genshi_xml      | 30.5 ms                                                | 31.3 ms: 1.03x slower                                                      |
| django_template | 19.7 ms                                                | 21.9 ms: 1.11x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                               |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-darwin-arm64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 13.7 ms: 2.34x faster                                                      |
| mdp                              | 1.49 sec                                               | 756 ms: 1.97x faster                                                       |
| async_tree_eager_io              | 666 ms                                                 | 361 ms: 1.84x faster                                                       |
| async_tree_io                    | 672 ms                                                 | 372 ms: 1.80x faster                                                       |
| async_tree_io_tg                 | 673 ms                                                 | 378 ms: 1.78x faster                                                       |
| async_tree_eager_io_tg           | 617 ms                                                 | 372 ms: 1.66x faster                                                       |
| async_tree_memoization_tg        | 318 ms                                                 | 192 ms: 1.66x faster                                                       |
| async_tree_none_tg               | 255 ms                                                 | 156 ms: 1.64x faster                                                       |
| async_tree_none                  | 263 ms                                                 | 162 ms: 1.62x faster                                                       |
| async_tree_memoization           | 310 ms                                                 | 193 ms: 1.61x faster                                                       |
| deepcopy                         | 226 us                                                 | 156 us: 1.45x faster                                                       |
| deepcopy_memo                    | 26.0 us                                                | 19.6 us: 1.33x faster                                                      |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 411 ms: 1.29x faster                                                       |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 414 ms: 1.27x faster                                                       |
| generators                       | 29.4 ms                                                | 24.2 ms: 1.22x faster                                                      |
| deepcopy_reduce                  | 2.01 us                                                | 1.68 us: 1.20x faster                                                      |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.20x faster                                                       |
| dulwich_log                      | 29.2 ms                                                | 25.2 ms: 1.16x faster                                                      |
| coroutines                       | 19.7 ms                                                | 17.1 ms: 1.15x faster                                                      |
| spectral_norm                    | 76.5 ms                                                | 66.8 ms: 1.14x faster                                                      |
| raytrace                         | 204 ms                                                 | 179 ms: 1.14x faster                                                       |
| k_core                           | 1.72 sec                                               | 1.52 sec: 1.13x faster                                                     |
| comprehensions                   | 14.0 us                                                | 12.4 us: 1.13x faster                                                      |
| go                               | 98.5 ms                                                | 87.3 ms: 1.13x faster                                                      |
| pylint                           | 182 ms                                                 | 163 ms: 1.11x faster                                                       |
| tomli_loads                      | 1.36 sec                                               | 1.24 sec: 1.10x faster                                                     |
| xml_etree_generate               | 55.4 ms                                                | 50.8 ms: 1.09x faster                                                      |
| xml_etree_process                | 38.9 ms                                                | 35.7 ms: 1.09x faster                                                      |
| float                            | 54.1 ms                                                | 49.8 ms: 1.09x faster                                                      |
| unpickle_pure_python             | 145 us                                                 | 135 us: 1.08x faster                                                       |
| pyflate                          | 311 ms                                                 | 288 ms: 1.08x faster                                                       |
| mako                             | 7.44 ms                                                | 6.92 ms: 1.08x faster                                                      |
| bpe_tokeniser                    | 3.28 sec                                               | 3.07 sec: 1.07x faster                                                     |
| regex_compile                    | 75.9 ms                                                | 71.3 ms: 1.07x faster                                                      |
| thrift                           | 468 us                                                 | 441 us: 1.06x faster                                                       |
| chaos                            | 41.6 ms                                                | 39.3 ms: 1.06x faster                                                      |
| xml_etree_parse                  | 108 ms                                                 | 102 ms: 1.06x faster                                                       |
| async_generators                 | 299 ms                                                 | 283 ms: 1.06x faster                                                       |
| html5lib                         | 33.4 ms                                                | 31.6 ms: 1.05x faster                                                      |
| sphinx                           | 613 ms                                                 | 583 ms: 1.05x faster                                                       |
| logging_format                   | 3.90 us                                                | 3.71 us: 1.05x faster                                                      |
| logging_simple                   | 3.60 us                                                | 3.44 us: 1.05x faster                                                      |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 358 ms: 1.04x faster                                                       |
| xml_etree_iterparse              | 75.5 ms                                                | 72.3 ms: 1.04x faster                                                      |
| regex_effbot                     | 2.44 ms                                                | 2.34 ms: 1.04x faster                                                      |
| pathlib                          | 24.7 ms                                                | 23.8 ms: 1.04x faster                                                      |
| json                             | 3.00 ms                                                | 2.89 ms: 1.04x faster                                                      |
| json_loads                       | 17.0 us                                                | 16.4 us: 1.04x faster                                                      |
| async_tree_eager                 | 65.8 ms                                                | 63.6 ms: 1.03x faster                                                      |
| regex_dna                        | 143 ms                                                 | 138 ms: 1.03x faster                                                       |
| dask                             | 779 ms                                                 | 769 ms: 1.01x faster                                                       |
| sympy_sum                        | 76.2 ms                                                | 75.7 ms: 1.01x faster                                                      |
| logging_silent                   | 72.5 ns                                                | 72.2 ns: 1.00x faster                                                      |
| pidigits                         | 283 ms                                                 | 284 ms: 1.00x slower                                                       |
| sympy_integrate                  | 11.1 ms                                                | 11.1 ms: 1.01x slower                                                      |
| genshi_text                      | 14.7 ms                                                | 14.9 ms: 1.01x slower                                                      |
| 2to3                             | 168 ms                                                 | 171 ms: 1.02x slower                                                       |
| shortest_path                    | 331 ms                                                 | 337 ms: 1.02x slower                                                       |
| scimark_fft                      | 194 ms                                                 | 198 ms: 1.02x slower                                                       |
| sqlite_synth                     | 1.55 us                                                | 1.58 us: 1.02x slower                                                      |
| deltablue                        | 2.57 ms                                                | 2.62 ms: 1.02x slower                                                      |
| genshi_xml                       | 30.5 ms                                                | 31.3 ms: 1.03x slower                                                      |
| pycparser                        | 673 ms                                                 | 692 ms: 1.03x slower                                                       |
| scimark_monte_carlo              | 44.5 ms                                                | 45.9 ms: 1.03x slower                                                      |
| nqueens                          | 59.5 ms                                                | 61.5 ms: 1.03x slower                                                      |
| scimark_sor                      | 85.8 ms                                                | 88.7 ms: 1.03x slower                                                      |
| connected_components             | 300 ms                                                 | 310 ms: 1.03x slower                                                       |
| regex_v8                         | 15.1 ms                                                | 15.6 ms: 1.04x slower                                                      |
| sympy_expand                     | 233 ms                                                 | 244 ms: 1.05x slower                                                       |
| json_dumps                       | 6.19 ms                                                | 6.55 ms: 1.06x slower                                                      |
| python_startup                   | 17.8 ms                                                | 18.9 ms: 1.06x slower                                                      |
| pickle_pure_python               | 197 us                                                 | 210 us: 1.06x slower                                                       |
| crypto_pyaes                     | 51.4 ms                                                | 55.6 ms: 1.08x slower                                                      |
| typing_runtime_protocols         | 91.5 us                                                | 98.9 us: 1.08x slower                                                      |
| gc_traversal                     | 2.95 ms                                                | 3.19 ms: 1.08x slower                                                      |
| python_startup_no_site           | 13.2 ms                                                | 14.4 ms: 1.09x slower                                                      |
| hexiom                           | 4.38 ms                                                | 4.77 ms: 1.09x slower                                                      |
| pprint_pformat                   | 986 ms                                                 | 1.08 sec: 1.09x slower                                                     |
| pprint_safe_repr                 | 483 ms                                                 | 532 ms: 1.10x slower                                                       |
| django_template                  | 19.7 ms                                                | 21.9 ms: 1.11x slower                                                      |
| scimark_lu                       | 73.5 ms                                                | 82.2 ms: 1.12x slower                                                      |
| nbody                            | 67.6 ms                                                | 75.6 ms: 1.12x slower                                                      |
| meteor_contest                   | 69.1 ms                                                | 77.5 ms: 1.12x slower                                                      |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 390 ms: 1.12x slower                                                       |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.55 ms: 1.13x slower                                                      |
| richards_super                   | 34.6 ms                                                | 39.3 ms: 1.13x slower                                                      |
| richards                         | 30.6 ms                                                | 35.2 ms: 1.15x slower                                                      |
| fannkuch                         | 250 ms                                                 | 292 ms: 1.17x slower                                                       |
| telco                            | 3.92 ms                                                | 4.60 ms: 1.17x slower                                                      |
| many_optionals                   | 403 us                                                 | 475 us: 1.18x slower                                                       |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 168 ms: 1.19x slower                                                       |
| create_gc_cycles                 | 1.15 ms                                                | 1.37 ms: 1.19x slower                                                      |
| coverage                         | 38.5 ms                                                | 48.5 ms: 1.26x slower                                                      |
| async_tree_eager_tg              | 46.9 ms                                                | 129 ms: 2.74x slower                                                       |
| Geometric mean                   | (ref)                                                  | 1.06x faster                                                               |

Benchmark hidden because not significant (3): asyncio_websockets, sympy_str, docutils
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250708-3.15.0a0-73832b2-JIT/bm-20250708-darwin-arm64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.061x faster

# HPT report

- Reliability score: 96.11% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.14x