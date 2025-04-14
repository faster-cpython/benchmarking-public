# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: tail_call
- machine: darwin-arm64
- commit hash: df5d01c
- commit date: 2025-01-16
- overall geometric mean: 1.170x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250116-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 156 ms: 1.08x faster                                                  |
| docutils       | 1.45 sec                                               | 1.36 sec: 1.07x faster                                                |
| html5lib       | 33.4 ms                                                | 28.9 ms: 1.15x faster                                                 |
| sphinx         | 613 ms                                                 | 544 ms: 1.13x faster                                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250116-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 339 ms: 1.98x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 346 ms: 1.94x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 344 ms: 1.94x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 142 ms: 1.80x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 179 ms: 1.78x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 348 ms: 1.77x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 151 ms: 1.75x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 190 ms: 1.63x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 397 ms: 1.33x faster                                                  |
| coroutines                       | 19.7 ms                                                | 15.0 ms: 1.31x faster                                                 |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 407 ms: 1.29x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 135 ms: 1.24x faster                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 116 ms: 1.23x faster                                                  |
| async_generators                 | 299 ms                                                 | 247 ms: 1.21x faster                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 41.0 ms: 1.14x faster                                                 |
| async_tree_eager                 | 65.8 ms                                                | 60.4 ms: 1.09x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 351 ms: 1.07x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 330 ms: 1.05x faster                                                  |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                  |
| Geometric mean                   | (ref)                                                  | 1.41x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250116-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 44.1 ms: 1.23x faster                                                 |
| nbody          | 67.6 ms                                                | 63.9 ms: 1.06x faster                                                 |
| pidigits       | 283 ms                                                 | 280 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250116-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 62.9 ms: 1.21x faster                                                 |
| regex_effbot   | 2.44 ms                                                | 2.05 ms: 1.19x faster                                                 |
| regex_dna      | 143 ms                                                 | 138 ms: 1.03x faster                                                  |
| regex_v8       | 15.1 ms                                                | 16.9 ms: 1.12x slower                                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250116-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 145 us                                                 | 125 us: 1.17x faster                                                  |
| tomli_loads          | 1.36 sec                                               | 1.16 sec: 1.16x faster                                                |
| xml_etree_generate   | 55.4 ms                                                | 49.2 ms: 1.13x faster                                                 |
| xml_etree_process    | 38.9 ms                                                | 34.7 ms: 1.12x faster                                                 |
| xml_etree_iterparse  | 75.5 ms                                                | 69.4 ms: 1.09x faster                                                 |
| pickle_pure_python   | 197 us                                                 | 182 us: 1.08x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 102 ms: 1.06x faster                                                  |
| json_loads           | 17.0 us                                                | 16.3 us: 1.05x faster                                                 |
| json_dumps           | 6.19 ms                                                | 7.10 ms: 1.15x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250116-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 13.2 ms                                                | 11.6 ms: 1.13x faster                                                 |
| python_startup         | 17.8 ms                                                | 16.3 ms: 1.09x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250116-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 14.7 ms                                                | 12.4 ms: 1.18x faster                                                 |
| genshi_xml      | 30.5 ms                                                | 26.5 ms: 1.15x faster                                                 |
| mako            | 7.44 ms                                                | 7.05 ms: 1.06x faster                                                 |
| django_template | 19.7 ms                                                | 19.6 ms: 1.01x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250116-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 11.6 ms: 2.77x faster                                                 |
| async_tree_io_tg                 | 673 ms                                                 | 339 ms: 1.98x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 346 ms: 1.94x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 344 ms: 1.94x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 142 ms: 1.80x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 179 ms: 1.78x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 348 ms: 1.77x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 151 ms: 1.75x faster                                                  |
| generators                       | 29.4 ms                                                | 17.0 ms: 1.73x faster                                                 |
| async_tree_memoization           | 310 ms                                                 | 190 ms: 1.63x faster                                                  |
| deepcopy                         | 226 us                                                 | 143 us: 1.58x faster                                                  |
| deepcopy_memo                    | 26.0 us                                                | 17.0 us: 1.53x faster                                                 |
| go                               | 98.5 ms                                                | 71.8 ms: 1.37x faster                                                 |
| deepcopy_reduce                  | 2.01 us                                                | 1.49 us: 1.36x faster                                                 |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 397 ms: 1.33x faster                                                  |
| coroutines                       | 19.7 ms                                                | 15.0 ms: 1.31x faster                                                 |
| raytrace                         | 204 ms                                                 | 156 ms: 1.31x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 407 ms: 1.29x faster                                                  |
| deltablue                        | 2.57 ms                                                | 2.03 ms: 1.26x faster                                                 |
| logging_silent                   | 72.5 ns                                                | 58.4 ns: 1.24x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 135 ms: 1.24x faster                                                  |
| logging_simple                   | 3.60 us                                                | 2.93 us: 1.23x faster                                                 |
| spectral_norm                    | 76.5 ms                                                | 62.2 ms: 1.23x faster                                                 |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 116 ms: 1.23x faster                                                  |
| float                            | 54.1 ms                                                | 44.1 ms: 1.23x faster                                                 |
| comprehensions                   | 14.0 us                                                | 11.5 us: 1.21x faster                                                 |
| pylint                           | 182 ms                                                 | 150 ms: 1.21x faster                                                  |
| async_generators                 | 299 ms                                                 | 247 ms: 1.21x faster                                                  |
| regex_compile                    | 75.9 ms                                                | 62.9 ms: 1.21x faster                                                 |
| logging_format                   | 3.90 us                                                | 3.23 us: 1.21x faster                                                 |
| regex_effbot                     | 2.44 ms                                                | 2.05 ms: 1.19x faster                                                 |
| genshi_text                      | 14.7 ms                                                | 12.4 ms: 1.18x faster                                                 |
| unpickle_pure_python             | 145 us                                                 | 125 us: 1.17x faster                                                  |
| chaos                            | 41.6 ms                                                | 35.7 ms: 1.17x faster                                                 |
| hexiom                           | 4.38 ms                                                | 3.75 ms: 1.17x faster                                                 |
| sqlglot_parse                    | 808 us                                                 | 694 us: 1.16x faster                                                  |
| tomli_loads                      | 1.36 sec                                               | 1.16 sec: 1.16x faster                                                |
| k_core                           | 1.72 sec                                               | 1.48 sec: 1.16x faster                                                |
| nqueens                          | 59.5 ms                                                | 51.5 ms: 1.15x faster                                                 |
| html5lib                         | 33.4 ms                                                | 28.9 ms: 1.15x faster                                                 |
| scimark_sor                      | 85.8 ms                                                | 74.6 ms: 1.15x faster                                                 |
| genshi_xml                       | 30.5 ms                                                | 26.5 ms: 1.15x faster                                                 |
| sqlglot_transpile                | 973 us                                                 | 848 us: 1.15x faster                                                  |
| bpe_tokeniser                    | 3.28 sec                                               | 2.86 sec: 1.15x faster                                                |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 2.75 ms: 1.14x faster                                                 |
| async_tree_eager_tg              | 46.9 ms                                                | 41.0 ms: 1.14x faster                                                 |
| python_startup_no_site           | 13.2 ms                                                | 11.6 ms: 1.13x faster                                                 |
| scimark_monte_carlo              | 44.5 ms                                                | 39.3 ms: 1.13x faster                                                 |
| pyflate                          | 311 ms                                                 | 275 ms: 1.13x faster                                                  |
| sphinx                           | 613 ms                                                 | 544 ms: 1.13x faster                                                  |
| thrift                           | 468 us                                                 | 415 us: 1.13x faster                                                  |
| xml_etree_generate               | 55.4 ms                                                | 49.2 ms: 1.13x faster                                                 |
| xml_etree_process                | 38.9 ms                                                | 34.7 ms: 1.12x faster                                                 |
| scimark_lu                       | 73.5 ms                                                | 65.7 ms: 1.12x faster                                                 |
| pprint_pformat                   | 986 ms                                                 | 885 ms: 1.11x faster                                                  |
| bench_mp_pool                    | 65.5 ms                                                | 58.9 ms: 1.11x faster                                                 |
| pathlib                          | 24.7 ms                                                | 22.2 ms: 1.11x faster                                                 |
| richards_super                   | 34.6 ms                                                | 31.2 ms: 1.11x faster                                                 |
| scimark_fft                      | 194 ms                                                 | 176 ms: 1.11x faster                                                  |
| sqlalchemy_declarative           | 61.9 ms                                                | 56.1 ms: 1.10x faster                                                 |
| pprint_safe_repr                 | 483 ms                                                 | 439 ms: 1.10x faster                                                  |
| dulwich_log                      | 29.2 ms                                                | 26.6 ms: 1.10x faster                                                 |
| richards                         | 30.6 ms                                                | 27.8 ms: 1.10x faster                                                 |
| crypto_pyaes                     | 51.4 ms                                                | 47.0 ms: 1.09x faster                                                 |
| python_startup                   | 17.8 ms                                                | 16.3 ms: 1.09x faster                                                 |
| async_tree_eager                 | 65.8 ms                                                | 60.4 ms: 1.09x faster                                                 |
| sympy_str                        | 144 ms                                                 | 132 ms: 1.09x faster                                                  |
| xml_etree_iterparse              | 75.5 ms                                                | 69.4 ms: 1.09x faster                                                 |
| sympy_sum                        | 76.2 ms                                                | 70.3 ms: 1.08x faster                                                 |
| 2to3                             | 168 ms                                                 | 156 ms: 1.08x faster                                                  |
| pickle_pure_python               | 197 us                                                 | 182 us: 1.08x faster                                                  |
| sympy_integrate                  | 11.1 ms                                                | 10.3 ms: 1.08x faster                                                 |
| sqlglot_optimize                 | 33.2 ms                                                | 30.9 ms: 1.08x faster                                                 |
| docutils                         | 1.45 sec                                               | 1.36 sec: 1.07x faster                                                |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 351 ms: 1.07x faster                                                  |
| sqlglot_normalize                | 180 ms                                                 | 169 ms: 1.06x faster                                                  |
| json                             | 3.00 ms                                                | 2.83 ms: 1.06x faster                                                 |
| xml_etree_parse                  | 108 ms                                                 | 102 ms: 1.06x faster                                                  |
| sqlalchemy_imperative            | 6.60 ms                                                | 6.24 ms: 1.06x faster                                                 |
| nbody                            | 67.6 ms                                                | 63.9 ms: 1.06x faster                                                 |
| mako                             | 7.44 ms                                                | 7.05 ms: 1.06x faster                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 330 ms: 1.05x faster                                                  |
| sympy_expand                     | 233 ms                                                 | 223 ms: 1.05x faster                                                  |
| json_loads                       | 17.0 us                                                | 16.3 us: 1.05x faster                                                 |
| bench_thread_pool                | 483 us                                                 | 464 us: 1.04x faster                                                  |
| mdp                              | 1.49 sec                                               | 1.44 sec: 1.03x faster                                                |
| regex_dna                        | 143 ms                                                 | 138 ms: 1.03x faster                                                  |
| pycparser                        | 673 ms                                                 | 656 ms: 1.03x faster                                                  |
| fannkuch                         | 250 ms                                                 | 245 ms: 1.02x faster                                                  |
| shortest_path                    | 331 ms                                                 | 325 ms: 1.02x faster                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.53 us: 1.01x faster                                                 |
| dask                             | 779 ms                                                 | 770 ms: 1.01x faster                                                  |
| pidigits                         | 283 ms                                                 | 280 ms: 1.01x faster                                                  |
| django_template                  | 19.7 ms                                                | 19.6 ms: 1.01x faster                                                 |
| connected_components             | 300 ms                                                 | 298 ms: 1.00x faster                                                  |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                  |
| meteor_contest                   | 69.1 ms                                                | 70.8 ms: 1.02x slower                                                 |
| gc_traversal                     | 2.95 ms                                                | 3.11 ms: 1.05x slower                                                 |
| many_optionals                   | 403 us                                                 | 426 us: 1.06x slower                                                  |
| create_gc_cycles                 | 1.15 ms                                                | 1.29 ms: 1.12x slower                                                 |
| regex_v8                         | 15.1 ms                                                | 16.9 ms: 1.12x slower                                                 |
| telco                            | 3.92 ms                                                | 4.41 ms: 1.13x slower                                                 |
| json_dumps                       | 6.19 ms                                                | 7.10 ms: 1.15x slower                                                 |
| coverage                         | 38.5 ms                                                | 45.1 ms: 1.17x slower                                                 |
| Geometric mean                   | (ref)                                                  | 1.17x faster                                                          |

Benchmark hidden because not significant (1): typing_runtime_protocols
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.170x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: 1.05x