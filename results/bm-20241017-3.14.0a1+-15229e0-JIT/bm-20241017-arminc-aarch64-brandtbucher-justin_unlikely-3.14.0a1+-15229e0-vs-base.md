# Results vs. base

- fork: brandtbucher
- ref: justin_unlikely
- machine: linux-aarch64
- commit hash: 15229e0
- commit date: 2024-10-17
- overall geometric mean: 1.00x slower
- HPT reliability: 77.64%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| html5lib       | 72.2 ms                                                                  | 71.1 ms: 1.01x faster                                                     |
| tornado_http   | 154 ms                                                                   | 146 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                                    | 1.01x faster                                                              |

Benchmark hidden because not significant (3): 2to3, docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|------------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_generators | 507 ms                                                                   | 513 ms: 1.01x slower                                                      |
| asyncio_tcp_ssl  | 2.25 sec                                                                 | 2.29 sec: 1.01x slower                                                    |
| asyncio_tcp      | 630 ms                                                                   | 639 ms: 1.01x slower                                                      |
| Geometric mean   | (ref)                                                                    | 1.00x faster                                                              |

Benchmark hidden because not significant (10): async_tree_io, async_tree_memoization_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none, asyncio_websockets, coroutines, async_tree_none_tg, async_tree_io_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 114 ms                                                                   | 119 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                                    | 1.01x slower                                                              |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 251 ms                                                                   | 245 ms: 1.02x faster                                                      |
| regex_effbot   | 4.94 ms                                                                  | 4.88 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                                    | 1.00x faster                                                              |

Benchmark hidden because not significant (2): regex_v8, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle               | 14.1 us                                                                  | 13.7 us: 1.02x faster                                                     |
| pickle_list          | 5.30 us                                                                  | 5.22 us: 1.02x faster                                                     |
| xml_etree_parse      | 187 ms                                                                   | 185 ms: 1.01x faster                                                      |
| unpickle_pure_python | 268 us                                                                   | 266 us: 1.01x faster                                                      |
| xml_etree_process    | 81.2 ms                                                                  | 80.6 ms: 1.01x faster                                                     |
| Geometric mean       | (ref)                                                                    | 1.00x faster                                                              |

