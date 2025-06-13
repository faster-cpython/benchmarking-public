# Results vs. 3.10.4

- fork: python
- ref: afc5ab6cce9d7095b99c
- machine: darwin-arm64
- commit hash: afc5ab6
- commit date: 2025-06-13
- overall geometric mean: 1.159x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-darwin-arm64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 186 ms: 1.08x faster                                                  |
| docutils       | 1.74 sec                                               | 1.51 sec: 1.15x faster                                                |
| html5lib       | 43.5 ms                                                | 34.2 ms: 1.27x faster                                                 |
| sphinx         | 729 ms                                                 | 614 ms: 1.19x faster                                                  |
| Geometric mean | (ref)                                                  | 1.17x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-darwin-arm64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 72.9 ms: 5.37x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 151 ms: 3.21x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 392 ms: 2.58x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 413 ms: 2.47x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 215 ms: 2.24x faster                                                  |
| async_tree_none               | 391 ms                                                 | 182 ms: 2.15x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 368 ms: 1.82x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 433 ms: 1.55x faster                                                  |
| coroutines                    | 20.5 ms                                                | 19.3 ms: 1.06x faster                                                 |
| async_generators              | 233 ms                                                 | 274 ms: 1.17x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.92x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-darwin-arm64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 57.5 ms: 1.26x faster                                                 |
| nbody          | 92.5 ms                                                | 84.6 ms: 1.09x faster                                                 |
| pidigits       | 280 ms                                                 | 283 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-darwin-arm64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 175 ms                                                 | 143 ms: 1.22x faster                                                  |
| regex_compile  | 95.6 ms                                                | 81.1 ms: 1.18x faster                                                 |
| regex_v8       | 19.1 ms                                                | 16.3 ms: 1.17x faster                                                 |
| regex_effbot   | 2.34 ms                                                | 2.37 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-darwin-arm64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 8.31 ms                                                | 6.79 ms: 1.22x faster                                                 |
| tomli_loads          | 1.72 sec                                               | 1.44 sec: 1.19x faster                                                |
| pickle_pure_python   | 285 us                                                 | 241 us: 1.18x faster                                                  |
| unpickle_pure_python | 198 us                                                 | 178 us: 1.11x faster                                                  |
| xml_etree_parse      | 109 ms                                                 | 104 ms: 1.05x faster                                                  |
| xml_etree_process    | 44.6 ms                                                | 43.1 ms: 1.04x faster                                                 |
| xml_etree_iterparse  | 74.5 ms                                                | 74.0 ms: 1.01x faster                                                 |
| xml_etree_generate   | 53.9 ms                                                | 58.1 ms: 1.08x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-darwin-arm64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 16.4 ms: 1.20x faster                                                 |
| python_startup_no_site | 12.8 ms                                                | 12.0 ms: 1.07x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-darwin-arm64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 9.03 ms: 1.09x faster                                                 |
| django_template | 24.4 ms                                                | 25.2 ms: 1.03x slower                                                 |
| genshi_xml      | 35.1 ms                                                | 36.4 ms: 1.04x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-darwin-arm64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 72.9 ms: 5.37x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 151 ms: 3.21x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 110 us: 2.98x faster                                                  |
| subparsers                    | 39.8 ms                                                | 14.8 ms: 2.68x faster                                                 |
| async_tree_eager_io           | 1.01 sec                                               | 392 ms: 2.58x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 413 ms: 2.47x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 215 ms: 2.24x faster                                                  |
| async_tree_none               | 391 ms                                                 | 182 ms: 2.15x faster                                                  |
| mdp                           | 1.65 sec                                               | 828 ms: 1.99x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 368 ms: 1.82x faster                                                  |
| deltablue                     | 4.99 ms                                                | 2.81 ms: 1.77x faster                                                 |
| go                            | 163 ms                                                 | 100 ms: 1.63x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 21.8 us: 1.59x faster                                                 |
| deepcopy                      | 276 us                                                 | 176 us: 1.57x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 433 ms: 1.55x faster                                                  |
| raytrace                      | 327 ms                                                 | 212 ms: 1.54x faster                                                  |
| scimark_sor                   | 140 ms                                                 | 90.9 ms: 1.54x faster                                                 |
| richards_super                | 61.0 ms                                                | 41.8 ms: 1.46x faster                                                 |
| richards                      | 52.3 ms                                                | 37.4 ms: 1.40x faster                                                 |
| chaos                         | 67.7 ms                                                | 48.4 ms: 1.40x faster                                                 |
| pylint                        | 231 ms                                                 | 168 ms: 1.38x faster                                                  |
| k_core                        | 2.01 sec                                               | 1.47 sec: 1.37x faster                                                |
| scimark_monte_carlo           | 72.4 ms                                                | 53.0 ms: 1.37x faster                                                 |
| pyflate                       | 448 ms                                                 | 337 ms: 1.33x faster                                                  |
| dulwich_log                   | 35.6 ms                                                | 26.8 ms: 1.33x faster                                                 |
| comprehensions                | 17.3 us                                                | 13.1 us: 1.32x faster                                                 |
| spectral_norm                 | 95.3 ms                                                | 74.7 ms: 1.28x faster                                                 |
| html5lib                      | 43.5 ms                                                | 34.2 ms: 1.27x faster                                                 |
| float                         | 72.4 ms                                                | 57.5 ms: 1.26x faster                                                 |
| hexiom                        | 6.25 ms                                                | 5.10 ms: 1.22x faster                                                 |
| json_dumps                    | 8.31 ms                                                | 6.79 ms: 1.22x faster                                                 |
| regex_dna                     | 175 ms                                                 | 143 ms: 1.22x faster                                                  |
| deepcopy_reduce               | 2.32 us                                                | 1.90 us: 1.22x faster                                                 |
| scimark_lu                    | 103 ms                                                 | 84.4 ms: 1.22x faster                                                 |
| python_startup                | 19.6 ms                                                | 16.4 ms: 1.20x faster                                                 |
| pycparser                     | 887 ms                                                 | 743 ms: 1.19x faster                                                  |
| tomli_loads                   | 1.72 sec                                               | 1.44 sec: 1.19x faster                                                |
| crypto_pyaes                  | 73.3 ms                                                | 61.7 ms: 1.19x faster                                                 |
| sphinx                        | 729 ms                                                 | 614 ms: 1.19x faster                                                  |
| pickle_pure_python            | 285 us                                                 | 241 us: 1.18x faster                                                  |
| regex_compile                 | 95.6 ms                                                | 81.1 ms: 1.18x faster                                                 |
| regex_v8                      | 19.1 ms                                                | 16.3 ms: 1.17x faster                                                 |
| sympy_integrate               | 13.2 ms                                                | 11.4 ms: 1.16x faster                                                 |
| logging_format                | 5.03 us                                                | 4.37 us: 1.15x faster                                                 |
| docutils                      | 1.74 sec                                               | 1.51 sec: 1.15x faster                                                |
| sympy_sum                     | 92.7 ms                                                | 81.2 ms: 1.14x faster                                                 |
| logging_simple                | 4.59 us                                                | 4.06 us: 1.13x faster                                                 |
| unpickle_pure_python          | 198 us                                                 | 178 us: 1.11x faster                                                  |
| nbody                         | 92.5 ms                                                | 84.6 ms: 1.09x faster                                                 |
| scimark_fft                   | 225 ms                                                 | 206 ms: 1.09x faster                                                  |
| mako                          | 9.81 ms                                                | 9.03 ms: 1.09x faster                                                 |
| 2to3                          | 201 ms                                                 | 186 ms: 1.08x faster                                                  |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.17 ms: 1.08x faster                                                 |
| sympy_str                     | 166 ms                                                 | 154 ms: 1.08x faster                                                  |
| python_startup_no_site        | 12.8 ms                                                | 12.0 ms: 1.07x faster                                                 |
| coroutines                    | 20.5 ms                                                | 19.3 ms: 1.06x faster                                                 |
| pathlib                       | 25.7 ms                                                | 24.3 ms: 1.06x faster                                                 |
| json                          | 3.10 ms                                                | 2.93 ms: 1.06x faster                                                 |
| connected_components          | 318 ms                                                 | 302 ms: 1.05x faster                                                  |
| xml_etree_parse               | 109 ms                                                 | 104 ms: 1.05x faster                                                  |
| pprint_pformat                | 1.33 sec                                               | 1.26 sec: 1.05x faster                                                |
| bpe_tokeniser                 | 3.44 sec                                               | 3.28 sec: 1.05x faster                                                |
| pprint_safe_repr              | 648 ms                                                 | 621 ms: 1.04x faster                                                  |
| meteor_contest                | 77.8 ms                                                | 75.0 ms: 1.04x faster                                                 |
| xml_etree_process             | 44.6 ms                                                | 43.1 ms: 1.04x faster                                                 |
| sympy_expand                  | 269 ms                                                 | 261 ms: 1.03x faster                                                  |
| dask                          | 789 ms                                                 | 771 ms: 1.02x faster                                                  |
| xml_etree_iterparse           | 74.5 ms                                                | 74.0 ms: 1.01x faster                                                 |
| generators                    | 31.7 ms                                                | 31.5 ms: 1.01x faster                                                 |
| shortest_path                 | 328 ms                                                 | 327 ms: 1.00x faster                                                  |
| pidigits                      | 280 ms                                                 | 283 ms: 1.01x slower                                                  |
| many_optionals                | 486 us                                                 | 493 us: 1.02x slower                                                  |
| regex_effbot                  | 2.34 ms                                                | 2.37 ms: 1.02x slower                                                 |
| fannkuch                      | 303 ms                                                 | 310 ms: 1.02x slower                                                  |
| django_template               | 24.4 ms                                                | 25.2 ms: 1.03x slower                                                 |
| genshi_xml                    | 35.1 ms                                                | 36.4 ms: 1.04x slower                                                 |
| xml_etree_generate            | 53.9 ms                                                | 58.1 ms: 1.08x slower                                                 |
| sqlite_synth                  | 1.48 us                                                | 1.62 us: 1.10x slower                                                 |
| nqueens                       | 63.8 ms                                                | 71.4 ms: 1.12x slower                                                 |
| create_gc_cycles              | 1.16 ms                                                | 1.35 ms: 1.16x slower                                                 |
| async_generators              | 233 ms                                                 | 274 ms: 1.17x slower                                                  |
| gc_traversal                  | 2.71 ms                                                | 3.19 ms: 1.18x slower                                                 |
| telco                         | 3.49 ms                                                | 4.77 ms: 1.37x slower                                                 |
| logging_silent                | 117 ns                                                 | 336 ns: 2.87x slower                                                  |
| coverage                      | 41.2 ms                                                | 337 ms: 8.17x slower                                                  |
| thrift                        | 562 us                                                 | 43.9 ms: 78.08x slower                                                |
| Geometric mean                | (ref)                                                  | 1.14x faster                                                          |

Benchmark hidden because not significant (3): json_loads, asyncio_websockets, genshi_text
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250613-3.15.0a0-afc5ab6/bm-20250613-darwin-arm64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.159x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.17x