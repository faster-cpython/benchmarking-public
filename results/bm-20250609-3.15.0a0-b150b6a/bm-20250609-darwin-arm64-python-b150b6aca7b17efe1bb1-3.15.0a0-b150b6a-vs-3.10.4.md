# Results vs. 3.10.4

- fork: python
- ref: b150b6aca7b17efe1bb1
- machine: darwin-arm64
- commit hash: b150b6a
- commit date: 2025-06-09
- overall geometric mean: 1.154x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-darwin-arm64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 186 ms: 1.08x faster                                                  |
| docutils       | 1.74 sec                                               | 1.51 sec: 1.15x faster                                                |
| html5lib       | 43.5 ms                                                | 34.2 ms: 1.27x faster                                                 |
| sphinx         | 729 ms                                                 | 615 ms: 1.19x faster                                                  |
| Geometric mean | (ref)                                                  | 1.17x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-darwin-arm64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 74.2 ms: 5.28x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 151 ms: 3.20x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 397 ms: 2.56x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 414 ms: 2.46x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 215 ms: 2.24x faster                                                  |
| async_tree_none               | 391 ms                                                 | 183 ms: 2.14x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 372 ms: 1.80x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 433 ms: 1.54x faster                                                  |
| coroutines                    | 20.5 ms                                                | 19.3 ms: 1.06x faster                                                 |
| async_generators              | 233 ms                                                 | 274 ms: 1.17x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.92x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-darwin-arm64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 57.5 ms: 1.26x faster                                                 |
| nbody          | 92.5 ms                                                | 84.9 ms: 1.09x faster                                                 |
| pidigits       | 280 ms                                                 | 283 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-darwin-arm64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 175 ms                                                 | 143 ms: 1.22x faster                                                  |
| regex_v8       | 19.1 ms                                                | 16.2 ms: 1.18x faster                                                 |
| regex_compile  | 95.6 ms                                                | 81.1 ms: 1.18x faster                                                 |
| regex_effbot   | 2.34 ms                                                | 2.34 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                  | 1.14x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-darwin-arm64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 8.31 ms                                                | 6.79 ms: 1.22x faster                                                 |
| tomli_loads          | 1.72 sec                                               | 1.43 sec: 1.20x faster                                                |
| pickle_pure_python   | 285 us                                                 | 241 us: 1.18x faster                                                  |
| unpickle_pure_python | 198 us                                                 | 177 us: 1.12x faster                                                  |
| xml_etree_parse      | 109 ms                                                 | 104 ms: 1.05x faster                                                  |
| xml_etree_process    | 44.6 ms                                                | 43.1 ms: 1.03x faster                                                 |
| xml_etree_generate   | 53.9 ms                                                | 58.3 ms: 1.08x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (2): xml_etree_iterparse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-darwin-arm64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 18.6 ms: 1.06x faster                                                 |
| python_startup_no_site | 12.8 ms                                                | 14.0 ms: 1.10x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-darwin-arm64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 9.02 ms: 1.09x faster                                                 |
| genshi_text     | 17.7 ms                                                | 17.6 ms: 1.00x faster                                                 |
| django_template | 24.4 ms                                                | 25.2 ms: 1.03x slower                                                 |
| genshi_xml      | 35.1 ms                                                | 36.4 ms: 1.04x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                          |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-darwin-arm64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 74.2 ms: 5.28x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 151 ms: 3.20x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 110 us: 2.97x faster                                                  |
| subparsers                    | 39.8 ms                                                | 14.9 ms: 2.68x faster                                                 |
| async_tree_eager_io           | 1.01 sec                                               | 397 ms: 2.56x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 414 ms: 2.46x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 215 ms: 2.24x faster                                                  |
| async_tree_none               | 391 ms                                                 | 183 ms: 2.14x faster                                                  |
| mdp                           | 1.65 sec                                               | 827 ms: 2.00x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 372 ms: 1.80x faster                                                  |
| deltablue                     | 4.99 ms                                                | 2.82 ms: 1.77x faster                                                 |
| go                            | 163 ms                                                 | 100 ms: 1.63x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 21.8 us: 1.59x faster                                                 |
| deepcopy                      | 276 us                                                 | 175 us: 1.58x faster                                                  |
| raytrace                      | 327 ms                                                 | 211 ms: 1.55x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 433 ms: 1.54x faster                                                  |
| scimark_sor                   | 140 ms                                                 | 91.3 ms: 1.53x faster                                                 |
| richards_super                | 61.0 ms                                                | 41.8 ms: 1.46x faster                                                 |
| chaos                         | 67.7 ms                                                | 48.3 ms: 1.40x faster                                                 |
| richards                      | 52.3 ms                                                | 37.3 ms: 1.40x faster                                                 |
| pylint                        | 231 ms                                                 | 168 ms: 1.38x faster                                                  |
| k_core                        | 2.01 sec                                               | 1.46 sec: 1.37x faster                                                |
| scimark_monte_carlo           | 72.4 ms                                                | 53.0 ms: 1.37x faster                                                 |
| pyflate                       | 448 ms                                                 | 336 ms: 1.33x faster                                                  |
| dulwich_log                   | 35.6 ms                                                | 26.8 ms: 1.33x faster                                                 |
| comprehensions                | 17.3 us                                                | 13.1 us: 1.32x faster                                                 |
| spectral_norm                 | 95.3 ms                                                | 74.3 ms: 1.28x faster                                                 |
| html5lib                      | 43.5 ms                                                | 34.2 ms: 1.27x faster                                                 |
| float                         | 72.4 ms                                                | 57.5 ms: 1.26x faster                                                 |
| deepcopy_reduce               | 2.32 us                                                | 1.90 us: 1.22x faster                                                 |
| regex_dna                     | 175 ms                                                 | 143 ms: 1.22x faster                                                  |
| hexiom                        | 6.25 ms                                                | 5.11 ms: 1.22x faster                                                 |
| json_dumps                    | 8.31 ms                                                | 6.79 ms: 1.22x faster                                                 |
| scimark_lu                    | 103 ms                                                 | 84.2 ms: 1.22x faster                                                 |
| tomli_loads                   | 1.72 sec                                               | 1.43 sec: 1.20x faster                                                |
| crypto_pyaes                  | 73.3 ms                                                | 61.3 ms: 1.20x faster                                                 |
| pycparser                     | 887 ms                                                 | 744 ms: 1.19x faster                                                  |
| sphinx                        | 729 ms                                                 | 615 ms: 1.19x faster                                                  |
| regex_v8                      | 19.1 ms                                                | 16.2 ms: 1.18x faster                                                 |
| pickle_pure_python            | 285 us                                                 | 241 us: 1.18x faster                                                  |
| regex_compile                 | 95.6 ms                                                | 81.1 ms: 1.18x faster                                                 |
| sympy_integrate               | 13.2 ms                                                | 11.3 ms: 1.16x faster                                                 |
| logging_format                | 5.03 us                                                | 4.36 us: 1.15x faster                                                 |
| docutils                      | 1.74 sec                                               | 1.51 sec: 1.15x faster                                                |
| sympy_sum                     | 92.7 ms                                                | 81.2 ms: 1.14x faster                                                 |
| logging_simple                | 4.59 us                                                | 4.07 us: 1.13x faster                                                 |
| unpickle_pure_python          | 198 us                                                 | 177 us: 1.12x faster                                                  |
| pathlib                       | 25.7 ms                                                | 23.0 ms: 1.12x faster                                                 |
| scimark_fft                   | 225 ms                                                 | 207 ms: 1.09x faster                                                  |
| nbody                         | 92.5 ms                                                | 84.9 ms: 1.09x faster                                                 |
| mako                          | 9.81 ms                                                | 9.02 ms: 1.09x faster                                                 |
| 2to3                          | 201 ms                                                 | 186 ms: 1.08x faster                                                  |
| sympy_str                     | 166 ms                                                 | 154 ms: 1.08x faster                                                  |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.19 ms: 1.07x faster                                                 |
| coroutines                    | 20.5 ms                                                | 19.3 ms: 1.06x faster                                                 |
| python_startup                | 19.6 ms                                                | 18.6 ms: 1.06x faster                                                 |
| bpe_tokeniser                 | 3.44 sec                                               | 3.27 sec: 1.05x faster                                                |
| xml_etree_parse               | 109 ms                                                 | 104 ms: 1.05x faster                                                  |
| connected_components          | 318 ms                                                 | 303 ms: 1.05x faster                                                  |
| json                          | 3.10 ms                                                | 2.96 ms: 1.05x faster                                                 |
| pprint_pformat                | 1.33 sec                                               | 1.27 sec: 1.05x faster                                                |
| meteor_contest                | 77.8 ms                                                | 74.8 ms: 1.04x faster                                                 |
| pprint_safe_repr              | 648 ms                                                 | 624 ms: 1.04x faster                                                  |
| xml_etree_process             | 44.6 ms                                                | 43.1 ms: 1.03x faster                                                 |
| sympy_expand                  | 269 ms                                                 | 262 ms: 1.03x faster                                                  |
| genshi_text                   | 17.7 ms                                                | 17.6 ms: 1.00x faster                                                 |
| generators                    | 31.7 ms                                                | 31.6 ms: 1.00x faster                                                 |
| regex_effbot                  | 2.34 ms                                                | 2.34 ms: 1.00x slower                                                 |
| pidigits                      | 280 ms                                                 | 283 ms: 1.01x slower                                                  |
| many_optionals                | 486 us                                                 | 494 us: 1.02x slower                                                  |
| fannkuch                      | 303 ms                                                 | 310 ms: 1.03x slower                                                  |
| django_template               | 24.4 ms                                                | 25.2 ms: 1.03x slower                                                 |
| genshi_xml                    | 35.1 ms                                                | 36.4 ms: 1.04x slower                                                 |
| dask                          | 789 ms                                                 | 847 ms: 1.07x slower                                                  |
| xml_etree_generate            | 53.9 ms                                                | 58.3 ms: 1.08x slower                                                 |
| sqlite_synth                  | 1.48 us                                                | 1.62 us: 1.09x slower                                                 |
| python_startup_no_site        | 12.8 ms                                                | 14.0 ms: 1.10x slower                                                 |
| nqueens                       | 63.8 ms                                                | 71.4 ms: 1.12x slower                                                 |
| create_gc_cycles              | 1.16 ms                                                | 1.36 ms: 1.16x slower                                                 |
| async_generators              | 233 ms                                                 | 274 ms: 1.17x slower                                                  |
| gc_traversal                  | 2.71 ms                                                | 3.34 ms: 1.23x slower                                                 |
| telco                         | 3.49 ms                                                | 4.76 ms: 1.37x slower                                                 |
| logging_silent                | 117 ns                                                 | 343 ns: 2.93x slower                                                  |
| coverage                      | 41.2 ms                                                | 336 ms: 8.15x slower                                                  |
| thrift                        | 562 us                                                 | 44.0 ms: 78.28x slower                                                |
| Geometric mean                | (ref)                                                  | 1.14x faster                                                          |

Benchmark hidden because not significant (4): xml_etree_iterparse, shortest_path, json_loads, asyncio_websockets
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250609-3.15.0a0-b150b6a/bm-20250609-darwin-arm64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.154x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.17x