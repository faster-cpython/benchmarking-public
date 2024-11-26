# Results vs. base

- fork: brandtbucher
- ref: justin_unlikely
- machine: windows-amd64
- commit hash: 15229e0
- commit date: 2024-10-17
- overall geometric mean: 1.002x slower
- HPT reliability: 95.78%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241017-pythonperf1-amd64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 249 ms                                                                      | 251 ms: 1.01x slower                                                         |
| docutils       | 1.92 sec                                                                    | 1.93 sec: 1.01x slower                                                       |
| tornado_http   | 98.2 ms                                                                     | 101 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                 |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark      | bm-20241017-pythonperf1-amd64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| coroutines     | 14.5 ms                                                                     | 14.1 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                 |

Benchmark hidden because not significant (11): async_tree_cpu_io_mixed, async_generators, async_tree_memoization_tg, asyncio_tcp_ssl, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, asyncio_tcp, async_tree_none, async_tree_none_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241017-pythonperf1-amd64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 55.8 ms                                                                     | 51.8 ms: 1.08x faster                                                        |
| float          | 47.6 ms                                                                     | 46.7 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                                       | 1.03x faster                                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241017-pythonperf1-amd64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 93.7 ms                                                                     | 92.5 ms: 1.01x faster                                                        |
| regex_v8       | 14.5 ms                                                                     | 14.7 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                 |

Benchmark hidden because not significant (2): regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241017-pythonperf1-amd64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_list        | 2.91 us                                                                     | 2.86 us: 1.02x faster                                                        |
| pickle_list          | 2.78 us                                                                     | 2.74 us: 1.01x faster                                                        |
| pickle               | 7.47 us                                                                     | 7.38 us: 1.01x faster                                                        |
| json_dumps           | 6.18 ms                                                                     | 6.24 ms: 1.01x slower                                                        |
| unpickle_pure_python | 146 us                                                                      | 147 us: 1.01x slower                                                         |
| xml_etree_generate   | 50.3 ms                                                                     | 51.0 ms: 1.01x slower                                                        |
| xml_etree_iterparse  | 62.6 ms                                                                     | 63.5 ms: 1.01x slower                                                        |
| pickle_pure_python   | 200 us                                                                      | 202 us: 1.01x slower                                                         |
| json_loads           | 14.1 us                                                                     | 14.4 us: 1.02x slower                                                        |
| xml_etree_process    | 35.6 ms                                                                     | 36.4 ms: 1.02x slower                                                        |
| tomli_loads          | 1.28 sec                                                                    | 1.32 sec: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                                       | 1.01x slower                                                                 |

Benchmark hidden because not significant (3): unpickle, xml_etree_parse, pickle_dict

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241017-pythonperf1-amd64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-----------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 27.2 ms                                                                     | 27.0 ms: 1.01x faster                                                        |
| genshi_xml      | 46.5 ms                                                                     | 46.9 ms: 1.01x slower                                                        |
| Geometric mean  | (ref)                                                                       | 1.00x faster                                                                 |

Benchmark hidden because not significant (2): mako, genshi_text

All benchmarks:
===============

