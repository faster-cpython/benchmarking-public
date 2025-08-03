# Results vs. 3.10.4

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: darwin-arm64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.290x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: 1.35x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 184 ms: 1.09x faster                                                  |
| docutils       | 1.74 sec                                               | 1.39 sec: 1.25x faster                                                |
| html5lib       | 43.5 ms                                                | 32.4 ms: 1.34x faster                                                 |
| sphinx         | 729 ms                                                 | 580 ms: 1.26x faster                                                  |
| Geometric mean | (ref)                                                  | 1.23x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 73.8 ms: 5.31x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 138 ms: 3.50x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 305 ms: 3.33x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 319 ms: 3.19x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 184 ms: 2.62x faster                                                  |
| async_tree_none               | 391 ms                                                 | 153 ms: 2.55x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 357 ms: 1.88x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 397 ms: 1.68x faster                                                  |
| coroutines                    | 20.5 ms                                                | 16.8 ms: 1.22x faster                                                 |
| asyncio_websockets            | 242 ms                                                 | 238 ms: 1.02x faster                                                  |
| async_generators              | 233 ms                                                 | 284 ms: 1.22x slower                                                  |
| Geometric mean                | (ref)                                                  | 2.14x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 46.9 ms: 1.54x faster                                                 |
| nbody          | 92.5 ms                                                | 87.0 ms: 1.06x faster                                                 |
| pidigits       | 280 ms                                                 | 277 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.18x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 19.1 ms                                                | 14.8 ms: 1.30x faster                                                 |
| regex_dna      | 175 ms                                                 | 137 ms: 1.28x faster                                                  |
| regex_compile  | 95.6 ms                                                | 78.0 ms: 1.23x faster                                                 |
| regex_effbot   | 2.34 ms                                                | 2.23 ms: 1.05x faster                                                 |
| Geometric mean | (ref)                                                  | 1.21x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 285 us                                                 | 222 us: 1.28x faster                                                  |
| json_dumps           | 8.31 ms                                                | 6.80 ms: 1.22x faster                                                 |
| unpickle_pure_python | 198 us                                                 | 163 us: 1.21x faster                                                  |
| xml_etree_iterparse  | 74.5 ms                                                | 63.3 ms: 1.18x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 95.8 ms: 1.14x faster                                                 |
| tomli_loads          | 1.72 sec                                               | 1.52 sec: 1.13x faster                                                |
| xml_etree_process    | 44.6 ms                                                | 41.4 ms: 1.08x faster                                                 |
| xml_etree_generate   | 53.9 ms                                                | 56.9 ms: 1.06x slower                                                 |
| json_loads           | 16.6 us                                                | 17.9 us: 1.08x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 19.0 ms: 1.03x faster                                                 |
| python_startup_no_site | 12.8 ms                                                | 14.5 ms: 1.14x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 24.4 ms                                                | 23.9 ms: 1.02x faster                                                 |
| genshi_text     | 17.7 ms                                                | 17.5 ms: 1.01x faster                                                 |
| genshi_xml      | 35.1 ms                                                | 36.2 ms: 1.03x slower                                                 |
| mako            | 9.81 ms                                                | 10.4 ms: 1.06x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                          |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 73.8 ms: 5.31x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 138 ms: 3.50x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 305 ms: 3.33x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 319 ms: 3.19x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 113 us: 2.88x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 184 ms: 2.62x faster                                                  |
| async_tree_none               | 391 ms                                                 | 153 ms: 2.55x faster                                                  |
| gc_traversal                  | 2.71 ms                                                | 1.30 ms: 2.09x faster                                                 |
| deltablue                     | 4.99 ms                                                | 2.48 ms: 2.01x faster                                                 |
| mdp                           | 1.65 sec                                               | 835 ms: 1.98x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 357 ms: 1.88x faster                                                  |
| go                            | 163 ms                                                 | 89.3 ms: 1.83x faster                                                 |
| raytrace                      | 327 ms                                                 | 191 ms: 1.71x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 397 ms: 1.68x faster                                                  |
| chaos                         | 67.7 ms                                                | 41.6 ms: 1.63x faster                                                 |
| scimark_sor                   | 140 ms                                                 | 87.3 ms: 1.60x faster                                                 |
| logging_silent                | 117 ns                                                 | 75.7 ns: 1.55x faster                                                 |
| float                         | 72.4 ms                                                | 46.9 ms: 1.54x faster                                                 |
| deepcopy_memo                 | 34.7 us                                                | 22.6 us: 1.53x faster                                                 |
| deepcopy                      | 276 us                                                 | 182 us: 1.51x faster                                                  |
| create_gc_cycles              | 1.16 ms                                                | 782 us: 1.49x faster                                                  |
| richards_super                | 61.0 ms                                                | 41.2 ms: 1.48x faster                                                 |
| scimark_monte_carlo           | 72.4 ms                                                | 49.2 ms: 1.47x faster                                                 |
| subparsers                    | 39.8 ms                                                | 27.2 ms: 1.46x faster                                                 |
| pyflate                       | 448 ms                                                 | 307 ms: 1.46x faster                                                  |
| richards                      | 52.3 ms                                                | 36.5 ms: 1.43x faster                                                 |
| pylint                        | 231 ms                                                 | 166 ms: 1.39x faster                                                  |
| dulwich_log                   | 35.6 ms                                                | 25.8 ms: 1.38x faster                                                 |
| comprehensions                | 17.3 us                                                | 12.6 us: 1.37x faster                                                 |
| html5lib                      | 43.5 ms                                                | 32.4 ms: 1.34x faster                                                 |
| spectral_norm                 | 95.3 ms                                                | 72.8 ms: 1.31x faster                                                 |
| regex_v8                      | 19.1 ms                                                | 14.8 ms: 1.30x faster                                                 |
| hexiom                        | 6.25 ms                                                | 4.85 ms: 1.29x faster                                                 |
| pickle_pure_python            | 285 us                                                 | 222 us: 1.28x faster                                                  |
| pycparser                     | 887 ms                                                 | 694 ms: 1.28x faster                                                  |
| regex_dna                     | 175 ms                                                 | 137 ms: 1.28x faster                                                  |
| generators                    | 31.7 ms                                                | 25.0 ms: 1.27x faster                                                 |
| k_core                        | 2.01 sec                                               | 1.60 sec: 1.26x faster                                                |
| crypto_pyaes                  | 73.3 ms                                                | 58.3 ms: 1.26x faster                                                 |
| sphinx                        | 729 ms                                                 | 580 ms: 1.26x faster                                                  |
| docutils                      | 1.74 sec                                               | 1.39 sec: 1.25x faster                                                |
| logging_simple                | 4.59 us                                                | 3.70 us: 1.24x faster                                                 |
| regex_compile                 | 95.6 ms                                                | 78.0 ms: 1.23x faster                                                 |
| logging_format                | 5.03 us                                                | 4.11 us: 1.22x faster                                                 |
| json_dumps                    | 8.31 ms                                                | 6.80 ms: 1.22x faster                                                 |
| deepcopy_reduce               | 2.32 us                                                | 1.90 us: 1.22x faster                                                 |
| coroutines                    | 20.5 ms                                                | 16.8 ms: 1.22x faster                                                 |
| scimark_lu                    | 103 ms                                                 | 84.4 ms: 1.21x faster                                                 |
| unpickle_pure_python          | 198 us                                                 | 163 us: 1.21x faster                                                  |
| xml_etree_iterparse           | 74.5 ms                                                | 63.3 ms: 1.18x faster                                                 |
| xml_etree_parse               | 109 ms                                                 | 95.8 ms: 1.14x faster                                                 |
| sympy_integrate               | 13.2 ms                                                | 11.5 ms: 1.14x faster                                                 |
| pprint_pformat                | 1.33 sec                                               | 1.17 sec: 1.13x faster                                                |
| tomli_loads                   | 1.72 sec                                               | 1.52 sec: 1.13x faster                                                |
| thrift                        | 562 us                                                 | 497 us: 1.13x faster                                                  |
| bpe_tokeniser                 | 3.44 sec                                               | 3.05 sec: 1.13x faster                                                |
| sympy_sum                     | 92.7 ms                                                | 82.4 ms: 1.12x faster                                                 |
| pathlib                       | 25.7 ms                                                | 23.0 ms: 1.12x faster                                                 |
| pprint_safe_repr              | 648 ms                                                 | 578 ms: 1.12x faster                                                  |
| scimark_fft                   | 225 ms                                                 | 202 ms: 1.12x faster                                                  |
| 2to3                          | 201 ms                                                 | 184 ms: 1.09x faster                                                  |
| sqlite_synth                  | 1.48 us                                                | 1.37 us: 1.08x faster                                                 |
| xml_etree_process             | 44.6 ms                                                | 41.4 ms: 1.08x faster                                                 |
| nbody                         | 92.5 ms                                                | 87.0 ms: 1.06x faster                                                 |
| sympy_str                     | 166 ms                                                 | 157 ms: 1.06x faster                                                  |
| fannkuch                      | 303 ms                                                 | 287 ms: 1.05x faster                                                  |
| regex_effbot                  | 2.34 ms                                                | 2.23 ms: 1.05x faster                                                 |
| python_startup                | 19.6 ms                                                | 19.0 ms: 1.03x faster                                                 |
| json                          | 3.10 ms                                                | 3.02 ms: 1.03x faster                                                 |
| django_template               | 24.4 ms                                                | 23.9 ms: 1.02x faster                                                 |
| asyncio_websockets            | 242 ms                                                 | 238 ms: 1.02x faster                                                  |
| genshi_text                   | 17.7 ms                                                | 17.5 ms: 1.01x faster                                                 |
| pidigits                      | 280 ms                                                 | 277 ms: 1.01x faster                                                  |
| nqueens                       | 63.8 ms                                                | 64.6 ms: 1.01x slower                                                 |
| sympy_expand                  | 269 ms                                                 | 273 ms: 1.01x slower                                                  |
| connected_components          | 318 ms                                                 | 323 ms: 1.02x slower                                                  |
| dask                          | 789 ms                                                 | 807 ms: 1.02x slower                                                  |
| genshi_xml                    | 35.1 ms                                                | 36.2 ms: 1.03x slower                                                 |
| meteor_contest                | 77.8 ms                                                | 80.8 ms: 1.04x slower                                                 |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.57 ms: 1.04x slower                                                 |
| xml_etree_generate            | 53.9 ms                                                | 56.9 ms: 1.06x slower                                                 |
| mako                          | 9.81 ms                                                | 10.4 ms: 1.06x slower                                                 |
| shortest_path                 | 328 ms                                                 | 351 ms: 1.07x slower                                                  |
| json_loads                    | 16.6 us                                                | 17.9 us: 1.08x slower                                                 |
| python_startup_no_site        | 12.8 ms                                                | 14.5 ms: 1.14x slower                                                 |
| async_generators              | 233 ms                                                 | 284 ms: 1.22x slower                                                  |
| many_optionals                | 486 us                                                 | 606 us: 1.25x slower                                                  |
| bench_mp_pool                 | 56.0 ms                                                | 74.3 ms: 1.33x slower                                                 |
| bench_thread_pool             | 545 us                                                 | 756 us: 1.39x slower                                                  |
| telco                         | 3.49 ms                                                | 4.96 ms: 1.42x slower                                                 |
| coverage                      | 41.2 ms                                                | 61.7 ms: 1.50x slower                                                 |
| Geometric mean                | (ref)                                                  | 1.28x faster                                                          |
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (20) of results/bm-20250802-3.15.0a0-801cf3f-NOGIL/bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.290x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: 1.35x