# Results vs. base

- fork: brandtbucher
- ref: no_generators_alt_al
- machine: linux-x86_64
- commit hash: 8b4af65
- commit date: 2025-02-04
- overall geometric mean: 1.009x faster
- HPT reliability: 93.31%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-8b4af65 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 261 ms                                                                 | 258 ms: 1.01x faster                                                         |
| docutils       | 2.67 sec                                                               | 2.69 sec: 1.01x slower                                                       |
| html5lib       | 63.3 ms                                                                | 62.7 ms: 1.01x faster                                                        |
| sphinx         | 1.04 sec                                                               | 1.02 sec: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-8b4af65 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| coroutines             | 23.0 ms                                                                | 22.5 ms: 1.02x faster                                                        |
| async_generators       | 411 ms                                                                 | 405 ms: 1.01x faster                                                         |
| async_tree_memoization | 327 ms                                                                 | 330 ms: 1.01x slower                                                         |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (8): async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_io, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_memoization_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-8b4af65 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (2): nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-8b4af65 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 211 ms                                                                 | 195 ms: 1.08x faster                                                         |
| regex_effbot   | 3.18 ms                                                                | 2.99 ms: 1.07x faster                                                        |
| regex_v8       | 24.0 ms                                                                | 23.8 ms: 1.01x faster                                                        |
| regex_compile  | 130 ms                                                                 | 129 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                                  | 1.04x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-8b4af65 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 1.84 sec                                                               | 1.81 sec: 1.01x faster                                                       |
| json_loads           | 28.9 us                                                                | 28.7 us: 1.00x faster                                                        |
| xml_etree_process    | 54.6 ms                                                                | 55.0 ms: 1.01x slower                                                        |
| xml_etree_iterparse  | 94.7 ms                                                                | 95.6 ms: 1.01x slower                                                        |
| unpickle_pure_python | 200 us                                                                 | 202 us: 1.01x slower                                                         |
| json_dumps           | 11.1 ms                                                                | 11.3 ms: 1.01x slower                                                        |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (3): xml_etree_generate, xml_etree_parse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-8b4af65 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 12.9 ms                                                                | 12.8 ms: 1.01x faster                                                        |
| python_startup_no_site | 7.06 ms                                                                | 7.02 ms: 1.01x faster                                                        |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-8b4af65 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml     | 57.7 ms                                                                | 49.1 ms: 1.17x faster                                                        |
| genshi_text    | 23.0 ms                                                                | 20.9 ms: 1.10x faster                                                        |
| mako           | 10.3 ms                                                                | 9.98 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                                  | 1.07x faster                                                                 |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-8b4af65 |
|-------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators              | 37.5 ms                                                                | 28.4 ms: 1.32x faster                                                        |
| genshi_xml              | 57.7 ms                                                                | 49.1 ms: 1.17x faster                                                        |
| nqueens                 | 89.5 ms                                                                | 79.6 ms: 1.12x faster                                                        |
| genshi_text             | 23.0 ms                                                                | 20.9 ms: 1.10x faster                                                        |
| regex_dna               | 211 ms                                                                 | 195 ms: 1.08x faster                                                         |
| regex_effbot            | 3.18 ms                                                                | 2.99 ms: 1.07x faster                                                        |
| mako                    | 10.3 ms                                                                | 9.98 ms: 1.03x faster                                                        |
| hexiom                  | 7.46 ms                                                                | 7.26 ms: 1.03x faster                                                        |
| sqlglot_normalize       | 108 ms                                                                 | 105 ms: 1.02x faster                                                         |
| bench_thread_pool       | 894 us                                                                 | 874 us: 1.02x faster                                                         |
| mdp                     | 2.54 sec                                                               | 2.49 sec: 1.02x faster                                                       |
| coroutines              | 23.0 ms                                                                | 22.5 ms: 1.02x faster                                                        |
| pyflate                 | 463 ms                                                                 | 454 ms: 1.02x faster                                                         |
| scimark_monte_carlo     | 63.9 ms                                                                | 62.8 ms: 1.02x faster                                                        |
| scimark_sparse_mat_mult | 4.63 ms                                                                | 4.55 ms: 1.02x faster                                                        |
| go                      | 128 ms                                                                 | 126 ms: 1.02x faster                                                         |
| async_generators        | 411 ms                                                                 | 405 ms: 1.01x faster                                                         |
| comprehensions          | 17.1 us                                                                | 16.9 us: 1.01x faster                                                        |
| sphinx                  | 1.04 sec                                                               | 1.02 sec: 1.01x faster                                                       |
| sympy_sum               | 154 ms                                                                 | 152 ms: 1.01x faster                                                         |
| tomli_loads             | 1.84 sec                                                               | 1.81 sec: 1.01x faster                                                       |
| sqlglot_optimize        | 54.1 ms                                                                | 53.4 ms: 1.01x faster                                                        |
| telco                   | 7.70 ms                                                                | 7.61 ms: 1.01x faster                                                        |
| 2to3                    | 261 ms                                                                 | 258 ms: 1.01x faster                                                         |
| scimark_fft             | 314 ms                                                                 | 310 ms: 1.01x faster                                                         |
| html5lib                | 63.3 ms                                                                | 62.7 ms: 1.01x faster                                                        |
| bench_mp_pool           | 81.0 ms                                                                | 80.3 ms: 1.01x faster                                                        |
| regex_v8                | 24.0 ms                                                                | 23.8 ms: 1.01x faster                                                        |
| dulwich_log             | 66.8 ms                                                                | 66.3 ms: 1.01x faster                                                        |
| python_startup          | 12.9 ms                                                                | 12.8 ms: 1.01x faster                                                        |
| regex_compile           | 130 ms                                                                 | 129 ms: 1.01x faster                                                         |
| sympy_str               | 279 ms                                                                 | 277 ms: 1.01x faster                                                         |
| python_startup_no_site  | 7.06 ms                                                                | 7.02 ms: 1.01x faster                                                        |
| pathlib                 | 16.1 ms                                                                | 16.0 ms: 1.01x faster                                                        |
| json_loads              | 28.9 us                                                                | 28.7 us: 1.00x faster                                                        |
| meteor_contest          | 108 ms                                                                 | 108 ms: 1.00x faster                                                         |
| pidigits                | 186 ms                                                                 | 186 ms: 1.00x faster                                                         |
| shortest_path           | 481 ms                                                                 | 482 ms: 1.00x slower                                                         |
| sympy_expand            | 470 ms                                                                 | 472 ms: 1.00x slower                                                         |
| create_gc_cycles        | 2.45 ms                                                                | 2.46 ms: 1.00x slower                                                        |
| sqlalchemy_declarative  | 131 ms                                                                 | 132 ms: 1.00x slower                                                         |
| bpe_tokeniser           | 4.36 sec                                                               | 4.38 sec: 1.00x slower                                                       |
| many_optionals          | 958 us                                                                 | 963 us: 1.01x slower                                                         |
| docutils                | 2.67 sec                                                               | 2.69 sec: 1.01x slower                                                       |
| xml_etree_process       | 54.6 ms                                                                | 55.0 ms: 1.01x slower                                                        |
| richards_super          | 49.7 ms                                                                | 50.1 ms: 1.01x slower                                                        |
| richards                | 43.5 ms                                                                | 43.9 ms: 1.01x slower                                                        |
| xml_etree_iterparse     | 94.7 ms                                                                | 95.6 ms: 1.01x slower                                                        |
| unpickle_pure_python    | 200 us                                                                 | 202 us: 1.01x slower                                                         |
| async_tree_memoization  | 327 ms                                                                 | 330 ms: 1.01x slower                                                         |
| sqlglot_parse           | 1.28 ms                                                                | 1.29 ms: 1.01x slower                                                        |
| deepcopy_memo           | 30.2 us                                                                | 30.5 us: 1.01x slower                                                        |
| sqlglot_transpile       | 1.58 ms                                                                | 1.60 ms: 1.01x slower                                                        |
| json_dumps              | 11.1 ms                                                                | 11.3 ms: 1.01x slower                                                        |
| scimark_lu              | 113 ms                                                                 | 115 ms: 1.01x slower                                                         |
| chaos                   | 58.8 ms                                                                | 59.8 ms: 1.02x slower                                                        |
| pprint_pformat          | 1.50 sec                                                               | 1.53 sec: 1.02x slower                                                       |
| thrift                  | 771 us                                                                 | 785 us: 1.02x slower                                                         |
| logging_simple          | 5.63 us                                                                | 5.76 us: 1.02x slower                                                        |
| deepcopy                | 265 us                                                                 | 271 us: 1.02x slower                                                         |
| pprint_safe_repr        | 728 ms                                                                 | 745 ms: 1.02x slower                                                         |
| logging_silent          | 108 ns                                                                 | 110 ns: 1.02x slower                                                         |
| gc_traversal            | 4.77 ms                                                                | 4.93 ms: 1.03x slower                                                        |
| logging_format          | 6.17 us                                                                | 6.46 us: 1.05x slower                                                        |
| pycparser               | 1.14 sec                                                               | 1.19 sec: 1.05x slower                                                       |
| Geometric mean          | (ref)                                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (31): pylint, raytrace, fannkuch, crypto_pyaes, subparsers, spectral_norm, sqlite_synth, xml_etree_generate, sympy_integrate, coverage, async_tree_none_tg, k_core, connected_components, django_template, typing_runtime_protocols, async_tree_cpu_io_mixed_tg, xml_etree_parse, async_tree_io, json, asyncio_websockets, deltablue, sqlalchemy_imperative, scimark_sor, nbody, async_tree_cpu_io_mixed, async_tree_io_tg, float, async_tree_memoization_tg, async_tree_none, pickle_pure_python, deepcopy_reduce

- Geometric mean (including insignificant results): 1.009x faster

# HPT report

- Reliability score: 93.31% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x