Benchmark hidden because not significant (9): pickle_pure_python, xml_etree_iterparse, tomli_loads, json_dumps, json_loads, unpickle, pickle_dict, unpickle_list, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|------------------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.9 ms                                                                  | 14.6 ms: 1.01x faster                                                     |
| python_startup_no_site | 8.81 ms                                                                  | 8.73 ms: 1.01x faster                                                     |
| Geometric mean         | (ref)                                                                    | 1.01x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-----------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 51.6 ms                                                                  | 50.9 ms: 1.01x faster                                                     |
| mako            | 13.1 ms                                                                  | 13.4 ms: 1.02x slower                                                     |
| genshi_xml      | 82.8 ms                                                                  | 84.6 ms: 1.02x slower                                                     |
| Geometric mean  | (ref)                                                                    | 1.01x slower                                                              |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-------------------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tornado_http            | 154 ms                                                                   | 146 ms: 1.05x faster                                                      |
| regex_dna               | 251 ms                                                                   | 245 ms: 1.02x faster                                                      |
| pickle                  | 14.1 us                                                                  | 13.7 us: 1.02x faster                                                     |
| deepcopy_reduce         | 4.07 us                                                                  | 3.99 us: 1.02x faster                                                     |
| logging_simple          | 7.56 us                                                                  | 7.41 us: 1.02x faster                                                     |
| logging_format          | 8.19 us                                                                  | 8.06 us: 1.02x faster                                                     |
| pickle_list             | 5.30 us                                                                  | 5.22 us: 1.02x faster                                                     |
| html5lib                | 72.2 ms                                                                  | 71.1 ms: 1.01x faster                                                     |
| django_template         | 51.6 ms                                                                  | 50.9 ms: 1.01x faster                                                     |
| python_startup          | 14.9 ms                                                                  | 14.6 ms: 1.01x faster                                                     |
| regex_effbot            | 4.94 ms                                                                  | 4.88 ms: 1.01x faster                                                     |
| xml_etree_parse         | 187 ms                                                                   | 185 ms: 1.01x faster                                                      |
| bench_thread_pool       | 1.39 ms                                                                  | 1.37 ms: 1.01x faster                                                     |
| python_startup_no_site  | 8.81 ms                                                                  | 8.73 ms: 1.01x faster                                                     |
| unpickle_pure_python    | 268 us                                                                   | 266 us: 1.01x faster                                                      |
| xml_etree_process       | 81.2 ms                                                                  | 80.6 ms: 1.01x faster                                                     |
| scimark_lu              | 149 ms                                                                   | 148 ms: 1.01x faster                                                      |
| generators              | 58.8 ms                                                                  | 58.9 ms: 1.00x slower                                                     |
| comprehensions          | 24.7 us                                                                  | 24.9 us: 1.01x slower                                                     |
| sqlglot_optimize        | 82.1 ms                                                                  | 82.9 ms: 1.01x slower                                                     |
| richards_super          | 71.0 ms                                                                  | 71.7 ms: 1.01x slower                                                     |
| async_generators        | 507 ms                                                                   | 513 ms: 1.01x slower                                                      |
| scimark_sparse_mat_mult | 7.07 ms                                                                  | 7.16 ms: 1.01x slower                                                     |
| asyncio_tcp_ssl         | 2.25 sec                                                                 | 2.29 sec: 1.01x slower                                                    |
| asyncio_tcp             | 630 ms                                                                   | 639 ms: 1.01x slower                                                      |
| scimark_monte_carlo     | 89.3 ms                                                                  | 90.7 ms: 1.02x slower                                                     |
| hexiom                  | 10.1 ms                                                                  | 10.2 ms: 1.02x slower                                                     |
| logging_silent          | 133 ns                                                                   | 135 ns: 1.02x slower                                                      |
| crypto_pyaes            | 89.2 ms                                                                  | 90.7 ms: 1.02x slower                                                     |
| meteor_contest          | 122 ms                                                                   | 124 ms: 1.02x slower                                                      |
| scimark_fft             | 454 ms                                                                   | 463 ms: 1.02x slower                                                      |
| bpe_tokeniser           | 5.93 sec                                                                 | 6.04 sec: 1.02x slower                                                    |
| pprint_pformat          | 2.56 sec                                                                 | 2.61 sec: 1.02x slower                                                    |
| scimark_sor             | 154 ms                                                                   | 157 ms: 1.02x slower                                                      |
| mako                    | 13.1 ms                                                                  | 13.4 ms: 1.02x slower                                                     |
| genshi_xml              | 82.8 ms                                                                  | 84.6 ms: 1.02x slower                                                     |
| json                    | 5.62 ms                                                                  | 5.74 ms: 1.02x slower                                                     |
| sqlite_synth            | 3.81 us                                                                  | 3.91 us: 1.03x slower                                                     |
| pprint_safe_repr        | 1.21 sec                                                                 | 1.24 sec: 1.03x slower                                                    |
| chaos                   | 84.2 ms                                                                  | 87.2 ms: 1.04x slower                                                     |
| pyflate                 | 617 ms                                                                   | 643 ms: 1.04x slower                                                      |
| nbody                   | 114 ms                                                                   | 119 ms: 1.04x slower                                                      |
| Geometric mean          | (ref)                                                                    | 1.00x slower                                                              |

Benchmark hidden because not significant (56): sqlglot_parse, async_tree_io, go, async_tree_memoization_tg, coverage, pickle_pure_python, sphinx, dulwich_log, pathlib, async_tree_memoization, deepcopy, gc_traversal, nqueens, async_tree_cpu_io_mixed, typing_runtime_protocols, sympy_integrate, async_tree_none, sqlglot_normalize, richards, float, xml_etree_iterparse, tomli_loads, mdp, unpack_sequence, sympy_expand, asyncio_websockets, coroutines, json_dumps, thrift, pycparser, async_tree_none_tg, regex_v8, spectral_norm, async_tree_io_tg, async_tree_cpu_io_mixed_tg, docutils, pidigits, genshi_text, json_loads, 2to3, unpickle, sympy_sum, pickle_dict, deepcopy_memo, create_gc_cycles, fannkuch, unpickle_list, raytrace, sympy_str, sqlglot_transpile, pylint, telco, xml_etree_generate, regex_compile, deltablue, bench_mp_pool

# HPT report

- Reliability score: 77.64% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x