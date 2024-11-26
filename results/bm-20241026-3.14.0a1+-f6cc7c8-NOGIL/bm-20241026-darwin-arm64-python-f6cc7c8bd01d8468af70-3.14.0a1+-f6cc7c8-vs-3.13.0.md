# Results vs. 3.13.0

- fork: python
- ref: f6cc7c8bd01d8468af70
- machine: darwin-arm64
- commit hash: f6cc7c8
- commit date: 2024-10-26
- overall geometric mean: 1.223x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x slower
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 242 ms: 1.29x slower                                                   |
| docutils       | 1.44 sec                                               | 1.68 sec: 1.17x slower                                                 |
| html5lib       | 36.6 ms                                                | 50.3 ms: 1.38x slower                                                  |
| sphinx         | 603 ms                                                 | 715 ms: 1.19x slower                                                   |
| tornado_http   | 75.8 ms                                                | 108 ms: 1.43x slower                                                   |
| Geometric mean | (ref)                                                  | 1.29x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 260 ms: 1.11x faster                                                   |
| async_tree_eager_io              | 514 ms                                                 | 474 ms: 1.08x faster                                                   |
| async_tree_eager_io_tg           | 477 ms                                                 | 452 ms: 1.05x faster                                                   |
| asyncio_websockets               | 242 ms                                                 | 238 ms: 1.01x faster                                                   |
| async_tree_io                    | 507 ms                                                 | 515 ms: 1.02x slower                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 459 ms: 1.02x slower                                                   |
| async_tree_none_tg               | 198 ms                                                 | 203 ms: 1.03x slower                                                   |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 483 ms: 1.05x slower                                                   |
| async_tree_none                  | 215 ms                                                 | 227 ms: 1.05x slower                                                   |
| async_tree_memoization           | 268 ms                                                 | 283 ms: 1.06x slower                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 394 ms: 1.06x slower                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 367 ms: 1.06x slower                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 182 ms: 1.08x slower                                                   |
| async_generators                 | 295 ms                                                 | 327 ms: 1.11x slower                                                   |
| coroutines                       | 19.8 ms                                                | 22.8 ms: 1.15x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 159 ms: 1.16x slower                                                   |
| async_tree_eager                 | 70.1 ms                                                | 102 ms: 1.46x slower                                                   |
| async_tree_eager_tg              | 47.8 ms                                                | 72.8 ms: 1.52x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.07x slower                                                           |

