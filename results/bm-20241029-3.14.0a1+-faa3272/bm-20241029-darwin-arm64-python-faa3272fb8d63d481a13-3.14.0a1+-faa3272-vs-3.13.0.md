# Results vs. 3.13.0

- fork: python
- ref: faa3272fb8d63d481a13
- machine: darwin-arm64
- commit hash: faa3272
- commit date: 2024-10-29
- overall geometric mean: 1.078x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-darwin-arm64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 165 ms: 1.14x faster                                                   |
| docutils       | 1.44 sec                                               | 1.41 sec: 1.02x faster                                                 |
| html5lib       | 36.6 ms                                                | 30.2 ms: 1.21x faster                                                  |
| sphinx         | 603 ms                                                 | 581 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-darwin-arm64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 234 ms: 1.23x faster                                                   |
| coroutines                       | 19.8 ms                                                | 16.3 ms: 1.21x faster                                                  |
| async_tree_eager                 | 70.1 ms                                                | 60.8 ms: 1.15x faster                                                  |
| async_tree_eager_tg              | 47.8 ms                                                | 42.1 ms: 1.14x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 152 ms: 1.11x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 247 ms: 1.08x faster                                                   |
| async_tree_none                  | 215 ms                                                 | 200 ms: 1.08x faster                                                   |
| async_generators                 | 295 ms                                                 | 277 ms: 1.06x faster                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 131 ms: 1.05x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 357 ms: 1.04x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 333 ms: 1.04x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 469 ms: 1.05x slower                                                   |
| async_tree_none_tg               | 198 ms                                                 | 214 ms: 1.08x slower                                                   |
| async_tree_io                    | 507 ms                                                 | 596 ms: 1.18x slower                                                   |
| async_tree_io_tg                 | 497 ms                                                 | 618 ms: 1.24x slower                                                   |
| async_tree_eager_io              | 514 ms                                                 | 670 ms: 1.30x slower                                                   |
| async_tree_eager_io_tg           | 477 ms                                                 | 730 ms: 1.53x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-darwin-arm64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 56.0 ms                                                | 49.5 ms: 1.13x faster                                                  |
| nbody          | 74.0 ms                                                | 65.5 ms: 1.13x faster                                                  |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-darwin-arm64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 78.6 ms                                                | 68.6 ms: 1.15x faster                                                  |
| regex_effbot   | 2.63 ms                                                | 2.44 ms: 1.07x faster                                                  |
| regex_dna      | 149 ms                                                 | 141 ms: 1.06x faster                                                   |
| regex_v8       | 17.0 ms                                                | 16.7 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-darwin-arm64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 214 us                                                 | 184 us: 1.16x faster                                                   |
| unpickle_pure_python | 164 us                                                 | 143 us: 1.15x faster                                                   |
| xml_etree_generate   | 57.0 ms                                                | 52.7 ms: 1.08x faster                                                  |
| xml_etree_process    | 41.0 ms                                                | 37.9 ms: 1.08x faster                                                  |
| tomli_loads          | 1.57 sec                                               | 1.49 sec: 1.05x faster                                                 |
| json_loads           | 17.0 us                                                | 16.5 us: 1.03x faster                                                  |
| json_dumps           | 6.52 ms                                                | 7.26 ms: 1.11x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-darwin-arm64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 14.5 ms                                                | 12.2 ms: 1.19x faster                                                  |
| python_startup         | 18.9 ms                                                | 16.8 ms: 1.13x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.16x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-darwin-arm64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 13.7 ms: 1.23x faster                                                  |
| mako            | 7.68 ms                                                | 6.60 ms: 1.16x faster                                                  |
| genshi_xml      | 34.4 ms                                                | 30.0 ms: 1.15x faster                                                  |
| django_template | 22.2 ms                                                | 19.7 ms: 1.13x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.17x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-darwin-arm64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy                         | 237 us                                                 | 146 us: 1.62x faster                                                   |
| deepcopy_memo                    | 27.4 us                                                | 17.0 us: 1.61x faster                                                  |
| generators                       | 31.5 ms                                                | 20.2 ms: 1.56x faster                                                  |
| go                               | 115 ms                                                 | 82.9 ms: 1.39x faster                                                  |
| deepcopy_reduce                  | 2.07 us                                                | 1.51 us: 1.37x faster                                                  |
| genshi_text                      | 16.9 ms                                                | 13.7 ms: 1.23x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 234 ms: 1.23x faster                                                   |
| html5lib                         | 36.6 ms                                                | 30.2 ms: 1.21x faster                                                  |
| coroutines                       | 19.8 ms                                                | 16.3 ms: 1.21x faster                                                  |
| deltablue                        | 2.68 ms                                                | 2.25 ms: 1.19x faster                                                  |
| python_startup_no_site           | 14.5 ms                                                | 12.2 ms: 1.19x faster                                                  |
| logging_simple                   | 3.60 us                                                | 3.06 us: 1.18x faster                                                  |
| raytrace                         | 181 ms                                                 | 154 ms: 1.18x faster                                                   |
| hexiom                           | 4.86 ms                                                | 4.14 ms: 1.17x faster                                                  |
| pickle_pure_python               | 214 us                                                 | 184 us: 1.16x faster                                                   |
| pprint_safe_repr                 | 533 ms                                                 | 458 ms: 1.16x faster                                                   |
| mako                             | 7.68 ms                                                | 6.60 ms: 1.16x faster                                                  |
| logging_format                   | 3.89 us                                                | 3.35 us: 1.16x faster                                                  |
| pprint_pformat                   | 1.08 sec                                               | 935 ms: 1.16x faster                                                   |
| scimark_monte_carlo              | 50.4 ms                                                | 43.6 ms: 1.16x faster                                                  |
| async_tree_eager                 | 70.1 ms                                                | 60.8 ms: 1.15x faster                                                  |
| bench_thread_pool                | 505 us                                                 | 438 us: 1.15x faster                                                   |
| sqlglot_parse                    | 856 us                                                 | 743 us: 1.15x faster                                                   |
| unpickle_pure_python             | 164 us                                                 | 143 us: 1.15x faster                                                   |
| genshi_xml                       | 34.4 ms                                                | 30.0 ms: 1.15x faster                                                  |
| regex_compile                    | 78.6 ms                                                | 68.6 ms: 1.15x faster                                                  |
| nqueens                          | 62.5 ms                                                | 54.7 ms: 1.14x faster                                                  |
| 2to3                             | 187 ms                                                 | 165 ms: 1.14x faster                                                   |
| async_tree_eager_tg              | 47.8 ms                                                | 42.1 ms: 1.14x faster                                                  |
| chaos                            | 41.2 ms                                                | 36.3 ms: 1.14x faster                                                  |
| scimark_lu                       | 76.7 ms                                                | 67.6 ms: 1.13x faster                                                  |
| float                            | 56.0 ms                                                | 49.5 ms: 1.13x faster                                                  |
| richards_super                   | 39.1 ms                                                | 34.6 ms: 1.13x faster                                                  |
| richards                         | 35.2 ms                                                | 31.1 ms: 1.13x faster                                                  |
| nbody                            | 74.0 ms                                                | 65.5 ms: 1.13x faster                                                  |
| django_template                  | 22.2 ms                                                | 19.7 ms: 1.13x faster                                                  |
| python_startup                   | 18.9 ms                                                | 16.8 ms: 1.13x faster                                                  |
| sqlglot_transpile                | 1.02 ms                                                | 907 us: 1.13x faster                                                   |
| sqlglot_normalize                | 189 ms                                                 | 168 ms: 1.12x faster                                                   |
| thrift                           | 466 us                                                 | 416 us: 1.12x faster                                                   |
| logging_silent                   | 70.1 ns                                                | 62.6 ns: 1.12x faster                                                  |
| sqlglot_optimize                 | 34.9 ms                                                | 31.4 ms: 1.11x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 152 ms: 1.11x faster                                                   |
| pycparser                        | 705 ms                                                 | 638 ms: 1.11x faster                                                   |
| spectral_norm                    | 76.3 ms                                                | 69.5 ms: 1.10x faster                                                  |
| scimark_sor                      | 105 ms                                                 | 96.2 ms: 1.10x faster                                                  |
| typing_runtime_protocols         | 101 us                                                 | 92.4 us: 1.10x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 247 ms: 1.08x faster                                                   |
| sympy_expand                     | 246 ms                                                 | 227 ms: 1.08x faster                                                   |
| xml_etree_generate               | 57.0 ms                                                | 52.7 ms: 1.08x faster                                                  |
| pyflate                          | 351 ms                                                 | 325 ms: 1.08x faster                                                   |
| sympy_str                        | 145 ms                                                 | 135 ms: 1.08x faster                                                   |
| xml_etree_process                | 41.0 ms                                                | 37.9 ms: 1.08x faster                                                  |
| async_tree_none                  | 215 ms                                                 | 200 ms: 1.08x faster                                                   |
| sympy_sum                        | 75.4 ms                                                | 69.9 ms: 1.08x faster                                                  |
| comprehensions                   | 12.3 us                                                | 11.4 us: 1.08x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.44 ms: 1.07x faster                                                  |
| fannkuch                         | 284 ms                                                 | 265 ms: 1.07x faster                                                   |
| bench_mp_pool                    | 62.5 ms                                                | 58.5 ms: 1.07x faster                                                  |
| async_generators                 | 295 ms                                                 | 277 ms: 1.06x faster                                                   |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.82 ms: 1.06x faster                                                  |
| crypto_pyaes                     | 54.2 ms                                                | 51.2 ms: 1.06x faster                                                  |
| regex_dna                        | 149 ms                                                 | 141 ms: 1.06x faster                                                   |
| scimark_fft                      | 201 ms                                                 | 190 ms: 1.06x faster                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 131 ms: 1.05x faster                                                   |
| tomli_loads                      | 1.57 sec                                               | 1.49 sec: 1.05x faster                                                 |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.37 ms: 1.05x faster                                                  |
| dulwich_log                      | 28.5 ms                                                | 27.2 ms: 1.05x faster                                                  |
| json                             | 3.03 ms                                                | 2.89 ms: 1.05x faster                                                  |
| sqlalchemy_declarative           | 58.9 ms                                                | 56.1 ms: 1.05x faster                                                  |
| bpe_tokeniser                    | 3.25 sec                                               | 3.10 sec: 1.05x faster                                                 |
| coverage                         | 46.0 ms                                                | 44.0 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 357 ms: 1.04x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 333 ms: 1.04x faster                                                   |
| pathlib                          | 23.4 ms                                                | 22.4 ms: 1.04x faster                                                  |
| meteor_contest                   | 74.0 ms                                                | 71.1 ms: 1.04x faster                                                  |
| sphinx                           | 603 ms                                                 | 581 ms: 1.04x faster                                                   |
| telco                            | 4.76 ms                                                | 4.64 ms: 1.03x faster                                                  |
| sympy_integrate                  | 11.3 ms                                                | 11.0 ms: 1.03x faster                                                  |
| json_loads                       | 17.0 us                                                | 16.5 us: 1.03x faster                                                  |
| regex_v8                         | 17.0 ms                                                | 16.7 ms: 1.02x faster                                                  |
| docutils                         | 1.44 sec                                               | 1.41 sec: 1.02x faster                                                 |
| mdp                              | 1.49 sec                                               | 1.47 sec: 1.01x faster                                                 |
| shortest_path                    | 347 ms                                                 | 346 ms: 1.00x faster                                                   |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                                   |
| gc_traversal                     | 2.91 ms                                                | 2.97 ms: 1.02x slower                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 469 ms: 1.05x slower                                                   |
| async_tree_none_tg               | 198 ms                                                 | 214 ms: 1.08x slower                                                   |
| json_dumps                       | 6.52 ms                                                | 7.26 ms: 1.11x slower                                                  |
| create_gc_cycles                 | 1.17 ms                                                | 1.33 ms: 1.14x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 596 ms: 1.18x slower                                                   |
| async_tree_io_tg                 | 497 ms                                                 | 618 ms: 1.24x slower                                                   |
| async_tree_eager_io              | 514 ms                                                 | 670 ms: 1.30x slower                                                   |
| k_core                           | 1.61 sec                                               | 2.31 sec: 1.44x slower                                                 |
| async_tree_eager_io_tg           | 477 ms                                                 | 730 ms: 1.53x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.08x faster                                                           |

Benchmark hidden because not significant (7): xml_etree_parse, pylint, async_tree_cpu_io_mixed, tornado_http, xml_etree_iterparse, asyncio_websockets, connected_components
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, gevent_hub, mypy2
Ignored benchmarks (1) of results/bm-20241029-3.14.0a1+-faa3272/bm-20241029-darwin-arm64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272.json: sqlite_synth

- Geometric mean (including insignificant results): 1.078x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.01x