# Results vs. 3.13.0

- fork: brandtbucher
- ref: warmup_side_4096
- machine: darwin-arm64
- commit hash: a8a4ed3
- commit date: 2024-11-22
- overall geometric mean: 1.037x faster
- HPT reliability: 99.95%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-darwin-arm64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 170 ms: 1.10x faster                                                     |
| docutils       | 1.44 sec                                               | 1.49 sec: 1.03x slower                                                   |
| html5lib       | 36.6 ms                                                | 32.6 ms: 1.12x faster                                                    |
| sphinx         | 603 ms                                                 | 618 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                  | 1.04x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-darwin-arm64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 17.6 ms: 1.12x faster                                                    |
| async_tree_memoization_tg        | 288 ms                                                 | 258 ms: 1.12x faster                                                     |
| async_tree_eager_tg              | 47.8 ms                                                | 44.6 ms: 1.07x faster                                                    |
| async_tree_memoization           | 268 ms                                                 | 251 ms: 1.07x faster                                                     |
| async_tree_eager                 | 70.1 ms                                                | 66.7 ms: 1.05x faster                                                    |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 132 ms: 1.05x faster                                                     |
| async_tree_eager_memoization     | 168 ms                                                 | 162 ms: 1.04x faster                                                     |
| async_tree_none                  | 215 ms                                                 | 208 ms: 1.03x faster                                                     |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 362 ms: 1.03x faster                                                     |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 343 ms: 1.01x faster                                                     |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 469 ms: 1.02x slower                                                     |
| async_generators                 | 295 ms                                                 | 304 ms: 1.03x slower                                                     |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 479 ms: 1.07x slower                                                     |
| async_tree_io                    | 507 ms                                                 | 606 ms: 1.20x slower                                                     |
| async_tree_io_tg                 | 497 ms                                                 | 595 ms: 1.20x slower                                                     |
| async_tree_eager_io              | 514 ms                                                 | 710 ms: 1.38x slower                                                     |
| async_tree_eager_io_tg           | 477 ms                                                 | 697 ms: 1.46x slower                                                     |
| Geometric mean                   | (ref)                                                  | 1.03x slower                                                             |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-darwin-arm64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 74.0 ms                                                | 63.5 ms: 1.17x faster                                                    |
| float          | 56.0 ms                                                | 48.9 ms: 1.15x faster                                                    |
| Geometric mean | (ref)                                                  | 1.10x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-darwin-arm64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.02 ms: 1.30x faster                                                    |
| regex_compile  | 78.6 ms                                                | 70.4 ms: 1.12x faster                                                    |
| regex_dna      | 149 ms                                                 | 135 ms: 1.10x faster                                                     |
| regex_v8       | 17.0 ms                                                | 15.8 ms: 1.07x faster                                                    |
| Geometric mean | (ref)                                                  | 1.14x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-darwin-arm64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 164 us                                                 | 122 us: 1.34x faster                                                     |
| tomli_loads          | 1.57 sec                                               | 1.26 sec: 1.25x faster                                                   |
| xml_etree_process    | 41.0 ms                                                | 35.3 ms: 1.16x faster                                                    |
| xml_etree_generate   | 57.0 ms                                                | 49.9 ms: 1.14x faster                                                    |
| pickle_pure_python   | 214 us                                                 | 193 us: 1.11x faster                                                     |
| json_loads           | 17.0 us                                                | 16.5 us: 1.03x faster                                                    |
| json_dumps           | 6.52 ms                                                | 7.13 ms: 1.09x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                             |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-darwin-arm64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 14.5 ms                                                | 15.1 ms: 1.04x slower                                                    |
| python_startup         | 18.9 ms                                                | 19.8 ms: 1.05x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.04x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-darwin-arm64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.21 ms: 1.24x faster                                                    |
| genshi_text     | 16.9 ms                                                | 17.4 ms: 1.03x slower                                                    |
| django_template | 22.2 ms                                                | 23.1 ms: 1.04x slower                                                    |
| genshi_xml      | 34.4 ms                                                | 40.2 ms: 1.17x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                             |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-darwin-arm64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy_memo                    | 27.4 us                                                | 17.5 us: 1.56x faster                                                    |
| deepcopy                         | 237 us                                                 | 157 us: 1.50x faster                                                     |
| unpickle_pure_python             | 164 us                                                 | 122 us: 1.34x faster                                                     |
| deepcopy_reduce                  | 2.07 us                                                | 1.56 us: 1.33x faster                                                    |
| regex_effbot                     | 2.63 ms                                                | 2.02 ms: 1.30x faster                                                    |
| tomli_loads                      | 1.57 sec                                               | 1.26 sec: 1.25x faster                                                   |
| mako                             | 7.68 ms                                                | 6.21 ms: 1.24x faster                                                    |
| scimark_sor                      | 105 ms                                                 | 87.0 ms: 1.21x faster                                                    |
| nbody                            | 74.0 ms                                                | 63.5 ms: 1.17x faster                                                    |
| xml_etree_process                | 41.0 ms                                                | 35.3 ms: 1.16x faster                                                    |
| generators                       | 31.5 ms                                                | 27.1 ms: 1.16x faster                                                    |
| pylint                           | 180 ms                                                 | 156 ms: 1.15x faster                                                     |
| go                               | 115 ms                                                 | 100 ms: 1.15x faster                                                     |
| float                            | 56.0 ms                                                | 48.9 ms: 1.15x faster                                                    |
| xml_etree_generate               | 57.0 ms                                                | 49.9 ms: 1.14x faster                                                    |
| coroutines                       | 19.8 ms                                                | 17.6 ms: 1.12x faster                                                    |
| html5lib                         | 36.6 ms                                                | 32.6 ms: 1.12x faster                                                    |
| scimark_lu                       | 76.7 ms                                                | 68.5 ms: 1.12x faster                                                    |
| scimark_monte_carlo              | 50.4 ms                                                | 45.0 ms: 1.12x faster                                                    |
| regex_compile                    | 78.6 ms                                                | 70.4 ms: 1.12x faster                                                    |
| async_tree_memoization_tg        | 288 ms                                                 | 258 ms: 1.12x faster                                                     |
| pickle_pure_python               | 214 us                                                 | 193 us: 1.11x faster                                                     |
| 2to3                             | 187 ms                                                 | 170 ms: 1.10x faster                                                     |
| regex_dna                        | 149 ms                                                 | 135 ms: 1.10x faster                                                     |
| pprint_pformat                   | 1.08 sec                                               | 990 ms: 1.09x faster                                                     |
| bpe_tokeniser                    | 3.25 sec                                               | 2.98 sec: 1.09x faster                                                   |
| spectral_norm                    | 76.3 ms                                                | 70.1 ms: 1.09x faster                                                    |
| pyflate                          | 351 ms                                                 | 323 ms: 1.09x faster                                                     |
| scimark_fft                      | 201 ms                                                 | 185 ms: 1.08x faster                                                     |
| pprint_safe_repr                 | 533 ms                                                 | 492 ms: 1.08x faster                                                     |
| connected_components             | 319 ms                                                 | 297 ms: 1.08x faster                                                     |
| regex_v8                         | 17.0 ms                                                | 15.8 ms: 1.07x faster                                                    |
| async_tree_eager_tg              | 47.8 ms                                                | 44.6 ms: 1.07x faster                                                    |
| async_tree_memoization           | 268 ms                                                 | 251 ms: 1.07x faster                                                     |
| fannkuch                         | 284 ms                                                 | 266 ms: 1.06x faster                                                     |
| telco                            | 4.76 ms                                                | 4.47 ms: 1.06x faster                                                    |
| shortest_path                    | 347 ms                                                 | 326 ms: 1.06x faster                                                     |
| thrift                           | 466 us                                                 | 440 us: 1.06x faster                                                     |
| json                             | 3.03 ms                                                | 2.88 ms: 1.05x faster                                                    |
| async_tree_eager                 | 70.1 ms                                                | 66.7 ms: 1.05x faster                                                    |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 132 ms: 1.05x faster                                                     |
| deltablue                        | 2.68 ms                                                | 2.56 ms: 1.04x faster                                                    |
| logging_simple                   | 3.60 us                                                | 3.46 us: 1.04x faster                                                    |
| pycparser                        | 705 ms                                                 | 677 ms: 1.04x faster                                                     |
| logging_format                   | 3.89 us                                                | 3.75 us: 1.04x faster                                                    |
| async_tree_eager_memoization     | 168 ms                                                 | 162 ms: 1.04x faster                                                     |
| async_tree_none                  | 215 ms                                                 | 208 ms: 1.03x faster                                                     |
| pathlib                          | 23.4 ms                                                | 22.6 ms: 1.03x faster                                                    |
| bench_thread_pool                | 505 us                                                 | 489 us: 1.03x faster                                                     |
| richards                         | 35.2 ms                                                | 34.2 ms: 1.03x faster                                                    |
| json_loads                       | 17.0 us                                                | 16.5 us: 1.03x faster                                                    |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 362 ms: 1.03x faster                                                     |
| richards_super                   | 39.1 ms                                                | 38.1 ms: 1.03x faster                                                    |
| typing_runtime_protocols         | 101 us                                                 | 99.1 us: 1.02x faster                                                    |
| sqlglot_optimize                 | 34.9 ms                                                | 34.3 ms: 1.02x faster                                                    |
| sqlglot_normalize                | 189 ms                                                 | 186 ms: 1.02x faster                                                     |
| bench_mp_pool                    | 62.5 ms                                                | 61.6 ms: 1.02x faster                                                    |
| sympy_expand                     | 246 ms                                                 | 243 ms: 1.01x faster                                                     |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.60 ms: 1.01x faster                                                    |
| nqueens                          | 62.5 ms                                                | 61.7 ms: 1.01x faster                                                    |
| sympy_sum                        | 75.4 ms                                                | 74.4 ms: 1.01x faster                                                    |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 343 ms: 1.01x faster                                                     |
| meteor_contest                   | 74.0 ms                                                | 73.2 ms: 1.01x faster                                                    |
| coverage                         | 46.0 ms                                                | 45.5 ms: 1.01x faster                                                    |
| sympy_str                        | 145 ms                                                 | 144 ms: 1.01x faster                                                     |
| crypto_pyaes                     | 54.2 ms                                                | 54.6 ms: 1.01x slower                                                    |
| sqlglot_parse                    | 856 us                                                 | 862 us: 1.01x slower                                                     |
| raytrace                         | 181 ms                                                 | 182 ms: 1.01x slower                                                     |
| sqlglot_transpile                | 1.02 ms                                                | 1.03 ms: 1.01x slower                                                    |
| gc_traversal                     | 2.91 ms                                                | 2.96 ms: 1.02x slower                                                    |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 3.05 ms: 1.02x slower                                                    |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 469 ms: 1.02x slower                                                     |
| sphinx                           | 603 ms                                                 | 618 ms: 1.03x slower                                                     |
| genshi_text                      | 16.9 ms                                                | 17.4 ms: 1.03x slower                                                    |
| sympy_integrate                  | 11.3 ms                                                | 11.7 ms: 1.03x slower                                                    |
| async_generators                 | 295 ms                                                 | 304 ms: 1.03x slower                                                     |
| docutils                         | 1.44 sec                                               | 1.49 sec: 1.03x slower                                                   |
| dulwich_log                      | 28.5 ms                                                | 29.5 ms: 1.03x slower                                                    |
| django_template                  | 22.2 ms                                                | 23.1 ms: 1.04x slower                                                    |
| python_startup_no_site           | 14.5 ms                                                | 15.1 ms: 1.04x slower                                                    |
| python_startup                   | 18.9 ms                                                | 19.8 ms: 1.05x slower                                                    |
| chaos                            | 41.2 ms                                                | 43.6 ms: 1.06x slower                                                    |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 479 ms: 1.07x slower                                                     |
| mdp                              | 1.49 sec                                               | 1.60 sec: 1.07x slower                                                   |
| logging_silent                   | 70.1 ns                                                | 75.9 ns: 1.08x slower                                                    |
| json_dumps                       | 6.52 ms                                                | 7.13 ms: 1.09x slower                                                    |
| comprehensions                   | 12.3 us                                                | 13.5 us: 1.10x slower                                                    |
| create_gc_cycles                 | 1.17 ms                                                | 1.32 ms: 1.12x slower                                                    |
| k_core                           | 1.61 sec                                               | 1.87 sec: 1.17x slower                                                   |
| genshi_xml                       | 34.4 ms                                                | 40.2 ms: 1.17x slower                                                    |
| async_tree_io                    | 507 ms                                                 | 606 ms: 1.20x slower                                                     |
| async_tree_io_tg                 | 497 ms                                                 | 595 ms: 1.20x slower                                                     |
| async_tree_eager_io              | 514 ms                                                 | 710 ms: 1.38x slower                                                     |
| async_tree_eager_io_tg           | 477 ms                                                 | 697 ms: 1.46x slower                                                     |
| Geometric mean                   | (ref)                                                  | 1.04x faster                                                             |

Benchmark hidden because not significant (7): pidigits, asyncio_websockets, sqlalchemy_declarative, hexiom, xml_etree_iterparse, xml_etree_parse, async_tree_none_tg
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, gevent_hub, mypy2, tornado_http
Ignored benchmarks (3) of results/bm-20241122-3.14.0a2+-a8a4ed3-JIT/bm-20241122-darwin-arm64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3.json: many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.037x faster
# HPT report

- Reliability score: 99.95% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x