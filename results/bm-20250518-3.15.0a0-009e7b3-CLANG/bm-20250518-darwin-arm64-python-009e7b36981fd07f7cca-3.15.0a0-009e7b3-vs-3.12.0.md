# Results vs. 3.12.0

- fork: python
- ref: 009e7b36981fd07f7cca
- machine: darwin-arm64
- commit hash: 009e7b3
- commit date: 2025-05-18
- overall geometric mean: 1.059x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 158 ms: 1.07x faster                                                  |
| docutils       | 1.45 sec                                               | 1.40 sec: 1.04x faster                                                |
| html5lib       | 33.4 ms                                                | 29.4 ms: 1.14x faster                                                 |
| sphinx         | 613 ms                                                 | 559 ms: 1.10x faster                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 335 ms: 1.99x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 340 ms: 1.97x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 342 ms: 1.97x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 347 ms: 1.78x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 145 ms: 1.76x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 182 ms: 1.75x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 152 ms: 1.74x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 180 ms: 1.72x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 402 ms: 1.31x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 408 ms: 1.29x faster                                                  |
| coroutines                       | 19.7 ms                                                | 15.3 ms: 1.29x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 133 ms: 1.26x faster                                                  |
| async_tree_eager                 | 65.8 ms                                                | 57.3 ms: 1.15x faster                                                 |
| async_generators                 | 299 ms                                                 | 266 ms: 1.12x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 350 ms: 1.07x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 381 ms: 1.10x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 159 ms: 1.12x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 120 ms: 2.56x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.30x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 43.9 ms: 1.23x faster                                                 |
| pidigits       | 283 ms                                                 | 280 ms: 1.01x faster                                                  |
| nbody          | 67.6 ms                                                | 73.8 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 61.6 ms: 1.23x faster                                                 |
| regex_effbot   | 2.44 ms                                                | 2.20 ms: 1.11x faster                                                 |
| regex_dna      | 143 ms                                                 | 141 ms: 1.01x faster                                                  |
| regex_v8       | 15.1 ms                                                | 15.5 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                               | 1.20 sec: 1.13x faster                                                |
| unpickle_pure_python | 145 us                                                 | 129 us: 1.12x faster                                                  |
| pickle_pure_python   | 197 us                                                 | 188 us: 1.05x faster                                                  |
| xml_etree_iterparse  | 75.5 ms                                                | 72.9 ms: 1.04x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 107 ms: 1.01x faster                                                  |
| xml_etree_generate   | 55.4 ms                                                | 55.6 ms: 1.00x slower                                                 |
| xml_etree_process    | 38.9 ms                                                | 39.4 ms: 1.01x slower                                                 |
| json_dumps           | 6.19 ms                                                | 6.36 ms: 1.03x slower                                                 |
| json_loads           | 17.0 us                                                | 18.4 us: 1.08x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 18.3 ms: 1.03x slower                                                 |
| python_startup_no_site | 13.2 ms                                                | 13.9 ms: 1.05x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.04x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text    | 14.7 ms                                                | 12.8 ms: 1.14x faster                                                 |
| genshi_xml     | 30.5 ms                                                | 27.1 ms: 1.13x faster                                                 |
| mako           | 7.44 ms                                                | 7.22 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 12.9 ms: 2.50x faster                                                 |
| mdp                              | 1.49 sec                                               | 709 ms: 2.11x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 335 ms: 1.99x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 340 ms: 1.97x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 342 ms: 1.97x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 347 ms: 1.78x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 145 ms: 1.76x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 182 ms: 1.75x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 152 ms: 1.74x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 180 ms: 1.72x faster                                                  |
| deepcopy_memo                    | 26.0 us                                                | 16.4 us: 1.59x faster                                                 |
| deepcopy                         | 226 us                                                 | 145 us: 1.56x faster                                                  |
| generators                       | 29.4 ms                                                | 18.9 ms: 1.56x faster                                                 |
| go                               | 98.5 ms                                                | 71.2 ms: 1.38x faster                                                 |
| comprehensions                   | 14.0 us                                                | 10.6 us: 1.32x faster                                                 |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 402 ms: 1.31x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 408 ms: 1.29x faster                                                  |
| coroutines                       | 19.7 ms                                                | 15.3 ms: 1.29x faster                                                 |
| raytrace                         | 204 ms                                                 | 161 ms: 1.27x faster                                                  |
| deepcopy_reduce                  | 2.01 us                                                | 1.59 us: 1.27x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 133 ms: 1.26x faster                                                  |
| deltablue                        | 2.57 ms                                                | 2.04 ms: 1.26x faster                                                 |
| regex_compile                    | 75.9 ms                                                | 61.6 ms: 1.23x faster                                                 |
| float                            | 54.1 ms                                                | 43.9 ms: 1.23x faster                                                 |
| dulwich_log                      | 29.2 ms                                                | 23.8 ms: 1.23x faster                                                 |
| pylint                           | 182 ms                                                 | 153 ms: 1.19x faster                                                  |
| chaos                            | 41.6 ms                                                | 35.6 ms: 1.17x faster                                                 |
| hexiom                           | 4.38 ms                                                | 3.79 ms: 1.16x faster                                                 |
| async_tree_eager                 | 65.8 ms                                                | 57.3 ms: 1.15x faster                                                 |
| genshi_text                      | 14.7 ms                                                | 12.8 ms: 1.14x faster                                                 |
| html5lib                         | 33.4 ms                                                | 29.4 ms: 1.14x faster                                                 |
| bpe_tokeniser                    | 3.28 sec                                               | 2.89 sec: 1.13x faster                                                |
| k_core                           | 1.72 sec                                               | 1.53 sec: 1.13x faster                                                |
| genshi_xml                       | 30.5 ms                                                | 27.1 ms: 1.13x faster                                                 |
| tomli_loads                      | 1.36 sec                                               | 1.20 sec: 1.13x faster                                                |
| async_generators                 | 299 ms                                                 | 266 ms: 1.12x faster                                                  |
| unpickle_pure_python             | 145 us                                                 | 129 us: 1.12x faster                                                  |
| pyflate                          | 311 ms                                                 | 277 ms: 1.12x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 68.6 ms: 1.11x faster                                                 |
| regex_effbot                     | 2.44 ms                                                | 2.20 ms: 1.11x faster                                                 |
| logging_simple                   | 3.60 us                                                | 3.27 us: 1.10x faster                                                 |
| nqueens                          | 59.5 ms                                                | 54.0 ms: 1.10x faster                                                 |
| scimark_sor                      | 85.8 ms                                                | 77.9 ms: 1.10x faster                                                 |
| scimark_monte_carlo              | 44.5 ms                                                | 40.4 ms: 1.10x faster                                                 |
| sphinx                           | 613 ms                                                 | 559 ms: 1.10x faster                                                  |
| sympy_str                        | 144 ms                                                 | 131 ms: 1.09x faster                                                  |
| sympy_sum                        | 76.2 ms                                                | 69.7 ms: 1.09x faster                                                 |
| sympy_integrate                  | 11.1 ms                                                | 10.2 ms: 1.09x faster                                                 |
| logging_format                   | 3.90 us                                                | 3.58 us: 1.09x faster                                                 |
| pprint_pformat                   | 986 ms                                                 | 907 ms: 1.09x faster                                                  |
| pprint_safe_repr                 | 483 ms                                                 | 447 ms: 1.08x faster                                                  |
| pycparser                        | 673 ms                                                 | 629 ms: 1.07x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 350 ms: 1.07x faster                                                  |
| 2to3                             | 168 ms                                                 | 158 ms: 1.07x faster                                                  |
| scimark_lu                       | 73.5 ms                                                | 69.7 ms: 1.05x faster                                                 |
| sympy_expand                     | 233 ms                                                 | 222 ms: 1.05x faster                                                  |
| pickle_pure_python               | 197 us                                                 | 188 us: 1.05x faster                                                  |
| richards_super                   | 34.6 ms                                                | 33.2 ms: 1.04x faster                                                 |
| docutils                         | 1.45 sec                                               | 1.40 sec: 1.04x faster                                                |
| richards                         | 30.6 ms                                                | 29.5 ms: 1.04x faster                                                 |
| xml_etree_iterparse              | 75.5 ms                                                | 72.9 ms: 1.04x faster                                                 |
| crypto_pyaes                     | 51.4 ms                                                | 49.9 ms: 1.03x faster                                                 |
| mako                             | 7.44 ms                                                | 7.22 ms: 1.03x faster                                                 |
| bench_thread_pool                | 483 us                                                 | 471 us: 1.03x faster                                                  |
| pathlib                          | 24.7 ms                                                | 24.1 ms: 1.02x faster                                                 |
| regex_dna                        | 143 ms                                                 | 141 ms: 1.01x faster                                                  |
| shortest_path                    | 331 ms                                                 | 327 ms: 1.01x faster                                                  |
| pidigits                         | 283 ms                                                 | 280 ms: 1.01x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 107 ms: 1.01x faster                                                  |
| xml_etree_generate               | 55.4 ms                                                | 55.6 ms: 1.00x slower                                                 |
| connected_components             | 300 ms                                                 | 302 ms: 1.01x slower                                                  |
| xml_etree_process                | 38.9 ms                                                | 39.4 ms: 1.01x slower                                                 |
| sqlite_synth                     | 1.55 us                                                | 1.57 us: 1.01x slower                                                 |
| json                             | 3.00 ms                                                | 3.05 ms: 1.01x slower                                                 |
| fannkuch                         | 250 ms                                                 | 254 ms: 1.02x slower                                                  |
| dask                             | 779 ms                                                 | 799 ms: 1.03x slower                                                  |
| regex_v8                         | 15.1 ms                                                | 15.5 ms: 1.03x slower                                                 |
| meteor_contest                   | 69.1 ms                                                | 71.0 ms: 1.03x slower                                                 |
| json_dumps                       | 6.19 ms                                                | 6.36 ms: 1.03x slower                                                 |
| python_startup                   | 17.8 ms                                                | 18.3 ms: 1.03x slower                                                 |
| python_startup_no_site           | 13.2 ms                                                | 13.9 ms: 1.05x slower                                                 |
| bench_mp_pool                    | 65.5 ms                                                | 69.6 ms: 1.06x slower                                                 |
| scimark_fft                      | 194 ms                                                 | 207 ms: 1.07x slower                                                  |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.37 ms: 1.07x slower                                                 |
| gc_traversal                     | 2.95 ms                                                | 3.18 ms: 1.08x slower                                                 |
| json_loads                       | 17.0 us                                                | 18.4 us: 1.08x slower                                                 |
| many_optionals                   | 403 us                                                 | 439 us: 1.09x slower                                                  |
| nbody                            | 67.6 ms                                                | 73.8 ms: 1.09x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 381 ms: 1.10x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 159 ms: 1.12x slower                                                  |
| telco                            | 3.92 ms                                                | 4.56 ms: 1.16x slower                                                 |
| create_gc_cycles                 | 1.15 ms                                                | 1.34 ms: 1.16x slower                                                 |
| async_tree_eager_tg              | 46.9 ms                                                | 120 ms: 2.56x slower                                                  |
| logging_silent                   | 72.5 ns                                                | 302 ns: 4.17x slower                                                  |
| coverage                         | 38.5 ms                                                | 258 ms: 6.71x slower                                                  |
| thrift                           | 468 us                                                 | 43.1 ms: 92.23x slower                                                |
| Geometric mean                   | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (3): django_template, asyncio_websockets, typing_runtime_protocols
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250518-3.15.0a0-009e7b3-CLANG/bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.059x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.12x