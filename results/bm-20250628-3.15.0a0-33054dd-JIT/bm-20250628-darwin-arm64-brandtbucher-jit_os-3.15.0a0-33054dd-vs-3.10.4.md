# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_os
- machine: darwin-arm64
- commit hash: 33054dd
- commit date: 2025-06-28
- overall geometric mean: 1.339x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-darwin-arm64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 174 ms: 1.16x faster                                          |
| docutils       | 1.74 sec                                               | 1.47 sec: 1.18x faster                                        |
| html5lib       | 43.5 ms                                                | 31.7 ms: 1.37x faster                                         |
| sphinx         | 729 ms                                                 | 587 ms: 1.24x faster                                          |
| Geometric mean | (ref)                                                  | 1.23x faster                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-darwin-arm64-brandtbucher-jit_os-3.15.0a0-33054dd |
|-------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 64.5 ms: 6.08x faster                                         |
| async_tree_eager_memoization  | 483 ms                                                 | 141 ms: 3.43x faster                                          |
| async_tree_eager_io           | 1.01 sec                                               | 361 ms: 2.81x faster                                          |
| async_tree_io                 | 1.02 sec                                               | 376 ms: 2.71x faster                                          |
| async_tree_memoization        | 481 ms                                                 | 194 ms: 2.48x faster                                          |
| async_tree_none               | 391 ms                                                 | 162 ms: 2.41x faster                                          |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 358 ms: 1.87x faster                                          |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 415 ms: 1.61x faster                                          |
| coroutines                    | 20.5 ms                                                | 17.0 ms: 1.20x faster                                         |
| async_generators              | 233 ms                                                 | 278 ms: 1.19x slower                                          |
| Geometric mean                | (ref)                                                  | 2.06x faster                                                  |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-darwin-arm64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 72.4 ms                                                | 49.9 ms: 1.45x faster                                         |
| nbody          | 92.5 ms                                                | 75.7 ms: 1.22x faster                                         |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                          |
| Geometric mean | (ref)                                                  | 1.21x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-darwin-arm64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 71.4 ms: 1.34x faster                                         |
| regex_dna      | 175 ms                                                 | 143 ms: 1.22x faster                                          |
| regex_v8       | 19.1 ms                                                | 16.1 ms: 1.19x faster                                         |
| regex_effbot   | 2.34 ms                                                | 2.34 ms: 1.00x slower                                         |
| Geometric mean | (ref)                                                  | 1.18x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-darwin-arm64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 134 us: 1.48x faster                                          |
| tomli_loads          | 1.72 sec                                               | 1.24 sec: 1.39x faster                                        |
| pickle_pure_python   | 285 us                                                 | 211 us: 1.35x faster                                          |
| json_dumps           | 8.31 ms                                                | 6.57 ms: 1.26x faster                                         |
| xml_etree_process    | 44.6 ms                                                | 35.8 ms: 1.25x faster                                         |
| xml_etree_parse      | 109 ms                                                 | 103 ms: 1.07x faster                                          |
| xml_etree_generate   | 53.9 ms                                                | 51.0 ms: 1.06x faster                                         |
| xml_etree_iterparse  | 74.5 ms                                                | 72.3 ms: 1.03x faster                                         |
| json_loads           | 16.6 us                                                | 16.4 us: 1.01x faster                                         |
| Geometric mean       | (ref)                                                  | 1.20x faster                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-darwin-arm64-brandtbucher-jit_os-3.15.0a0-33054dd |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 18.7 ms: 1.05x faster                                         |
| python_startup_no_site | 12.8 ms                                                | 14.2 ms: 1.11x slower                                         |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-darwin-arm64-brandtbucher-jit_os-3.15.0a0-33054dd |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 6.99 ms: 1.40x faster                                         |
| genshi_text     | 17.7 ms                                                | 14.9 ms: 1.19x faster                                         |
| genshi_xml      | 35.1 ms                                                | 31.3 ms: 1.12x faster                                         |
| django_template | 24.4 ms                                                | 22.0 ms: 1.11x faster                                         |
| Geometric mean  | (ref)                                                  | 1.20x faster                                                  |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-darwin-arm64-brandtbucher-jit_os-3.15.0a0-33054dd |
|-------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 64.5 ms: 6.08x faster                                         |
| async_tree_eager_memoization  | 483 ms                                                 | 141 ms: 3.43x faster                                          |
| typing_runtime_protocols      | 326 us                                                 | 98.0 us: 3.33x faster                                         |
| subparsers                    | 39.8 ms                                                | 13.8 ms: 2.89x faster                                         |
| async_tree_eager_io           | 1.01 sec                                               | 361 ms: 2.81x faster                                          |
| async_tree_io                 | 1.02 sec                                               | 376 ms: 2.71x faster                                          |
| async_tree_memoization        | 481 ms                                                 | 194 ms: 2.48x faster                                          |
| async_tree_none               | 391 ms                                                 | 162 ms: 2.41x faster                                          |
| mdp                           | 1.65 sec                                               | 759 ms: 2.17x faster                                          |
| deltablue                     | 4.99 ms                                                | 2.67 ms: 1.87x faster                                         |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 358 ms: 1.87x faster                                          |
| go                            | 163 ms                                                 | 88.1 ms: 1.85x faster                                         |
| raytrace                      | 327 ms                                                 | 179 ms: 1.82x faster                                          |
| deepcopy_memo                 | 34.7 us                                                | 19.5 us: 1.78x faster                                         |
| deepcopy                      | 276 us                                                 | 156 us: 1.77x faster                                          |
| chaos                         | 67.7 ms                                                | 39.7 ms: 1.70x faster                                         |
| logging_silent                | 117 ns                                                 | 72.3 ns: 1.62x faster                                         |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 415 ms: 1.61x faster                                          |
| scimark_monte_carlo           | 72.4 ms                                                | 46.0 ms: 1.57x faster                                         |
| scimark_sor                   | 140 ms                                                 | 88.9 ms: 1.57x faster                                         |
| pyflate                       | 448 ms                                                 | 292 ms: 1.53x faster                                          |
| richards_super                | 61.0 ms                                                | 41.2 ms: 1.48x faster                                         |
| unpickle_pure_python          | 198 us                                                 | 134 us: 1.48x faster                                          |
| float                         | 72.4 ms                                                | 49.9 ms: 1.45x faster                                         |
| richards                      | 52.3 ms                                                | 36.5 ms: 1.43x faster                                         |
| dulwich_log                   | 35.6 ms                                                | 25.0 ms: 1.42x faster                                         |
| pylint                        | 231 ms                                                 | 163 ms: 1.42x faster                                          |
| comprehensions                | 17.3 us                                                | 12.2 us: 1.41x faster                                         |
| spectral_norm                 | 95.3 ms                                                | 67.8 ms: 1.41x faster                                         |
| mako                          | 9.81 ms                                                | 6.99 ms: 1.40x faster                                         |
| deepcopy_reduce               | 2.32 us                                                | 1.67 us: 1.39x faster                                         |
| tomli_loads                   | 1.72 sec                                               | 1.24 sec: 1.39x faster                                        |
| html5lib                      | 43.5 ms                                                | 31.7 ms: 1.37x faster                                         |
| pickle_pure_python            | 285 us                                                 | 211 us: 1.35x faster                                          |
| regex_compile                 | 95.6 ms                                                | 71.4 ms: 1.34x faster                                         |
| logging_format                | 5.03 us                                                | 3.79 us: 1.33x faster                                         |
| logging_simple                | 4.59 us                                                | 3.47 us: 1.32x faster                                         |
| generators                    | 31.7 ms                                                | 24.1 ms: 1.32x faster                                         |
| k_core                        | 2.01 sec                                               | 1.53 sec: 1.32x faster                                        |
| hexiom                        | 6.25 ms                                                | 4.75 ms: 1.31x faster                                         |
| crypto_pyaes                  | 73.3 ms                                                | 56.1 ms: 1.31x faster                                         |
| thrift                        | 562 us                                                 | 443 us: 1.27x faster                                          |
| json_dumps                    | 8.31 ms                                                | 6.57 ms: 1.26x faster                                         |
| pycparser                     | 887 ms                                                 | 710 ms: 1.25x faster                                          |
| xml_etree_process             | 44.6 ms                                                | 35.8 ms: 1.25x faster                                         |
| sphinx                        | 729 ms                                                 | 587 ms: 1.24x faster                                          |
| scimark_lu                    | 103 ms                                                 | 82.8 ms: 1.24x faster                                         |
| regex_dna                     | 175 ms                                                 | 143 ms: 1.22x faster                                          |
| nbody                         | 92.5 ms                                                | 75.7 ms: 1.22x faster                                         |
| sympy_sum                     | 92.7 ms                                                | 76.0 ms: 1.22x faster                                         |
| pprint_safe_repr              | 648 ms                                                 | 537 ms: 1.21x faster                                          |
| pprint_pformat                | 1.33 sec                                               | 1.10 sec: 1.20x faster                                        |
| coroutines                    | 20.5 ms                                                | 17.0 ms: 1.20x faster                                         |
| genshi_text                   | 17.7 ms                                                | 14.9 ms: 1.19x faster                                         |
| sympy_integrate               | 13.2 ms                                                | 11.1 ms: 1.19x faster                                         |
| regex_v8                      | 19.1 ms                                                | 16.1 ms: 1.19x faster                                         |
| docutils                      | 1.74 sec                                               | 1.47 sec: 1.18x faster                                        |
| 2to3                          | 201 ms                                                 | 174 ms: 1.16x faster                                          |
| sympy_str                     | 166 ms                                                 | 144 ms: 1.15x faster                                          |
| pathlib                       | 25.7 ms                                                | 22.5 ms: 1.14x faster                                         |
| scimark_fft                   | 225 ms                                                 | 198 ms: 1.14x faster                                          |
| genshi_xml                    | 35.1 ms                                                | 31.3 ms: 1.12x faster                                         |
| django_template               | 24.4 ms                                                | 22.0 ms: 1.11x faster                                         |
| bpe_tokeniser                 | 3.44 sec                                               | 3.10 sec: 1.11x faster                                        |
| sympy_expand                  | 269 ms                                                 | 245 ms: 1.10x faster                                          |
| json                          | 3.10 ms                                                | 2.91 ms: 1.07x faster                                         |
| xml_etree_parse               | 109 ms                                                 | 103 ms: 1.07x faster                                          |
| xml_etree_generate            | 53.9 ms                                                | 51.0 ms: 1.06x faster                                         |
| python_startup                | 19.6 ms                                                | 18.7 ms: 1.05x faster                                         |
| nqueens                       | 63.8 ms                                                | 61.7 ms: 1.03x faster                                         |
| dask                          | 789 ms                                                 | 766 ms: 1.03x faster                                          |
| xml_etree_iterparse           | 74.5 ms                                                | 72.3 ms: 1.03x faster                                         |
| connected_components          | 318 ms                                                 | 310 ms: 1.03x faster                                          |
| meteor_contest                | 77.8 ms                                                | 76.5 ms: 1.02x faster                                         |
| json_loads                    | 16.6 us                                                | 16.4 us: 1.01x faster                                         |
| fannkuch                      | 303 ms                                                 | 299 ms: 1.01x faster                                          |
| many_optionals                | 486 us                                                 | 481 us: 1.01x faster                                          |
| regex_effbot                  | 2.34 ms                                                | 2.34 ms: 1.00x slower                                         |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                          |
| shortest_path                 | 328 ms                                                 | 337 ms: 1.03x slower                                          |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.51 ms: 1.03x slower                                         |
| sqlite_synth                  | 1.48 us                                                | 1.59 us: 1.07x slower                                         |
| python_startup_no_site        | 12.8 ms                                                | 14.2 ms: 1.11x slower                                         |
| coverage                      | 41.2 ms                                                | 47.9 ms: 1.16x slower                                         |
| create_gc_cycles              | 1.16 ms                                                | 1.36 ms: 1.17x slower                                         |
| gc_traversal                  | 2.71 ms                                                | 3.21 ms: 1.19x slower                                         |
| async_generators              | 233 ms                                                 | 278 ms: 1.19x slower                                          |
| telco                         | 3.49 ms                                                | 4.55 ms: 1.30x slower                                         |
| Geometric mean                | (ref)                                                  | 1.34x faster                                                  |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250628-3.15.0a0-33054dd-JIT/bm-20250628-darwin-arm64-brandtbucher-jit_os-3.15.0a0-33054dd.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.339x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: 1.19x