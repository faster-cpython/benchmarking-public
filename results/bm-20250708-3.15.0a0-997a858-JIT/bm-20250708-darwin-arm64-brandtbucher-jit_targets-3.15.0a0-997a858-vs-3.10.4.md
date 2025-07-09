# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_targets
- machine: darwin-arm64
- commit hash: 997a858
- commit date: 2025-07-08
- overall geometric mean: 1.365x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 169 ms: 1.19x faster                                               |
| docutils       | 1.74 sec                                               | 1.44 sec: 1.21x faster                                             |
| html5lib       | 43.5 ms                                                | 32.5 ms: 1.34x faster                                              |
| sphinx         | 729 ms                                                 | 581 ms: 1.25x faster                                               |
| Geometric mean | (ref)                                                  | 1.25x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|-------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 62.9 ms: 6.23x faster                                              |
| async_tree_eager_memoization  | 483 ms                                                 | 139 ms: 3.47x faster                                               |
| async_tree_eager_io           | 1.01 sec                                               | 358 ms: 2.83x faster                                               |
| async_tree_io                 | 1.02 sec                                               | 370 ms: 2.75x faster                                               |
| async_tree_memoization        | 481 ms                                                 | 192 ms: 2.51x faster                                               |
| async_tree_none               | 391 ms                                                 | 161 ms: 2.43x faster                                               |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 357 ms: 1.87x faster                                               |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 415 ms: 1.61x faster                                               |
| coroutines                    | 20.5 ms                                                | 17.1 ms: 1.20x faster                                              |
| async_generators              | 233 ms                                                 | 280 ms: 1.20x slower                                               |
| Geometric mean                | (ref)                                                  | 2.08x faster                                                       |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 49.9 ms: 1.45x faster                                              |
| nbody          | 92.5 ms                                                | 72.0 ms: 1.28x faster                                              |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                  | 1.23x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 70.6 ms: 1.35x faster                                              |
| regex_dna      | 175 ms                                                 | 144 ms: 1.22x faster                                               |
| regex_v8       | 19.1 ms                                                | 16.0 ms: 1.19x faster                                              |
| regex_effbot   | 2.34 ms                                                | 2.35 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                  | 1.18x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 129 us: 1.54x faster                                               |
| tomli_loads          | 1.72 sec                                               | 1.19 sec: 1.44x faster                                             |
| pickle_pure_python   | 285 us                                                 | 205 us: 1.39x faster                                               |
| xml_etree_process    | 44.6 ms                                                | 34.8 ms: 1.28x faster                                              |
| json_dumps           | 8.31 ms                                                | 6.65 ms: 1.25x faster                                              |
| xml_etree_generate   | 53.9 ms                                                | 49.6 ms: 1.09x faster                                              |
| xml_etree_parse      | 109 ms                                                 | 102 ms: 1.07x faster                                               |
| xml_etree_iterparse  | 74.5 ms                                                | 72.0 ms: 1.03x faster                                              |
| json_loads           | 16.6 us                                                | 16.5 us: 1.00x faster                                              |
| Geometric mean       | (ref)                                                  | 1.22x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 20.5 ms: 1.04x slower                                              |
| python_startup_no_site | 12.8 ms                                                | 15.9 ms: 1.24x slower                                              |
| Geometric mean         | (ref)                                                  | 1.14x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 6.64 ms: 1.48x faster                                              |
| genshi_text     | 17.7 ms                                                | 14.9 ms: 1.19x faster                                              |
| genshi_xml      | 35.1 ms                                                | 31.2 ms: 1.13x faster                                              |
| django_template | 24.4 ms                                                | 21.7 ms: 1.12x faster                                              |
| Geometric mean  | (ref)                                                  | 1.22x faster                                                       |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|-------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 62.9 ms: 6.23x faster                                              |
| typing_runtime_protocols      | 326 us                                                 | 93.8 us: 3.48x faster                                              |
| async_tree_eager_memoization  | 483 ms                                                 | 139 ms: 3.47x faster                                               |
| subparsers                    | 39.8 ms                                                | 13.7 ms: 2.92x faster                                              |
| async_tree_eager_io           | 1.01 sec                                               | 358 ms: 2.83x faster                                               |
| async_tree_io                 | 1.02 sec                                               | 370 ms: 2.75x faster                                               |
| async_tree_memoization        | 481 ms                                                 | 192 ms: 2.51x faster                                               |
| async_tree_none               | 391 ms                                                 | 161 ms: 2.43x faster                                               |
| mdp                           | 1.65 sec                                               | 754 ms: 2.19x faster                                               |
| deltablue                     | 4.99 ms                                                | 2.60 ms: 1.92x faster                                              |
| go                            | 163 ms                                                 | 86.1 ms: 1.90x faster                                              |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 357 ms: 1.87x faster                                               |
| raytrace                      | 327 ms                                                 | 178 ms: 1.83x faster                                               |
| deepcopy_memo                 | 34.7 us                                                | 19.5 us: 1.78x faster                                              |
| deepcopy                      | 276 us                                                 | 156 us: 1.77x faster                                               |
| chaos                         | 67.7 ms                                                | 39.1 ms: 1.73x faster                                              |
| logging_silent                | 117 ns                                                 | 72.2 ns: 1.62x faster                                              |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 415 ms: 1.61x faster                                               |
| pyflate                       | 448 ms                                                 | 283 ms: 1.58x faster                                               |
| scimark_monte_carlo           | 72.4 ms                                                | 45.9 ms: 1.58x faster                                              |
| scimark_sor                   | 140 ms                                                 | 89.2 ms: 1.57x faster                                              |
| richards_super                | 61.0 ms                                                | 39.3 ms: 1.55x faster                                              |
| unpickle_pure_python          | 198 us                                                 | 129 us: 1.54x faster                                               |
| comprehensions                | 17.3 us                                                | 11.3 us: 1.53x faster                                              |
| spectral_norm                 | 95.3 ms                                                | 64.1 ms: 1.49x faster                                              |
| richards                      | 52.3 ms                                                | 35.2 ms: 1.49x faster                                              |
| mako                          | 9.81 ms                                                | 6.64 ms: 1.48x faster                                              |
| pprint_pformat                | 1.33 sec                                               | 901 ms: 1.47x faster                                               |
| pprint_safe_repr              | 648 ms                                                 | 446 ms: 1.45x faster                                               |
| float                         | 72.4 ms                                                | 49.9 ms: 1.45x faster                                              |
| tomli_loads                   | 1.72 sec                                               | 1.19 sec: 1.44x faster                                             |
| pylint                        | 231 ms                                                 | 161 ms: 1.43x faster                                               |
| dulwich_log                   | 35.6 ms                                                | 25.1 ms: 1.42x faster                                              |
| hexiom                        | 6.25 ms                                                | 4.47 ms: 1.40x faster                                              |
| deepcopy_reduce               | 2.32 us                                                | 1.67 us: 1.39x faster                                              |
| pickle_pure_python            | 285 us                                                 | 205 us: 1.39x faster                                               |
| crypto_pyaes                  | 73.3 ms                                                | 53.9 ms: 1.36x faster                                              |
| regex_compile                 | 95.6 ms                                                | 70.6 ms: 1.35x faster                                              |
| logging_format                | 5.03 us                                                | 3.72 us: 1.35x faster                                              |
| html5lib                      | 43.5 ms                                                | 32.5 ms: 1.34x faster                                              |
| logging_simple                | 4.59 us                                                | 3.43 us: 1.34x faster                                              |
| k_core                        | 2.01 sec                                               | 1.51 sec: 1.33x faster                                             |
| generators                    | 31.7 ms                                                | 24.1 ms: 1.32x faster                                              |
| pycparser                     | 887 ms                                                 | 679 ms: 1.31x faster                                               |
| nbody                         | 92.5 ms                                                | 72.0 ms: 1.28x faster                                              |
| xml_etree_process             | 44.6 ms                                                | 34.8 ms: 1.28x faster                                              |
| thrift                        | 562 us                                                 | 440 us: 1.28x faster                                               |
| sphinx                        | 729 ms                                                 | 581 ms: 1.25x faster                                               |
| json_dumps                    | 8.31 ms                                                | 6.65 ms: 1.25x faster                                              |
| scimark_lu                    | 103 ms                                                 | 82.1 ms: 1.25x faster                                              |
| sympy_sum                     | 92.7 ms                                                | 74.8 ms: 1.24x faster                                              |
| regex_dna                     | 175 ms                                                 | 144 ms: 1.22x faster                                               |
| docutils                      | 1.74 sec                                               | 1.44 sec: 1.21x faster                                             |
| coroutines                    | 20.5 ms                                                | 17.1 ms: 1.20x faster                                              |
| sympy_integrate               | 13.2 ms                                                | 11.0 ms: 1.20x faster                                              |
| regex_v8                      | 19.1 ms                                                | 16.0 ms: 1.19x faster                                              |
| genshi_text                   | 17.7 ms                                                | 14.9 ms: 1.19x faster                                              |
| 2to3                          | 201 ms                                                 | 169 ms: 1.19x faster                                               |
| scimark_fft                   | 225 ms                                                 | 190 ms: 1.19x faster                                               |
| fannkuch                      | 303 ms                                                 | 257 ms: 1.18x faster                                               |
| bpe_tokeniser                 | 3.44 sec                                               | 2.94 sec: 1.17x faster                                             |
| sympy_str                     | 166 ms                                                 | 143 ms: 1.16x faster                                               |
| pathlib                       | 25.7 ms                                                | 22.2 ms: 1.16x faster                                              |
| genshi_xml                    | 35.1 ms                                                | 31.2 ms: 1.13x faster                                              |
| django_template               | 24.4 ms                                                | 21.7 ms: 1.12x faster                                              |
| sympy_expand                  | 269 ms                                                 | 242 ms: 1.11x faster                                               |
| xml_etree_generate            | 53.9 ms                                                | 49.6 ms: 1.09x faster                                              |
| meteor_contest                | 77.8 ms                                                | 71.6 ms: 1.09x faster                                              |
| xml_etree_parse               | 109 ms                                                 | 102 ms: 1.07x faster                                               |
| json                          | 3.10 ms                                                | 2.89 ms: 1.07x faster                                              |
| nqueens                       | 63.8 ms                                                | 61.7 ms: 1.04x faster                                              |
| xml_etree_iterparse           | 74.5 ms                                                | 72.0 ms: 1.03x faster                                              |
| many_optionals                | 486 us                                                 | 470 us: 1.03x faster                                               |
| connected_components          | 318 ms                                                 | 308 ms: 1.03x faster                                               |
| dask                          | 789 ms                                                 | 766 ms: 1.03x faster                                               |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.35 ms: 1.02x faster                                              |
| json_loads                    | 16.6 us                                                | 16.5 us: 1.00x faster                                              |
| regex_effbot                  | 2.34 ms                                                | 2.35 ms: 1.01x slower                                              |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                               |
| shortest_path                 | 328 ms                                                 | 337 ms: 1.03x slower                                               |
| python_startup                | 19.6 ms                                                | 20.5 ms: 1.04x slower                                              |
| sqlite_synth                  | 1.48 us                                                | 1.56 us: 1.06x slower                                              |
| coverage                      | 41.2 ms                                                | 48.4 ms: 1.17x slower                                              |
| create_gc_cycles              | 1.16 ms                                                | 1.37 ms: 1.18x slower                                              |
| gc_traversal                  | 2.71 ms                                                | 3.19 ms: 1.18x slower                                              |
| async_generators              | 233 ms                                                 | 280 ms: 1.20x slower                                               |
| python_startup_no_site        | 12.8 ms                                                | 15.9 ms: 1.24x slower                                              |
| telco                         | 3.49 ms                                                | 4.41 ms: 1.26x slower                                              |
| Geometric mean                | (ref)                                                  | 1.37x faster                                                       |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250708-3.15.0a0-997a858-JIT/bm-20250708-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-997a858.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.365x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.19x