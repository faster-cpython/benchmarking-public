# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: trace_function_entry
- machine: darwin-arm64
- commit hash: 553888a
- commit date: 2025-03-07
- overall geometric mean: 1.066x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 165 ms: 1.02x faster                                                             |
| html5lib       | 33.4 ms                                                | 29.7 ms: 1.12x faster                                                            |
| sphinx         | 613 ms                                                 | 578 ms: 1.06x faster                                                             |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 366 ms: 1.84x faster                                                             |
| async_tree_eager_io              | 666 ms                                                 | 362 ms: 1.84x faster                                                             |
| async_tree_io                    | 672 ms                                                 | 366 ms: 1.83x faster                                                             |
| async_tree_eager_io_tg           | 617 ms                                                 | 374 ms: 1.65x faster                                                             |
| async_tree_none_tg               | 255 ms                                                 | 156 ms: 1.64x faster                                                             |
| async_tree_none                  | 263 ms                                                 | 161 ms: 1.63x faster                                                             |
| async_tree_memoization_tg        | 318 ms                                                 | 198 ms: 1.61x faster                                                             |
| async_tree_memoization           | 310 ms                                                 | 203 ms: 1.53x faster                                                             |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 417 ms: 1.27x faster                                                             |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 417 ms: 1.26x faster                                                             |
| async_tree_eager_memoization     | 168 ms                                                 | 141 ms: 1.18x faster                                                             |
| async_generators                 | 299 ms                                                 | 255 ms: 1.17x faster                                                             |
| coroutines                       | 19.7 ms                                                | 16.8 ms: 1.17x faster                                                            |
| async_tree_eager                 | 65.8 ms                                                | 62.1 ms: 1.06x faster                                                            |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 359 ms: 1.04x faster                                                             |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                             |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 392 ms: 1.13x slower                                                             |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 175 ms: 1.24x slower                                                             |
| async_tree_eager_tg              | 46.9 ms                                                | 131 ms: 2.78x slower                                                             |
| Geometric mean                   | (ref)                                                  | 1.23x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 47.9 ms: 1.13x faster                                                            |
| nbody          | 67.6 ms                                                | 67.7 ms: 1.00x slower                                                            |
| pidigits       | 283 ms                                                 | 284 ms: 1.00x slower                                                             |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.24 ms: 1.09x faster                                                            |
| regex_compile  | 75.9 ms                                                | 71.0 ms: 1.07x faster                                                            |
| regex_dna      | 143 ms                                                 | 141 ms: 1.01x faster                                                             |
| regex_v8       | 15.1 ms                                                | 16.7 ms: 1.11x slower                                                            |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| xml_etree_generate   | 55.4 ms                                                | 52.2 ms: 1.06x faster                                                            |
| xml_etree_iterparse  | 75.5 ms                                                | 71.1 ms: 1.06x faster                                                            |
| tomli_loads          | 1.36 sec                                               | 1.29 sec: 1.05x faster                                                           |
| xml_etree_parse      | 108 ms                                                 | 103 ms: 1.05x faster                                                             |
| xml_etree_process    | 38.9 ms                                                | 37.2 ms: 1.04x faster                                                            |
| unpickle_pure_python | 145 us                                                 | 142 us: 1.03x faster                                                             |
| json_loads           | 17.0 us                                                | 17.7 us: 1.04x slower                                                            |
| pickle_pure_python   | 197 us                                                 | 214 us: 1.09x slower                                                             |
| json_dumps           | 6.19 ms                                                | 7.29 ms: 1.18x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 19.6 ms: 1.10x slower                                                            |
| python_startup_no_site | 13.2 ms                                                | 15.1 ms: 1.15x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 7.44 ms                                                | 6.66 ms: 1.12x faster                                                            |
| genshi_text     | 14.7 ms                                                | 14.1 ms: 1.04x faster                                                            |
| genshi_xml      | 30.5 ms                                                | 29.6 ms: 1.03x faster                                                            |
| django_template | 19.7 ms                                                | 21.3 ms: 1.08x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                                     |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 12.2 ms: 2.63x faster                                                            |
| async_tree_io_tg                 | 673 ms                                                 | 366 ms: 1.84x faster                                                             |
| async_tree_eager_io              | 666 ms                                                 | 362 ms: 1.84x faster                                                             |
| async_tree_io                    | 672 ms                                                 | 366 ms: 1.83x faster                                                             |
| async_tree_eager_io_tg           | 617 ms                                                 | 374 ms: 1.65x faster                                                             |
| async_tree_none_tg               | 255 ms                                                 | 156 ms: 1.64x faster                                                             |
| async_tree_none                  | 263 ms                                                 | 161 ms: 1.63x faster                                                             |
| async_tree_memoization_tg        | 318 ms                                                 | 198 ms: 1.61x faster                                                             |
| async_tree_memoization           | 310 ms                                                 | 203 ms: 1.53x faster                                                             |
| deepcopy                         | 226 us                                                 | 152 us: 1.49x faster                                                             |
| deepcopy_memo                    | 26.0 us                                                | 18.7 us: 1.39x faster                                                            |
| deepcopy_reduce                  | 2.01 us                                                | 1.58 us: 1.27x faster                                                            |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 417 ms: 1.27x faster                                                             |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 417 ms: 1.26x faster                                                             |
| generators                       | 29.4 ms                                                | 23.8 ms: 1.23x faster                                                            |
| comprehensions                   | 14.0 us                                                | 11.8 us: 1.19x faster                                                            |
| go                               | 98.5 ms                                                | 83.1 ms: 1.18x faster                                                            |
| async_tree_eager_memoization     | 168 ms                                                 | 141 ms: 1.18x faster                                                             |
| async_generators                 | 299 ms                                                 | 255 ms: 1.17x faster                                                             |
| coroutines                       | 19.7 ms                                                | 16.8 ms: 1.17x faster                                                            |
| k_core                           | 1.72 sec                                               | 1.52 sec: 1.13x faster                                                           |
| float                            | 54.1 ms                                                | 47.9 ms: 1.13x faster                                                            |
| html5lib                         | 33.4 ms                                                | 29.7 ms: 1.12x faster                                                            |
| logging_simple                   | 3.60 us                                                | 3.22 us: 1.12x faster                                                            |
| mako                             | 7.44 ms                                                | 6.66 ms: 1.12x faster                                                            |
| raytrace                         | 204 ms                                                 | 183 ms: 1.12x faster                                                             |
| pylint                           | 182 ms                                                 | 164 ms: 1.11x faster                                                             |
| logging_format                   | 3.90 us                                                | 3.53 us: 1.10x faster                                                            |
| bpe_tokeniser                    | 3.28 sec                                               | 3.00 sec: 1.10x faster                                                           |
| regex_effbot                     | 2.44 ms                                                | 2.24 ms: 1.09x faster                                                            |
| thrift                           | 468 us                                                 | 435 us: 1.08x faster                                                             |
| logging_silent                   | 72.5 ns                                                | 67.7 ns: 1.07x faster                                                            |
| bench_mp_pool                    | 65.5 ms                                                | 61.2 ms: 1.07x faster                                                            |
| regex_compile                    | 75.9 ms                                                | 71.0 ms: 1.07x faster                                                            |
| xml_etree_generate               | 55.4 ms                                                | 52.2 ms: 1.06x faster                                                            |
| xml_etree_iterparse              | 75.5 ms                                                | 71.1 ms: 1.06x faster                                                            |
| sphinx                           | 613 ms                                                 | 578 ms: 1.06x faster                                                             |
| scimark_sor                      | 85.8 ms                                                | 80.9 ms: 1.06x faster                                                            |
| async_tree_eager                 | 65.8 ms                                                | 62.1 ms: 1.06x faster                                                            |
| deltablue                        | 2.57 ms                                                | 2.42 ms: 1.06x faster                                                            |
| spectral_norm                    | 76.5 ms                                                | 72.2 ms: 1.06x faster                                                            |
| pathlib                          | 24.7 ms                                                | 23.4 ms: 1.06x faster                                                            |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 2.97 ms: 1.06x faster                                                            |
| chaos                            | 41.6 ms                                                | 39.6 ms: 1.05x faster                                                            |
| tomli_loads                      | 1.36 sec                                               | 1.29 sec: 1.05x faster                                                           |
| xml_etree_parse                  | 108 ms                                                 | 103 ms: 1.05x faster                                                             |
| sqlalchemy_declarative           | 61.9 ms                                                | 59.2 ms: 1.05x faster                                                            |
| xml_etree_process                | 38.9 ms                                                | 37.2 ms: 1.04x faster                                                            |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 359 ms: 1.04x faster                                                             |
| genshi_text                      | 14.7 ms                                                | 14.1 ms: 1.04x faster                                                            |
| scimark_fft                      | 194 ms                                                 | 187 ms: 1.04x faster                                                             |
| genshi_xml                       | 30.5 ms                                                | 29.6 ms: 1.03x faster                                                            |
| sympy_sum                        | 76.2 ms                                                | 74.2 ms: 1.03x faster                                                            |
| unpickle_pure_python             | 145 us                                                 | 142 us: 1.03x faster                                                             |
| scimark_monte_carlo              | 44.5 ms                                                | 43.5 ms: 1.02x faster                                                            |
| 2to3                             | 168 ms                                                 | 165 ms: 1.02x faster                                                             |
| dask                             | 779 ms                                                 | 767 ms: 1.02x faster                                                             |
| sympy_str                        | 144 ms                                                 | 142 ms: 1.02x faster                                                             |
| dulwich_log                      | 29.2 ms                                                | 28.8 ms: 1.02x faster                                                            |
| regex_dna                        | 143 ms                                                 | 141 ms: 1.01x faster                                                             |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                             |
| sqlite_synth                     | 1.55 us                                                | 1.54 us: 1.00x faster                                                            |
| nbody                            | 67.6 ms                                                | 67.7 ms: 1.00x slower                                                            |
| pidigits                         | 283 ms                                                 | 284 ms: 1.00x slower                                                             |
| pyflate                          | 311 ms                                                 | 313 ms: 1.01x slower                                                             |
| nqueens                          | 59.5 ms                                                | 60.1 ms: 1.01x slower                                                            |
| scimark_lu                       | 73.5 ms                                                | 74.3 ms: 1.01x slower                                                            |
| hexiom                           | 4.38 ms                                                | 4.47 ms: 1.02x slower                                                            |
| sqlalchemy_imperative            | 6.60 ms                                                | 6.76 ms: 1.03x slower                                                            |
| bench_thread_pool                | 483 us                                                 | 496 us: 1.03x slower                                                             |
| sympy_expand                     | 233 ms                                                 | 241 ms: 1.03x slower                                                             |
| typing_runtime_protocols         | 91.5 us                                                | 94.5 us: 1.03x slower                                                            |
| sympy_integrate                  | 11.1 ms                                                | 11.5 ms: 1.03x slower                                                            |
| json_loads                       | 17.0 us                                                | 17.7 us: 1.04x slower                                                            |
| gc_traversal                     | 2.95 ms                                                | 3.09 ms: 1.05x slower                                                            |
| meteor_contest                   | 69.1 ms                                                | 74.0 ms: 1.07x slower                                                            |
| richards                         | 30.6 ms                                                | 32.8 ms: 1.07x slower                                                            |
| richards_super                   | 34.6 ms                                                | 37.2 ms: 1.08x slower                                                            |
| django_template                  | 19.7 ms                                                | 21.3 ms: 1.08x slower                                                            |
| crypto_pyaes                     | 51.4 ms                                                | 56.0 ms: 1.09x slower                                                            |
| pickle_pure_python               | 197 us                                                 | 214 us: 1.09x slower                                                             |
| sqlglot_transpile                | 973 us                                                 | 1.07 ms: 1.10x slower                                                            |
| python_startup                   | 17.8 ms                                                | 19.6 ms: 1.10x slower                                                            |
| create_gc_cycles                 | 1.15 ms                                                | 1.27 ms: 1.10x slower                                                            |
| regex_v8                         | 15.1 ms                                                | 16.7 ms: 1.11x slower                                                            |
| sqlglot_parse                    | 808 us                                                 | 900 us: 1.11x slower                                                             |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 392 ms: 1.13x slower                                                             |
| many_optionals                   | 403 us                                                 | 456 us: 1.13x slower                                                             |
| python_startup_no_site           | 13.2 ms                                                | 15.1 ms: 1.15x slower                                                            |
| telco                            | 3.92 ms                                                | 4.55 ms: 1.16x slower                                                            |
| json_dumps                       | 6.19 ms                                                | 7.29 ms: 1.18x slower                                                            |
| coverage                         | 38.5 ms                                                | 46.4 ms: 1.20x slower                                                            |
| fannkuch                         | 250 ms                                                 | 305 ms: 1.22x slower                                                             |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 175 ms: 1.24x slower                                                             |
| async_tree_eager_tg              | 46.9 ms                                                | 131 ms: 2.78x slower                                                             |
| Geometric mean                   | (ref)                                                  | 1.07x faster                                                                     |

Benchmark hidden because not significant (5): shortest_path, connected_components, mdp, pycparser, json
Ignored benchmarks (10) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, docutils, gevent_hub, gunicorn, pprint_pformat, pprint_safe_repr, sqlglot_normalize, sqlglot_optimize, tornado_http

- Geometric mean (including insignificant results): 1.066x faster

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.11x