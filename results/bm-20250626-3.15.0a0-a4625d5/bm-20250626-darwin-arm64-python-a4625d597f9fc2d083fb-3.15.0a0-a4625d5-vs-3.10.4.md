# Results vs. 3.10.4

- fork: python
- ref: a4625d597f9fc2d083fb
- machine: darwin-arm64
- commit hash: a4625d5
- commit date: 2025-06-26
- overall geometric mean: 1.233x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-darwin-arm64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 187 ms: 1.08x faster                                                  |
| docutils       | 1.74 sec                                               | 1.53 sec: 1.14x faster                                                |
| html5lib       | 43.5 ms                                                | 104 ms: 2.40x slower                                                  |
| sphinx         | 729 ms                                                 | 618 ms: 1.18x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-darwin-arm64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 73.0 ms: 5.37x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 150 ms: 3.23x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 391 ms: 2.59x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 409 ms: 2.49x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 217 ms: 2.21x faster                                                  |
| async_tree_none               | 391 ms                                                 | 180 ms: 2.18x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 367 ms: 1.82x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 436 ms: 1.53x faster                                                  |
| coroutines                    | 20.5 ms                                                | 18.7 ms: 1.09x faster                                                 |
| async_generators              | 233 ms                                                 | 277 ms: 1.19x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.93x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-darwin-arm64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 57.1 ms: 1.27x faster                                                 |
| nbody          | 92.5 ms                                                | 85.2 ms: 1.09x faster                                                 |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-darwin-arm64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 175 ms                                                 | 143 ms: 1.22x faster                                                  |
| regex_v8       | 19.1 ms                                                | 16.2 ms: 1.18x faster                                                 |
| regex_compile  | 95.6 ms                                                | 81.0 ms: 1.18x faster                                                 |
| regex_effbot   | 2.34 ms                                                | 2.37 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.14x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-darwin-arm64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 8.31 ms                                                | 6.82 ms: 1.22x faster                                                 |
| tomli_loads          | 1.72 sec                                               | 1.43 sec: 1.20x faster                                                |
| pickle_pure_python   | 285 us                                                 | 241 us: 1.18x faster                                                  |
| unpickle_pure_python | 198 us                                                 | 177 us: 1.12x faster                                                  |
| xml_etree_parse      | 109 ms                                                 | 104 ms: 1.05x faster                                                  |
| xml_etree_process    | 44.6 ms                                                | 43.4 ms: 1.03x faster                                                 |
| xml_etree_generate   | 53.9 ms                                                | 58.8 ms: 1.09x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                          |

