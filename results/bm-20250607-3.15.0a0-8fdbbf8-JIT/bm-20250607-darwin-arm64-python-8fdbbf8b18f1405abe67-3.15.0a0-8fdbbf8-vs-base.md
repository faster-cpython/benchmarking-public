# Results vs. base

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: darwin-arm64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.015x faster
- HPT reliability: 99.08%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 186 ms                                                                                                          | 185 ms: 1.00x faster                                                                                                |
| docutils       | 1.51 sec                                                                                                        | 1.52 sec: 1.01x slower                                                                                              |
| Geometric mean | (ref)                                                                                                           | 1.00x slower                                                                                                        |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                       | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|---------------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| async_tree_memoization          | 215 ms                                                                                                          | 208 ms: 1.03x faster                                                                                                |
| async_tree_none_tg              | 172 ms                                                                                                          | 166 ms: 1.03x faster                                                                                                |
| async_tree_none                 | 182 ms                                                                                                          | 178 ms: 1.02x faster                                                                                                |
| async_tree_eager_tg             | 143 ms                                                                                                          | 140 ms: 1.02x faster                                                                                                |
| async_tree_io_tg                | 405 ms                                                                                                          | 397 ms: 1.02x faster                                                                                                |
| async_tree_eager                | 73.0 ms                                                                                                         | 71.5 ms: 1.02x faster                                                                                               |
| async_tree_memoization_tg       | 207 ms                                                                                                          | 203 ms: 1.02x faster                                                                                                |
| async_tree_io                   | 413 ms                                                                                                          | 407 ms: 1.02x faster                                                                                                |
| async_tree_eager_memoization_tg | 182 ms                                                                                                          | 179 ms: 1.02x faster                                                                                                |
| async_tree_cpu_io_mixed         | 432 ms                                                                                                          | 428 ms: 1.01x faster                                                                                                |
| asyncio_websockets              | 242 ms                                                                                                          | 242 ms: 1.00x faster                                                                                                |
| async_generators                | 275 ms                                                                                                          | 289 ms: 1.05x slower                                                                                                |
| Geometric mean                  | (ref)                                                                                                           | 1.01x faster                                                                                                        |

Benchmark hidden because not significant (7): async_tree_eager_io_tg, async_tree_eager_io, async_tree_eager_memoization, async_tree_cpu_io_mixed_tg, coroutines, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| nbody          | 85.1 ms                                                                                                         | 76.3 ms: 1.12x faster                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.04x faster                                                                                                        |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 81.2 ms                                                                                                         | 79.6 ms: 1.02x faster                                                                                               |
| regex_dna      | 143 ms                                                                                                          | 143 ms: 1.00x faster                                                                                                |
| regex_v8       | 16.3 ms                                                                                                         | 16.3 ms: 1.00x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.00x faster                                                                                                        |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 177 us                                                                                                          | 138 us: 1.29x faster                                                                                                |
| xml_etree_process    | 43.0 ms                                                                                                         | 37.5 ms: 1.15x faster                                                                                               |
| xml_etree_generate   | 58.3 ms                                                                                                         | 51.9 ms: 1.12x faster                                                                                               |
| pickle_pure_python   | 242 us                                                                                                          | 226 us: 1.07x faster                                                                                                |
| tomli_loads          | 1.45 sec                                                                                                        | 1.36 sec: 1.06x faster                                                                                              |
| xml_etree_parse      | 104 ms                                                                                                          | 102 ms: 1.02x faster                                                                                                |
| xml_etree_iterparse  | 74.1 ms                                                                                                         | 73.7 ms: 1.01x faster                                                                                               |
| json_dumps           | 6.81 ms                                                                                                         | 6.85 ms: 1.01x slower                                                                                               |
| Geometric mean       | (ref)                                                                                                           | 1.07x faster                                                                                                        |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| mako            | 9.00 ms                                                                                                         | 6.93 ms: 1.30x faster                                                                                               |
| genshi_xml      | 36.4 ms                                                                                                         | 36.2 ms: 1.01x faster                                                                                               |
| django_template | 25.1 ms                                                                                                         | 25.3 ms: 1.01x slower                                                                                               |
| genshi_text     | 17.6 ms                                                                                                         | 17.7 ms: 1.01x slower                                                                                               |
| Geometric mean  | (ref)                                                                                                           | 1.07x faster                                                                                                        |

All benchmarks:
===============

