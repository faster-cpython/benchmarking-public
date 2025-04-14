# Results vs. base

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: darwin-arm64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.022x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 203 ms                                                                                                            | 170 ms: 1.19x faster                                                                                                  |
| docutils       | 1.48 sec                                                                                                          | 1.48 sec: 1.01x slower                                                                                                |
| html5lib       | 32.6 ms                                                                                                           | 32.3 ms: 1.01x faster                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.05x faster                                                                                                          |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|----------------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| async_tree_memoization_tg        | 204 ms                                                                                                            | 198 ms: 1.03x faster                                                                                                  |
| async_tree_none                  | 171 ms                                                                                                            | 167 ms: 1.02x faster                                                                                                  |
| async_tree_none_tg               | 164 ms                                                                                                            | 161 ms: 1.02x faster                                                                                                  |
| async_tree_eager_memoization_tg  | 180 ms                                                                                                            | 177 ms: 1.02x faster                                                                                                  |
| async_tree_eager_io              | 392 ms                                                                                                            | 385 ms: 1.02x faster                                                                                                  |
| async_tree_memoization           | 205 ms                                                                                                            | 202 ms: 1.02x faster                                                                                                  |
| async_tree_io                    | 397 ms                                                                                                            | 391 ms: 1.01x faster                                                                                                  |
| async_tree_eager_cpu_io_mixed_tg | 395 ms                                                                                                            | 392 ms: 1.01x faster                                                                                                  |
| async_tree_cpu_io_mixed_tg       | 419 ms                                                                                                            | 417 ms: 1.01x faster                                                                                                  |
| async_tree_cpu_io_mixed          | 419 ms                                                                                                            | 416 ms: 1.01x faster                                                                                                  |
| async_tree_io_tg                 | 383 ms                                                                                                            | 381 ms: 1.01x faster                                                                                                  |
| async_tree_eager                 | 65.7 ms                                                                                                           | 65.4 ms: 1.00x faster                                                                                                 |
| asyncio_tcp                      | 426 ms                                                                                                            | 452 ms: 1.06x slower                                                                                                  |
| async_generators                 | 264 ms                                                                                                            | 283 ms: 1.07x slower                                                                                                  |
| Geometric mean                   | (ref)                                                                                                             | 1.00x faster                                                                                                          |

Benchmark hidden because not significant (7): async_tree_eager_tg, async_tree_eager_io_tg, asyncio_tcp_ssl, async_tree_eager_cpu_io_mixed, async_tree_eager_memoization, coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| nbody          | 81.1 ms                                                                                                           | 69.6 ms: 1.17x faster                                                                                                 |
| float          | 52.7 ms                                                                                                           | 45.7 ms: 1.15x faster                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.10x faster                                                                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 74.9 ms                                                                                                           | 73.5 ms: 1.02x faster                                                                                                 |
| regex_dna      | 141 ms                                                                                                            | 140 ms: 1.00x faster                                                                                                  |
| regex_v8       | 15.7 ms                                                                                                           | 15.9 ms: 1.01x slower                                                                                                 |
| regex_effbot   | 2.24 ms                                                                                                           | 2.27 ms: 1.01x slower                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.00x slower                                                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 165 us                                                                                                            | 140 us: 1.18x faster                                                                                                  |
| tomli_loads          | 1.40 sec                                                                                                          | 1.25 sec: 1.12x faster                                                                                                |
| xml_etree_process    | 40.9 ms                                                                                                           | 36.5 ms: 1.12x faster                                                                                                 |
| xml_etree_generate   | 56.2 ms                                                                                                           | 51.4 ms: 1.09x faster                                                                                                 |
| pickle_pure_python   | 221 us                                                                                                            | 212 us: 1.05x faster                                                                                                  |
| xml_etree_parse      | 103 ms                                                                                                            | 99.1 ms: 1.04x faster                                                                                                 |
| unpickle             | 9.55 us                                                                                                           | 9.26 us: 1.03x faster                                                                                                 |
| unpickle_list        | 2.98 us                                                                                                           | 2.93 us: 1.02x faster                                                                                                 |
| xml_etree_iterparse  | 73.5 ms                                                                                                           | 72.5 ms: 1.01x faster                                                                                                 |
| json_loads           | 17.9 us                                                                                                           | 17.8 us: 1.00x faster                                                                                                 |
| json_dumps           | 7.48 ms                                                                                                           | 7.53 ms: 1.01x slower                                                                                                 |
| pickle_dict          | 18.0 us                                                                                                           | 18.1 us: 1.01x slower                                                                                                 |
| Geometric mean       | (ref)                                                                                                             | 1.05x faster                                                                                                          |

