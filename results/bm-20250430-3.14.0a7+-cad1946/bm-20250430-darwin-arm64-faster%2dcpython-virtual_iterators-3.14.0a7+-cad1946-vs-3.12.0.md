# Results vs. 3.12.0

- fork: faster-cpython
- ref: virtual_iterators
- machine: darwin-arm64
- commit hash: cad1946
- commit date: 2025-04-30
- overall geometric mean: 1.038x slower
- HPT reliability: 99.69%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 219 ms: 1.30x slower                                                          |
| docutils       | 1.45 sec                                               | 1.53 sec: 1.06x slower                                                        |
| html5lib       | 33.4 ms                                                | 34.8 ms: 1.04x slower                                                         |
| sphinx         | 613 ms                                                 | 619 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                  | 1.10x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 410 ms: 1.63x faster                                                          |
| async_tree_io_tg                 | 673 ms                                                 | 421 ms: 1.60x faster                                                          |
| async_tree_io                    | 672 ms                                                 | 425 ms: 1.58x faster                                                          |
| async_tree_memoization_tg        | 318 ms                                                 | 212 ms: 1.50x faster                                                          |
| async_tree_eager_io_tg           | 617 ms                                                 | 413 ms: 1.49x faster                                                          |
| async_tree_none_tg               | 255 ms                                                 | 177 ms: 1.44x faster                                                          |
| async_tree_none                  | 263 ms                                                 | 188 ms: 1.40x faster                                                          |
| async_tree_memoization           | 310 ms                                                 | 226 ms: 1.38x faster                                                          |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 431 ms: 1.22x faster                                                          |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 441 ms: 1.20x faster                                                          |
| async_tree_eager_memoization     | 168 ms                                                 | 154 ms: 1.09x faster                                                          |
| async_generators                 | 299 ms                                                 | 277 ms: 1.08x faster                                                          |
| asyncio_websockets               | 243 ms                                                 | 244 ms: 1.01x slower                                                          |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 404 ms: 1.16x slower                                                          |
| async_tree_eager                 | 65.8 ms                                                | 76.7 ms: 1.17x slower                                                         |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 189 ms: 1.34x slower                                                          |
| async_tree_eager_tg              | 46.9 ms                                                | 149 ms: 3.17x slower                                                          |
| Geometric mean                   | (ref)                                                  | 1.11x faster                                                                  |

