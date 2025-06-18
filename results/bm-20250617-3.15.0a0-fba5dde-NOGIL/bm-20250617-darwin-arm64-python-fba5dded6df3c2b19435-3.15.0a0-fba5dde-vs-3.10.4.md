# Results vs. 3.10.4

- fork: python
- ref: fba5dded6df3c2b19435
- machine: darwin-arm64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.158x faster
- HPT reliability: 99.49%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| docutils       | 1.74 sec                                               | 1.59 sec: 1.10x faster                                                |
| html5lib       | 43.5 ms                                                | 34.3 ms: 1.27x faster                                                 |
| sphinx         | 729 ms                                                 | 678 ms: 1.08x faster                                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                                          |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 81.9 ms: 4.78x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 148 ms: 3.26x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 332 ms: 3.05x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 343 ms: 2.97x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 198 ms: 2.43x faster                                                  |
| async_tree_none               | 391 ms                                                 | 164 ms: 2.39x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 391 ms: 1.71x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 432 ms: 1.55x faster                                                  |
| coroutines                    | 20.5 ms                                                | 18.0 ms: 1.14x faster                                                 |
| asyncio_websockets            | 242 ms                                                 | 238 ms: 1.02x faster                                                  |
| async_generators              | 233 ms                                                 | 324 ms: 1.39x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.98x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 48.6 ms: 1.49x faster                                                 |
| pidigits       | 280 ms                                                 | 281 ms: 1.00x slower                                                  |
| nbody          | 92.5 ms                                                | 93.1 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.14x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 175 ms                                                 | 145 ms: 1.21x faster                                                  |
| regex_compile  | 95.6 ms                                                | 83.7 ms: 1.14x faster                                                 |
| regex_v8       | 19.1 ms                                                | 17.1 ms: 1.12x faster                                                 |
| regex_effbot   | 2.34 ms                                                | 2.22 ms: 1.05x faster                                                 |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 285 us                                                 | 237 us: 1.20x faster                                                  |
| unpickle_pure_python | 198 us                                                 | 169 us: 1.18x faster                                                  |
| tomli_loads          | 1.72 sec                                               | 1.55 sec: 1.11x faster                                                |
| xml_etree_iterparse  | 74.5 ms                                                | 69.2 ms: 1.08x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 111 ms: 1.02x slower                                                  |
| xml_etree_process    | 44.6 ms                                                | 50.0 ms: 1.12x slower                                                 |
| xml_etree_generate   | 53.9 ms                                                | 72.5 ms: 1.34x slower                                                 |
| json_loads           | 16.6 us                                                | 24.5 us: 1.48x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.03x slower                                                          |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 20.5 ms: 1.04x slower                                                 |
| python_startup_no_site | 12.8 ms                                                | 15.5 ms: 1.21x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 17.7 ms                                                | 18.4 ms: 1.04x slower                                                 |
| mako            | 9.81 ms                                                | 10.8 ms: 1.10x slower                                                 |
| genshi_xml      | 35.1 ms                                                | 39.3 ms: 1.12x slower                                                 |
| django_template | 24.4 ms                                                | 28.4 ms: 1.16x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.11x slower                                                          |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 81.9 ms: 4.78x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 148 ms: 3.26x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 332 ms: 3.05x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 343 ms: 2.97x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 198 ms: 2.43x faster                                                  |
| async_tree_none               | 391 ms                                                 | 164 ms: 2.39x faster                                                  |
| subparsers                    | 39.8 ms                                                | 17.0 ms: 2.34x faster                                                 |
| typing_runtime_protocols      | 326 us                                                 | 140 us: 2.32x faster                                                  |
| go                            | 163 ms                                                 | 84.2 ms: 1.94x faster                                                 |
| gc_traversal                  | 2.71 ms                                                | 1.41 ms: 1.91x faster                                                 |
| deltablue                     | 4.99 ms                                                | 2.70 ms: 1.85x faster                                                 |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 391 ms: 1.71x faster                                                  |
| mdp                           | 1.65 sec                                               | 993 ms: 1.66x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 22.1 us: 1.57x faster                                                 |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 432 ms: 1.55x faster                                                  |
| float                         | 72.4 ms                                                | 48.6 ms: 1.49x faster                                                 |
| pyflate                       | 448 ms                                                 | 316 ms: 1.42x faster                                                  |
| scimark_sor                   | 140 ms                                                 | 99.3 ms: 1.41x faster                                                 |
| chaos                         | 67.7 ms                                                | 48.2 ms: 1.40x faster                                                 |
| raytrace                      | 327 ms                                                 | 235 ms: 1.39x faster                                                  |
| create_gc_cycles              | 1.16 ms                                                | 859 us: 1.35x faster                                                  |
| generators                    | 31.7 ms                                                | 24.0 ms: 1.32x faster                                                 |
| scimark_monte_carlo           | 72.4 ms                                                | 54.9 ms: 1.32x faster                                                 |
| richards_super                | 61.0 ms                                                | 46.4 ms: 1.31x faster                                                 |
| deepcopy                      | 276 us                                                 | 213 us: 1.30x faster                                                  |
| richards                      | 52.3 ms                                                | 40.4 ms: 1.29x faster                                                 |
| html5lib                      | 43.5 ms                                                | 34.3 ms: 1.27x faster                                                 |
| hexiom                        | 6.25 ms                                                | 4.99 ms: 1.25x faster                                                 |
| dulwich_log                   | 35.6 ms                                                | 28.6 ms: 1.24x faster                                                 |
| pylint                        | 231 ms                                                 | 189 ms: 1.22x faster                                                  |
| k_core                        | 2.01 sec                                               | 1.65 sec: 1.22x faster                                                |
| regex_dna                     | 175 ms                                                 | 145 ms: 1.21x faster                                                  |
| pycparser                     | 887 ms                                                 | 739 ms: 1.20x faster                                                  |
| pickle_pure_python            | 285 us                                                 | 237 us: 1.20x faster                                                  |
| unpickle_pure_python          | 198 us                                                 | 169 us: 1.18x faster                                                  |
| regex_compile                 | 95.6 ms                                                | 83.7 ms: 1.14x faster                                                 |
| coroutines                    | 20.5 ms                                                | 18.0 ms: 1.14x faster                                                 |
| comprehensions                | 17.3 us                                                | 15.3 us: 1.13x faster                                                 |
| regex_v8                      | 19.1 ms                                                | 17.1 ms: 1.12x faster                                                 |
| tomli_loads                   | 1.72 sec                                               | 1.55 sec: 1.11x faster                                                |
| docutils                      | 1.74 sec                                               | 1.59 sec: 1.10x faster                                                |
| sphinx                        | 729 ms                                                 | 678 ms: 1.08x faster                                                  |
| xml_etree_iterparse           | 74.5 ms                                                | 69.2 ms: 1.08x faster                                                 |
| spectral_norm                 | 95.3 ms                                                | 89.6 ms: 1.06x faster                                                 |
| pathlib                       | 25.7 ms                                                | 24.5 ms: 1.05x faster                                                 |
| regex_effbot                  | 2.34 ms                                                | 2.22 ms: 1.05x faster                                                 |
| logging_simple                | 4.59 us                                                | 4.40 us: 1.04x faster                                                 |
| crypto_pyaes                  | 73.3 ms                                                | 70.3 ms: 1.04x faster                                                 |
| logging_format                | 5.03 us                                                | 4.84 us: 1.04x faster                                                 |
| scimark_lu                    | 103 ms                                                 | 99.9 ms: 1.03x faster                                                 |
| deepcopy_reduce               | 2.32 us                                                | 2.27 us: 1.02x faster                                                 |
| asyncio_websockets            | 242 ms                                                 | 238 ms: 1.02x faster                                                  |
| sympy_integrate               | 13.2 ms                                                | 13.0 ms: 1.01x faster                                                 |
| pidigits                      | 280 ms                                                 | 281 ms: 1.00x slower                                                  |
| sympy_sum                     | 92.7 ms                                                | 93.1 ms: 1.00x slower                                                 |
| connected_components          | 318 ms                                                 | 320 ms: 1.01x slower                                                  |
| nbody                         | 92.5 ms                                                | 93.1 ms: 1.01x slower                                                 |
| xml_etree_parse               | 109 ms                                                 | 111 ms: 1.02x slower                                                  |
| genshi_text                   | 17.7 ms                                                | 18.4 ms: 1.04x slower                                                 |
| python_startup                | 19.6 ms                                                | 20.5 ms: 1.04x slower                                                 |
| pprint_pformat                | 1.33 sec                                               | 1.39 sec: 1.05x slower                                                |
| bpe_tokeniser                 | 3.44 sec                                               | 3.61 sec: 1.05x slower                                                |
| shortest_path                 | 328 ms                                                 | 346 ms: 1.05x slower                                                  |
| pprint_safe_repr              | 648 ms                                                 | 684 ms: 1.06x slower                                                  |
| meteor_contest                | 77.8 ms                                                | 82.8 ms: 1.06x slower                                                 |
| sqlite_synth                  | 1.48 us                                                | 1.62 us: 1.10x slower                                                 |
| mako                          | 9.81 ms                                                | 10.8 ms: 1.10x slower                                                 |
| sympy_str                     | 166 ms                                                 | 184 ms: 1.11x slower                                                  |
| genshi_xml                    | 35.1 ms                                                | 39.3 ms: 1.12x slower                                                 |
| xml_etree_process             | 44.6 ms                                                | 50.0 ms: 1.12x slower                                                 |
| nqueens                       | 63.8 ms                                                | 71.7 ms: 1.12x slower                                                 |
| many_optionals                | 486 us                                                 | 546 us: 1.12x slower                                                  |
| thrift                        | 562 us                                                 | 635 us: 1.13x slower                                                  |
| fannkuch                      | 303 ms                                                 | 348 ms: 1.15x slower                                                  |
| django_template               | 24.4 ms                                                | 28.4 ms: 1.16x slower                                                 |
| sympy_expand                  | 269 ms                                                 | 325 ms: 1.21x slower                                                  |
| python_startup_no_site        | 12.8 ms                                                | 15.5 ms: 1.21x slower                                                 |
| scimark_fft                   | 225 ms                                                 | 280 ms: 1.24x slower                                                  |
| json                          | 3.10 ms                                                | 4.04 ms: 1.30x slower                                                 |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 4.50 ms: 1.32x slower                                                 |
| xml_etree_generate            | 53.9 ms                                                | 72.5 ms: 1.34x slower                                                 |
| bench_mp_pool                 | 56.0 ms                                                | 77.6 ms: 1.39x slower                                                 |
| async_generators              | 233 ms                                                 | 324 ms: 1.39x slower                                                  |
| bench_thread_pool             | 545 us                                                 | 780 us: 1.43x slower                                                  |
| json_loads                    | 16.6 us                                                | 24.5 us: 1.48x slower                                                 |
| telco                         | 3.49 ms                                                | 6.14 ms: 1.76x slower                                                 |
| coverage                      | 41.2 ms                                                | 75.3 ms: 1.83x slower                                                 |
| logging_silent                | 117 ns                                                 | 442 ns: 3.78x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.14x faster                                                          |

Benchmark hidden because not significant (3): dask, 2to3, json_dumps
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (20) of results/bm-20250617-3.15.0a0-fba5dde-NOGIL/bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.158x faster

# HPT report

- Reliability score: 99.49% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.33x