# Results vs. 3.12.0

- fork: mdboom
- ref: aa_test_2025_2
- machine: darwin-arm64
- commit hash: 8ffb2c1
- commit date: 2025-01-23
- overall geometric mean: 1.068x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 195 ms: 1.16x slower                                             |
| docutils       | 1.45 sec                                               | 1.45 sec: 1.00x faster                                           |
| html5lib       | 33.4 ms                                                | 31.2 ms: 1.07x faster                                            |
| sphinx         | 613 ms                                                 | 582 ms: 1.05x faster                                             |
| Geometric mean | (ref)                                                  | 1.01x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 373 ms: 1.80x faster                                             |
| async_tree_io                    | 672 ms                                                 | 378 ms: 1.78x faster                                             |
| async_tree_eager_io              | 666 ms                                                 | 376 ms: 1.77x faster                                             |
| async_tree_memoization_tg        | 318 ms                                                 | 190 ms: 1.67x faster                                             |
| async_tree_none_tg               | 255 ms                                                 | 153 ms: 1.66x faster                                             |
| async_tree_none                  | 263 ms                                                 | 160 ms: 1.65x faster                                             |
| async_tree_eager_io_tg           | 617 ms                                                 | 394 ms: 1.57x faster                                             |
| async_tree_memoization           | 310 ms                                                 | 203 ms: 1.53x faster                                             |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 411 ms: 1.28x faster                                             |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 417 ms: 1.26x faster                                             |
| coroutines                       | 19.7 ms                                                | 16.0 ms: 1.23x faster                                            |
| async_generators                 | 299 ms                                                 | 250 ms: 1.19x faster                                             |
| async_tree_eager_memoization     | 168 ms                                                 | 141 ms: 1.19x faster                                             |
| async_tree_eager                 | 65.8 ms                                                | 62.0 ms: 1.06x faster                                            |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 359 ms: 1.04x faster                                             |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                             |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 389 ms: 1.12x slower                                             |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 170 ms: 1.20x slower                                             |
| async_tree_eager_tg              | 46.9 ms                                                | 127 ms: 2.70x slower                                             |
| Geometric mean                   | (ref)                                                  | 1.23x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 54.1 ms                                                | 48.6 ms: 1.11x faster                                            |
| pidigits       | 283 ms                                                 | 283 ms: 1.00x slower                                             |
| nbody          | 67.6 ms                                                | 68.4 ms: 1.01x slower                                            |
| Geometric mean | (ref)                                                  | 1.03x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 66.9 ms: 1.13x faster                                            |
| regex_effbot   | 2.44 ms                                                | 2.27 ms: 1.08x faster                                            |
| regex_dna      | 143 ms                                                 | 141 ms: 1.01x faster                                             |
| regex_v8       | 15.1 ms                                                | 16.8 ms: 1.11x slower                                            |
| Geometric mean | (ref)                                                  | 1.03x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                               | 1.20 sec: 1.13x faster                                           |
| xml_etree_iterparse  | 75.5 ms                                                | 71.2 ms: 1.06x faster                                            |
| xml_etree_parse      | 108 ms                                                 | 102 ms: 1.05x faster                                             |
| xml_etree_generate   | 55.4 ms                                                | 53.2 ms: 1.04x faster                                            |
| json_loads           | 17.0 us                                                | 16.6 us: 1.02x faster                                            |
| unpickle_pure_python | 145 us                                                 | 147 us: 1.01x slower                                             |
| xml_etree_process    | 38.9 ms                                                | 41.0 ms: 1.05x slower                                            |
| json_dumps           | 6.19 ms                                                | 7.48 ms: 1.21x slower                                            |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                     |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 19.3 ms: 1.09x slower                                            |
| python_startup_no_site | 13.2 ms                                                | 14.4 ms: 1.10x slower                                            |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 7.44 ms                                                | 6.99 ms: 1.06x faster                                            |
| genshi_xml      | 30.5 ms                                                | 28.8 ms: 1.06x faster                                            |
| genshi_text     | 14.7 ms                                                | 14.5 ms: 1.01x faster                                            |
| django_template | 19.7 ms                                                | 21.3 ms: 1.08x slower                                            |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                     |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 12.3 ms: 2.61x faster                                            |
| async_tree_io_tg                 | 673 ms                                                 | 373 ms: 1.80x faster                                             |
| async_tree_io                    | 672 ms                                                 | 378 ms: 1.78x faster                                             |
| async_tree_eager_io              | 666 ms                                                 | 376 ms: 1.77x faster                                             |
| async_tree_memoization_tg        | 318 ms                                                 | 190 ms: 1.67x faster                                             |
| async_tree_none_tg               | 255 ms                                                 | 153 ms: 1.66x faster                                             |
| async_tree_none                  | 263 ms                                                 | 160 ms: 1.65x faster                                             |
| async_tree_eager_io_tg           | 617 ms                                                 | 394 ms: 1.57x faster                                             |
| async_tree_memoization           | 310 ms                                                 | 203 ms: 1.53x faster                                             |
| deepcopy                         | 226 us                                                 | 149 us: 1.52x faster                                             |
| deepcopy_memo                    | 26.0 us                                                | 18.0 us: 1.45x faster                                            |
| generators                       | 29.4 ms                                                | 22.4 ms: 1.31x faster                                            |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 411 ms: 1.28x faster                                             |
| deepcopy_reduce                  | 2.01 us                                                | 1.57 us: 1.28x faster                                            |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 417 ms: 1.26x faster                                             |
| spectral_norm                    | 76.5 ms                                                | 60.8 ms: 1.26x faster                                            |
| coroutines                       | 19.7 ms                                                | 16.0 ms: 1.23x faster                                            |
| async_generators                 | 299 ms                                                 | 250 ms: 1.19x faster                                             |
| async_tree_eager_memoization     | 168 ms                                                 | 141 ms: 1.19x faster                                             |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 2.69 ms: 1.17x faster                                            |
| k_core                           | 1.72 sec                                               | 1.51 sec: 1.14x faster                                           |
| regex_compile                    | 75.9 ms                                                | 66.9 ms: 1.13x faster                                            |
| tomli_loads                      | 1.36 sec                                               | 1.20 sec: 1.13x faster                                           |
| pylint                           | 182 ms                                                 | 162 ms: 1.12x faster                                             |
| go                               | 98.5 ms                                                | 87.9 ms: 1.12x faster                                            |
| scimark_fft                      | 194 ms                                                 | 174 ms: 1.12x faster                                             |
| float                            | 54.1 ms                                                | 48.6 ms: 1.11x faster                                            |
| bpe_tokeniser                    | 3.28 sec                                               | 2.95 sec: 1.11x faster                                           |
| comprehensions                   | 14.0 us                                                | 12.9 us: 1.09x faster                                            |
| bench_mp_pool                    | 65.5 ms                                                | 60.5 ms: 1.08x faster                                            |
| logging_format                   | 3.90 us                                                | 3.62 us: 1.08x faster                                            |
| logging_simple                   | 3.60 us                                                | 3.35 us: 1.08x faster                                            |
| regex_effbot                     | 2.44 ms                                                | 2.27 ms: 1.08x faster                                            |
| pathlib                          | 24.7 ms                                                | 23.0 ms: 1.07x faster                                            |
| html5lib                         | 33.4 ms                                                | 31.2 ms: 1.07x faster                                            |
| mako                             | 7.44 ms                                                | 6.99 ms: 1.06x faster                                            |
| dulwich_log                      | 29.2 ms                                                | 27.5 ms: 1.06x faster                                            |
| async_tree_eager                 | 65.8 ms                                                | 62.0 ms: 1.06x faster                                            |
| xml_etree_iterparse              | 75.5 ms                                                | 71.2 ms: 1.06x faster                                            |
| pprint_pformat                   | 986 ms                                                 | 930 ms: 1.06x faster                                             |
| genshi_xml                       | 30.5 ms                                                | 28.8 ms: 1.06x faster                                            |
| chaos                            | 41.6 ms                                                | 39.5 ms: 1.05x faster                                            |
| xml_etree_parse                  | 108 ms                                                 | 102 ms: 1.05x faster                                             |
| sphinx                           | 613 ms                                                 | 582 ms: 1.05x faster                                             |
| pprint_safe_repr                 | 483 ms                                                 | 462 ms: 1.05x faster                                             |
| json                             | 3.00 ms                                                | 2.87 ms: 1.05x faster                                            |
| xml_etree_generate               | 55.4 ms                                                | 53.2 ms: 1.04x faster                                            |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 359 ms: 1.04x faster                                             |
| pyflate                          | 311 ms                                                 | 300 ms: 1.04x faster                                             |
| pycparser                        | 673 ms                                                 | 652 ms: 1.03x faster                                             |
| nqueens                          | 59.5 ms                                                | 57.7 ms: 1.03x faster                                            |
| hexiom                           | 4.38 ms                                                | 4.24 ms: 1.03x faster                                            |
| sympy_str                        | 144 ms                                                 | 140 ms: 1.03x faster                                             |
| sympy_sum                        | 76.2 ms                                                | 74.2 ms: 1.03x faster                                            |
| json_loads                       | 17.0 us                                                | 16.6 us: 1.02x faster                                            |
| thrift                           | 468 us                                                 | 458 us: 1.02x faster                                             |
| sqlalchemy_declarative           | 61.9 ms                                                | 60.6 ms: 1.02x faster                                            |
| shortest_path                    | 331 ms                                                 | 324 ms: 1.02x faster                                             |
| fannkuch                         | 250 ms                                                 | 246 ms: 1.02x faster                                             |
| genshi_text                      | 14.7 ms                                                | 14.5 ms: 1.01x faster                                            |
| regex_dna                        | 143 ms                                                 | 141 ms: 1.01x faster                                             |
| dask                             | 779 ms                                                 | 771 ms: 1.01x faster                                             |
| connected_components             | 300 ms                                                 | 297 ms: 1.01x faster                                             |
| scimark_lu                       | 73.5 ms                                                | 72.8 ms: 1.01x faster                                            |
| sqlite_synth                     | 1.55 us                                                | 1.53 us: 1.01x faster                                            |
| scimark_sor                      | 85.8 ms                                                | 85.3 ms: 1.01x faster                                            |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                             |
| sqlglot_optimize                 | 33.2 ms                                                | 33.1 ms: 1.00x faster                                            |
| docutils                         | 1.45 sec                                               | 1.45 sec: 1.00x faster                                           |
| raytrace                         | 204 ms                                                 | 204 ms: 1.00x faster                                             |
| pidigits                         | 283 ms                                                 | 283 ms: 1.00x slower                                             |
| sqlglot_normalize                | 180 ms                                                 | 181 ms: 1.01x slower                                             |
| sympy_expand                     | 233 ms                                                 | 235 ms: 1.01x slower                                             |
| bench_thread_pool                | 483 us                                                 | 488 us: 1.01x slower                                             |
| nbody                            | 67.6 ms                                                | 68.4 ms: 1.01x slower                                            |
| sympy_integrate                  | 11.1 ms                                                | 11.2 ms: 1.01x slower                                            |
| unpickle_pure_python             | 145 us                                                 | 147 us: 1.01x slower                                             |
| mdp                              | 1.49 sec                                               | 1.52 sec: 1.02x slower                                           |
| sqlalchemy_imperative            | 6.60 ms                                                | 6.77 ms: 1.03x slower                                            |
| crypto_pyaes                     | 51.4 ms                                                | 53.0 ms: 1.03x slower                                            |
| meteor_contest                   | 69.1 ms                                                | 71.7 ms: 1.04x slower                                            |
| sqlglot_transpile                | 973 us                                                 | 1.01 ms: 1.04x slower                                            |
| sqlglot_parse                    | 808 us                                                 | 846 us: 1.05x slower                                             |
| xml_etree_process                | 38.9 ms                                                | 41.0 ms: 1.05x slower                                            |
| gc_traversal                     | 2.95 ms                                                | 3.11 ms: 1.06x slower                                            |
| deltablue                        | 2.57 ms                                                | 2.72 ms: 1.06x slower                                            |
| typing_runtime_protocols         | 91.5 us                                                | 97.6 us: 1.07x slower                                            |
| logging_silent                   | 72.5 ns                                                | 77.5 ns: 1.07x slower                                            |
| django_template                  | 19.7 ms                                                | 21.3 ms: 1.08x slower                                            |
| python_startup                   | 17.8 ms                                                | 19.3 ms: 1.09x slower                                            |
| python_startup_no_site           | 13.2 ms                                                | 14.4 ms: 1.10x slower                                            |
| richards_super                   | 34.6 ms                                                | 38.1 ms: 1.10x slower                                            |
| many_optionals                   | 403 us                                                 | 447 us: 1.11x slower                                             |
| create_gc_cycles                 | 1.15 ms                                                | 1.28 ms: 1.11x slower                                            |
| regex_v8                         | 15.1 ms                                                | 16.8 ms: 1.11x slower                                            |
| scimark_monte_carlo              | 44.5 ms                                                | 49.7 ms: 1.12x slower                                            |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 389 ms: 1.12x slower                                             |
| richards                         | 30.6 ms                                                | 34.3 ms: 1.12x slower                                            |
| telco                            | 3.92 ms                                                | 4.55 ms: 1.16x slower                                            |
| 2to3                             | 168 ms                                                 | 195 ms: 1.16x slower                                             |
| coverage                         | 38.5 ms                                                | 46.2 ms: 1.20x slower                                            |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 170 ms: 1.20x slower                                             |
| json_dumps                       | 6.19 ms                                                | 7.48 ms: 1.21x slower                                            |
| async_tree_eager_tg              | 46.9 ms                                                | 127 ms: 2.70x slower                                             |
| Geometric mean                   | (ref)                                                  | 1.07x faster                                                     |

Benchmark hidden because not significant (1): pickle_pure_python
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.068x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.10x