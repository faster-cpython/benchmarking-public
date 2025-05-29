# Results vs. base

- fork: python
- ref: 009e7b36981fd07f7cca
- machine: linux-x86_64
- commit hash: 009e7b3
- commit date: 2025-05-18
- overall geometric mean: 1.027x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250518-3.15.0a0-009e7b3/bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json | results/bm-20250518-3.15.0a0-009e7b3-CLANG/bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                                                                          | 253 ms: 1.01x faster                                                                                                  |
| docutils       | 2.61 sec                                                                                                        | 2.62 sec: 1.00x slower                                                                                                |
| Geometric mean | (ref)                                                                                                           | 1.01x faster                                                                                                          |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | results/bm-20250518-3.15.0a0-009e7b3/bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json | results/bm-20250518-3.15.0a0-009e7b3-CLANG/bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json |
|----------------------------------|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| coroutines                       | 25.0 ms                                                                                                         | 22.4 ms: 1.12x faster                                                                                                 |
| async_tree_eager                 | 102 ms                                                                                                          | 98.1 ms: 1.04x faster                                                                                                 |
| async_generators                 | 406 ms                                                                                                          | 392 ms: 1.03x faster                                                                                                  |
| asyncio_tcp                      | 487 ms                                                                                                          | 479 ms: 1.02x faster                                                                                                  |
| async_tree_memoization           | 312 ms                                                                                                          | 308 ms: 1.01x faster                                                                                                  |
| async_tree_none_tg               | 249 ms                                                                                                          | 246 ms: 1.01x faster                                                                                                  |
| async_tree_eager_memoization     | 199 ms                                                                                                          | 197 ms: 1.01x faster                                                                                                  |
| async_tree_io                    | 593 ms                                                                                                          | 587 ms: 1.01x faster                                                                                                  |
| asyncio_tcp_ssl                  | 1.80 sec                                                                                                        | 1.79 sec: 1.01x faster                                                                                                |
| async_tree_cpu_io_mixed          | 489 ms                                                                                                          | 502 ms: 1.03x slower                                                                                                  |
| async_tree_cpu_io_mixed_tg       | 482 ms                                                                                                          | 496 ms: 1.03x slower                                                                                                  |
| async_tree_eager_cpu_io_mixed    | 381 ms                                                                                                          | 395 ms: 1.04x slower                                                                                                  |
| async_tree_eager_cpu_io_mixed_tg | 455 ms                                                                                                          | 475 ms: 1.04x slower                                                                                                  |
| Geometric mean                   | (ref)                                                                                                           | 1.01x faster                                                                                                          |

Benchmark hidden because not significant (8): async_tree_eager_tg, async_tree_memoization_tg, async_tree_none, async_tree_eager_memoization_tg, async_tree_eager_io_tg, async_tree_io_tg, async_tree_eager_io, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250518-3.15.0a0-009e7b3/bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json | results/bm-20250518-3.15.0a0-009e7b3-CLANG/bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| nbody          | 101 ms                                                                                                          | 84.8 ms: 1.19x faster                                                                                                 |
| float          | 71.2 ms                                                                                                         | 67.4 ms: 1.06x faster                                                                                                 |
| pidigits       | 187 ms                                                                                                          | 203 ms: 1.08x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                           | 1.05x faster                                                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250518-3.15.0a0-009e7b3/bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json | results/bm-20250518-3.15.0a0-009e7b3-CLANG/bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 213 ms                                                                                                          | 198 ms: 1.08x faster                                                                                                  |
| regex_compile  | 127 ms                                                                                                          | 123 ms: 1.03x faster                                                                                                  |
| regex_effbot   | 3.40 ms                                                                                                         | 3.43 ms: 1.01x slower                                                                                                 |
| regex_v8       | 23.9 ms                                                                                                         | 25.1 ms: 1.05x slower                                                                                                 |
| Geometric mean | (ref)                                                                                                           | 1.01x faster                                                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250518-3.15.0a0-009e7b3/bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json | results/bm-20250518-3.15.0a0-009e7b3-CLANG/bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| unpickle_list        | 5.53 us                                                                                                         | 4.71 us: 1.17x faster                                                                                                 |
| tomli_loads          | 2.02 sec                                                                                                        | 1.88 sec: 1.07x faster                                                                                                |
| unpickle             | 14.9 us                                                                                                         | 14.1 us: 1.06x faster                                                                                                 |
| pickle_pure_python   | 321 us                                                                                                          | 305 us: 1.05x faster                                                                                                  |
| unpickle_pure_python | 220 us                                                                                                          | 210 us: 1.04x faster                                                                                                  |
| json_loads           | 29.6 us                                                                                                         | 29.8 us: 1.01x slower                                                                                                 |
| xml_etree_process    | 59.4 ms                                                                                                         | 59.8 ms: 1.01x slower                                                                                                 |
| xml_etree_generate   | 85.8 ms                                                                                                         | 88.0 ms: 1.03x slower                                                                                                 |
| xml_etree_iterparse  | 98.2 ms                                                                                                         | 102 ms: 1.04x slower                                                                                                  |
| pickle               | 12.7 us                                                                                                         | 13.3 us: 1.05x slower                                                                                                 |
| pickle_dict          | 33.0 us                                                                                                         | 34.7 us: 1.05x slower                                                                                                 |
| json_dumps           | 10.9 ms                                                                                                         | 11.9 ms: 1.09x slower                                                                                                 |
| xml_etree_parse      | 141 ms                                                                                                          | 160 ms: 1.13x slower                                                                                                  |
| Geometric mean       | (ref)                                                                                                           | 1.00x faster                                                                                                          |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250518-3.15.0a0-009e7b3/bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json | results/bm-20250518-3.15.0a0-009e7b3-CLANG/bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 12.2 ms                                                                                                         | 12.1 ms: 1.00x faster                                                                                                 |
| python_startup_no_site | 6.90 ms                                                                                                         | 6.93 ms: 1.00x slower                                                                                                 |
| Geometric mean         | (ref)                                                                                                           | 1.00x slower                                                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250518-3.15.0a0-009e7b3/bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json | results/bm-20250518-3.15.0a0-009e7b3-CLANG/bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 49.6 ms                                                                                                         | 48.0 ms: 1.03x faster                                                                                                 |
| genshi_text     | 21.2 ms                                                                                                         | 20.8 ms: 1.02x faster                                                                                                 |
| django_template | 32.0 ms                                                                                                         | 31.8 ms: 1.01x faster                                                                                                 |
| mako            | 11.7 ms                                                                                                         | 12.1 ms: 1.04x slower                                                                                                 |
| Geometric mean  | (ref)                                                                                                           | 1.01x faster                                                                                                          |

