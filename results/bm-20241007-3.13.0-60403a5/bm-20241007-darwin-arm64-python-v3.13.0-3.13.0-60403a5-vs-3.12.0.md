# Results vs. 3.12.0

- fork: python
- ref: v3.13.0
- machine: darwin-arm64
- commit hash: 60403a5
- commit date: 2024-10-07
- overall geometric mean: 1.002x faster
- HPT reliability: 91.26%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 179 ms: 1.06x slower                                   |
| chameleon      | 4.55 ms                                                | 4.95 ms: 1.09x slower                                  |
| docutils       | 1.45 sec                                               | 1.44 sec: 1.01x faster                                 |
| html5lib       | 33.4 ms                                                | 36.7 ms: 1.10x slower                                  |
| sphinx         | 613 ms                                                 | 602 ms: 1.02x faster                                   |
| Geometric mean | (ref)                                                  | 1.02x slower                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|---------------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_io_tg                | 673 ms                                                 | 500 ms: 1.34x faster                                   |
| async_tree_io                   | 672 ms                                                 | 508 ms: 1.32x faster                                   |
| async_tree_eager_io             | 666 ms                                                 | 511 ms: 1.30x faster                                   |
| async_tree_eager_io_tg          | 617 ms                                                 | 479 ms: 1.29x faster                                   |
| async_tree_none_tg              | 255 ms                                                 | 198 ms: 1.29x faster                                   |
| async_tree_none                 | 263 ms                                                 | 212 ms: 1.24x faster                                   |
| async_tree_cpu_io_mixed_tg      | 528 ms                                                 | 448 ms: 1.18x faster                                   |
| async_tree_memoization          | 310 ms                                                 | 268 ms: 1.16x faster                                   |
| async_tree_cpu_io_mixed         | 527 ms                                                 | 459 ms: 1.15x faster                                   |
| async_tree_memoization_tg       | 318 ms                                                 | 288 ms: 1.11x faster                                   |
| async_tree_eager_memoization_tg | 142 ms                                                 | 138 ms: 1.03x faster                                   |
| async_generators                | 299 ms                                                 | 294 ms: 1.02x faster                                   |
| async_tree_eager_tg             | 46.9 ms                                                | 47.4 ms: 1.01x slower                                  |
| coroutines                      | 19.7 ms                                                | 20.0 ms: 1.02x slower                                  |
| async_tree_eager                | 65.8 ms                                                | 69.9 ms: 1.06x slower                                  |
| Geometric mean                  | (ref)                                                  | 1.12x faster                                           |

Benchmark hidden because not significant (4): async_tree_eager_cpu_io_mixed, asyncio_websockets, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pidigits       | 283 ms                                                 | 284 ms: 1.00x slower                                   |
| float          | 54.1 ms                                                | 55.8 ms: 1.03x slower                                  |
| nbody          | 67.6 ms                                                | 73.6 ms: 1.09x slower                                  |
| Geometric mean | (ref)                                                  | 1.04x slower                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 78.3 ms: 1.03x slower                                  |
| regex_dna      | 143 ms                                                 | 149 ms: 1.04x slower                                   |
| regex_effbot   | 2.44 ms                                                | 2.63 ms: 1.08x slower                                  |
| regex_v8       | 15.1 ms                                                | 17.0 ms: 1.13x slower                                  |
| Geometric mean | (ref)                                                  | 1.07x slower                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| xml_etree_iterparse  | 75.5 ms                                                | 74.2 ms: 1.02x faster                                  |
| xml_etree_generate   | 55.4 ms                                                | 57.1 ms: 1.03x slower                                  |
| json_dumps           | 6.19 ms                                                | 6.47 ms: 1.05x slower                                  |
| xml_etree_process    | 38.9 ms                                                | 41.3 ms: 1.06x slower                                  |
| pickle_pure_python   | 197 us                                                 | 215 us: 1.09x slower                                   |
| unpickle_pure_python | 145 us                                                 | 165 us: 1.14x slower                                   |
| tomli_loads          | 1.36 sec                                               | 1.57 sec: 1.15x slower                                 |
| Geometric mean       | (ref)                                                  | 1.05x slower                                           |

Benchmark hidden because not significant (2): xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 13.2 ms                                                | 13.7 ms: 1.04x slower                                  |
| python_startup         | 17.8 ms                                                | 18.8 ms: 1.06x slower                                  |
| Geometric mean         | (ref)                                                  | 1.05x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| django_template | 19.7 ms                                                | 20.5 ms: 1.04x slower                                  |
| mako            | 7.44 ms                                                | 7.75 ms: 1.04x slower                                  |
| genshi_xml      | 30.5 ms                                                | 34.1 ms: 1.12x slower                                  |
| genshi_text     | 14.7 ms                                                | 16.9 ms: 1.15x slower                                  |
| Geometric mean  | (ref)                                                  | 1.09x slower                                           |

All benchmarks:
===============

