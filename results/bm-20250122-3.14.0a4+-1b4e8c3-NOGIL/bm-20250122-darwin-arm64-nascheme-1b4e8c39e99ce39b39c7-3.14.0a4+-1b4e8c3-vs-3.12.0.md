# Results vs. 3.12.0

- fork: nascheme
- ref: 1b4e8c39e99ce39b39c7
- machine: darwin-arm64
- commit hash: 1b4e8c3
- commit date: 2025-01-22
- overall geometric mean: 1.032x faster
- HPT reliability: 55.38%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250122-darwin-arm64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 183 ms: 1.09x slower                                                     |
| docutils       | 1.45 sec                                               | 1.40 sec: 1.04x faster                                                   |
| html5lib       | 33.4 ms                                                | 31.0 ms: 1.08x faster                                                    |
| sphinx         | 613 ms                                                 | 597 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                  | 1.01x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250122-darwin-arm64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 306 ms: 2.20x faster                                                     |
| async_tree_eager_io              | 666 ms                                                 | 316 ms: 2.11x faster                                                     |
| async_tree_eager_io_tg           | 617 ms                                                 | 295 ms: 2.09x faster                                                     |
| async_tree_io                    | 672 ms                                                 | 331 ms: 2.03x faster                                                     |
| async_tree_none_tg               | 255 ms                                                 | 134 ms: 1.90x faster                                                     |
| async_tree_memoization_tg        | 318 ms                                                 | 173 ms: 1.84x faster                                                     |
| async_tree_none                  | 263 ms                                                 | 159 ms: 1.65x faster                                                     |
| async_tree_memoization           | 310 ms                                                 | 197 ms: 1.58x faster                                                     |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 382 ms: 1.38x faster                                                     |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 405 ms: 1.30x faster                                                     |
| coroutines                       | 19.7 ms                                                | 16.8 ms: 1.17x faster                                                    |
| async_generators                 | 299 ms                                                 | 259 ms: 1.15x faster                                                     |
| async_tree_eager_memoization     | 168 ms                                                 | 152 ms: 1.10x faster                                                     |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 131 ms: 1.09x faster                                                     |
| asyncio_websockets               | 243 ms                                                 | 237 ms: 1.03x faster                                                     |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 369 ms: 1.01x faster                                                     |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 344 ms: 1.01x faster                                                     |
| async_tree_eager_tg              | 46.9 ms                                                | 56.0 ms: 1.19x slower                                                    |
| async_tree_eager                 | 65.8 ms                                                | 82.1 ms: 1.25x slower                                                    |
| Geometric mean                   | (ref)                                                  | 1.36x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250122-darwin-arm64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 47.1 ms: 1.15x faster                                                    |
| pidigits       | 283 ms                                                 | 280 ms: 1.01x faster                                                     |
| nbody          | 67.6 ms                                                | 87.1 ms: 1.29x slower                                                    |
| Geometric mean | (ref)                                                  | 1.04x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250122-darwin-arm64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.08 ms: 1.17x faster                                                    |
| regex_dna      | 143 ms                                                 | 137 ms: 1.04x faster                                                     |
| regex_compile  | 75.9 ms                                                | 75.0 ms: 1.01x faster                                                    |
| regex_v8       | 15.1 ms                                                | 15.4 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                  | 1.05x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250122-darwin-arm64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_loads           | 17.0 us                                                | 17.7 us: 1.04x slower                                                    |
| unpickle_pure_python | 145 us                                                 | 153 us: 1.05x slower                                                     |
| pickle_pure_python   | 197 us                                                 | 222 us: 1.13x slower                                                     |
| json_dumps           | 6.19 ms                                                | 7.65 ms: 1.24x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.09x slower                                                             |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250122-darwin-arm64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 20.7 ms: 1.17x slower                                                    |
| python_startup_no_site | 13.2 ms                                                | 16.1 ms: 1.22x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.20x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250122-darwin-arm64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 30.5 ms                                                | 32.3 ms: 1.06x slower                                                    |
| genshi_text     | 14.7 ms                                                | 15.9 ms: 1.08x slower                                                    |
| django_template | 19.7 ms                                                | 24.0 ms: 1.22x slower                                                    |
| mako            | 7.44 ms                                                | 9.96 ms: 1.34x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.17x slower                                                             |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250122-darwin-arm64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 12.8 ms: 2.52x faster                                                    |
| async_tree_io_tg                 | 673 ms                                                 | 306 ms: 2.20x faster                                                     |
| async_tree_eager_io              | 666 ms                                                 | 316 ms: 2.11x faster                                                     |
| async_tree_eager_io_tg           | 617 ms                                                 | 295 ms: 2.09x faster                                                     |
| async_tree_io                    | 672 ms                                                 | 331 ms: 2.03x faster                                                     |
| async_tree_none_tg               | 255 ms                                                 | 134 ms: 1.90x faster                                                     |
| async_tree_memoization_tg        | 318 ms                                                 | 173 ms: 1.84x faster                                                     |
| async_tree_none                  | 263 ms                                                 | 159 ms: 1.65x faster                                                     |
| async_tree_memoization           | 310 ms                                                 | 197 ms: 1.58x faster                                                     |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 382 ms: 1.38x faster                                                     |
| deepcopy                         | 226 us                                                 | 172 us: 1.31x faster                                                     |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 405 ms: 1.30x faster                                                     |
| generators                       | 29.4 ms                                                | 24.0 ms: 1.22x faster                                                    |
| deepcopy_memo                    | 26.0 us                                                | 21.5 us: 1.21x faster                                                    |
| regex_effbot                     | 2.44 ms                                                | 2.08 ms: 1.17x faster                                                    |
| sqlite_synth                     | 1.55 us                                                | 1.32 us: 1.17x faster                                                    |
| coroutines                       | 19.7 ms                                                | 16.8 ms: 1.17x faster                                                    |
| async_generators                 | 299 ms                                                 | 259 ms: 1.15x faster                                                     |
| float                            | 54.1 ms                                                | 47.1 ms: 1.15x faster                                                    |
| deepcopy_reduce                  | 2.01 us                                                | 1.78 us: 1.13x faster                                                    |
| async_tree_eager_memoization     | 168 ms                                                 | 152 ms: 1.10x faster                                                     |
| bpe_tokeniser                    | 3.28 sec                                               | 3.01 sec: 1.09x faster                                                   |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 131 ms: 1.09x faster                                                     |
| create_gc_cycles                 | 1.15 ms                                                | 1.06 ms: 1.08x faster                                                    |
| pylint                           | 182 ms                                                 | 168 ms: 1.08x faster                                                     |
| pathlib                          | 24.7 ms                                                | 22.8 ms: 1.08x faster                                                    |
| go                               | 98.5 ms                                                | 91.2 ms: 1.08x faster                                                    |
| html5lib                         | 33.4 ms                                                | 31.0 ms: 1.08x faster                                                    |
| k_core                           | 1.72 sec                                               | 1.62 sec: 1.07x faster                                                   |
| pycparser                        | 673 ms                                                 | 633 ms: 1.06x faster                                                     |
| comprehensions                   | 14.0 us                                                | 13.3 us: 1.06x faster                                                    |
| spectral_norm                    | 76.5 ms                                                | 72.6 ms: 1.05x faster                                                    |
| docutils                         | 1.45 sec                                               | 1.40 sec: 1.04x faster                                                   |
| regex_dna                        | 143 ms                                                 | 137 ms: 1.04x faster                                                     |
| sphinx                           | 613 ms                                                 | 597 ms: 1.03x faster                                                     |
| asyncio_websockets               | 243 ms                                                 | 237 ms: 1.03x faster                                                     |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 369 ms: 1.01x faster                                                     |
| pyflate                          | 311 ms                                                 | 307 ms: 1.01x faster                                                     |
| regex_compile                    | 75.9 ms                                                | 75.0 ms: 1.01x faster                                                    |
| json                             | 3.00 ms                                                | 2.97 ms: 1.01x faster                                                    |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 344 ms: 1.01x faster                                                     |
| pidigits                         | 283 ms                                                 | 280 ms: 1.01x faster                                                     |
| nqueens                          | 59.5 ms                                                | 60.2 ms: 1.01x slower                                                    |
| bench_mp_pool                    | 65.5 ms                                                | 66.3 ms: 1.01x slower                                                    |
| logging_simple                   | 3.60 us                                                | 3.66 us: 1.02x slower                                                    |
| regex_v8                         | 15.1 ms                                                | 15.4 ms: 1.02x slower                                                    |
| sqlglot_optimize                 | 33.2 ms                                                | 34.4 ms: 1.03x slower                                                    |
| raytrace                         | 204 ms                                                 | 211 ms: 1.04x slower                                                     |
| chaos                            | 41.6 ms                                                | 43.1 ms: 1.04x slower                                                    |
| json_loads                       | 17.0 us                                                | 17.7 us: 1.04x slower                                                    |
| logging_format                   | 3.90 us                                                | 4.07 us: 1.04x slower                                                    |
| sqlglot_normalize                | 180 ms                                                 | 188 ms: 1.04x slower                                                     |
| sympy_sum                        | 76.2 ms                                                | 79.8 ms: 1.05x slower                                                    |
| scimark_sor                      | 85.8 ms                                                | 90.2 ms: 1.05x slower                                                    |
| mdp                              | 1.49 sec                                               | 1.57 sec: 1.05x slower                                                   |
| unpickle_pure_python             | 145 us                                                 | 153 us: 1.05x slower                                                     |
| shortest_path                    | 331 ms                                                 | 349 ms: 1.06x slower                                                     |
| genshi_xml                       | 30.5 ms                                                | 32.3 ms: 1.06x slower                                                    |
| thrift                           | 468 us                                                 | 496 us: 1.06x slower                                                     |
| sqlalchemy_declarative           | 61.9 ms                                                | 66.9 ms: 1.08x slower                                                    |
| scimark_fft                      | 194 ms                                                 | 210 ms: 1.08x slower                                                     |
| genshi_text                      | 14.7 ms                                                | 15.9 ms: 1.08x slower                                                    |
| sympy_str                        | 144 ms                                                 | 156 ms: 1.09x slower                                                     |
| 2to3                             | 168 ms                                                 | 183 ms: 1.09x slower                                                     |
| connected_components             | 300 ms                                                 | 326 ms: 1.09x slower                                                     |
| sqlglot_parse                    | 808 us                                                 | 881 us: 1.09x slower                                                     |
| logging_silent                   | 72.5 ns                                                | 79.3 ns: 1.09x slower                                                    |
| sqlglot_transpile                | 973 us                                                 | 1.07 ms: 1.09x slower                                                    |
| hexiom                           | 4.38 ms                                                | 4.80 ms: 1.10x slower                                                    |
| sqlalchemy_imperative            | 6.60 ms                                                | 7.26 ms: 1.10x slower                                                    |
| sympy_integrate                  | 11.1 ms                                                | 12.2 ms: 1.11x slower                                                    |
| pprint_pformat                   | 986 ms                                                 | 1.10 sec: 1.11x slower                                                   |
| deltablue                        | 2.57 ms                                                | 2.86 ms: 1.12x slower                                                    |
| pprint_safe_repr                 | 483 ms                                                 | 541 ms: 1.12x slower                                                     |
| scimark_monte_carlo              | 44.5 ms                                                | 49.9 ms: 1.12x slower                                                    |
| pickle_pure_python               | 197 us                                                 | 222 us: 1.13x slower                                                     |
| fannkuch                         | 250 ms                                                 | 283 ms: 1.13x slower                                                     |
| sympy_expand                     | 233 ms                                                 | 264 ms: 1.13x slower                                                     |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.56 ms: 1.13x slower                                                    |
| many_optionals                   | 403 us                                                 | 456 us: 1.13x slower                                                     |
| crypto_pyaes                     | 51.4 ms                                                | 58.7 ms: 1.14x slower                                                    |
| meteor_contest                   | 69.1 ms                                                | 79.0 ms: 1.14x slower                                                    |
| richards_super                   | 34.6 ms                                                | 40.3 ms: 1.16x slower                                                    |
| richards                         | 30.6 ms                                                | 35.6 ms: 1.17x slower                                                    |
| python_startup                   | 17.8 ms                                                | 20.7 ms: 1.17x slower                                                    |
| async_tree_eager_tg              | 46.9 ms                                                | 56.0 ms: 1.19x slower                                                    |
| scimark_lu                       | 73.5 ms                                                | 88.2 ms: 1.20x slower                                                    |
| django_template                  | 19.7 ms                                                | 24.0 ms: 1.22x slower                                                    |
| python_startup_no_site           | 13.2 ms                                                | 16.1 ms: 1.22x slower                                                    |
| json_dumps                       | 6.19 ms                                                | 7.65 ms: 1.24x slower                                                    |
| typing_runtime_protocols         | 91.5 us                                                | 113 us: 1.24x slower                                                     |
| async_tree_eager                 | 65.8 ms                                                | 82.1 ms: 1.25x slower                                                    |
| telco                            | 3.92 ms                                                | 4.94 ms: 1.26x slower                                                    |
| gc_traversal                     | 2.95 ms                                                | 3.74 ms: 1.27x slower                                                    |
| nbody                            | 67.6 ms                                                | 87.1 ms: 1.29x slower                                                    |
| mako                             | 7.44 ms                                                | 9.96 ms: 1.34x slower                                                    |
| coverage                         | 38.5 ms                                                | 54.2 ms: 1.41x slower                                                    |
| bench_thread_pool                | 483 us                                                 | 788 us: 1.63x slower                                                     |
| Geometric mean                   | (ref)                                                  | 1.03x faster                                                             |

Benchmark hidden because not significant (2): dulwich_log, tomli_loads
Ignored benchmarks (10) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http, xml_etree_generate, xml_etree_iterparse, xml_etree_parse, xml_etree_process

- Geometric mean (including insignificant results): 1.032x faster

# HPT report

- Reliability score: 55.38% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.17x