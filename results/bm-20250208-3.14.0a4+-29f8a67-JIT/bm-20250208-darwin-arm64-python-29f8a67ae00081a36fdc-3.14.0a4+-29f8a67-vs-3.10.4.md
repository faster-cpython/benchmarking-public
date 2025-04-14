# Results vs. 3.10.4

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: darwin-arm64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.377x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 167 ms: 1.21x faster                                                   |
| docutils       | 1.74 sec                                               | 1.45 sec: 1.20x faster                                                 |
| html5lib       | 43.5 ms                                                | 29.4 ms: 1.48x faster                                                  |
| sphinx         | 729 ms                                                 | 567 ms: 1.28x faster                                                   |
| Geometric mean | (ref)                                                  | 1.29x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 65.9 ms: 5.94x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 145 ms: 3.33x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 361 ms: 2.81x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 372 ms: 2.74x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 197 ms: 2.45x faster                                                   |
| async_tree_none               | 391 ms                                                 | 160 ms: 2.44x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 364 ms: 1.84x faster                                                   |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 415 ms: 1.61x faster                                                   |
| coroutines                    | 20.5 ms                                                | 15.8 ms: 1.30x faster                                                  |
| async_generators              | 233 ms                                                 | 271 ms: 1.16x slower                                                   |
| Geometric mean                | (ref)                                                  | 2.07x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 46.8 ms: 1.55x faster                                                  |
| nbody          | 92.5 ms                                                | 65.0 ms: 1.42x faster                                                  |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.30x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 67.8 ms: 1.41x faster                                                  |
| regex_dna      | 175 ms                                                 | 140 ms: 1.24x faster                                                   |
| regex_v8       | 19.1 ms                                                | 16.7 ms: 1.14x faster                                                  |
| regex_effbot   | 2.34 ms                                                | 2.25 ms: 1.04x faster                                                  |
| Geometric mean | (ref)                                                  | 1.20x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 130 us: 1.53x faster                                                   |
| pickle_pure_python   | 285 us                                                 | 194 us: 1.46x faster                                                   |
| tomli_loads          | 1.72 sec                                               | 1.21 sec: 1.42x faster                                                 |
| xml_etree_process    | 44.6 ms                                                | 35.7 ms: 1.25x faster                                                  |
| json_dumps           | 8.31 ms                                                | 7.26 ms: 1.14x faster                                                  |
| xml_etree_parse      | 109 ms                                                 | 102 ms: 1.07x faster                                                   |
| xml_etree_generate   | 53.9 ms                                                | 50.3 ms: 1.07x faster                                                  |
| xml_etree_iterparse  | 74.5 ms                                                | 70.0 ms: 1.06x faster                                                  |
| json_loads           | 16.6 us                                                | 17.7 us: 1.07x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.20x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 19.0 ms: 1.03x faster                                                  |
| python_startup_no_site | 12.8 ms                                                | 14.1 ms: 1.10x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 6.48 ms: 1.51x faster                                                  |
| genshi_text     | 17.7 ms                                                | 13.5 ms: 1.31x faster                                                  |
| genshi_xml      | 35.1 ms                                                | 29.0 ms: 1.21x faster                                                  |
| django_template | 24.4 ms                                                | 20.9 ms: 1.17x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.29x faster                                                           |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 65.9 ms: 5.94x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 95.1 us: 3.43x faster                                                  |
| subparsers                    | 39.8 ms                                                | 11.8 ms: 3.38x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 145 ms: 3.33x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 361 ms: 2.81x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 372 ms: 2.74x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 197 ms: 2.45x faster                                                   |
| async_tree_none               | 391 ms                                                 | 160 ms: 2.44x faster                                                   |
| deltablue                     | 4.99 ms                                                | 2.36 ms: 2.11x faster                                                  |
| go                            | 163 ms                                                 | 80.6 ms: 2.03x faster                                                  |
| raytrace                      | 327 ms                                                 | 172 ms: 1.90x faster                                                   |
| deepcopy_memo                 | 34.7 us                                                | 18.4 us: 1.89x faster                                                  |
| deepcopy                      | 276 us                                                 | 149 us: 1.85x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 364 ms: 1.84x faster                                                   |
| scimark_sor                   | 140 ms                                                 | 77.9 ms: 1.80x faster                                                  |
| logging_silent                | 117 ns                                                 | 65.9 ns: 1.78x faster                                                  |
| chaos                         | 67.7 ms                                                | 39.0 ms: 1.73x faster                                                  |
| scimark_monte_carlo           | 72.4 ms                                                | 42.5 ms: 1.70x faster                                                  |
| richards_super                | 61.0 ms                                                | 36.1 ms: 1.69x faster                                                  |
| richards                      | 52.3 ms                                                | 31.7 ms: 1.65x faster                                                  |
| sqlglot_parse                 | 1.35 ms                                                | 826 us: 1.64x faster                                                   |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 415 ms: 1.61x faster                                                   |
| pyflate                       | 448 ms                                                 | 283 ms: 1.58x faster                                                   |
| sqlglot_transpile             | 1.56 ms                                                | 996 us: 1.57x faster                                                   |
| float                         | 72.4 ms                                                | 46.8 ms: 1.55x faster                                                  |
| spectral_norm                 | 95.3 ms                                                | 61.6 ms: 1.55x faster                                                  |
| unpickle_pure_python          | 198 us                                                 | 130 us: 1.53x faster                                                   |
| mako                          | 9.81 ms                                                | 6.48 ms: 1.51x faster                                                  |
| html5lib                      | 43.5 ms                                                | 29.4 ms: 1.48x faster                                                  |
| deepcopy_reduce               | 2.32 us                                                | 1.57 us: 1.48x faster                                                  |
| pickle_pure_python            | 285 us                                                 | 194 us: 1.46x faster                                                   |
| logging_simple                | 4.59 us                                                | 3.14 us: 1.46x faster                                                  |
| logging_format                | 5.03 us                                                | 3.44 us: 1.46x faster                                                  |
| pylint                        | 231 ms                                                 | 160 ms: 1.44x faster                                                   |
| nbody                         | 92.5 ms                                                | 65.0 ms: 1.42x faster                                                  |
| tomli_loads                   | 1.72 sec                                               | 1.21 sec: 1.42x faster                                                 |
| regex_compile                 | 95.6 ms                                                | 67.8 ms: 1.41x faster                                                  |
| scimark_lu                    | 103 ms                                                 | 73.3 ms: 1.40x faster                                                  |
| comprehensions                | 17.3 us                                                | 12.5 us: 1.39x faster                                                  |
| generators                    | 31.7 ms                                                | 22.9 ms: 1.38x faster                                                  |
| hexiom                        | 6.25 ms                                                | 4.51 ms: 1.38x faster                                                  |
| crypto_pyaes                  | 73.3 ms                                                | 53.2 ms: 1.38x faster                                                  |
| sqlalchemy_imperative         | 9.07 ms                                                | 6.66 ms: 1.36x faster                                                  |
| pycparser                     | 887 ms                                                 | 673 ms: 1.32x faster                                                   |
| scimark_fft                   | 225 ms                                                 | 172 ms: 1.31x faster                                                   |
| genshi_text                   | 17.7 ms                                                | 13.5 ms: 1.31x faster                                                  |
| coroutines                    | 20.5 ms                                                | 15.8 ms: 1.30x faster                                                  |
| thrift                        | 562 us                                                 | 435 us: 1.29x faster                                                   |
| k_core                        | 2.01 sec                                               | 1.56 sec: 1.29x faster                                                 |
| pprint_pformat                | 1.33 sec                                               | 1.03 sec: 1.29x faster                                                 |
| sqlalchemy_declarative        | 75.7 ms                                                | 58.7 ms: 1.29x faster                                                  |
| sphinx                        | 729 ms                                                 | 567 ms: 1.28x faster                                                   |
| pprint_safe_repr              | 648 ms                                                 | 508 ms: 1.27x faster                                                   |
| dulwich_log                   | 35.6 ms                                                | 28.1 ms: 1.27x faster                                                  |
| xml_etree_process             | 44.6 ms                                                | 35.7 ms: 1.25x faster                                                  |
| regex_dna                     | 175 ms                                                 | 140 ms: 1.24x faster                                                   |
| sympy_sum                     | 92.7 ms                                                | 74.5 ms: 1.24x faster                                                  |
| genshi_xml                    | 35.1 ms                                                | 29.0 ms: 1.21x faster                                                  |
| 2to3                          | 201 ms                                                 | 167 ms: 1.21x faster                                                   |
| docutils                      | 1.74 sec                                               | 1.45 sec: 1.20x faster                                                 |
| bpe_tokeniser                 | 3.44 sec                                               | 2.87 sec: 1.20x faster                                                 |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 2.89 ms: 1.18x faster                                                  |
| sympy_str                     | 166 ms                                                 | 141 ms: 1.18x faster                                                   |
| django_template               | 24.4 ms                                                | 20.9 ms: 1.17x faster                                                  |
| sympy_integrate               | 13.2 ms                                                | 11.5 ms: 1.15x faster                                                  |
| json_dumps                    | 8.31 ms                                                | 7.26 ms: 1.14x faster                                                  |
| regex_v8                      | 19.1 ms                                                | 16.7 ms: 1.14x faster                                                  |
| fannkuch                      | 303 ms                                                 | 266 ms: 1.14x faster                                                   |
| sympy_expand                  | 269 ms                                                 | 238 ms: 1.13x faster                                                   |
| sqlglot_optimize              | 37.2 ms                                                | 33.1 ms: 1.13x faster                                                  |
| pathlib                       | 25.7 ms                                                | 23.1 ms: 1.12x faster                                                  |
| bench_thread_pool             | 545 us                                                 | 498 us: 1.10x faster                                                   |
| mdp                           | 1.65 sec                                               | 1.51 sec: 1.09x faster                                                 |
| many_optionals                | 486 us                                                 | 448 us: 1.08x faster                                                   |
| xml_etree_parse               | 109 ms                                                 | 102 ms: 1.07x faster                                                   |
| xml_etree_generate            | 53.9 ms                                                | 50.3 ms: 1.07x faster                                                  |
| xml_etree_iterparse           | 74.5 ms                                                | 70.0 ms: 1.06x faster                                                  |
| sqlglot_normalize             | 192 ms                                                 | 181 ms: 1.06x faster                                                   |
| meteor_contest                | 77.8 ms                                                | 73.4 ms: 1.06x faster                                                  |
| connected_components          | 318 ms                                                 | 304 ms: 1.05x faster                                                   |
| nqueens                       | 63.8 ms                                                | 61.2 ms: 1.04x faster                                                  |
| regex_effbot                  | 2.34 ms                                                | 2.25 ms: 1.04x faster                                                  |
| python_startup                | 19.6 ms                                                | 19.0 ms: 1.03x faster                                                  |
| json                          | 3.10 ms                                                | 3.00 ms: 1.03x faster                                                  |
| dask                          | 789 ms                                                 | 768 ms: 1.03x faster                                                   |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                                   |
| sqlite_synth                  | 1.48 us                                                | 1.54 us: 1.04x slower                                                  |
| shortest_path                 | 328 ms                                                 | 344 ms: 1.05x slower                                                   |
| bench_mp_pool                 | 56.0 ms                                                | 59.5 ms: 1.06x slower                                                  |
| json_loads                    | 16.6 us                                                | 17.7 us: 1.07x slower                                                  |
| create_gc_cycles              | 1.16 ms                                                | 1.28 ms: 1.10x slower                                                  |
| python_startup_no_site        | 12.8 ms                                                | 14.1 ms: 1.10x slower                                                  |
| coverage                      | 41.2 ms                                                | 45.7 ms: 1.11x slower                                                  |
| gc_traversal                  | 2.71 ms                                                | 3.11 ms: 1.15x slower                                                  |
| async_generators              | 233 ms                                                 | 271 ms: 1.16x slower                                                   |
| telco                         | 3.49 ms                                                | 4.48 ms: 1.28x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.37x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, tornado_http
Ignored benchmarks (16) of results/bm-20250208-3.14.0a4+-29f8a67-JIT/bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.377x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.16x