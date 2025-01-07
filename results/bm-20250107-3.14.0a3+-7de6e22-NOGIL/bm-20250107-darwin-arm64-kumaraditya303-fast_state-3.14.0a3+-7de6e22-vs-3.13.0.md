# Results vs. 3.13.0

- fork: kumaraditya303
- ref: fast_state
- machine: darwin-arm64
- commit hash: 7de6e22
- commit date: 2025-01-07
- overall geometric mean: 1.066x slower
- HPT reliability: 99.83%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 181 ms                                                 | 206 ms: 1.14x slower                                                 |
| docutils       | 1.44 sec                                               | 1.50 sec: 1.04x slower                                               |
| html5lib       | 36.6 ms                                                | 41.7 ms: 1.14x slower                                                |
| sphinx         | 600 ms                                                 | 628 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.09x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg        | 289 ms                                                 | 216 ms: 1.34x faster                                                 |
| async_tree_eager_io              | 514 ms                                                 | 384 ms: 1.34x faster                                                 |
| async_tree_eager_io_tg           | 481 ms                                                 | 369 ms: 1.30x faster                                                 |
| async_tree_io_tg                 | 499 ms                                                 | 391 ms: 1.28x faster                                                 |
| async_tree_io                    | 510 ms                                                 | 415 ms: 1.23x faster                                                 |
| coroutines                       | 19.8 ms                                                | 16.6 ms: 1.19x faster                                                |
| async_tree_none_tg               | 199 ms                                                 | 170 ms: 1.17x faster                                                 |
| async_tree_memoization           | 268 ms                                                 | 235 ms: 1.14x faster                                                 |
| async_tree_none                  | 212 ms                                                 | 191 ms: 1.11x faster                                                 |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 419 ms: 1.07x faster                                                 |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 441 ms: 1.04x faster                                                 |
| asyncio_websockets               | 243 ms                                                 | 238 ms: 1.02x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 165 ms: 1.02x faster                                                 |
| async_generators                 | 292 ms                                                 | 295 ms: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 381 ms: 1.02x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 346 ms                                                 | 360 ms: 1.04x slower                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 147 ms: 1.07x slower                                                 |
| async_tree_eager                 | 69.9 ms                                                | 92.0 ms: 1.32x slower                                                |
| async_tree_eager_tg              | 48.0 ms                                                | 67.7 ms: 1.41x slower                                                |
| Geometric mean                   | (ref)                                                  | 1.07x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 284 ms                                                 | 280 ms: 1.01x faster                                                 |
| float          | 56.3 ms                                                | 65.8 ms: 1.17x slower                                                |
| nbody          | 73.9 ms                                                | 86.5 ms: 1.17x slower                                                |
| Geometric mean | (ref)                                                  | 1.11x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 2.62 ms                                                | 2.10 ms: 1.24x faster                                                |
| regex_dna      | 148 ms                                                 | 136 ms: 1.09x faster                                                 |
| regex_v8       | 17.0 ms                                                | 15.8 ms: 1.07x faster                                                |
| regex_compile  | 78.6 ms                                                | 83.2 ms: 1.06x slower                                                |
| Geometric mean | (ref)                                                  | 1.08x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_iterparse  | 74.1 ms                                                | 66.1 ms: 1.12x faster                                                |
| tomli_loads          | 1.56 sec                                               | 1.47 sec: 1.07x faster                                               |
| xml_etree_parse      | 107 ms                                                 | 102 ms: 1.05x faster                                                 |
| json_loads           | 17.0 us                                                | 17.2 us: 1.01x slower                                                |
| xml_etree_generate   | 57.0 ms                                                | 58.3 ms: 1.02x slower                                                |
| xml_etree_process    | 41.0 ms                                                | 44.0 ms: 1.07x slower                                                |
| unpickle_pure_python | 164 us                                                 | 201 us: 1.22x slower                                                 |
| json_dumps           | 6.51 ms                                                | 8.16 ms: 1.25x slower                                                |
| pickle_pure_python   | 214 us                                                 | 289 us: 1.35x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.07x slower                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 15.8 ms                                                | 15.2 ms: 1.03x faster                                                |
| python_startup         | 20.6 ms                                                | 20.2 ms: 1.02x faster                                                |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_xml      | 34.1 ms                                                | 34.0 ms: 1.00x faster                                                |
| django_template | 20.5 ms                                                | 27.1 ms: 1.32x slower                                                |
| mako            | 7.70 ms                                                | 11.1 ms: 1.45x slower                                                |
| Geometric mean  | (ref)                                                  | 1.17x slower                                                         |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| deepcopy                         | 234 us                                                 | 174 us: 1.34x faster                                                 |
| async_tree_memoization_tg        | 289 ms                                                 | 216 ms: 1.34x faster                                                 |
| async_tree_eager_io              | 514 ms                                                 | 384 ms: 1.34x faster                                                 |
| async_tree_eager_io_tg           | 481 ms                                                 | 369 ms: 1.30x faster                                                 |
| async_tree_io_tg                 | 499 ms                                                 | 391 ms: 1.28x faster                                                 |
| regex_effbot                     | 2.62 ms                                                | 2.10 ms: 1.24x faster                                                |
| async_tree_io                    | 510 ms                                                 | 415 ms: 1.23x faster                                                 |
| deepcopy_memo                    | 27.3 us                                                | 22.8 us: 1.20x faster                                                |
| coroutines                       | 19.8 ms                                                | 16.6 ms: 1.19x faster                                                |
| async_tree_none_tg               | 199 ms                                                 | 170 ms: 1.17x faster                                                 |
| sqlite_synth                     | 1.56 us                                                | 1.35 us: 1.15x faster                                                |
| deepcopy_reduce                  | 2.08 us                                                | 1.82 us: 1.15x faster                                                |
| async_tree_memoization           | 268 ms                                                 | 235 ms: 1.14x faster                                                 |
| generators                       | 31.5 ms                                                | 27.9 ms: 1.13x faster                                                |
| xml_etree_iterparse              | 74.1 ms                                                | 66.1 ms: 1.12x faster                                                |
| async_tree_none                  | 212 ms                                                 | 191 ms: 1.11x faster                                                 |
| gc_traversal                     | 2.93 ms                                                | 2.64 ms: 1.11x faster                                                |
| regex_dna                        | 148 ms                                                 | 136 ms: 1.09x faster                                                 |
| regex_v8                         | 17.0 ms                                                | 15.8 ms: 1.07x faster                                                |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 419 ms: 1.07x faster                                                 |
| tomli_loads                      | 1.56 sec                                               | 1.47 sec: 1.07x faster                                               |
| xml_etree_parse                  | 107 ms                                                 | 102 ms: 1.05x faster                                                 |
| nqueens                          | 61.8 ms                                                | 58.9 ms: 1.05x faster                                                |
| json                             | 3.06 ms                                                | 2.93 ms: 1.04x faster                                                |
| create_gc_cycles                 | 1.20 ms                                                | 1.15 ms: 1.04x faster                                                |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 441 ms: 1.04x faster                                                 |
| python_startup_no_site           | 15.8 ms                                                | 15.2 ms: 1.03x faster                                                |
| bpe_tokeniser                    | 3.25 sec                                               | 3.16 sec: 1.03x faster                                               |
| asyncio_websockets               | 243 ms                                                 | 238 ms: 1.02x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 165 ms: 1.02x faster                                                 |
| pathlib                          | 23.3 ms                                                | 22.8 ms: 1.02x faster                                                |
| python_startup                   | 20.6 ms                                                | 20.2 ms: 1.02x faster                                                |
| spectral_norm                    | 76.3 ms                                                | 75.1 ms: 1.02x faster                                                |
| pidigits                         | 284 ms                                                 | 280 ms: 1.01x faster                                                 |
| genshi_xml                       | 34.1 ms                                                | 34.0 ms: 1.00x faster                                                |
| async_generators                 | 292 ms                                                 | 295 ms: 1.01x slower                                                 |
| json_loads                       | 17.0 us                                                | 17.2 us: 1.01x slower                                                |
| fannkuch                         | 285 ms                                                 | 290 ms: 1.02x slower                                                 |
| pycparser                        | 708 ms                                                 | 721 ms: 1.02x slower                                                 |
| shortest_path                    | 349 ms                                                 | 355 ms: 1.02x slower                                                 |
| xml_etree_generate               | 57.0 ms                                                | 58.3 ms: 1.02x slower                                                |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 381 ms: 1.02x slower                                                 |
| connected_components             | 320 ms                                                 | 330 ms: 1.03x slower                                                 |
| k_core                           | 1.62 sec                                               | 1.68 sec: 1.04x slower                                               |
| async_tree_eager_cpu_io_mixed_tg | 346 ms                                                 | 360 ms: 1.04x slower                                                 |
| docutils                         | 1.44 sec                                               | 1.50 sec: 1.04x slower                                               |
| sphinx                           | 600 ms                                                 | 628 ms: 1.05x slower                                                 |
| telco                            | 4.79 ms                                                | 5.04 ms: 1.05x slower                                                |
| bench_mp_pool                    | 64.9 ms                                                | 68.4 ms: 1.05x slower                                                |
| regex_compile                    | 78.6 ms                                                | 83.2 ms: 1.06x slower                                                |
| meteor_contest                   | 75.1 ms                                                | 79.9 ms: 1.06x slower                                                |
| scimark_fft                      | 200 ms                                                 | 213 ms: 1.06x slower                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 147 ms: 1.07x slower                                                 |
| sqlglot_optimize                 | 34.8 ms                                                | 37.1 ms: 1.07x slower                                                |
| mdp                              | 1.50 sec                                               | 1.60 sec: 1.07x slower                                               |
| xml_etree_process                | 41.0 ms                                                | 44.0 ms: 1.07x slower                                                |
| sqlglot_normalize                | 188 ms                                                 | 203 ms: 1.08x slower                                                 |
| pyflate                          | 355 ms                                                 | 386 ms: 1.09x slower                                                 |
| sympy_sum                        | 75.1 ms                                                | 83.7 ms: 1.11x slower                                                |
| scimark_sor                      | 106 ms                                                 | 118 ms: 1.12x slower                                                 |
| sympy_expand                     | 247 ms                                                 | 276 ms: 1.12x slower                                                 |
| sympy_str                        | 145 ms                                                 | 162 ms: 1.12x slower                                                 |
| sympy_integrate                  | 11.3 ms                                                | 12.7 ms: 1.12x slower                                                |
| 2to3                             | 181 ms                                                 | 206 ms: 1.14x slower                                                 |
| thrift                           | 465 us                                                 | 529 us: 1.14x slower                                                 |
| html5lib                         | 36.6 ms                                                | 41.7 ms: 1.14x slower                                                |
| coverage                         | 45.5 ms                                                | 51.9 ms: 1.14x slower                                                |
| pprint_pformat                   | 1.10 sec                                               | 1.26 sec: 1.14x slower                                               |
| typing_runtime_protocols         | 103 us                                                 | 117 us: 1.15x slower                                                 |
| dulwich_log                      | 28.6 ms                                                | 32.9 ms: 1.15x slower                                                |
| crypto_pyaes                     | 54.4 ms                                                | 62.6 ms: 1.15x slower                                                |
| pprint_safe_repr                 | 535 ms                                                 | 618 ms: 1.15x slower                                                 |
| float                            | 56.3 ms                                                | 65.8 ms: 1.17x slower                                                |
| nbody                            | 73.9 ms                                                | 86.5 ms: 1.17x slower                                                |
| scimark_sparse_mat_mult          | 3.00 ms                                                | 3.61 ms: 1.20x slower                                                |
| richards_super                   | 39.2 ms                                                | 47.4 ms: 1.21x slower                                                |
| hexiom                           | 4.83 ms                                                | 5.86 ms: 1.21x slower                                                |
| logging_simple                   | 3.59 us                                                | 4.36 us: 1.21x slower                                                |
| richards                         | 35.2 ms                                                | 42.7 ms: 1.22x slower                                                |
| unpickle_pure_python             | 164 us                                                 | 201 us: 1.22x slower                                                 |
| logging_format                   | 3.90 us                                                | 4.81 us: 1.23x slower                                                |
| sqlalchemy_imperative            | 6.68 ms                                                | 8.29 ms: 1.24x slower                                                |
| go                               | 115 ms                                                 | 143 ms: 1.25x slower                                                 |
| scimark_lu                       | 76.7 ms                                                | 95.8 ms: 1.25x slower                                                |
| json_dumps                       | 6.51 ms                                                | 8.16 ms: 1.25x slower                                                |
| scimark_monte_carlo              | 50.6 ms                                                | 63.9 ms: 1.26x slower                                                |
| sqlalchemy_declarative           | 59.1 ms                                                | 75.1 ms: 1.27x slower                                                |
| async_tree_eager                 | 69.9 ms                                                | 92.0 ms: 1.32x slower                                                |
| django_template                  | 20.5 ms                                                | 27.1 ms: 1.32x slower                                                |
| pickle_pure_python               | 214 us                                                 | 289 us: 1.35x slower                                                 |
| chaos                            | 41.3 ms                                                | 57.0 ms: 1.38x slower                                                |
| async_tree_eager_tg              | 48.0 ms                                                | 67.7 ms: 1.41x slower                                                |
| comprehensions                   | 12.0 us                                                | 17.0 us: 1.42x slower                                                |
| sqlglot_transpile                | 1.03 ms                                                | 1.48 ms: 1.44x slower                                                |
| mako                             | 7.70 ms                                                | 11.1 ms: 1.45x slower                                                |
| sqlglot_parse                    | 859 us                                                 | 1.26 ms: 1.47x slower                                                |
| many_optionals                   | 324 us                                                 | 482 us: 1.49x slower                                                 |
| subparsers                       | 9.50 ms                                                | 14.3 ms: 1.51x slower                                                |
| raytrace                         | 181 ms                                                 | 282 ms: 1.55x slower                                                 |
| bench_thread_pool                | 508 us                                                 | 817 us: 1.61x slower                                                 |
| logging_silent                   | 70.1 ns                                                | 113 ns: 1.61x slower                                                 |
| deltablue                        | 2.67 ms                                                | 4.54 ms: 1.70x slower                                                |
| Geometric mean                   | (ref)                                                  | 1.08x slower                                                         |

Benchmark hidden because not significant (2): genshi_text, pylint
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20250107-3.14.0a3+-7de6e22-NOGIL/bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3+-7de6e22.json: mypy2

- Geometric mean (including insignificant results): 1.066x slower

# HPT report

- Reliability score: 99.83% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.17x