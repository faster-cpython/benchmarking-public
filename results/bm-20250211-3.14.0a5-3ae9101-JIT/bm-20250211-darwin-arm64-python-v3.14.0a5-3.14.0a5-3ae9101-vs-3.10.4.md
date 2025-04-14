# Results vs. 3.10.4

- fork: python
- ref: v3.14.0a5
- machine: darwin-arm64
- commit hash: 3ae9101
- commit date: 2025-02-11
- overall geometric mean: 1.302x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250211-darwin-arm64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 176 ms: 1.15x faster                                       |
| docutils       | 1.74 sec                                               | 1.51 sec: 1.15x faster                                     |
| html5lib       | 43.5 ms                                                | 33.1 ms: 1.32x faster                                      |
| sphinx         | 729 ms                                                 | 598 ms: 1.22x faster                                       |
| Geometric mean | (ref)                                                  | 1.21x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250211-darwin-arm64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 69.9 ms: 5.61x faster                                      |
| async_tree_eager_memoization  | 483 ms                                                 | 151 ms: 3.20x faster                                       |
| async_tree_eager_io           | 1.01 sec                                               | 394 ms: 2.58x faster                                       |
| async_tree_io                 | 1.02 sec                                               | 407 ms: 2.50x faster                                       |
| async_tree_memoization        | 481 ms                                                 | 211 ms: 2.28x faster                                       |
| async_tree_none               | 391 ms                                                 | 173 ms: 2.26x faster                                       |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 369 ms: 1.82x faster                                       |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 426 ms: 1.57x faster                                       |
| coroutines                    | 20.5 ms                                                | 17.9 ms: 1.15x faster                                      |
| async_generators              | 233 ms                                                 | 283 ms: 1.21x slower                                       |
| Geometric mean                | (ref)                                                  | 1.96x faster                                               |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250211-darwin-arm64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 92.5 ms                                                | 65.0 ms: 1.42x faster                                      |
| float          | 72.4 ms                                                | 52.6 ms: 1.38x faster                                      |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                       |
| Geometric mean | (ref)                                                  | 1.25x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250211-darwin-arm64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 73.5 ms: 1.30x faster                                      |
| regex_dna      | 175 ms                                                 | 140 ms: 1.25x faster                                       |
| regex_v8       | 19.1 ms                                                | 16.9 ms: 1.13x faster                                      |
| regex_effbot   | 2.34 ms                                                | 2.24 ms: 1.04x faster                                      |
| Geometric mean | (ref)                                                  | 1.18x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250211-darwin-arm64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 134 us: 1.48x faster                                       |
| pickle_pure_python   | 285 us                                                 | 210 us: 1.36x faster                                       |
| tomli_loads          | 1.72 sec                                               | 1.29 sec: 1.34x faster                                     |
| xml_etree_process    | 44.6 ms                                                | 36.7 ms: 1.22x faster                                      |
| json_dumps           | 8.31 ms                                                | 7.53 ms: 1.10x faster                                      |
| xml_etree_parse      | 109 ms                                                 | 101 ms: 1.08x faster                                       |
| xml_etree_generate   | 53.9 ms                                                | 50.6 ms: 1.06x faster                                      |
| xml_etree_iterparse  | 74.5 ms                                                | 70.7 ms: 1.05x faster                                      |
| json_loads           | 16.6 us                                                | 17.9 us: 1.08x slower                                      |
| Geometric mean       | (ref)                                                  | 1.17x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250211-darwin-arm64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup | 19.6 ms                                                | 17.5 ms: 1.12x faster                                      |
| Geometric mean | (ref)                                                  | 1.06x faster                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250211-darwin-arm64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 9.81 ms                                                | 6.49 ms: 1.51x faster                                      |
| genshi_text     | 17.7 ms                                                | 15.8 ms: 1.12x faster                                      |
| genshi_xml      | 35.1 ms                                                | 33.3 ms: 1.05x faster                                      |
| django_template | 24.4 ms                                                | 23.9 ms: 1.02x faster                                      |
| Geometric mean  | (ref)                                                  | 1.16x faster                                               |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250211-darwin-arm64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 69.9 ms: 5.61x faster                                      |
| typing_runtime_protocols      | 326 us                                                 | 102 us: 3.21x faster                                       |
| async_tree_eager_memoization  | 483 ms                                                 | 151 ms: 3.20x faster                                       |
| subparsers                    | 39.8 ms                                                | 12.5 ms: 3.19x faster                                      |
| async_tree_eager_io           | 1.01 sec                                               | 394 ms: 2.58x faster                                       |
| async_tree_io                 | 1.02 sec                                               | 407 ms: 2.50x faster                                       |
| async_tree_memoization        | 481 ms                                                 | 211 ms: 2.28x faster                                       |
| async_tree_none               | 391 ms                                                 | 173 ms: 2.26x faster                                       |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 369 ms: 1.82x faster                                       |
| deltablue                     | 4.99 ms                                                | 2.77 ms: 1.80x faster                                      |
| go                            | 163 ms                                                 | 94.2 ms: 1.73x faster                                      |
| raytrace                      | 327 ms                                                 | 199 ms: 1.65x faster                                       |
| deepcopy                      | 276 us                                                 | 168 us: 1.64x faster                                       |
| deepcopy_memo                 | 34.7 us                                                | 21.2 us: 1.64x faster                                      |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 426 ms: 1.57x faster                                       |
| logging_silent                | 117 ns                                                 | 75.6 ns: 1.55x faster                                      |
| chaos                         | 67.7 ms                                                | 43.8 ms: 1.54x faster                                      |
| sqlglot_parse                 | 1.35 ms                                                | 887 us: 1.52x faster                                       |
| scimark_sor                   | 140 ms                                                 | 92.3 ms: 1.52x faster                                      |
| mako                          | 9.81 ms                                                | 6.49 ms: 1.51x faster                                      |
| unpickle_pure_python          | 198 us                                                 | 134 us: 1.48x faster                                       |
| pyflate                       | 448 ms                                                 | 303 ms: 1.48x faster                                       |
| scimark_monte_carlo           | 72.4 ms                                                | 49.4 ms: 1.47x faster                                      |
| sqlglot_transpile             | 1.56 ms                                                | 1.06 ms: 1.46x faster                                      |
| richards_super                | 61.0 ms                                                | 41.7 ms: 1.46x faster                                      |
| spectral_norm                 | 95.3 ms                                                | 66.9 ms: 1.42x faster                                      |
| nbody                         | 92.5 ms                                                | 65.0 ms: 1.42x faster                                      |
| richards                      | 52.3 ms                                                | 37.7 ms: 1.39x faster                                      |
| float                         | 72.4 ms                                                | 52.6 ms: 1.38x faster                                      |
| crypto_pyaes                  | 73.3 ms                                                | 53.9 ms: 1.36x faster                                      |
| pylint                        | 231 ms                                                 | 170 ms: 1.36x faster                                       |
| pickle_pure_python            | 285 us                                                 | 210 us: 1.36x faster                                       |
| tomli_loads                   | 1.72 sec                                               | 1.29 sec: 1.34x faster                                     |
| comprehensions                | 17.3 us                                                | 13.0 us: 1.33x faster                                      |
| html5lib                      | 43.5 ms                                                | 33.1 ms: 1.32x faster                                      |
| deepcopy_reduce               | 2.32 us                                                | 1.77 us: 1.31x faster                                      |
| scimark_fft                   | 225 ms                                                 | 172 ms: 1.31x faster                                       |
| k_core                        | 2.01 sec                                               | 1.53 sec: 1.31x faster                                     |
| regex_compile                 | 95.6 ms                                                | 73.5 ms: 1.30x faster                                      |
| logging_format                | 5.03 us                                                | 3.91 us: 1.29x faster                                      |
| sqlalchemy_imperative         | 9.07 ms                                                | 7.10 ms: 1.28x faster                                      |
| logging_simple                | 4.59 us                                                | 3.60 us: 1.27x faster                                      |
| pprint_pformat                | 1.33 sec                                               | 1.06 sec: 1.26x faster                                     |
| hexiom                        | 6.25 ms                                                | 4.97 ms: 1.26x faster                                      |
| pprint_safe_repr              | 648 ms                                                 | 519 ms: 1.25x faster                                       |
| regex_dna                     | 175 ms                                                 | 140 ms: 1.25x faster                                       |
| pycparser                     | 887 ms                                                 | 713 ms: 1.24x faster                                       |
| scimark_lu                    | 103 ms                                                 | 83.0 ms: 1.24x faster                                      |
| sqlalchemy_declarative        | 75.7 ms                                                | 61.7 ms: 1.23x faster                                      |
| sphinx                        | 729 ms                                                 | 598 ms: 1.22x faster                                       |
| thrift                        | 562 us                                                 | 461 us: 1.22x faster                                       |
| xml_etree_process             | 44.6 ms                                                | 36.7 ms: 1.22x faster                                      |
| dulwich_log                   | 35.6 ms                                                | 29.6 ms: 1.20x faster                                      |
| bpe_tokeniser                 | 3.44 sec                                               | 2.88 sec: 1.19x faster                                     |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 2.87 ms: 1.19x faster                                      |
| sympy_sum                     | 92.7 ms                                                | 78.4 ms: 1.18x faster                                      |
| docutils                      | 1.74 sec                                               | 1.51 sec: 1.15x faster                                     |
| coroutines                    | 20.5 ms                                                | 17.9 ms: 1.15x faster                                      |
| 2to3                          | 201 ms                                                 | 176 ms: 1.15x faster                                       |
| regex_v8                      | 19.1 ms                                                | 16.9 ms: 1.13x faster                                      |
| python_startup                | 19.6 ms                                                | 17.5 ms: 1.12x faster                                      |
| genshi_text                   | 17.7 ms                                                | 15.8 ms: 1.12x faster                                      |
| fannkuch                      | 303 ms                                                 | 272 ms: 1.11x faster                                       |
| generators                    | 31.7 ms                                                | 28.5 ms: 1.11x faster                                      |
| pathlib                       | 25.7 ms                                                | 23.3 ms: 1.11x faster                                      |
| json_dumps                    | 8.31 ms                                                | 7.53 ms: 1.10x faster                                      |
| sympy_str                     | 166 ms                                                 | 151 ms: 1.10x faster                                       |
| sympy_integrate               | 13.2 ms                                                | 12.1 ms: 1.08x faster                                      |
| xml_etree_parse               | 109 ms                                                 | 101 ms: 1.08x faster                                       |
| connected_components          | 318 ms                                                 | 299 ms: 1.07x faster                                       |
| xml_etree_generate            | 53.9 ms                                                | 50.6 ms: 1.06x faster                                      |
| genshi_xml                    | 35.1 ms                                                | 33.3 ms: 1.05x faster                                      |
| bench_thread_pool             | 545 us                                                 | 518 us: 1.05x faster                                       |
| xml_etree_iterparse           | 74.5 ms                                                | 70.7 ms: 1.05x faster                                      |
| sympy_expand                  | 269 ms                                                 | 256 ms: 1.05x faster                                       |
| mdp                           | 1.65 sec                                               | 1.58 sec: 1.05x faster                                     |
| sqlglot_optimize              | 37.2 ms                                                | 35.6 ms: 1.05x faster                                      |
| regex_effbot                  | 2.34 ms                                                | 2.24 ms: 1.04x faster                                      |
| meteor_contest                | 77.8 ms                                                | 75.0 ms: 1.04x faster                                      |
| many_optionals                | 486 us                                                 | 470 us: 1.03x faster                                       |
| json                          | 3.10 ms                                                | 3.01 ms: 1.03x faster                                      |
| dask                          | 789 ms                                                 | 768 ms: 1.03x faster                                       |
| django_template               | 24.4 ms                                                | 23.9 ms: 1.02x faster                                      |
| nqueens                       | 63.8 ms                                                | 64.0 ms: 1.00x slower                                      |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                       |
| sqlglot_normalize             | 192 ms                                                 | 196 ms: 1.02x slower                                       |
| sqlite_synth                  | 1.48 us                                                | 1.55 us: 1.05x slower                                      |
| bench_mp_pool                 | 56.0 ms                                                | 60.3 ms: 1.08x slower                                      |
| json_loads                    | 16.6 us                                                | 17.9 us: 1.08x slower                                      |
| create_gc_cycles              | 1.16 ms                                                | 1.28 ms: 1.10x slower                                      |
| gc_traversal                  | 2.71 ms                                                | 3.11 ms: 1.15x slower                                      |
| coverage                      | 41.2 ms                                                | 47.5 ms: 1.15x slower                                      |
| async_generators              | 233 ms                                                 | 283 ms: 1.21x slower                                       |
| telco                         | 3.49 ms                                                | 4.49 ms: 1.29x slower                                      |
| Geometric mean                | (ref)                                                  | 1.30x faster                                               |

Benchmark hidden because not significant (3): python_startup_no_site, asyncio_websockets, shortest_path
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, tornado_http
Ignored benchmarks (8) of results/bm-20250211-3.14.0a5-3ae9101-JIT/bm-20250211-darwin-arm64-python-v3.14.0a5-3.14.0a5-3ae9101.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.302x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: 1.15x