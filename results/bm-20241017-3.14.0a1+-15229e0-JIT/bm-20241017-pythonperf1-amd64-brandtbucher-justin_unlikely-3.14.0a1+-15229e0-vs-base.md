# Results vs. base

- fork: brandtbucher
- ref: justin_unlikely
- machine: windows-amd64
- commit hash: 15229e0
- commit date: 2024-10-17
- overall geometric mean: 1.00x slower
- HPT reliability: 94.69%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241017-pythonperf1-amd64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 249 ms                                                                      | 251 ms: 1.01x slower                                                         |
| docutils       | 1.92 sec                                                                    | 1.93 sec: 1.00x slower                                                       |
| html5lib       | 38.8 ms                                                                     | 39.9 ms: 1.03x slower                                                        |
| tornado_http   | 99.2 ms                                                                     | 101 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241017-pythonperf1-amd64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| coroutines                 | 15.3 ms                                                                     | 14.1 ms: 1.09x faster                                                        |
| async_tree_cpu_io_mixed_tg | 397 ms                                                                      | 406 ms: 1.02x slower                                                         |
| async_tree_none_tg         | 206 ms                                                                      | 211 ms: 1.02x slower                                                         |
| async_generators           | 261 ms                                                                      | 269 ms: 1.03x slower                                                         |
| Geometric mean             | (ref)                                                                       | 1.00x slower                                                                 |

Benchmark hidden because not significant (8): asyncio_tcp_ssl, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_io, asyncio_tcp, async_tree_none, async_tree_memoization_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241017-pythonperf1-amd64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 53.7 ms                                                                     | 51.8 ms: 1.04x faster                                                        |
| float          | 47.0 ms                                                                     | 46.7 ms: 1.01x faster                                                        |
| pidigits       | 148 ms                                                                      | 148 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                                       | 1.02x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241017-pythonperf1-amd64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 123 ms                                                                      | 114 ms: 1.08x faster                                                         |
| regex_v8       | 15.3 ms                                                                     | 14.7 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                                       | 1.03x faster                                                                 |

Benchmark hidden because not significant (2): regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241017-pythonperf1-amd64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle             | 9.30 us                                                                     | 9.08 us: 1.02x faster                                                        |
| xml_etree_generate   | 52.0 ms                                                                     | 51.0 ms: 1.02x faster                                                        |
| json_dumps           | 6.36 ms                                                                     | 6.24 ms: 1.02x faster                                                        |
| xml_etree_parse      | 96.4 ms                                                                     | 95.3 ms: 1.01x faster                                                        |
| pickle_dict          | 17.7 us                                                                     | 17.9 us: 1.01x slower                                                        |
| xml_etree_iterparse  | 62.9 ms                                                                     | 63.5 ms: 1.01x slower                                                        |
| pickle               | 7.30 us                                                                     | 7.38 us: 1.01x slower                                                        |
| unpickle_list        | 2.80 us                                                                     | 2.86 us: 1.02x slower                                                        |
| tomli_loads          | 1.28 sec                                                                    | 1.32 sec: 1.03x slower                                                       |
| pickle_pure_python   | 195 us                                                                      | 202 us: 1.04x slower                                                         |
| unpickle_pure_python | 141 us                                                                      | 147 us: 1.04x slower                                                         |
| Geometric mean       | (ref)                                                                       | 1.01x slower                                                                 |

