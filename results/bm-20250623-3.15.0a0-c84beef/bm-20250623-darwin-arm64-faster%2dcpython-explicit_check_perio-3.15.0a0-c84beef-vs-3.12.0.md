# Results vs. 3.12.0

- fork: faster-cpython
- ref: explicit_check_perio
- machine: darwin-arm64
- commit hash: c84beef
- commit date: 2025-06-23
- overall geometric mean: 1.016x slower
- HPT reliability: 95.26%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 187 ms: 1.11x slower                                                            |
| docutils       | 1.45 sec                                               | 1.52 sec: 1.04x slower                                                          |
| html5lib       | 33.4 ms                                                | 34.2 ms: 1.03x slower                                                           |
| sphinx         | 613 ms                                                 | 618 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                  | 1.05x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 393 ms: 1.69x faster                                                            |
| async_tree_io_tg                 | 673 ms                                                 | 408 ms: 1.65x faster                                                            |
| async_tree_io                    | 672 ms                                                 | 414 ms: 1.62x faster                                                            |
| async_tree_eager_io_tg           | 617 ms                                                 | 403 ms: 1.53x faster                                                            |
| async_tree_memoization_tg        | 318 ms                                                 | 208 ms: 1.53x faster                                                            |
| async_tree_none_tg               | 255 ms                                                 | 172 ms: 1.49x faster                                                            |
| async_tree_memoization           | 310 ms                                                 | 215 ms: 1.44x faster                                                            |
| async_tree_none                  | 263 ms                                                 | 183 ms: 1.44x faster                                                            |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 422 ms: 1.25x faster                                                            |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 433 ms: 1.22x faster                                                            |
| async_tree_eager_memoization     | 168 ms                                                 | 151 ms: 1.11x faster                                                            |
| async_generators                 | 299 ms                                                 | 276 ms: 1.08x faster                                                            |
| coroutines                       | 19.7 ms                                                | 18.7 ms: 1.05x faster                                                           |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 368 ms: 1.02x faster                                                            |
| async_tree_eager                 | 65.8 ms                                                | 73.1 ms: 1.11x slower                                                           |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 399 ms: 1.15x slower                                                            |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 182 ms: 1.28x slower                                                            |
| async_tree_eager_tg              | 46.9 ms                                                | 143 ms: 3.05x slower                                                            |
| Geometric mean                   | (ref)                                                  | 1.14x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 283 ms                                                 | 284 ms: 1.00x slower                                                            |
| float          | 54.1 ms                                                | 57.7 ms: 1.07x slower                                                           |
| nbody          | 67.6 ms                                                | 85.1 ms: 1.26x slower                                                           |
| Geometric mean | (ref)                                                  | 1.10x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.35 ms: 1.04x faster                                                           |
| regex_dna      | 143 ms                                                 | 144 ms: 1.01x slower                                                            |
| regex_compile  | 75.9 ms                                                | 81.5 ms: 1.07x slower                                                           |
| regex_v8       | 15.1 ms                                                | 16.3 ms: 1.08x slower                                                           |
| Geometric mean | (ref)                                                  | 1.03x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 104 ms: 1.03x faster                                                            |
| json_loads           | 17.0 us                                                | 16.5 us: 1.03x faster                                                           |
| xml_etree_iterparse  | 75.5 ms                                                | 74.1 ms: 1.02x faster                                                           |
| xml_etree_generate   | 55.4 ms                                                | 59.1 ms: 1.07x slower                                                           |
| tomli_loads          | 1.36 sec                                               | 1.46 sec: 1.08x slower                                                          |
| json_dumps           | 6.19 ms                                                | 6.81 ms: 1.10x slower                                                           |
| xml_etree_process    | 38.9 ms                                                | 43.5 ms: 1.12x slower                                                           |
| pickle_pure_python   | 197 us                                                 | 243 us: 1.23x slower                                                            |
| unpickle_pure_python | 145 us                                                 | 180 us: 1.24x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.08x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 13.2 ms                                                | 13.3 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 30.5 ms                                                | 36.3 ms: 1.19x slower                                                           |
| genshi_text     | 14.7 ms                                                | 17.8 ms: 1.21x slower                                                           |
| mako            | 7.44 ms                                                | 9.21 ms: 1.24x slower                                                           |
| django_template | 19.7 ms                                                | 25.5 ms: 1.29x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.23x slower                                                                    |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 14.9 ms: 2.16x faster                                                           |
| mdp                              | 1.49 sec                                               | 830 ms: 1.80x faster                                                            |
| async_tree_eager_io              | 666 ms                                                 | 393 ms: 1.69x faster                                                            |
| async_tree_io_tg                 | 673 ms                                                 | 408 ms: 1.65x faster                                                            |
| async_tree_io                    | 672 ms                                                 | 414 ms: 1.62x faster                                                            |
| async_tree_eager_io_tg           | 617 ms                                                 | 403 ms: 1.53x faster                                                            |
| async_tree_memoization_tg        | 318 ms                                                 | 208 ms: 1.53x faster                                                            |
| async_tree_none_tg               | 255 ms                                                 | 172 ms: 1.49x faster                                                            |
| async_tree_memoization           | 310 ms                                                 | 215 ms: 1.44x faster                                                            |
| async_tree_none                  | 263 ms                                                 | 183 ms: 1.44x faster                                                            |
| deepcopy                         | 226 us                                                 | 176 us: 1.29x faster                                                            |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 422 ms: 1.25x faster                                                            |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 433 ms: 1.22x faster                                                            |
| deepcopy_memo                    | 26.0 us                                                | 22.0 us: 1.18x faster                                                           |
| k_core                           | 1.72 sec                                               | 1.47 sec: 1.17x faster                                                          |
| async_tree_eager_memoization     | 168 ms                                                 | 151 ms: 1.11x faster                                                            |
| dulwich_log                      | 29.2 ms                                                | 26.5 ms: 1.10x faster                                                           |
| async_generators                 | 299 ms                                                 | 276 ms: 1.08x faster                                                            |
| pathlib                          | 24.7 ms                                                | 23.0 ms: 1.07x faster                                                           |
| pylint                           | 182 ms                                                 | 169 ms: 1.07x faster                                                            |
| spectral_norm                    | 76.5 ms                                                | 71.7 ms: 1.07x faster                                                           |
| comprehensions                   | 14.0 us                                                | 13.2 us: 1.06x faster                                                           |
| deepcopy_reduce                  | 2.01 us                                                | 1.91 us: 1.05x faster                                                           |
| coroutines                       | 19.7 ms                                                | 18.7 ms: 1.05x faster                                                           |
| regex_effbot                     | 2.44 ms                                                | 2.35 ms: 1.04x faster                                                           |
| xml_etree_parse                  | 108 ms                                                 | 104 ms: 1.03x faster                                                            |
| json_loads                       | 17.0 us                                                | 16.5 us: 1.03x faster                                                           |
| xml_etree_iterparse              | 75.5 ms                                                | 74.1 ms: 1.02x faster                                                           |
| json                             | 3.00 ms                                                | 2.95 ms: 1.02x faster                                                           |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 368 ms: 1.02x faster                                                            |
| dask                             | 779 ms                                                 | 769 ms: 1.01x faster                                                            |
| shortest_path                    | 331 ms                                                 | 328 ms: 1.01x faster                                                            |
| bpe_tokeniser                    | 3.28 sec                                               | 3.26 sec: 1.01x faster                                                          |
| pidigits                         | 283 ms                                                 | 284 ms: 1.00x slower                                                            |
| python_startup_no_site           | 13.2 ms                                                | 13.3 ms: 1.01x slower                                                           |
| go                               | 98.5 ms                                                | 99.2 ms: 1.01x slower                                                           |
| regex_dna                        | 143 ms                                                 | 144 ms: 1.01x slower                                                            |
| sphinx                           | 613 ms                                                 | 618 ms: 1.01x slower                                                            |
| thrift                           | 468 us                                                 | 473 us: 1.01x slower                                                            |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.18 ms: 1.01x slower                                                           |
| html5lib                         | 33.4 ms                                                | 34.2 ms: 1.03x slower                                                           |
| sympy_integrate                  | 11.1 ms                                                | 11.4 ms: 1.03x slower                                                           |
| scimark_fft                      | 194 ms                                                 | 201 ms: 1.03x slower                                                            |
| raytrace                         | 204 ms                                                 | 212 ms: 1.04x slower                                                            |
| docutils                         | 1.45 sec                                               | 1.52 sec: 1.04x slower                                                          |
| scimark_sor                      | 85.8 ms                                                | 89.7 ms: 1.05x slower                                                           |
| sqlite_synth                     | 1.55 us                                                | 1.62 us: 1.05x slower                                                           |
| xml_etree_generate               | 55.4 ms                                                | 59.1 ms: 1.07x slower                                                           |
| float                            | 54.1 ms                                                | 57.7 ms: 1.07x slower                                                           |
| sympy_sum                        | 76.2 ms                                                | 81.4 ms: 1.07x slower                                                           |
| regex_compile                    | 75.9 ms                                                | 81.5 ms: 1.07x slower                                                           |
| meteor_contest                   | 69.1 ms                                                | 74.2 ms: 1.07x slower                                                           |
| tomli_loads                      | 1.36 sec                                               | 1.46 sec: 1.08x slower                                                          |
| generators                       | 29.4 ms                                                | 31.6 ms: 1.08x slower                                                           |
| sympy_str                        | 144 ms                                                 | 155 ms: 1.08x slower                                                            |
| pyflate                          | 311 ms                                                 | 336 ms: 1.08x slower                                                            |
| regex_v8                         | 15.1 ms                                                | 16.3 ms: 1.08x slower                                                           |
| gc_traversal                     | 2.95 ms                                                | 3.19 ms: 1.08x slower                                                           |
| deltablue                        | 2.57 ms                                                | 2.81 ms: 1.10x slower                                                           |
| json_dumps                       | 6.19 ms                                                | 6.81 ms: 1.10x slower                                                           |
| 2to3                             | 168 ms                                                 | 187 ms: 1.11x slower                                                            |
| pycparser                        | 673 ms                                                 | 748 ms: 1.11x slower                                                            |
| async_tree_eager                 | 65.8 ms                                                | 73.1 ms: 1.11x slower                                                           |
| xml_etree_process                | 38.9 ms                                                | 43.5 ms: 1.12x slower                                                           |
| logging_format                   | 3.90 us                                                | 4.38 us: 1.12x slower                                                           |
| sympy_expand                     | 233 ms                                                 | 263 ms: 1.13x slower                                                            |
| chaos                            | 41.6 ms                                                | 47.2 ms: 1.13x slower                                                           |
| logging_simple                   | 3.60 us                                                | 4.10 us: 1.14x slower                                                           |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 399 ms: 1.15x slower                                                            |
| scimark_lu                       | 73.5 ms                                                | 85.4 ms: 1.16x slower                                                           |
| hexiom                           | 4.38 ms                                                | 5.10 ms: 1.17x slower                                                           |
| create_gc_cycles                 | 1.15 ms                                                | 1.36 ms: 1.18x slower                                                           |
| crypto_pyaes                     | 51.4 ms                                                | 60.9 ms: 1.18x slower                                                           |
| scimark_monte_carlo              | 44.5 ms                                                | 52.7 ms: 1.18x slower                                                           |
| genshi_xml                       | 30.5 ms                                                | 36.3 ms: 1.19x slower                                                           |
| nqueens                          | 59.5 ms                                                | 70.9 ms: 1.19x slower                                                           |
| richards_super                   | 34.6 ms                                                | 41.5 ms: 1.20x slower                                                           |
| typing_runtime_protocols         | 91.5 us                                                | 110 us: 1.20x slower                                                            |
| telco                            | 3.92 ms                                                | 4.74 ms: 1.21x slower                                                           |
| genshi_text                      | 14.7 ms                                                | 17.8 ms: 1.21x slower                                                           |
| fannkuch                         | 250 ms                                                 | 305 ms: 1.22x slower                                                            |
| richards                         | 30.6 ms                                                | 37.6 ms: 1.23x slower                                                           |
| pickle_pure_python               | 197 us                                                 | 243 us: 1.23x slower                                                            |
| unpickle_pure_python             | 145 us                                                 | 180 us: 1.24x slower                                                            |
| mako                             | 7.44 ms                                                | 9.21 ms: 1.24x slower                                                           |
| many_optionals                   | 403 us                                                 | 502 us: 1.25x slower                                                            |
| nbody                            | 67.6 ms                                                | 85.1 ms: 1.26x slower                                                           |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 182 ms: 1.28x slower                                                            |
| coverage                         | 38.5 ms                                                | 49.6 ms: 1.29x slower                                                           |
| pprint_pformat                   | 986 ms                                                 | 1.27 sec: 1.29x slower                                                          |
| django_template                  | 19.7 ms                                                | 25.5 ms: 1.29x slower                                                           |
| pprint_safe_repr                 | 483 ms                                                 | 627 ms: 1.30x slower                                                            |
| async_tree_eager_tg              | 46.9 ms                                                | 143 ms: 3.05x slower                                                            |
| logging_silent                   | 72.5 ns                                                | 345 ns: 4.76x slower                                                            |
| Geometric mean                   | (ref)                                                  | 1.03x slower                                                                    |

Benchmark hidden because not significant (3): asyncio_websockets, connected_components, python_startup
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250623-3.15.0a0-c84beef/bm-20250623-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.016x slower

# HPT report

- Reliability score: 95.26% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.12x