| Benchmark                | bm-20241017-pythonperf1-amd64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|--------------------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody                    | 55.8 ms                                                                     | 51.8 ms: 1.08x faster                                                        |
| scimark_sor              | 67.4 ms                                                                     | 62.8 ms: 1.07x faster                                                        |
| logging_silent           | 60.0 ns                                                                     | 57.4 ns: 1.05x faster                                                        |
| coroutines               | 14.5 ms                                                                     | 14.1 ms: 1.03x faster                                                        |
| spectral_norm            | 54.8 ms                                                                     | 53.2 ms: 1.03x faster                                                        |
| crypto_pyaes             | 41.0 ms                                                                     | 39.9 ms: 1.03x faster                                                        |
| fannkuch                 | 239 ms                                                                      | 234 ms: 1.02x faster                                                         |
| deepcopy                 | 196 us                                                                      | 192 us: 1.02x faster                                                         |
| float                    | 47.6 ms                                                                     | 46.7 ms: 1.02x faster                                                        |
| unpickle_list            | 2.91 us                                                                     | 2.86 us: 1.02x faster                                                        |
| chaos                    | 42.3 ms                                                                     | 41.5 ms: 1.02x faster                                                        |
| coverage                 | 47.7 ms                                                                     | 47.1 ms: 1.01x faster                                                        |
| pickle_list              | 2.78 us                                                                     | 2.74 us: 1.01x faster                                                        |
| regex_compile            | 93.7 ms                                                                     | 92.5 ms: 1.01x faster                                                        |
| pickle                   | 7.47 us                                                                     | 7.38 us: 1.01x faster                                                        |
| pyflate                  | 293 ms                                                                      | 289 ms: 1.01x faster                                                         |
| deepcopy_reduce          | 1.92 us                                                                     | 1.90 us: 1.01x faster                                                        |
| logging_simple           | 6.23 us                                                                     | 6.18 us: 1.01x faster                                                        |
| django_template          | 27.2 ms                                                                     | 27.0 ms: 1.01x faster                                                        |
| generators               | 23.1 ms                                                                     | 22.9 ms: 1.01x faster                                                        |
| sqlglot_normalize        | 208 ms                                                                      | 209 ms: 1.00x slower                                                         |
| docutils                 | 1.92 sec                                                                    | 1.93 sec: 1.01x slower                                                       |
| hexiom                   | 5.21 ms                                                                     | 5.25 ms: 1.01x slower                                                        |
| genshi_xml               | 46.5 ms                                                                     | 46.9 ms: 1.01x slower                                                        |
| pprint_pformat           | 916 ms                                                                      | 924 ms: 1.01x slower                                                         |
| nqueens                  | 62.9 ms                                                                     | 63.5 ms: 1.01x slower                                                        |
| sympy_expand             | 327 ms                                                                      | 331 ms: 1.01x slower                                                         |
| sqlglot_transpile        | 1.20 ms                                                                     | 1.21 ms: 1.01x slower                                                        |
| json_dumps               | 6.18 ms                                                                     | 6.24 ms: 1.01x slower                                                        |
| sqlglot_optimize         | 42.7 ms                                                                     | 43.2 ms: 1.01x slower                                                        |
| dulwich_log              | 41.1 ms                                                                     | 41.5 ms: 1.01x slower                                                        |
| 2to3                     | 249 ms                                                                      | 251 ms: 1.01x slower                                                         |
| unpickle_pure_python     | 146 us                                                                      | 147 us: 1.01x slower                                                         |
| json                     | 2.96 ms                                                                     | 3.00 ms: 1.01x slower                                                        |
| xml_etree_generate       | 50.3 ms                                                                     | 51.0 ms: 1.01x slower                                                        |
| pprint_safe_repr         | 444 ms                                                                      | 449 ms: 1.01x slower                                                         |
| regex_v8                 | 14.5 ms                                                                     | 14.7 ms: 1.01x slower                                                        |
| xml_etree_iterparse      | 62.6 ms                                                                     | 63.5 ms: 1.01x slower                                                        |
| scimark_fft              | 155 ms                                                                      | 157 ms: 1.01x slower                                                         |
| richards                 | 34.0 ms                                                                     | 34.5 ms: 1.01x slower                                                        |
| pickle_pure_python       | 200 us                                                                      | 202 us: 1.01x slower                                                         |
| thrift                   | 518 us                                                                      | 526 us: 1.02x slower                                                         |
| sqlglot_parse            | 900 us                                                                      | 915 us: 1.02x slower                                                         |
| richards_super           | 38.4 ms                                                                     | 39.1 ms: 1.02x slower                                                        |
| deltablue                | 2.33 ms                                                                     | 2.37 ms: 1.02x slower                                                        |
| json_loads               | 14.1 us                                                                     | 14.4 us: 1.02x slower                                                        |
| scimark_monte_carlo      | 37.0 ms                                                                     | 37.8 ms: 1.02x slower                                                        |
| go                       | 93.4 ms                                                                     | 95.4 ms: 1.02x slower                                                        |
| typing_runtime_protocols | 114 us                                                                      | 116 us: 1.02x slower                                                         |
| xml_etree_process        | 35.6 ms                                                                     | 36.4 ms: 1.02x slower                                                        |
| tornado_http             | 98.2 ms                                                                     | 101 ms: 1.02x slower                                                         |
| tomli_loads              | 1.28 sec                                                                    | 1.32 sec: 1.03x slower                                                       |
| unpack_sequence          | 58.8 ns                                                                     | 60.8 ns: 1.03x slower                                                        |
| scimark_sparse_mat_mult  | 2.17 ms                                                                     | 2.26 ms: 1.04x slower                                                        |
| deepcopy_memo            | 16.3 us                                                                     | 17.1 us: 1.05x slower                                                        |
| Geometric mean           | (ref)                                                                       | 1.00x slower                                                                 |

Benchmark hidden because not significant (41): mako, telco, python_startup_no_site, create_gc_cycles, unpickle, async_tree_cpu_io_mixed, bench_thread_pool, bench_mp_pool, xml_etree_parse, raytrace, sympy_sum, html5lib, python_startup, scimark_lu, meteor_contest, regex_dna, comprehensions, mdp, gc_traversal, pidigits, async_generators, pathlib, pickle_dict, async_tree_memoization_tg, pycparser, sympy_integrate, asyncio_tcp_ssl, sqlite_synth, genshi_text, async_tree_cpu_io_mixed_tg, logging_format, async_tree_io, async_tree_io_tg, sphinx, asyncio_tcp, async_tree_none, async_tree_none_tg, regex_effbot, sympy_str, pylint, async_tree_memoization

- Geometric mean (including insignificant results): 1.002x slower
# HPT report

- Reliability score: 95.78% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown