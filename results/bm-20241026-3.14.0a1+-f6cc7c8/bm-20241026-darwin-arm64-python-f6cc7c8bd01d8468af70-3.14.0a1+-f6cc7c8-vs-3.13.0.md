# Results vs. 3.13.0

- fork: python
- ref: f6cc7c8bd01d8468af70
- machine: darwin-arm64
- commit hash: f6cc7c8
- commit date: 2024-10-26
- overall geometric mean: 1.083x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 160 ms: 1.17x faster                                                   |
| docutils       | 1.44 sec                                               | 1.40 sec: 1.03x faster                                                 |
| html5lib       | 36.6 ms                                                | 30.1 ms: 1.22x faster                                                  |
| sphinx         | 603 ms                                                 | 576 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 236 ms: 1.22x faster                                                   |
| coroutines                       | 19.8 ms                                                | 16.5 ms: 1.20x faster                                                  |
| async_tree_eager                 | 70.1 ms                                                | 61.1 ms: 1.15x faster                                                  |
| async_tree_eager_tg              | 47.8 ms                                                | 42.3 ms: 1.13x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 150 ms: 1.12x faster                                                   |
| async_tree_none                  | 215 ms                                                 | 199 ms: 1.08x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 249 ms: 1.08x faster                                                   |
| async_generators                 | 295 ms                                                 | 277 ms: 1.07x faster                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 130 ms: 1.06x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 359 ms: 1.04x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 335 ms: 1.04x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 469 ms: 1.05x slower                                                   |
| async_tree_none_tg               | 198 ms                                                 | 217 ms: 1.09x slower                                                   |
| async_tree_io                    | 507 ms                                                 | 583 ms: 1.15x slower                                                   |
| async_tree_io_tg                 | 497 ms                                                 | 611 ms: 1.23x slower                                                   |
| async_tree_eager_io              | 514 ms                                                 | 654 ms: 1.27x slower                                                   |
| async_tree_eager_io_tg           | 477 ms                                                 | 704 ms: 1.48x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 56.0 ms                                                | 49.8 ms: 1.13x faster                                                  |
| nbody          | 74.0 ms                                                | 66.0 ms: 1.12x faster                                                  |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 78.6 ms                                                | 68.1 ms: 1.15x faster                                                  |
| regex_effbot   | 2.63 ms                                                | 2.45 ms: 1.07x faster                                                  |
| regex_dna      | 149 ms                                                 | 142 ms: 1.05x faster                                                   |
| regex_v8       | 17.0 ms                                                | 16.6 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 214 us                                                 | 183 us: 1.17x faster                                                   |
| unpickle_pure_python | 164 us                                                 | 142 us: 1.15x faster                                                   |
| xml_etree_process    | 41.0 ms                                                | 37.2 ms: 1.10x faster                                                  |
| xml_etree_generate   | 57.0 ms                                                | 52.3 ms: 1.09x faster                                                  |
| tomli_loads          | 1.57 sec                                               | 1.49 sec: 1.05x faster                                                 |
| json_loads           | 17.0 us                                                | 16.6 us: 1.02x faster                                                  |
| xml_etree_iterparse  | 73.6 ms                                                | 74.6 ms: 1.01x slower                                                  |
| json_dumps           | 6.52 ms                                                | 7.18 ms: 1.10x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 14.5 ms                                                | 14.3 ms: 1.01x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 13.8 ms: 1.22x faster                                                  |
| genshi_xml      | 34.4 ms                                                | 30.1 ms: 1.14x faster                                                  |
| django_template | 22.2 ms                                                | 19.9 ms: 1.12x faster                                                  |
| mako            | 7.68 ms                                                | 6.97 ms: 1.10x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.15x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy                         | 237 us                                                 | 145 us: 1.63x faster                                                   |
| deepcopy_memo                    | 27.4 us                                                | 17.0 us: 1.61x faster                                                  |
| generators                       | 31.5 ms                                                | 20.1 ms: 1.57x faster                                                  |
| go                               | 115 ms                                                 | 82.4 ms: 1.40x faster                                                  |
| deepcopy_reduce                  | 2.07 us                                                | 1.54 us: 1.35x faster                                                  |
| genshi_text                      | 16.9 ms                                                | 13.8 ms: 1.22x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 236 ms: 1.22x faster                                                   |
| html5lib                         | 36.6 ms                                                | 30.1 ms: 1.22x faster                                                  |
| deltablue                        | 2.68 ms                                                | 2.24 ms: 1.20x faster                                                  |
| coroutines                       | 19.8 ms                                                | 16.5 ms: 1.20x faster                                                  |
| logging_simple                   | 3.60 us                                                | 3.03 us: 1.19x faster                                                  |
| logging_format                   | 3.89 us                                                | 3.31 us: 1.18x faster                                                  |
| hexiom                           | 4.86 ms                                                | 4.13 ms: 1.18x faster                                                  |
| raytrace                         | 181 ms                                                 | 154 ms: 1.18x faster                                                   |
| pickle_pure_python               | 214 us                                                 | 183 us: 1.17x faster                                                   |
| 2to3                             | 187 ms                                                 | 160 ms: 1.17x faster                                                   |
| pprint_safe_repr                 | 533 ms                                                 | 459 ms: 1.16x faster                                                   |
| pprint_pformat                   | 1.08 sec                                               | 935 ms: 1.16x faster                                                   |
| regex_compile                    | 78.6 ms                                                | 68.1 ms: 1.15x faster                                                  |
| unpickle_pure_python             | 164 us                                                 | 142 us: 1.15x faster                                                   |
| logging_silent                   | 70.1 ns                                                | 60.9 ns: 1.15x faster                                                  |
| sqlglot_parse                    | 856 us                                                 | 746 us: 1.15x faster                                                   |
| async_tree_eager                 | 70.1 ms                                                | 61.1 ms: 1.15x faster                                                  |
| scimark_lu                       | 76.7 ms                                                | 67.0 ms: 1.14x faster                                                  |
| genshi_xml                       | 34.4 ms                                                | 30.1 ms: 1.14x faster                                                  |
| nqueens                          | 62.5 ms                                                | 54.8 ms: 1.14x faster                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 44.2 ms: 1.14x faster                                                  |
| sqlglot_normalize                | 189 ms                                                 | 166 ms: 1.14x faster                                                   |
| sqlglot_transpile                | 1.02 ms                                                | 902 us: 1.13x faster                                                   |
| async_tree_eager_tg              | 47.8 ms                                                | 42.3 ms: 1.13x faster                                                  |
| richards                         | 35.2 ms                                                | 31.1 ms: 1.13x faster                                                  |
| richards_super                   | 39.1 ms                                                | 34.6 ms: 1.13x faster                                                  |
| float                            | 56.0 ms                                                | 49.8 ms: 1.13x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 150 ms: 1.12x faster                                                   |
| sqlglot_optimize                 | 34.9 ms                                                | 31.1 ms: 1.12x faster                                                  |
| nbody                            | 74.0 ms                                                | 66.0 ms: 1.12x faster                                                  |
| chaos                            | 41.2 ms                                                | 36.8 ms: 1.12x faster                                                  |
| django_template                  | 22.2 ms                                                | 19.9 ms: 1.12x faster                                                  |
| bench_thread_pool                | 505 us                                                 | 453 us: 1.11x faster                                                   |
| thrift                           | 466 us                                                 | 419 us: 1.11x faster                                                   |
| pycparser                        | 705 ms                                                 | 635 ms: 1.11x faster                                                   |
| xml_etree_process                | 41.0 ms                                                | 37.2 ms: 1.10x faster                                                  |
| mako                             | 7.68 ms                                                | 6.97 ms: 1.10x faster                                                  |
| scimark_sor                      | 105 ms                                                 | 96.1 ms: 1.10x faster                                                  |
| spectral_norm                    | 76.3 ms                                                | 70.0 ms: 1.09x faster                                                  |
| sympy_expand                     | 246 ms                                                 | 226 ms: 1.09x faster                                                   |
| xml_etree_generate               | 57.0 ms                                                | 52.3 ms: 1.09x faster                                                  |
| typing_runtime_protocols         | 101 us                                                 | 93.0 us: 1.09x faster                                                  |
| sympy_str                        | 145 ms                                                 | 134 ms: 1.09x faster                                                   |
| async_tree_none                  | 215 ms                                                 | 199 ms: 1.08x faster                                                   |
| sympy_sum                        | 75.4 ms                                                | 69.8 ms: 1.08x faster                                                  |
| pyflate                          | 351 ms                                                 | 326 ms: 1.08x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 249 ms: 1.08x faster                                                   |
| comprehensions                   | 12.3 us                                                | 11.4 us: 1.08x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.45 ms: 1.07x faster                                                  |
| async_generators                 | 295 ms                                                 | 277 ms: 1.07x faster                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 130 ms: 1.06x faster                                                   |
| pathlib                          | 23.4 ms                                                | 22.0 ms: 1.06x faster                                                  |
| fannkuch                         | 284 ms                                                 | 267 ms: 1.06x faster                                                   |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.82 ms: 1.06x faster                                                  |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.36 ms: 1.05x faster                                                  |
| sqlalchemy_declarative           | 58.9 ms                                                | 56.0 ms: 1.05x faster                                                  |
| coverage                         | 46.0 ms                                                | 43.7 ms: 1.05x faster                                                  |
| tomli_loads                      | 1.57 sec                                               | 1.49 sec: 1.05x faster                                                 |
| crypto_pyaes                     | 54.2 ms                                                | 51.7 ms: 1.05x faster                                                  |
| regex_dna                        | 149 ms                                                 | 142 ms: 1.05x faster                                                   |
| scimark_fft                      | 201 ms                                                 | 192 ms: 1.05x faster                                                   |
| meteor_contest                   | 74.0 ms                                                | 70.6 ms: 1.05x faster                                                  |
| sphinx                           | 603 ms                                                 | 576 ms: 1.05x faster                                                   |
| json                             | 3.03 ms                                                | 2.90 ms: 1.05x faster                                                  |
| bpe_tokeniser                    | 3.25 sec                                               | 3.11 sec: 1.04x faster                                                 |
| bench_mp_pool                    | 62.5 ms                                                | 59.9 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 359 ms: 1.04x faster                                                   |
| telco                            | 4.76 ms                                                | 4.59 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 335 ms: 1.04x faster                                                   |
| dulwich_log                      | 28.5 ms                                                | 27.6 ms: 1.03x faster                                                  |
| sympy_integrate                  | 11.3 ms                                                | 11.0 ms: 1.03x faster                                                  |
| docutils                         | 1.44 sec                                               | 1.40 sec: 1.03x faster                                                 |
| regex_v8                         | 17.0 ms                                                | 16.6 ms: 1.02x faster                                                  |
| json_loads                       | 17.0 us                                                | 16.6 us: 1.02x faster                                                  |
| python_startup_no_site           | 14.5 ms                                                | 14.3 ms: 1.01x faster                                                  |
| mdp                              | 1.49 sec                                               | 1.48 sec: 1.01x faster                                                 |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                                   |
| gc_traversal                     | 2.91 ms                                                | 2.93 ms: 1.01x slower                                                  |
| xml_etree_iterparse              | 73.6 ms                                                | 74.6 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 469 ms: 1.05x slower                                                   |
| async_tree_none_tg               | 198 ms                                                 | 217 ms: 1.09x slower                                                   |
| json_dumps                       | 6.52 ms                                                | 7.18 ms: 1.10x slower                                                  |
| create_gc_cycles                 | 1.17 ms                                                | 1.31 ms: 1.12x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 583 ms: 1.15x slower                                                   |
| async_tree_io_tg                 | 497 ms                                                 | 611 ms: 1.23x slower                                                   |
| async_tree_eager_io              | 514 ms                                                 | 654 ms: 1.27x slower                                                   |
| async_tree_eager_io_tg           | 477 ms                                                 | 704 ms: 1.48x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.09x faster                                                           |

Benchmark hidden because not significant (6): tornado_http, async_tree_cpu_io_mixed, pylint, python_startup, asyncio_websockets, xml_etree_parse
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dask, gevent_hub, k_core, mypy2, shortest_path

- Geometric mean (including insignificant results): 1.083x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.01x