# Results vs. 3.12.0

- fork: faster-cpython
- ref: use_stackrefs_single
- machine: darwin-arm64
- commit hash: 916faf4
- commit date: 2025-03-07
- overall geometric mean: 1.014x slower
- HPT reliability: 97.94%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-darwin-arm64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 179 ms: 1.06x slower                                                             |
| docutils       | 1.45 sec                                               | 1.51 sec: 1.04x slower                                                           |
| html5lib       | 33.4 ms                                                | 32.6 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                     |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-darwin-arm64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 395 ms: 1.70x faster                                                             |
| async_tree_eager_io              | 666 ms                                                 | 395 ms: 1.69x faster                                                             |
| async_tree_io                    | 672 ms                                                 | 416 ms: 1.61x faster                                                             |
| async_tree_eager_io_tg           | 617 ms                                                 | 406 ms: 1.52x faster                                                             |
| async_tree_none_tg               | 255 ms                                                 | 170 ms: 1.50x faster                                                             |
| async_tree_memoization_tg        | 318 ms                                                 | 213 ms: 1.50x faster                                                             |
| async_tree_none                  | 263 ms                                                 | 178 ms: 1.48x faster                                                             |
| async_tree_memoization           | 310 ms                                                 | 218 ms: 1.42x faster                                                             |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 428 ms: 1.23x faster                                                             |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 430 ms: 1.22x faster                                                             |
| async_generators                 | 299 ms                                                 | 264 ms: 1.13x faster                                                             |
| async_tree_eager_memoization     | 168 ms                                                 | 152 ms: 1.10x faster                                                             |
| coroutines                       | 19.7 ms                                                | 18.0 ms: 1.09x faster                                                            |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 366 ms: 1.02x faster                                                             |
| async_tree_eager                 | 65.8 ms                                                | 70.3 ms: 1.07x slower                                                            |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 405 ms: 1.17x slower                                                             |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 191 ms: 1.35x slower                                                             |
| async_tree_eager_tg              | 46.9 ms                                                | 143 ms: 3.04x slower                                                             |
| Geometric mean                   | (ref)                                                  | 1.15x faster                                                                     |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-darwin-arm64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 283 ms                                                 | 284 ms: 1.00x slower                                                             |
| float          | 54.1 ms                                                | 56.4 ms: 1.04x slower                                                            |
| nbody          | 67.6 ms                                                | 90.5 ms: 1.34x slower                                                            |
| Geometric mean | (ref)                                                  | 1.12x slower                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-darwin-arm64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.29 ms: 1.06x faster                                                            |
| regex_dna      | 143 ms                                                 | 141 ms: 1.01x faster                                                             |
| regex_compile  | 75.9 ms                                                | 78.5 ms: 1.03x slower                                                            |
| regex_v8       | 15.1 ms                                                | 17.0 ms: 1.12x slower                                                            |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-darwin-arm64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 104 ms: 1.04x faster                                                             |
| xml_etree_iterparse  | 75.5 ms                                                | 73.9 ms: 1.02x faster                                                            |
| tomli_loads          | 1.36 sec                                               | 1.35 sec: 1.01x faster                                                           |
| xml_etree_generate   | 55.4 ms                                                | 58.1 ms: 1.05x slower                                                            |
| json_loads           | 17.0 us                                                | 17.9 us: 1.05x slower                                                            |
| xml_etree_process    | 38.9 ms                                                | 42.0 ms: 1.08x slower                                                            |
| unpickle_pure_python | 145 us                                                 | 173 us: 1.19x slower                                                             |
| pickle_pure_python   | 197 us                                                 | 237 us: 1.20x slower                                                             |
| json_dumps           | 6.19 ms                                                | 7.54 ms: 1.22x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.08x slower                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-darwin-arm64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 19.4 ms: 1.09x slower                                                            |
| python_startup_no_site | 13.2 ms                                                | 14.4 ms: 1.09x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-darwin-arm64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 30.5 ms                                                | 33.5 ms: 1.10x slower                                                            |
| genshi_text     | 14.7 ms                                                | 16.3 ms: 1.11x slower                                                            |
| mako            | 7.44 ms                                                | 8.64 ms: 1.16x slower                                                            |
| django_template | 19.7 ms                                                | 23.4 ms: 1.19x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.14x slower                                                                     |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-darwin-arm64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 12.8 ms: 2.51x faster                                                            |
| async_tree_io_tg                 | 673 ms                                                 | 395 ms: 1.70x faster                                                             |
| async_tree_eager_io              | 666 ms                                                 | 395 ms: 1.69x faster                                                             |
| async_tree_io                    | 672 ms                                                 | 416 ms: 1.61x faster                                                             |
| async_tree_eager_io_tg           | 617 ms                                                 | 406 ms: 1.52x faster                                                             |
| async_tree_none_tg               | 255 ms                                                 | 170 ms: 1.50x faster                                                             |
| async_tree_memoization_tg        | 318 ms                                                 | 213 ms: 1.50x faster                                                             |
| async_tree_none                  | 263 ms                                                 | 178 ms: 1.48x faster                                                             |
| async_tree_memoization           | 310 ms                                                 | 218 ms: 1.42x faster                                                             |
| deepcopy                         | 226 us                                                 | 172 us: 1.31x faster                                                             |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 428 ms: 1.23x faster                                                             |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 430 ms: 1.22x faster                                                             |
| deepcopy_memo                    | 26.0 us                                                | 22.7 us: 1.14x faster                                                            |
| deepcopy_reduce                  | 2.01 us                                                | 1.78 us: 1.13x faster                                                            |
| async_generators                 | 299 ms                                                 | 264 ms: 1.13x faster                                                             |
| async_tree_eager_memoization     | 168 ms                                                 | 152 ms: 1.10x faster                                                             |
| k_core                           | 1.72 sec                                               | 1.57 sec: 1.10x faster                                                           |
| coroutines                       | 19.7 ms                                                | 18.0 ms: 1.09x faster                                                            |
| bench_mp_pool                    | 65.5 ms                                                | 61.3 ms: 1.07x faster                                                            |
| regex_effbot                     | 2.44 ms                                                | 2.29 ms: 1.06x faster                                                            |
| generators                       | 29.4 ms                                                | 27.8 ms: 1.06x faster                                                            |
| spectral_norm                    | 76.5 ms                                                | 72.8 ms: 1.05x faster                                                            |
| comprehensions                   | 14.0 us                                                | 13.3 us: 1.05x faster                                                            |
| xml_etree_parse                  | 108 ms                                                 | 104 ms: 1.04x faster                                                             |
| pathlib                          | 24.7 ms                                                | 23.9 ms: 1.03x faster                                                            |
| html5lib                         | 33.4 ms                                                | 32.6 ms: 1.02x faster                                                            |
| raytrace                         | 204 ms                                                 | 199 ms: 1.02x faster                                                             |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 366 ms: 1.02x faster                                                             |
| xml_etree_iterparse              | 75.5 ms                                                | 73.9 ms: 1.02x faster                                                            |
| bpe_tokeniser                    | 3.28 sec                                               | 3.24 sec: 1.01x faster                                                           |
| dask                             | 779 ms                                                 | 769 ms: 1.01x faster                                                             |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.11 ms: 1.01x faster                                                            |
| regex_dna                        | 143 ms                                                 | 141 ms: 1.01x faster                                                             |
| sqlite_synth                     | 1.55 us                                                | 1.54 us: 1.01x faster                                                            |
| tomli_loads                      | 1.36 sec                                               | 1.35 sec: 1.01x faster                                                           |
| pidigits                         | 283 ms                                                 | 284 ms: 1.00x slower                                                             |
| dulwich_log                      | 29.2 ms                                                | 29.5 ms: 1.01x slower                                                            |
| json                             | 3.00 ms                                                | 3.04 ms: 1.01x slower                                                            |
| go                               | 98.5 ms                                                | 101 ms: 1.03x slower                                                             |
| sqlalchemy_declarative           | 61.9 ms                                                | 63.7 ms: 1.03x slower                                                            |
| logging_simple                   | 3.60 us                                                | 3.71 us: 1.03x slower                                                            |
| scimark_fft                      | 194 ms                                                 | 201 ms: 1.03x slower                                                             |
| shortest_path                    | 331 ms                                                 | 342 ms: 1.03x slower                                                             |
| regex_compile                    | 75.9 ms                                                | 78.5 ms: 1.03x slower                                                            |
| logging_format                   | 3.90 us                                                | 4.04 us: 1.04x slower                                                            |
| docutils                         | 1.45 sec                                               | 1.51 sec: 1.04x slower                                                           |
| sympy_sum                        | 76.2 ms                                                | 79.4 ms: 1.04x slower                                                            |
| float                            | 54.1 ms                                                | 56.4 ms: 1.04x slower                                                            |
| mdp                              | 1.49 sec                                               | 1.56 sec: 1.05x slower                                                           |
| xml_etree_generate               | 55.4 ms                                                | 58.1 ms: 1.05x slower                                                            |
| json_loads                       | 17.0 us                                                | 17.9 us: 1.05x slower                                                            |
| gc_traversal                     | 2.95 ms                                                | 3.10 ms: 1.05x slower                                                            |
| connected_components             | 300 ms                                                 | 315 ms: 1.05x slower                                                             |
| 2to3                             | 168 ms                                                 | 179 ms: 1.06x slower                                                             |
| sympy_str                        | 144 ms                                                 | 153 ms: 1.07x slower                                                             |
| sqlglot_optimize                 | 33.2 ms                                                | 35.5 ms: 1.07x slower                                                            |
| async_tree_eager                 | 65.8 ms                                                | 70.3 ms: 1.07x slower                                                            |
| sqlalchemy_imperative            | 6.60 ms                                                | 7.06 ms: 1.07x slower                                                            |
| bench_thread_pool                | 483 us                                                 | 519 us: 1.07x slower                                                             |
| scimark_sor                      | 85.8 ms                                                | 92.3 ms: 1.08x slower                                                            |
| logging_silent                   | 72.5 ns                                                | 78.4 ns: 1.08x slower                                                            |
| xml_etree_process                | 38.9 ms                                                | 42.0 ms: 1.08x slower                                                            |
| pycparser                        | 673 ms                                                 | 728 ms: 1.08x slower                                                             |
| scimark_lu                       | 73.5 ms                                                | 80.0 ms: 1.09x slower                                                            |
| python_startup                   | 17.8 ms                                                | 19.4 ms: 1.09x slower                                                            |
| sympy_expand                     | 233 ms                                                 | 255 ms: 1.09x slower                                                             |
| python_startup_no_site           | 13.2 ms                                                | 14.4 ms: 1.09x slower                                                            |
| pyflate                          | 311 ms                                                 | 340 ms: 1.09x slower                                                             |
| chaos                            | 41.6 ms                                                | 45.6 ms: 1.09x slower                                                            |
| sqlglot_normalize                | 180 ms                                                 | 197 ms: 1.10x slower                                                             |
| genshi_xml                       | 30.5 ms                                                | 33.5 ms: 1.10x slower                                                            |
| pprint_pformat                   | 986 ms                                                 | 1.08 sec: 1.10x slower                                                           |
| deltablue                        | 2.57 ms                                                | 2.83 ms: 1.10x slower                                                            |
| create_gc_cycles                 | 1.15 ms                                                | 1.27 ms: 1.11x slower                                                            |
| pprint_safe_repr                 | 483 ms                                                 | 535 ms: 1.11x slower                                                             |
| sympy_integrate                  | 11.1 ms                                                | 12.3 ms: 1.11x slower                                                            |
| genshi_text                      | 14.7 ms                                                | 16.3 ms: 1.11x slower                                                            |
| typing_runtime_protocols         | 91.5 us                                                | 103 us: 1.12x slower                                                             |
| nqueens                          | 59.5 ms                                                | 66.8 ms: 1.12x slower                                                            |
| scimark_monte_carlo              | 44.5 ms                                                | 49.9 ms: 1.12x slower                                                            |
| regex_v8                         | 15.1 ms                                                | 17.0 ms: 1.12x slower                                                            |
| sqlglot_parse                    | 808 us                                                 | 912 us: 1.13x slower                                                             |
| sqlglot_transpile                | 973 us                                                 | 1.10 ms: 1.13x slower                                                            |
| meteor_contest                   | 69.1 ms                                                | 78.3 ms: 1.13x slower                                                            |
| mako                             | 7.44 ms                                                | 8.64 ms: 1.16x slower                                                            |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 405 ms: 1.17x slower                                                             |
| many_optionals                   | 403 us                                                 | 472 us: 1.17x slower                                                             |
| django_template                  | 19.7 ms                                                | 23.4 ms: 1.19x slower                                                            |
| unpickle_pure_python             | 145 us                                                 | 173 us: 1.19x slower                                                             |
| crypto_pyaes                     | 51.4 ms                                                | 61.5 ms: 1.20x slower                                                            |
| pickle_pure_python               | 197 us                                                 | 237 us: 1.20x slower                                                             |
| richards                         | 30.6 ms                                                | 36.9 ms: 1.21x slower                                                            |
| hexiom                           | 4.38 ms                                                | 5.29 ms: 1.21x slower                                                            |
| telco                            | 3.92 ms                                                | 4.75 ms: 1.21x slower                                                            |
| fannkuch                         | 250 ms                                                 | 304 ms: 1.22x slower                                                             |
| json_dumps                       | 6.19 ms                                                | 7.54 ms: 1.22x slower                                                            |
| coverage                         | 38.5 ms                                                | 47.0 ms: 1.22x slower                                                            |
| richards_super                   | 34.6 ms                                                | 42.6 ms: 1.23x slower                                                            |
| nbody                            | 67.6 ms                                                | 90.5 ms: 1.34x slower                                                            |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 191 ms: 1.35x slower                                                             |
| async_tree_eager_tg              | 46.9 ms                                                | 143 ms: 3.04x slower                                                             |
| Geometric mean                   | (ref)                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (4): pylint, asyncio_websockets, sphinx, thrift
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.014x slower

# HPT report

- Reliability score: 97.94% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.12x