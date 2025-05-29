# Results vs. 3.12.0

- fork: python
- ref: 85bc489b649fe261f962
- machine: darwin-arm64
- commit hash: 85bc489
- commit date: 2025-04-05
- overall geometric mean: 1.154x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250405-darwin-arm64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 151 ms: 1.11x faster                                                   |
| docutils       | 1.45 sec                                               | 1.36 sec: 1.07x faster                                                 |
| html5lib       | 33.4 ms                                                | 29.1 ms: 1.15x faster                                                  |
| sphinx         | 613 ms                                                 | 549 ms: 1.12x faster                                                   |
| Geometric mean | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250405-darwin-arm64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io                    | 672 ms                                                 | 336 ms: 2.00x faster                                                   |
| async_tree_io_tg                 | 673 ms                                                 | 338 ms: 1.99x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 338 ms: 1.97x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 142 ms: 1.80x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 346 ms: 1.78x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 180 ms: 1.77x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 149 ms: 1.77x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 177 ms: 1.75x faster                                                   |
| coroutines                       | 19.7 ms                                                | 14.7 ms: 1.34x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 396 ms: 1.33x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 396 ms: 1.33x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 130 ms: 1.29x faster                                                   |
| async_generators                 | 299 ms                                                 | 254 ms: 1.18x faster                                                   |
| async_tree_eager                 | 65.8 ms                                                | 56.0 ms: 1.18x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 344 ms: 1.09x faster                                                   |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 377 ms: 1.08x slower                                                   |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 160 ms: 1.13x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 121 ms: 2.58x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.32x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250405-darwin-arm64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 43.0 ms: 1.26x faster                                                  |
| pidigits       | 283 ms                                                 | 280 ms: 1.01x faster                                                   |
| nbody          | 67.6 ms                                                | 71.8 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250405-darwin-arm64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 61.3 ms: 1.24x faster                                                  |
| regex_effbot   | 2.44 ms                                                | 2.39 ms: 1.02x faster                                                  |
| regex_dna      | 143 ms                                                 | 148 ms: 1.04x slower                                                   |
| regex_v8       | 15.1 ms                                                | 16.9 ms: 1.12x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250405-darwin-arm64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                               | 1.15 sec: 1.17x faster                                                 |
| xml_etree_generate   | 55.4 ms                                                | 48.5 ms: 1.14x faster                                                  |
| xml_etree_process    | 38.9 ms                                                | 34.3 ms: 1.13x faster                                                  |
| unpickle_pure_python | 145 us                                                 | 129 us: 1.13x faster                                                   |
| xml_etree_iterparse  | 75.5 ms                                                | 69.7 ms: 1.08x faster                                                  |
| pickle_pure_python   | 197 us                                                 | 186 us: 1.06x faster                                                   |
| xml_etree_parse      | 108 ms                                                 | 102 ms: 1.06x faster                                                   |
| json_loads           | 17.0 us                                                | 17.8 us: 1.05x slower                                                  |
| json_dumps           | 6.19 ms                                                | 7.17 ms: 1.16x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250405-darwin-arm64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 19.2 ms: 1.08x slower                                                  |
| python_startup_no_site | 13.2 ms                                                | 14.8 ms: 1.13x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250405-darwin-arm64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 14.7 ms                                                | 12.6 ms: 1.16x faster                                                  |
| genshi_xml      | 30.5 ms                                                | 26.7 ms: 1.14x faster                                                  |
| mako            | 7.44 ms                                                | 7.33 ms: 1.02x faster                                                  |
| django_template | 19.7 ms                                                | 19.5 ms: 1.01x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250405-darwin-arm64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 11.4 ms: 2.81x faster                                                  |
| mdp                              | 1.49 sec                                               | 688 ms: 2.17x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 336 ms: 2.00x faster                                                   |
| async_tree_io_tg                 | 673 ms                                                 | 338 ms: 1.99x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 338 ms: 1.97x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 142 ms: 1.80x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 346 ms: 1.78x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 180 ms: 1.77x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 149 ms: 1.77x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 177 ms: 1.75x faster                                                   |
| deepcopy                         | 226 us                                                 | 139 us: 1.63x faster                                                   |
| deepcopy_memo                    | 26.0 us                                                | 16.1 us: 1.61x faster                                                  |
| generators                       | 29.4 ms                                                | 19.1 ms: 1.54x faster                                                  |
| comprehensions                   | 14.0 us                                                | 10.1 us: 1.39x faster                                                  |
| go                               | 98.5 ms                                                | 70.9 ms: 1.39x faster                                                  |
| deepcopy_reduce                  | 2.01 us                                                | 1.48 us: 1.36x faster                                                  |
| coroutines                       | 19.7 ms                                                | 14.7 ms: 1.34x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 396 ms: 1.33x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 396 ms: 1.33x faster                                                   |
| raytrace                         | 204 ms                                                 | 157 ms: 1.30x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 130 ms: 1.29x faster                                                   |
| logging_silent                   | 72.5 ns                                                | 57.4 ns: 1.26x faster                                                  |
| float                            | 54.1 ms                                                | 43.0 ms: 1.26x faster                                                  |
| deltablue                        | 2.57 ms                                                | 2.06 ms: 1.25x faster                                                  |
| regex_compile                    | 75.9 ms                                                | 61.3 ms: 1.24x faster                                                  |
| dulwich_log                      | 29.2 ms                                                | 23.6 ms: 1.24x faster                                                  |
| logging_simple                   | 3.60 us                                                | 2.96 us: 1.22x faster                                                  |
| pylint                           | 182 ms                                                 | 151 ms: 1.21x faster                                                   |
| logging_format                   | 3.90 us                                                | 3.25 us: 1.20x faster                                                  |
| async_generators                 | 299 ms                                                 | 254 ms: 1.18x faster                                                   |
| async_tree_eager                 | 65.8 ms                                                | 56.0 ms: 1.18x faster                                                  |
| tomli_loads                      | 1.36 sec                                               | 1.15 sec: 1.17x faster                                                 |
| scimark_sor                      | 85.8 ms                                                | 73.2 ms: 1.17x faster                                                  |
| bpe_tokeniser                    | 3.28 sec                                               | 2.81 sec: 1.17x faster                                                 |
| genshi_text                      | 14.7 ms                                                | 12.6 ms: 1.16x faster                                                  |
| chaos                            | 41.6 ms                                                | 36.0 ms: 1.16x faster                                                  |
| k_core                           | 1.72 sec                                               | 1.49 sec: 1.15x faster                                                 |
| hexiom                           | 4.38 ms                                                | 3.80 ms: 1.15x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 66.7 ms: 1.15x faster                                                  |
| html5lib                         | 33.4 ms                                                | 29.1 ms: 1.15x faster                                                  |
| genshi_xml                       | 30.5 ms                                                | 26.7 ms: 1.14x faster                                                  |
| xml_etree_generate               | 55.4 ms                                                | 48.5 ms: 1.14x faster                                                  |
| pyflate                          | 311 ms                                                 | 274 ms: 1.14x faster                                                   |
| xml_etree_process                | 38.9 ms                                                | 34.3 ms: 1.13x faster                                                  |
| unpickle_pure_python             | 145 us                                                 | 129 us: 1.13x faster                                                   |
| scimark_monte_carlo              | 44.5 ms                                                | 39.6 ms: 1.12x faster                                                  |
| sqlalchemy_declarative           | 61.9 ms                                                | 55.3 ms: 1.12x faster                                                  |
| nqueens                          | 59.5 ms                                                | 53.3 ms: 1.12x faster                                                  |
| sphinx                           | 613 ms                                                 | 549 ms: 1.12x faster                                                   |
| 2to3                             | 168 ms                                                 | 151 ms: 1.11x faster                                                   |
| sympy_str                        | 144 ms                                                 | 130 ms: 1.11x faster                                                   |
| sympy_integrate                  | 11.1 ms                                                | 10.0 ms: 1.10x faster                                                  |
| sympy_sum                        | 76.2 ms                                                | 69.3 ms: 1.10x faster                                                  |
| bench_mp_pool                    | 65.5 ms                                                | 60.0 ms: 1.09x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 344 ms: 1.09x faster                                                   |
| xml_etree_iterparse              | 75.5 ms                                                | 69.7 ms: 1.08x faster                                                  |
| sympy_expand                     | 233 ms                                                 | 217 ms: 1.08x faster                                                   |
| pycparser                        | 673 ms                                                 | 625 ms: 1.08x faster                                                   |
| sqlalchemy_imperative            | 6.60 ms                                                | 6.15 ms: 1.07x faster                                                  |
| pprint_pformat                   | 986 ms                                                 | 919 ms: 1.07x faster                                                   |
| pathlib                          | 24.7 ms                                                | 23.1 ms: 1.07x faster                                                  |
| docutils                         | 1.45 sec                                               | 1.36 sec: 1.07x faster                                                 |
| pprint_safe_repr                 | 483 ms                                                 | 453 ms: 1.07x faster                                                   |
| pickle_pure_python               | 197 us                                                 | 186 us: 1.06x faster                                                   |
| xml_etree_parse                  | 108 ms                                                 | 102 ms: 1.06x faster                                                   |
| scimark_lu                       | 73.5 ms                                                | 69.4 ms: 1.06x faster                                                  |
| bench_thread_pool                | 483 us                                                 | 457 us: 1.06x faster                                                   |
| typing_runtime_protocols         | 91.5 us                                                | 86.7 us: 1.06x faster                                                  |
| richards_super                   | 34.6 ms                                                | 33.0 ms: 1.05x faster                                                  |
| richards                         | 30.6 ms                                                | 29.3 ms: 1.04x faster                                                  |
| crypto_pyaes                     | 51.4 ms                                                | 49.4 ms: 1.04x faster                                                  |
| regex_effbot                     | 2.44 ms                                                | 2.39 ms: 1.02x faster                                                  |
| shortest_path                    | 331 ms                                                 | 325 ms: 1.02x faster                                                   |
| sqlite_synth                     | 1.55 us                                                | 1.52 us: 1.02x faster                                                  |
| mako                             | 7.44 ms                                                | 7.33 ms: 1.02x faster                                                  |
| scimark_fft                      | 194 ms                                                 | 192 ms: 1.01x faster                                                   |
| django_template                  | 19.7 ms                                                | 19.5 ms: 1.01x faster                                                  |
| pidigits                         | 283 ms                                                 | 280 ms: 1.01x faster                                                   |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                   |
| fannkuch                         | 250 ms                                                 | 249 ms: 1.00x faster                                                   |
| meteor_contest                   | 69.1 ms                                                | 70.1 ms: 1.02x slower                                                  |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.21 ms: 1.02x slower                                                  |
| regex_dna                        | 143 ms                                                 | 148 ms: 1.04x slower                                                   |
| many_optionals                   | 403 us                                                 | 419 us: 1.04x slower                                                   |
| gc_traversal                     | 2.95 ms                                                | 3.08 ms: 1.04x slower                                                  |
| json_loads                       | 17.0 us                                                | 17.8 us: 1.05x slower                                                  |
| nbody                            | 67.6 ms                                                | 71.8 ms: 1.06x slower                                                  |
| python_startup                   | 17.8 ms                                                | 19.2 ms: 1.08x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 377 ms: 1.08x slower                                                   |
| create_gc_cycles                 | 1.15 ms                                                | 1.26 ms: 1.10x slower                                                  |
| regex_v8                         | 15.1 ms                                                | 16.9 ms: 1.12x slower                                                  |
| python_startup_no_site           | 13.2 ms                                                | 14.8 ms: 1.13x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 160 ms: 1.13x slower                                                   |
| telco                            | 3.92 ms                                                | 4.49 ms: 1.14x slower                                                  |
| json_dumps                       | 6.19 ms                                                | 7.17 ms: 1.16x slower                                                  |
| coverage                         | 38.5 ms                                                | 45.4 ms: 1.18x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 121 ms: 2.58x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.16x faster                                                           |

Benchmark hidden because not significant (2): connected_components, json
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250405-3.14.0a6+-85bc489-CLANG/bm-20250405-darwin-arm64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.154x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.10x