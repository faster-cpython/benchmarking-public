# Results vs. 3.10.4

- fork: python
- ref: c419af9e277bea7dd78f
- machine: darwin-arm64
- commit hash: c419af9
- commit date: 2025-06-28
- overall geometric mean: 1.344x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-darwin-arm64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 172 ms: 1.17x faster                                                  |
| docutils       | 1.74 sec                                               | 1.46 sec: 1.19x faster                                                |
| html5lib       | 43.5 ms                                                | 31.5 ms: 1.38x faster                                                 |
| sphinx         | 729 ms                                                 | 584 ms: 1.25x faster                                                  |
| Geometric mean | (ref)                                                  | 1.25x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-darwin-arm64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 64.3 ms: 6.10x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 141 ms: 3.44x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 360 ms: 2.82x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 374 ms: 2.72x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 194 ms: 2.49x faster                                                  |
| async_tree_none               | 391 ms                                                 | 163 ms: 2.41x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 358 ms: 1.87x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 415 ms: 1.61x faster                                                  |
| coroutines                    | 20.5 ms                                                | 17.0 ms: 1.20x faster                                                 |
| async_generators              | 233 ms                                                 | 280 ms: 1.20x slower                                                  |
| Geometric mean                | (ref)                                                  | 2.06x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-darwin-arm64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 49.9 ms: 1.45x faster                                                 |
| nbody          | 92.5 ms                                                | 75.4 ms: 1.23x faster                                                 |
| pidigits       | 280 ms                                                 | 283 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.21x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-darwin-arm64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 71.1 ms: 1.34x faster                                                 |
| regex_dna      | 175 ms                                                 | 143 ms: 1.22x faster                                                  |
| regex_v8       | 19.1 ms                                                | 16.2 ms: 1.18x faster                                                 |
| regex_effbot   | 2.34 ms                                                | 2.37 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.17x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-darwin-arm64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 134 us: 1.48x faster                                                  |
| tomli_loads          | 1.72 sec                                               | 1.23 sec: 1.39x faster                                                |
| pickle_pure_python   | 285 us                                                 | 210 us: 1.36x faster                                                  |
| json_dumps           | 8.31 ms                                                | 6.55 ms: 1.27x faster                                                 |
| xml_etree_process    | 44.6 ms                                                | 35.6 ms: 1.25x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 102 ms: 1.07x faster                                                  |
| xml_etree_generate   | 53.9 ms                                                | 50.9 ms: 1.06x faster                                                 |
| xml_etree_iterparse  | 74.5 ms                                                | 72.5 ms: 1.03x faster                                                 |
| json_loads           | 16.6 us                                                | 16.5 us: 1.01x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.20x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-darwin-arm64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 18.5 ms: 1.06x faster                                                 |
| python_startup_no_site | 12.8 ms                                                | 13.8 ms: 1.08x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-darwin-arm64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 6.93 ms: 1.42x faster                                                 |
| genshi_text     | 17.7 ms                                                | 14.9 ms: 1.19x faster                                                 |
| genshi_xml      | 35.1 ms                                                | 31.1 ms: 1.13x faster                                                 |
| django_template | 24.4 ms                                                | 21.8 ms: 1.12x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.21x faster                                                          |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-darwin-arm64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 64.3 ms: 6.10x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 141 ms: 3.44x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 97.6 us: 3.34x faster                                                 |
| subparsers                    | 39.8 ms                                                | 13.8 ms: 2.89x faster                                                 |
| async_tree_eager_io           | 1.01 sec                                               | 360 ms: 2.82x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 374 ms: 2.72x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 194 ms: 2.49x faster                                                  |
| async_tree_none               | 391 ms                                                 | 163 ms: 2.41x faster                                                  |
| mdp                           | 1.65 sec                                               | 759 ms: 2.17x faster                                                  |
| go                            | 163 ms                                                 | 87.3 ms: 1.87x faster                                                 |
| deltablue                     | 4.99 ms                                                | 2.67 ms: 1.87x faster                                                 |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 358 ms: 1.87x faster                                                  |
| raytrace                      | 327 ms                                                 | 179 ms: 1.83x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 19.5 us: 1.78x faster                                                 |
| deepcopy                      | 276 us                                                 | 155 us: 1.77x faster                                                  |
| chaos                         | 67.7 ms                                                | 39.5 ms: 1.72x faster                                                 |
| logging_silent                | 117 ns                                                 | 72.5 ns: 1.61x faster                                                 |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 415 ms: 1.61x faster                                                  |
| scimark_monte_carlo           | 72.4 ms                                                | 45.9 ms: 1.58x faster                                                 |
| scimark_sor                   | 140 ms                                                 | 89.2 ms: 1.57x faster                                                 |
| pyflate                       | 448 ms                                                 | 292 ms: 1.53x faster                                                  |
| richards_super                | 61.0 ms                                                | 39.9 ms: 1.53x faster                                                 |
| unpickle_pure_python          | 198 us                                                 | 134 us: 1.48x faster                                                  |
| richards                      | 52.3 ms                                                | 35.8 ms: 1.46x faster                                                 |
| float                         | 72.4 ms                                                | 49.9 ms: 1.45x faster                                                 |
| comprehensions                | 17.3 us                                                | 12.1 us: 1.43x faster                                                 |
| dulwich_log                   | 35.6 ms                                                | 25.1 ms: 1.42x faster                                                 |
| pylint                        | 231 ms                                                 | 163 ms: 1.42x faster                                                  |
| mako                          | 9.81 ms                                                | 6.93 ms: 1.42x faster                                                 |
| spectral_norm                 | 95.3 ms                                                | 67.9 ms: 1.40x faster                                                 |
| tomli_loads                   | 1.72 sec                                               | 1.23 sec: 1.39x faster                                                |
| deepcopy_reduce               | 2.32 us                                                | 1.67 us: 1.39x faster                                                 |
| html5lib                      | 43.5 ms                                                | 31.5 ms: 1.38x faster                                                 |
| pickle_pure_python            | 285 us                                                 | 210 us: 1.36x faster                                                  |
| regex_compile                 | 95.6 ms                                                | 71.1 ms: 1.34x faster                                                 |
| logging_format                | 5.03 us                                                | 3.76 us: 1.34x faster                                                 |
| k_core                        | 2.01 sec                                               | 1.52 sec: 1.32x faster                                                |
| hexiom                        | 6.25 ms                                                | 4.72 ms: 1.32x faster                                                 |
| logging_simple                | 4.59 us                                                | 3.47 us: 1.32x faster                                                 |
| crypto_pyaes                  | 73.3 ms                                                | 55.6 ms: 1.32x faster                                                 |
| generators                    | 31.7 ms                                                | 24.0 ms: 1.32x faster                                                 |
| json_dumps                    | 8.31 ms                                                | 6.55 ms: 1.27x faster                                                 |
| thrift                        | 562 us                                                 | 443 us: 1.27x faster                                                  |
| pycparser                     | 887 ms                                                 | 702 ms: 1.26x faster                                                  |
| xml_etree_process             | 44.6 ms                                                | 35.6 ms: 1.25x faster                                                 |
| scimark_lu                    | 103 ms                                                 | 82.0 ms: 1.25x faster                                                 |
| sphinx                        | 729 ms                                                 | 584 ms: 1.25x faster                                                  |
| pprint_pformat                | 1.33 sec                                               | 1.08 sec: 1.23x faster                                                |
| nbody                         | 92.5 ms                                                | 75.4 ms: 1.23x faster                                                 |
| sympy_sum                     | 92.7 ms                                                | 75.7 ms: 1.22x faster                                                 |
| regex_dna                     | 175 ms                                                 | 143 ms: 1.22x faster                                                  |
| pprint_safe_repr              | 648 ms                                                 | 537 ms: 1.21x faster                                                  |
| coroutines                    | 20.5 ms                                                | 17.0 ms: 1.20x faster                                                 |
| docutils                      | 1.74 sec                                               | 1.46 sec: 1.19x faster                                                |
| genshi_text                   | 17.7 ms                                                | 14.9 ms: 1.19x faster                                                 |
| sympy_integrate               | 13.2 ms                                                | 11.0 ms: 1.19x faster                                                 |
| regex_v8                      | 19.1 ms                                                | 16.2 ms: 1.18x faster                                                 |
| pathlib                       | 25.7 ms                                                | 21.9 ms: 1.18x faster                                                 |
| 2to3                          | 201 ms                                                 | 172 ms: 1.17x faster                                                  |
| sympy_str                     | 166 ms                                                 | 143 ms: 1.16x faster                                                  |
| scimark_fft                   | 225 ms                                                 | 199 ms: 1.13x faster                                                  |
| genshi_xml                    | 35.1 ms                                                | 31.1 ms: 1.13x faster                                                 |
| django_template               | 24.4 ms                                                | 21.8 ms: 1.12x faster                                                 |
| bpe_tokeniser                 | 3.44 sec                                               | 3.08 sec: 1.12x faster                                                |
| sympy_expand                  | 269 ms                                                 | 244 ms: 1.10x faster                                                  |
| xml_etree_parse               | 109 ms                                                 | 102 ms: 1.07x faster                                                  |
| python_startup                | 19.6 ms                                                | 18.5 ms: 1.06x faster                                                 |
| xml_etree_generate            | 53.9 ms                                                | 50.9 ms: 1.06x faster                                                 |
| json                          | 3.10 ms                                                | 2.94 ms: 1.06x faster                                                 |
| nqueens                       | 63.8 ms                                                | 61.5 ms: 1.04x faster                                                 |
| dask                          | 789 ms                                                 | 766 ms: 1.03x faster                                                  |
| xml_etree_iterparse           | 74.5 ms                                                | 72.5 ms: 1.03x faster                                                 |
| connected_components          | 318 ms                                                 | 311 ms: 1.02x faster                                                  |
| meteor_contest                | 77.8 ms                                                | 76.1 ms: 1.02x faster                                                 |
| many_optionals                | 486 us                                                 | 476 us: 1.02x faster                                                  |
| json_loads                    | 16.6 us                                                | 16.5 us: 1.01x faster                                                 |
| pidigits                      | 280 ms                                                 | 283 ms: 1.01x slower                                                  |
| regex_effbot                  | 2.34 ms                                                | 2.37 ms: 1.02x slower                                                 |
| shortest_path                 | 328 ms                                                 | 337 ms: 1.03x slower                                                  |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.54 ms: 1.03x slower                                                 |
| sqlite_synth                  | 1.48 us                                                | 1.58 us: 1.07x slower                                                 |
| python_startup_no_site        | 12.8 ms                                                | 13.8 ms: 1.08x slower                                                 |
| coverage                      | 41.2 ms                                                | 47.9 ms: 1.16x slower                                                 |
| create_gc_cycles              | 1.16 ms                                                | 1.37 ms: 1.17x slower                                                 |
| gc_traversal                  | 2.71 ms                                                | 3.22 ms: 1.19x slower                                                 |
| async_generators              | 233 ms                                                 | 280 ms: 1.20x slower                                                  |
| telco                         | 3.49 ms                                                | 4.61 ms: 1.32x slower                                                 |
| Geometric mean                | (ref)                                                  | 1.35x faster                                                          |

Benchmark hidden because not significant (2): fannkuch, asyncio_websockets
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250628-3.15.0a0-c419af9-JIT/bm-20250628-darwin-arm64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.344x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: 1.19x