Benchmark hidden because not significant (3): xml_etree_process, pickle_list, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241017-pythonperf1-amd64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|------------------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 18.8 ms                                                                     | 18.4 ms: 1.02x faster                                                        |
| Geometric mean         | (ref)                                                                       | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241017-pythonperf1-amd64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-----------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 47.7 ms                                                                     | 46.9 ms: 1.02x faster                                                        |
| django_template | 27.3 ms                                                                     | 27.0 ms: 1.01x faster                                                        |
| genshi_text     | 19.2 ms                                                                     | 19.5 ms: 1.01x slower                                                        |
| Geometric mean  | (ref)                                                                       | 1.00x faster                                                                 |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241017-pythonperf1-amd64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| coroutines                 | 15.3 ms                                                                     | 14.1 ms: 1.09x faster                                                        |
| regex_dna                  | 123 ms                                                                      | 114 ms: 1.08x faster                                                         |
| chaos                      | 43.4 ms                                                                     | 41.5 ms: 1.05x faster                                                        |
| mdp                        | 1.62 sec                                                                    | 1.55 sec: 1.04x faster                                                       |
| regex_v8                   | 15.3 ms                                                                     | 14.7 ms: 1.04x faster                                                        |
| nbody                      | 53.7 ms                                                                     | 51.8 ms: 1.04x faster                                                        |
| pprint_safe_repr           | 463 ms                                                                      | 449 ms: 1.03x faster                                                         |
| pprint_pformat             | 950 ms                                                                      | 924 ms: 1.03x faster                                                         |
| deepcopy                   | 197 us                                                                      | 192 us: 1.03x faster                                                         |
| unpickle                   | 9.30 us                                                                     | 9.08 us: 1.02x faster                                                        |
| xml_etree_generate         | 52.0 ms                                                                     | 51.0 ms: 1.02x faster                                                        |
| thrift                     | 537 us                                                                      | 526 us: 1.02x faster                                                         |
| json_dumps                 | 6.36 ms                                                                     | 6.24 ms: 1.02x faster                                                        |
| scimark_sor                | 64.0 ms                                                                     | 62.8 ms: 1.02x faster                                                        |
| python_startup_no_site     | 18.8 ms                                                                     | 18.4 ms: 1.02x faster                                                        |
| bench_thread_pool          | 840 us                                                                      | 825 us: 1.02x faster                                                         |
| crypto_pyaes               | 40.6 ms                                                                     | 39.9 ms: 1.02x faster                                                        |
| genshi_xml                 | 47.7 ms                                                                     | 46.9 ms: 1.02x faster                                                        |
| coverage                   | 47.8 ms                                                                     | 47.1 ms: 1.02x faster                                                        |
| django_template            | 27.3 ms                                                                     | 27.0 ms: 1.01x faster                                                        |
| xml_etree_parse            | 96.4 ms                                                                     | 95.3 ms: 1.01x faster                                                        |
| meteor_contest             | 76.1 ms                                                                     | 75.2 ms: 1.01x faster                                                        |
| spectral_norm              | 53.6 ms                                                                     | 53.2 ms: 1.01x faster                                                        |
| fannkuch                   | 236 ms                                                                      | 234 ms: 1.01x faster                                                         |
| float                      | 47.0 ms                                                                     | 46.7 ms: 1.01x faster                                                        |
| pidigits                   | 148 ms                                                                      | 148 ms: 1.00x faster                                                         |
| docutils                   | 1.92 sec                                                                    | 1.93 sec: 1.00x slower                                                       |
| logging_simple             | 6.14 us                                                                     | 6.18 us: 1.01x slower                                                        |
| pickle_dict                | 17.7 us                                                                     | 17.9 us: 1.01x slower                                                        |
| deltablue                  | 2.35 ms                                                                     | 2.37 ms: 1.01x slower                                                        |
| xml_etree_iterparse        | 62.9 ms                                                                     | 63.5 ms: 1.01x slower                                                        |
| 2to3                       | 249 ms                                                                      | 251 ms: 1.01x slower                                                         |
| pickle                     | 7.30 us                                                                     | 7.38 us: 1.01x slower                                                        |
| sqlglot_normalize          | 206 ms                                                                      | 209 ms: 1.01x slower                                                         |
| tornado_http               | 99.2 ms                                                                     | 101 ms: 1.01x slower                                                         |
| genshi_text                | 19.2 ms                                                                     | 19.5 ms: 1.01x slower                                                        |
| sympy_expand               | 326 ms                                                                      | 331 ms: 1.01x slower                                                         |
| scimark_monte_carlo        | 37.2 ms                                                                     | 37.8 ms: 1.02x slower                                                        |
| richards                   | 33.9 ms                                                                     | 34.5 ms: 1.02x slower                                                        |
| richards_super             | 38.4 ms                                                                     | 39.1 ms: 1.02x slower                                                        |
| sqlglot_parse              | 897 us                                                                      | 915 us: 1.02x slower                                                         |
| scimark_sparse_mat_mult    | 2.22 ms                                                                     | 2.26 ms: 1.02x slower                                                        |
| unpickle_list              | 2.80 us                                                                     | 2.86 us: 1.02x slower                                                        |
| async_tree_cpu_io_mixed_tg | 397 ms                                                                      | 406 ms: 1.02x slower                                                         |
| logging_silent             | 56.1 ns                                                                     | 57.4 ns: 1.02x slower                                                        |
| scimark_lu                 | 53.8 ms                                                                     | 55.0 ms: 1.02x slower                                                        |
| dulwich_log                | 40.6 ms                                                                     | 41.5 ms: 1.02x slower                                                        |
| async_tree_none_tg         | 206 ms                                                                      | 211 ms: 1.02x slower                                                         |
| sympy_str                  | 190 ms                                                                      | 196 ms: 1.03x slower                                                         |
| scimark_fft                | 152 ms                                                                      | 157 ms: 1.03x slower                                                         |
| html5lib                   | 38.8 ms                                                                     | 39.9 ms: 1.03x slower                                                        |
| async_generators           | 261 ms                                                                      | 269 ms: 1.03x slower                                                         |
| tomli_loads                | 1.28 sec                                                                    | 1.32 sec: 1.03x slower                                                       |
| raytrace                   | 208 ms                                                                      | 214 ms: 1.03x slower                                                         |
| sqlglot_transpile          | 1.18 ms                                                                     | 1.21 ms: 1.03x slower                                                        |
| pickle_pure_python         | 195 us                                                                      | 202 us: 1.04x slower                                                         |
| typing_runtime_protocols   | 112 us                                                                      | 116 us: 1.04x slower                                                         |
| deepcopy_memo              | 16.4 us                                                                     | 17.1 us: 1.04x slower                                                        |
| unpack_sequence            | 58.4 ns                                                                     | 60.8 ns: 1.04x slower                                                        |
| unpickle_pure_python       | 141 us                                                                      | 147 us: 1.04x slower                                                         |
| go                         | 90.5 ms                                                                     | 95.4 ms: 1.05x slower                                                        |
| Geometric mean             | (ref)                                                                       | 1.00x slower                                                                 |

Benchmark hidden because not significant (35): regex_effbot, comprehensions, asyncio_tcp_ssl, xml_etree_process, bench_mp_pool, mako, python_startup, pycparser, sympy_sum, pickle_list, generators, json_loads, gc_traversal, regex_compile, create_gc_cycles, sqlglot_optimize, async_tree_cpu_io_mixed, logging_format, sphinx, pyflate, deepcopy_reduce, sqlite_synth, async_tree_io_tg, nqueens, hexiom, json, pathlib, sympy_integrate, pylint, async_tree_io, telco, asyncio_tcp, async_tree_none, async_tree_memoization_tg, async_tree_memoization

# HPT report

- Reliability score: 94.69% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown