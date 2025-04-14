# Results vs. 3.10.4

- fork: python
- ref: 295b53df2aa18deb625a
- machine: darwin-arm64
- commit hash: 295b53d
- commit date: 2025-03-18
- overall geometric mean: 1.315x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-darwin-arm64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 171 ms: 1.18x faster                                                   |
| docutils       | 1.74 sec                                               | 1.49 sec: 1.17x faster                                                 |
| html5lib       | 43.5 ms                                                | 32.4 ms: 1.35x faster                                                  |
| sphinx         | 729 ms                                                 | 598 ms: 1.22x faster                                                   |
| Geometric mean | (ref)                                                  | 1.22x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-darwin-arm64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 66.3 ms: 5.91x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 148 ms: 3.26x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 378 ms: 2.68x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 393 ms: 2.59x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 206 ms: 2.33x faster                                                   |
| async_tree_none               | 391 ms                                                 | 169 ms: 2.32x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 363 ms: 1.84x faster                                                   |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 419 ms: 1.59x faster                                                   |
| coroutines                    | 20.5 ms                                                | 17.3 ms: 1.18x faster                                                  |
| async_generators              | 233 ms                                                 | 288 ms: 1.23x slower                                                   |
| Geometric mean                | (ref)                                                  | 2.00x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-darwin-arm64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 46.1 ms: 1.57x faster                                                  |
| nbody          | 92.5 ms                                                | 69.7 ms: 1.33x faster                                                  |
| pidigits       | 280 ms                                                 | 283 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.27x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-darwin-arm64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 74.0 ms: 1.29x faster                                                  |
| regex_dna      | 175 ms                                                 | 140 ms: 1.25x faster                                                   |
| regex_v8       | 19.1 ms                                                | 15.8 ms: 1.21x faster                                                  |
| regex_effbot   | 2.34 ms                                                | 2.25 ms: 1.04x faster                                                  |
| Geometric mean | (ref)                                                  | 1.19x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-darwin-arm64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 143 us: 1.39x faster                                                   |
| tomli_loads          | 1.72 sec                                               | 1.27 sec: 1.35x faster                                                 |
| pickle_pure_python   | 285 us                                                 | 213 us: 1.34x faster                                                   |
| xml_etree_process    | 44.6 ms                                                | 36.9 ms: 1.21x faster                                                  |
| json_dumps           | 8.31 ms                                                | 7.56 ms: 1.10x faster                                                  |
| xml_etree_parse      | 109 ms                                                 | 103 ms: 1.06x faster                                                   |
| xml_etree_generate   | 53.9 ms                                                | 51.9 ms: 1.04x faster                                                  |
| xml_etree_iterparse  | 74.5 ms                                                | 73.1 ms: 1.02x faster                                                  |
| json_loads           | 16.6 us                                                | 18.0 us: 1.08x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-darwin-arm64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 17.6 ms: 1.12x faster                                                  |
| python_startup_no_site | 12.8 ms                                                | 13.3 ms: 1.04x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-darwin-arm64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 6.72 ms: 1.46x faster                                                  |
| genshi_text     | 17.7 ms                                                | 15.4 ms: 1.15x faster                                                  |
| genshi_xml      | 35.1 ms                                                | 32.0 ms: 1.10x faster                                                  |
| django_template | 24.4 ms                                                | 22.6 ms: 1.08x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.19x faster                                                           |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-darwin-arm64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 66.3 ms: 5.91x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 99.2 us: 3.29x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 148 ms: 3.26x faster                                                   |
| subparsers                    | 39.8 ms                                                | 12.8 ms: 3.11x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 378 ms: 2.68x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 393 ms: 2.59x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 206 ms: 2.33x faster                                                   |
| async_tree_none               | 391 ms                                                 | 169 ms: 2.32x faster                                                   |
| deltablue                     | 4.99 ms                                                | 2.24 ms: 2.22x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 363 ms: 1.84x faster                                                   |
| richards_super                | 61.0 ms                                                | 35.0 ms: 1.74x faster                                                  |
| raytrace                      | 327 ms                                                 | 193 ms: 1.69x faster                                                   |
| deepcopy                      | 276 us                                                 | 163 us: 1.69x faster                                                   |
| richards                      | 52.3 ms                                                | 31.3 ms: 1.67x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 20.9 us: 1.66x faster                                                  |
| go                            | 163 ms                                                 | 100 ms: 1.63x faster                                                   |
| logging_silent                | 117 ns                                                 | 72.4 ns: 1.62x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 419 ms: 1.59x faster                                                   |
| scimark_sor                   | 140 ms                                                 | 89.1 ms: 1.57x faster                                                  |
| float                         | 72.4 ms                                                | 46.1 ms: 1.57x faster                                                  |
| scimark_monte_carlo           | 72.4 ms                                                | 46.5 ms: 1.56x faster                                                  |
| chaos                         | 67.7 ms                                                | 44.5 ms: 1.52x faster                                                  |
| spectral_norm                 | 95.3 ms                                                | 65.3 ms: 1.46x faster                                                  |
| mako                          | 9.81 ms                                                | 6.72 ms: 1.46x faster                                                  |
| pyflate                       | 448 ms                                                 | 323 ms: 1.39x faster                                                   |
| unpickle_pure_python          | 198 us                                                 | 143 us: 1.39x faster                                                   |
| comprehensions                | 17.3 us                                                | 12.7 us: 1.37x faster                                                  |
| pylint                        | 231 ms                                                 | 170 ms: 1.36x faster                                                   |
| dulwich_log                   | 35.6 ms                                                | 26.2 ms: 1.36x faster                                                  |
| tomli_loads                   | 1.72 sec                                               | 1.27 sec: 1.35x faster                                                 |
| deepcopy_reduce               | 2.32 us                                                | 1.72 us: 1.35x faster                                                  |
| html5lib                      | 43.5 ms                                                | 32.4 ms: 1.35x faster                                                  |
| pickle_pure_python            | 285 us                                                 | 213 us: 1.34x faster                                                   |
| nbody                         | 92.5 ms                                                | 69.7 ms: 1.33x faster                                                  |
| k_core                        | 2.01 sec                                               | 1.55 sec: 1.30x faster                                                 |
| regex_compile                 | 95.6 ms                                                | 74.0 ms: 1.29x faster                                                  |
| scimark_lu                    | 103 ms                                                 | 79.7 ms: 1.29x faster                                                  |
| sqlalchemy_imperative         | 9.07 ms                                                | 7.05 ms: 1.29x faster                                                  |
| logging_format                | 5.03 us                                                | 3.92 us: 1.28x faster                                                  |
| logging_simple                | 4.59 us                                                | 3.59 us: 1.28x faster                                                  |
| generators                    | 31.7 ms                                                | 25.0 ms: 1.27x faster                                                  |
| pprint_pformat                | 1.33 sec                                               | 1.06 sec: 1.25x faster                                                 |
| regex_dna                     | 175 ms                                                 | 140 ms: 1.25x faster                                                   |
| hexiom                        | 6.25 ms                                                | 5.03 ms: 1.24x faster                                                  |
| pycparser                     | 887 ms                                                 | 715 ms: 1.24x faster                                                   |
| sqlalchemy_declarative        | 75.7 ms                                                | 61.4 ms: 1.23x faster                                                  |
| pprint_safe_repr              | 648 ms                                                 | 527 ms: 1.23x faster                                                   |
| thrift                        | 562 us                                                 | 461 us: 1.22x faster                                                   |
| sphinx                        | 729 ms                                                 | 598 ms: 1.22x faster                                                   |
| regex_v8                      | 19.1 ms                                                | 15.8 ms: 1.21x faster                                                  |
| xml_etree_process             | 44.6 ms                                                | 36.9 ms: 1.21x faster                                                  |
| crypto_pyaes                  | 73.3 ms                                                | 60.7 ms: 1.21x faster                                                  |
| sympy_sum                     | 92.7 ms                                                | 76.9 ms: 1.21x faster                                                  |
| coroutines                    | 20.5 ms                                                | 17.3 ms: 1.18x faster                                                  |
| 2to3                          | 201 ms                                                 | 171 ms: 1.18x faster                                                   |
| docutils                      | 1.74 sec                                               | 1.49 sec: 1.17x faster                                                 |
| scimark_fft                   | 225 ms                                                 | 193 ms: 1.17x faster                                                   |
| genshi_text                   | 17.7 ms                                                | 15.4 ms: 1.15x faster                                                  |
| sympy_str                     | 166 ms                                                 | 148 ms: 1.12x faster                                                   |
| bpe_tokeniser                 | 3.44 sec                                               | 3.07 sec: 1.12x faster                                                 |
| python_startup                | 19.6 ms                                                | 17.6 ms: 1.12x faster                                                  |
| mdp                           | 1.65 sec                                               | 1.49 sec: 1.11x faster                                                 |
| json_dumps                    | 8.31 ms                                                | 7.56 ms: 1.10x faster                                                  |
| genshi_xml                    | 35.1 ms                                                | 32.0 ms: 1.10x faster                                                  |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.11 ms: 1.10x faster                                                  |
| sympy_integrate               | 13.2 ms                                                | 12.0 ms: 1.09x faster                                                  |
| django_template               | 24.4 ms                                                | 22.6 ms: 1.08x faster                                                  |
| bench_thread_pool             | 545 us                                                 | 507 us: 1.08x faster                                                   |
| pathlib                       | 25.7 ms                                                | 24.0 ms: 1.07x faster                                                  |
| sympy_expand                  | 269 ms                                                 | 251 ms: 1.07x faster                                                   |
| xml_etree_parse               | 109 ms                                                 | 103 ms: 1.06x faster                                                   |
| connected_components          | 318 ms                                                 | 305 ms: 1.05x faster                                                   |
| xml_etree_generate            | 53.9 ms                                                | 51.9 ms: 1.04x faster                                                  |
| regex_effbot                  | 2.34 ms                                                | 2.25 ms: 1.04x faster                                                  |
| fannkuch                      | 303 ms                                                 | 294 ms: 1.03x faster                                                   |
| many_optionals                | 486 us                                                 | 473 us: 1.03x faster                                                   |
| dask                          | 789 ms                                                 | 768 ms: 1.03x faster                                                   |
| meteor_contest                | 77.8 ms                                                | 76.0 ms: 1.02x faster                                                  |
| xml_etree_iterparse           | 74.5 ms                                                | 73.1 ms: 1.02x faster                                                  |
| pidigits                      | 280 ms                                                 | 283 ms: 1.01x slower                                                   |
| json                          | 3.10 ms                                                | 3.15 ms: 1.02x slower                                                  |
| shortest_path                 | 328 ms                                                 | 335 ms: 1.02x slower                                                   |
| nqueens                       | 63.8 ms                                                | 66.0 ms: 1.03x slower                                                  |
| python_startup_no_site        | 12.8 ms                                                | 13.3 ms: 1.04x slower                                                  |
| sqlite_synth                  | 1.48 us                                                | 1.56 us: 1.05x slower                                                  |
| json_loads                    | 16.6 us                                                | 18.0 us: 1.08x slower                                                  |
| bench_mp_pool                 | 56.0 ms                                                | 61.0 ms: 1.09x slower                                                  |
| create_gc_cycles              | 1.16 ms                                                | 1.30 ms: 1.12x slower                                                  |
| coverage                      | 41.2 ms                                                | 46.8 ms: 1.14x slower                                                  |
| gc_traversal                  | 2.71 ms                                                | 3.13 ms: 1.16x slower                                                  |
| async_generators              | 233 ms                                                 | 288 ms: 1.23x slower                                                   |
| telco                         | 3.49 ms                                                | 4.58 ms: 1.31x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.31x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250318-3.14.0a6+-295b53d-JIT/bm-20250318-darwin-arm64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.315x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: 1.16x