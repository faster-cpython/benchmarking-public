# Results vs. 3.12.0

- fork: faster-cpython
- ref: use_stackrefs
- machine: darwin-arm64
- commit hash: 3e929d7
- commit date: 2025-02-28
- overall geometric mean: 1.012x faster
- HPT reliability: 85.74%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 173 ms: 1.03x slower                                                      |
| docutils       | 1.45 sec                                               | 1.50 sec: 1.03x slower                                                    |
| html5lib       | 33.4 ms                                                | 32.3 ms: 1.03x faster                                                     |
| sphinx         | 613 ms                                                 | 599 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.00x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 385 ms: 1.75x faster                                                      |
| async_tree_eager_io              | 666 ms                                                 | 384 ms: 1.73x faster                                                      |
| async_tree_io                    | 672 ms                                                 | 400 ms: 1.68x faster                                                      |
| async_tree_eager_io_tg           | 617 ms                                                 | 395 ms: 1.56x faster                                                      |
| async_tree_none_tg               | 255 ms                                                 | 165 ms: 1.55x faster                                                      |
| async_tree_memoization_tg        | 318 ms                                                 | 206 ms: 1.55x faster                                                      |
| async_tree_none                  | 263 ms                                                 | 172 ms: 1.53x faster                                                      |
| async_tree_memoization           | 310 ms                                                 | 209 ms: 1.49x faster                                                      |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 424 ms: 1.25x faster                                                      |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 426 ms: 1.24x faster                                                      |
| async_generators                 | 299 ms                                                 | 262 ms: 1.14x faster                                                      |
| async_tree_eager_memoization     | 168 ms                                                 | 149 ms: 1.13x faster                                                      |
| coroutines                       | 19.7 ms                                                | 17.6 ms: 1.12x faster                                                     |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 363 ms: 1.03x faster                                                      |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                      |
| async_tree_eager                 | 65.8 ms                                                | 67.3 ms: 1.02x slower                                                     |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 404 ms: 1.16x slower                                                      |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 187 ms: 1.32x slower                                                      |
| async_tree_eager_tg              | 46.9 ms                                                | 140 ms: 2.99x slower                                                      |
| Geometric mean                   | (ref)                                                  | 1.17x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 53.0 ms: 1.02x faster                                                     |
| pidigits       | 283 ms                                                 | 283 ms: 1.00x slower                                                      |
| nbody          | 67.6 ms                                                | 79.9 ms: 1.18x slower                                                     |
| Geometric mean | (ref)                                                  | 1.05x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.29 ms: 1.06x faster                                                     |
| regex_dna      | 143 ms                                                 | 141 ms: 1.01x faster                                                      |
| regex_compile  | 75.9 ms                                                | 75.5 ms: 1.01x faster                                                     |
| regex_v8       | 15.1 ms                                                | 16.9 ms: 1.12x slower                                                     |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 102 ms: 1.06x faster                                                      |
| xml_etree_iterparse  | 75.5 ms                                                | 73.4 ms: 1.03x faster                                                     |
| xml_etree_generate   | 55.4 ms                                                | 56.6 ms: 1.02x slower                                                     |
| json_loads           | 17.0 us                                                | 17.6 us: 1.03x slower                                                     |
| tomli_loads          | 1.36 sec                                               | 1.43 sec: 1.05x slower                                                    |
| xml_etree_process    | 38.9 ms                                                | 40.9 ms: 1.05x slower                                                     |
| pickle_pure_python   | 197 us                                                 | 223 us: 1.13x slower                                                      |
| unpickle_pure_python | 145 us                                                 | 168 us: 1.16x slower                                                      |
| json_dumps           | 6.19 ms                                                | 7.45 ms: 1.20x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.06x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 13.2 ms                                                | 11.8 ms: 1.12x faster                                                     |
| python_startup         | 17.8 ms                                                | 16.6 ms: 1.07x faster                                                     |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 14.7 ms                                                | 15.4 ms: 1.05x slower                                                     |
| genshi_xml      | 30.5 ms                                                | 32.0 ms: 1.05x slower                                                     |
| mako            | 7.44 ms                                                | 7.81 ms: 1.05x slower                                                     |
| django_template | 19.7 ms                                                | 22.7 ms: 1.15x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.07x slower                                                              |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 12.7 ms: 2.54x faster                                                     |
| async_tree_io_tg                 | 673 ms                                                 | 385 ms: 1.75x faster                                                      |
| async_tree_eager_io              | 666 ms                                                 | 384 ms: 1.73x faster                                                      |
| async_tree_io                    | 672 ms                                                 | 400 ms: 1.68x faster                                                      |
| async_tree_eager_io_tg           | 617 ms                                                 | 395 ms: 1.56x faster                                                      |
| async_tree_none_tg               | 255 ms                                                 | 165 ms: 1.55x faster                                                      |
| async_tree_memoization_tg        | 318 ms                                                 | 206 ms: 1.55x faster                                                      |
| async_tree_none                  | 263 ms                                                 | 172 ms: 1.53x faster                                                      |
| async_tree_memoization           | 310 ms                                                 | 209 ms: 1.49x faster                                                      |
| deepcopy                         | 226 us                                                 | 164 us: 1.38x faster                                                      |
| deepcopy_memo                    | 26.0 us                                                | 20.3 us: 1.28x faster                                                     |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 424 ms: 1.25x faster                                                      |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 426 ms: 1.24x faster                                                      |
| deepcopy_reduce                  | 2.01 us                                                | 1.71 us: 1.18x faster                                                     |
| generators                       | 29.4 ms                                                | 24.9 ms: 1.18x faster                                                     |
| async_generators                 | 299 ms                                                 | 262 ms: 1.14x faster                                                      |
| async_tree_eager_memoization     | 168 ms                                                 | 149 ms: 1.13x faster                                                      |
| coroutines                       | 19.7 ms                                                | 17.6 ms: 1.12x faster                                                     |
| python_startup_no_site           | 13.2 ms                                                | 11.8 ms: 1.12x faster                                                     |
| bench_mp_pool                    | 65.5 ms                                                | 59.7 ms: 1.10x faster                                                     |
| k_core                           | 1.72 sec                                               | 1.58 sec: 1.09x faster                                                    |
| comprehensions                   | 14.0 us                                                | 12.9 us: 1.09x faster                                                     |
| pylint                           | 182 ms                                                 | 168 ms: 1.08x faster                                                      |
| python_startup                   | 17.8 ms                                                | 16.6 ms: 1.07x faster                                                     |
| regex_effbot                     | 2.44 ms                                                | 2.29 ms: 1.06x faster                                                     |
| go                               | 98.5 ms                                                | 93.0 ms: 1.06x faster                                                     |
| xml_etree_parse                  | 108 ms                                                 | 102 ms: 1.06x faster                                                      |
| raytrace                         | 204 ms                                                 | 193 ms: 1.05x faster                                                      |
| pathlib                          | 24.7 ms                                                | 23.5 ms: 1.05x faster                                                     |
| html5lib                         | 33.4 ms                                                | 32.3 ms: 1.03x faster                                                     |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 363 ms: 1.03x faster                                                      |
| thrift                           | 468 us                                                 | 454 us: 1.03x faster                                                      |
| xml_etree_iterparse              | 75.5 ms                                                | 73.4 ms: 1.03x faster                                                     |
| sphinx                           | 613 ms                                                 | 599 ms: 1.02x faster                                                      |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.07 ms: 1.02x faster                                                     |
| float                            | 54.1 ms                                                | 53.0 ms: 1.02x faster                                                     |
| logging_silent                   | 72.5 ns                                                | 71.4 ns: 1.02x faster                                                     |
| dask                             | 779 ms                                                 | 769 ms: 1.01x faster                                                      |
| regex_dna                        | 143 ms                                                 | 141 ms: 1.01x faster                                                      |
| dulwich_log                      | 29.2 ms                                                | 29.0 ms: 1.01x faster                                                     |
| sqlalchemy_declarative           | 61.9 ms                                                | 61.5 ms: 1.01x faster                                                     |
| regex_compile                    | 75.9 ms                                                | 75.5 ms: 1.01x faster                                                     |
| sqlite_synth                     | 1.55 us                                                | 1.54 us: 1.01x faster                                                     |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                      |
| pidigits                         | 283 ms                                                 | 283 ms: 1.00x slower                                                      |
| logging_simple                   | 3.60 us                                                | 3.62 us: 1.00x slower                                                     |
| logging_format                   | 3.90 us                                                | 3.92 us: 1.00x slower                                                     |
| bpe_tokeniser                    | 3.28 sec                                               | 3.32 sec: 1.01x slower                                                    |
| sympy_sum                        | 76.2 ms                                                | 77.5 ms: 1.02x slower                                                     |
| xml_etree_generate               | 55.4 ms                                                | 56.6 ms: 1.02x slower                                                     |
| async_tree_eager                 | 65.8 ms                                                | 67.3 ms: 1.02x slower                                                     |
| mdp                              | 1.49 sec                                               | 1.53 sec: 1.02x slower                                                    |
| 2to3                             | 168 ms                                                 | 173 ms: 1.03x slower                                                      |
| docutils                         | 1.45 sec                                               | 1.50 sec: 1.03x slower                                                    |
| scimark_fft                      | 194 ms                                                 | 200 ms: 1.03x slower                                                      |
| json_loads                       | 17.0 us                                                | 17.6 us: 1.03x slower                                                     |
| sympy_str                        | 144 ms                                                 | 149 ms: 1.03x slower                                                      |
| deltablue                        | 2.57 ms                                                | 2.66 ms: 1.04x slower                                                     |
| scimark_sor                      | 85.8 ms                                                | 89.1 ms: 1.04x slower                                                     |
| spectral_norm                    | 76.5 ms                                                | 79.5 ms: 1.04x slower                                                     |
| pycparser                        | 673 ms                                                 | 700 ms: 1.04x slower                                                      |
| sqlglot_optimize                 | 33.2 ms                                                | 34.6 ms: 1.04x slower                                                     |
| pprint_pformat                   | 986 ms                                                 | 1.03 sec: 1.04x slower                                                    |
| sqlalchemy_imperative            | 6.60 ms                                                | 6.88 ms: 1.04x slower                                                     |
| genshi_text                      | 14.7 ms                                                | 15.4 ms: 1.05x slower                                                     |
| genshi_xml                       | 30.5 ms                                                | 32.0 ms: 1.05x slower                                                     |
| mako                             | 7.44 ms                                                | 7.81 ms: 1.05x slower                                                     |
| tomli_loads                      | 1.36 sec                                               | 1.43 sec: 1.05x slower                                                    |
| gc_traversal                     | 2.95 ms                                                | 3.10 ms: 1.05x slower                                                     |
| sqlglot_normalize                | 180 ms                                                 | 189 ms: 1.05x slower                                                      |
| xml_etree_process                | 38.9 ms                                                | 40.9 ms: 1.05x slower                                                     |
| pprint_safe_repr                 | 483 ms                                                 | 509 ms: 1.05x slower                                                      |
| sqlglot_parse                    | 808 us                                                 | 856 us: 1.06x slower                                                      |
| chaos                            | 41.6 ms                                                | 44.1 ms: 1.06x slower                                                     |
| shortest_path                    | 331 ms                                                 | 351 ms: 1.06x slower                                                      |
| sympy_expand                     | 233 ms                                                 | 249 ms: 1.06x slower                                                      |
| sqlglot_transpile                | 973 us                                                 | 1.04 ms: 1.06x slower                                                     |
| scimark_monte_carlo              | 44.5 ms                                                | 47.5 ms: 1.07x slower                                                     |
| sympy_integrate                  | 11.1 ms                                                | 12.1 ms: 1.09x slower                                                     |
| bench_thread_pool                | 483 us                                                 | 528 us: 1.09x slower                                                      |
| connected_components             | 300 ms                                                 | 328 ms: 1.10x slower                                                      |
| typing_runtime_protocols         | 91.5 us                                                | 101 us: 1.10x slower                                                      |
| create_gc_cycles                 | 1.15 ms                                                | 1.27 ms: 1.11x slower                                                     |
| scimark_lu                       | 73.5 ms                                                | 81.8 ms: 1.11x slower                                                     |
| regex_v8                         | 15.1 ms                                                | 16.9 ms: 1.12x slower                                                     |
| meteor_contest                   | 69.1 ms                                                | 77.5 ms: 1.12x slower                                                     |
| pyflate                          | 311 ms                                                 | 352 ms: 1.13x slower                                                      |
| pickle_pure_python               | 197 us                                                 | 223 us: 1.13x slower                                                      |
| hexiom                           | 4.38 ms                                                | 4.96 ms: 1.13x slower                                                     |
| many_optionals                   | 403 us                                                 | 462 us: 1.15x slower                                                      |
| django_template                  | 19.7 ms                                                | 22.7 ms: 1.15x slower                                                     |
| unpickle_pure_python             | 145 us                                                 | 168 us: 1.16x slower                                                      |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 404 ms: 1.16x slower                                                      |
| nqueens                          | 59.5 ms                                                | 69.2 ms: 1.16x slower                                                     |
| nbody                            | 67.6 ms                                                | 79.9 ms: 1.18x slower                                                     |
| telco                            | 3.92 ms                                                | 4.66 ms: 1.19x slower                                                     |
| crypto_pyaes                     | 51.4 ms                                                | 61.5 ms: 1.20x slower                                                     |
| json_dumps                       | 6.19 ms                                                | 7.45 ms: 1.20x slower                                                     |
| richards_super                   | 34.6 ms                                                | 41.8 ms: 1.21x slower                                                     |
| coverage                         | 38.5 ms                                                | 47.1 ms: 1.22x slower                                                     |
| richards                         | 30.6 ms                                                | 37.5 ms: 1.23x slower                                                     |
| fannkuch                         | 250 ms                                                 | 309 ms: 1.23x slower                                                      |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 187 ms: 1.32x slower                                                      |
| async_tree_eager_tg              | 46.9 ms                                                | 140 ms: 2.99x slower                                                      |
| Geometric mean                   | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (1): json
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.012x faster

# HPT report

- Reliability score: 85.74% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.13x