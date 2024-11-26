# Results vs. 3.13.0

- fork: brandtbucher
- ref: jump_backoff
- machine: darwin-arm64
- commit hash: 5dd5806
- commit date: 2024-11-13
- overall geometric mean: 1.030x faster
- HPT reliability: 98.75%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-darwin-arm64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 177 ms: 1.06x faster                                                 |
| docutils       | 1.44 sec                                               | 1.55 sec: 1.08x slower                                               |
| html5lib       | 36.6 ms                                                | 32.6 ms: 1.12x faster                                                |
| sphinx         | 603 ms                                                 | 649 ms: 1.08x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-darwin-arm64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 240 ms: 1.20x faster                                                 |
| coroutines                       | 19.8 ms                                                | 17.4 ms: 1.13x faster                                                |
| async_tree_eager_memoization     | 168 ms                                                 | 157 ms: 1.07x faster                                                 |
| async_tree_memoization           | 268 ms                                                 | 254 ms: 1.05x faster                                                 |
| async_tree_eager_tg              | 47.8 ms                                                | 45.6 ms: 1.05x faster                                                |
| async_tree_none                  | 215 ms                                                 | 206 ms: 1.05x faster                                                 |
| async_tree_eager                 | 70.1 ms                                                | 67.3 ms: 1.04x faster                                                |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 133 ms: 1.04x faster                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 340 ms: 1.02x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 368 ms: 1.01x faster                                                 |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 468 ms: 1.02x slower                                                 |
| async_generators                 | 295 ms                                                 | 306 ms: 1.04x slower                                                 |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 479 ms: 1.07x slower                                                 |
| async_tree_none_tg               | 198 ms                                                 | 218 ms: 1.10x slower                                                 |
| async_tree_io                    | 507 ms                                                 | 591 ms: 1.17x slower                                                 |
| async_tree_io_tg                 | 497 ms                                                 | 627 ms: 1.26x slower                                                 |
| async_tree_eager_io              | 514 ms                                                 | 686 ms: 1.33x slower                                                 |
| async_tree_eager_io_tg           | 477 ms                                                 | 727 ms: 1.52x slower                                                 |
| Geometric mean                   | (ref)                                                  | 1.04x slower                                                         |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-darwin-arm64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 74.0 ms                                                | 63.0 ms: 1.18x faster                                                |
| float          | 56.0 ms                                                | 48.8 ms: 1.15x faster                                                |
| Geometric mean | (ref)                                                  | 1.10x faster                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-darwin-arm64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.33 ms: 1.13x faster                                                |
| regex_dna      | 149 ms                                                 | 136 ms: 1.10x faster                                                 |
| regex_v8       | 17.0 ms                                                | 15.8 ms: 1.07x faster                                                |
| regex_compile  | 78.6 ms                                                | 73.4 ms: 1.07x faster                                                |
| Geometric mean | (ref)                                                  | 1.09x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-darwin-arm64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| unpickle_pure_python | 164 us                                                 | 122 us: 1.34x faster                                                 |
| tomli_loads          | 1.57 sec                                               | 1.26 sec: 1.25x faster                                               |
| xml_etree_process    | 41.0 ms                                                | 35.3 ms: 1.16x faster                                                |
| xml_etree_generate   | 57.0 ms                                                | 49.8 ms: 1.14x faster                                                |
| pickle_pure_python   | 214 us                                                 | 194 us: 1.11x faster                                                 |
| json_loads           | 17.0 us                                                | 16.5 us: 1.03x faster                                                |
| xml_etree_iterparse  | 73.6 ms                                                | 72.0 ms: 1.02x faster                                                |
| xml_etree_parse      | 107 ms                                                 | 105 ms: 1.02x faster                                                 |
| json_dumps           | 6.52 ms                                                | 7.11 ms: 1.09x slower                                                |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-darwin-arm64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 14.5 ms                                                | 15.0 ms: 1.04x slower                                                |
| python_startup         | 18.9 ms                                                | 19.7 ms: 1.04x slower                                                |
| Geometric mean         | (ref)                                                  | 1.04x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-darwin-arm64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.23 ms: 1.23x faster                                                |
| genshi_text     | 16.9 ms                                                | 15.7 ms: 1.08x faster                                                |
| django_template | 22.2 ms                                                | 22.3 ms: 1.00x slower                                                |
| genshi_xml      | 34.4 ms                                                | 38.6 ms: 1.12x slower                                                |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                         |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-darwin-arm64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| deepcopy_memo                    | 27.4 us                                                | 17.6 us: 1.55x faster                                                |
| deepcopy                         | 237 us                                                 | 158 us: 1.50x faster                                                 |
| deepcopy_reduce                  | 2.07 us                                                | 1.54 us: 1.34x faster                                                |
| unpickle_pure_python             | 164 us                                                 | 122 us: 1.34x faster                                                 |
| tomli_loads                      | 1.57 sec                                               | 1.26 sec: 1.25x faster                                               |
| mako                             | 7.68 ms                                                | 6.23 ms: 1.23x faster                                                |
| scimark_sor                      | 105 ms                                                 | 87.2 ms: 1.21x faster                                                |
| async_tree_memoization_tg        | 288 ms                                                 | 240 ms: 1.20x faster                                                 |
| generators                       | 31.5 ms                                                | 26.7 ms: 1.18x faster                                                |
| nbody                            | 74.0 ms                                                | 63.0 ms: 1.18x faster                                                |
| xml_etree_process                | 41.0 ms                                                | 35.3 ms: 1.16x faster                                                |
| go                               | 115 ms                                                 | 99.9 ms: 1.15x faster                                                |
| float                            | 56.0 ms                                                | 48.8 ms: 1.15x faster                                                |
| xml_etree_generate               | 57.0 ms                                                | 49.8 ms: 1.14x faster                                                |
| coroutines                       | 19.8 ms                                                | 17.4 ms: 1.13x faster                                                |
| regex_effbot                     | 2.63 ms                                                | 2.33 ms: 1.13x faster                                                |
| html5lib                         | 36.6 ms                                                | 32.6 ms: 1.12x faster                                                |
| scimark_monte_carlo              | 50.4 ms                                                | 45.2 ms: 1.11x faster                                                |
| scimark_lu                       | 76.7 ms                                                | 68.9 ms: 1.11x faster                                                |
| pprint_safe_repr                 | 533 ms                                                 | 480 ms: 1.11x faster                                                 |
| pickle_pure_python               | 214 us                                                 | 194 us: 1.11x faster                                                 |
| pprint_pformat                   | 1.08 sec                                               | 982 ms: 1.10x faster                                                 |
| regex_dna                        | 149 ms                                                 | 136 ms: 1.10x faster                                                 |
| spectral_norm                    | 76.3 ms                                                | 69.8 ms: 1.09x faster                                                |
| logging_simple                   | 3.60 us                                                | 3.33 us: 1.08x faster                                                |
| scimark_fft                      | 201 ms                                                 | 186 ms: 1.08x faster                                                 |
| genshi_text                      | 16.9 ms                                                | 15.7 ms: 1.08x faster                                                |
| regex_v8                         | 17.0 ms                                                | 15.8 ms: 1.07x faster                                                |
| async_tree_eager_memoization     | 168 ms                                                 | 157 ms: 1.07x faster                                                 |
| pyflate                          | 351 ms                                                 | 328 ms: 1.07x faster                                                 |
| regex_compile                    | 78.6 ms                                                | 73.4 ms: 1.07x faster                                                |
| connected_components             | 319 ms                                                 | 298 ms: 1.07x faster                                                 |
| telco                            | 4.76 ms                                                | 4.48 ms: 1.06x faster                                                |
| logging_format                   | 3.89 us                                                | 3.66 us: 1.06x faster                                                |
| json                             | 3.03 ms                                                | 2.86 ms: 1.06x faster                                                |
| thrift                           | 466 us                                                 | 441 us: 1.06x faster                                                 |
| 2to3                             | 187 ms                                                 | 177 ms: 1.06x faster                                                 |
| bpe_tokeniser                    | 3.25 sec                                               | 3.08 sec: 1.05x faster                                               |
| async_tree_memoization           | 268 ms                                                 | 254 ms: 1.05x faster                                                 |
| richards                         | 35.2 ms                                                | 33.4 ms: 1.05x faster                                                |
| pycparser                        | 705 ms                                                 | 672 ms: 1.05x faster                                                 |
| richards_super                   | 39.1 ms                                                | 37.3 ms: 1.05x faster                                                |
| async_tree_eager_tg              | 47.8 ms                                                | 45.6 ms: 1.05x faster                                                |
| bench_thread_pool                | 505 us                                                 | 482 us: 1.05x faster                                                 |
| async_tree_none                  | 215 ms                                                 | 206 ms: 1.05x faster                                                 |
| shortest_path                    | 347 ms                                                 | 332 ms: 1.04x faster                                                 |
| async_tree_eager                 | 70.1 ms                                                | 67.3 ms: 1.04x faster                                                |
| coverage                         | 46.0 ms                                                | 44.3 ms: 1.04x faster                                                |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 133 ms: 1.04x faster                                                 |
| deltablue                        | 2.68 ms                                                | 2.59 ms: 1.03x faster                                                |
| json_loads                       | 17.0 us                                                | 16.5 us: 1.03x faster                                                |
| fannkuch                         | 284 ms                                                 | 278 ms: 1.02x faster                                                 |
| xml_etree_iterparse              | 73.6 ms                                                | 72.0 ms: 1.02x faster                                                |
| pathlib                          | 23.4 ms                                                | 22.9 ms: 1.02x faster                                                |
| nqueens                          | 62.5 ms                                                | 61.3 ms: 1.02x faster                                                |
| typing_runtime_protocols         | 101 us                                                 | 99.2 us: 1.02x faster                                                |
| meteor_contest                   | 74.0 ms                                                | 72.6 ms: 1.02x faster                                                |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 340 ms: 1.02x faster                                                 |
| xml_etree_parse                  | 107 ms                                                 | 105 ms: 1.02x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 368 ms: 1.01x faster                                                 |
| sqlglot_normalize                | 189 ms                                                 | 187 ms: 1.01x faster                                                 |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.64 ms: 1.01x faster                                                |
| bench_mp_pool                    | 62.5 ms                                                | 62.2 ms: 1.01x faster                                                |
| django_template                  | 22.2 ms                                                | 22.3 ms: 1.00x slower                                                |
| sympy_sum                        | 75.4 ms                                                | 75.8 ms: 1.01x slower                                                |
| gc_traversal                     | 2.91 ms                                                | 2.93 ms: 1.01x slower                                                |
| sqlalchemy_declarative           | 58.9 ms                                                | 59.4 ms: 1.01x slower                                                |
| crypto_pyaes                     | 54.2 ms                                                | 54.8 ms: 1.01x slower                                                |
| sympy_str                        | 145 ms                                                 | 147 ms: 1.01x slower                                                 |
| hexiom                           | 4.86 ms                                                | 4.93 ms: 1.01x slower                                                |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 468 ms: 1.02x slower                                                 |
| sqlglot_parse                    | 856 us                                                 | 873 us: 1.02x slower                                                 |
| dulwich_log                      | 28.5 ms                                                | 29.1 ms: 1.02x slower                                                |
| raytrace                         | 181 ms                                                 | 186 ms: 1.03x slower                                                 |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 3.08 ms: 1.03x slower                                                |
| sqlglot_transpile                | 1.02 ms                                                | 1.06 ms: 1.03x slower                                                |
| python_startup_no_site           | 14.5 ms                                                | 15.0 ms: 1.04x slower                                                |
| async_generators                 | 295 ms                                                 | 306 ms: 1.04x slower                                                 |
| sympy_expand                     | 246 ms                                                 | 255 ms: 1.04x slower                                                 |
| python_startup                   | 18.9 ms                                                | 19.7 ms: 1.04x slower                                                |
| logging_silent                   | 70.1 ns                                                | 73.8 ns: 1.05x slower                                                |
| chaos                            | 41.2 ms                                                | 43.4 ms: 1.05x slower                                                |
| sympy_integrate                  | 11.3 ms                                                | 12.0 ms: 1.06x slower                                                |
| mdp                              | 1.49 sec                                               | 1.59 sec: 1.06x slower                                               |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 479 ms: 1.07x slower                                                 |
| sphinx                           | 603 ms                                                 | 649 ms: 1.08x slower                                                 |
| docutils                         | 1.44 sec                                               | 1.55 sec: 1.08x slower                                               |
| json_dumps                       | 6.52 ms                                                | 7.11 ms: 1.09x slower                                                |
| async_tree_none_tg               | 198 ms                                                 | 218 ms: 1.10x slower                                                 |
| comprehensions                   | 12.3 us                                                | 13.7 us: 1.11x slower                                                |
| genshi_xml                       | 34.4 ms                                                | 38.6 ms: 1.12x slower                                                |
| create_gc_cycles                 | 1.17 ms                                                | 1.33 ms: 1.14x slower                                                |
| async_tree_io                    | 507 ms                                                 | 591 ms: 1.17x slower                                                 |
| async_tree_io_tg                 | 497 ms                                                 | 627 ms: 1.26x slower                                                 |
| async_tree_eager_io              | 514 ms                                                 | 686 ms: 1.33x slower                                                 |
| k_core                           | 1.61 sec                                               | 2.26 sec: 1.41x slower                                               |
| async_tree_eager_io_tg           | 477 ms                                                 | 727 ms: 1.52x slower                                                 |
| Geometric mean                   | (ref)                                                  | 1.03x faster                                                         |

Benchmark hidden because not significant (4): sqlglot_optimize, asyncio_websockets, pidigits, pylint
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, gevent_hub, mypy2, tornado_http
Ignored benchmarks (1) of results/bm-20241113-3.14.0a1+-5dd5806-JIT/bm-20241113-darwin-arm64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806.json: sqlite_synth

- Geometric mean (including insignificant results): 1.030x faster
# HPT report

- Reliability score: 98.75% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x