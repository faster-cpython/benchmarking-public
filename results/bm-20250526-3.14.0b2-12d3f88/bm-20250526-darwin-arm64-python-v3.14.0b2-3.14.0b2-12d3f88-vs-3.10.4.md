# Results vs. 3.10.4

- fork: python
- ref: v3.14.0b2
- machine: darwin-arm64
- commit hash: 12d3f88
- commit date: 2025-05-26
- overall geometric mean: 1.230x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250526-darwin-arm64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 190 ms: 1.06x faster                                       |
| docutils       | 1.74 sec                                               | 1.53 sec: 1.14x faster                                     |
| html5lib       | 43.5 ms                                                | 34.1 ms: 1.28x faster                                      |
| sphinx         | 729 ms                                                 | 627 ms: 1.16x faster                                       |
| Geometric mean | (ref)                                                  | 1.16x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250526-darwin-arm64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 73.6 ms: 5.33x faster                                      |
| async_tree_eager_memoization  | 483 ms                                                 | 152 ms: 3.18x faster                                       |
| async_tree_eager_io           | 1.01 sec                                               | 394 ms: 2.58x faster                                       |
| async_tree_io                 | 1.02 sec                                               | 416 ms: 2.45x faster                                       |
| async_tree_memoization        | 481 ms                                                 | 216 ms: 2.23x faster                                       |
| async_tree_none               | 391 ms                                                 | 184 ms: 2.13x faster                                       |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 369 ms: 1.81x faster                                       |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 435 ms: 1.54x faster                                       |
| coroutines                    | 20.5 ms                                                | 19.3 ms: 1.06x faster                                      |
| async_generators              | 233 ms                                                 | 274 ms: 1.18x slower                                       |
| Geometric mean                | (ref)                                                  | 1.92x faster                                               |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250526-darwin-arm64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 72.4 ms                                                | 58.7 ms: 1.23x faster                                      |
| nbody          | 92.5 ms                                                | 86.7 ms: 1.07x faster                                      |
| pidigits       | 280 ms                                                 | 283 ms: 1.01x slower                                       |
| Geometric mean | (ref)                                                  | 1.09x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250526-darwin-arm64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_dna      | 175 ms                                                 | 143 ms: 1.23x faster                                       |
| regex_v8       | 19.1 ms                                                | 16.2 ms: 1.18x faster                                      |
| regex_compile  | 95.6 ms                                                | 82.4 ms: 1.16x faster                                      |
| regex_effbot   | 2.34 ms                                                | 2.34 ms: 1.00x slower                                      |
| Geometric mean | (ref)                                                  | 1.14x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250526-darwin-arm64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| json_dumps           | 8.31 ms                                                | 6.85 ms: 1.21x faster                                      |
| pickle_pure_python   | 285 us                                                 | 241 us: 1.18x faster                                       |
| tomli_loads          | 1.72 sec                                               | 1.47 sec: 1.17x faster                                     |
| unpickle_pure_python | 198 us                                                 | 177 us: 1.12x faster                                       |
| xml_etree_parse      | 109 ms                                                 | 100 ms: 1.09x faster                                       |
| xml_etree_iterparse  | 74.5 ms                                                | 70.7 ms: 1.05x faster                                      |
| xml_etree_process    | 44.6 ms                                                | 43.9 ms: 1.02x faster                                      |
| xml_etree_generate   | 53.9 ms                                                | 58.8 ms: 1.09x slower                                      |
| json_loads           | 16.6 us                                                | 18.2 us: 1.10x slower                                      |
| Geometric mean       | (ref)                                                  | 1.07x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250526-darwin-arm64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site | 12.8 ms                                                | 18.7 ms: 1.46x slower                                      |
| python_startup         | 19.6 ms                                                | 31.4 ms: 1.60x slower                                      |
| Geometric mean         | (ref)                                                  | 1.53x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250526-darwin-arm64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 9.81 ms                                                | 8.72 ms: 1.12x faster                                      |
| genshi_text     | 17.7 ms                                                | 18.1 ms: 1.02x slower                                      |
| django_template | 24.4 ms                                                | 25.6 ms: 1.05x slower                                      |
| genshi_xml      | 35.1 ms                                                | 37.0 ms: 1.05x slower                                      |
| Geometric mean  | (ref)                                                  | 1.00x slower                                               |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250526-darwin-arm64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 73.6 ms: 5.33x faster                                      |
| async_tree_eager_memoization  | 483 ms                                                 | 152 ms: 3.18x faster                                       |
| typing_runtime_protocols      | 326 us                                                 | 115 us: 2.84x faster                                       |
| subparsers                    | 39.8 ms                                                | 15.0 ms: 2.66x faster                                      |
| async_tree_eager_io           | 1.01 sec                                               | 394 ms: 2.58x faster                                       |
| async_tree_io                 | 1.02 sec                                               | 416 ms: 2.45x faster                                       |
| async_tree_memoization        | 481 ms                                                 | 216 ms: 2.23x faster                                       |
| async_tree_none               | 391 ms                                                 | 184 ms: 2.13x faster                                       |
| mdp                           | 1.65 sec                                               | 852 ms: 1.94x faster                                       |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 369 ms: 1.81x faster                                       |
| deltablue                     | 4.99 ms                                                | 2.78 ms: 1.79x faster                                      |
| go                            | 163 ms                                                 | 103 ms: 1.59x faster                                       |
| deepcopy_memo                 | 34.7 us                                                | 22.5 us: 1.54x faster                                      |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 435 ms: 1.54x faster                                       |
| raytrace                      | 327 ms                                                 | 213 ms: 1.54x faster                                       |
| deepcopy                      | 276 us                                                 | 180 us: 1.54x faster                                       |
| scimark_sor                   | 140 ms                                                 | 92.8 ms: 1.51x faster                                      |
| richards_super                | 61.0 ms                                                | 41.9 ms: 1.46x faster                                      |
| chaos                         | 67.7 ms                                                | 48.3 ms: 1.40x faster                                      |
| richards                      | 52.3 ms                                                | 37.5 ms: 1.39x faster                                      |
| k_core                        | 2.01 sec                                               | 1.47 sec: 1.37x faster                                     |
| scimark_monte_carlo           | 72.4 ms                                                | 53.8 ms: 1.35x faster                                      |
| pylint                        | 231 ms                                                 | 172 ms: 1.34x faster                                       |
| dulwich_log                   | 35.6 ms                                                | 26.8 ms: 1.33x faster                                      |
| pyflate                       | 448 ms                                                 | 342 ms: 1.31x faster                                       |
| pathlib                       | 25.7 ms                                                | 19.7 ms: 1.30x faster                                      |
| html5lib                      | 43.5 ms                                                | 34.1 ms: 1.28x faster                                      |
| spectral_norm                 | 95.3 ms                                                | 77.0 ms: 1.24x faster                                      |
| float                         | 72.4 ms                                                | 58.7 ms: 1.23x faster                                      |
| comprehensions                | 17.3 us                                                | 14.0 us: 1.23x faster                                      |
| scimark_lu                    | 103 ms                                                 | 83.6 ms: 1.23x faster                                      |
| sqlalchemy_imperative         | 9.07 ms                                                | 7.39 ms: 1.23x faster                                      |
| regex_dna                     | 175 ms                                                 | 143 ms: 1.23x faster                                       |
| json_dumps                    | 8.31 ms                                                | 6.85 ms: 1.21x faster                                      |
| hexiom                        | 6.25 ms                                                | 5.17 ms: 1.21x faster                                      |
| deepcopy_reduce               | 2.32 us                                                | 1.93 us: 1.20x faster                                      |
| crypto_pyaes                  | 73.3 ms                                                | 61.5 ms: 1.19x faster                                      |
| pycparser                     | 887 ms                                                 | 745 ms: 1.19x faster                                       |
| regex_v8                      | 19.1 ms                                                | 16.2 ms: 1.18x faster                                      |
| pickle_pure_python            | 285 us                                                 | 241 us: 1.18x faster                                       |
| tomli_loads                   | 1.72 sec                                               | 1.47 sec: 1.17x faster                                     |
| sphinx                        | 729 ms                                                 | 627 ms: 1.16x faster                                       |
| sqlalchemy_declarative        | 75.7 ms                                                | 65.1 ms: 1.16x faster                                      |
| regex_compile                 | 95.6 ms                                                | 82.4 ms: 1.16x faster                                      |
| sympy_integrate               | 13.2 ms                                                | 11.5 ms: 1.15x faster                                      |
| logging_format                | 5.03 us                                                | 4.41 us: 1.14x faster                                      |
| docutils                      | 1.74 sec                                               | 1.53 sec: 1.14x faster                                     |
| sympy_sum                     | 92.7 ms                                                | 81.9 ms: 1.13x faster                                      |
| mako                          | 9.81 ms                                                | 8.72 ms: 1.12x faster                                      |
| unpickle_pure_python          | 198 us                                                 | 177 us: 1.12x faster                                       |
| logging_simple                | 4.59 us                                                | 4.10 us: 1.12x faster                                      |
| pprint_pformat                | 1.33 sec                                               | 1.20 sec: 1.10x faster                                     |
| scimark_fft                   | 225 ms                                                 | 206 ms: 1.09x faster                                       |
| xml_etree_parse               | 109 ms                                                 | 100 ms: 1.09x faster                                       |
| pprint_safe_repr              | 648 ms                                                 | 598 ms: 1.08x faster                                       |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.19 ms: 1.07x faster                                      |
| connected_components          | 318 ms                                                 | 298 ms: 1.07x faster                                       |
| nbody                         | 92.5 ms                                                | 86.7 ms: 1.07x faster                                      |
| sympy_str                     | 166 ms                                                 | 156 ms: 1.06x faster                                       |
| coroutines                    | 20.5 ms                                                | 19.3 ms: 1.06x faster                                      |
| 2to3                          | 201 ms                                                 | 190 ms: 1.06x faster                                       |
| xml_etree_iterparse           | 74.5 ms                                                | 70.7 ms: 1.05x faster                                      |
| bpe_tokeniser                 | 3.44 sec                                               | 3.28 sec: 1.05x faster                                     |
| meteor_contest                | 77.8 ms                                                | 75.0 ms: 1.04x faster                                      |
| json                          | 3.10 ms                                                | 3.05 ms: 1.02x faster                                      |
| xml_etree_process             | 44.6 ms                                                | 43.9 ms: 1.02x faster                                      |
| sympy_expand                  | 269 ms                                                 | 265 ms: 1.02x faster                                       |
| shortest_path                 | 328 ms                                                 | 325 ms: 1.01x faster                                       |
| generators                    | 31.7 ms                                                | 31.6 ms: 1.00x faster                                      |
| regex_effbot                  | 2.34 ms                                                | 2.34 ms: 1.00x slower                                      |
| pidigits                      | 280 ms                                                 | 283 ms: 1.01x slower                                       |
| genshi_text                   | 17.7 ms                                                | 18.1 ms: 1.02x slower                                      |
| many_optionals                | 486 us                                                 | 501 us: 1.03x slower                                       |
| fannkuch                      | 303 ms                                                 | 312 ms: 1.03x slower                                       |
| django_template               | 24.4 ms                                                | 25.6 ms: 1.05x slower                                      |
| genshi_xml                    | 35.1 ms                                                | 37.0 ms: 1.05x slower                                      |
| xml_etree_generate            | 53.9 ms                                                | 58.8 ms: 1.09x slower                                      |
| json_loads                    | 16.6 us                                                | 18.2 us: 1.10x slower                                      |
| sqlite_synth                  | 1.48 us                                                | 1.62 us: 1.10x slower                                      |
| nqueens                       | 63.8 ms                                                | 72.1 ms: 1.13x slower                                      |
| create_gc_cycles              | 1.16 ms                                                | 1.36 ms: 1.17x slower                                      |
| async_generators              | 233 ms                                                 | 274 ms: 1.18x slower                                       |
| gc_traversal                  | 2.71 ms                                                | 3.18 ms: 1.18x slower                                      |
| coverage                      | 41.2 ms                                                | 49.6 ms: 1.20x slower                                      |
| telco                         | 3.49 ms                                                | 4.73 ms: 1.36x slower                                      |
| python_startup_no_site        | 12.8 ms                                                | 18.7 ms: 1.46x slower                                      |
| python_startup                | 19.6 ms                                                | 31.4 ms: 1.60x slower                                      |
| logging_silent                | 117 ns                                                 | 346 ns: 2.95x slower                                       |
| Geometric mean                | (ref)                                                  | 1.21x faster                                               |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: bench_mp_pool, bench_thread_pool, chameleon, dask, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250526-3.14.0b2-12d3f88/bm-20250526-darwin-arm64-python-v3.14.0b2-3.14.0b2-12d3f88.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.230x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: 1.16x