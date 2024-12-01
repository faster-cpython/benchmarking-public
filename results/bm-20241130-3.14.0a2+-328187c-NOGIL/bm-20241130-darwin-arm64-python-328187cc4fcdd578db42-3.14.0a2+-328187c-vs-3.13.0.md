# Results vs. 3.13.0

- fork: python
- ref: 328187cc4fcdd578db42
- machine: darwin-arm64
- commit hash: 328187c
- commit date: 2024-11-30
- overall geometric mean: 1.151x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 221 ms: 1.18x slower                                                   |
| docutils       | 1.44 sec                                               | 1.57 sec: 1.09x slower                                                 |
| html5lib       | 36.6 ms                                                | 45.9 ms: 1.26x slower                                                  |
| sphinx         | 603 ms                                                 | 660 ms: 1.10x slower                                                   |
| Geometric mean | (ref)                                                  | 1.15x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager_io              | 514 ms                                                 | 439 ms: 1.17x faster                                                   |
| async_tree_memoization_tg        | 288 ms                                                 | 246 ms: 1.17x faster                                                   |
| async_tree_eager_io_tg           | 477 ms                                                 | 422 ms: 1.13x faster                                                   |
| async_tree_io_tg                 | 497 ms                                                 | 459 ms: 1.08x faster                                                   |
| async_tree_io                    | 507 ms                                                 | 481 ms: 1.05x faster                                                   |
| coroutines                       | 19.8 ms                                                | 19.3 ms: 1.02x faster                                                  |
| asyncio_websockets               | 242 ms                                                 | 238 ms: 1.02x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 195 ms: 1.02x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 450 ms: 1.00x slower                                                   |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 472 ms: 1.03x slower                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 174 ms: 1.03x slower                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 389 ms: 1.04x slower                                                   |
| async_generators                 | 295 ms                                                 | 309 ms: 1.05x slower                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 367 ms: 1.06x slower                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 155 ms: 1.13x slower                                                   |
| async_tree_eager                 | 70.1 ms                                                | 96.6 ms: 1.38x slower                                                  |
| async_tree_eager_tg              | 47.8 ms                                                | 71.9 ms: 1.50x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.02x slower                                                           |

