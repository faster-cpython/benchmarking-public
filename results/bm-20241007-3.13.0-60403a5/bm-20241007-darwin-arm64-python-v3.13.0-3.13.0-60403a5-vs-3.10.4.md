# Results vs. 3.10.4

- fork: python
- ref: v3.13.0
- machine: darwin-arm64
- commit hash: 60403a5
- commit date: 2024-10-07
- overall geometric mean: 1.258x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 179 ms: 1.13x faster                                   |
| chameleon      | 5.98 ms                                                | 4.95 ms: 1.21x faster                                  |
| docutils       | 1.74 sec                                               | 1.44 sec: 1.20x faster                                 |
| html5lib       | 43.5 ms                                                | 36.7 ms: 1.19x faster                                  |
| sphinx         | 729 ms                                                 | 602 ms: 1.21x faster                                   |
| tornado_http   | 137 ms                                                 | 92.0 ms: 1.49x faster                                  |
| Geometric mean | (ref)                                                  | 1.23x faster                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|-------------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 69.9 ms: 5.60x faster                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 168 ms: 2.87x faster                                   |
| async_tree_io                 | 1.02 sec                                               | 508 ms: 2.00x faster                                   |
| async_tree_eager_io           | 1.01 sec                                               | 511 ms: 1.99x faster                                   |
| async_tree_none               | 391 ms                                                 | 212 ms: 1.85x faster                                   |
| async_tree_memoization        | 481 ms                                                 | 268 ms: 1.80x faster                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 373 ms: 1.80x faster                                   |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 459 ms: 1.46x faster                                   |
| coroutines                    | 20.5 ms                                                | 20.0 ms: 1.02x faster                                  |
| async_generators              | 233 ms                                                 | 294 ms: 1.26x slower                                   |
| Geometric mean                | (ref)                                                  | 1.74x faster                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 72.4 ms                                                | 55.8 ms: 1.30x faster                                  |
| nbody          | 92.5 ms                                                | 73.6 ms: 1.26x faster                                  |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                   |
| Geometric mean | (ref)                                                  | 1.17x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 78.3 ms: 1.22x faster                                  |
| regex_dna      | 175 ms                                                 | 149 ms: 1.17x faster                                   |
| regex_v8       | 19.1 ms                                                | 17.0 ms: 1.12x faster                                  |
| regex_effbot   | 2.34 ms                                                | 2.63 ms: 1.13x slower                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 285 us                                                 | 215 us: 1.33x faster                                   |
| json_dumps           | 8.31 ms                                                | 6.47 ms: 1.28x faster                                  |
| unpickle_pure_python | 198 us                                                 | 165 us: 1.20x faster                                   |
| tomli_loads          | 1.72 sec                                               | 1.57 sec: 1.10x faster                                 |
| xml_etree_process    | 44.6 ms                                                | 41.3 ms: 1.08x faster                                  |
| xml_etree_parse      | 109 ms                                                 | 108 ms: 1.01x faster                                   |
| json_loads           | 16.6 us                                                | 17.0 us: 1.03x slower                                  |
| xml_etree_generate   | 53.9 ms                                                | 57.1 ms: 1.06x slower                                  |
| Geometric mean       | (ref)                                                  | 1.09x faster                                           |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 18.8 ms: 1.05x faster                                  |
| python_startup_no_site | 12.8 ms                                                | 13.7 ms: 1.07x slower                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 9.81 ms                                                | 7.75 ms: 1.27x faster                                  |
| django_template | 24.4 ms                                                | 20.5 ms: 1.19x faster                                  |
| genshi_text     | 17.7 ms                                                | 16.9 ms: 1.05x faster                                  |
| genshi_xml      | 35.1 ms                                                | 34.1 ms: 1.03x faster                                  |
| Geometric mean  | (ref)                                                  | 1.13x faster                                           |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|-------------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 69.9 ms: 5.60x faster                                  |
| subparsers                    | 39.8 ms                                                | 9.44 ms: 4.22x faster                                  |
| typing_runtime_protocols      | 326 us                                                 | 101 us: 3.24x faster                                   |
| async_tree_eager_memoization  | 483 ms                                                 | 168 ms: 2.87x faster                                   |
| async_tree_io                 | 1.02 sec                                               | 508 ms: 2.00x faster                                   |
| async_tree_eager_io           | 1.01 sec                                               | 511 ms: 1.99x faster                                   |
| deltablue                     | 4.99 ms                                                | 2.65 ms: 1.88x faster                                  |
| async_tree_none               | 391 ms                                                 | 212 ms: 1.85x faster                                   |
| raytrace                      | 327 ms                                                 | 181 ms: 1.80x faster                                   |
| async_tree_memoization        | 481 ms                                                 | 268 ms: 1.80x faster                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 373 ms: 1.80x faster                                   |
| logging_silent                | 117 ns                                                 | 71.0 ns: 1.65x faster                                  |
| chaos                         | 67.7 ms                                                | 41.1 ms: 1.65x faster                                  |
| sqlglot_parse                 | 1.35 ms                                                | 852 us: 1.58x faster                                   |
| richards_super                | 61.0 ms                                                | 39.2 ms: 1.55x faster                                  |
| sqlglot_transpile             | 1.56 ms                                                | 1.04 ms: 1.50x faster                                  |
| tornado_http                  | 137 ms                                                 | 92.0 ms: 1.49x faster                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 459 ms: 1.46x faster                                   |
| comprehensions                | 17.3 us                                                | 12.0 us: 1.45x faster                                  |
| richards                      | 52.3 ms                                                | 36.2 ms: 1.45x faster                                  |
| scimark_monte_carlo           | 72.4 ms                                                | 50.4 ms: 1.44x faster                                  |
| go                            | 163 ms                                                 | 117 ms: 1.40x faster                                   |
| sqlalchemy_imperative         | 9.07 ms                                                | 6.69 ms: 1.35x faster                                  |
| scimark_lu                    | 103 ms                                                 | 75.9 ms: 1.35x faster                                  |
| crypto_pyaes                  | 73.3 ms                                                | 55.3 ms: 1.33x faster                                  |
| pickle_pure_python            | 285 us                                                 | 215 us: 1.33x faster                                   |
| scimark_sor                   | 140 ms                                                 | 106 ms: 1.32x faster                                   |
| logging_format                | 5.03 us                                                | 3.85 us: 1.31x faster                                  |
| float                         | 72.4 ms                                                | 55.8 ms: 1.30x faster                                  |
| logging_simple                | 4.59 us                                                | 3.56 us: 1.29x faster                                  |
| pylint                        | 231 ms                                                 | 180 ms: 1.28x faster                                   |
| json_dumps                    | 8.31 ms                                                | 6.47 ms: 1.28x faster                                  |
| hexiom                        | 6.25 ms                                                | 4.87 ms: 1.28x faster                                  |
| sqlalchemy_declarative        | 75.7 ms                                                | 59.0 ms: 1.28x faster                                  |
| pyflate                       | 448 ms                                                 | 352 ms: 1.27x faster                                   |
| deepcopy_memo                 | 34.7 us                                                | 27.4 us: 1.27x faster                                  |
| pycparser                     | 887 ms                                                 | 701 ms: 1.27x faster                                   |
| mako                          | 9.81 ms                                                | 7.75 ms: 1.27x faster                                  |
| nbody                         | 92.5 ms                                                | 73.6 ms: 1.26x faster                                  |
| k_core                        | 2.01 sec                                               | 1.61 sec: 1.25x faster                                 |
| spectral_norm                 | 95.3 ms                                                | 76.5 ms: 1.25x faster                                  |
| dulwich_log                   | 35.6 ms                                                | 28.7 ms: 1.24x faster                                  |
| sympy_sum                     | 92.7 ms                                                | 75.1 ms: 1.23x faster                                  |
| regex_compile                 | 95.6 ms                                                | 78.3 ms: 1.22x faster                                  |
| sphinx                        | 729 ms                                                 | 602 ms: 1.21x faster                                   |
| chameleon                     | 5.98 ms                                                | 4.95 ms: 1.21x faster                                  |
| pprint_pformat                | 1.33 sec                                               | 1.10 sec: 1.21x faster                                 |
| thrift                        | 562 us                                                 | 466 us: 1.21x faster                                   |
| docutils                      | 1.74 sec                                               | 1.44 sec: 1.20x faster                                 |
| unpickle_pure_python          | 198 us                                                 | 165 us: 1.20x faster                                   |
| pprint_safe_repr              | 648 ms                                                 | 541 ms: 1.20x faster                                   |
| django_template               | 24.4 ms                                                | 20.5 ms: 1.19x faster                                  |
| many_optionals                | 486 us                                                 | 409 us: 1.19x faster                                   |
| html5lib                      | 43.5 ms                                                | 36.7 ms: 1.19x faster                                  |
| djangocms                     | 8.31 us                                                | 7.05 us: 1.18x faster                                  |
| regex_dna                     | 175 ms                                                 | 149 ms: 1.17x faster                                   |
| deepcopy                      | 276 us                                                 | 236 us: 1.17x faster                                   |
| sympy_integrate               | 13.2 ms                                                | 11.3 ms: 1.16x faster                                  |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 2.98 ms: 1.15x faster                                  |
| sympy_str                     | 166 ms                                                 | 146 ms: 1.14x faster                                   |
| scimark_fft                   | 225 ms                                                 | 200 ms: 1.13x faster                                   |
| 2to3                          | 201 ms                                                 | 179 ms: 1.13x faster                                   |
| regex_v8                      | 19.1 ms                                                | 17.0 ms: 1.12x faster                                  |
| pathlib                       | 25.7 ms                                                | 23.2 ms: 1.11x faster                                  |
| deepcopy_reduce               | 2.32 us                                                | 2.09 us: 1.11x faster                                  |
| mdp                           | 1.65 sec                                               | 1.50 sec: 1.10x faster                                 |
| tomli_loads                   | 1.72 sec                                               | 1.57 sec: 1.10x faster                                 |
| sympy_expand                  | 269 ms                                                 | 248 ms: 1.09x faster                                   |
| fannkuch                      | 303 ms                                                 | 279 ms: 1.09x faster                                   |
| bench_thread_pool             | 545 us                                                 | 503 us: 1.08x faster                                   |
| xml_etree_process             | 44.6 ms                                                | 41.3 ms: 1.08x faster                                  |
| sqlglot_optimize              | 37.2 ms                                                | 34.7 ms: 1.07x faster                                  |
| bpe_tokeniser                 | 3.44 sec                                               | 3.26 sec: 1.05x faster                                 |
| meteor_contest                | 77.8 ms                                                | 74.0 ms: 1.05x faster                                  |
| genshi_text                   | 17.7 ms                                                | 16.9 ms: 1.05x faster                                  |
| python_startup                | 19.6 ms                                                | 18.8 ms: 1.05x faster                                  |
| nqueens                       | 63.8 ms                                                | 61.8 ms: 1.03x faster                                  |
| genshi_xml                    | 35.1 ms                                                | 34.1 ms: 1.03x faster                                  |
| coroutines                    | 20.5 ms                                                | 20.0 ms: 1.02x faster                                  |
| dask                          | 789 ms                                                 | 771 ms: 1.02x faster                                   |
| sqlglot_normalize             | 192 ms                                                 | 188 ms: 1.02x faster                                   |
| json                          | 3.10 ms                                                | 3.04 ms: 1.02x faster                                  |
| xml_etree_parse               | 109 ms                                                 | 108 ms: 1.01x faster                                   |
| generators                    | 31.7 ms                                                | 31.9 ms: 1.01x slower                                  |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                   |
| create_gc_cycles              | 1.16 ms                                                | 1.19 ms: 1.02x slower                                  |
| json_loads                    | 16.6 us                                                | 17.0 us: 1.03x slower                                  |
| sqlite_synth                  | 1.48 us                                                | 1.55 us: 1.05x slower                                  |
| shortest_path                 | 328 ms                                                 | 345 ms: 1.05x slower                                   |
| xml_etree_generate            | 53.9 ms                                                | 57.1 ms: 1.06x slower                                  |
| python_startup_no_site        | 12.8 ms                                                | 13.7 ms: 1.07x slower                                  |
| gc_traversal                  | 2.71 ms                                                | 2.94 ms: 1.08x slower                                  |
| gevent_hub                    | 0.61 ns                                                | 0.68 ns: 1.11x slower                                  |
| coverage                      | 41.2 ms                                                | 46.2 ms: 1.12x slower                                  |
| regex_effbot                  | 2.34 ms                                                | 2.63 ms: 1.13x slower                                  |
| bench_mp_pool                 | 56.0 ms                                                | 64.7 ms: 1.16x slower                                  |
| async_generators              | 233 ms                                                 | 294 ms: 1.26x slower                                   |
| telco                         | 3.49 ms                                                | 4.84 ms: 1.39x slower                                  |
| Geometric mean                | (ref)                                                  | 1.25x faster                                           |

Benchmark hidden because not significant (3): xml_etree_iterparse, connected_components, asyncio_websockets
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, gunicorn

- Geometric mean (including insignificant results): 1.258x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: 1.11x