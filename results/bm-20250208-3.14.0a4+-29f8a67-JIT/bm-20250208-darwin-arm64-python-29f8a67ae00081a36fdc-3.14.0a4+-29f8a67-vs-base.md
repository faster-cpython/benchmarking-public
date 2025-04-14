# Results vs. base

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: darwin-arm64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.008x slower
- HPT reliability: 99.23%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-JIT/bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 163 ms                                                                                                            | 167 ms: 1.03x slower                                                                                                  |
| docutils       | 1.41 sec                                                                                                          | 1.45 sec: 1.03x slower                                                                                                |
| Geometric mean | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-JIT/bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|-------------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| async_tree_io                 | 381 ms                                                                                                            | 372 ms: 1.03x faster                                                                                                  |
| coroutines                    | 15.9 ms                                                                                                           | 15.8 ms: 1.00x faster                                                                                                 |
| async_tree_eager_cpu_io_mixed | 360 ms                                                                                                            | 364 ms: 1.01x slower                                                                                                  |
| async_tree_eager_memoization  | 141 ms                                                                                                            | 145 ms: 1.03x slower                                                                                                  |
| async_tree_eager              | 62.6 ms                                                                                                           | 65.9 ms: 1.05x slower                                                                                                 |
| async_generators              | 252 ms                                                                                                            | 271 ms: 1.07x slower                                                                                                  |
| Geometric mean                | (ref)                                                                                                             | 1.00x slower                                                                                                          |

Benchmark hidden because not significant (15): async_tree_io_tg, async_tree_eager_tg, async_tree_none_tg, async_tree_none, async_tree_eager_memoization_tg, async_tree_eager_io_tg, async_tree_eager_io, asyncio_tcp, async_tree_memoization, async_tree_eager_cpu_io_mixed_tg, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-JIT/bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| nbody          | 71.1 ms                                                                                                           | 65.0 ms: 1.09x faster                                                                                                 |
| pidigits       | 283 ms                                                                                                            | 284 ms: 1.00x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.03x faster                                                                                                          |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-JIT/bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 2.36 ms                                                                                                           | 2.25 ms: 1.05x faster                                                                                                 |
| regex_dna      | 144 ms                                                                                                            | 140 ms: 1.03x faster                                                                                                  |
| regex_v8       | 17.1 ms                                                                                                           | 16.7 ms: 1.02x faster                                                                                                 |
| regex_compile  | 67.1 ms                                                                                                           | 67.8 ms: 1.01x slower                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.02x faster                                                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-JIT/bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 143 us                                                                                                            | 130 us: 1.10x faster                                                                                                  |
| xml_etree_process    | 38.6 ms                                                                                                           | 35.7 ms: 1.08x faster                                                                                                 |
| xml_etree_generate   | 53.4 ms                                                                                                           | 50.3 ms: 1.06x faster                                                                                                 |
| pickle_pure_python   | 199 us                                                                                                            | 194 us: 1.03x faster                                                                                                  |
| unpickle_list        | 2.94 us                                                                                                           | 2.89 us: 1.01x faster                                                                                                 |
| pickle               | 7.99 us                                                                                                           | 7.95 us: 1.00x faster                                                                                                 |
| pickle_dict          | 18.4 us                                                                                                           | 18.4 us: 1.00x faster                                                                                                 |
| json_dumps           | 7.29 ms                                                                                                           | 7.26 ms: 1.00x faster                                                                                                 |
| unpickle             | 9.03 us                                                                                                           | 9.08 us: 1.01x slower                                                                                                 |
| tomli_loads          | 1.20 sec                                                                                                          | 1.21 sec: 1.01x slower                                                                                                |
| Geometric mean       | (ref)                                                                                                             | 1.02x faster                                                                                                          |

