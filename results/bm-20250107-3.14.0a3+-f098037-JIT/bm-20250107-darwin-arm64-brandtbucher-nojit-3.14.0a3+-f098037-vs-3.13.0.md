# Results vs. 3.13.0

- fork: brandtbucher
- ref: nojit
- machine: darwin-arm64
- commit hash: f098037
- commit date: 2025-01-07
- overall geometric mean: 1.091x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 181 ms                                                 | 165 ms: 1.10x faster                                          |
| html5lib       | 36.6 ms                                                | 31.2 ms: 1.17x faster                                         |
| sphinx         | 600 ms                                                 | 589 ms: 1.02x faster                                          |
| Geometric mean | (ref)                                                  | 1.07x faster                                                  |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_memoization_tg        | 289 ms                                                 | 188 ms: 1.54x faster                                          |
| async_tree_io_tg                 | 499 ms                                                 | 352 ms: 1.42x faster                                          |
| async_tree_eager_io              | 514 ms                                                 | 363 ms: 1.42x faster                                          |
| async_tree_io                    | 510 ms                                                 | 366 ms: 1.39x faster                                          |
| async_tree_memoization           | 268 ms                                                 | 200 ms: 1.34x faster                                          |
| async_tree_none                  | 212 ms                                                 | 159 ms: 1.33x faster                                          |
| async_tree_none_tg               | 199 ms                                                 | 149 ms: 1.33x faster                                          |
| async_tree_eager_io_tg           | 481 ms                                                 | 368 ms: 1.31x faster                                          |
| coroutines                       | 19.8 ms                                                | 15.8 ms: 1.26x faster                                         |
| async_tree_eager_memoization     | 168 ms                                                 | 144 ms: 1.17x faster                                          |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 124 ms: 1.11x faster                                          |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 408 ms: 1.10x faster                                          |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 420 ms: 1.10x faster                                          |
| async_tree_eager_tg              | 48.0 ms                                                | 43.9 ms: 1.09x faster                                         |
| async_tree_eager                 | 69.9 ms                                                | 65.3 ms: 1.07x faster                                         |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 364 ms: 1.02x faster                                          |
| async_tree_eager_cpu_io_mixed_tg | 346 ms                                                 | 339 ms: 1.02x faster                                          |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.01x faster                                          |
| async_generators                 | 292 ms                                                 | 301 ms: 1.03x slower                                          |
| Geometric mean                   | (ref)                                                  | 1.20x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 56.3 ms                                                | 44.6 ms: 1.26x faster                                         |
| nbody          | 73.9 ms                                                | 63.5 ms: 1.16x faster                                         |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                          |
| Geometric mean | (ref)                                                  | 1.14x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_effbot   | 2.62 ms                                                | 2.01 ms: 1.30x faster                                         |
| regex_compile  | 78.6 ms                                                | 67.6 ms: 1.16x faster                                         |
| regex_dna      | 148 ms                                                 | 136 ms: 1.09x faster                                          |
| regex_v8       | 17.0 ms                                                | 15.9 ms: 1.07x faster                                         |
| Geometric mean | (ref)                                                  | 1.15x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| tomli_loads          | 1.56 sec                                               | 1.18 sec: 1.33x faster                                        |
| unpickle_pure_python | 164 us                                                 | 124 us: 1.33x faster                                          |
| xml_etree_process    | 41.0 ms                                                | 35.5 ms: 1.15x faster                                         |
| pickle_pure_python   | 214 us                                                 | 187 us: 1.14x faster                                          |
| xml_etree_generate   | 57.0 ms                                                | 50.0 ms: 1.14x faster                                         |
| xml_etree_iterparse  | 74.1 ms                                                | 70.0 ms: 1.06x faster                                         |
| xml_etree_parse      | 107 ms                                                 | 102 ms: 1.05x faster                                          |
| json_loads           | 17.0 us                                                | 16.4 us: 1.04x faster                                         |
| json_dumps           | 6.51 ms                                                | 7.12 ms: 1.09x slower                                         |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3+-f098037 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup_no_site | 15.8 ms                                                | 13.8 ms: 1.14x faster                                         |
| python_startup         | 20.6 ms                                                | 18.8 ms: 1.10x faster                                         |
| Geometric mean         | (ref)                                                  | 1.12x faster                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3+-f098037 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mako            | 7.70 ms                                                | 6.26 ms: 1.23x faster                                         |
| genshi_text     | 16.9 ms                                                | 15.6 ms: 1.09x faster                                         |
| django_template | 20.5 ms                                                | 22.7 ms: 1.11x slower                                         |
| genshi_xml      | 34.1 ms                                                | 39.2 ms: 1.15x slower                                         |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                  |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| deepcopy_memo                    | 27.3 us                                                | 17.1 us: 1.60x faster                                         |
| async_tree_memoization_tg        | 289 ms                                                 | 188 ms: 1.54x faster                                          |
| deepcopy                         | 234 us                                                 | 156 us: 1.50x faster                                          |
| async_tree_io_tg                 | 499 ms                                                 | 352 ms: 1.42x faster                                          |
| async_tree_eager_io              | 514 ms                                                 | 363 ms: 1.42x faster                                          |
| async_tree_io                    | 510 ms                                                 | 366 ms: 1.39x faster                                          |
| deepcopy_reduce                  | 2.08 us                                                | 1.55 us: 1.35x faster                                         |
| async_tree_memoization           | 268 ms                                                 | 200 ms: 1.34x faster                                          |
| async_tree_none                  | 212 ms                                                 | 159 ms: 1.33x faster                                          |
| async_tree_none_tg               | 199 ms                                                 | 149 ms: 1.33x faster                                          |
| tomli_loads                      | 1.56 sec                                               | 1.18 sec: 1.33x faster                                        |
| unpickle_pure_python             | 164 us                                                 | 124 us: 1.33x faster                                          |
| async_tree_eager_io_tg           | 481 ms                                                 | 368 ms: 1.31x faster                                          |
| regex_effbot                     | 2.62 ms                                                | 2.01 ms: 1.30x faster                                         |
| scimark_sor                      | 106 ms                                                 | 81.7 ms: 1.29x faster                                         |
| float                            | 56.3 ms                                                | 44.6 ms: 1.26x faster                                         |
| coroutines                       | 19.8 ms                                                | 15.8 ms: 1.26x faster                                         |
| spectral_norm                    | 76.3 ms                                                | 62.0 ms: 1.23x faster                                         |
| mako                             | 7.70 ms                                                | 6.26 ms: 1.23x faster                                         |
| go                               | 115 ms                                                 | 96.1 ms: 1.20x faster                                         |
| scimark_fft                      | 200 ms                                                 | 170 ms: 1.17x faster                                          |
| html5lib                         | 36.6 ms                                                | 31.2 ms: 1.17x faster                                         |
| async_tree_eager_memoization     | 168 ms                                                 | 144 ms: 1.17x faster                                          |
| regex_compile                    | 78.6 ms                                                | 67.6 ms: 1.16x faster                                         |
| nbody                            | 73.9 ms                                                | 63.5 ms: 1.16x faster                                         |
| generators                       | 31.5 ms                                                | 27.1 ms: 1.16x faster                                         |
| xml_etree_process                | 41.0 ms                                                | 35.5 ms: 1.15x faster                                         |
| pyflate                          | 355 ms                                                 | 308 ms: 1.15x faster                                          |
| pickle_pure_python               | 214 us                                                 | 187 us: 1.14x faster                                          |
| xml_etree_generate               | 57.0 ms                                                | 50.0 ms: 1.14x faster                                         |
| python_startup_no_site           | 15.8 ms                                                | 13.8 ms: 1.14x faster                                         |
| scimark_monte_carlo              | 50.6 ms                                                | 44.7 ms: 1.13x faster                                         |
| pprint_pformat                   | 1.10 sec                                               | 977 ms: 1.12x faster                                          |
| scimark_lu                       | 76.7 ms                                                | 68.7 ms: 1.12x faster                                         |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 124 ms: 1.11x faster                                          |
| bpe_tokeniser                    | 3.25 sec                                               | 2.94 sec: 1.11x faster                                        |
| pprint_safe_repr                 | 535 ms                                                 | 484 ms: 1.11x faster                                          |
| 2to3                             | 181 ms                                                 | 165 ms: 1.10x faster                                          |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 408 ms: 1.10x faster                                          |
| python_startup                   | 20.6 ms                                                | 18.8 ms: 1.10x faster                                         |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 420 ms: 1.10x faster                                          |
| async_tree_eager_tg              | 48.0 ms                                                | 43.9 ms: 1.09x faster                                         |
| regex_dna                        | 148 ms                                                 | 136 ms: 1.09x faster                                          |
| pylint                           | 179 ms                                                 | 165 ms: 1.09x faster                                          |
| genshi_text                      | 16.9 ms                                                | 15.6 ms: 1.09x faster                                         |
| connected_components             | 320 ms                                                 | 296 ms: 1.08x faster                                          |
| telco                            | 4.79 ms                                                | 4.44 ms: 1.08x faster                                         |
| json                             | 3.06 ms                                                | 2.85 ms: 1.07x faster                                         |
| deltablue                        | 2.67 ms                                                | 2.49 ms: 1.07x faster                                         |
| bench_mp_pool                    | 64.9 ms                                                | 60.5 ms: 1.07x faster                                         |
| k_core                           | 1.62 sec                                               | 1.51 sec: 1.07x faster                                        |
| async_tree_eager                 | 69.9 ms                                                | 65.3 ms: 1.07x faster                                         |
| shortest_path                    | 349 ms                                                 | 326 ms: 1.07x faster                                          |
| regex_v8                         | 17.0 ms                                                | 15.9 ms: 1.07x faster                                         |
| fannkuch                         | 285 ms                                                 | 269 ms: 1.06x faster                                          |
| xml_etree_iterparse              | 74.1 ms                                                | 70.0 ms: 1.06x faster                                         |
| logging_simple                   | 3.59 us                                                | 3.40 us: 1.06x faster                                         |
| richards_super                   | 39.2 ms                                                | 37.1 ms: 1.05x faster                                         |
| pycparser                        | 708 ms                                                 | 672 ms: 1.05x faster                                          |
| richards                         | 35.2 ms                                                | 33.4 ms: 1.05x faster                                         |
| thrift                           | 465 us                                                 | 443 us: 1.05x faster                                          |
| xml_etree_parse                  | 107 ms                                                 | 102 ms: 1.05x faster                                          |
| scimark_sparse_mat_mult          | 3.00 ms                                                | 2.87 ms: 1.05x faster                                         |
| typing_runtime_protocols         | 103 us                                                 | 98.2 us: 1.04x faster                                         |
| logging_format                   | 3.90 us                                                | 3.74 us: 1.04x faster                                         |
| meteor_contest                   | 75.1 ms                                                | 72.5 ms: 1.04x faster                                         |
| json_loads                       | 17.0 us                                                | 16.4 us: 1.04x faster                                         |
| sqlglot_parse                    | 859 us                                                 | 837 us: 1.03x faster                                          |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 364 ms: 1.02x faster                                          |
| bench_thread_pool                | 508 us                                                 | 497 us: 1.02x faster                                          |
| pathlib                          | 23.3 ms                                                | 22.8 ms: 1.02x faster                                         |
| sympy_expand                     | 247 ms                                                 | 242 ms: 1.02x faster                                          |
| nqueens                          | 61.8 ms                                                | 60.5 ms: 1.02x faster                                         |
| async_tree_eager_cpu_io_mixed_tg | 346 ms                                                 | 339 ms: 1.02x faster                                          |
| crypto_pyaes                     | 54.4 ms                                                | 53.3 ms: 1.02x faster                                         |
| sphinx                           | 600 ms                                                 | 589 ms: 1.02x faster                                          |
| sqlglot_optimize                 | 34.8 ms                                                | 34.2 ms: 1.02x faster                                         |
| sympy_str                        | 145 ms                                                 | 143 ms: 1.01x faster                                          |
| sqlglot_transpile                | 1.03 ms                                                | 1.02 ms: 1.01x faster                                         |
| dulwich_log                      | 28.6 ms                                                | 28.4 ms: 1.01x faster                                         |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.01x faster                                          |
| sqlglot_normalize                | 188 ms                                                 | 188 ms: 1.00x faster                                          |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                          |
| hexiom                           | 4.83 ms                                                | 4.87 ms: 1.01x slower                                         |
| coverage                         | 45.5 ms                                                | 45.9 ms: 1.01x slower                                         |
| chaos                            | 41.3 ms                                                | 41.9 ms: 1.01x slower                                         |
| sympy_integrate                  | 11.3 ms                                                | 11.5 ms: 1.01x slower                                         |
| raytrace                         | 181 ms                                                 | 185 ms: 1.02x slower                                          |
| async_generators                 | 292 ms                                                 | 301 ms: 1.03x slower                                          |
| gc_traversal                     | 2.93 ms                                                | 3.07 ms: 1.05x slower                                         |
| create_gc_cycles                 | 1.20 ms                                                | 1.27 ms: 1.06x slower                                         |
| mdp                              | 1.50 sec                                               | 1.60 sec: 1.07x slower                                        |
| logging_silent                   | 70.1 ns                                                | 75.8 ns: 1.08x slower                                         |
| json_dumps                       | 6.51 ms                                                | 7.12 ms: 1.09x slower                                         |
| django_template                  | 20.5 ms                                                | 22.7 ms: 1.11x slower                                         |
| genshi_xml                       | 34.1 ms                                                | 39.2 ms: 1.15x slower                                         |
| comprehensions                   | 12.0 us                                                | 13.8 us: 1.15x slower                                         |
| subparsers                       | 9.50 ms                                                | 12.0 ms: 1.27x slower                                         |
| many_optionals                   | 324 us                                                 | 455 us: 1.40x slower                                          |
| Geometric mean                   | (ref)                                                  | 1.09x faster                                                  |

Benchmark hidden because not significant (5): sqlalchemy_imperative, sqlalchemy_declarative, sympy_sum, sqlite_synth, docutils
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20250107-3.14.0a3+-f098037-JIT/bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3+-f098037.json: mypy2

- Geometric mean (including insignificant results): 1.091x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.05x