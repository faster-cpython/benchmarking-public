# Results vs. 3.10.4

- fork: python
- ref: fba5dded6df3c2b19435
- machine: darwin-arm64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.221x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 187 ms: 1.08x faster                                                  |
| docutils       | 1.74 sec                                               | 1.64 sec: 1.06x faster                                                |
| html5lib       | 43.5 ms                                                | 33.3 ms: 1.31x faster                                                 |
| sphinx         | 729 ms                                                 | 647 ms: 1.13x faster                                                  |
| Geometric mean | (ref)                                                  | 1.14x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 70.5 ms: 5.56x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 148 ms: 3.27x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 386 ms: 2.63x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 400 ms: 2.55x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 204 ms: 2.35x faster                                                  |
| async_tree_none               | 391 ms                                                 | 173 ms: 2.27x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 389 ms: 1.72x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 450 ms: 1.49x faster                                                  |
| coroutines                    | 20.5 ms                                                | 18.1 ms: 1.13x faster                                                 |
| asyncio_websockets            | 242 ms                                                 | 243 ms: 1.00x slower                                                  |
| async_generators              | 233 ms                                                 | 310 ms: 1.33x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.93x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 51.4 ms: 1.41x faster                                                 |
| nbody          | 92.5 ms                                                | 83.1 ms: 1.11x faster                                                 |
| pidigits       | 280 ms                                                 | 285 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.16x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 74.2 ms: 1.29x faster                                                 |
| regex_dna      | 175 ms                                                 | 145 ms: 1.21x faster                                                  |
| regex_v8       | 19.1 ms                                                | 17.4 ms: 1.10x faster                                                 |
| regex_effbot   | 2.34 ms                                                | 2.19 ms: 1.07x faster                                                 |
| Geometric mean | (ref)                                                  | 1.16x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 285 us                                                 | 221 us: 1.29x faster                                                  |
| unpickle_pure_python | 198 us                                                 | 155 us: 1.28x faster                                                  |
| tomli_loads          | 1.72 sec                                               | 1.39 sec: 1.24x faster                                                |
| json_dumps           | 8.31 ms                                                | 8.09 ms: 1.03x faster                                                 |
| xml_etree_process    | 44.6 ms                                                | 43.9 ms: 1.02x faster                                                 |
| xml_etree_iterparse  | 74.5 ms                                                | 76.0 ms: 1.02x slower                                                 |
| xml_etree_parse      | 109 ms                                                 | 112 ms: 1.02x slower                                                  |
| xml_etree_generate   | 53.9 ms                                                | 65.2 ms: 1.21x slower                                                 |
| json_loads           | 16.6 us                                                | 22.7 us: 1.37x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 20.2 ms: 1.03x slower                                                 |
| python_startup_no_site | 12.8 ms                                                | 15.3 ms: 1.20x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 8.21 ms: 1.20x faster                                                 |
| genshi_text     | 17.7 ms                                                | 15.7 ms: 1.13x faster                                                 |
| genshi_xml      | 35.1 ms                                                | 33.1 ms: 1.06x faster                                                 |
| django_template | 24.4 ms                                                | 25.5 ms: 1.05x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                          |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 70.5 ms: 5.56x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 148 ms: 3.27x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 120 us: 2.72x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 386 ms: 2.63x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 400 ms: 2.55x faster                                                  |
| subparsers                    | 39.8 ms                                                | 15.9 ms: 2.50x faster                                                 |
| async_tree_memoization        | 481 ms                                                 | 204 ms: 2.35x faster                                                  |
| async_tree_none               | 391 ms                                                 | 173 ms: 2.27x faster                                                  |
| go                            | 163 ms                                                 | 77.2 ms: 2.12x faster                                                 |
| deltablue                     | 4.99 ms                                                | 2.61 ms: 1.91x faster                                                 |
| mdp                           | 1.65 sec                                               | 883 ms: 1.87x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 19.3 us: 1.80x faster                                                 |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 389 ms: 1.72x faster                                                  |
| scimark_monte_carlo           | 72.4 ms                                                | 46.7 ms: 1.55x faster                                                 |
| raytrace                      | 327 ms                                                 | 211 ms: 1.55x faster                                                  |
| scimark_sor                   | 140 ms                                                 | 91.2 ms: 1.54x faster                                                 |
| chaos                         | 67.7 ms                                                | 44.1 ms: 1.53x faster                                                 |
| richards_super                | 61.0 ms                                                | 40.4 ms: 1.51x faster                                                 |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 450 ms: 1.49x faster                                                  |
| deepcopy                      | 276 us                                                 | 186 us: 1.48x faster                                                  |
| pyflate                       | 448 ms                                                 | 303 ms: 1.48x faster                                                  |
| richards                      | 52.3 ms                                                | 35.9 ms: 1.46x faster                                                 |
| comprehensions                | 17.3 us                                                | 12.0 us: 1.45x faster                                                 |
| float                         | 72.4 ms                                                | 51.4 ms: 1.41x faster                                                 |
| generators                    | 31.7 ms                                                | 22.8 ms: 1.39x faster                                                 |
| hexiom                        | 6.25 ms                                                | 4.58 ms: 1.36x faster                                                 |
| dulwich_log                   | 35.6 ms                                                | 27.0 ms: 1.32x faster                                                 |
| pylint                        | 231 ms                                                 | 176 ms: 1.31x faster                                                  |
| k_core                        | 2.01 sec                                               | 1.54 sec: 1.31x faster                                                |
| html5lib                      | 43.5 ms                                                | 33.3 ms: 1.31x faster                                                 |
| regex_compile                 | 95.6 ms                                                | 74.2 ms: 1.29x faster                                                 |
| pickle_pure_python            | 285 us                                                 | 221 us: 1.29x faster                                                  |
| unpickle_pure_python          | 198 us                                                 | 155 us: 1.28x faster                                                  |
| tomli_loads                   | 1.72 sec                                               | 1.39 sec: 1.24x faster                                                |
| crypto_pyaes                  | 73.3 ms                                                | 60.1 ms: 1.22x faster                                                 |
| regex_dna                     | 175 ms                                                 | 145 ms: 1.21x faster                                                  |
| pycparser                     | 887 ms                                                 | 741 ms: 1.20x faster                                                  |
| mako                          | 9.81 ms                                                | 8.21 ms: 1.20x faster                                                 |
| spectral_norm                 | 95.3 ms                                                | 79.9 ms: 1.19x faster                                                 |
| scimark_lu                    | 103 ms                                                 | 86.6 ms: 1.18x faster                                                 |
| logging_format                | 5.03 us                                                | 4.29 us: 1.17x faster                                                 |
| deepcopy_reduce               | 2.32 us                                                | 1.98 us: 1.17x faster                                                 |
| logging_simple                | 4.59 us                                                | 3.96 us: 1.16x faster                                                 |
| coroutines                    | 20.5 ms                                                | 18.1 ms: 1.13x faster                                                 |
| genshi_text                   | 17.7 ms                                                | 15.7 ms: 1.13x faster                                                 |
| sphinx                        | 729 ms                                                 | 647 ms: 1.13x faster                                                  |
| sympy_integrate               | 13.2 ms                                                | 11.8 ms: 1.12x faster                                                 |
| pprint_pformat                | 1.33 sec                                               | 1.19 sec: 1.12x faster                                                |
| nbody                         | 92.5 ms                                                | 83.1 ms: 1.11x faster                                                 |
| pprint_safe_repr              | 648 ms                                                 | 586 ms: 1.11x faster                                                  |
| regex_v8                      | 19.1 ms                                                | 17.4 ms: 1.10x faster                                                 |
| sympy_sum                     | 92.7 ms                                                | 85.1 ms: 1.09x faster                                                 |
| 2to3                          | 201 ms                                                 | 187 ms: 1.08x faster                                                  |
| regex_effbot                  | 2.34 ms                                                | 2.19 ms: 1.07x faster                                                 |
| genshi_xml                    | 35.1 ms                                                | 33.1 ms: 1.06x faster                                                 |
| docutils                      | 1.74 sec                                               | 1.64 sec: 1.06x faster                                                |
| pathlib                       | 25.7 ms                                                | 24.3 ms: 1.06x faster                                                 |
| json_dumps                    | 8.31 ms                                                | 8.09 ms: 1.03x faster                                                 |
| meteor_contest                | 77.8 ms                                                | 75.8 ms: 1.03x faster                                                 |
| dask                          | 789 ms                                                 | 772 ms: 1.02x faster                                                  |
| connected_components          | 318 ms                                                 | 312 ms: 1.02x faster                                                  |
| xml_etree_process             | 44.6 ms                                                | 43.9 ms: 1.02x faster                                                 |
| bench_thread_pool             | 545 us                                                 | 538 us: 1.01x faster                                                  |
| sympy_str                     | 166 ms                                                 | 164 ms: 1.01x faster                                                  |
| asyncio_websockets            | 242 ms                                                 | 243 ms: 1.00x slower                                                  |
| pidigits                      | 280 ms                                                 | 285 ms: 1.02x slower                                                  |
| thrift                        | 562 us                                                 | 571 us: 1.02x slower                                                  |
| xml_etree_iterparse           | 74.5 ms                                                | 76.0 ms: 1.02x slower                                                 |
| xml_etree_parse               | 109 ms                                                 | 112 ms: 1.02x slower                                                  |
| python_startup                | 19.6 ms                                                | 20.2 ms: 1.03x slower                                                 |
| fannkuch                      | 303 ms                                                 | 311 ms: 1.03x slower                                                  |
| shortest_path                 | 328 ms                                                 | 340 ms: 1.03x slower                                                  |
| django_template               | 24.4 ms                                                | 25.5 ms: 1.05x slower                                                 |
| nqueens                       | 63.8 ms                                                | 67.5 ms: 1.06x slower                                                 |
| bpe_tokeniser                 | 3.44 sec                                               | 3.65 sec: 1.06x slower                                                |
| sympy_expand                  | 269 ms                                                 | 286 ms: 1.06x slower                                                  |
| many_optionals                | 486 us                                                 | 520 us: 1.07x slower                                                  |
| gc_traversal                  | 2.71 ms                                                | 3.20 ms: 1.18x slower                                                 |
| scimark_fft                   | 225 ms                                                 | 267 ms: 1.18x slower                                                  |
| create_gc_cycles              | 1.16 ms                                                | 1.39 ms: 1.19x slower                                                 |
| python_startup_no_site        | 12.8 ms                                                | 15.3 ms: 1.20x slower                                                 |
| xml_etree_generate            | 53.9 ms                                                | 65.2 ms: 1.21x slower                                                 |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 4.19 ms: 1.23x slower                                                 |
| json                          | 3.10 ms                                                | 3.83 ms: 1.23x slower                                                 |
| sqlite_synth                  | 1.48 us                                                | 1.89 us: 1.27x slower                                                 |
| async_generators              | 233 ms                                                 | 310 ms: 1.33x slower                                                  |
| bench_mp_pool                 | 56.0 ms                                                | 75.5 ms: 1.35x slower                                                 |
| json_loads                    | 16.6 us                                                | 22.7 us: 1.37x slower                                                 |
| coverage                      | 41.2 ms                                                | 59.8 ms: 1.45x slower                                                 |
| telco                         | 3.49 ms                                                | 5.50 ms: 1.58x slower                                                 |
| logging_silent                | 117 ns                                                 | 413 ns: 3.53x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.20x faster                                                          |
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (20) of results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.221x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.14x