Benchmark hidden because not significant (4): xml_etree_iterparse, json_loads, pickle_list, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-JIT/bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 18.6 ms                                                                                                           | 19.0 ms: 1.02x slower                                                                                                 |
| python_startup_no_site | 13.7 ms                                                                                                           | 14.1 ms: 1.03x slower                                                                                                 |
| Geometric mean         | (ref)                                                                                                             | 1.02x slower                                                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-JIT/bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako            | 7.37 ms                                                                                                           | 6.48 ms: 1.14x faster                                                                                                 |
| django_template | 20.8 ms                                                                                                           | 20.9 ms: 1.00x slower                                                                                                 |
| genshi_xml      | 28.4 ms                                                                                                           | 29.0 ms: 1.02x slower                                                                                                 |
| Geometric mean  | (ref)                                                                                                             | 1.03x faster                                                                                                          |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                     | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-JIT/bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|-------------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako                          | 7.37 ms                                                                                                           | 6.48 ms: 1.14x faster                                                                                                 |
| unpickle_pure_python          | 143 us                                                                                                            | 130 us: 1.10x faster                                                                                                  |
| nbody                         | 71.1 ms                                                                                                           | 65.0 ms: 1.09x faster                                                                                                 |
| xml_etree_process             | 38.6 ms                                                                                                           | 35.7 ms: 1.08x faster                                                                                                 |
| xml_etree_generate            | 53.4 ms                                                                                                           | 50.3 ms: 1.06x faster                                                                                                 |
| regex_effbot                  | 2.36 ms                                                                                                           | 2.25 ms: 1.05x faster                                                                                                 |
| async_tree_io                 | 381 ms                                                                                                            | 372 ms: 1.03x faster                                                                                                  |
| regex_dna                     | 144 ms                                                                                                            | 140 ms: 1.03x faster                                                                                                  |
| pickle_pure_python            | 199 us                                                                                                            | 194 us: 1.03x faster                                                                                                  |
| regex_v8                      | 17.1 ms                                                                                                           | 16.7 ms: 1.02x faster                                                                                                 |
| pyflate                       | 288 ms                                                                                                            | 283 ms: 1.02x faster                                                                                                  |
| telco                         | 4.55 ms                                                                                                           | 4.48 ms: 1.02x faster                                                                                                 |
| unpickle_list                 | 2.94 us                                                                                                           | 2.89 us: 1.01x faster                                                                                                 |
| logging_simple                | 3.19 us                                                                                                           | 3.14 us: 1.01x faster                                                                                                 |
| logging_format                | 3.49 us                                                                                                           | 3.44 us: 1.01x faster                                                                                                 |
| deepcopy_reduce               | 1.58 us                                                                                                           | 1.57 us: 1.01x faster                                                                                                 |
| coverage                      | 46.0 ms                                                                                                           | 45.7 ms: 1.01x faster                                                                                                 |
| scimark_monte_carlo           | 42.7 ms                                                                                                           | 42.5 ms: 1.00x faster                                                                                                 |
| pickle                        | 7.99 us                                                                                                           | 7.95 us: 1.00x faster                                                                                                 |
| bpe_tokeniser                 | 2.89 sec                                                                                                          | 2.87 sec: 1.00x faster                                                                                                |
| pickle_dict                   | 18.4 us                                                                                                           | 18.4 us: 1.00x faster                                                                                                 |
| coroutines                    | 15.9 ms                                                                                                           | 15.8 ms: 1.00x faster                                                                                                 |
| json_dumps                    | 7.29 ms                                                                                                           | 7.26 ms: 1.00x faster                                                                                                 |
| thrift                        | 436 us                                                                                                            | 435 us: 1.00x faster                                                                                                  |
| scimark_sor                   | 78.1 ms                                                                                                           | 77.9 ms: 1.00x faster                                                                                                 |
| pidigits                      | 283 ms                                                                                                            | 284 ms: 1.00x slower                                                                                                  |
| gc_traversal                  | 3.11 ms                                                                                                           | 3.11 ms: 1.00x slower                                                                                                 |
| deepcopy                      | 148 us                                                                                                            | 149 us: 1.00x slower                                                                                                  |
| scimark_fft                   | 172 ms                                                                                                            | 172 ms: 1.00x slower                                                                                                  |
| richards_super                | 35.9 ms                                                                                                           | 36.1 ms: 1.00x slower                                                                                                 |
| chaos                         | 38.9 ms                                                                                                           | 39.0 ms: 1.00x slower                                                                                                 |
| scimark_lu                    | 73.0 ms                                                                                                           | 73.3 ms: 1.00x slower                                                                                                 |
| django_template               | 20.8 ms                                                                                                           | 20.9 ms: 1.00x slower                                                                                                 |
| unpickle                      | 9.03 us                                                                                                           | 9.08 us: 1.01x slower                                                                                                 |
| json                          | 2.99 ms                                                                                                           | 3.00 ms: 1.01x slower                                                                                                 |
| pathlib                       | 22.9 ms                                                                                                           | 23.1 ms: 1.01x slower                                                                                                 |
| tomli_loads                   | 1.20 sec                                                                                                          | 1.21 sec: 1.01x slower                                                                                                |
| spectral_norm                 | 61.0 ms                                                                                                           | 61.6 ms: 1.01x slower                                                                                                 |
| regex_compile                 | 67.1 ms                                                                                                           | 67.8 ms: 1.01x slower                                                                                                 |
| sqlalchemy_declarative        | 58.1 ms                                                                                                           | 58.7 ms: 1.01x slower                                                                                                 |
| async_tree_eager_cpu_io_mixed | 360 ms                                                                                                            | 364 ms: 1.01x slower                                                                                                  |
| deltablue                     | 2.34 ms                                                                                                           | 2.36 ms: 1.01x slower                                                                                                 |
| go                            | 79.6 ms                                                                                                           | 80.6 ms: 1.01x slower                                                                                                 |
| bench_thread_pool             | 491 us                                                                                                            | 498 us: 1.01x slower                                                                                                  |
| crypto_pyaes                  | 52.5 ms                                                                                                           | 53.2 ms: 1.01x slower                                                                                                 |
| sqlite_synth                  | 1.52 us                                                                                                           | 1.54 us: 1.02x slower                                                                                                 |
| sympy_sum                     | 73.1 ms                                                                                                           | 74.5 ms: 1.02x slower                                                                                                 |
| sympy_str                     | 138 ms                                                                                                            | 141 ms: 1.02x slower                                                                                                  |
| python_startup                | 18.6 ms                                                                                                           | 19.0 ms: 1.02x slower                                                                                                 |
| genshi_xml                    | 28.4 ms                                                                                                           | 29.0 ms: 1.02x slower                                                                                                 |
| sqlglot_normalize             | 177 ms                                                                                                            | 181 ms: 1.02x slower                                                                                                  |
| sympy_expand                  | 232 ms                                                                                                            | 238 ms: 1.02x slower                                                                                                  |
| 2to3                          | 163 ms                                                                                                            | 167 ms: 1.03x slower                                                                                                  |
| connected_components          | 297 ms                                                                                                            | 304 ms: 1.03x slower                                                                                                  |
| mdp                           | 1.48 sec                                                                                                          | 1.51 sec: 1.03x slower                                                                                                |
| sympy_integrate               | 11.2 ms                                                                                                           | 11.5 ms: 1.03x slower                                                                                                 |
| docutils                      | 1.41 sec                                                                                                          | 1.45 sec: 1.03x slower                                                                                                |
| sqlglot_optimize              | 32.2 ms                                                                                                           | 33.1 ms: 1.03x slower                                                                                                 |
| python_startup_no_site        | 13.7 ms                                                                                                           | 14.1 ms: 1.03x slower                                                                                                 |
| dulwich_log                   | 27.3 ms                                                                                                           | 28.1 ms: 1.03x slower                                                                                                 |
| typing_runtime_protocols      | 92.4 us                                                                                                           | 95.1 us: 1.03x slower                                                                                                 |
| async_tree_eager_memoization  | 141 ms                                                                                                            | 145 ms: 1.03x slower                                                                                                  |
| k_core                        | 1.51 sec                                                                                                          | 1.56 sec: 1.03x slower                                                                                                |
| many_optionals                | 432 us                                                                                                            | 448 us: 1.04x slower                                                                                                  |
| sqlalchemy_imperative         | 6.43 ms                                                                                                           | 6.66 ms: 1.04x slower                                                                                                 |
| pycparser                     | 647 ms                                                                                                            | 673 ms: 1.04x slower                                                                                                  |
| meteor_contest                | 70.3 ms                                                                                                           | 73.4 ms: 1.04x slower                                                                                                 |
| hexiom                        | 4.31 ms                                                                                                           | 4.51 ms: 1.05x slower                                                                                                 |
| nqueens                       | 58.3 ms                                                                                                           | 61.2 ms: 1.05x slower                                                                                                 |
| fannkuch                      | 254 ms                                                                                                            | 266 ms: 1.05x slower                                                                                                  |
| async_tree_eager              | 62.6 ms                                                                                                           | 65.9 ms: 1.05x slower                                                                                                 |
| scimark_sparse_mat_mult       | 2.75 ms                                                                                                           | 2.89 ms: 1.05x slower                                                                                                 |
| comprehensions                | 11.8 us                                                                                                           | 12.5 us: 1.06x slower                                                                                                 |
| shortest_path                 | 325 ms                                                                                                            | 344 ms: 1.06x slower                                                                                                  |
| async_generators              | 252 ms                                                                                                            | 271 ms: 1.07x slower                                                                                                  |
| sqlglot_parse                 | 763 us                                                                                                            | 826 us: 1.08x slower                                                                                                  |
| sqlglot_transpile             | 919 us                                                                                                            | 996 us: 1.08x slower                                                                                                  |
| pprint_safe_repr              | 462 ms                                                                                                            | 508 ms: 1.10x slower                                                                                                  |
| pprint_pformat                | 931 ms                                                                                                            | 1.03 sec: 1.11x slower                                                                                                |
| unpack_sequence               | 49.3 ns                                                                                                           | 59.5 ns: 1.21x slower                                                                                                 |
| Geometric mean                | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (33): async_tree_io_tg, async_tree_eager_tg, xml_etree_iterparse, async_tree_none_tg, async_tree_none, async_tree_eager_memoization_tg, async_tree_eager_io_tg, async_tree_eager_io, asyncio_tcp, float, async_tree_memoization, dask, async_tree_eager_cpu_io_mixed_tg, json_loads, deepcopy_memo, generators, richards, genshi_text, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_memoization_tg, subparsers, create_gc_cycles, logging_silent, async_tree_cpu_io_mixed_tg, sphinx, raytrace, asyncio_tcp_ssl, pickle_list, xml_etree_parse, bench_mp_pool, html5lib, pylint

- Geometric mean (including insignificant results): 1.008x slower

# HPT report

- Reliability score: 99.23% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x