Benchmark hidden because not significant (2): pickle_list, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 13.7 ms                                                                                                           | 14.2 ms: 1.04x slower                                                                                                 |
| python_startup         | 17.9 ms                                                                                                           | 18.7 ms: 1.04x slower                                                                                                 |
| Geometric mean         | (ref)                                                                                                             | 1.04x slower                                                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako            | 7.83 ms                                                                                                           | 6.69 ms: 1.17x faster                                                                                                 |
| genshi_text     | 15.6 ms                                                                                                           | 15.4 ms: 1.01x faster                                                                                                 |
| genshi_xml      | 32.2 ms                                                                                                           | 32.1 ms: 1.01x faster                                                                                                 |
| django_template | 22.8 ms                                                                                                           | 22.7 ms: 1.00x faster                                                                                                 |
| Geometric mean  | (ref)                                                                                                             | 1.05x faster                                                                                                          |

All benchmarks:
===============

| Benchmark                        | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|----------------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| spectral_norm                    | 79.5 ms                                                                                                           | 64.3 ms: 1.24x faster                                                                                                 |
| 2to3                             | 203 ms                                                                                                            | 170 ms: 1.19x faster                                                                                                  |
| richards                         | 37.4 ms                                                                                                           | 31.7 ms: 1.18x faster                                                                                                 |
| richards_super                   | 41.6 ms                                                                                                           | 35.3 ms: 1.18x faster                                                                                                 |
| unpickle_pure_python             | 165 us                                                                                                            | 140 us: 1.18x faster                                                                                                  |
| mako                             | 7.83 ms                                                                                                           | 6.69 ms: 1.17x faster                                                                                                 |
| nbody                            | 81.1 ms                                                                                                           | 69.6 ms: 1.17x faster                                                                                                 |
| float                            | 52.7 ms                                                                                                           | 45.7 ms: 1.15x faster                                                                                                 |
| deltablue                        | 2.63 ms                                                                                                           | 2.29 ms: 1.15x faster                                                                                                 |
| tomli_loads                      | 1.40 sec                                                                                                          | 1.25 sec: 1.12x faster                                                                                                |
| xml_etree_process                | 40.9 ms                                                                                                           | 36.5 ms: 1.12x faster                                                                                                 |
| bpe_tokeniser                    | 3.30 sec                                                                                                          | 3.02 sec: 1.09x faster                                                                                                |
| xml_etree_generate               | 56.2 ms                                                                                                           | 51.4 ms: 1.09x faster                                                                                                 |
| pyflate                          | 350 ms                                                                                                            | 321 ms: 1.09x faster                                                                                                  |
| fannkuch                         | 303 ms                                                                                                            | 287 ms: 1.06x faster                                                                                                  |
| nqueens                          | 69.2 ms                                                                                                           | 66.0 ms: 1.05x faster                                                                                                 |
| pickle_pure_python               | 221 us                                                                                                            | 212 us: 1.05x faster                                                                                                  |
| xml_etree_parse                  | 103 ms                                                                                                            | 99.1 ms: 1.04x faster                                                                                                 |
| connected_components             | 316 ms                                                                                                            | 304 ms: 1.04x faster                                                                                                  |
| comprehensions                   | 12.9 us                                                                                                           | 12.4 us: 1.04x faster                                                                                                 |
| telco                            | 4.63 ms                                                                                                           | 4.49 ms: 1.03x faster                                                                                                 |
| unpickle                         | 9.55 us                                                                                                           | 9.26 us: 1.03x faster                                                                                                 |
| scimark_fft                      | 194 ms                                                                                                            | 189 ms: 1.03x faster                                                                                                  |
| async_tree_memoization_tg        | 204 ms                                                                                                            | 198 ms: 1.03x faster                                                                                                  |
| k_core                           | 1.60 sec                                                                                                          | 1.55 sec: 1.03x faster                                                                                                |
| mdp                              | 1.52 sec                                                                                                          | 1.48 sec: 1.03x faster                                                                                                |
| async_tree_none                  | 171 ms                                                                                                            | 167 ms: 1.02x faster                                                                                                  |
| json                             | 3.14 ms                                                                                                           | 3.07 ms: 1.02x faster                                                                                                 |
| shortest_path                    | 342 ms                                                                                                            | 336 ms: 1.02x faster                                                                                                  |
| regex_compile                    | 74.9 ms                                                                                                           | 73.5 ms: 1.02x faster                                                                                                 |
| async_tree_none_tg               | 164 ms                                                                                                            | 161 ms: 1.02x faster                                                                                                  |
| async_tree_eager_memoization_tg  | 180 ms                                                                                                            | 177 ms: 1.02x faster                                                                                                  |
| typing_runtime_protocols         | 100.0 us                                                                                                          | 98.3 us: 1.02x faster                                                                                                 |
| sympy_sum                        | 77.3 ms                                                                                                           | 76.1 ms: 1.02x faster                                                                                                 |
| unpickle_list                    | 2.98 us                                                                                                           | 2.93 us: 1.02x faster                                                                                                 |
| async_tree_eager_io              | 392 ms                                                                                                            | 385 ms: 1.02x faster                                                                                                  |
| async_tree_memoization           | 205 ms                                                                                                            | 202 ms: 1.02x faster                                                                                                  |
| scimark_monte_carlo              | 47.0 ms                                                                                                           | 46.3 ms: 1.02x faster                                                                                                 |
| async_tree_io                    | 397 ms                                                                                                            | 391 ms: 1.01x faster                                                                                                  |
| meteor_contest                   | 76.9 ms                                                                                                           | 75.8 ms: 1.01x faster                                                                                                 |
| xml_etree_iterparse              | 73.5 ms                                                                                                           | 72.5 ms: 1.01x faster                                                                                                 |
| html5lib                         | 32.6 ms                                                                                                           | 32.3 ms: 1.01x faster                                                                                                 |
| sympy_str                        | 148 ms                                                                                                            | 146 ms: 1.01x faster                                                                                                  |
| pathlib                          | 24.1 ms                                                                                                           | 23.9 ms: 1.01x faster                                                                                                 |
| genshi_text                      | 15.6 ms                                                                                                           | 15.4 ms: 1.01x faster                                                                                                 |
| deepcopy_memo                    | 20.4 us                                                                                                           | 20.3 us: 1.01x faster                                                                                                 |
| scimark_sparse_mat_mult          | 3.10 ms                                                                                                           | 3.07 ms: 1.01x faster                                                                                                 |
| async_tree_eager_cpu_io_mixed_tg | 395 ms                                                                                                            | 392 ms: 1.01x faster                                                                                                  |
| async_tree_cpu_io_mixed_tg       | 419 ms                                                                                                            | 417 ms: 1.01x faster                                                                                                  |
| async_tree_cpu_io_mixed          | 419 ms                                                                                                            | 416 ms: 1.01x faster                                                                                                  |
| async_tree_io_tg                 | 383 ms                                                                                                            | 381 ms: 1.01x faster                                                                                                  |
| genshi_xml                       | 32.2 ms                                                                                                           | 32.1 ms: 1.01x faster                                                                                                 |
| django_template                  | 22.8 ms                                                                                                           | 22.7 ms: 1.00x faster                                                                                                 |
| json_loads                       | 17.9 us                                                                                                           | 17.8 us: 1.00x faster                                                                                                 |
| generators                       | 25.1 ms                                                                                                           | 25.0 ms: 1.00x faster                                                                                                 |
| async_tree_eager                 | 65.7 ms                                                                                                           | 65.4 ms: 1.00x faster                                                                                                 |
| raytrace                         | 192 ms                                                                                                            | 192 ms: 1.00x faster                                                                                                  |
| regex_dna                        | 141 ms                                                                                                            | 140 ms: 1.00x faster                                                                                                  |
| gc_traversal                     | 3.12 ms                                                                                                           | 3.13 ms: 1.00x slower                                                                                                 |
| sqlglot_v2_normalize             | 69.9 ms                                                                                                           | 70.2 ms: 1.00x slower                                                                                                 |
| sqlalchemy_declarative           | 61.1 ms                                                                                                           | 61.4 ms: 1.00x slower                                                                                                 |
| json_dumps                       | 7.48 ms                                                                                                           | 7.53 ms: 1.01x slower                                                                                                 |
| pickle_dict                      | 18.0 us                                                                                                           | 18.1 us: 1.01x slower                                                                                                 |
| logging_format                   | 3.90 us                                                                                                           | 3.92 us: 1.01x slower                                                                                                 |
| docutils                         | 1.48 sec                                                                                                          | 1.48 sec: 1.01x slower                                                                                                |
| sympy_integrate                  | 11.6 ms                                                                                                           | 11.7 ms: 1.01x slower                                                                                                 |
| deepcopy_reduce                  | 1.73 us                                                                                                           | 1.74 us: 1.01x slower                                                                                                 |
| subparsers                       | 12.7 ms                                                                                                           | 12.8 ms: 1.01x slower                                                                                                 |
| sqlglot_v2_optimize              | 34.7 ms                                                                                                           | 34.9 ms: 1.01x slower                                                                                                 |
| regex_v8                         | 15.7 ms                                                                                                           | 15.9 ms: 1.01x slower                                                                                                 |
| sympy_expand                     | 248 ms                                                                                                            | 250 ms: 1.01x slower                                                                                                  |
| hexiom                           | 5.01 ms                                                                                                           | 5.06 ms: 1.01x slower                                                                                                 |
| bench_mp_pool                    | 60.7 ms                                                                                                           | 61.4 ms: 1.01x slower                                                                                                 |
| sqlite_synth                     | 1.54 us                                                                                                           | 1.55 us: 1.01x slower                                                                                                 |
| pprint_pformat                   | 1.02 sec                                                                                                          | 1.04 sec: 1.01x slower                                                                                                |
| dulwich_log                      | 25.6 ms                                                                                                           | 25.9 ms: 1.01x slower                                                                                                 |
| scimark_lu                       | 78.9 ms                                                                                                           | 79.9 ms: 1.01x slower                                                                                                 |
| logging_silent                   | 70.4 ns                                                                                                           | 71.3 ns: 1.01x slower                                                                                                 |
| regex_effbot                     | 2.24 ms                                                                                                           | 2.27 ms: 1.01x slower                                                                                                 |
| sqlalchemy_imperative            | 6.84 ms                                                                                                           | 6.96 ms: 1.02x slower                                                                                                 |
| pycparser                        | 696 ms                                                                                                            | 713 ms: 1.02x slower                                                                                                  |
| coverage                         | 45.9 ms                                                                                                           | 47.1 ms: 1.02x slower                                                                                                 |
| python_startup_no_site           | 13.7 ms                                                                                                           | 14.2 ms: 1.04x slower                                                                                                 |
| python_startup                   | 17.9 ms                                                                                                           | 18.7 ms: 1.04x slower                                                                                                 |
| sqlglot_v2_transpile             | 1.03 ms                                                                                                           | 1.08 ms: 1.04x slower                                                                                                 |
| sqlglot_v2_parse                 | 860 us                                                                                                            | 904 us: 1.05x slower                                                                                                  |
| asyncio_tcp                      | 426 ms                                                                                                            | 452 ms: 1.06x slower                                                                                                  |
| async_generators                 | 264 ms                                                                                                            | 283 ms: 1.07x slower                                                                                                  |
| go                               | 92.7 ms                                                                                                           | 100 ms: 1.08x slower                                                                                                  |
| unpack_sequence                  | 52.5 ns                                                                                                           | 61.6 ns: 1.17x slower                                                                                                 |
| Geometric mean                   | (ref)                                                                                                             | 1.02x faster                                                                                                          |

Benchmark hidden because not significant (23): async_tree_eager_tg, async_tree_eager_io_tg, asyncio_tcp_ssl, bench_thread_pool, create_gc_cycles, async_tree_eager_cpu_io_mixed, async_tree_eager_memoization, pylint, scimark_sor, coroutines, asyncio_websockets, dask, pidigits, crypto_pyaes, pickle_list, deepcopy, chaos, pprint_safe_repr, logging_simple, thrift, pickle, many_optionals, sphinx

- Geometric mean (including insignificant results): 1.022x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x