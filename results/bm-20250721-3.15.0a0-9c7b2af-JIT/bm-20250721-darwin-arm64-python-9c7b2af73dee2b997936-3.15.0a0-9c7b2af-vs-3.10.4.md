# Results vs. 3.10.4

- fork: python
- ref: 9c7b2af73dee2b997936
- machine: darwin-arm64
- commit hash: 9c7b2af
- commit date: 2025-07-21
- overall geometric mean: 1.357x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250721-darwin-arm64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 169 ms: 1.19x faster                                                  |
| docutils       | 1.74 sec                                               | 1.45 sec: 1.20x faster                                                |
| html5lib       | 43.5 ms                                                | 32.8 ms: 1.33x faster                                                 |
| sphinx         | 729 ms                                                 | 573 ms: 1.27x faster                                                  |
| Geometric mean | (ref)                                                  | 1.25x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250721-darwin-arm64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 63.9 ms: 6.14x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 140 ms: 3.44x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 361 ms: 2.81x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 380 ms: 2.68x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 194 ms: 2.48x faster                                                  |
| async_tree_none               | 391 ms                                                 | 165 ms: 2.38x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 360 ms: 1.86x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 418 ms: 1.60x faster                                                  |
| coroutines                    | 20.5 ms                                                | 16.6 ms: 1.24x faster                                                 |
| asyncio_websockets            | 242 ms                                                 | 243 ms: 1.00x slower                                                  |
| async_generators              | 233 ms                                                 | 284 ms: 1.22x slower                                                  |
| Geometric mean                | (ref)                                                  | 2.06x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250721-darwin-arm64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 51.2 ms: 1.41x faster                                                 |
| nbody          | 92.5 ms                                                | 72.4 ms: 1.28x faster                                                 |
| pidigits       | 280 ms                                                 | 280 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.22x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250721-darwin-arm64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 72.3 ms: 1.32x faster                                                 |
| regex_dna      | 175 ms                                                 | 138 ms: 1.27x faster                                                  |
| regex_v8       | 19.1 ms                                                | 15.3 ms: 1.25x faster                                                 |
| regex_effbot   | 2.34 ms                                                | 2.16 ms: 1.08x faster                                                 |
| Geometric mean | (ref)                                                  | 1.23x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250721-darwin-arm64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 127 us: 1.56x faster                                                  |
| tomli_loads          | 1.72 sec                                               | 1.22 sec: 1.41x faster                                                |
| pickle_pure_python   | 285 us                                                 | 206 us: 1.38x faster                                                  |
| xml_etree_process    | 44.6 ms                                                | 34.3 ms: 1.30x faster                                                 |
| json_dumps           | 8.31 ms                                                | 6.55 ms: 1.27x faster                                                 |
| xml_etree_generate   | 53.9 ms                                                | 49.3 ms: 1.09x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 104 ms: 1.06x faster                                                  |
| xml_etree_iterparse  | 74.5 ms                                                | 72.6 ms: 1.03x faster                                                 |
| json_loads           | 16.6 us                                                | 17.0 us: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.22x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250721-darwin-arm64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 17.2 ms: 1.14x faster                                                 |
| python_startup_no_site | 12.8 ms                                                | 12.9 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250721-darwin-arm64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 6.57 ms: 1.49x faster                                                 |
| genshi_text     | 17.7 ms                                                | 15.3 ms: 1.16x faster                                                 |
| genshi_xml      | 35.1 ms                                                | 33.0 ms: 1.06x faster                                                 |
| django_template | 24.4 ms                                                | 23.0 ms: 1.06x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.18x faster                                                          |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250721-darwin-arm64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 63.9 ms: 6.14x faster                                                 |
| typing_runtime_protocols      | 326 us                                                 | 94.1 us: 3.47x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 140 ms: 3.44x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 361 ms: 2.81x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 380 ms: 2.68x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 194 ms: 2.48x faster                                                  |
| async_tree_none               | 391 ms                                                 | 165 ms: 2.38x faster                                                  |
| mdp                           | 1.65 sec                                               | 744 ms: 2.22x faster                                                  |
| deltablue                     | 4.99 ms                                                | 2.40 ms: 2.08x faster                                                 |
| raytrace                      | 327 ms                                                 | 172 ms: 1.90x faster                                                  |
| go                            | 163 ms                                                 | 86.0 ms: 1.90x faster                                                 |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 360 ms: 1.86x faster                                                  |
| chaos                         | 67.7 ms                                                | 38.4 ms: 1.76x faster                                                 |
| scimark_sor                   | 140 ms                                                 | 83.2 ms: 1.68x faster                                                 |
| richards_super                | 61.0 ms                                                | 37.4 ms: 1.63x faster                                                 |
| deepcopy_memo                 | 34.7 us                                                | 21.5 us: 1.61x faster                                                 |
| deepcopy                      | 276 us                                                 | 172 us: 1.61x faster                                                  |
| scimark_monte_carlo           | 72.4 ms                                                | 45.2 ms: 1.60x faster                                                 |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 418 ms: 1.60x faster                                                  |
| logging_silent                | 117 ns                                                 | 73.3 ns: 1.60x faster                                                 |
| pyflate                       | 448 ms                                                 | 283 ms: 1.58x faster                                                  |
| subparsers                    | 39.8 ms                                                | 25.4 ms: 1.57x faster                                                 |
| richards                      | 52.3 ms                                                | 33.3 ms: 1.57x faster                                                 |
| unpickle_pure_python          | 198 us                                                 | 127 us: 1.56x faster                                                  |
| comprehensions                | 17.3 us                                                | 11.2 us: 1.55x faster                                                 |
| spectral_norm                 | 95.3 ms                                                | 63.4 ms: 1.50x faster                                                 |
| mako                          | 9.81 ms                                                | 6.57 ms: 1.49x faster                                                 |
| crypto_pyaes                  | 73.3 ms                                                | 49.6 ms: 1.48x faster                                                 |
| pylint                        | 231 ms                                                 | 161 ms: 1.43x faster                                                  |
| pprint_pformat                | 1.33 sec                                               | 931 ms: 1.43x faster                                                  |
| dulwich_log                   | 35.6 ms                                                | 25.0 ms: 1.42x faster                                                 |
| pprint_safe_repr              | 648 ms                                                 | 457 ms: 1.42x faster                                                  |
| float                         | 72.4 ms                                                | 51.2 ms: 1.41x faster                                                 |
| tomli_loads                   | 1.72 sec                                               | 1.22 sec: 1.41x faster                                                |
| logging_format                | 5.03 us                                                | 3.64 us: 1.38x faster                                                 |
| pickle_pure_python            | 285 us                                                 | 206 us: 1.38x faster                                                  |
| hexiom                        | 6.25 ms                                                | 4.53 ms: 1.38x faster                                                 |
| scimark_lu                    | 103 ms                                                 | 74.9 ms: 1.37x faster                                                 |
| logging_simple                | 4.59 us                                                | 3.36 us: 1.37x faster                                                 |
| html5lib                      | 43.5 ms                                                | 32.8 ms: 1.33x faster                                                 |
| regex_compile                 | 95.6 ms                                                | 72.3 ms: 1.32x faster                                                 |
| deepcopy_reduce               | 2.32 us                                                | 1.78 us: 1.30x faster                                                 |
| xml_etree_process             | 44.6 ms                                                | 34.3 ms: 1.30x faster                                                 |
| generators                    | 31.7 ms                                                | 24.5 ms: 1.29x faster                                                 |
| pycparser                     | 887 ms                                                 | 693 ms: 1.28x faster                                                  |
| nbody                         | 92.5 ms                                                | 72.4 ms: 1.28x faster                                                 |
| sphinx                        | 729 ms                                                 | 573 ms: 1.27x faster                                                  |
| json_dumps                    | 8.31 ms                                                | 6.55 ms: 1.27x faster                                                 |
| k_core                        | 2.01 sec                                               | 1.59 sec: 1.27x faster                                                |
| regex_dna                     | 175 ms                                                 | 138 ms: 1.27x faster                                                  |
| thrift                        | 562 us                                                 | 448 us: 1.26x faster                                                  |
| regex_v8                      | 19.1 ms                                                | 15.3 ms: 1.25x faster                                                 |
| coroutines                    | 20.5 ms                                                | 16.6 ms: 1.24x faster                                                 |
| fannkuch                      | 303 ms                                                 | 249 ms: 1.21x faster                                                  |
| sympy_sum                     | 92.7 ms                                                | 76.6 ms: 1.21x faster                                                 |
| sympy_integrate               | 13.2 ms                                                | 10.9 ms: 1.20x faster                                                 |
| docutils                      | 1.74 sec                                               | 1.45 sec: 1.20x faster                                                |
| scimark_fft                   | 225 ms                                                 | 188 ms: 1.20x faster                                                  |
| 2to3                          | 201 ms                                                 | 169 ms: 1.19x faster                                                  |
| bpe_tokeniser                 | 3.44 sec                                               | 2.90 sec: 1.18x faster                                                |
| genshi_text                   | 17.7 ms                                                | 15.3 ms: 1.16x faster                                                 |
| sympy_str                     | 166 ms                                                 | 144 ms: 1.15x faster                                                  |
| python_startup                | 19.6 ms                                                | 17.2 ms: 1.14x faster                                                 |
| pathlib                       | 25.7 ms                                                | 22.7 ms: 1.13x faster                                                 |
| sympy_expand                  | 269 ms                                                 | 245 ms: 1.10x faster                                                  |
| xml_etree_generate            | 53.9 ms                                                | 49.3 ms: 1.09x faster                                                 |
| meteor_contest                | 77.8 ms                                                | 71.8 ms: 1.08x faster                                                 |
| regex_effbot                  | 2.34 ms                                                | 2.16 ms: 1.08x faster                                                 |
| genshi_xml                    | 35.1 ms                                                | 33.0 ms: 1.06x faster                                                 |
| django_template               | 24.4 ms                                                | 23.0 ms: 1.06x faster                                                 |
| xml_etree_parse               | 109 ms                                                 | 104 ms: 1.06x faster                                                  |
| nqueens                       | 63.8 ms                                                | 61.0 ms: 1.05x faster                                                 |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.30 ms: 1.04x faster                                                 |
| json                          | 3.10 ms                                                | 3.00 ms: 1.03x faster                                                 |
| dask                          | 789 ms                                                 | 770 ms: 1.03x faster                                                  |
| xml_etree_iterparse           | 74.5 ms                                                | 72.6 ms: 1.03x faster                                                 |
| pidigits                      | 280 ms                                                 | 280 ms: 1.00x faster                                                  |
| asyncio_websockets            | 242 ms                                                 | 243 ms: 1.00x slower                                                  |
| python_startup_no_site        | 12.8 ms                                                | 12.9 ms: 1.01x slower                                                 |
| connected_components          | 318 ms                                                 | 322 ms: 1.01x slower                                                  |
| json_loads                    | 16.6 us                                                | 17.0 us: 1.02x slower                                                 |
| shortest_path                 | 328 ms                                                 | 351 ms: 1.07x slower                                                  |
| sqlite_synth                  | 1.48 us                                                | 1.60 us: 1.08x slower                                                 |
| coverage                      | 41.2 ms                                                | 47.4 ms: 1.15x slower                                                 |
| create_gc_cycles              | 1.16 ms                                                | 1.36 ms: 1.17x slower                                                 |
| gc_traversal                  | 2.71 ms                                                | 3.19 ms: 1.18x slower                                                 |
| async_generators              | 233 ms                                                 | 284 ms: 1.22x slower                                                  |
| many_optionals                | 486 us                                                 | 593 us: 1.22x slower                                                  |
| telco                         | 3.49 ms                                                | 4.39 ms: 1.26x slower                                                 |
| Geometric mean                | (ref)                                                  | 1.36x faster                                                          |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250721-3.15.0a0-9c7b2af-JIT/bm-20250721-darwin-arm64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.357x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.19x