# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_hot
- machine: darwin-arm64
- commit hash: a987be7
- commit date: 2025-06-23
- overall geometric mean: 1.250x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 277 ms: 1.38x slower                                              |
| docutils       | 1.74 sec                                               | 1.59 sec: 1.09x faster                                            |
| html5lib       | 43.5 ms                                                | 34.0 ms: 1.28x faster                                             |
| sphinx         | 729 ms                                                 | 622 ms: 1.17x faster                                              |
| Geometric mean | (ref)                                                  | 1.04x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|-------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 71.8 ms: 5.46x faster                                             |
| async_tree_eager_memoization  | 483 ms                                                 | 150 ms: 3.22x faster                                              |
| async_tree_eager_io           | 1.01 sec                                               | 387 ms: 2.62x faster                                              |
| async_tree_io                 | 1.02 sec                                               | 405 ms: 2.51x faster                                              |
| async_tree_memoization        | 481 ms                                                 | 208 ms: 2.32x faster                                              |
| async_tree_none               | 391 ms                                                 | 178 ms: 2.20x faster                                              |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 368 ms: 1.82x faster                                              |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 427 ms: 1.57x faster                                              |
| coroutines                    | 20.5 ms                                                | 19.2 ms: 1.07x faster                                             |
| async_generators              | 233 ms                                                 | 288 ms: 1.23x slower                                              |
| Geometric mean                | (ref)                                                  | 1.94x faster                                                      |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 72.4 ms                                                | 57.8 ms: 1.25x faster                                             |
| nbody          | 92.5 ms                                                | 76.2 ms: 1.21x faster                                             |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                  | 1.15x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_dna      | 175 ms                                                 | 143 ms: 1.22x faster                                              |
| regex_compile  | 95.6 ms                                                | 79.5 ms: 1.20x faster                                             |
| regex_v8       | 19.1 ms                                                | 16.2 ms: 1.18x faster                                             |
| regex_effbot   | 2.34 ms                                                | 2.34 ms: 1.00x slower                                             |
| Geometric mean | (ref)                                                  | 1.15x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 137 us: 1.44x faster                                              |
| tomli_loads          | 1.72 sec                                               | 1.35 sec: 1.27x faster                                            |
| pickle_pure_python   | 285 us                                                 | 226 us: 1.26x faster                                              |
| json_dumps           | 8.31 ms                                                | 6.88 ms: 1.21x faster                                             |
| xml_etree_process    | 44.6 ms                                                | 37.4 ms: 1.19x faster                                             |
| xml_etree_parse      | 109 ms                                                 | 98.9 ms: 1.11x faster                                             |
| xml_etree_iterparse  | 74.5 ms                                                | 70.4 ms: 1.06x faster                                             |
| xml_etree_generate   | 53.9 ms                                                | 51.5 ms: 1.05x faster                                             |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                      |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 27.6 ms: 1.41x slower                                             |
| python_startup_no_site | 12.8 ms                                                | 18.1 ms: 1.42x slower                                             |
| Geometric mean         | (ref)                                                  | 1.41x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 6.93 ms: 1.41x faster                                             |
| genshi_text     | 17.7 ms                                                | 17.7 ms: 1.00x faster                                             |
| genshi_xml      | 35.1 ms                                                | 36.0 ms: 1.03x slower                                             |
| django_template | 24.4 ms                                                | 25.2 ms: 1.04x slower                                             |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                      |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|-------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 71.8 ms: 5.46x faster                                             |
| async_tree_eager_memoization  | 483 ms                                                 | 150 ms: 3.22x faster                                              |
| typing_runtime_protocols      | 326 us                                                 | 103 us: 3.16x faster                                              |
| subparsers                    | 39.8 ms                                                | 15.0 ms: 2.65x faster                                             |
| async_tree_eager_io           | 1.01 sec                                               | 387 ms: 2.62x faster                                              |
| async_tree_io                 | 1.02 sec                                               | 405 ms: 2.51x faster                                              |
| async_tree_memoization        | 481 ms                                                 | 208 ms: 2.32x faster                                              |
| async_tree_none               | 391 ms                                                 | 178 ms: 2.20x faster                                              |
| mdp                           | 1.65 sec                                               | 824 ms: 2.00x faster                                              |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 368 ms: 1.82x faster                                              |
| deltablue                     | 4.99 ms                                                | 2.91 ms: 1.71x faster                                             |
| go                            | 163 ms                                                 | 101 ms: 1.63x faster                                              |
| deepcopy                      | 276 us                                                 | 174 us: 1.58x faster                                              |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 427 ms: 1.57x faster                                              |
| deepcopy_memo                 | 34.7 us                                                | 22.4 us: 1.55x faster                                             |
| raytrace                      | 327 ms                                                 | 211 ms: 1.55x faster                                              |
| scimark_sor                   | 140 ms                                                 | 90.8 ms: 1.54x faster                                             |
| richards_super                | 61.0 ms                                                | 42.0 ms: 1.45x faster                                             |
| unpickle_pure_python          | 198 us                                                 | 137 us: 1.44x faster                                              |
| mako                          | 9.81 ms                                                | 6.93 ms: 1.41x faster                                             |
| chaos                         | 67.7 ms                                                | 48.1 ms: 1.41x faster                                             |
| pyflate                       | 448 ms                                                 | 321 ms: 1.39x faster                                              |
| richards                      | 52.3 ms                                                | 37.6 ms: 1.39x faster                                             |
| scimark_monte_carlo           | 72.4 ms                                                | 53.6 ms: 1.35x faster                                             |
| pylint                        | 231 ms                                                 | 171 ms: 1.35x faster                                              |
| comprehensions                | 17.3 us                                                | 13.0 us: 1.33x faster                                             |
| dulwich_log                   | 35.6 ms                                                | 26.8 ms: 1.33x faster                                             |
| k_core                        | 2.01 sec                                               | 1.52 sec: 1.32x faster                                            |
| pathlib                       | 25.7 ms                                                | 19.7 ms: 1.31x faster                                             |
| spectral_norm                 | 95.3 ms                                                | 74.5 ms: 1.28x faster                                             |
| html5lib                      | 43.5 ms                                                | 34.0 ms: 1.28x faster                                             |
| tomli_loads                   | 1.72 sec                                               | 1.35 sec: 1.27x faster                                            |
| crypto_pyaes                  | 73.3 ms                                                | 57.7 ms: 1.27x faster                                             |
| pickle_pure_python            | 285 us                                                 | 226 us: 1.26x faster                                              |
| float                         | 72.4 ms                                                | 57.8 ms: 1.25x faster                                             |
| hexiom                        | 6.25 ms                                                | 4.99 ms: 1.25x faster                                             |
| regex_dna                     | 175 ms                                                 | 143 ms: 1.22x faster                                              |
| deepcopy_reduce               | 2.32 us                                                | 1.90 us: 1.22x faster                                             |
| nbody                         | 92.5 ms                                                | 76.2 ms: 1.21x faster                                             |
| json_dumps                    | 8.31 ms                                                | 6.88 ms: 1.21x faster                                             |
| regex_compile                 | 95.6 ms                                                | 79.5 ms: 1.20x faster                                             |
| xml_etree_process             | 44.6 ms                                                | 37.4 ms: 1.19x faster                                             |
| thrift                        | 562 us                                                 | 472 us: 1.19x faster                                              |
| regex_v8                      | 19.1 ms                                                | 16.2 ms: 1.18x faster                                             |
| scimark_lu                    | 103 ms                                                 | 86.8 ms: 1.18x faster                                             |
| pycparser                     | 887 ms                                                 | 753 ms: 1.18x faster                                              |
| sphinx                        | 729 ms                                                 | 622 ms: 1.17x faster                                              |
| logging_format                | 5.03 us                                                | 4.38 us: 1.15x faster                                             |
| sympy_sum                     | 92.7 ms                                                | 80.8 ms: 1.15x faster                                             |
| sympy_integrate               | 13.2 ms                                                | 11.5 ms: 1.15x faster                                             |
| logging_simple                | 4.59 us                                                | 4.09 us: 1.12x faster                                             |
| pprint_pformat                | 1.33 sec                                               | 1.19 sec: 1.12x faster                                            |
| bpe_tokeniser                 | 3.44 sec                                               | 3.08 sec: 1.12x faster                                            |
| pprint_safe_repr              | 648 ms                                                 | 583 ms: 1.11x faster                                              |
| xml_etree_parse               | 109 ms                                                 | 98.9 ms: 1.11x faster                                             |
| docutils                      | 1.74 sec                                               | 1.59 sec: 1.09x faster                                            |
| scimark_fft                   | 225 ms                                                 | 209 ms: 1.08x faster                                              |
| sympy_str                     | 166 ms                                                 | 155 ms: 1.07x faster                                              |
| coroutines                    | 20.5 ms                                                | 19.2 ms: 1.07x faster                                             |
| json                          | 3.10 ms                                                | 2.92 ms: 1.06x faster                                             |
| xml_etree_iterparse           | 74.5 ms                                                | 70.4 ms: 1.06x faster                                             |
| xml_etree_generate            | 53.9 ms                                                | 51.5 ms: 1.05x faster                                             |
| connected_components          | 318 ms                                                 | 310 ms: 1.03x faster                                              |
| dask                          | 789 ms                                                 | 771 ms: 1.02x faster                                              |
| sympy_expand                  | 269 ms                                                 | 264 ms: 1.02x faster                                              |
| meteor_contest                | 77.8 ms                                                | 77.1 ms: 1.01x faster                                             |
| genshi_text                   | 17.7 ms                                                | 17.7 ms: 1.00x faster                                             |
| regex_effbot                  | 2.34 ms                                                | 2.34 ms: 1.00x slower                                             |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                              |
| genshi_xml                    | 35.1 ms                                                | 36.0 ms: 1.03x slower                                             |
| shortest_path                 | 328 ms                                                 | 338 ms: 1.03x slower                                              |
| django_template               | 24.4 ms                                                | 25.2 ms: 1.04x slower                                             |
| many_optionals                | 486 us                                                 | 507 us: 1.04x slower                                              |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.65 ms: 1.07x slower                                             |
| sqlite_synth                  | 1.48 us                                                | 1.60 us: 1.08x slower                                             |
| nqueens                       | 63.8 ms                                                | 69.5 ms: 1.09x slower                                             |
| create_gc_cycles              | 1.16 ms                                                | 1.36 ms: 1.17x slower                                             |
| gc_traversal                  | 2.71 ms                                                | 3.20 ms: 1.18x slower                                             |
| coverage                      | 41.2 ms                                                | 49.7 ms: 1.21x slower                                             |
| async_generators              | 233 ms                                                 | 288 ms: 1.23x slower                                              |
| telco                         | 3.49 ms                                                | 4.59 ms: 1.32x slower                                             |
| 2to3                          | 201 ms                                                 | 277 ms: 1.38x slower                                              |
| python_startup                | 19.6 ms                                                | 27.6 ms: 1.41x slower                                             |
| python_startup_no_site        | 12.8 ms                                                | 18.1 ms: 1.42x slower                                             |
| logging_silent                | 117 ns                                                 | 345 ns: 2.95x slower                                              |
| Geometric mean                | (ref)                                                  | 1.23x faster                                                      |

Benchmark hidden because not significant (4): json_loads, generators, asyncio_websockets, fannkuch
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250623-3.15.0a0-a987be7-JIT/bm-20250623-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-a987be7.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.250x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: 1.18x