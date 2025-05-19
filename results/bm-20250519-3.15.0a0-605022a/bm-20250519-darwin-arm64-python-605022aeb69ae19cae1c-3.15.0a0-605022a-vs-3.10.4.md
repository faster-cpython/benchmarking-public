# Results vs. 3.10.4

- fork: python
- ref: 605022aeb69ae19cae1c
- machine: darwin-arm64
- commit hash: 605022a
- commit date: 2025-05-19
- overall geometric mean: 1.124x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250519-darwin-arm64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 193 ms: 1.04x faster                                                  |
| docutils       | 1.74 sec                                               | 1.57 sec: 1.11x faster                                                |
| html5lib       | 43.5 ms                                                | 35.2 ms: 1.24x faster                                                 |
| sphinx         | 729 ms                                                 | 637 ms: 1.14x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250519-darwin-arm64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 77.6 ms: 5.05x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 155 ms: 3.11x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 407 ms: 2.49x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 425 ms: 2.39x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 222 ms: 2.17x faster                                                  |
| async_tree_none               | 391 ms                                                 | 186 ms: 2.11x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 372 ms: 1.80x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 440 ms: 1.52x faster                                                  |
| coroutines                    | 20.5 ms                                                | 19.7 ms: 1.04x faster                                                 |
| async_generators              | 233 ms                                                 | 274 ms: 1.18x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.88x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250519-darwin-arm64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 58.9 ms: 1.23x faster                                                 |
| nbody          | 92.5 ms                                                | 91.7 ms: 1.01x faster                                                 |
| pidigits       | 280 ms                                                 | 283 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250519-darwin-arm64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 175 ms                                                 | 137 ms: 1.27x faster                                                  |
| regex_v8       | 19.1 ms                                                | 15.8 ms: 1.21x faster                                                 |
| regex_compile  | 95.6 ms                                                | 86.7 ms: 1.10x faster                                                 |
| regex_effbot   | 2.34 ms                                                | 2.16 ms: 1.08x faster                                                 |
| Geometric mean | (ref)                                                  | 1.16x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250519-darwin-arm64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 8.31 ms                                                | 7.16 ms: 1.16x faster                                                 |
| pickle_pure_python   | 285 us                                                 | 250 us: 1.14x faster                                                  |
| tomli_loads          | 1.72 sec                                               | 1.52 sec: 1.13x faster                                                |
| unpickle_pure_python | 198 us                                                 | 189 us: 1.05x faster                                                  |
| xml_etree_parse      | 109 ms                                                 | 105 ms: 1.04x faster                                                  |
| xml_etree_process    | 44.6 ms                                                | 45.8 ms: 1.03x slower                                                 |
| xml_etree_iterparse  | 74.5 ms                                                | 77.0 ms: 1.03x slower                                                 |
| json_loads           | 16.6 us                                                | 18.3 us: 1.10x slower                                                 |
| xml_etree_generate   | 53.9 ms                                                | 61.4 ms: 1.14x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250519-darwin-arm64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 18.9 ms: 1.04x faster                                                 |
| python_startup_no_site | 12.8 ms                                                | 14.4 ms: 1.12x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.04x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250519-darwin-arm64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 9.10 ms: 1.08x faster                                                 |
| genshi_text     | 17.7 ms                                                | 18.6 ms: 1.05x slower                                                 |
| genshi_xml      | 35.1 ms                                                | 37.6 ms: 1.07x slower                                                 |
| django_template | 24.4 ms                                                | 26.6 ms: 1.09x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                          |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250519-darwin-arm64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 77.6 ms: 5.05x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 155 ms: 3.11x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 112 us: 2.90x faster                                                  |
| subparsers                    | 39.8 ms                                                | 15.2 ms: 2.62x faster                                                 |
| async_tree_eager_io           | 1.01 sec                                               | 407 ms: 2.49x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 425 ms: 2.39x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 222 ms: 2.17x faster                                                  |
| async_tree_none               | 391 ms                                                 | 186 ms: 2.11x faster                                                  |
| mdp                           | 1.65 sec                                               | 867 ms: 1.90x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 372 ms: 1.80x faster                                                  |
| deltablue                     | 4.99 ms                                                | 2.86 ms: 1.74x faster                                                 |
| raytrace                      | 327 ms                                                 | 207 ms: 1.58x faster                                                  |
| go                            | 163 ms                                                 | 105 ms: 1.55x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 440 ms: 1.52x faster                                                  |
| scimark_sor                   | 140 ms                                                 | 94.8 ms: 1.48x faster                                                 |
| deepcopy                      | 276 us                                                 | 187 us: 1.48x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 23.8 us: 1.46x faster                                                 |
| chaos                         | 67.7 ms                                                | 46.9 ms: 1.44x faster                                                 |
| richards_super                | 61.0 ms                                                | 44.0 ms: 1.38x faster                                                 |
| scimark_monte_carlo           | 72.4 ms                                                | 53.8 ms: 1.35x faster                                                 |
| richards                      | 52.3 ms                                                | 39.4 ms: 1.33x faster                                                 |
| pylint                        | 231 ms                                                 | 175 ms: 1.32x faster                                                  |
| dulwich_log                   | 35.6 ms                                                | 27.4 ms: 1.30x faster                                                 |
| k_core                        | 2.01 sec                                               | 1.57 sec: 1.28x faster                                                |
| pyflate                       | 448 ms                                                 | 350 ms: 1.28x faster                                                  |
| regex_dna                     | 175 ms                                                 | 137 ms: 1.27x faster                                                  |
| html5lib                      | 43.5 ms                                                | 35.2 ms: 1.24x faster                                                 |
| float                         | 72.4 ms                                                | 58.9 ms: 1.23x faster                                                 |
| regex_v8                      | 19.1 ms                                                | 15.8 ms: 1.21x faster                                                 |
| spectral_norm                 | 95.3 ms                                                | 78.5 ms: 1.21x faster                                                 |
| crypto_pyaes                  | 73.3 ms                                                | 61.4 ms: 1.19x faster                                                 |
| scimark_lu                    | 103 ms                                                 | 86.3 ms: 1.19x faster                                                 |
| comprehensions                | 17.3 us                                                | 14.6 us: 1.19x faster                                                 |
| deepcopy_reduce               | 2.32 us                                                | 1.99 us: 1.17x faster                                                 |
| json_dumps                    | 8.31 ms                                                | 7.16 ms: 1.16x faster                                                 |
| pycparser                     | 887 ms                                                 | 766 ms: 1.16x faster                                                  |
| sphinx                        | 729 ms                                                 | 637 ms: 1.14x faster                                                  |
| hexiom                        | 6.25 ms                                                | 5.47 ms: 1.14x faster                                                 |
| pickle_pure_python            | 285 us                                                 | 250 us: 1.14x faster                                                  |
| sympy_integrate               | 13.2 ms                                                | 11.6 ms: 1.13x faster                                                 |
| tomli_loads                   | 1.72 sec                                               | 1.52 sec: 1.13x faster                                                |
| sympy_sum                     | 92.7 ms                                                | 82.8 ms: 1.12x faster                                                 |
| pprint_pformat                | 1.33 sec                                               | 1.19 sec: 1.11x faster                                                |
| docutils                      | 1.74 sec                                               | 1.57 sec: 1.11x faster                                                |
| logging_format                | 5.03 us                                                | 4.54 us: 1.11x faster                                                 |
| regex_compile                 | 95.6 ms                                                | 86.7 ms: 1.10x faster                                                 |
| pprint_safe_repr              | 648 ms                                                 | 588 ms: 1.10x faster                                                  |
| logging_simple                | 4.59 us                                                | 4.22 us: 1.09x faster                                                 |
| regex_effbot                  | 2.34 ms                                                | 2.16 ms: 1.08x faster                                                 |
| mako                          | 9.81 ms                                                | 9.10 ms: 1.08x faster                                                 |
| scimark_fft                   | 225 ms                                                 | 209 ms: 1.08x faster                                                  |
| pathlib                       | 25.7 ms                                                | 24.2 ms: 1.06x faster                                                 |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.24 ms: 1.05x faster                                                 |
| unpickle_pure_python          | 198 us                                                 | 189 us: 1.05x faster                                                  |
| 2to3                          | 201 ms                                                 | 193 ms: 1.04x faster                                                  |
| xml_etree_parse               | 109 ms                                                 | 105 ms: 1.04x faster                                                  |
| python_startup                | 19.6 ms                                                | 18.9 ms: 1.04x faster                                                 |
| coroutines                    | 20.5 ms                                                | 19.7 ms: 1.04x faster                                                 |
| sympy_str                     | 166 ms                                                 | 160 ms: 1.04x faster                                                  |
| bpe_tokeniser                 | 3.44 sec                                               | 3.31 sec: 1.04x faster                                                |
| connected_components          | 318 ms                                                 | 313 ms: 1.02x faster                                                  |
| nbody                         | 92.5 ms                                                | 91.7 ms: 1.01x faster                                                 |
| generators                    | 31.7 ms                                                | 31.5 ms: 1.01x faster                                                 |
| fannkuch                      | 303 ms                                                 | 301 ms: 1.00x faster                                                  |
| sympy_expand                  | 269 ms                                                 | 271 ms: 1.01x slower                                                  |
| pidigits                      | 280 ms                                                 | 283 ms: 1.01x slower                                                  |
| xml_etree_process             | 44.6 ms                                                | 45.8 ms: 1.03x slower                                                 |
| xml_etree_iterparse           | 74.5 ms                                                | 77.0 ms: 1.03x slower                                                 |
| shortest_path                 | 328 ms                                                 | 341 ms: 1.04x slower                                                  |
| genshi_text                   | 17.7 ms                                                | 18.6 ms: 1.05x slower                                                 |
| many_optionals                | 486 us                                                 | 512 us: 1.05x slower                                                  |
| genshi_xml                    | 35.1 ms                                                | 37.6 ms: 1.07x slower                                                 |
| sqlite_synth                  | 1.48 us                                                | 1.59 us: 1.08x slower                                                 |
| dask                          | 789 ms                                                 | 860 ms: 1.09x slower                                                  |
| django_template               | 24.4 ms                                                | 26.6 ms: 1.09x slower                                                 |
| json_loads                    | 16.6 us                                                | 18.3 us: 1.10x slower                                                 |
| python_startup_no_site        | 12.8 ms                                                | 14.4 ms: 1.12x slower                                                 |
| xml_etree_generate            | 53.9 ms                                                | 61.4 ms: 1.14x slower                                                 |
| create_gc_cycles              | 1.16 ms                                                | 1.37 ms: 1.18x slower                                                 |
| async_generators              | 233 ms                                                 | 274 ms: 1.18x slower                                                  |
| nqueens                       | 63.8 ms                                                | 75.7 ms: 1.19x slower                                                 |
| gc_traversal                  | 2.71 ms                                                | 3.22 ms: 1.19x slower                                                 |
| bench_mp_pool                 | 56.0 ms                                                | 71.4 ms: 1.27x slower                                                 |
| telco                         | 3.49 ms                                                | 4.82 ms: 1.38x slower                                                 |
| logging_silent                | 117 ns                                                 | 344 ns: 2.94x slower                                                  |
| coverage                      | 41.2 ms                                                | 332 ms: 8.06x slower                                                  |
| thrift                        | 562 us                                                 | 43.9 ms: 78.11x slower                                                |
| Geometric mean                | (ref)                                                  | 1.10x faster                                                          |

Benchmark hidden because not significant (4): bench_thread_pool, meteor_contest, asyncio_websockets, json
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250519-3.15.0a0-605022a/bm-20250519-darwin-arm64-python-605022aeb69ae19cae1c-3.15.0a0-605022a.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.124x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.17x