| Benchmark                       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|---------------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| subparsers                      | 32.1 ms                                                | 9.44 ms: 3.41x faster                                  |
| djangocms                       | 9.55 us                                                | 7.05 us: 1.35x faster                                  |
| async_tree_io_tg                | 673 ms                                                 | 500 ms: 1.34x faster                                   |
| async_tree_io                   | 672 ms                                                 | 508 ms: 1.32x faster                                   |
| async_tree_eager_io             | 666 ms                                                 | 511 ms: 1.30x faster                                   |
| async_tree_eager_io_tg          | 617 ms                                                 | 479 ms: 1.29x faster                                   |
| async_tree_none_tg              | 255 ms                                                 | 198 ms: 1.29x faster                                   |
| async_tree_none                 | 263 ms                                                 | 212 ms: 1.24x faster                                   |
| gunicorn                        | 1.71 ms                                                | 1.40 ms: 1.22x faster                                  |
| async_tree_cpu_io_mixed_tg      | 528 ms                                                 | 448 ms: 1.18x faster                                   |
| comprehensions                  | 14.0 us                                                | 12.0 us: 1.17x faster                                  |
| async_tree_memoization          | 310 ms                                                 | 268 ms: 1.16x faster                                   |
| async_tree_cpu_io_mixed         | 527 ms                                                 | 459 ms: 1.15x faster                                   |
| raytrace                        | 204 ms                                                 | 181 ms: 1.13x faster                                   |
| async_tree_memoization_tg       | 318 ms                                                 | 288 ms: 1.11x faster                                   |
| k_core                          | 1.72 sec                                               | 1.61 sec: 1.07x faster                                 |
| pathlib                         | 24.7 ms                                                | 23.2 ms: 1.06x faster                                  |
| gevent_hub                      | 0.72 ns                                                | 0.68 ns: 1.06x faster                                  |
| scimark_sparse_mat_mult         | 3.14 ms                                                | 2.98 ms: 1.05x faster                                  |
| sqlalchemy_declarative          | 61.9 ms                                                | 59.0 ms: 1.05x faster                                  |
| async_tree_eager_memoization_tg | 142 ms                                                 | 138 ms: 1.03x faster                                   |
| logging_silent                  | 72.5 ns                                                | 71.0 ns: 1.02x faster                                  |
| sphinx                          | 613 ms                                                 | 602 ms: 1.02x faster                                   |
| async_generators                | 299 ms                                                 | 294 ms: 1.02x faster                                   |
| xml_etree_iterparse             | 75.5 ms                                                | 74.2 ms: 1.02x faster                                  |
| dulwich_log                     | 29.2 ms                                                | 28.7 ms: 1.02x faster                                  |
| sympy_sum                       | 76.2 ms                                                | 75.1 ms: 1.02x faster                                  |
| chaos                           | 41.6 ms                                                | 41.1 ms: 1.01x faster                                  |
| logging_simple                  | 3.60 us                                                | 3.56 us: 1.01x faster                                  |
| logging_format                  | 3.90 us                                                | 3.85 us: 1.01x faster                                  |
| bench_mp_pool                   | 65.5 ms                                                | 64.7 ms: 1.01x faster                                  |
| dask                            | 779 ms                                                 | 771 ms: 1.01x faster                                   |
| bpe_tokeniser                   | 3.28 sec                                               | 3.26 sec: 1.01x faster                                 |
| docutils                        | 1.45 sec                                               | 1.44 sec: 1.01x faster                                 |
| gc_traversal                    | 2.95 ms                                                | 2.94 ms: 1.00x faster                                  |
| thrift                          | 468 us                                                 | 466 us: 1.00x faster                                   |
| pidigits                        | 283 ms                                                 | 284 ms: 1.00x slower                                   |
| mdp                             | 1.49 sec                                               | 1.50 sec: 1.00x slower                                 |
| sqlite_synth                    | 1.55 us                                                | 1.55 us: 1.01x slower                                  |
| async_tree_eager_tg             | 46.9 ms                                                | 47.4 ms: 1.01x slower                                  |
| sympy_str                       | 144 ms                                                 | 146 ms: 1.01x slower                                   |
| json                            | 3.00 ms                                                | 3.04 ms: 1.01x slower                                  |
| many_optionals                  | 403 us                                                 | 409 us: 1.01x slower                                   |
| sqlalchemy_imperative           | 6.60 ms                                                | 6.69 ms: 1.01x slower                                  |
| coroutines                      | 19.7 ms                                                | 20.0 ms: 1.02x slower                                  |
| sympy_integrate                 | 11.1 ms                                                | 11.3 ms: 1.02x slower                                  |
| scimark_fft                     | 194 ms                                                 | 200 ms: 1.03x slower                                   |
| xml_etree_generate              | 55.4 ms                                                | 57.1 ms: 1.03x slower                                  |
| deltablue                       | 2.57 ms                                                | 2.65 ms: 1.03x slower                                  |
| regex_compile                   | 75.9 ms                                                | 78.3 ms: 1.03x slower                                  |
| float                           | 54.1 ms                                                | 55.8 ms: 1.03x slower                                  |
| scimark_lu                      | 73.5 ms                                                | 75.9 ms: 1.03x slower                                  |
| create_gc_cycles                | 1.15 ms                                                | 1.19 ms: 1.04x slower                                  |
| nqueens                         | 59.5 ms                                                | 61.8 ms: 1.04x slower                                  |
| django_template                 | 19.7 ms                                                | 20.5 ms: 1.04x slower                                  |
| deepcopy_reduce                 | 2.01 us                                                | 2.09 us: 1.04x slower                                  |
| pycparser                       | 673 ms                                                 | 701 ms: 1.04x slower                                   |
| mako                            | 7.44 ms                                                | 7.75 ms: 1.04x slower                                  |
| python_startup_no_site          | 13.2 ms                                                | 13.7 ms: 1.04x slower                                  |
| bench_thread_pool               | 483 us                                                 | 503 us: 1.04x slower                                   |
| sqlglot_optimize                | 33.2 ms                                                | 34.7 ms: 1.04x slower                                  |
| regex_dna                       | 143 ms                                                 | 149 ms: 1.04x slower                                   |
| shortest_path                   | 331 ms                                                 | 345 ms: 1.04x slower                                   |
| deepcopy                        | 226 us                                                 | 236 us: 1.04x slower                                   |
| json_dumps                      | 6.19 ms                                                | 6.47 ms: 1.05x slower                                  |
| sqlglot_normalize               | 180 ms                                                 | 188 ms: 1.05x slower                                   |
| deepcopy_memo                   | 26.0 us                                                | 27.4 us: 1.05x slower                                  |
| sqlglot_parse                   | 808 us                                                 | 852 us: 1.05x slower                                   |
| python_startup                  | 17.8 ms                                                | 18.8 ms: 1.06x slower                                  |
| 2to3                            | 168 ms                                                 | 179 ms: 1.06x slower                                   |
| sympy_expand                    | 233 ms                                                 | 248 ms: 1.06x slower                                   |
| xml_etree_process               | 38.9 ms                                                | 41.3 ms: 1.06x slower                                  |
| async_tree_eager                | 65.8 ms                                                | 69.9 ms: 1.06x slower                                  |
| connected_components            | 300 ms                                                 | 319 ms: 1.06x slower                                   |
| sqlglot_transpile               | 973 us                                                 | 1.04 ms: 1.07x slower                                  |
| meteor_contest                  | 69.1 ms                                                | 74.0 ms: 1.07x slower                                  |
| crypto_pyaes                    | 51.4 ms                                                | 55.3 ms: 1.07x slower                                  |
| regex_effbot                    | 2.44 ms                                                | 2.63 ms: 1.08x slower                                  |
| chameleon                       | 4.55 ms                                                | 4.95 ms: 1.09x slower                                  |
| generators                      | 29.4 ms                                                | 31.9 ms: 1.09x slower                                  |
| nbody                           | 67.6 ms                                                | 73.6 ms: 1.09x slower                                  |
| pickle_pure_python              | 197 us                                                 | 215 us: 1.09x slower                                   |
| html5lib                        | 33.4 ms                                                | 36.7 ms: 1.10x slower                                  |
| typing_runtime_protocols        | 91.5 us                                                | 101 us: 1.10x slower                                   |
| hexiom                          | 4.38 ms                                                | 4.87 ms: 1.11x slower                                  |
| fannkuch                        | 250 ms                                                 | 279 ms: 1.11x slower                                   |
| pprint_pformat                  | 986 ms                                                 | 1.10 sec: 1.12x slower                                 |
| genshi_xml                      | 30.5 ms                                                | 34.1 ms: 1.12x slower                                  |
| pprint_safe_repr                | 483 ms                                                 | 541 ms: 1.12x slower                                   |
| regex_v8                        | 15.1 ms                                                | 17.0 ms: 1.13x slower                                  |
| pyflate                         | 311 ms                                                 | 352 ms: 1.13x slower                                   |
| richards_super                  | 34.6 ms                                                | 39.2 ms: 1.13x slower                                  |
| scimark_monte_carlo             | 44.5 ms                                                | 50.4 ms: 1.13x slower                                  |
| unpickle_pure_python            | 145 us                                                 | 165 us: 1.14x slower                                   |
| genshi_text                     | 14.7 ms                                                | 16.9 ms: 1.15x slower                                  |
| tomli_loads                     | 1.36 sec                                               | 1.57 sec: 1.15x slower                                 |
| richards                        | 30.6 ms                                                | 36.2 ms: 1.18x slower                                  |
| go                              | 98.5 ms                                                | 117 ms: 1.19x slower                                   |
| coverage                        | 38.5 ms                                                | 46.2 ms: 1.20x slower                                  |
| scimark_sor                     | 85.8 ms                                                | 106 ms: 1.23x slower                                   |
| telco                           | 3.92 ms                                                | 4.84 ms: 1.23x slower                                  |
| Geometric mean                  | (ref)                                                  | 1.00x faster                                           |

Benchmark hidden because not significant (9): tornado_http, pylint, async_tree_eager_cpu_io_mixed, asyncio_websockets, async_tree_eager_cpu_io_mixed_tg, spectral_norm, xml_etree_parse, json_loads, async_tree_eager_memoization

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 91.26% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x