| Benchmark                       | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|---------------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| mako                            | 9.00 ms                                                                                                         | 6.93 ms: 1.30x faster                                                                                               |
| unpickle_pure_python            | 177 us                                                                                                          | 138 us: 1.29x faster                                                                                                |
| xml_etree_process               | 43.0 ms                                                                                                         | 37.5 ms: 1.15x faster                                                                                               |
| xml_etree_generate              | 58.3 ms                                                                                                         | 51.9 ms: 1.12x faster                                                                                               |
| sqlglot_v2_parse                | 992 us                                                                                                          | 888 us: 1.12x faster                                                                                                |
| nbody                           | 85.1 ms                                                                                                         | 76.3 ms: 1.12x faster                                                                                               |
| sqlglot_v2_transpile            | 1.17 ms                                                                                                         | 1.08 ms: 1.09x faster                                                                                               |
| pprint_pformat                  | 1.27 sec                                                                                                        | 1.17 sec: 1.08x faster                                                                                              |
| pprint_safe_repr                | 623 ms                                                                                                          | 578 ms: 1.08x faster                                                                                                |
| pickle_pure_python              | 242 us                                                                                                          | 226 us: 1.07x faster                                                                                                |
| tomli_loads                     | 1.45 sec                                                                                                        | 1.36 sec: 1.06x faster                                                                                              |
| typing_runtime_protocols        | 110 us                                                                                                          | 104 us: 1.06x faster                                                                                                |
| bpe_tokeniser                   | 3.28 sec                                                                                                        | 3.11 sec: 1.05x faster                                                                                              |
| telco                           | 4.82 ms                                                                                                         | 4.60 ms: 1.05x faster                                                                                               |
| pyflate                         | 336 ms                                                                                                          | 321 ms: 1.05x faster                                                                                                |
| crypto_pyaes                    | 61.3 ms                                                                                                         | 58.9 ms: 1.04x faster                                                                                               |
| async_tree_memoization          | 215 ms                                                                                                          | 208 ms: 1.03x faster                                                                                                |
| async_tree_none_tg              | 172 ms                                                                                                          | 166 ms: 1.03x faster                                                                                                |
| nqueens                         | 71.4 ms                                                                                                         | 69.3 ms: 1.03x faster                                                                                               |
| async_tree_none                 | 182 ms                                                                                                          | 178 ms: 1.02x faster                                                                                                |
| async_tree_eager_tg             | 143 ms                                                                                                          | 140 ms: 1.02x faster                                                                                                |
| async_tree_io_tg                | 405 ms                                                                                                          | 397 ms: 1.02x faster                                                                                                |
| async_tree_eager                | 73.0 ms                                                                                                         | 71.5 ms: 1.02x faster                                                                                               |
| regex_compile                   | 81.2 ms                                                                                                         | 79.6 ms: 1.02x faster                                                                                               |
| async_tree_memoization_tg       | 207 ms                                                                                                          | 203 ms: 1.02x faster                                                                                                |
| async_tree_io                   | 413 ms                                                                                                          | 407 ms: 1.02x faster                                                                                                |
| xml_etree_parse                 | 104 ms                                                                                                          | 102 ms: 1.02x faster                                                                                                |
| async_tree_eager_memoization_tg | 182 ms                                                                                                          | 179 ms: 1.02x faster                                                                                                |
| sqlite_synth                    | 1.62 us                                                                                                         | 1.60 us: 1.01x faster                                                                                               |
| comprehensions                  | 13.1 us                                                                                                         | 13.0 us: 1.01x faster                                                                                               |
| async_tree_cpu_io_mixed         | 432 ms                                                                                                          | 428 ms: 1.01x faster                                                                                                |
| sympy_sum                       | 81.5 ms                                                                                                         | 80.8 ms: 1.01x faster                                                                                               |
| deepcopy                        | 176 us                                                                                                          | 174 us: 1.01x faster                                                                                                |
| mdp                             | 826 ms                                                                                                          | 820 ms: 1.01x faster                                                                                                |
| genshi_xml                      | 36.4 ms                                                                                                         | 36.2 ms: 1.01x faster                                                                                               |
| xml_etree_iterparse             | 74.1 ms                                                                                                         | 73.7 ms: 1.01x faster                                                                                               |
| scimark_sor                     | 91.2 ms                                                                                                         | 90.7 ms: 1.01x faster                                                                                               |
| 2to3                            | 186 ms                                                                                                          | 185 ms: 1.00x faster                                                                                                |
| coverage                        | 49.7 ms                                                                                                         | 49.5 ms: 1.00x faster                                                                                               |
| regex_dna                       | 143 ms                                                                                                          | 143 ms: 1.00x faster                                                                                                |
| asyncio_websockets              | 242 ms                                                                                                          | 242 ms: 1.00x faster                                                                                                |
| raytrace                        | 211 ms                                                                                                          | 211 ms: 1.00x faster                                                                                                |
| spectral_norm                   | 74.2 ms                                                                                                         | 74.3 ms: 1.00x slower                                                                                               |
| scimark_fft                     | 207 ms                                                                                                          | 207 ms: 1.00x slower                                                                                                |
| generators                      | 31.5 ms                                                                                                         | 31.6 ms: 1.00x slower                                                                                               |
| regex_v8                        | 16.3 ms                                                                                                         | 16.3 ms: 1.00x slower                                                                                               |
| gc_traversal                    | 3.18 ms                                                                                                         | 3.19 ms: 1.00x slower                                                                                               |
| richards                        | 37.4 ms                                                                                                         | 37.5 ms: 1.00x slower                                                                                               |
| richards_super                  | 41.8 ms                                                                                                         | 41.9 ms: 1.00x slower                                                                                               |
| thrift                          | 468 us                                                                                                          | 471 us: 1.00x slower                                                                                                |
| go                              | 100 ms                                                                                                          | 101 ms: 1.01x slower                                                                                                |
| sqlglot_v2_optimize             | 36.4 ms                                                                                                         | 36.7 ms: 1.01x slower                                                                                               |
| scimark_lu                      | 84.1 ms                                                                                                         | 84.7 ms: 1.01x slower                                                                                               |
| django_template                 | 25.1 ms                                                                                                         | 25.3 ms: 1.01x slower                                                                                               |
| json_dumps                      | 6.81 ms                                                                                                         | 6.85 ms: 1.01x slower                                                                                               |
| subparsers                      | 14.8 ms                                                                                                         | 14.9 ms: 1.01x slower                                                                                               |
| genshi_text                     | 17.6 ms                                                                                                         | 17.7 ms: 1.01x slower                                                                                               |
| docutils                        | 1.51 sec                                                                                                        | 1.52 sec: 1.01x slower                                                                                              |
| scimark_monte_carlo             | 52.9 ms                                                                                                         | 53.4 ms: 1.01x slower                                                                                               |
| dulwich_log                     | 26.5 ms                                                                                                         | 26.8 ms: 1.01x slower                                                                                               |
| hexiom                          | 5.10 ms                                                                                                         | 5.15 ms: 1.01x slower                                                                                               |
| sympy_expand                    | 262 ms                                                                                                          | 264 ms: 1.01x slower                                                                                                |
| logging_simple                  | 4.05 us                                                                                                         | 4.09 us: 1.01x slower                                                                                               |
| logging_format                  | 4.35 us                                                                                                         | 4.40 us: 1.01x slower                                                                                               |
| create_gc_cycles                | 1.35 ms                                                                                                         | 1.37 ms: 1.01x slower                                                                                               |
| sympy_integrate                 | 11.3 ms                                                                                                         | 11.5 ms: 1.01x slower                                                                                               |
| deepcopy_memo                   | 21.8 us                                                                                                         | 22.3 us: 1.02x slower                                                                                               |
| connected_components            | 304 ms                                                                                                          | 310 ms: 1.02x slower                                                                                                |
| many_optionals                  | 494 us                                                                                                          | 507 us: 1.02x slower                                                                                                |
| shortest_path                   | 328 ms                                                                                                          | 338 ms: 1.03x slower                                                                                                |
| deltablue                       | 2.81 ms                                                                                                         | 2.91 ms: 1.04x slower                                                                                               |
| k_core                          | 1.47 sec                                                                                                        | 1.52 sec: 1.04x slower                                                                                              |
| meteor_contest                  | 74.2 ms                                                                                                         | 77.8 ms: 1.05x slower                                                                                               |
| async_generators                | 275 ms                                                                                                          | 289 ms: 1.05x slower                                                                                                |
| scimark_sparse_mat_mult         | 3.18 ms                                                                                                         | 3.56 ms: 1.12x slower                                                                                               |
| Geometric mean                  | (ref)                                                                                                           | 1.01x faster                                                                                                        |

Benchmark hidden because not significant (26): async_tree_eager_io_tg, async_tree_eager_io, async_tree_eager_memoization, json, float, html5lib, deepcopy_reduce, pathlib, sqlglot_v2_normalize, async_tree_cpu_io_mixed_tg, dask, fannkuch, json_loads, regex_effbot, chaos, coroutines, pidigits, async_tree_eager_cpu_io_mixed, python_startup_no_site, logging_silent, async_tree_eager_cpu_io_mixed_tg, python_startup, sympy_str, sphinx, pycparser, pylint

- Geometric mean (including insignificant results): 1.015x faster

# HPT report

- Reliability score: 99.08% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x