Benchmark hidden because not significant (2): coroutines, async_tree_eager_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 283 ms                                                 | 284 ms: 1.00x slower                                                          |
| float          | 54.1 ms                                                | 57.7 ms: 1.07x slower                                                         |
| nbody          | 67.6 ms                                                | 89.1 ms: 1.32x slower                                                         |
| Geometric mean | (ref)                                                  | 1.12x slower                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.24 ms: 1.09x faster                                                         |
| regex_dna      | 143 ms                                                 | 140 ms: 1.02x faster                                                          |
| regex_v8       | 15.1 ms                                                | 15.8 ms: 1.05x slower                                                         |
| regex_compile  | 75.9 ms                                                | 85.4 ms: 1.12x slower                                                         |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 106 ms: 1.02x faster                                                          |
| json_loads           | 17.0 us                                                | 18.8 us: 1.10x slower                                                         |
| tomli_loads          | 1.36 sec                                               | 1.50 sec: 1.10x slower                                                        |
| xml_etree_generate   | 55.4 ms                                                | 61.4 ms: 1.11x slower                                                         |
| xml_etree_process    | 38.9 ms                                                | 45.0 ms: 1.16x slower                                                         |
| unpickle_pure_python | 145 us                                                 | 183 us: 1.26x slower                                                          |
| pickle_pure_python   | 197 us                                                 | 251 us: 1.27x slower                                                          |
| json_dumps           | 6.19 ms                                                | 8.16 ms: 1.32x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.14x slower                                                                  |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 13.2 ms                                                | 14.7 ms: 1.11x slower                                                         |
| python_startup         | 17.8 ms                                                | 19.8 ms: 1.12x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_xml      | 30.5 ms                                                | 36.7 ms: 1.20x slower                                                         |
| mako            | 7.44 ms                                                | 9.07 ms: 1.22x slower                                                         |
| genshi_text     | 14.7 ms                                                | 18.2 ms: 1.24x slower                                                         |
| django_template | 19.7 ms                                                | 25.6 ms: 1.30x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.24x slower                                                                  |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 13.6 ms: 2.37x faster                                                         |
| mdp                              | 1.49 sec                                               | 855 ms: 1.75x faster                                                          |
| async_tree_eager_io              | 666 ms                                                 | 410 ms: 1.63x faster                                                          |
| async_tree_io_tg                 | 673 ms                                                 | 421 ms: 1.60x faster                                                          |
| async_tree_io                    | 672 ms                                                 | 425 ms: 1.58x faster                                                          |
| async_tree_memoization_tg        | 318 ms                                                 | 212 ms: 1.50x faster                                                          |
| async_tree_eager_io_tg           | 617 ms                                                 | 413 ms: 1.49x faster                                                          |
| async_tree_none_tg               | 255 ms                                                 | 177 ms: 1.44x faster                                                          |
| async_tree_none                  | 263 ms                                                 | 188 ms: 1.40x faster                                                          |
| async_tree_memoization           | 310 ms                                                 | 226 ms: 1.38x faster                                                          |
| deepcopy                         | 226 us                                                 | 184 us: 1.23x faster                                                          |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 431 ms: 1.22x faster                                                          |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 441 ms: 1.20x faster                                                          |
| k_core                           | 1.72 sec                                               | 1.55 sec: 1.11x faster                                                        |
| deepcopy_memo                    | 26.0 us                                                | 23.6 us: 1.10x faster                                                         |
| regex_effbot                     | 2.44 ms                                                | 2.24 ms: 1.09x faster                                                         |
| async_tree_eager_memoization     | 168 ms                                                 | 154 ms: 1.09x faster                                                          |
| async_generators                 | 299 ms                                                 | 277 ms: 1.08x faster                                                          |
| dulwich_log                      | 29.2 ms                                                | 27.2 ms: 1.07x faster                                                         |
| deepcopy_reduce                  | 2.01 us                                                | 1.97 us: 1.02x faster                                                         |
| comprehensions                   | 14.0 us                                                | 13.7 us: 1.02x faster                                                         |
| xml_etree_parse                  | 108 ms                                                 | 106 ms: 1.02x faster                                                          |
| regex_dna                        | 143 ms                                                 | 140 ms: 1.02x faster                                                          |
| raytrace                         | 204 ms                                                 | 203 ms: 1.00x faster                                                          |
| pidigits                         | 283 ms                                                 | 284 ms: 1.00x slower                                                          |
| asyncio_websockets               | 243 ms                                                 | 244 ms: 1.01x slower                                                          |
| sphinx                           | 613 ms                                                 | 619 ms: 1.01x slower                                                          |
| spectral_norm                    | 76.5 ms                                                | 77.4 ms: 1.01x slower                                                         |
| pathlib                          | 24.7 ms                                                | 25.2 ms: 1.02x slower                                                         |
| bpe_tokeniser                    | 3.28 sec                                               | 3.38 sec: 1.03x slower                                                        |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.24 ms: 1.03x slower                                                         |
| shortest_path                    | 331 ms                                                 | 341 ms: 1.03x slower                                                          |
| bench_mp_pool                    | 65.5 ms                                                | 67.7 ms: 1.03x slower                                                         |
| go                               | 98.5 ms                                                | 102 ms: 1.04x slower                                                          |
| sqlite_synth                     | 1.55 us                                                | 1.61 us: 1.04x slower                                                         |
| html5lib                         | 33.4 ms                                                | 34.8 ms: 1.04x slower                                                         |
| regex_v8                         | 15.1 ms                                                | 15.8 ms: 1.05x slower                                                         |
| sqlalchemy_declarative           | 61.9 ms                                                | 65.1 ms: 1.05x slower                                                         |
| docutils                         | 1.45 sec                                               | 1.53 sec: 1.06x slower                                                        |
| generators                       | 29.4 ms                                                | 31.0 ms: 1.06x slower                                                         |
| connected_components             | 300 ms                                                 | 317 ms: 1.06x slower                                                          |
| gc_traversal                     | 2.95 ms                                                | 3.12 ms: 1.06x slower                                                         |
| float                            | 54.1 ms                                                | 57.7 ms: 1.07x slower                                                         |
| scimark_fft                      | 194 ms                                                 | 209 ms: 1.08x slower                                                          |
| json                             | 3.00 ms                                                | 3.24 ms: 1.08x slower                                                         |
| logging_silent                   | 72.5 ns                                                | 78.5 ns: 1.08x slower                                                         |
| logging_format                   | 3.90 us                                                | 4.23 us: 1.09x slower                                                         |
| logging_simple                   | 3.60 us                                                | 3.94 us: 1.09x slower                                                         |
| scimark_sor                      | 85.8 ms                                                | 93.8 ms: 1.09x slower                                                         |
| json_loads                       | 17.0 us                                                | 18.8 us: 1.10x slower                                                         |
| tomli_loads                      | 1.36 sec                                               | 1.50 sec: 1.10x slower                                                        |
| xml_etree_generate               | 55.4 ms                                                | 61.4 ms: 1.11x slower                                                         |
| pyflate                          | 311 ms                                                 | 346 ms: 1.11x slower                                                          |
| python_startup_no_site           | 13.2 ms                                                | 14.7 ms: 1.11x slower                                                         |
| deltablue                        | 2.57 ms                                                | 2.86 ms: 1.12x slower                                                         |
| python_startup                   | 17.8 ms                                                | 19.8 ms: 1.12x slower                                                         |
| sqlalchemy_imperative            | 6.60 ms                                                | 7.37 ms: 1.12x slower                                                         |
| pycparser                        | 673 ms                                                 | 754 ms: 1.12x slower                                                          |
| meteor_contest                   | 69.1 ms                                                | 77.5 ms: 1.12x slower                                                         |
| bench_thread_pool                | 483 us                                                 | 542 us: 1.12x slower                                                          |
| chaos                            | 41.6 ms                                                | 46.8 ms: 1.12x slower                                                         |
| regex_compile                    | 75.9 ms                                                | 85.4 ms: 1.12x slower                                                         |
| create_gc_cycles                 | 1.15 ms                                                | 1.30 ms: 1.13x slower                                                         |
| scimark_lu                       | 73.5 ms                                                | 83.3 ms: 1.13x slower                                                         |
| xml_etree_process                | 38.9 ms                                                | 45.0 ms: 1.16x slower                                                         |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 404 ms: 1.16x slower                                                          |
| pprint_pformat                   | 986 ms                                                 | 1.15 sec: 1.16x slower                                                        |
| async_tree_eager                 | 65.8 ms                                                | 76.7 ms: 1.17x slower                                                         |
| typing_runtime_protocols         | 91.5 us                                                | 107 us: 1.17x slower                                                          |
| pprint_safe_repr                 | 483 ms                                                 | 568 ms: 1.17x slower                                                          |
| genshi_xml                       | 30.5 ms                                                | 36.7 ms: 1.20x slower                                                         |
| scimark_monte_carlo              | 44.5 ms                                                | 53.6 ms: 1.21x slower                                                         |
| crypto_pyaes                     | 51.4 ms                                                | 62.1 ms: 1.21x slower                                                         |
| many_optionals                   | 403 us                                                 | 489 us: 1.21x slower                                                          |
| hexiom                           | 4.38 ms                                                | 5.33 ms: 1.22x slower                                                         |
| mako                             | 7.44 ms                                                | 9.07 ms: 1.22x slower                                                         |
| genshi_text                      | 14.7 ms                                                | 18.2 ms: 1.24x slower                                                         |
| nqueens                          | 59.5 ms                                                | 74.0 ms: 1.24x slower                                                         |
| unpickle_pure_python             | 145 us                                                 | 183 us: 1.26x slower                                                          |
| fannkuch                         | 250 ms                                                 | 316 ms: 1.26x slower                                                          |
| telco                            | 3.92 ms                                                | 4.96 ms: 1.27x slower                                                         |
| pickle_pure_python               | 197 us                                                 | 251 us: 1.27x slower                                                          |
| richards_super                   | 34.6 ms                                                | 44.1 ms: 1.27x slower                                                         |
| richards                         | 30.6 ms                                                | 39.4 ms: 1.29x slower                                                         |
| 2to3                             | 168 ms                                                 | 219 ms: 1.30x slower                                                          |
| django_template                  | 19.7 ms                                                | 25.6 ms: 1.30x slower                                                         |
| coverage                         | 38.5 ms                                                | 50.3 ms: 1.31x slower                                                         |
| json_dumps                       | 6.19 ms                                                | 8.16 ms: 1.32x slower                                                         |
| nbody                            | 67.6 ms                                                | 89.1 ms: 1.32x slower                                                         |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 189 ms: 1.34x slower                                                          |
| async_tree_eager_tg              | 46.9 ms                                                | 149 ms: 3.17x slower                                                          |
| Geometric mean                   | (ref)                                                  | 1.04x slower                                                                  |

Benchmark hidden because not significant (3): coroutines, xml_etree_iterparse, async_tree_eager_cpu_io_mixed
Ignored benchmarks (16) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, dask, djangocms, gevent_hub, gunicorn, pylint, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250430-3.14.0a7+-cad1946/bm-20250430-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.038x slower

# HPT report

- Reliability score: 99.69% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.10x