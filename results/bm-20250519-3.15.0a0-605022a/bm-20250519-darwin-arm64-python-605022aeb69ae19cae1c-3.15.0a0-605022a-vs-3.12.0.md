# Results vs. 3.12.0

- fork: python
- ref: 605022aeb69ae19cae1c
- machine: darwin-arm64
- commit hash: 605022a
- commit date: 2025-05-19
- overall geometric mean: 1.106x slower
- HPT reliability: 99.94%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250519-darwin-arm64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 193 ms: 1.14x slower                                                  |
| docutils       | 1.45 sec                                               | 1.57 sec: 1.08x slower                                                |
| html5lib       | 33.4 ms                                                | 35.2 ms: 1.06x slower                                                 |
| sphinx         | 613 ms                                                 | 637 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.08x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250519-darwin-arm64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 407 ms: 1.64x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 417 ms: 1.61x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 425 ms: 1.58x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 413 ms: 1.50x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 215 ms: 1.48x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 176 ms: 1.45x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 186 ms: 1.42x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 222 ms: 1.40x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 426 ms: 1.24x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 440 ms: 1.20x faster                                                  |
| async_generators                 | 299 ms                                                 | 274 ms: 1.09x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 155 ms: 1.08x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 372 ms: 1.01x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 401 ms: 1.16x slower                                                  |
| async_tree_eager                 | 65.8 ms                                                | 77.6 ms: 1.18x slower                                                 |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 188 ms: 1.32x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 145 ms: 3.08x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.12x faster                                                          |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250519-darwin-arm64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 283 ms                                                 | 283 ms: 1.00x slower                                                  |
| float          | 54.1 ms                                                | 58.9 ms: 1.09x slower                                                 |
| nbody          | 67.6 ms                                                | 91.7 ms: 1.36x slower                                                 |
| Geometric mean | (ref)                                                  | 1.14x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250519-darwin-arm64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.16 ms: 1.13x faster                                                 |
| regex_dna      | 143 ms                                                 | 137 ms: 1.04x faster                                                  |
| regex_v8       | 15.1 ms                                                | 15.8 ms: 1.04x slower                                                 |
| regex_compile  | 75.9 ms                                                | 86.7 ms: 1.14x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250519-darwin-arm64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 105 ms: 1.03x faster                                                  |
| xml_etree_iterparse  | 75.5 ms                                                | 77.0 ms: 1.02x slower                                                 |
| json_loads           | 17.0 us                                                | 18.3 us: 1.07x slower                                                 |
| xml_etree_generate   | 55.4 ms                                                | 61.4 ms: 1.11x slower                                                 |
| tomli_loads          | 1.36 sec                                               | 1.52 sec: 1.12x slower                                                |
| json_dumps           | 6.19 ms                                                | 7.16 ms: 1.16x slower                                                 |
| xml_etree_process    | 38.9 ms                                                | 45.8 ms: 1.18x slower                                                 |
| pickle_pure_python   | 197 us                                                 | 250 us: 1.27x slower                                                  |
| unpickle_pure_python | 145 us                                                 | 189 us: 1.30x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.13x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250519-darwin-arm64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 18.9 ms: 1.06x slower                                                 |
| python_startup_no_site | 13.2 ms                                                | 14.4 ms: 1.09x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250519-darwin-arm64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.44 ms                                                | 9.10 ms: 1.22x slower                                                 |
| genshi_xml      | 30.5 ms                                                | 37.6 ms: 1.23x slower                                                 |
| genshi_text     | 14.7 ms                                                | 18.6 ms: 1.27x slower                                                 |
| django_template | 19.7 ms                                                | 26.6 ms: 1.35x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.27x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250519-darwin-arm64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 15.2 ms: 2.11x faster                                                 |
| mdp                              | 1.49 sec                                               | 867 ms: 1.72x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 407 ms: 1.64x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 417 ms: 1.61x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 425 ms: 1.58x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 413 ms: 1.50x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 215 ms: 1.48x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 176 ms: 1.45x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 186 ms: 1.42x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 222 ms: 1.40x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 426 ms: 1.24x faster                                                  |
| deepcopy                         | 226 us                                                 | 187 us: 1.21x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 440 ms: 1.20x faster                                                  |
| regex_effbot                     | 2.44 ms                                                | 2.16 ms: 1.13x faster                                                 |
| k_core                           | 1.72 sec                                               | 1.57 sec: 1.10x faster                                                |
| deepcopy_memo                    | 26.0 us                                                | 23.8 us: 1.09x faster                                                 |
| async_generators                 | 299 ms                                                 | 274 ms: 1.09x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 155 ms: 1.08x faster                                                  |
| dulwich_log                      | 29.2 ms                                                | 27.4 ms: 1.07x faster                                                 |
| regex_dna                        | 143 ms                                                 | 137 ms: 1.04x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 105 ms: 1.03x faster                                                  |
| pathlib                          | 24.7 ms                                                | 24.2 ms: 1.02x faster                                                 |
| deepcopy_reduce                  | 2.01 us                                                | 1.99 us: 1.01x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 372 ms: 1.01x faster                                                  |
| pidigits                         | 283 ms                                                 | 283 ms: 1.00x slower                                                  |
| bpe_tokeniser                    | 3.28 sec                                               | 3.31 sec: 1.01x slower                                                |
| raytrace                         | 204 ms                                                 | 207 ms: 1.01x slower                                                  |
| xml_etree_iterparse              | 75.5 ms                                                | 77.0 ms: 1.02x slower                                                 |
| spectral_norm                    | 76.5 ms                                                | 78.5 ms: 1.03x slower                                                 |
| shortest_path                    | 331 ms                                                 | 341 ms: 1.03x slower                                                  |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.24 ms: 1.03x slower                                                 |
| sqlite_synth                     | 1.55 us                                                | 1.59 us: 1.03x slower                                                 |
| json                             | 3.00 ms                                                | 3.11 ms: 1.04x slower                                                 |
| comprehensions                   | 14.0 us                                                | 14.6 us: 1.04x slower                                                 |
| sphinx                           | 613 ms                                                 | 637 ms: 1.04x slower                                                  |
| connected_components             | 300 ms                                                 | 313 ms: 1.04x slower                                                  |
| regex_v8                         | 15.1 ms                                                | 15.8 ms: 1.04x slower                                                 |
| sympy_integrate                  | 11.1 ms                                                | 11.6 ms: 1.05x slower                                                 |
| html5lib                         | 33.4 ms                                                | 35.2 ms: 1.06x slower                                                 |
| python_startup                   | 17.8 ms                                                | 18.9 ms: 1.06x slower                                                 |
| go                               | 98.5 ms                                                | 105 ms: 1.07x slower                                                  |
| generators                       | 29.4 ms                                                | 31.5 ms: 1.07x slower                                                 |
| json_loads                       | 17.0 us                                                | 18.3 us: 1.07x slower                                                 |
| scimark_fft                      | 194 ms                                                 | 209 ms: 1.08x slower                                                  |
| docutils                         | 1.45 sec                                               | 1.57 sec: 1.08x slower                                                |
| sympy_sum                        | 76.2 ms                                                | 82.8 ms: 1.09x slower                                                 |
| float                            | 54.1 ms                                                | 58.9 ms: 1.09x slower                                                 |
| bench_mp_pool                    | 65.5 ms                                                | 71.4 ms: 1.09x slower                                                 |
| python_startup_no_site           | 13.2 ms                                                | 14.4 ms: 1.09x slower                                                 |
| gc_traversal                     | 2.95 ms                                                | 3.22 ms: 1.09x slower                                                 |
| dask                             | 779 ms                                                 | 860 ms: 1.10x slower                                                  |
| scimark_sor                      | 85.8 ms                                                | 94.8 ms: 1.11x slower                                                 |
| xml_etree_generate               | 55.4 ms                                                | 61.4 ms: 1.11x slower                                                 |
| sympy_str                        | 144 ms                                                 | 160 ms: 1.11x slower                                                  |
| deltablue                        | 2.57 ms                                                | 2.86 ms: 1.12x slower                                                 |
| tomli_loads                      | 1.36 sec                                               | 1.52 sec: 1.12x slower                                                |
| pyflate                          | 311 ms                                                 | 350 ms: 1.12x slower                                                  |
| meteor_contest                   | 69.1 ms                                                | 77.8 ms: 1.13x slower                                                 |
| chaos                            | 41.6 ms                                                | 46.9 ms: 1.13x slower                                                 |
| bench_thread_pool                | 483 us                                                 | 544 us: 1.13x slower                                                  |
| pycparser                        | 673 ms                                                 | 766 ms: 1.14x slower                                                  |
| regex_compile                    | 75.9 ms                                                | 86.7 ms: 1.14x slower                                                 |
| 2to3                             | 168 ms                                                 | 193 ms: 1.14x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 401 ms: 1.16x slower                                                  |
| json_dumps                       | 6.19 ms                                                | 7.16 ms: 1.16x slower                                                 |
| sympy_expand                     | 233 ms                                                 | 271 ms: 1.16x slower                                                  |
| logging_format                   | 3.90 us                                                | 4.54 us: 1.16x slower                                                 |
| logging_simple                   | 3.60 us                                                | 4.22 us: 1.17x slower                                                 |
| scimark_lu                       | 73.5 ms                                                | 86.3 ms: 1.17x slower                                                 |
| xml_etree_process                | 38.9 ms                                                | 45.8 ms: 1.18x slower                                                 |
| async_tree_eager                 | 65.8 ms                                                | 77.6 ms: 1.18x slower                                                 |
| create_gc_cycles                 | 1.15 ms                                                | 1.37 ms: 1.19x slower                                                 |
| crypto_pyaes                     | 51.4 ms                                                | 61.4 ms: 1.19x slower                                                 |
| fannkuch                         | 250 ms                                                 | 301 ms: 1.21x slower                                                  |
| pprint_pformat                   | 986 ms                                                 | 1.19 sec: 1.21x slower                                                |
| scimark_monte_carlo              | 44.5 ms                                                | 53.8 ms: 1.21x slower                                                 |
| pprint_safe_repr                 | 483 ms                                                 | 588 ms: 1.22x slower                                                  |
| mako                             | 7.44 ms                                                | 9.10 ms: 1.22x slower                                                 |
| typing_runtime_protocols         | 91.5 us                                                | 112 us: 1.23x slower                                                  |
| telco                            | 3.92 ms                                                | 4.82 ms: 1.23x slower                                                 |
| genshi_xml                       | 30.5 ms                                                | 37.6 ms: 1.23x slower                                                 |
| hexiom                           | 4.38 ms                                                | 5.47 ms: 1.25x slower                                                 |
| pickle_pure_python               | 197 us                                                 | 250 us: 1.27x slower                                                  |
| genshi_text                      | 14.7 ms                                                | 18.6 ms: 1.27x slower                                                 |
| many_optionals                   | 403 us                                                 | 512 us: 1.27x slower                                                  |
| richards_super                   | 34.6 ms                                                | 44.0 ms: 1.27x slower                                                 |
| nqueens                          | 59.5 ms                                                | 75.7 ms: 1.27x slower                                                 |
| richards                         | 30.6 ms                                                | 39.4 ms: 1.29x slower                                                 |
| unpickle_pure_python             | 145 us                                                 | 189 us: 1.30x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 188 ms: 1.32x slower                                                  |
| django_template                  | 19.7 ms                                                | 26.6 ms: 1.35x slower                                                 |
| nbody                            | 67.6 ms                                                | 91.7 ms: 1.36x slower                                                 |
| async_tree_eager_tg              | 46.9 ms                                                | 145 ms: 3.08x slower                                                  |
| logging_silent                   | 72.5 ns                                                | 344 ns: 4.74x slower                                                  |
| coverage                         | 38.5 ms                                                | 332 ms: 8.63x slower                                                  |
| thrift                           | 468 us                                                 | 43.9 ms: 93.92x slower                                                |
| Geometric mean                   | (ref)                                                  | 1.13x slower                                                          |

Benchmark hidden because not significant (3): pylint, asyncio_websockets, coroutines
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250519-3.15.0a0-605022a/bm-20250519-darwin-arm64-python-605022aeb69ae19cae1c-3.15.0a0-605022a.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.106x slower

# HPT report

- Reliability score: 99.94% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.11x