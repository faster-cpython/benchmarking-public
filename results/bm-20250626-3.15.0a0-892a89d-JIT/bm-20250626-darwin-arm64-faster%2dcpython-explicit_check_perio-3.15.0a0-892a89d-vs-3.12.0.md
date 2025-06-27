# Results vs. 3.12.0

- fork: faster-cpython
- ref: explicit_check_perio
- machine: darwin-arm64
- commit hash: 892a89d
- commit date: 2025-06-26
- overall geometric mean: 1.091x faster
- HPT reliability: 99.94%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 168 ms: 1.00x faster                                                            |
| html5lib       | 33.4 ms                                                | 29.4 ms: 1.14x faster                                                           |
| sphinx         | 613 ms                                                 | 574 ms: 1.07x faster                                                            |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                    |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 348 ms: 1.91x faster                                                            |
| async_tree_io_tg                 | 673 ms                                                 | 360 ms: 1.87x faster                                                            |
| async_tree_io                    | 672 ms                                                 | 368 ms: 1.83x faster                                                            |
| async_tree_eager_io_tg           | 617 ms                                                 | 361 ms: 1.71x faster                                                            |
| async_tree_memoization_tg        | 318 ms                                                 | 187 ms: 1.70x faster                                                            |
| async_tree_none_tg               | 255 ms                                                 | 151 ms: 1.69x faster                                                            |
| async_tree_none                  | 263 ms                                                 | 156 ms: 1.68x faster                                                            |
| async_tree_memoization           | 310 ms                                                 | 186 ms: 1.67x faster                                                            |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 407 ms: 1.30x faster                                                            |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 410 ms: 1.29x faster                                                            |
| coroutines                       | 19.7 ms                                                | 16.1 ms: 1.23x faster                                                           |
| async_tree_eager_memoization     | 168 ms                                                 | 138 ms: 1.22x faster                                                            |
| async_generators                 | 299 ms                                                 | 276 ms: 1.08x faster                                                            |
| async_tree_eager                 | 65.8 ms                                                | 61.3 ms: 1.07x faster                                                           |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 356 ms: 1.05x faster                                                            |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 387 ms: 1.11x slower                                                            |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 163 ms: 1.15x slower                                                            |
| async_tree_eager_tg              | 46.9 ms                                                | 125 ms: 2.66x slower                                                            |
| Geometric mean                   | (ref)                                                  | 1.26x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 46.8 ms: 1.16x faster                                                           |
| nbody          | 67.6 ms                                                | 74.3 ms: 1.10x slower                                                           |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 66.6 ms: 1.14x faster                                                           |
| regex_effbot   | 2.44 ms                                                | 2.34 ms: 1.04x faster                                                           |
| regex_v8       | 15.1 ms                                                | 16.1 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                    |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                               | 1.17 sec: 1.16x faster                                                          |
| xml_etree_process    | 38.9 ms                                                | 35.0 ms: 1.11x faster                                                           |
| xml_etree_generate   | 55.4 ms                                                | 50.2 ms: 1.10x faster                                                           |
| unpickle_pure_python | 145 us                                                 | 133 us: 1.10x faster                                                            |
| xml_etree_iterparse  | 75.5 ms                                                | 70.8 ms: 1.07x faster                                                           |
| xml_etree_parse      | 108 ms                                                 | 102 ms: 1.05x faster                                                            |
| json_loads           | 17.0 us                                                | 16.4 us: 1.04x faster                                                           |
| pickle_pure_python   | 197 us                                                 | 200 us: 1.01x slower                                                            |
| json_dumps           | 6.19 ms                                                | 6.46 ms: 1.04x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 13.2 ms                                                | 13.4 ms: 1.02x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 7.44 ms                                                | 6.82 ms: 1.09x faster                                                           |
| genshi_text     | 14.7 ms                                                | 13.5 ms: 1.09x faster                                                           |
| genshi_xml      | 30.5 ms                                                | 29.0 ms: 1.05x faster                                                           |
| django_template | 19.7 ms                                                | 21.0 ms: 1.07x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                                    |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 13.1 ms: 2.44x faster                                                           |
| mdp                              | 1.49 sec                                               | 732 ms: 2.04x faster                                                            |
| async_tree_eager_io              | 666 ms                                                 | 348 ms: 1.91x faster                                                            |
| async_tree_io_tg                 | 673 ms                                                 | 360 ms: 1.87x faster                                                            |
| async_tree_io                    | 672 ms                                                 | 368 ms: 1.83x faster                                                            |
| async_tree_eager_io_tg           | 617 ms                                                 | 361 ms: 1.71x faster                                                            |
| async_tree_memoization_tg        | 318 ms                                                 | 187 ms: 1.70x faster                                                            |
| async_tree_none_tg               | 255 ms                                                 | 151 ms: 1.69x faster                                                            |
| async_tree_none                  | 263 ms                                                 | 156 ms: 1.68x faster                                                            |
| async_tree_memoization           | 310 ms                                                 | 186 ms: 1.67x faster                                                            |
| deepcopy                         | 226 us                                                 | 149 us: 1.51x faster                                                            |
| deepcopy_memo                    | 26.0 us                                                | 18.3 us: 1.42x faster                                                           |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 407 ms: 1.30x faster                                                            |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 410 ms: 1.29x faster                                                            |
| generators                       | 29.4 ms                                                | 23.1 ms: 1.27x faster                                                           |
| go                               | 98.5 ms                                                | 77.9 ms: 1.26x faster                                                           |
| deepcopy_reduce                  | 2.01 us                                                | 1.62 us: 1.24x faster                                                           |
| coroutines                       | 19.7 ms                                                | 16.1 ms: 1.23x faster                                                           |
| async_tree_eager_memoization     | 168 ms                                                 | 138 ms: 1.22x faster                                                            |
| comprehensions                   | 14.0 us                                                | 11.6 us: 1.21x faster                                                           |
| dulwich_log                      | 29.2 ms                                                | 24.2 ms: 1.21x faster                                                           |
| raytrace                         | 204 ms                                                 | 170 ms: 1.20x faster                                                            |
| spectral_norm                    | 76.5 ms                                                | 64.7 ms: 1.18x faster                                                           |
| tomli_loads                      | 1.36 sec                                               | 1.17 sec: 1.16x faster                                                          |
| float                            | 54.1 ms                                                | 46.8 ms: 1.16x faster                                                           |
| pylint                           | 182 ms                                                 | 159 ms: 1.14x faster                                                            |
| regex_compile                    | 75.9 ms                                                | 66.6 ms: 1.14x faster                                                           |
| k_core                           | 1.72 sec                                               | 1.52 sec: 1.14x faster                                                          |
| html5lib                         | 33.4 ms                                                | 29.4 ms: 1.14x faster                                                           |
| pathlib                          | 24.7 ms                                                | 21.9 ms: 1.12x faster                                                           |
| chaos                            | 41.6 ms                                                | 37.0 ms: 1.12x faster                                                           |
| scimark_sor                      | 85.8 ms                                                | 76.3 ms: 1.12x faster                                                           |
| pyflate                          | 311 ms                                                 | 277 ms: 1.12x faster                                                            |
| xml_etree_process                | 38.9 ms                                                | 35.0 ms: 1.11x faster                                                           |
| xml_etree_generate               | 55.4 ms                                                | 50.2 ms: 1.10x faster                                                           |
| unpickle_pure_python             | 145 us                                                 | 133 us: 1.10x faster                                                            |
| mako                             | 7.44 ms                                                | 6.82 ms: 1.09x faster                                                           |
| genshi_text                      | 14.7 ms                                                | 13.5 ms: 1.09x faster                                                           |
| async_generators                 | 299 ms                                                 | 276 ms: 1.08x faster                                                            |
| bpe_tokeniser                    | 3.28 sec                                               | 3.04 sec: 1.08x faster                                                          |
| thrift                           | 468 us                                                 | 434 us: 1.08x faster                                                            |
| async_tree_eager                 | 65.8 ms                                                | 61.3 ms: 1.07x faster                                                           |
| sphinx                           | 613 ms                                                 | 574 ms: 1.07x faster                                                            |
| xml_etree_iterparse              | 75.5 ms                                                | 70.8 ms: 1.07x faster                                                           |
| xml_etree_parse                  | 108 ms                                                 | 102 ms: 1.05x faster                                                            |
| genshi_xml                       | 30.5 ms                                                | 29.0 ms: 1.05x faster                                                           |
| scimark_monte_carlo              | 44.5 ms                                                | 42.3 ms: 1.05x faster                                                           |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 356 ms: 1.05x faster                                                            |
| regex_effbot                     | 2.44 ms                                                | 2.34 ms: 1.04x faster                                                           |
| json                             | 3.00 ms                                                | 2.88 ms: 1.04x faster                                                           |
| logging_simple                   | 3.60 us                                                | 3.47 us: 1.04x faster                                                           |
| sympy_sum                        | 76.2 ms                                                | 73.3 ms: 1.04x faster                                                           |
| json_loads                       | 17.0 us                                                | 16.4 us: 1.04x faster                                                           |
| sympy_integrate                  | 11.1 ms                                                | 10.7 ms: 1.04x faster                                                           |
| sympy_str                        | 144 ms                                                 | 139 ms: 1.04x faster                                                            |
| deltablue                        | 2.57 ms                                                | 2.49 ms: 1.03x faster                                                           |
| logging_format                   | 3.90 us                                                | 3.79 us: 1.03x faster                                                           |
| dask                             | 779 ms                                                 | 768 ms: 1.01x faster                                                            |
| nqueens                          | 59.5 ms                                                | 58.9 ms: 1.01x faster                                                           |
| 2to3                             | 168 ms                                                 | 168 ms: 1.00x faster                                                            |
| scimark_lu                       | 73.5 ms                                                | 74.0 ms: 1.01x slower                                                           |
| sympy_expand                     | 233 ms                                                 | 236 ms: 1.01x slower                                                            |
| shortest_path                    | 331 ms                                                 | 335 ms: 1.01x slower                                                            |
| pickle_pure_python               | 197 us                                                 | 200 us: 1.01x slower                                                            |
| sqlite_synth                     | 1.55 us                                                | 1.57 us: 1.01x slower                                                           |
| pycparser                        | 673 ms                                                 | 686 ms: 1.02x slower                                                            |
| python_startup_no_site           | 13.2 ms                                                | 13.4 ms: 1.02x slower                                                           |
| hexiom                           | 4.38 ms                                                | 4.49 ms: 1.03x slower                                                           |
| connected_components             | 300 ms                                                 | 309 ms: 1.03x slower                                                            |
| scimark_fft                      | 194 ms                                                 | 201 ms: 1.04x slower                                                            |
| typing_runtime_protocols         | 91.5 us                                                | 95.2 us: 1.04x slower                                                           |
| json_dumps                       | 6.19 ms                                                | 6.46 ms: 1.04x slower                                                           |
| richards                         | 30.6 ms                                                | 32.5 ms: 1.06x slower                                                           |
| regex_v8                         | 15.1 ms                                                | 16.1 ms: 1.06x slower                                                           |
| richards_super                   | 34.6 ms                                                | 37.0 ms: 1.07x slower                                                           |
| django_template                  | 19.7 ms                                                | 21.0 ms: 1.07x slower                                                           |
| crypto_pyaes                     | 51.4 ms                                                | 55.0 ms: 1.07x slower                                                           |
| meteor_contest                   | 69.1 ms                                                | 75.7 ms: 1.10x slower                                                           |
| nbody                            | 67.6 ms                                                | 74.3 ms: 1.10x slower                                                           |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 387 ms: 1.11x slower                                                            |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.55 ms: 1.13x slower                                                           |
| gc_traversal                     | 2.95 ms                                                | 3.35 ms: 1.14x slower                                                           |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 163 ms: 1.15x slower                                                            |
| many_optionals                   | 403 us                                                 | 466 us: 1.16x slower                                                            |
| fannkuch                         | 250 ms                                                 | 290 ms: 1.16x slower                                                            |
| pprint_pformat                   | 986 ms                                                 | 1.14 sec: 1.16x slower                                                          |
| pprint_safe_repr                 | 483 ms                                                 | 568 ms: 1.18x slower                                                            |
| telco                            | 3.92 ms                                                | 4.62 ms: 1.18x slower                                                           |
| create_gc_cycles                 | 1.15 ms                                                | 1.37 ms: 1.19x slower                                                           |
| coverage                         | 38.5 ms                                                | 47.0 ms: 1.22x slower                                                           |
| async_tree_eager_tg              | 46.9 ms                                                | 125 ms: 2.66x slower                                                            |
| logging_silent                   | 72.5 ns                                                | 325 ns: 4.49x slower                                                            |
| Geometric mean                   | (ref)                                                  | 1.08x faster                                                                    |

Benchmark hidden because not significant (5): asyncio_websockets, docutils, pidigits, regex_dna, python_startup
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250626-3.15.0a0-892a89d-JIT/bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.091x faster

# HPT report

- Reliability score: 99.94% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.14x