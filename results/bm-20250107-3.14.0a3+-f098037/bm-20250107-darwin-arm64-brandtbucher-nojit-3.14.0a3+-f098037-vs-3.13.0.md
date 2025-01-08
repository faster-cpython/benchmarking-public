# Results vs. 3.13.0

- fork: brandtbucher
- ref: nojit
- machine: darwin-arm64
- commit hash: f098037
- commit date: 2025-01-07
- overall geometric mean: 1.124x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 181 ms                                                 | 160 ms: 1.13x faster                                          |
| docutils       | 1.44 sec                                               | 1.40 sec: 1.03x faster                                        |
| html5lib       | 36.6 ms                                                | 29.2 ms: 1.26x faster                                         |
| sphinx         | 600 ms                                                 | 565 ms: 1.06x faster                                          |
| Geometric mean | (ref)                                                  | 1.12x faster                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_memoization_tg        | 289 ms                                                 | 187 ms: 1.55x faster                                          |
| async_tree_eager_io              | 514 ms                                                 | 361 ms: 1.42x faster                                          |
| async_tree_io_tg                 | 499 ms                                                 | 353 ms: 1.42x faster                                          |
| async_tree_io                    | 510 ms                                                 | 366 ms: 1.39x faster                                          |
| async_tree_memoization           | 268 ms                                                 | 198 ms: 1.36x faster                                          |
| async_tree_none                  | 212 ms                                                 | 158 ms: 1.34x faster                                          |
| async_tree_none_tg               | 199 ms                                                 | 149 ms: 1.33x faster                                          |
| async_tree_eager_io_tg           | 481 ms                                                 | 369 ms: 1.30x faster                                          |
| coroutines                       | 19.8 ms                                                | 15.8 ms: 1.26x faster                                         |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.20x faster                                          |
| async_tree_eager                 | 69.9 ms                                                | 61.7 ms: 1.13x faster                                         |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 121 ms: 1.13x faster                                          |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 415 ms: 1.11x faster                                          |
| async_tree_eager_tg              | 48.0 ms                                                | 43.4 ms: 1.11x faster                                         |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 407 ms: 1.10x faster                                          |
| async_generators                 | 292 ms                                                 | 277 ms: 1.06x faster                                          |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 359 ms: 1.04x faster                                          |
| async_tree_eager_cpu_io_mixed_tg | 346 ms                                                 | 338 ms: 1.02x faster                                          |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.01x faster                                          |
| Geometric mean                   | (ref)                                                  | 1.22x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 56.3 ms                                                | 46.4 ms: 1.21x faster                                         |
| nbody          | 73.9 ms                                                | 68.1 ms: 1.08x faster                                         |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                          |
| Geometric mean | (ref)                                                  | 1.10x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_effbot   | 2.62 ms                                                | 2.04 ms: 1.28x faster                                         |
| regex_compile  | 78.6 ms                                                | 66.8 ms: 1.18x faster                                         |
| regex_dna      | 148 ms                                                 | 135 ms: 1.09x faster                                          |
| regex_v8       | 17.0 ms                                                | 15.7 ms: 1.08x faster                                         |
| Geometric mean | (ref)                                                  | 1.16x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| tomli_loads          | 1.56 sec                                               | 1.19 sec: 1.31x faster                                        |
| unpickle_pure_python | 164 us                                                 | 136 us: 1.21x faster                                          |
| xml_etree_generate   | 57.0 ms                                                | 52.4 ms: 1.09x faster                                         |
| pickle_pure_python   | 214 us                                                 | 197 us: 1.09x faster                                          |
| xml_etree_process    | 41.0 ms                                                | 38.1 ms: 1.08x faster                                         |
| xml_etree_iterparse  | 74.1 ms                                                | 71.5 ms: 1.04x faster                                         |
| xml_etree_parse      | 107 ms                                                 | 104 ms: 1.03x faster                                          |
| json_loads           | 17.0 us                                                | 16.5 us: 1.03x faster                                         |
| json_dumps           | 6.51 ms                                                | 7.26 ms: 1.12x slower                                         |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3+-f098037 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup_no_site | 15.8 ms                                                | 13.7 ms: 1.15x faster                                         |
| python_startup         | 20.6 ms                                                | 18.7 ms: 1.10x faster                                         |
| Geometric mean         | (ref)                                                  | 1.13x faster                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3+-f098037 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 13.5 ms: 1.25x faster                                         |
| genshi_xml      | 34.1 ms                                                | 28.2 ms: 1.21x faster                                         |
| mako            | 7.70 ms                                                | 6.94 ms: 1.11x faster                                         |
| django_template | 20.5 ms                                                | 20.9 ms: 1.02x slower                                         |
| Geometric mean  | (ref)                                                  | 1.13x faster                                                  |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| deepcopy                         | 234 us                                                 | 149 us: 1.57x faster                                          |
| async_tree_memoization_tg        | 289 ms                                                 | 187 ms: 1.55x faster                                          |
| deepcopy_memo                    | 27.3 us                                                | 18.0 us: 1.52x faster                                         |
| go                               | 115 ms                                                 | 78.2 ms: 1.47x faster                                         |
| generators                       | 31.5 ms                                                | 22.1 ms: 1.42x faster                                         |
| async_tree_eager_io              | 514 ms                                                 | 361 ms: 1.42x faster                                          |
| async_tree_io_tg                 | 499 ms                                                 | 353 ms: 1.42x faster                                          |
| async_tree_io                    | 510 ms                                                 | 366 ms: 1.39x faster                                          |
| async_tree_memoization           | 268 ms                                                 | 198 ms: 1.36x faster                                          |
| deepcopy_reduce                  | 2.08 us                                                | 1.55 us: 1.35x faster                                         |
| scimark_sor                      | 106 ms                                                 | 78.5 ms: 1.35x faster                                         |
| async_tree_none                  | 212 ms                                                 | 158 ms: 1.34x faster                                          |
| async_tree_none_tg               | 199 ms                                                 | 149 ms: 1.33x faster                                          |
| tomli_loads                      | 1.56 sec                                               | 1.19 sec: 1.31x faster                                        |
| async_tree_eager_io_tg           | 481 ms                                                 | 369 ms: 1.30x faster                                          |
| regex_effbot                     | 2.62 ms                                                | 2.04 ms: 1.28x faster                                         |
| html5lib                         | 36.6 ms                                                | 29.2 ms: 1.26x faster                                         |
| coroutines                       | 19.8 ms                                                | 15.8 ms: 1.26x faster                                         |
| genshi_text                      | 16.9 ms                                                | 13.5 ms: 1.25x faster                                         |
| spectral_norm                    | 76.3 ms                                                | 61.7 ms: 1.24x faster                                         |
| pyflate                          | 355 ms                                                 | 289 ms: 1.23x faster                                          |
| scimark_monte_carlo              | 50.6 ms                                                | 41.5 ms: 1.22x faster                                         |
| float                            | 56.3 ms                                                | 46.4 ms: 1.21x faster                                         |
| genshi_xml                       | 34.1 ms                                                | 28.2 ms: 1.21x faster                                         |
| unpickle_pure_python             | 164 us                                                 | 136 us: 1.21x faster                                          |
| pprint_pformat                   | 1.10 sec                                               | 913 ms: 1.20x faster                                          |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.20x faster                                          |
| pprint_safe_repr                 | 535 ms                                                 | 452 ms: 1.18x faster                                          |
| regex_compile                    | 78.6 ms                                                | 66.8 ms: 1.18x faster                                         |
| scimark_fft                      | 200 ms                                                 | 171 ms: 1.17x faster                                          |
| hexiom                           | 4.83 ms                                                | 4.14 ms: 1.17x faster                                         |
| fannkuch                         | 285 ms                                                 | 244 ms: 1.17x faster                                          |
| python_startup_no_site           | 15.8 ms                                                | 13.7 ms: 1.15x faster                                         |
| logging_simple                   | 3.59 us                                                | 3.13 us: 1.15x faster                                         |
| deltablue                        | 2.67 ms                                                | 2.34 ms: 1.14x faster                                         |
| logging_format                   | 3.90 us                                                | 3.44 us: 1.13x faster                                         |
| async_tree_eager                 | 69.9 ms                                                | 61.7 ms: 1.13x faster                                         |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 121 ms: 1.13x faster                                          |
| pylint                           | 179 ms                                                 | 159 ms: 1.13x faster                                          |
| 2to3                             | 181 ms                                                 | 160 ms: 1.13x faster                                          |
| scimark_sparse_mat_mult          | 3.00 ms                                                | 2.65 ms: 1.13x faster                                         |
| sqlglot_parse                    | 859 us                                                 | 763 us: 1.13x faster                                          |
| richards                         | 35.2 ms                                                | 31.5 ms: 1.12x faster                                         |
| richards_super                   | 39.2 ms                                                | 35.2 ms: 1.11x faster                                         |
| pycparser                        | 708 ms                                                 | 637 ms: 1.11x faster                                          |
| mako                             | 7.70 ms                                                | 6.94 ms: 1.11x faster                                         |
| sqlglot_transpile                | 1.03 ms                                                | 927 us: 1.11x faster                                          |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 415 ms: 1.11x faster                                          |
| async_tree_eager_tg              | 48.0 ms                                                | 43.4 ms: 1.11x faster                                         |
| python_startup                   | 20.6 ms                                                | 18.7 ms: 1.10x faster                                         |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 407 ms: 1.10x faster                                          |
| nqueens                          | 61.8 ms                                                | 56.2 ms: 1.10x faster                                         |
| regex_dna                        | 148 ms                                                 | 135 ms: 1.09x faster                                          |
| bpe_tokeniser                    | 3.25 sec                                               | 2.97 sec: 1.09x faster                                        |
| k_core                           | 1.62 sec                                               | 1.48 sec: 1.09x faster                                        |
| xml_etree_generate               | 57.0 ms                                                | 52.4 ms: 1.09x faster                                         |
| pickle_pure_python               | 214 us                                                 | 197 us: 1.09x faster                                          |
| json                             | 3.06 ms                                                | 2.82 ms: 1.09x faster                                         |
| nbody                            | 73.9 ms                                                | 68.1 ms: 1.08x faster                                         |
| chaos                            | 41.3 ms                                                | 38.0 ms: 1.08x faster                                         |
| regex_v8                         | 17.0 ms                                                | 15.7 ms: 1.08x faster                                         |
| logging_silent                   | 70.1 ns                                                | 64.8 ns: 1.08x faster                                         |
| connected_components             | 320 ms                                                 | 297 ms: 1.08x faster                                          |
| xml_etree_process                | 41.0 ms                                                | 38.1 ms: 1.08x faster                                         |
| raytrace                         | 181 ms                                                 | 169 ms: 1.07x faster                                          |
| bench_thread_pool                | 508 us                                                 | 474 us: 1.07x faster                                          |
| shortest_path                    | 349 ms                                                 | 325 ms: 1.07x faster                                          |
| typing_runtime_protocols         | 103 us                                                 | 95.9 us: 1.07x faster                                         |
| sqlglot_optimize                 | 34.8 ms                                                | 32.5 ms: 1.07x faster                                         |
| bench_mp_pool                    | 64.9 ms                                                | 60.9 ms: 1.07x faster                                         |
| thrift                           | 465 us                                                 | 437 us: 1.07x faster                                          |
| meteor_contest                   | 75.1 ms                                                | 70.6 ms: 1.06x faster                                         |
| dulwich_log                      | 28.6 ms                                                | 26.9 ms: 1.06x faster                                         |
| sphinx                           | 600 ms                                                 | 565 ms: 1.06x faster                                          |
| scimark_lu                       | 76.7 ms                                                | 72.5 ms: 1.06x faster                                         |
| async_generators                 | 292 ms                                                 | 277 ms: 1.06x faster                                          |
| sympy_expand                     | 247 ms                                                 | 234 ms: 1.06x faster                                          |
| sqlglot_normalize                | 188 ms                                                 | 178 ms: 1.05x faster                                          |
| telco                            | 4.79 ms                                                | 4.56 ms: 1.05x faster                                         |
| sympy_str                        | 145 ms                                                 | 138 ms: 1.05x faster                                          |
| pathlib                          | 23.3 ms                                                | 22.3 ms: 1.05x faster                                         |
| sqlalchemy_imperative            | 6.68 ms                                                | 6.41 ms: 1.04x faster                                         |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 359 ms: 1.04x faster                                          |
| xml_etree_iterparse              | 74.1 ms                                                | 71.5 ms: 1.04x faster                                         |
| xml_etree_parse                  | 107 ms                                                 | 104 ms: 1.03x faster                                          |
| json_loads                       | 17.0 us                                                | 16.5 us: 1.03x faster                                         |
| docutils                         | 1.44 sec                                               | 1.40 sec: 1.03x faster                                        |
| crypto_pyaes                     | 54.4 ms                                                | 52.8 ms: 1.03x faster                                         |
| async_tree_eager_cpu_io_mixed_tg | 346 ms                                                 | 338 ms: 1.02x faster                                          |
| sympy_sum                        | 75.1 ms                                                | 73.5 ms: 1.02x faster                                         |
| sqlalchemy_declarative           | 59.1 ms                                                | 57.8 ms: 1.02x faster                                         |
| sympy_integrate                  | 11.3 ms                                                | 11.1 ms: 1.02x faster                                         |
| sqlite_synth                     | 1.56 us                                                | 1.53 us: 1.02x faster                                         |
| mdp                              | 1.50 sec                                               | 1.49 sec: 1.01x faster                                        |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.01x faster                                          |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                          |
| coverage                         | 45.5 ms                                                | 46.1 ms: 1.01x slower                                         |
| django_template                  | 20.5 ms                                                | 20.9 ms: 1.02x slower                                         |
| comprehensions                   | 12.0 us                                                | 12.4 us: 1.04x slower                                         |
| create_gc_cycles                 | 1.20 ms                                                | 1.28 ms: 1.07x slower                                         |
| gc_traversal                     | 2.93 ms                                                | 3.22 ms: 1.10x slower                                         |
| json_dumps                       | 6.51 ms                                                | 7.26 ms: 1.12x slower                                         |
| subparsers                       | 9.50 ms                                                | 11.8 ms: 1.24x slower                                         |
| many_optionals                   | 324 us                                                 | 439 us: 1.35x slower                                          |
| Geometric mean                   | (ref)                                                  | 1.12x faster                                                  |
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20250107-3.14.0a3+-f098037/bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3+-f098037.json: mypy2

- Geometric mean (including insignificant results): 1.124x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.03x