# Results vs. 3.13.0

- fork: python
- ref: 2de048ce79e621f5ae05
- machine: darwin-arm64
- commit hash: 2de048c
- commit date: 2024-12-13
- overall geometric mean: 1.073x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-darwin-arm64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 181 ms                                                 | 170 ms: 1.07x faster                                                   |
| docutils       | 1.44 sec                                               | 1.45 sec: 1.01x slower                                                 |
| html5lib       | 36.6 ms                                                | 33.4 ms: 1.10x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-darwin-arm64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 289 ms                                                 | 193 ms: 1.50x faster                                                   |
| async_tree_io_tg                 | 499 ms                                                 | 361 ms: 1.38x faster                                                   |
| async_tree_eager_io              | 514 ms                                                 | 372 ms: 1.38x faster                                                   |
| async_tree_io                    | 510 ms                                                 | 378 ms: 1.35x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 205 ms: 1.31x faster                                                   |
| async_tree_none_tg               | 199 ms                                                 | 154 ms: 1.29x faster                                                   |
| async_tree_eager_io_tg           | 481 ms                                                 | 375 ms: 1.28x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 168 ms: 1.27x faster                                                   |
| coroutines                       | 19.8 ms                                                | 17.5 ms: 1.13x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 150 ms: 1.13x faster                                                   |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 422 ms: 1.09x faster                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 128 ms: 1.07x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 419 ms: 1.07x faster                                                   |
| async_tree_eager_tg              | 48.0 ms                                                | 45.8 ms: 1.05x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 67.8 ms: 1.03x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 368 ms: 1.01x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 346 ms                                                 | 344 ms: 1.01x faster                                                   |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.01x faster                                                   |
| async_generators                 | 292 ms                                                 | 300 ms: 1.03x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.17x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-darwin-arm64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 56.3 ms                                                | 47.8 ms: 1.18x faster                                                  |
| nbody          | 73.9 ms                                                | 63.7 ms: 1.16x faster                                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-darwin-arm64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.62 ms                                                | 2.01 ms: 1.30x faster                                                  |
| regex_compile  | 78.6 ms                                                | 69.5 ms: 1.13x faster                                                  |
| regex_dna      | 148 ms                                                 | 136 ms: 1.09x faster                                                   |
| regex_v8       | 17.0 ms                                                | 16.0 ms: 1.06x faster                                                  |
| Geometric mean | (ref)                                                  | 1.14x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-darwin-arm64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 164 us                                                 | 125 us: 1.31x faster                                                   |
| tomli_loads          | 1.56 sec                                               | 1.21 sec: 1.29x faster                                                 |
| xml_etree_process    | 41.0 ms                                                | 35.1 ms: 1.17x faster                                                  |
| xml_etree_generate   | 57.0 ms                                                | 49.3 ms: 1.16x faster                                                  |
| pickle_pure_python   | 214 us                                                 | 197 us: 1.08x faster                                                   |
| xml_etree_iterparse  | 74.1 ms                                                | 69.9 ms: 1.06x faster                                                  |
| xml_etree_parse      | 107 ms                                                 | 103 ms: 1.04x faster                                                   |
| json_loads           | 17.0 us                                                | 16.5 us: 1.03x faster                                                  |
| json_dumps           | 6.51 ms                                                | 7.16 ms: 1.10x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-darwin-arm64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                | 21.6 ms: 1.05x slower                                                  |
| python_startup_no_site | 15.8 ms                                                | 16.6 ms: 1.05x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-darwin-arm64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.70 ms                                                | 6.26 ms: 1.23x faster                                                  |
| genshi_text     | 16.9 ms                                                | 17.6 ms: 1.04x slower                                                  |
| django_template | 20.5 ms                                                | 23.2 ms: 1.13x slower                                                  |
| genshi_xml      | 34.1 ms                                                | 41.6 ms: 1.22x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-darwin-arm64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy_memo                    | 27.3 us                                                | 17.2 us: 1.59x faster                                                  |
| async_tree_memoization_tg        | 289 ms                                                 | 193 ms: 1.50x faster                                                   |
| deepcopy                         | 234 us                                                 | 158 us: 1.48x faster                                                   |
| async_tree_io_tg                 | 499 ms                                                 | 361 ms: 1.38x faster                                                   |
| async_tree_eager_io              | 514 ms                                                 | 372 ms: 1.38x faster                                                   |
| async_tree_io                    | 510 ms                                                 | 378 ms: 1.35x faster                                                   |
| unpickle_pure_python             | 164 us                                                 | 125 us: 1.31x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 205 ms: 1.31x faster                                                   |
| deepcopy_reduce                  | 2.08 us                                                | 1.59 us: 1.31x faster                                                  |
| regex_effbot                     | 2.62 ms                                                | 2.01 ms: 1.30x faster                                                  |
| async_tree_none_tg               | 199 ms                                                 | 154 ms: 1.29x faster                                                   |
| tomli_loads                      | 1.56 sec                                               | 1.21 sec: 1.29x faster                                                 |
| scimark_sor                      | 106 ms                                                 | 82.2 ms: 1.28x faster                                                  |
| async_tree_eager_io_tg           | 481 ms                                                 | 375 ms: 1.28x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 168 ms: 1.27x faster                                                   |
| mako                             | 7.70 ms                                                | 6.26 ms: 1.23x faster                                                  |
| spectral_norm                    | 76.3 ms                                                | 62.0 ms: 1.23x faster                                                  |
| float                            | 56.3 ms                                                | 47.8 ms: 1.18x faster                                                  |
| xml_etree_process                | 41.0 ms                                                | 35.1 ms: 1.17x faster                                                  |
| scimark_fft                      | 200 ms                                                 | 172 ms: 1.17x faster                                                   |
| nbody                            | 73.9 ms                                                | 63.7 ms: 1.16x faster                                                  |
| xml_etree_generate               | 57.0 ms                                                | 49.3 ms: 1.16x faster                                                  |
| go                               | 115 ms                                                 | 99.7 ms: 1.15x faster                                                  |
| regex_compile                    | 78.6 ms                                                | 69.5 ms: 1.13x faster                                                  |
| coroutines                       | 19.8 ms                                                | 17.5 ms: 1.13x faster                                                  |
| scimark_monte_carlo              | 50.6 ms                                                | 44.8 ms: 1.13x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 150 ms: 1.13x faster                                                   |
| scimark_lu                       | 76.7 ms                                                | 68.6 ms: 1.12x faster                                                  |
| pyflate                          | 355 ms                                                 | 319 ms: 1.11x faster                                                   |
| generators                       | 31.5 ms                                                | 28.4 ms: 1.11x faster                                                  |
| bpe_tokeniser                    | 3.25 sec                                               | 2.94 sec: 1.11x faster                                                 |
| html5lib                         | 36.6 ms                                                | 33.4 ms: 1.10x faster                                                  |
| pprint_pformat                   | 1.10 sec                                               | 1.01 sec: 1.09x faster                                                 |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 422 ms: 1.09x faster                                                   |
| regex_dna                        | 148 ms                                                 | 136 ms: 1.09x faster                                                   |
| pickle_pure_python               | 214 us                                                 | 197 us: 1.08x faster                                                   |
| connected_components             | 320 ms                                                 | 296 ms: 1.08x faster                                                   |
| pylint                           | 179 ms                                                 | 166 ms: 1.08x faster                                                   |
| pprint_safe_repr                 | 535 ms                                                 | 498 ms: 1.07x faster                                                   |
| telco                            | 4.79 ms                                                | 4.46 ms: 1.07x faster                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 128 ms: 1.07x faster                                                   |
| k_core                           | 1.62 sec                                               | 1.51 sec: 1.07x faster                                                 |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 419 ms: 1.07x faster                                                   |
| 2to3                             | 181 ms                                                 | 170 ms: 1.07x faster                                                   |
| shortest_path                    | 349 ms                                                 | 326 ms: 1.07x faster                                                   |
| json                             | 3.06 ms                                                | 2.88 ms: 1.06x faster                                                  |
| xml_etree_iterparse              | 74.1 ms                                                | 69.9 ms: 1.06x faster                                                  |
| regex_v8                         | 17.0 ms                                                | 16.0 ms: 1.06x faster                                                  |
| thrift                           | 465 us                                                 | 443 us: 1.05x faster                                                   |
| fannkuch                         | 285 ms                                                 | 272 ms: 1.05x faster                                                   |
| logging_simple                   | 3.59 us                                                | 3.43 us: 1.05x faster                                                  |
| async_tree_eager_tg              | 48.0 ms                                                | 45.8 ms: 1.05x faster                                                  |
| deltablue                        | 2.67 ms                                                | 2.55 ms: 1.05x faster                                                  |
| logging_format                   | 3.90 us                                                | 3.73 us: 1.05x faster                                                  |
| xml_etree_parse                  | 107 ms                                                 | 103 ms: 1.04x faster                                                   |
| pathlib                          | 23.3 ms                                                | 22.4 ms: 1.04x faster                                                  |
| pycparser                        | 708 ms                                                 | 680 ms: 1.04x faster                                                   |
| scimark_sparse_mat_mult          | 3.00 ms                                                | 2.89 ms: 1.04x faster                                                  |
| json_loads                       | 17.0 us                                                | 16.5 us: 1.03x faster                                                  |
| meteor_contest                   | 75.1 ms                                                | 72.7 ms: 1.03x faster                                                  |
| coverage                         | 45.5 ms                                                | 44.2 ms: 1.03x faster                                                  |
| typing_runtime_protocols         | 103 us                                                 | 99.5 us: 1.03x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 67.8 ms: 1.03x faster                                                  |
| bench_mp_pool                    | 64.9 ms                                                | 63.3 ms: 1.03x faster                                                  |
| richards_super                   | 39.2 ms                                                | 38.4 ms: 1.02x faster                                                  |
| richards                         | 35.2 ms                                                | 34.6 ms: 1.02x faster                                                  |
| sqlglot_optimize                 | 34.8 ms                                                | 34.2 ms: 1.02x faster                                                  |
| sympy_expand                     | 247 ms                                                 | 244 ms: 1.01x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 368 ms: 1.01x faster                                                   |
| crypto_pyaes                     | 54.4 ms                                                | 53.8 ms: 1.01x faster                                                  |
| bench_thread_pool                | 508 us                                                 | 503 us: 1.01x faster                                                   |
| sqlite_synth                     | 1.56 us                                                | 1.54 us: 1.01x faster                                                  |
| sqlalchemy_imperative            | 6.68 ms                                                | 6.64 ms: 1.01x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 346 ms                                                 | 344 ms: 1.01x faster                                                   |
| sqlglot_parse                    | 859 us                                                 | 854 us: 1.01x faster                                                   |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.01x faster                                                   |
| sympy_str                        | 145 ms                                                 | 144 ms: 1.00x faster                                                   |
| sqlglot_normalize                | 188 ms                                                 | 187 ms: 1.00x faster                                                   |
| sqlalchemy_declarative           | 59.1 ms                                                | 58.9 ms: 1.00x faster                                                  |
| sqlglot_transpile                | 1.03 ms                                                | 1.03 ms: 1.01x slower                                                  |
| docutils                         | 1.44 sec                                               | 1.45 sec: 1.01x slower                                                 |
| dulwich_log                      | 28.6 ms                                                | 29.0 ms: 1.01x slower                                                  |
| nqueens                          | 61.8 ms                                                | 62.7 ms: 1.01x slower                                                  |
| hexiom                           | 4.83 ms                                                | 4.91 ms: 1.02x slower                                                  |
| raytrace                         | 181 ms                                                 | 184 ms: 1.02x slower                                                   |
| async_generators                 | 292 ms                                                 | 300 ms: 1.03x slower                                                   |
| chaos                            | 41.3 ms                                                | 42.4 ms: 1.03x slower                                                  |
| sympy_integrate                  | 11.3 ms                                                | 11.8 ms: 1.04x slower                                                  |
| genshi_text                      | 16.9 ms                                                | 17.6 ms: 1.04x slower                                                  |
| python_startup                   | 20.6 ms                                                | 21.6 ms: 1.05x slower                                                  |
| gc_traversal                     | 2.93 ms                                                | 3.07 ms: 1.05x slower                                                  |
| python_startup_no_site           | 15.8 ms                                                | 16.6 ms: 1.05x slower                                                  |
| mdp                              | 1.50 sec                                               | 1.57 sec: 1.05x slower                                                 |
| create_gc_cycles                 | 1.20 ms                                                | 1.28 ms: 1.07x slower                                                  |
| logging_silent                   | 70.1 ns                                                | 75.7 ns: 1.08x slower                                                  |
| json_dumps                       | 6.51 ms                                                | 7.16 ms: 1.10x slower                                                  |
| django_template                  | 20.5 ms                                                | 23.2 ms: 1.13x slower                                                  |
| many_optionals                   | 324 us                                                 | 377 us: 1.16x slower                                                   |
| comprehensions                   | 12.0 us                                                | 14.0 us: 1.16x slower                                                  |
| genshi_xml                       | 34.1 ms                                                | 41.6 ms: 1.22x slower                                                  |
| subparsers                       | 9.50 ms                                                | 12.2 ms: 1.29x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.07x faster                                                           |

Benchmark hidden because not significant (3): sphinx, pidigits, sympy_sum
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20241213-3.14.0a2+-2de048c-JIT/bm-20241213-darwin-arm64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c.json: mypy2

- Geometric mean (including insignificant results): 1.073x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.05x