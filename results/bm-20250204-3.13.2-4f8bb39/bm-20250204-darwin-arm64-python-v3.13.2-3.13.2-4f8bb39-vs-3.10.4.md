# Results vs. 3.10.4

- fork: python
- ref: v3.13.2
- machine: darwin-arm64
- commit hash: 4f8bb39
- commit date: 2025-02-04
- overall geometric mean: 1.260x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-darwin-arm64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 180 ms: 1.12x faster                                   |
| chameleon      | 5.98 ms                                                | 4.95 ms: 1.21x faster                                  |
| docutils       | 1.74 sec                                               | 1.44 sec: 1.21x faster                                 |
| html5lib       | 43.5 ms                                                | 36.2 ms: 1.20x faster                                  |
| sphinx         | 729 ms                                                 | 599 ms: 1.22x faster                                   |
| tornado_http   | 137 ms                                                 | 76.1 ms: 1.80x faster                                  |
| Geometric mean | (ref)                                                  | 1.28x faster                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-darwin-arm64-python-v3.13.2-3.13.2-4f8bb39 |
|-------------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 70.6 ms: 5.55x faster                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 170 ms: 2.85x faster                                   |
| async_tree_io                 | 1.02 sec                                               | 511 ms: 1.99x faster                                   |
| async_tree_eager_io           | 1.01 sec                                               | 515 ms: 1.97x faster                                   |
| async_tree_none               | 391 ms                                                 | 213 ms: 1.83x faster                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 374 ms: 1.79x faster                                   |
| async_tree_memoization        | 481 ms                                                 | 272 ms: 1.77x faster                                   |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 462 ms: 1.45x faster                                   |
| coroutines                    | 20.5 ms                                                | 19.8 ms: 1.04x faster                                  |
| async_generators              | 233 ms                                                 | 262 ms: 1.12x slower                                   |
| Geometric mean                | (ref)                                                  | 1.75x faster                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-darwin-arm64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 72.4 ms                                                | 55.9 ms: 1.30x faster                                  |
| nbody          | 92.5 ms                                                | 74.4 ms: 1.24x faster                                  |
| pidigits       | 280 ms                                                 | 283 ms: 1.01x slower                                   |
| Geometric mean | (ref)                                                  | 1.17x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-darwin-arm64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_dna      | 175 ms                                                 | 141 ms: 1.24x faster                                   |
| regex_compile  | 95.6 ms                                                | 78.9 ms: 1.21x faster                                  |
| regex_v8       | 19.1 ms                                                | 17.0 ms: 1.13x faster                                  |
| regex_effbot   | 2.34 ms                                                | 2.28 ms: 1.02x faster                                  |
| Geometric mean | (ref)                                                  | 1.15x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-darwin-arm64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 285 us                                                 | 216 us: 1.32x faster                                   |
| json_dumps           | 8.31 ms                                                | 6.50 ms: 1.28x faster                                  |
| unpickle_pure_python | 198 us                                                 | 164 us: 1.21x faster                                   |
| tomli_loads          | 1.72 sec                                               | 1.57 sec: 1.10x faster                                 |
| xml_etree_process    | 44.6 ms                                                | 41.5 ms: 1.08x faster                                  |
| xml_etree_parse      | 109 ms                                                 | 106 ms: 1.03x faster                                   |
| json_loads           | 16.6 us                                                | 17.0 us: 1.03x slower                                  |
| xml_etree_generate   | 53.9 ms                                                | 56.8 ms: 1.05x slower                                  |
| Geometric mean       | (ref)                                                  | 1.10x faster                                           |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-darwin-arm64-python-v3.13.2-3.13.2-4f8bb39 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 18.4 ms: 1.07x faster                                  |
| python_startup_no_site | 12.8 ms                                                | 13.4 ms: 1.05x slower                                  |
| Geometric mean         | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-darwin-arm64-python-v3.13.2-3.13.2-4f8bb39 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 9.81 ms                                                | 7.72 ms: 1.27x faster                                  |
| django_template | 24.4 ms                                                | 20.6 ms: 1.18x faster                                  |
| genshi_text     | 17.7 ms                                                | 16.9 ms: 1.05x faster                                  |
| genshi_xml      | 35.1 ms                                                | 34.1 ms: 1.03x faster                                  |
| Geometric mean  | (ref)                                                  | 1.13x faster                                           |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-darwin-arm64-python-v3.13.2-3.13.2-4f8bb39 |
|-------------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 70.6 ms: 5.55x faster                                  |
| subparsers                    | 39.8 ms                                                | 9.48 ms: 4.20x faster                                  |
| typing_runtime_protocols      | 326 us                                                 | 101 us: 3.22x faster                                   |
| async_tree_eager_memoization  | 483 ms                                                 | 170 ms: 2.85x faster                                   |
| async_tree_io                 | 1.02 sec                                               | 511 ms: 1.99x faster                                   |
| async_tree_eager_io           | 1.01 sec                                               | 515 ms: 1.97x faster                                   |
| deltablue                     | 4.99 ms                                                | 2.66 ms: 1.87x faster                                  |
| async_tree_none               | 391 ms                                                 | 213 ms: 1.83x faster                                   |
| tornado_http                  | 137 ms                                                 | 76.1 ms: 1.80x faster                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 374 ms: 1.79x faster                                   |
| async_tree_memoization        | 481 ms                                                 | 272 ms: 1.77x faster                                   |
| raytrace                      | 327 ms                                                 | 185 ms: 1.76x faster                                   |
| logging_silent                | 117 ns                                                 | 70.3 ns: 1.67x faster                                  |
| chaos                         | 67.7 ms                                                | 42.5 ms: 1.59x faster                                  |
| sqlglot_parse                 | 1.35 ms                                                | 851 us: 1.59x faster                                   |
| richards_super                | 61.0 ms                                                | 39.2 ms: 1.56x faster                                  |
| sqlglot_transpile             | 1.56 ms                                                | 1.03 ms: 1.52x faster                                  |
| richards                      | 52.3 ms                                                | 35.3 ms: 1.48x faster                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 462 ms: 1.45x faster                                   |
| scimark_monte_carlo           | 72.4 ms                                                | 50.8 ms: 1.42x faster                                  |
| go                            | 163 ms                                                 | 115 ms: 1.42x faster                                   |
| comprehensions                | 17.3 us                                                | 12.3 us: 1.41x faster                                  |
| sqlalchemy_imperative         | 9.07 ms                                                | 6.68 ms: 1.36x faster                                  |
| crypto_pyaes                  | 73.3 ms                                                | 54.4 ms: 1.35x faster                                  |
| scimark_lu                    | 103 ms                                                 | 76.7 ms: 1.34x faster                                  |
| pickle_pure_python            | 285 us                                                 | 216 us: 1.32x faster                                   |
| scimark_sor                   | 140 ms                                                 | 106 ms: 1.32x faster                                   |
| float                         | 72.4 ms                                                | 55.9 ms: 1.30x faster                                  |
| logging_format                | 5.03 us                                                | 3.91 us: 1.29x faster                                  |
| sqlalchemy_declarative        | 75.7 ms                                                | 58.9 ms: 1.29x faster                                  |
| hexiom                        | 6.25 ms                                                | 4.87 ms: 1.28x faster                                  |
| pylint                        | 231 ms                                                 | 181 ms: 1.28x faster                                   |
| json_dumps                    | 8.31 ms                                                | 6.50 ms: 1.28x faster                                  |
| pyflate                       | 448 ms                                                 | 352 ms: 1.27x faster                                   |
| mako                          | 9.81 ms                                                | 7.72 ms: 1.27x faster                                  |
| pycparser                     | 887 ms                                                 | 698 ms: 1.27x faster                                   |
| logging_simple                | 4.59 us                                                | 3.62 us: 1.27x faster                                  |
| deepcopy_memo                 | 34.7 us                                                | 27.4 us: 1.27x faster                                  |
| k_core                        | 2.01 sec                                               | 1.62 sec: 1.24x faster                                 |
| nbody                         | 92.5 ms                                                | 74.4 ms: 1.24x faster                                  |
| regex_dna                     | 175 ms                                                 | 141 ms: 1.24x faster                                   |
| spectral_norm                 | 95.3 ms                                                | 76.8 ms: 1.24x faster                                  |
| dulwich_log                   | 35.6 ms                                                | 29.0 ms: 1.23x faster                                  |
| pprint_pformat                | 1.33 sec                                               | 1.08 sec: 1.23x faster                                 |
| sympy_sum                     | 92.7 ms                                                | 75.8 ms: 1.22x faster                                  |
| sphinx                        | 729 ms                                                 | 599 ms: 1.22x faster                                   |
| pprint_safe_repr              | 648 ms                                                 | 535 ms: 1.21x faster                                   |
| regex_compile                 | 95.6 ms                                                | 78.9 ms: 1.21x faster                                  |
| docutils                      | 1.74 sec                                               | 1.44 sec: 1.21x faster                                 |
| djangocms                     | 8.31 us                                                | 6.87 us: 1.21x faster                                  |
| thrift                        | 562 us                                                 | 465 us: 1.21x faster                                   |
| chameleon                     | 5.98 ms                                                | 4.95 ms: 1.21x faster                                  |
| unpickle_pure_python          | 198 us                                                 | 164 us: 1.21x faster                                   |
| html5lib                      | 43.5 ms                                                | 36.2 ms: 1.20x faster                                  |
| django_template               | 24.4 ms                                                | 20.6 ms: 1.18x faster                                  |
| many_optionals                | 486 us                                                 | 412 us: 1.18x faster                                   |
| deepcopy                      | 276 us                                                 | 235 us: 1.17x faster                                   |
| sympy_integrate               | 13.2 ms                                                | 11.3 ms: 1.16x faster                                  |
| sympy_str                     | 166 ms                                                 | 146 ms: 1.14x faster                                   |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.02 ms: 1.13x faster                                  |
| regex_v8                      | 19.1 ms                                                | 17.0 ms: 1.13x faster                                  |
| deepcopy_reduce               | 2.32 us                                                | 2.07 us: 1.12x faster                                  |
| 2to3                          | 201 ms                                                 | 180 ms: 1.12x faster                                   |
| scimark_fft                   | 225 ms                                                 | 202 ms: 1.11x faster                                   |
| pathlib                       | 25.7 ms                                                | 23.4 ms: 1.10x faster                                  |
| tomli_loads                   | 1.72 sec                                               | 1.57 sec: 1.10x faster                                 |
| mdp                           | 1.65 sec                                               | 1.51 sec: 1.10x faster                                 |
| sympy_expand                  | 269 ms                                                 | 247 ms: 1.09x faster                                   |
| bench_thread_pool             | 545 us                                                 | 504 us: 1.08x faster                                   |
| fannkuch                      | 303 ms                                                 | 280 ms: 1.08x faster                                   |
| xml_etree_process             | 44.6 ms                                                | 41.5 ms: 1.08x faster                                  |
| python_startup                | 19.6 ms                                                | 18.4 ms: 1.07x faster                                  |
| sqlglot_optimize              | 37.2 ms                                                | 35.0 ms: 1.06x faster                                  |
| bpe_tokeniser                 | 3.44 sec                                               | 3.26 sec: 1.05x faster                                 |
| meteor_contest                | 77.8 ms                                                | 73.9 ms: 1.05x faster                                  |
| genshi_text                   | 17.7 ms                                                | 16.9 ms: 1.05x faster                                  |
| json                          | 3.10 ms                                                | 2.98 ms: 1.04x faster                                  |
| coroutines                    | 20.5 ms                                                | 19.8 ms: 1.04x faster                                  |
| nqueens                       | 63.8 ms                                                | 61.5 ms: 1.04x faster                                  |
| genshi_xml                    | 35.1 ms                                                | 34.1 ms: 1.03x faster                                  |
| xml_etree_parse               | 109 ms                                                 | 106 ms: 1.03x faster                                   |
| regex_effbot                  | 2.34 ms                                                | 2.28 ms: 1.02x faster                                  |
| dask                          | 789 ms                                                 | 772 ms: 1.02x faster                                   |
| sqlglot_normalize             | 192 ms                                                 | 191 ms: 1.01x faster                                   |
| generators                    | 31.7 ms                                                | 31.5 ms: 1.01x faster                                  |
| pidigits                      | 280 ms                                                 | 283 ms: 1.01x slower                                   |
| json_loads                    | 16.6 us                                                | 17.0 us: 1.03x slower                                  |
| create_gc_cycles              | 1.16 ms                                                | 1.20 ms: 1.03x slower                                  |
| sqlite_synth                  | 1.48 us                                                | 1.54 us: 1.04x slower                                  |
| python_startup_no_site        | 12.8 ms                                                | 13.4 ms: 1.05x slower                                  |
| xml_etree_generate            | 53.9 ms                                                | 56.8 ms: 1.05x slower                                  |
| shortest_path                 | 328 ms                                                 | 347 ms: 1.06x slower                                   |
| gc_traversal                  | 2.71 ms                                                | 2.93 ms: 1.08x slower                                  |
| bench_mp_pool                 | 56.0 ms                                                | 61.5 ms: 1.10x slower                                  |
| gevent_hub                    | 0.61 ns                                                | 0.68 ns: 1.11x slower                                  |
| coverage                      | 41.2 ms                                                | 46.2 ms: 1.12x slower                                  |
| async_generators              | 233 ms                                                 | 262 ms: 1.12x slower                                   |
| telco                         | 3.49 ms                                                | 4.81 ms: 1.38x slower                                  |
| Geometric mean                | (ref)                                                  | 1.26x faster                                           |

Benchmark hidden because not significant (3): xml_etree_iterparse, asyncio_websockets, connected_components
Ignored benchmarks (9) of results/bm-20250204-3.13.2-4f8bb39/bm-20250204-darwin-arm64-python-v3.13.2-3.13.2-4f8bb39.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, gunicorn

- Geometric mean (including insignificant results): 1.260x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: 1.11x