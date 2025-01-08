# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: tail_call
- machine: darwin-arm64
- commit hash: f1d3190
- commit date: 2025-01-07
- overall geometric mean: 1.187x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 181 ms                                                 | 151 ms: 1.20x faster                                                  |
| docutils       | 1.44 sec                                               | 1.37 sec: 1.06x faster                                                |
| html5lib       | 36.6 ms                                                | 29.0 ms: 1.26x faster                                                 |
| sphinx         | 600 ms                                                 | 539 ms: 1.11x faster                                                  |
| Geometric mean | (ref)                                                  | 1.16x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 289 ms                                                 | 181 ms: 1.60x faster                                                  |
| async_tree_eager_io              | 514 ms                                                 | 340 ms: 1.51x faster                                                  |
| async_tree_io_tg                 | 499 ms                                                 | 331 ms: 1.51x faster                                                  |
| async_tree_io                    | 510 ms                                                 | 348 ms: 1.47x faster                                                  |
| async_tree_none_tg               | 199 ms                                                 | 138 ms: 1.44x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 191 ms: 1.41x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 152 ms: 1.39x faster                                                  |
| async_tree_eager_io_tg           | 481 ms                                                 | 345 ms: 1.39x faster                                                  |
| coroutines                       | 19.8 ms                                                | 14.7 ms: 1.35x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 135 ms: 1.25x faster                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 115 ms: 1.19x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 58.8 ms: 1.19x faster                                                 |
| async_tree_eager_tg              | 48.0 ms                                                | 40.4 ms: 1.19x faster                                                 |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 401 ms: 1.15x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 398 ms: 1.13x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 350 ms: 1.06x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 346 ms                                                 | 329 ms: 1.05x faster                                                  |
| async_generators                 | 292 ms                                                 | 279 ms: 1.05x faster                                                  |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.01x faster                                                  |
| Geometric mean                   | (ref)                                                  | 1.27x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 56.3 ms                                                | 43.4 ms: 1.30x faster                                                 |
| nbody          | 73.9 ms                                                | 60.2 ms: 1.23x faster                                                 |
| pidigits       | 284 ms                                                 | 280 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.17x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.62 ms                                                | 2.05 ms: 1.27x faster                                                 |
| regex_compile  | 78.6 ms                                                | 61.9 ms: 1.27x faster                                                 |
| regex_dna      | 148 ms                                                 | 138 ms: 1.07x faster                                                  |
| regex_v8       | 17.0 ms                                                | 16.8 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.15x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.56 sec                                               | 1.14 sec: 1.37x faster                                                |
| unpickle_pure_python | 164 us                                                 | 120 us: 1.37x faster                                                  |
| xml_etree_process    | 41.0 ms                                                | 33.9 ms: 1.21x faster                                                 |
| xml_etree_generate   | 57.0 ms                                                | 48.4 ms: 1.18x faster                                                 |
| pickle_pure_python   | 214 us                                                 | 182 us: 1.17x faster                                                  |
| xml_etree_parse      | 107 ms                                                 | 97.7 ms: 1.10x faster                                                 |
| xml_etree_iterparse  | 74.1 ms                                                | 68.8 ms: 1.08x faster                                                 |
| json_loads           | 17.0 us                                                | 16.1 us: 1.06x faster                                                 |
| json_dumps           | 6.51 ms                                                | 7.08 ms: 1.09x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 15.8 ms                                                | 13.6 ms: 1.16x faster                                                 |
| python_startup         | 20.6 ms                                                | 18.6 ms: 1.11x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 12.4 ms: 1.36x faster                                                 |
| genshi_xml      | 34.1 ms                                                | 26.5 ms: 1.29x faster                                                 |
| mako            | 7.70 ms                                                | 6.91 ms: 1.11x faster                                                 |
| django_template | 20.5 ms                                                | 19.1 ms: 1.08x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.20x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| generators                       | 31.5 ms                                                | 17.2 ms: 1.83x faster                                                 |
| deepcopy                         | 234 us                                                 | 140 us: 1.68x faster                                                  |
| deepcopy_memo                    | 27.3 us                                                | 16.5 us: 1.65x faster                                                 |
| go                               | 115 ms                                                 | 70.9 ms: 1.62x faster                                                 |
| async_tree_memoization_tg        | 289 ms                                                 | 181 ms: 1.60x faster                                                  |
| async_tree_eager_io              | 514 ms                                                 | 340 ms: 1.51x faster                                                  |
| async_tree_io_tg                 | 499 ms                                                 | 331 ms: 1.51x faster                                                  |
| async_tree_io                    | 510 ms                                                 | 348 ms: 1.47x faster                                                  |
| scimark_sor                      | 106 ms                                                 | 72.7 ms: 1.45x faster                                                 |
| async_tree_none_tg               | 199 ms                                                 | 138 ms: 1.44x faster                                                  |
| deepcopy_reduce                  | 2.08 us                                                | 1.46 us: 1.43x faster                                                 |
| async_tree_memoization           | 268 ms                                                 | 191 ms: 1.41x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 152 ms: 1.39x faster                                                  |
| async_tree_eager_io_tg           | 481 ms                                                 | 345 ms: 1.39x faster                                                  |
| tomli_loads                      | 1.56 sec                                               | 1.14 sec: 1.37x faster                                                |
| unpickle_pure_python             | 164 us                                                 | 120 us: 1.37x faster                                                  |
| genshi_text                      | 16.9 ms                                                | 12.4 ms: 1.36x faster                                                 |
| coroutines                       | 19.8 ms                                                | 14.7 ms: 1.35x faster                                                 |
| scimark_monte_carlo              | 50.6 ms                                                | 37.6 ms: 1.35x faster                                                 |
| hexiom                           | 4.83 ms                                                | 3.71 ms: 1.30x faster                                                 |
| deltablue                        | 2.67 ms                                                | 2.05 ms: 1.30x faster                                                 |
| float                            | 56.3 ms                                                | 43.4 ms: 1.30x faster                                                 |
| genshi_xml                       | 34.1 ms                                                | 26.5 ms: 1.29x faster                                                 |
| spectral_norm                    | 76.3 ms                                                | 59.4 ms: 1.28x faster                                                 |
| richards                         | 35.2 ms                                                | 27.4 ms: 1.28x faster                                                 |
| regex_effbot                     | 2.62 ms                                                | 2.05 ms: 1.27x faster                                                 |
| richards_super                   | 39.2 ms                                                | 30.8 ms: 1.27x faster                                                 |
| regex_compile                    | 78.6 ms                                                | 61.9 ms: 1.27x faster                                                 |
| html5lib                         | 36.6 ms                                                | 29.0 ms: 1.26x faster                                                 |
| pyflate                          | 355 ms                                                 | 282 ms: 1.26x faster                                                  |
| sqlglot_parse                    | 859 us                                                 | 684 us: 1.26x faster                                                  |
| pprint_pformat                   | 1.10 sec                                               | 875 ms: 1.26x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 135 ms: 1.25x faster                                                  |
| logging_simple                   | 3.59 us                                                | 2.92 us: 1.23x faster                                                 |
| nbody                            | 73.9 ms                                                | 60.2 ms: 1.23x faster                                                 |
| pprint_safe_repr                 | 535 ms                                                 | 437 ms: 1.23x faster                                                  |
| sqlglot_transpile                | 1.03 ms                                                | 840 us: 1.22x faster                                                  |
| nqueens                          | 61.8 ms                                                | 50.7 ms: 1.22x faster                                                 |
| logging_silent                   | 70.1 ns                                                | 57.8 ns: 1.21x faster                                                 |
| xml_etree_process                | 41.0 ms                                                | 33.9 ms: 1.21x faster                                                 |
| logging_format                   | 3.90 us                                                | 3.23 us: 1.21x faster                                                 |
| 2to3                             | 181 ms                                                 | 151 ms: 1.20x faster                                                  |
| scimark_fft                      | 200 ms                                                 | 167 ms: 1.20x faster                                                  |
| chaos                            | 41.3 ms                                                | 34.5 ms: 1.20x faster                                                 |
| pylint                           | 179 ms                                                 | 150 ms: 1.19x faster                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 115 ms: 1.19x faster                                                  |
| raytrace                         | 181 ms                                                 | 152 ms: 1.19x faster                                                  |
| fannkuch                         | 285 ms                                                 | 240 ms: 1.19x faster                                                  |
| scimark_lu                       | 76.7 ms                                                | 64.6 ms: 1.19x faster                                                 |
| async_tree_eager                 | 69.9 ms                                                | 58.8 ms: 1.19x faster                                                 |
| async_tree_eager_tg              | 48.0 ms                                                | 40.4 ms: 1.19x faster                                                 |
| xml_etree_generate               | 57.0 ms                                                | 48.4 ms: 1.18x faster                                                 |
| pickle_pure_python               | 214 us                                                 | 182 us: 1.17x faster                                                  |
| crypto_pyaes                     | 54.4 ms                                                | 46.6 ms: 1.17x faster                                                 |
| pycparser                        | 708 ms                                                 | 609 ms: 1.16x faster                                                  |
| python_startup_no_site           | 15.8 ms                                                | 13.6 ms: 1.16x faster                                                 |
| scimark_sparse_mat_mult          | 3.00 ms                                                | 2.60 ms: 1.15x faster                                                 |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 401 ms: 1.15x faster                                                  |
| sqlglot_optimize                 | 34.8 ms                                                | 30.4 ms: 1.14x faster                                                 |
| typing_runtime_protocols         | 103 us                                                 | 89.7 us: 1.14x faster                                                 |
| bpe_tokeniser                    | 3.25 sec                                               | 2.86 sec: 1.14x faster                                                |
| sqlglot_normalize                | 188 ms                                                 | 167 ms: 1.13x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 398 ms: 1.13x faster                                                  |
| sympy_expand                     | 247 ms                                                 | 220 ms: 1.13x faster                                                  |
| bench_thread_pool                | 508 us                                                 | 454 us: 1.12x faster                                                  |
| comprehensions                   | 12.0 us                                                | 10.7 us: 1.12x faster                                                 |
| thrift                           | 465 us                                                 | 416 us: 1.12x faster                                                  |
| sympy_str                        | 145 ms                                                 | 130 ms: 1.12x faster                                                  |
| sympy_integrate                  | 11.3 ms                                                | 10.2 ms: 1.11x faster                                                 |
| mako                             | 7.70 ms                                                | 6.91 ms: 1.11x faster                                                 |
| sphinx                           | 600 ms                                                 | 539 ms: 1.11x faster                                                  |
| python_startup                   | 20.6 ms                                                | 18.6 ms: 1.11x faster                                                 |
| k_core                           | 1.62 sec                                               | 1.47 sec: 1.10x faster                                                |
| json                             | 3.06 ms                                                | 2.78 ms: 1.10x faster                                                 |
| xml_etree_parse                  | 107 ms                                                 | 97.7 ms: 1.10x faster                                                 |
| shortest_path                    | 349 ms                                                 | 320 ms: 1.09x faster                                                  |
| dulwich_log                      | 28.6 ms                                                | 26.2 ms: 1.09x faster                                                 |
| sqlalchemy_imperative            | 6.68 ms                                                | 6.15 ms: 1.09x faster                                                 |
| telco                            | 4.79 ms                                                | 4.41 ms: 1.09x faster                                                 |
| sympy_sum                        | 75.1 ms                                                | 69.3 ms: 1.08x faster                                                 |
| bench_mp_pool                    | 64.9 ms                                                | 59.9 ms: 1.08x faster                                                 |
| xml_etree_iterparse              | 74.1 ms                                                | 68.8 ms: 1.08x faster                                                 |
| django_template                  | 20.5 ms                                                | 19.1 ms: 1.08x faster                                                 |
| meteor_contest                   | 75.1 ms                                                | 70.0 ms: 1.07x faster                                                 |
| regex_dna                        | 148 ms                                                 | 138 ms: 1.07x faster                                                  |
| sqlalchemy_declarative           | 59.1 ms                                                | 55.3 ms: 1.07x faster                                                 |
| connected_components             | 320 ms                                                 | 300 ms: 1.07x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 350 ms: 1.06x faster                                                  |
| json_loads                       | 17.0 us                                                | 16.1 us: 1.06x faster                                                 |
| docutils                         | 1.44 sec                                               | 1.37 sec: 1.06x faster                                                |
| async_tree_eager_cpu_io_mixed_tg | 346 ms                                                 | 329 ms: 1.05x faster                                                  |
| mdp                              | 1.50 sec                                               | 1.43 sec: 1.05x faster                                                |
| async_generators                 | 292 ms                                                 | 279 ms: 1.05x faster                                                  |
| pathlib                          | 23.3 ms                                                | 22.5 ms: 1.04x faster                                                 |
| pidigits                         | 284 ms                                                 | 280 ms: 1.01x faster                                                  |
| regex_v8                         | 17.0 ms                                                | 16.8 ms: 1.01x faster                                                 |
| coverage                         | 45.5 ms                                                | 45.0 ms: 1.01x faster                                                 |
| sqlite_synth                     | 1.56 us                                                | 1.54 us: 1.01x faster                                                 |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.01x faster                                                  |
| gc_traversal                     | 2.93 ms                                                | 3.06 ms: 1.04x slower                                                 |
| create_gc_cycles                 | 1.20 ms                                                | 1.27 ms: 1.06x slower                                                 |
| json_dumps                       | 6.51 ms                                                | 7.08 ms: 1.09x slower                                                 |
| subparsers                       | 9.50 ms                                                | 11.4 ms: 1.20x slower                                                 |
| many_optionals                   | 324 us                                                 | 423 us: 1.30x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.19x faster                                                          |
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.187x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: 1.03x