Benchmark hidden because not significant (2): async_tree_memoization, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 284 ms                                                 | 280 ms: 1.01x faster                                                   |
| nbody          | 74.0 ms                                                | 94.7 ms: 1.28x slower                                                  |
| float          | 56.0 ms                                                | 86.5 ms: 1.54x slower                                                  |
| Geometric mean | (ref)                                                  | 1.25x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.07 ms: 1.27x faster                                                  |
| regex_dna      | 149 ms                                                 | 136 ms: 1.10x faster                                                   |
| regex_v8       | 17.0 ms                                                | 16.0 ms: 1.06x faster                                                  |
| regex_compile  | 78.6 ms                                                | 97.1 ms: 1.24x slower                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 107 ms                                                 | 99.7 ms: 1.07x faster                                                  |
| xml_etree_iterparse  | 73.6 ms                                                | 69.0 ms: 1.07x faster                                                  |
| json_loads           | 17.0 us                                                | 17.6 us: 1.04x slower                                                  |
| xml_etree_generate   | 57.0 ms                                                | 60.3 ms: 1.06x slower                                                  |
| tomli_loads          | 1.57 sec                                               | 1.75 sec: 1.12x slower                                                 |
| xml_etree_process    | 41.0 ms                                                | 48.1 ms: 1.17x slower                                                  |
| json_dumps           | 6.52 ms                                                | 8.39 ms: 1.29x slower                                                  |
| unpickle_pure_python | 164 us                                                 | 230 us: 1.40x slower                                                   |
| pickle_pure_python   | 214 us                                                 | 312 us: 1.46x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.14x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 18.9 ms                                                | 22.8 ms: 1.21x slower                                                  |
| python_startup_no_site | 14.5 ms                                                | 17.8 ms: 1.23x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.22x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 34.4 ms                                                | 37.7 ms: 1.10x slower                                                  |
| genshi_text     | 16.9 ms                                                | 19.6 ms: 1.16x slower                                                  |
| django_template | 22.2 ms                                                | 30.6 ms: 1.38x slower                                                  |
| mako            | 7.68 ms                                                | 12.6 ms: 1.64x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.30x slower                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot                     | 2.63 ms                                                | 2.07 ms: 1.27x faster                                                  |
| deepcopy                         | 237 us                                                 | 196 us: 1.20x faster                                                   |
| async_tree_eager_io              | 514 ms                                                 | 439 ms: 1.17x faster                                                   |
| async_tree_memoization_tg        | 288 ms                                                 | 246 ms: 1.17x faster                                                   |
| async_tree_eager_io_tg           | 477 ms                                                 | 422 ms: 1.13x faster                                                   |
| gc_traversal                     | 2.91 ms                                                | 2.64 ms: 1.10x faster                                                  |
| regex_dna                        | 149 ms                                                 | 136 ms: 1.10x faster                                                   |
| async_tree_io_tg                 | 497 ms                                                 | 459 ms: 1.08x faster                                                   |
| xml_etree_parse                  | 107 ms                                                 | 99.7 ms: 1.07x faster                                                  |
| xml_etree_iterparse              | 73.6 ms                                                | 69.0 ms: 1.07x faster                                                  |
| regex_v8                         | 17.0 ms                                                | 16.0 ms: 1.06x faster                                                  |
| async_tree_io                    | 507 ms                                                 | 481 ms: 1.05x faster                                                   |
| generators                       | 31.5 ms                                                | 30.0 ms: 1.05x faster                                                  |
| deepcopy_memo                    | 27.4 us                                                | 26.2 us: 1.05x faster                                                  |
| deepcopy_reduce                  | 2.07 us                                                | 2.01 us: 1.03x faster                                                  |
| coroutines                       | 19.8 ms                                                | 19.3 ms: 1.02x faster                                                  |
| asyncio_websockets               | 242 ms                                                 | 238 ms: 1.02x faster                                                   |
| create_gc_cycles                 | 1.17 ms                                                | 1.15 ms: 1.02x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 195 ms: 1.02x faster                                                   |
| pidigits                         | 284 ms                                                 | 280 ms: 1.01x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 450 ms: 1.00x slower                                                   |
| pathlib                          | 23.4 ms                                                | 23.6 ms: 1.01x slower                                                  |
| nqueens                          | 62.5 ms                                                | 63.8 ms: 1.02x slower                                                  |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 472 ms: 1.03x slower                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 174 ms: 1.03x slower                                                   |
| json_loads                       | 17.0 us                                                | 17.6 us: 1.04x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 389 ms: 1.04x slower                                                   |
| async_generators                 | 295 ms                                                 | 309 ms: 1.05x slower                                                   |
| spectral_norm                    | 76.3 ms                                                | 80.1 ms: 1.05x slower                                                  |
| telco                            | 4.76 ms                                                | 5.03 ms: 1.06x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 367 ms: 1.06x slower                                                   |
| xml_etree_generate               | 57.0 ms                                                | 60.3 ms: 1.06x slower                                                  |
| shortest_path                    | 347 ms                                                 | 375 ms: 1.08x slower                                                   |
| bpe_tokeniser                    | 3.25 sec                                               | 3.53 sec: 1.09x slower                                                 |
| docutils                         | 1.44 sec                                               | 1.57 sec: 1.09x slower                                                 |
| pylint                           | 180 ms                                                 | 197 ms: 1.10x slower                                                   |
| sphinx                           | 603 ms                                                 | 660 ms: 1.10x slower                                                   |
| genshi_xml                       | 34.4 ms                                                | 37.7 ms: 1.10x slower                                                  |
| k_core                           | 1.61 sec                                               | 1.77 sec: 1.10x slower                                                 |
| connected_components             | 319 ms                                                 | 351 ms: 1.10x slower                                                   |
| fannkuch                         | 284 ms                                                 | 315 ms: 1.11x slower                                                   |
| tomli_loads                      | 1.57 sec                                               | 1.75 sec: 1.12x slower                                                 |
| mdp                              | 1.49 sec                                               | 1.68 sec: 1.12x slower                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 155 ms: 1.13x slower                                                   |
| meteor_contest                   | 74.0 ms                                                | 83.5 ms: 1.13x slower                                                  |
| scimark_fft                      | 201 ms                                                 | 228 ms: 1.13x slower                                                   |
| genshi_text                      | 16.9 ms                                                | 19.6 ms: 1.16x slower                                                  |
| coverage                         | 46.0 ms                                                | 53.8 ms: 1.17x slower                                                  |
| xml_etree_process                | 41.0 ms                                                | 48.1 ms: 1.17x slower                                                  |
| pycparser                        | 705 ms                                                 | 830 ms: 1.18x slower                                                   |
| 2to3                             | 187 ms                                                 | 221 ms: 1.18x slower                                                   |
| bench_mp_pool                    | 62.5 ms                                                | 74.1 ms: 1.18x slower                                                  |
| sqlglot_normalize                | 189 ms                                                 | 224 ms: 1.19x slower                                                   |
| sqlglot_optimize                 | 34.9 ms                                                | 41.9 ms: 1.20x slower                                                  |
| python_startup                   | 18.9 ms                                                | 22.8 ms: 1.21x slower                                                  |
| typing_runtime_protocols         | 101 us                                                 | 123 us: 1.22x slower                                                   |
| python_startup_no_site           | 14.5 ms                                                | 17.8 ms: 1.23x slower                                                  |
| regex_compile                    | 78.6 ms                                                | 97.1 ms: 1.24x slower                                                  |
| pyflate                          | 351 ms                                                 | 435 ms: 1.24x slower                                                   |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 3.74 ms: 1.25x slower                                                  |
| crypto_pyaes                     | 54.2 ms                                                | 68.0 ms: 1.25x slower                                                  |
| html5lib                         | 36.6 ms                                                | 45.9 ms: 1.26x slower                                                  |
| scimark_sor                      | 105 ms                                                 | 133 ms: 1.26x slower                                                   |
| nbody                            | 74.0 ms                                                | 94.7 ms: 1.28x slower                                                  |
| dulwich_log                      | 28.5 ms                                                | 36.7 ms: 1.29x slower                                                  |
| json_dumps                       | 6.52 ms                                                | 8.39 ms: 1.29x slower                                                  |
| sympy_integrate                  | 11.3 ms                                                | 14.6 ms: 1.30x slower                                                  |
| pprint_safe_repr                 | 533 ms                                                 | 698 ms: 1.31x slower                                                   |
| pprint_pformat                   | 1.08 sec                                               | 1.42 sec: 1.31x slower                                                 |
| thrift                           | 466 us                                                 | 615 us: 1.32x slower                                                   |
| sqlalchemy_imperative            | 6.69 ms                                                | 9.20 ms: 1.38x slower                                                  |
| django_template                  | 22.2 ms                                                | 30.6 ms: 1.38x slower                                                  |
| async_tree_eager                 | 70.1 ms                                                | 96.6 ms: 1.38x slower                                                  |
| hexiom                           | 4.86 ms                                                | 6.72 ms: 1.38x slower                                                  |
| sympy_str                        | 145 ms                                                 | 202 ms: 1.39x slower                                                   |
| go                               | 115 ms                                                 | 161 ms: 1.40x slower                                                   |
| unpickle_pure_python             | 164 us                                                 | 230 us: 1.40x slower                                                   |
| scimark_monte_carlo              | 50.4 ms                                                | 70.8 ms: 1.40x slower                                                  |
| sqlalchemy_declarative           | 58.9 ms                                                | 84.2 ms: 1.43x slower                                                  |
| richards                         | 35.2 ms                                                | 50.8 ms: 1.44x slower                                                  |
| logging_simple                   | 3.60 us                                                | 5.22 us: 1.45x slower                                                  |
| comprehensions                   | 12.3 us                                                | 17.9 us: 1.46x slower                                                  |
| logging_format                   | 3.89 us                                                | 5.67 us: 1.46x slower                                                  |
| pickle_pure_python               | 214 us                                                 | 312 us: 1.46x slower                                                   |
| async_tree_eager_tg              | 47.8 ms                                                | 71.9 ms: 1.50x slower                                                  |
| richards_super                   | 39.1 ms                                                | 59.5 ms: 1.52x slower                                                  |
| sympy_expand                     | 246 ms                                                 | 379 ms: 1.54x slower                                                   |
| float                            | 56.0 ms                                                | 86.5 ms: 1.54x slower                                                  |
| chaos                            | 41.2 ms                                                | 64.1 ms: 1.56x slower                                                  |
| bench_thread_pool                | 505 us                                                 | 793 us: 1.57x slower                                                   |
| scimark_lu                       | 76.7 ms                                                | 122 ms: 1.60x slower                                                   |
| mako                             | 7.68 ms                                                | 12.6 ms: 1.64x slower                                                  |
| sympy_sum                        | 75.4 ms                                                | 125 ms: 1.65x slower                                                   |
| sqlglot_transpile                | 1.02 ms                                                | 1.70 ms: 1.66x slower                                                  |
| logging_silent                   | 70.1 ns                                                | 122 ns: 1.74x slower                                                   |
| raytrace                         | 181 ms                                                 | 316 ms: 1.75x slower                                                   |
| sqlglot_parse                    | 856 us                                                 | 1.50 ms: 1.76x slower                                                  |
| deltablue                        | 2.68 ms                                                | 5.07 ms: 1.89x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.18x slower                                                           |

Benchmark hidden because not significant (3): async_tree_memoization, async_tree_none, json
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, gevent_hub, mypy2, tornado_http
Ignored benchmarks (3) of results/bm-20241130-3.14.0a2+-328187c-NOGIL/bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json: many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.151x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.09x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: 1.15x