All benchmarks:
===============

| Benchmark                        | results/bm-20250518-3.15.0a0-009e7b3/bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json | results/bm-20250518-3.15.0a0-009e7b3-CLANG/bm-20250518-linux-x86_64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json |
|----------------------------------|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| scimark_fft                      | 376 ms                                                                                                          | 307 ms: 1.22x faster                                                                                                  |
| scimark_sparse_mat_mult          | 5.30 ms                                                                                                         | 4.38 ms: 1.21x faster                                                                                                 |
| nbody                            | 101 ms                                                                                                          | 84.8 ms: 1.19x faster                                                                                                 |
| spectral_norm                    | 111 ms                                                                                                          | 94.4 ms: 1.18x faster                                                                                                 |
| unpickle_list                    | 5.53 us                                                                                                         | 4.71 us: 1.17x faster                                                                                                 |
| scimark_monte_carlo              | 68.4 ms                                                                                                         | 59.2 ms: 1.16x faster                                                                                                 |
| deltablue                        | 3.41 ms                                                                                                         | 2.95 ms: 1.16x faster                                                                                                 |
| pathlib                          | 17.5 ms                                                                                                         | 15.2 ms: 1.15x faster                                                                                                 |
| scimark_sor                      | 122 ms                                                                                                          | 107 ms: 1.14x faster                                                                                                  |
| coroutines                       | 25.0 ms                                                                                                         | 22.4 ms: 1.12x faster                                                                                                 |
| chaos                            | 59.7 ms                                                                                                         | 53.6 ms: 1.11x faster                                                                                                 |
| hexiom                           | 6.27 ms                                                                                                         | 5.67 ms: 1.10x faster                                                                                                 |
| telco                            | 7.94 ms                                                                                                         | 7.30 ms: 1.09x faster                                                                                                 |
| go                               | 115 ms                                                                                                          | 106 ms: 1.08x faster                                                                                                  |
| typing_runtime_protocols         | 172 us                                                                                                          | 159 us: 1.08x faster                                                                                                  |
| regex_dna                        | 213 ms                                                                                                          | 198 ms: 1.08x faster                                                                                                  |
| scimark_lu                       | 116 ms                                                                                                          | 108 ms: 1.08x faster                                                                                                  |
| raytrace                         | 272 ms                                                                                                          | 254 ms: 1.07x faster                                                                                                  |
| deepcopy                         | 263 us                                                                                                          | 245 us: 1.07x faster                                                                                                  |
| tomli_loads                      | 2.02 sec                                                                                                        | 1.88 sec: 1.07x faster                                                                                                |
| richards                         | 43.3 ms                                                                                                         | 40.4 ms: 1.07x faster                                                                                                 |
| generators                       | 30.1 ms                                                                                                         | 28.2 ms: 1.07x faster                                                                                                 |
| deepcopy_reduce                  | 2.72 us                                                                                                         | 2.55 us: 1.07x faster                                                                                                 |
| coverage                         | 424 ms                                                                                                          | 399 ms: 1.06x faster                                                                                                  |
| unpickle                         | 14.9 us                                                                                                         | 14.1 us: 1.06x faster                                                                                                 |
| float                            | 71.2 ms                                                                                                         | 67.4 ms: 1.06x faster                                                                                                 |
| richards_super                   | 49.6 ms                                                                                                         | 47.0 ms: 1.06x faster                                                                                                 |
| pickle_pure_python               | 321 us                                                                                                          | 305 us: 1.05x faster                                                                                                  |
| deepcopy_memo                    | 29.8 us                                                                                                         | 28.4 us: 1.05x faster                                                                                                 |
| bench_thread_pool                | 891 us                                                                                                          | 852 us: 1.05x faster                                                                                                  |
| unpickle_pure_python             | 220 us                                                                                                          | 210 us: 1.04x faster                                                                                                  |
| bpe_tokeniser                    | 4.49 sec                                                                                                        | 4.31 sec: 1.04x faster                                                                                                |
| sympy_integrate                  | 19.0 ms                                                                                                         | 18.3 ms: 1.04x faster                                                                                                 |
| comprehensions                   | 16.7 us                                                                                                         | 16.1 us: 1.04x faster                                                                                                 |
| async_tree_eager                 | 102 ms                                                                                                          | 98.1 ms: 1.04x faster                                                                                                 |
| sqlglot_v2_parse                 | 1.24 ms                                                                                                         | 1.20 ms: 1.03x faster                                                                                                 |
| async_generators                 | 406 ms                                                                                                          | 392 ms: 1.03x faster                                                                                                  |
| crypto_pyaes                     | 75.3 ms                                                                                                         | 72.9 ms: 1.03x faster                                                                                                 |
| dask                             | 915 ms                                                                                                          | 886 ms: 1.03x faster                                                                                                  |
| sqlite_synth                     | 2.85 us                                                                                                         | 2.76 us: 1.03x faster                                                                                                 |
| genshi_xml                       | 49.6 ms                                                                                                         | 48.0 ms: 1.03x faster                                                                                                 |
| sympy_expand                     | 457 ms                                                                                                          | 443 ms: 1.03x faster                                                                                                  |
| regex_compile                    | 127 ms                                                                                                          | 123 ms: 1.03x faster                                                                                                  |
| sympy_sum                        | 148 ms                                                                                                          | 144 ms: 1.03x faster                                                                                                  |
| dulwich_log                      | 59.7 ms                                                                                                         | 57.9 ms: 1.03x faster                                                                                                 |
| pyflate                          | 432 ms                                                                                                          | 420 ms: 1.03x faster                                                                                                  |
| nqueens                          | 81.4 ms                                                                                                         | 79.2 ms: 1.03x faster                                                                                                 |
| sqlglot_v2_transpile             | 1.54 ms                                                                                                         | 1.50 ms: 1.03x faster                                                                                                 |
| many_optionals                   | 976 us                                                                                                          | 952 us: 1.03x faster                                                                                                  |
| sympy_str                        | 266 ms                                                                                                          | 260 ms: 1.02x faster                                                                                                  |
| logging_simple                   | 6.10 us                                                                                                         | 5.96 us: 1.02x faster                                                                                                 |
| genshi_text                      | 21.2 ms                                                                                                         | 20.8 ms: 1.02x faster                                                                                                 |
| fannkuch                         | 412 ms                                                                                                          | 403 ms: 1.02x faster                                                                                                  |
| sqlglot_v2_normalize             | 105 ms                                                                                                          | 103 ms: 1.02x faster                                                                                                  |
| subparsers                       | 23.8 ms                                                                                                         | 23.3 ms: 1.02x faster                                                                                                 |
| asyncio_tcp                      | 487 ms                                                                                                          | 479 ms: 1.02x faster                                                                                                  |
| mdp                              | 1.23 sec                                                                                                        | 1.21 sec: 1.01x faster                                                                                                |
| async_tree_memoization           | 312 ms                                                                                                          | 308 ms: 1.01x faster                                                                                                  |
| 2to3                             | 257 ms                                                                                                          | 253 ms: 1.01x faster                                                                                                  |
| async_tree_none_tg               | 249 ms                                                                                                          | 246 ms: 1.01x faster                                                                                                  |
| async_tree_eager_memoization     | 199 ms                                                                                                          | 197 ms: 1.01x faster                                                                                                  |
| logging_format                   | 6.79 us                                                                                                         | 6.72 us: 1.01x faster                                                                                                 |
| async_tree_io                    | 593 ms                                                                                                          | 587 ms: 1.01x faster                                                                                                  |
| django_template                  | 32.0 ms                                                                                                         | 31.8 ms: 1.01x faster                                                                                                 |
| bench_mp_pool                    | 93.4 ms                                                                                                         | 92.7 ms: 1.01x faster                                                                                                 |
| sqlglot_v2_optimize              | 52.0 ms                                                                                                         | 51.6 ms: 1.01x faster                                                                                                 |
| asyncio_tcp_ssl                  | 1.80 sec                                                                                                        | 1.79 sec: 1.01x faster                                                                                                |
| python_startup                   | 12.2 ms                                                                                                         | 12.1 ms: 1.00x faster                                                                                                 |
| docutils                         | 2.61 sec                                                                                                        | 2.62 sec: 1.00x slower                                                                                                |
| unpack_sequence                  | 51.0 ns                                                                                                         | 51.2 ns: 1.00x slower                                                                                                 |
| python_startup_no_site           | 6.90 ms                                                                                                         | 6.93 ms: 1.00x slower                                                                                                 |
| json_loads                       | 29.6 us                                                                                                         | 29.8 us: 1.01x slower                                                                                                 |
| xml_etree_process                | 59.4 ms                                                                                                         | 59.8 ms: 1.01x slower                                                                                                 |
| regex_effbot                     | 3.40 ms                                                                                                         | 3.43 ms: 1.01x slower                                                                                                 |
| gc_traversal                     | 4.88 ms                                                                                                         | 4.97 ms: 1.02x slower                                                                                                 |
| connected_components             | 455 ms                                                                                                          | 465 ms: 1.02x slower                                                                                                  |
| shortest_path                    | 490 ms                                                                                                          | 502 ms: 1.02x slower                                                                                                  |
| xml_etree_generate               | 85.8 ms                                                                                                         | 88.0 ms: 1.03x slower                                                                                                 |
| async_tree_cpu_io_mixed          | 489 ms                                                                                                          | 502 ms: 1.03x slower                                                                                                  |
| async_tree_cpu_io_mixed_tg       | 482 ms                                                                                                          | 496 ms: 1.03x slower                                                                                                  |
| pycparser                        | 1.14 sec                                                                                                        | 1.17 sec: 1.03x slower                                                                                                |
| create_gc_cycles                 | 2.56 ms                                                                                                         | 2.64 ms: 1.03x slower                                                                                                 |
| pprint_pformat                   | 1.49 sec                                                                                                        | 1.54 sec: 1.03x slower                                                                                                |
| pprint_safe_repr                 | 730 ms                                                                                                          | 756 ms: 1.03x slower                                                                                                  |
| mako                             | 11.7 ms                                                                                                         | 12.1 ms: 1.04x slower                                                                                                 |
| async_tree_eager_cpu_io_mixed    | 381 ms                                                                                                          | 395 ms: 1.04x slower                                                                                                  |
| xml_etree_iterparse              | 98.2 ms                                                                                                         | 102 ms: 1.04x slower                                                                                                  |
| async_tree_eager_cpu_io_mixed_tg | 455 ms                                                                                                          | 475 ms: 1.04x slower                                                                                                  |
| pickle                           | 12.7 us                                                                                                         | 13.3 us: 1.05x slower                                                                                                 |
| meteor_contest                   | 108 ms                                                                                                          | 113 ms: 1.05x slower                                                                                                  |
| pickle_dict                      | 33.0 us                                                                                                         | 34.7 us: 1.05x slower                                                                                                 |
| regex_v8                         | 23.9 ms                                                                                                         | 25.1 ms: 1.05x slower                                                                                                 |
| logging_silent                   | 471 ns                                                                                                          | 503 ns: 1.07x slower                                                                                                  |
| pidigits                         | 187 ms                                                                                                          | 203 ms: 1.08x slower                                                                                                  |
| json_dumps                       | 10.9 ms                                                                                                         | 11.9 ms: 1.09x slower                                                                                                 |
| xml_etree_parse                  | 141 ms                                                                                                          | 160 ms: 1.13x slower                                                                                                  |
| Geometric mean                   | (ref)                                                                                                           | 1.03x faster                                                                                                          |

Benchmark hidden because not significant (15): async_tree_eager_tg, async_tree_memoization_tg, async_tree_none, async_tree_eager_memoization_tg, sphinx, async_tree_eager_io_tg, html5lib, pylint, async_tree_io_tg, pickle_list, thrift, async_tree_eager_io, asyncio_websockets, k_core, json

- Geometric mean (including insignificant results): 1.027x faster

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x