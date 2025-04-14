# Results vs. 3.10.4

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: darwin-arm64
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.415x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 158 ms: 1.27x faster                                                   |
| docutils       | 1.74 sec                                               | 1.40 sec: 1.25x faster                                                 |
| html5lib       | 43.5 ms                                                | 28.6 ms: 1.52x faster                                                  |
| sphinx         | 729 ms                                                 | 558 ms: 1.31x faster                                                   |
| Geometric mean | (ref)                                                  | 1.33x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 61.9 ms: 6.33x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 140 ms: 3.45x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 359 ms: 2.83x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 367 ms: 2.78x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 194 ms: 2.48x faster                                                   |
| async_tree_none               | 391 ms                                                 | 158 ms: 2.48x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 358 ms: 1.87x faster                                                   |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 413 ms: 1.62x faster                                                   |
| coroutines                    | 20.5 ms                                                | 15.7 ms: 1.31x faster                                                  |
| async_generators              | 233 ms                                                 | 246 ms: 1.06x slower                                                   |
| Geometric mean                | (ref)                                                  | 2.12x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 46.2 ms: 1.57x faster                                                  |
| nbody          | 92.5 ms                                                | 68.6 ms: 1.35x faster                                                  |
| pidigits       | 280 ms                                                 | 283 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.28x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 65.5 ms: 1.46x faster                                                  |
| regex_dna      | 175 ms                                                 | 141 ms: 1.24x faster                                                   |
| regex_v8       | 19.1 ms                                                | 16.8 ms: 1.14x faster                                                  |
| regex_effbot   | 2.34 ms                                                | 2.28 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.20x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 285 us                                                 | 195 us: 1.46x faster                                                   |
| tomli_loads          | 1.72 sec                                               | 1.18 sec: 1.45x faster                                                 |
| unpickle_pure_python | 198 us                                                 | 137 us: 1.44x faster                                                   |
| xml_etree_process    | 44.6 ms                                                | 37.7 ms: 1.18x faster                                                  |
| json_dumps           | 8.31 ms                                                | 7.29 ms: 1.14x faster                                                  |
| xml_etree_parse      | 109 ms                                                 | 102 ms: 1.08x faster                                                   |
| xml_etree_iterparse  | 74.5 ms                                                | 70.6 ms: 1.06x faster                                                  |
| xml_etree_generate   | 53.9 ms                                                | 51.9 ms: 1.04x faster                                                  |
| json_loads           | 16.6 us                                                | 17.7 us: 1.07x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 16.0 ms: 1.23x faster                                                  |
| python_startup_no_site | 12.8 ms                                                | 11.4 ms: 1.12x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.17x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 7.21 ms: 1.36x faster                                                  |
| genshi_text     | 17.7 ms                                                | 13.3 ms: 1.33x faster                                                  |
| genshi_xml      | 35.1 ms                                                | 28.0 ms: 1.25x faster                                                  |
| django_template | 24.4 ms                                                | 20.4 ms: 1.19x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.28x faster                                                           |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 61.9 ms: 6.33x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 92.7 us: 3.52x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 140 ms: 3.45x faster                                                   |
| subparsers                    | 39.8 ms                                                | 11.7 ms: 3.39x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 359 ms: 2.83x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 367 ms: 2.78x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 194 ms: 2.48x faster                                                   |
| async_tree_none               | 391 ms                                                 | 158 ms: 2.48x faster                                                   |
| deltablue                     | 4.99 ms                                                | 2.28 ms: 2.19x faster                                                  |
| go                            | 163 ms                                                 | 77.2 ms: 2.12x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 17.7 us: 1.96x faster                                                  |
| raytrace                      | 327 ms                                                 | 168 ms: 1.95x faster                                                   |
| deepcopy                      | 276 us                                                 | 146 us: 1.89x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 358 ms: 1.87x faster                                                   |
| scimark_sor                   | 140 ms                                                 | 75.9 ms: 1.84x faster                                                  |
| chaos                         | 67.7 ms                                                | 37.3 ms: 1.82x faster                                                  |
| sqlglot_parse                 | 1.35 ms                                                | 757 us: 1.78x faster                                                   |
| richards_super                | 61.0 ms                                                | 34.9 ms: 1.75x faster                                                  |
| logging_silent                | 117 ns                                                 | 67.3 ns: 1.74x faster                                                  |
| scimark_monte_carlo           | 72.4 ms                                                | 42.1 ms: 1.72x faster                                                  |
| sqlglot_transpile             | 1.56 ms                                                | 915 us: 1.70x faster                                                   |
| richards                      | 52.3 ms                                                | 31.2 ms: 1.68x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 413 ms: 1.62x faster                                                   |
| spectral_norm                 | 95.3 ms                                                | 59.6 ms: 1.60x faster                                                  |
| pyflate                       | 448 ms                                                 | 283 ms: 1.58x faster                                                   |
| float                         | 72.4 ms                                                | 46.2 ms: 1.57x faster                                                  |
| deepcopy_reduce               | 2.32 us                                                | 1.52 us: 1.53x faster                                                  |
| html5lib                      | 43.5 ms                                                | 28.6 ms: 1.52x faster                                                  |
| hexiom                        | 6.25 ms                                                | 4.16 ms: 1.50x faster                                                  |
| logging_simple                | 4.59 us                                                | 3.10 us: 1.48x faster                                                  |
| logging_format                | 5.03 us                                                | 3.40 us: 1.48x faster                                                  |
| pylint                        | 231 ms                                                 | 158 ms: 1.46x faster                                                   |
| comprehensions                | 17.3 us                                                | 11.8 us: 1.46x faster                                                  |
| regex_compile                 | 95.6 ms                                                | 65.5 ms: 1.46x faster                                                  |
| pickle_pure_python            | 285 us                                                 | 195 us: 1.46x faster                                                   |
| tomli_loads                   | 1.72 sec                                               | 1.18 sec: 1.45x faster                                                 |
| pprint_pformat                | 1.33 sec                                               | 919 ms: 1.45x faster                                                   |
| unpickle_pure_python          | 198 us                                                 | 137 us: 1.44x faster                                                   |
| pprint_safe_repr              | 648 ms                                                 | 452 ms: 1.43x faster                                                   |
| scimark_lu                    | 103 ms                                                 | 71.7 ms: 1.43x faster                                                  |
| sqlalchemy_imperative         | 9.07 ms                                                | 6.34 ms: 1.43x faster                                                  |
| crypto_pyaes                  | 73.3 ms                                                | 51.4 ms: 1.43x faster                                                  |
| pycparser                     | 887 ms                                                 | 633 ms: 1.40x faster                                                   |
| generators                    | 31.7 ms                                                | 23.1 ms: 1.37x faster                                                  |
| mako                          | 9.81 ms                                                | 7.21 ms: 1.36x faster                                                  |
| nbody                         | 92.5 ms                                                | 68.6 ms: 1.35x faster                                                  |
| k_core                        | 2.01 sec                                               | 1.51 sec: 1.34x faster                                                 |
| genshi_text                   | 17.7 ms                                                | 13.3 ms: 1.33x faster                                                  |
| scimark_fft                   | 225 ms                                                 | 170 ms: 1.33x faster                                                   |
| thrift                        | 562 us                                                 | 426 us: 1.32x faster                                                   |
| sqlalchemy_declarative        | 75.7 ms                                                | 57.6 ms: 1.32x faster                                                  |
| dulwich_log                   | 35.6 ms                                                | 27.2 ms: 1.31x faster                                                  |
| sphinx                        | 729 ms                                                 | 558 ms: 1.31x faster                                                   |
| coroutines                    | 20.5 ms                                                | 15.7 ms: 1.31x faster                                                  |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 2.62 ms: 1.30x faster                                                  |
| sympy_sum                     | 92.7 ms                                                | 72.3 ms: 1.28x faster                                                  |
| 2to3                          | 201 ms                                                 | 158 ms: 1.27x faster                                                   |
| genshi_xml                    | 35.1 ms                                                | 28.0 ms: 1.25x faster                                                  |
| fannkuch                      | 303 ms                                                 | 243 ms: 1.25x faster                                                   |
| docutils                      | 1.74 sec                                               | 1.40 sec: 1.25x faster                                                 |
| regex_dna                     | 175 ms                                                 | 141 ms: 1.24x faster                                                   |
| python_startup                | 19.6 ms                                                | 16.0 ms: 1.23x faster                                                  |
| sympy_str                     | 166 ms                                                 | 136 ms: 1.22x faster                                                   |
| bpe_tokeniser                 | 3.44 sec                                               | 2.85 sec: 1.21x faster                                                 |
| sympy_integrate               | 13.2 ms                                                | 11.0 ms: 1.20x faster                                                  |
| django_template               | 24.4 ms                                                | 20.4 ms: 1.19x faster                                                  |
| pathlib                       | 25.7 ms                                                | 21.8 ms: 1.18x faster                                                  |
| xml_etree_process             | 44.6 ms                                                | 37.7 ms: 1.18x faster                                                  |
| sympy_expand                  | 269 ms                                                 | 228 ms: 1.18x faster                                                   |
| sqlglot_optimize              | 37.2 ms                                                | 31.8 ms: 1.17x faster                                                  |
| bench_thread_pool             | 545 us                                                 | 477 us: 1.14x faster                                                   |
| json_dumps                    | 8.31 ms                                                | 7.29 ms: 1.14x faster                                                  |
| regex_v8                      | 19.1 ms                                                | 16.8 ms: 1.14x faster                                                  |
| nqueens                       | 63.8 ms                                                | 56.5 ms: 1.13x faster                                                  |
| many_optionals                | 486 us                                                 | 431 us: 1.13x faster                                                   |
| python_startup_no_site        | 12.8 ms                                                | 11.4 ms: 1.12x faster                                                  |
| mdp                           | 1.65 sec                                               | 1.48 sec: 1.12x faster                                                 |
| meteor_contest                | 77.8 ms                                                | 69.8 ms: 1.11x faster                                                  |
| sqlglot_normalize             | 192 ms                                                 | 176 ms: 1.09x faster                                                   |
| connected_components          | 318 ms                                                 | 295 ms: 1.08x faster                                                   |
| xml_etree_parse               | 109 ms                                                 | 102 ms: 1.08x faster                                                   |
| xml_etree_iterparse           | 74.5 ms                                                | 70.6 ms: 1.06x faster                                                  |
| json                          | 3.10 ms                                                | 2.96 ms: 1.05x faster                                                  |
| xml_etree_generate            | 53.9 ms                                                | 51.9 ms: 1.04x faster                                                  |
| dask                          | 789 ms                                                 | 766 ms: 1.03x faster                                                   |
| regex_effbot                  | 2.34 ms                                                | 2.28 ms: 1.02x faster                                                  |
| shortest_path                 | 328 ms                                                 | 323 ms: 1.01x faster                                                   |
| pidigits                      | 280 ms                                                 | 283 ms: 1.01x slower                                                   |
| sqlite_synth                  | 1.48 us                                                | 1.52 us: 1.03x slower                                                  |
| bench_mp_pool                 | 56.0 ms                                                | 58.2 ms: 1.04x slower                                                  |
| async_generators              | 233 ms                                                 | 246 ms: 1.06x slower                                                   |
| json_loads                    | 16.6 us                                                | 17.7 us: 1.07x slower                                                  |
| create_gc_cycles              | 1.16 ms                                                | 1.28 ms: 1.10x slower                                                  |
| coverage                      | 41.2 ms                                                | 45.8 ms: 1.11x slower                                                  |
| gc_traversal                  | 2.71 ms                                                | 3.10 ms: 1.15x slower                                                  |
| telco                         | 3.49 ms                                                | 4.54 ms: 1.30x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.41x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, tornado_http
Ignored benchmarks (16) of results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-darwin-arm64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.415x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.14x