Benchmark hidden because not significant (2): xml_etree_iterparse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-darwin-arm64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 17.8 ms: 1.10x faster                                                 |
| python_startup_no_site | 12.8 ms                                                | 13.3 ms: 1.04x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-darwin-arm64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 9.02 ms: 1.09x faster                                                 |
| genshi_text     | 17.7 ms                                                | 18.6 ms: 1.05x slower                                                 |
| genshi_xml      | 35.1 ms                                                | 37.2 ms: 1.06x slower                                                 |
| django_template | 24.4 ms                                                | 26.4 ms: 1.08x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                          |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-darwin-arm64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 73.0 ms: 5.37x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 150 ms: 3.23x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 105 us: 3.10x faster                                                  |
| subparsers                    | 39.8 ms                                                | 14.8 ms: 2.69x faster                                                 |
| async_tree_eager_io           | 1.01 sec                                               | 391 ms: 2.59x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 409 ms: 2.49x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 217 ms: 2.21x faster                                                  |
| async_tree_none               | 391 ms                                                 | 180 ms: 2.18x faster                                                  |
| mdp                           | 1.65 sec                                               | 817 ms: 2.02x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 367 ms: 1.82x faster                                                  |
| deltablue                     | 4.99 ms                                                | 2.74 ms: 1.82x faster                                                 |
| go                            | 163 ms                                                 | 99.6 ms: 1.64x faster                                                 |
| deepcopy                      | 276 us                                                 | 175 us: 1.58x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 22.0 us: 1.58x faster                                                 |
| raytrace                      | 327 ms                                                 | 210 ms: 1.56x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 436 ms: 1.53x faster                                                  |
| logging_silent                | 117 ns                                                 | 77.0 ns: 1.52x faster                                                 |
| scimark_sor                   | 140 ms                                                 | 92.6 ms: 1.51x faster                                                 |
| chaos                         | 67.7 ms                                                | 46.9 ms: 1.44x faster                                                 |
| richards                      | 52.3 ms                                                | 37.9 ms: 1.38x faster                                                 |
| k_core                        | 2.01 sec                                               | 1.47 sec: 1.37x faster                                                |
| pylint                        | 231 ms                                                 | 169 ms: 1.37x faster                                                  |
| richards_super                | 61.0 ms                                                | 44.8 ms: 1.36x faster                                                 |
| pyflate                       | 448 ms                                                 | 334 ms: 1.34x faster                                                  |
| dulwich_log                   | 35.6 ms                                                | 26.5 ms: 1.34x faster                                                 |
| scimark_monte_carlo           | 72.4 ms                                                | 54.7 ms: 1.32x faster                                                 |
| spectral_norm                 | 95.3 ms                                                | 72.3 ms: 1.32x faster                                                 |
| comprehensions                | 17.3 us                                                | 13.2 us: 1.31x faster                                                 |
| float                         | 72.4 ms                                                | 57.1 ms: 1.27x faster                                                 |
| hexiom                        | 6.25 ms                                                | 5.09 ms: 1.23x faster                                                 |
| deepcopy_reduce               | 2.32 us                                                | 1.89 us: 1.23x faster                                                 |
| regex_dna                     | 175 ms                                                 | 143 ms: 1.22x faster                                                  |
| json_dumps                    | 8.31 ms                                                | 6.82 ms: 1.22x faster                                                 |
| tomli_loads                   | 1.72 sec                                               | 1.43 sec: 1.20x faster                                                |
| crypto_pyaes                  | 73.3 ms                                                | 61.0 ms: 1.20x faster                                                 |
| thrift                        | 562 us                                                 | 470 us: 1.20x faster                                                  |
| pycparser                     | 887 ms                                                 | 742 ms: 1.20x faster                                                  |
| scimark_lu                    | 103 ms                                                 | 85.8 ms: 1.19x faster                                                 |
| regex_v8                      | 19.1 ms                                                | 16.2 ms: 1.18x faster                                                 |
| logging_format                | 5.03 us                                                | 4.26 us: 1.18x faster                                                 |
| pickle_pure_python            | 285 us                                                 | 241 us: 1.18x faster                                                  |
| sphinx                        | 729 ms                                                 | 618 ms: 1.18x faster                                                  |
| regex_compile                 | 95.6 ms                                                | 81.0 ms: 1.18x faster                                                 |
| sympy_integrate               | 13.2 ms                                                | 11.3 ms: 1.17x faster                                                 |
| logging_simple                | 4.59 us                                                | 3.95 us: 1.16x faster                                                 |
| sympy_sum                     | 92.7 ms                                                | 80.6 ms: 1.15x faster                                                 |
| pathlib                       | 25.7 ms                                                | 22.6 ms: 1.14x faster                                                 |
| docutils                      | 1.74 sec                                               | 1.53 sec: 1.14x faster                                                |
| unpickle_pure_python          | 198 us                                                 | 177 us: 1.12x faster                                                  |
| pprint_pformat                | 1.33 sec                                               | 1.19 sec: 1.12x faster                                                |
| pprint_safe_repr              | 648 ms                                                 | 583 ms: 1.11x faster                                                  |
| python_startup                | 19.6 ms                                                | 17.8 ms: 1.10x faster                                                 |
| coroutines                    | 20.5 ms                                                | 18.7 ms: 1.09x faster                                                 |
| mako                          | 9.81 ms                                                | 9.02 ms: 1.09x faster                                                 |
| nbody                         | 92.5 ms                                                | 85.2 ms: 1.09x faster                                                 |
| scimark_fft                   | 225 ms                                                 | 208 ms: 1.08x faster                                                  |
| 2to3                          | 201 ms                                                 | 187 ms: 1.08x faster                                                  |
| sympy_str                     | 166 ms                                                 | 154 ms: 1.07x faster                                                  |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.21 ms: 1.07x faster                                                 |
| bpe_tokeniser                 | 3.44 sec                                               | 3.23 sec: 1.06x faster                                                |
| json                          | 3.10 ms                                                | 2.95 ms: 1.05x faster                                                 |
| xml_etree_parse               | 109 ms                                                 | 104 ms: 1.05x faster                                                  |
| meteor_contest                | 77.8 ms                                                | 74.4 ms: 1.05x faster                                                 |
| connected_components          | 318 ms                                                 | 305 ms: 1.05x faster                                                  |
| fannkuch                      | 303 ms                                                 | 290 ms: 1.04x faster                                                  |
| sympy_expand                  | 269 ms                                                 | 259 ms: 1.04x faster                                                  |
| xml_etree_process             | 44.6 ms                                                | 43.4 ms: 1.03x faster                                                 |
| dask                          | 789 ms                                                 | 771 ms: 1.02x faster                                                  |
| generators                    | 31.7 ms                                                | 31.5 ms: 1.01x faster                                                 |
| shortest_path                 | 328 ms                                                 | 329 ms: 1.00x slower                                                  |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                                  |
| regex_effbot                  | 2.34 ms                                                | 2.37 ms: 1.01x slower                                                 |
| many_optionals                | 486 us                                                 | 493 us: 1.01x slower                                                  |
| python_startup_no_site        | 12.8 ms                                                | 13.3 ms: 1.04x slower                                                 |
| genshi_text                   | 17.7 ms                                                | 18.6 ms: 1.05x slower                                                 |
| genshi_xml                    | 35.1 ms                                                | 37.2 ms: 1.06x slower                                                 |
| django_template               | 24.4 ms                                                | 26.4 ms: 1.08x slower                                                 |
| xml_etree_generate            | 53.9 ms                                                | 58.8 ms: 1.09x slower                                                 |
| sqlite_synth                  | 1.48 us                                                | 1.64 us: 1.11x slower                                                 |
| nqueens                       | 63.8 ms                                                | 71.3 ms: 1.12x slower                                                 |
| create_gc_cycles              | 1.16 ms                                                | 1.35 ms: 1.16x slower                                                 |
| gc_traversal                  | 2.71 ms                                                | 3.18 ms: 1.18x slower                                                 |
| async_generators              | 233 ms                                                 | 277 ms: 1.19x slower                                                  |
| coverage                      | 41.2 ms                                                | 49.7 ms: 1.21x slower                                                 |
| telco                         | 3.49 ms                                                | 4.79 ms: 1.37x slower                                                 |
| html5lib                      | 43.5 ms                                                | 104 ms: 2.40x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.24x faster                                                          |

Benchmark hidden because not significant (3): xml_etree_iterparse, json_loads, asyncio_websockets
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250626-3.15.0a0-a4625d5/bm-20250626-darwin-arm64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.233x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: 1.16x