Benchmark hidden because not significant (1): async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 284 ms                                                 | 282 ms: 1.01x faster                                                   |
| float          | 56.0 ms                                                | 93.1 ms: 1.66x slower                                                  |
| nbody          | 74.0 ms                                                | 149 ms: 2.02x slower                                                   |
| Geometric mean | (ref)                                                  | 1.49x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.35 ms: 1.12x faster                                                  |
| regex_dna      | 149 ms                                                 | 135 ms: 1.10x faster                                                   |
| regex_v8       | 17.0 ms                                                | 16.3 ms: 1.04x faster                                                  |
| regex_compile  | 78.6 ms                                                | 118 ms: 1.50x slower                                                   |
| Geometric mean | (ref)                                                  | 1.04x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 107 ms                                                 | 98.2 ms: 1.09x faster                                                  |
| xml_etree_iterparse  | 73.6 ms                                                | 74.9 ms: 1.02x slower                                                  |
| json_loads           | 17.0 us                                                | 18.2 us: 1.08x slower                                                  |
| xml_etree_generate   | 57.0 ms                                                | 65.6 ms: 1.15x slower                                                  |
| tomli_loads          | 1.57 sec                                               | 1.97 sec: 1.26x slower                                                 |
| xml_etree_process    | 41.0 ms                                                | 53.2 ms: 1.30x slower                                                  |
| json_dumps           | 6.52 ms                                                | 8.69 ms: 1.33x slower                                                  |
| pickle_pure_python   | 214 us                                                 | 338 us: 1.58x slower                                                   |
| unpickle_pure_python | 164 us                                                 | 261 us: 1.59x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.23x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 18.9 ms                                                | 20.6 ms: 1.09x slower                                                  |
| python_startup_no_site | 14.5 ms                                                | 16.1 ms: 1.11x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 23.5 ms: 1.39x slower                                                  |
| genshi_xml      | 34.4 ms                                                | 48.0 ms: 1.40x slower                                                  |
| django_template | 22.2 ms                                                | 34.1 ms: 1.54x slower                                                  |
| mako            | 7.68 ms                                                | 13.4 ms: 1.75x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.51x slower                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| gc_traversal                     | 2.91 ms                                                | 2.51 ms: 1.16x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.35 ms: 1.12x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 260 ms: 1.11x faster                                                   |
| regex_dna                        | 149 ms                                                 | 135 ms: 1.10x faster                                                   |
| xml_etree_parse                  | 107 ms                                                 | 98.2 ms: 1.09x faster                                                  |
| async_tree_eager_io              | 514 ms                                                 | 474 ms: 1.08x faster                                                   |
| create_gc_cycles                 | 1.17 ms                                                | 1.09 ms: 1.07x faster                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 452 ms: 1.05x faster                                                   |
| regex_v8                         | 17.0 ms                                                | 16.3 ms: 1.04x faster                                                  |
| generators                       | 31.5 ms                                                | 31.0 ms: 1.02x faster                                                  |
| asyncio_websockets               | 242 ms                                                 | 238 ms: 1.01x faster                                                   |
| deepcopy                         | 237 us                                                 | 234 us: 1.01x faster                                                   |
| pidigits                         | 284 ms                                                 | 282 ms: 1.01x faster                                                   |
| async_tree_io                    | 507 ms                                                 | 515 ms: 1.02x slower                                                   |
| xml_etree_iterparse              | 73.6 ms                                                | 74.9 ms: 1.02x slower                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 459 ms: 1.02x slower                                                   |
| async_tree_none_tg               | 198 ms                                                 | 203 ms: 1.03x slower                                                   |
| pathlib                          | 23.4 ms                                                | 24.5 ms: 1.05x slower                                                  |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 483 ms: 1.05x slower                                                   |
| async_tree_none                  | 215 ms                                                 | 227 ms: 1.05x slower                                                   |
| async_tree_memoization           | 268 ms                                                 | 283 ms: 1.06x slower                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 394 ms: 1.06x slower                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 367 ms: 1.06x slower                                                   |
| json                             | 3.03 ms                                                | 3.22 ms: 1.06x slower                                                  |
| json_loads                       | 17.0 us                                                | 18.2 us: 1.08x slower                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 182 ms: 1.08x slower                                                   |
| python_startup                   | 18.9 ms                                                | 20.6 ms: 1.09x slower                                                  |
| deepcopy_memo                    | 27.4 us                                                | 29.9 us: 1.09x slower                                                  |
| bench_mp_pool                    | 62.5 ms                                                | 68.9 ms: 1.10x slower                                                  |
| async_generators                 | 295 ms                                                 | 327 ms: 1.11x slower                                                   |
| python_startup_no_site           | 14.5 ms                                                | 16.1 ms: 1.11x slower                                                  |
| deepcopy_reduce                  | 2.07 us                                                | 2.34 us: 1.13x slower                                                  |
| telco                            | 4.76 ms                                                | 5.43 ms: 1.14x slower                                                  |
| coverage                         | 46.0 ms                                                | 52.9 ms: 1.15x slower                                                  |
| xml_etree_generate               | 57.0 ms                                                | 65.6 ms: 1.15x slower                                                  |
| coroutines                       | 19.8 ms                                                | 22.8 ms: 1.15x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 159 ms: 1.16x slower                                                   |
| pylint                           | 180 ms                                                 | 209 ms: 1.16x slower                                                   |
| docutils                         | 1.44 sec                                               | 1.68 sec: 1.17x slower                                                 |
| nqueens                          | 62.5 ms                                                | 73.4 ms: 1.17x slower                                                  |
| sphinx                           | 603 ms                                                 | 715 ms: 1.19x slower                                                   |
| meteor_contest                   | 74.0 ms                                                | 88.1 ms: 1.19x slower                                                  |
| bpe_tokeniser                    | 3.25 sec                                               | 3.90 sec: 1.20x slower                                                 |
| mdp                              | 1.49 sec                                               | 1.82 sec: 1.22x slower                                                 |
| fannkuch                         | 284 ms                                                 | 356 ms: 1.26x slower                                                   |
| tomli_loads                      | 1.57 sec                                               | 1.97 sec: 1.26x slower                                                 |
| pycparser                        | 705 ms                                                 | 909 ms: 1.29x slower                                                   |
| 2to3                             | 187 ms                                                 | 242 ms: 1.29x slower                                                   |
| xml_etree_process                | 41.0 ms                                                | 53.2 ms: 1.30x slower                                                  |
| scimark_fft                      | 201 ms                                                 | 262 ms: 1.31x slower                                                   |
| json_dumps                       | 6.52 ms                                                | 8.69 ms: 1.33x slower                                                  |
| pyflate                          | 351 ms                                                 | 477 ms: 1.36x slower                                                   |
| html5lib                         | 36.6 ms                                                | 50.3 ms: 1.38x slower                                                  |
| sqlglot_normalize                | 189 ms                                                 | 261 ms: 1.38x slower                                                   |
| genshi_text                      | 16.9 ms                                                | 23.5 ms: 1.39x slower                                                  |
| thrift                           | 466 us                                                 | 650 us: 1.40x slower                                                   |
| genshi_xml                       | 34.4 ms                                                | 48.0 ms: 1.40x slower                                                  |
| sympy_integrate                  | 11.3 ms                                                | 15.9 ms: 1.41x slower                                                  |
| dulwich_log                      | 28.5 ms                                                | 40.2 ms: 1.41x slower                                                  |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 4.22 ms: 1.41x slower                                                  |
| typing_runtime_protocols         | 101 us                                                 | 143 us: 1.41x slower                                                   |
| sqlglot_optimize                 | 34.9 ms                                                | 49.9 ms: 1.43x slower                                                  |
| tornado_http                     | 75.8 ms                                                | 108 ms: 1.43x slower                                                   |
| crypto_pyaes                     | 54.2 ms                                                | 78.4 ms: 1.45x slower                                                  |
| async_tree_eager                 | 70.1 ms                                                | 102 ms: 1.46x slower                                                   |
| sqlalchemy_imperative            | 6.69 ms                                                | 9.86 ms: 1.47x slower                                                  |
| scimark_sor                      | 105 ms                                                 | 156 ms: 1.48x slower                                                   |
| pprint_safe_repr                 | 533 ms                                                 | 796 ms: 1.49x slower                                                   |
| pprint_pformat                   | 1.08 sec                                               | 1.62 sec: 1.49x slower                                                 |
| regex_compile                    | 78.6 ms                                                | 118 ms: 1.50x slower                                                   |
| sqlalchemy_declarative           | 58.9 ms                                                | 89.3 ms: 1.52x slower                                                  |
| async_tree_eager_tg              | 47.8 ms                                                | 72.8 ms: 1.52x slower                                                  |
| richards                         | 35.2 ms                                                | 53.7 ms: 1.53x slower                                                  |
| django_template                  | 22.2 ms                                                | 34.1 ms: 1.54x slower                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 77.7 ms: 1.54x slower                                                  |
| go                               | 115 ms                                                 | 178 ms: 1.54x slower                                                   |
| sympy_str                        | 145 ms                                                 | 226 ms: 1.56x slower                                                   |
| comprehensions                   | 12.3 us                                                | 19.1 us: 1.56x slower                                                  |
| bench_thread_pool                | 505 us                                                 | 794 us: 1.57x slower                                                   |
| hexiom                           | 4.86 ms                                                | 7.66 ms: 1.57x slower                                                  |
| pickle_pure_python               | 214 us                                                 | 338 us: 1.58x slower                                                   |
| logging_simple                   | 3.60 us                                                | 5.70 us: 1.58x slower                                                  |
| richards_super                   | 39.1 ms                                                | 61.9 ms: 1.58x slower                                                  |
| unpickle_pure_python             | 164 us                                                 | 261 us: 1.59x slower                                                   |
| logging_format                   | 3.89 us                                                | 6.22 us: 1.60x slower                                                  |
| float                            | 56.0 ms                                                | 93.1 ms: 1.66x slower                                                  |
| spectral_norm                    | 76.3 ms                                                | 127 ms: 1.67x slower                                                   |
| sympy_expand                     | 246 ms                                                 | 415 ms: 1.68x slower                                                   |
| mako                             | 7.68 ms                                                | 13.4 ms: 1.75x slower                                                  |
| sqlglot_transpile                | 1.02 ms                                                | 1.84 ms: 1.80x slower                                                  |
| sympy_sum                        | 75.4 ms                                                | 136 ms: 1.80x slower                                                   |
| chaos                            | 41.2 ms                                                | 75.1 ms: 1.82x slower                                                  |
| scimark_lu                       | 76.7 ms                                                | 142 ms: 1.85x slower                                                   |
| logging_silent                   | 70.1 ns                                                | 131 ns: 1.87x slower                                                   |
| sqlglot_parse                    | 856 us                                                 | 1.63 ms: 1.90x slower                                                  |
| raytrace                         | 181 ms                                                 | 357 ms: 1.98x slower                                                   |
| nbody                            | 74.0 ms                                                | 149 ms: 2.02x slower                                                   |
| deltablue                        | 2.68 ms                                                | 5.41 ms: 2.02x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.29x slower                                                           |

Benchmark hidden because not significant (1): async_tree_io_tg
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dask, gevent_hub, k_core, mypy2, shortest_path

- Geometric mean (including insignificant results): 1.223x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.19x
- 95% likely to have a slowdown of 1.18x
- 99% likely to have a slowdown of 1.16x

# Memory
- memory change: 1.12x