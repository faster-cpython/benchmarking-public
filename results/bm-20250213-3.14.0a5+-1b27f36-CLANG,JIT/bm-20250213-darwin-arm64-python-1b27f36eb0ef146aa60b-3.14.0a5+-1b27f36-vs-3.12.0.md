# Results vs. 3.12.0

- fork: python
- ref: 1b27f36eb0ef146aa60b
- machine: darwin-arm64
- commit hash: 1b27f36
- commit date: 2025-02-13
- overall geometric mean: 1.127x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250213-darwin-arm64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 179 ms: 1.06x slower                                                   |
| docutils       | 1.45 sec                                               | 1.39 sec: 1.04x faster                                                 |
| html5lib       | 33.4 ms                                                | 29.1 ms: 1.14x faster                                                  |
| sphinx         | 613 ms                                                 | 547 ms: 1.12x faster                                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250213-darwin-arm64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io                    | 672 ms                                                 | 345 ms: 1.95x faster                                                   |
| async_tree_io_tg                 | 673 ms                                                 | 351 ms: 1.92x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 349 ms: 1.91x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 352 ms: 1.75x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 147 ms: 1.74x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 154 ms: 1.71x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 187 ms: 1.70x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 185 ms: 1.67x faster                                                   |
| coroutines                       | 19.7 ms                                                | 15.0 ms: 1.31x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 407 ms: 1.29x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 410 ms: 1.29x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 138 ms: 1.22x faster                                                   |
| async_generators                 | 299 ms                                                 | 269 ms: 1.11x faster                                                   |
| async_tree_eager                 | 65.8 ms                                                | 61.2 ms: 1.08x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 353 ms: 1.06x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 382 ms: 1.10x slower                                                   |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 167 ms: 1.18x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 124 ms: 2.65x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.28x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250213-darwin-arm64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 44.2 ms: 1.22x faster                                                  |
| nbody          | 67.6 ms                                                | 63.6 ms: 1.06x faster                                                  |
| pidigits       | 283 ms                                                 | 280 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250213-darwin-arm64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 63.8 ms: 1.19x faster                                                  |
| regex_effbot   | 2.44 ms                                                | 2.39 ms: 1.02x faster                                                  |
| regex_dna      | 143 ms                                                 | 147 ms: 1.03x slower                                                   |
| regex_v8       | 15.1 ms                                                | 18.0 ms: 1.19x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250213-darwin-arm64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_process    | 38.9 ms                                                | 33.2 ms: 1.17x faster                                                  |
| tomli_loads          | 1.36 sec                                               | 1.16 sec: 1.17x faster                                                 |
| xml_etree_generate   | 55.4 ms                                                | 48.1 ms: 1.15x faster                                                  |
| unpickle_pure_python | 145 us                                                 | 128 us: 1.13x faster                                                   |
| xml_etree_parse      | 108 ms                                                 | 97.1 ms: 1.11x faster                                                  |
| xml_etree_iterparse  | 75.5 ms                                                | 69.0 ms: 1.09x faster                                                  |
| pickle_pure_python   | 197 us                                                 | 186 us: 1.06x faster                                                   |
| json_loads           | 17.0 us                                                | 17.9 us: 1.05x slower                                                  |
| json_dumps           | 6.19 ms                                                | 7.12 ms: 1.15x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250213-darwin-arm64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 13.2 ms                                                | 12.0 ms: 1.10x faster                                                  |
| python_startup         | 17.8 ms                                                | 16.7 ms: 1.06x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250213-darwin-arm64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 14.7 ms                                                | 12.7 ms: 1.15x faster                                                  |
| mako            | 7.44 ms                                                | 6.47 ms: 1.15x faster                                                  |
| genshi_xml      | 30.5 ms                                                | 27.4 ms: 1.11x faster                                                  |
| django_template | 19.7 ms                                                | 19.0 ms: 1.04x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.11x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250213-darwin-arm64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 11.5 ms: 2.81x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 345 ms: 1.95x faster                                                   |
| async_tree_io_tg                 | 673 ms                                                 | 351 ms: 1.92x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 349 ms: 1.91x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 352 ms: 1.75x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 147 ms: 1.74x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 154 ms: 1.71x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 187 ms: 1.70x faster                                                   |
| generators                       | 29.4 ms                                                | 17.4 ms: 1.69x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 185 ms: 1.67x faster                                                   |
| deepcopy                         | 226 us                                                 | 139 us: 1.63x faster                                                   |
| deepcopy_memo                    | 26.0 us                                                | 16.7 us: 1.56x faster                                                  |
| deepcopy_reduce                  | 2.01 us                                                | 1.49 us: 1.35x faster                                                  |
| go                               | 98.5 ms                                                | 72.8 ms: 1.35x faster                                                  |
| coroutines                       | 19.7 ms                                                | 15.0 ms: 1.31x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 407 ms: 1.29x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 410 ms: 1.29x faster                                                   |
| raytrace                         | 204 ms                                                 | 163 ms: 1.25x faster                                                   |
| logging_silent                   | 72.5 ns                                                | 58.4 ns: 1.24x faster                                                  |
| deltablue                        | 2.57 ms                                                | 2.07 ms: 1.24x faster                                                  |
| logging_simple                   | 3.60 us                                                | 2.93 us: 1.23x faster                                                  |
| float                            | 54.1 ms                                                | 44.2 ms: 1.22x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 138 ms: 1.22x faster                                                   |
| logging_format                   | 3.90 us                                                | 3.21 us: 1.22x faster                                                  |
| comprehensions                   | 14.0 us                                                | 11.6 us: 1.21x faster                                                  |
| pylint                           | 182 ms                                                 | 151 ms: 1.21x faster                                                   |
| regex_compile                    | 75.9 ms                                                | 63.8 ms: 1.19x faster                                                  |
| xml_etree_process                | 38.9 ms                                                | 33.2 ms: 1.17x faster                                                  |
| tomli_loads                      | 1.36 sec                                               | 1.16 sec: 1.17x faster                                                 |
| chaos                            | 41.6 ms                                                | 35.8 ms: 1.16x faster                                                  |
| scimark_sor                      | 85.8 ms                                                | 74.3 ms: 1.15x faster                                                  |
| xml_etree_generate               | 55.4 ms                                                | 48.1 ms: 1.15x faster                                                  |
| genshi_text                      | 14.7 ms                                                | 12.7 ms: 1.15x faster                                                  |
| mako                             | 7.44 ms                                                | 6.47 ms: 1.15x faster                                                  |
| html5lib                         | 33.4 ms                                                | 29.1 ms: 1.14x faster                                                  |
| thrift                           | 468 us                                                 | 410 us: 1.14x faster                                                   |
| bpe_tokeniser                    | 3.28 sec                                               | 2.89 sec: 1.14x faster                                                 |
| k_core                           | 1.72 sec                                               | 1.52 sec: 1.13x faster                                                 |
| unpickle_pure_python             | 145 us                                                 | 128 us: 1.13x faster                                                   |
| bench_mp_pool                    | 65.5 ms                                                | 58.0 ms: 1.13x faster                                                  |
| scimark_monte_carlo              | 44.5 ms                                                | 39.5 ms: 1.12x faster                                                  |
| nqueens                          | 59.5 ms                                                | 53.0 ms: 1.12x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 68.1 ms: 1.12x faster                                                  |
| sphinx                           | 613 ms                                                 | 547 ms: 1.12x faster                                                   |
| hexiom                           | 4.38 ms                                                | 3.91 ms: 1.12x faster                                                  |
| sqlalchemy_declarative           | 61.9 ms                                                | 55.5 ms: 1.11x faster                                                  |
| genshi_xml                       | 30.5 ms                                                | 27.4 ms: 1.11x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 97.1 ms: 1.11x faster                                                  |
| async_generators                 | 299 ms                                                 | 269 ms: 1.11x faster                                                   |
| richards_super                   | 34.6 ms                                                | 31.3 ms: 1.11x faster                                                  |
| richards                         | 30.6 ms                                                | 27.7 ms: 1.10x faster                                                  |
| pathlib                          | 24.7 ms                                                | 22.4 ms: 1.10x faster                                                  |
| python_startup_no_site           | 13.2 ms                                                | 12.0 ms: 1.10x faster                                                  |
| xml_etree_iterparse              | 75.5 ms                                                | 69.0 ms: 1.09x faster                                                  |
| sympy_str                        | 144 ms                                                 | 132 ms: 1.09x faster                                                   |
| sympy_sum                        | 76.2 ms                                                | 70.3 ms: 1.08x faster                                                  |
| dulwich_log                      | 29.2 ms                                                | 27.0 ms: 1.08x faster                                                  |
| async_tree_eager                 | 65.8 ms                                                | 61.2 ms: 1.08x faster                                                  |
| scimark_fft                      | 194 ms                                                 | 181 ms: 1.07x faster                                                   |
| sympy_integrate                  | 11.1 ms                                                | 10.3 ms: 1.07x faster                                                  |
| sqlglot_optimize                 | 33.2 ms                                                | 31.0 ms: 1.07x faster                                                  |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 2.94 ms: 1.07x faster                                                  |
| sqlglot_normalize                | 180 ms                                                 | 168 ms: 1.07x faster                                                   |
| python_startup                   | 17.8 ms                                                | 16.7 ms: 1.06x faster                                                  |
| nbody                            | 67.6 ms                                                | 63.6 ms: 1.06x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 353 ms: 1.06x faster                                                   |
| pickle_pure_python               | 197 us                                                 | 186 us: 1.06x faster                                                   |
| pyflate                          | 311 ms                                                 | 295 ms: 1.05x faster                                                   |
| bench_thread_pool                | 483 us                                                 | 459 us: 1.05x faster                                                   |
| sympy_expand                     | 233 ms                                                 | 222 ms: 1.05x faster                                                   |
| mdp                              | 1.49 sec                                               | 1.43 sec: 1.04x faster                                                 |
| docutils                         | 1.45 sec                                               | 1.39 sec: 1.04x faster                                                 |
| django_template                  | 19.7 ms                                                | 19.0 ms: 1.04x faster                                                  |
| sqlalchemy_imperative            | 6.60 ms                                                | 6.37 ms: 1.04x faster                                                  |
| scimark_lu                       | 73.5 ms                                                | 70.9 ms: 1.04x faster                                                  |
| pycparser                        | 673 ms                                                 | 656 ms: 1.03x faster                                                   |
| typing_runtime_protocols         | 91.5 us                                                | 89.4 us: 1.02x faster                                                  |
| regex_effbot                     | 2.44 ms                                                | 2.39 ms: 1.02x faster                                                  |
| dask                             | 779 ms                                                 | 770 ms: 1.01x faster                                                   |
| pidigits                         | 283 ms                                                 | 280 ms: 1.01x faster                                                   |
| shortest_path                    | 331 ms                                                 | 327 ms: 1.01x faster                                                   |
| sqlite_synth                     | 1.55 us                                                | 1.53 us: 1.01x faster                                                  |
| sqlglot_transpile                | 973 us                                                 | 968 us: 1.01x faster                                                   |
| sqlglot_parse                    | 808 us                                                 | 814 us: 1.01x slower                                                   |
| pprint_safe_repr                 | 483 ms                                                 | 487 ms: 1.01x slower                                                   |
| pprint_pformat                   | 986 ms                                                 | 993 ms: 1.01x slower                                                   |
| regex_dna                        | 143 ms                                                 | 147 ms: 1.03x slower                                                   |
| gc_traversal                     | 2.95 ms                                                | 3.09 ms: 1.05x slower                                                  |
| json_loads                       | 17.0 us                                                | 17.9 us: 1.05x slower                                                  |
| 2to3                             | 168 ms                                                 | 179 ms: 1.06x slower                                                   |
| many_optionals                   | 403 us                                                 | 430 us: 1.07x slower                                                   |
| meteor_contest                   | 69.1 ms                                                | 74.6 ms: 1.08x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 382 ms: 1.10x slower                                                   |
| create_gc_cycles                 | 1.15 ms                                                | 1.28 ms: 1.12x slower                                                  |
| fannkuch                         | 250 ms                                                 | 284 ms: 1.13x slower                                                   |
| telco                            | 3.92 ms                                                | 4.47 ms: 1.14x slower                                                  |
| json_dumps                       | 6.19 ms                                                | 7.12 ms: 1.15x slower                                                  |
| coverage                         | 38.5 ms                                                | 44.8 ms: 1.16x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 167 ms: 1.18x slower                                                   |
| regex_v8                         | 15.1 ms                                                | 18.0 ms: 1.19x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 124 ms: 2.65x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.13x faster                                                           |

Benchmark hidden because not significant (4): asyncio_websockets, connected_components, crypto_pyaes, json
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.127x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.12x