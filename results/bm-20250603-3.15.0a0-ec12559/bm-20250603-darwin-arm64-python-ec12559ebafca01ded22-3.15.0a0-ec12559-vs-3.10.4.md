# Results vs. 3.10.4

- fork: python
- ref: ec12559ebafca01ded22
- machine: darwin-arm64
- commit hash: ec12559
- commit date: 2025-06-03
- overall geometric mean: 1.228x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250603-darwin-arm64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 211 ms: 1.05x slower                                                  |
| docutils       | 1.74 sec                                               | 1.48 sec: 1.17x faster                                                |
| html5lib       | 43.5 ms                                                | 31.7 ms: 1.37x faster                                                 |
| sphinx         | 729 ms                                                 | 588 ms: 1.24x faster                                                  |
| Geometric mean | (ref)                                                  | 1.18x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250603-darwin-arm64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 64.4 ms: 6.09x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 141 ms: 3.42x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 369 ms: 2.75x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 383 ms: 2.66x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 197 ms: 2.44x faster                                                  |
| async_tree_none               | 391 ms                                                 | 165 ms: 2.37x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 359 ms: 1.87x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 416 ms: 1.61x faster                                                  |
| coroutines                    | 20.5 ms                                                | 17.1 ms: 1.20x faster                                                 |
| async_generators              | 233 ms                                                 | 262 ms: 1.12x slower                                                  |
| Geometric mean                | (ref)                                                  | 2.06x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250603-darwin-arm64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 49.9 ms: 1.45x faster                                                 |
| nbody          | 92.5 ms                                                | 75.3 ms: 1.23x faster                                                 |
| pidigits       | 280 ms                                                 | 283 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.21x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250603-darwin-arm64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 72.0 ms: 1.33x faster                                                 |
| regex_dna      | 175 ms                                                 | 143 ms: 1.22x faster                                                  |
| regex_v8       | 19.1 ms                                                | 16.1 ms: 1.19x faster                                                 |
| regex_effbot   | 2.34 ms                                                | 2.34 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                  | 1.18x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250603-darwin-arm64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 285 us                                                 | 219 us: 1.30x faster                                                  |
| json_dumps           | 8.31 ms                                                | 6.55 ms: 1.27x faster                                                 |
| tomli_loads          | 1.72 sec                                               | 1.36 sec: 1.26x faster                                                |
| unpickle_pure_python | 198 us                                                 | 161 us: 1.23x faster                                                  |
| xml_etree_process    | 44.6 ms                                                | 39.0 ms: 1.14x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 103 ms: 1.07x faster                                                  |
| xml_etree_iterparse  | 74.5 ms                                                | 73.4 ms: 1.01x faster                                                 |
| json_loads           | 16.6 us                                                | 16.4 us: 1.01x faster                                                 |
| xml_etree_generate   | 53.9 ms                                                | 53.7 ms: 1.00x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250603-darwin-arm64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 20.3 ms: 1.03x slower                                                 |
| python_startup_no_site | 12.8 ms                                                | 15.8 ms: 1.23x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250603-darwin-arm64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 7.81 ms: 1.26x faster                                                 |
| genshi_text     | 17.7 ms                                                | 14.7 ms: 1.20x faster                                                 |
| genshi_xml      | 35.1 ms                                                | 31.3 ms: 1.12x faster                                                 |
| django_template | 24.4 ms                                                | 22.2 ms: 1.10x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.17x faster                                                          |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250603-darwin-arm64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 64.4 ms: 6.09x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 141 ms: 3.42x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 96.5 us: 3.38x faster                                                 |
| subparsers                    | 39.8 ms                                                | 13.7 ms: 2.91x faster                                                 |
| async_tree_eager_io           | 1.01 sec                                               | 369 ms: 2.75x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 383 ms: 2.66x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 197 ms: 2.44x faster                                                  |
| async_tree_none               | 391 ms                                                 | 165 ms: 2.37x faster                                                  |
| mdp                           | 1.65 sec                                               | 764 ms: 2.16x faster                                                  |
| deltablue                     | 4.99 ms                                                | 2.58 ms: 1.93x faster                                                 |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 359 ms: 1.87x faster                                                  |
| go                            | 163 ms                                                 | 87.6 ms: 1.87x faster                                                 |
| raytrace                      | 327 ms                                                 | 180 ms: 1.81x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 19.2 us: 1.81x faster                                                 |
| deepcopy                      | 276 us                                                 | 157 us: 1.76x faster                                                  |
| chaos                         | 67.7 ms                                                | 40.3 ms: 1.68x faster                                                 |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 416 ms: 1.61x faster                                                  |
| scimark_sor                   | 140 ms                                                 | 89.0 ms: 1.57x faster                                                 |
| scimark_monte_carlo           | 72.4 ms                                                | 46.7 ms: 1.55x faster                                                 |
| richards_super                | 61.0 ms                                                | 41.5 ms: 1.47x faster                                                 |
| float                         | 72.4 ms                                                | 49.9 ms: 1.45x faster                                                 |
| comprehensions                | 17.3 us                                                | 12.0 us: 1.44x faster                                                 |
| richards                      | 52.3 ms                                                | 36.7 ms: 1.43x faster                                                 |
| dulwich_log                   | 35.6 ms                                                | 25.0 ms: 1.42x faster                                                 |
| pylint                        | 231 ms                                                 | 164 ms: 1.41x faster                                                  |
| pyflate                       | 448 ms                                                 | 325 ms: 1.38x faster                                                  |
| deepcopy_reduce               | 2.32 us                                                | 1.69 us: 1.37x faster                                                 |
| html5lib                      | 43.5 ms                                                | 31.7 ms: 1.37x faster                                                 |
| spectral_norm                 | 95.3 ms                                                | 71.0 ms: 1.34x faster                                                 |
| hexiom                        | 6.25 ms                                                | 4.67 ms: 1.34x faster                                                 |
| regex_compile                 | 95.6 ms                                                | 72.0 ms: 1.33x faster                                                 |
| generators                    | 31.7 ms                                                | 24.1 ms: 1.31x faster                                                 |
| pickle_pure_python            | 285 us                                                 | 219 us: 1.30x faster                                                  |
| pycparser                     | 887 ms                                                 | 683 ms: 1.30x faster                                                  |
| k_core                        | 2.01 sec                                               | 1.55 sec: 1.30x faster                                                |
| crypto_pyaes                  | 73.3 ms                                                | 57.2 ms: 1.28x faster                                                 |
| json_dumps                    | 8.31 ms                                                | 6.55 ms: 1.27x faster                                                 |
| tomli_loads                   | 1.72 sec                                               | 1.36 sec: 1.26x faster                                                |
| mako                          | 9.81 ms                                                | 7.81 ms: 1.26x faster                                                 |
| logging_format                | 5.03 us                                                | 4.01 us: 1.25x faster                                                 |
| logging_simple                | 4.59 us                                                | 3.69 us: 1.25x faster                                                 |
| sphinx                        | 729 ms                                                 | 588 ms: 1.24x faster                                                  |
| unpickle_pure_python          | 198 us                                                 | 161 us: 1.23x faster                                                  |
| nbody                         | 92.5 ms                                                | 75.3 ms: 1.23x faster                                                 |
| scimark_lu                    | 103 ms                                                 | 83.6 ms: 1.23x faster                                                 |
| regex_dna                     | 175 ms                                                 | 143 ms: 1.22x faster                                                  |
| sympy_sum                     | 92.7 ms                                                | 75.9 ms: 1.22x faster                                                 |
| coroutines                    | 20.5 ms                                                | 17.1 ms: 1.20x faster                                                 |
| genshi_text                   | 17.7 ms                                                | 14.7 ms: 1.20x faster                                                 |
| sympy_integrate               | 13.2 ms                                                | 11.0 ms: 1.19x faster                                                 |
| regex_v8                      | 19.1 ms                                                | 16.1 ms: 1.19x faster                                                 |
| pprint_pformat                | 1.33 sec                                               | 1.12 sec: 1.18x faster                                                |
| docutils                      | 1.74 sec                                               | 1.48 sec: 1.17x faster                                                |
| pprint_safe_repr              | 648 ms                                                 | 555 ms: 1.17x faster                                                  |
| sympy_str                     | 166 ms                                                 | 143 ms: 1.16x faster                                                  |
| scimark_fft                   | 225 ms                                                 | 196 ms: 1.15x faster                                                  |
| xml_etree_process             | 44.6 ms                                                | 39.0 ms: 1.14x faster                                                 |
| fannkuch                      | 303 ms                                                 | 267 ms: 1.13x faster                                                  |
| genshi_xml                    | 35.1 ms                                                | 31.3 ms: 1.12x faster                                                 |
| sympy_expand                  | 269 ms                                                 | 242 ms: 1.11x faster                                                  |
| bpe_tokeniser                 | 3.44 sec                                               | 3.09 sec: 1.11x faster                                                |
| pathlib                       | 25.7 ms                                                | 23.3 ms: 1.11x faster                                                 |
| django_template               | 24.4 ms                                                | 22.2 ms: 1.10x faster                                                 |
| json                          | 3.10 ms                                                | 2.90 ms: 1.07x faster                                                 |
| xml_etree_parse               | 109 ms                                                 | 103 ms: 1.07x faster                                                  |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.23 ms: 1.06x faster                                                 |
| meteor_contest                | 77.8 ms                                                | 73.6 ms: 1.06x faster                                                 |
| many_optionals                | 486 us                                                 | 467 us: 1.04x faster                                                  |
| nqueens                       | 63.8 ms                                                | 62.1 ms: 1.03x faster                                                 |
| xml_etree_iterparse           | 74.5 ms                                                | 73.4 ms: 1.01x faster                                                 |
| json_loads                    | 16.6 us                                                | 16.4 us: 1.01x faster                                                 |
| xml_etree_generate            | 53.9 ms                                                | 53.7 ms: 1.00x faster                                                 |
| regex_effbot                  | 2.34 ms                                                | 2.34 ms: 1.00x slower                                                 |
| connected_components          | 318 ms                                                 | 321 ms: 1.01x slower                                                  |
| pidigits                      | 280 ms                                                 | 283 ms: 1.01x slower                                                  |
| python_startup                | 19.6 ms                                                | 20.3 ms: 1.03x slower                                                 |
| 2to3                          | 201 ms                                                 | 211 ms: 1.05x slower                                                  |
| shortest_path                 | 328 ms                                                 | 344 ms: 1.05x slower                                                  |
| dask                          | 789 ms                                                 | 827 ms: 1.05x slower                                                  |
| sqlite_synth                  | 1.48 us                                                | 1.60 us: 1.08x slower                                                 |
| async_generators              | 233 ms                                                 | 262 ms: 1.12x slower                                                  |
| create_gc_cycles              | 1.16 ms                                                | 1.35 ms: 1.16x slower                                                 |
| gc_traversal                  | 2.71 ms                                                | 3.23 ms: 1.19x slower                                                 |
| python_startup_no_site        | 12.8 ms                                                | 15.8 ms: 1.23x slower                                                 |
| telco                         | 3.49 ms                                                | 4.55 ms: 1.30x slower                                                 |
| logging_silent                | 117 ns                                                 | 339 ns: 2.90x slower                                                  |
| coverage                      | 41.2 ms                                                | 292 ms: 7.08x slower                                                  |
| thrift                        | 562 us                                                 | 43.6 ms: 77.62x slower                                                |
| Geometric mean                | (ref)                                                  | 1.21x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250603-3.15.0a0-ec12559/bm-20250603-darwin-arm64-python-ec12559ebafca01ded22-3.15.0a0-ec12559.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.228x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: 1.17x