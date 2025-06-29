# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_o2
- machine: darwin-arm64
- commit hash: f528bf3
- commit date: 2025-06-28
- overall geometric mean: 1.060x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-darwin-arm64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 174 ms: 1.03x faster                                          |
| docutils       | 1.44 sec                                               | 1.47 sec: 1.02x slower                                        |
| html5lib       | 36.7 ms                                                | 31.5 ms: 1.16x faster                                         |
| sphinx         | 602 ms                                                 | 587 ms: 1.03x faster                                          |
| Geometric mean | (ref)                                                  | 1.05x faster                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-darwin-arm64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 192 ms: 1.50x faster                                          |
| async_tree_eager_io              | 511 ms                                                 | 361 ms: 1.42x faster                                          |
| async_tree_memoization           | 268 ms                                                 | 194 ms: 1.38x faster                                          |
| async_tree_io                    | 508 ms                                                 | 376 ms: 1.35x faster                                          |
| async_tree_io_tg                 | 500 ms                                                 | 378 ms: 1.32x faster                                          |
| async_tree_none                  | 212 ms                                                 | 163 ms: 1.30x faster                                          |
| async_tree_eager_io_tg           | 479 ms                                                 | 372 ms: 1.29x faster                                          |
| async_tree_none_tg               | 198 ms                                                 | 156 ms: 1.27x faster                                          |
| async_tree_eager_memoization     | 168 ms                                                 | 141 ms: 1.19x faster                                          |
| coroutines                       | 20.0 ms                                                | 17.1 ms: 1.17x faster                                         |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 415 ms: 1.11x faster                                          |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 411 ms: 1.09x faster                                          |
| async_tree_eager                 | 69.9 ms                                                | 64.6 ms: 1.08x faster                                         |
| async_generators                 | 294 ms                                                 | 277 ms: 1.06x faster                                          |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 359 ms: 1.04x faster                                          |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 390 ms: 1.12x slower                                          |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 168 ms: 1.22x slower                                          |
| async_tree_eager_tg              | 47.4 ms                                                | 129 ms: 2.71x slower                                          |
| Geometric mean                   | (ref)                                                  | 1.10x faster                                                  |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-darwin-arm64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 55.8 ms                                                | 49.9 ms: 1.12x faster                                         |
| nbody          | 73.6 ms                                                | 75.7 ms: 1.03x slower                                         |
| Geometric mean | (ref)                                                  | 1.03x faster                                                  |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-darwin-arm64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.36 ms: 1.11x faster                                         |
| regex_compile  | 78.3 ms                                                | 71.3 ms: 1.10x faster                                         |
| regex_v8       | 17.0 ms                                                | 16.1 ms: 1.05x faster                                         |
| regex_dna      | 149 ms                                                 | 143 ms: 1.04x faster                                          |
| Geometric mean | (ref)                                                  | 1.08x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-darwin-arm64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.23 sec: 1.27x faster                                        |
| unpickle_pure_python | 165 us                                                 | 134 us: 1.24x faster                                          |
| xml_etree_process    | 41.3 ms                                                | 36.0 ms: 1.15x faster                                         |
| xml_etree_generate   | 57.1 ms                                                | 51.1 ms: 1.12x faster                                         |
| xml_etree_parse      | 108 ms                                                 | 102 ms: 1.06x faster                                          |
| json_loads           | 17.0 us                                                | 16.4 us: 1.04x faster                                         |
| xml_etree_iterparse  | 74.2 ms                                                | 72.3 ms: 1.03x faster                                         |
| pickle_pure_python   | 215 us                                                 | 210 us: 1.02x faster                                          |
| json_dumps           | 6.47 ms                                                | 6.55 ms: 1.01x slower                                         |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-darwin-arm64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 18.5 ms: 1.02x faster                                         |
| python_startup_no_site | 13.7 ms                                                | 14.0 ms: 1.02x slower                                         |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-darwin-arm64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 14.8 ms: 1.14x faster                                         |
| mako            | 7.75 ms                                                | 6.94 ms: 1.12x faster                                         |
| genshi_xml      | 34.1 ms                                                | 31.1 ms: 1.09x faster                                         |
| django_template | 20.5 ms                                                | 21.9 ms: 1.07x slower                                         |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                  |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-darwin-arm64-brandtbucher-jit_o2-3.15.0a0-f528bf3 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 759 ms: 1.97x faster                                          |
| deepcopy                         | 236 us                                                 | 156 us: 1.51x faster                                          |
| async_tree_memoization_tg        | 288 ms                                                 | 192 ms: 1.50x faster                                          |
| async_tree_eager_io              | 511 ms                                                 | 361 ms: 1.42x faster                                          |
| deepcopy_memo                    | 27.4 us                                                | 19.5 us: 1.40x faster                                         |
| async_tree_memoization           | 268 ms                                                 | 194 ms: 1.38x faster                                          |
| async_tree_io                    | 508 ms                                                 | 376 ms: 1.35x faster                                          |
| go                               | 117 ms                                                 | 87.6 ms: 1.33x faster                                         |
| generators                       | 31.9 ms                                                | 24.1 ms: 1.32x faster                                         |
| async_tree_io_tg                 | 500 ms                                                 | 378 ms: 1.32x faster                                          |
| async_tree_none                  | 212 ms                                                 | 163 ms: 1.30x faster                                          |
| async_tree_eager_io_tg           | 479 ms                                                 | 372 ms: 1.29x faster                                          |
| async_tree_none_tg               | 198 ms                                                 | 156 ms: 1.27x faster                                          |
| tomli_loads                      | 1.57 sec                                               | 1.23 sec: 1.27x faster                                        |
| deepcopy_reduce                  | 2.09 us                                                | 1.67 us: 1.25x faster                                         |
| unpickle_pure_python             | 165 us                                                 | 134 us: 1.24x faster                                          |
| pyflate                          | 352 ms                                                 | 292 ms: 1.21x faster                                          |
| async_tree_eager_memoization     | 168 ms                                                 | 141 ms: 1.19x faster                                          |
| scimark_sor                      | 106 ms                                                 | 89.0 ms: 1.19x faster                                         |
| coroutines                       | 20.0 ms                                                | 17.1 ms: 1.17x faster                                         |
| html5lib                         | 36.7 ms                                                | 31.5 ms: 1.16x faster                                         |
| dulwich_log                      | 28.7 ms                                                | 24.9 ms: 1.15x faster                                         |
| xml_etree_process                | 41.3 ms                                                | 36.0 ms: 1.15x faster                                         |
| genshi_text                      | 16.9 ms                                                | 14.8 ms: 1.14x faster                                         |
| spectral_norm                    | 76.5 ms                                                | 67.9 ms: 1.13x faster                                         |
| float                            | 55.8 ms                                                | 49.9 ms: 1.12x faster                                         |
| xml_etree_generate               | 57.1 ms                                                | 51.1 ms: 1.12x faster                                         |
| mako                             | 7.75 ms                                                | 6.94 ms: 1.12x faster                                         |
| regex_effbot                     | 2.63 ms                                                | 2.36 ms: 1.11x faster                                         |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 415 ms: 1.11x faster                                          |
| pylint                           | 180 ms                                                 | 163 ms: 1.10x faster                                          |
| scimark_monte_carlo              | 50.4 ms                                                | 45.9 ms: 1.10x faster                                         |
| regex_compile                    | 78.3 ms                                                | 71.3 ms: 1.10x faster                                         |
| genshi_xml                       | 34.1 ms                                                | 31.1 ms: 1.09x faster                                         |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 411 ms: 1.09x faster                                          |
| async_tree_eager                 | 69.9 ms                                                | 64.6 ms: 1.08x faster                                         |
| async_generators                 | 294 ms                                                 | 277 ms: 1.06x faster                                          |
| k_core                           | 1.61 sec                                               | 1.52 sec: 1.06x faster                                        |
| thrift                           | 466 us                                                 | 440 us: 1.06x faster                                          |
| xml_etree_parse                  | 108 ms                                                 | 102 ms: 1.06x faster                                          |
| bpe_tokeniser                    | 3.26 sec                                               | 3.08 sec: 1.06x faster                                        |
| regex_v8                         | 17.0 ms                                                | 16.1 ms: 1.05x faster                                         |
| json                             | 3.04 ms                                                | 2.91 ms: 1.05x faster                                         |
| telco                            | 4.84 ms                                                | 4.64 ms: 1.04x faster                                         |
| regex_dna                        | 149 ms                                                 | 143 ms: 1.04x faster                                          |
| chaos                            | 41.1 ms                                                | 39.5 ms: 1.04x faster                                         |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 359 ms: 1.04x faster                                          |
| json_loads                       | 17.0 us                                                | 16.4 us: 1.04x faster                                         |
| pathlib                          | 23.2 ms                                                | 22.4 ms: 1.04x faster                                         |
| xml_etree_iterparse              | 74.2 ms                                                | 72.3 ms: 1.03x faster                                         |
| 2to3                             | 179 ms                                                 | 174 ms: 1.03x faster                                          |
| pprint_safe_repr                 | 541 ms                                                 | 527 ms: 1.03x faster                                          |
| shortest_path                    | 345 ms                                                 | 337 ms: 1.03x faster                                          |
| sphinx                           | 602 ms                                                 | 587 ms: 1.03x faster                                          |
| typing_runtime_protocols         | 101 us                                                 | 98.2 us: 1.03x faster                                         |
| connected_components             | 319 ms                                                 | 311 ms: 1.03x faster                                          |
| logging_simple                   | 3.56 us                                                | 3.48 us: 1.02x faster                                         |
| hexiom                           | 4.87 ms                                                | 4.76 ms: 1.02x faster                                         |
| sympy_integrate                  | 11.3 ms                                                | 11.1 ms: 1.02x faster                                         |
| pickle_pure_python               | 215 us                                                 | 210 us: 1.02x faster                                          |
| logging_format                   | 3.85 us                                                | 3.77 us: 1.02x faster                                         |
| pprint_pformat                   | 1.10 sec                                               | 1.08 sec: 1.02x faster                                        |
| python_startup                   | 18.8 ms                                                | 18.5 ms: 1.02x faster                                         |
| sympy_expand                     | 248 ms                                                 | 244 ms: 1.01x faster                                          |
| sympy_str                        | 146 ms                                                 | 144 ms: 1.01x faster                                          |
| raytrace                         | 181 ms                                                 | 179 ms: 1.01x faster                                          |
| dask                             | 771 ms                                                 | 766 ms: 1.01x faster                                          |
| scimark_fft                      | 200 ms                                                 | 200 ms: 1.00x slower                                          |
| richards                         | 36.2 ms                                                | 36.4 ms: 1.01x slower                                         |
| crypto_pyaes                     | 55.3 ms                                                | 56.0 ms: 1.01x slower                                         |
| json_dumps                       | 6.47 ms                                                | 6.55 ms: 1.01x slower                                         |
| pycparser                        | 701 ms                                                 | 712 ms: 1.02x slower                                          |
| python_startup_no_site           | 13.7 ms                                                | 14.0 ms: 1.02x slower                                         |
| comprehensions                   | 12.0 us                                                | 12.2 us: 1.02x slower                                         |
| sqlite_synth                     | 1.55 us                                                | 1.58 us: 1.02x slower                                         |
| docutils                         | 1.44 sec                                               | 1.47 sec: 1.02x slower                                        |
| logging_silent                   | 71.0 ns                                                | 72.8 ns: 1.03x slower                                         |
| meteor_contest                   | 74.0 ms                                                | 75.9 ms: 1.03x slower                                         |
| nbody                            | 73.6 ms                                                | 75.7 ms: 1.03x slower                                         |
| coverage                         | 46.2 ms                                                | 48.4 ms: 1.05x slower                                         |
| richards_super                   | 39.2 ms                                                | 41.1 ms: 1.05x slower                                         |
| django_template                  | 20.5 ms                                                | 21.9 ms: 1.07x slower                                         |
| fannkuch                         | 279 ms                                                 | 302 ms: 1.08x slower                                          |
| scimark_lu                       | 75.9 ms                                                | 82.4 ms: 1.09x slower                                         |
| gc_traversal                     | 2.94 ms                                                | 3.19 ms: 1.09x slower                                         |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 390 ms: 1.12x slower                                          |
| create_gc_cycles                 | 1.19 ms                                                | 1.35 ms: 1.13x slower                                         |
| many_optionals                   | 409 us                                                 | 479 us: 1.17x slower                                          |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.58 ms: 1.20x slower                                         |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 168 ms: 1.22x slower                                          |
| subparsers                       | 9.44 ms                                                | 13.8 ms: 1.46x slower                                         |
| async_tree_eager_tg              | 47.4 ms                                                | 129 ms: 2.71x slower                                          |
| Geometric mean                   | (ref)                                                  | 1.06x faster                                                  |

Benchmark hidden because not significant (5): asyncio_websockets, pidigits, sympy_sum, nqueens, deltablue
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250628-3.15.0a0-f528bf3-JIT/bm-20250628-darwin-arm64-brandtbucher-jit_o2-3.15.0a0-f528bf3.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.060x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.13x