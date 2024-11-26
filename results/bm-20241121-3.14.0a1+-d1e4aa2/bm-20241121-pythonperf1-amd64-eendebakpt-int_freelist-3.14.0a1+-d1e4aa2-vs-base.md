# Results vs. base

- fork: eendebakpt
- ref: int_freelist
- machine: windows-amd64
- commit hash: d1e4aa2
- commit date: 2024-11-21
- overall geometric mean: 1.001x slower
- HPT reliability: 91.28%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241116-pythonperf1-amd64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241121-pythonperf1-amd64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 1.70 sec                                                                    | 1.71 sec: 1.01x slower                                                  |
| html5lib       | 40.0 ms                                                                     | 40.3 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                            |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241116-pythonperf1-amd64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241121-pythonperf1-amd64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_generators | 243 ms                                                                      | 245 ms: 1.01x slower                                                    |
| Geometric mean   | (ref)                                                                       | 1.00x slower                                                            |

Benchmark hidden because not significant (10): async_tree_io_tg, async_tree_memoization, async_tree_none_tg, async_tree_io, async_tree_memoization_tg, coroutines, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_none, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241116-pythonperf1-amd64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241121-pythonperf1-amd64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 79.9 ms                                                                     | 78.8 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                            |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241116-pythonperf1-amd64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241121-pythonperf1-amd64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 116 ms                                                                      | 115 ms: 1.01x faster                                                    |
| regex_v8       | 14.7 ms                                                                     | 14.9 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                            |

Benchmark hidden because not significant (2): regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241116-pythonperf1-amd64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241121-pythonperf1-amd64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 1.60 sec                                                                    | 1.55 sec: 1.04x faster                                                  |
| xml_etree_parse      | 96.0 ms                                                                     | 94.0 ms: 1.02x faster                                                   |
| json_loads           | 14.6 us                                                                     | 14.4 us: 1.01x faster                                                   |
| xml_etree_process    | 41.2 ms                                                                     | 41.0 ms: 1.00x faster                                                   |
| xml_etree_generate   | 58.6 ms                                                                     | 58.3 ms: 1.00x faster                                                   |
| pickle_pure_python   | 229 us                                                                      | 231 us: 1.01x slower                                                    |
| unpickle_pure_python | 155 us                                                                      | 157 us: 1.02x slower                                                    |
| json_dumps           | 6.64 ms                                                                     | 6.78 ms: 1.02x slower                                                   |
| Geometric mean       | (ref)                                                                       | 1.00x faster                                                            |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241116-pythonperf1-amd64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241121-pythonperf1-amd64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 23.4 ms                                                                     | 23.2 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241116-pythonperf1-amd64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241121-pythonperf1-amd64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|-----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 25.0 ms                                                                     | 25.6 ms: 1.02x slower                                                   |
| Geometric mean  | (ref)                                                                       | 1.01x slower                                                            |

Benchmark hidden because not significant (3): mako, genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20241116-pythonperf1-amd64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241121-pythonperf1-amd64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|-------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| scimark_sparse_mat_mult | 2.72 ms                                                                     | 2.60 ms: 1.04x faster                                                   |
| scimark_fft             | 205 ms                                                                      | 197 ms: 1.04x faster                                                    |
| tomli_loads             | 1.60 sec                                                                    | 1.55 sec: 1.04x faster                                                  |
| xml_etree_parse         | 96.0 ms                                                                     | 94.0 ms: 1.02x faster                                                   |
| coverage                | 48.3 ms                                                                     | 47.4 ms: 1.02x faster                                                   |
| sqlite_synth            | 1.63 us                                                                     | 1.60 us: 1.02x faster                                                   |
| richards_super          | 37.1 ms                                                                     | 36.5 ms: 1.02x faster                                                   |
| richards                | 33.2 ms                                                                     | 32.7 ms: 1.02x faster                                                   |
| sqlglot_parse           | 932 us                                                                      | 918 us: 1.02x faster                                                    |
| pyflate                 | 323 ms                                                                      | 319 ms: 1.01x faster                                                    |
| json_loads              | 14.6 us                                                                     | 14.4 us: 1.01x faster                                                   |
| nbody                   | 79.9 ms                                                                     | 78.8 ms: 1.01x faster                                                   |
| raytrace                | 201 ms                                                                      | 198 ms: 1.01x faster                                                    |
| sqlglot_transpile       | 1.15 ms                                                                     | 1.14 ms: 1.01x faster                                                   |
| python_startup          | 23.4 ms                                                                     | 23.2 ms: 1.01x faster                                                   |
| thrift                  | 528 us                                                                      | 523 us: 1.01x faster                                                    |
| scimark_sor             | 92.5 ms                                                                     | 91.6 ms: 1.01x faster                                                   |
| gc_traversal            | 1.93 ms                                                                     | 1.92 ms: 1.01x faster                                                   |
| regex_dna               | 116 ms                                                                      | 115 ms: 1.01x faster                                                    |
| xml_etree_process       | 41.2 ms                                                                     | 41.0 ms: 1.00x faster                                                   |
| xml_etree_generate      | 58.6 ms                                                                     | 58.3 ms: 1.00x faster                                                   |
| fannkuch                | 280 ms                                                                      | 279 ms: 1.00x faster                                                    |
| html5lib                | 40.0 ms                                                                     | 40.3 ms: 1.01x slower                                                   |
| docutils                | 1.70 sec                                                                    | 1.71 sec: 1.01x slower                                                  |
| sympy_expand            | 309 ms                                                                      | 311 ms: 1.01x slower                                                    |
| pickle_pure_python      | 229 us                                                                      | 231 us: 1.01x slower                                                    |
| async_generators        | 243 ms                                                                      | 245 ms: 1.01x slower                                                    |
| meteor_contest          | 78.2 ms                                                                     | 78.9 ms: 1.01x slower                                                   |
| mdp                     | 1.45 sec                                                                    | 1.46 sec: 1.01x slower                                                  |
| logging_format          | 6.78 us                                                                     | 6.85 us: 1.01x slower                                                   |
| logging_simple          | 6.34 us                                                                     | 6.42 us: 1.01x slower                                                   |
| deltablue               | 2.32 ms                                                                     | 2.35 ms: 1.01x slower                                                   |
| spectral_norm           | 65.4 ms                                                                     | 66.2 ms: 1.01x slower                                                   |
| crypto_pyaes            | 48.5 ms                                                                     | 49.1 ms: 1.01x slower                                                   |
| logging_silent          | 64.9 ns                                                                     | 65.7 ns: 1.01x slower                                                   |
| bpe_tokeniser           | 3.09 sec                                                                    | 3.13 sec: 1.01x slower                                                  |
| regex_v8                | 14.7 ms                                                                     | 14.9 ms: 1.02x slower                                                   |
| nqueens                 | 64.1 ms                                                                     | 65.1 ms: 1.02x slower                                                   |
| unpickle_pure_python    | 155 us                                                                      | 157 us: 1.02x slower                                                    |
| pprint_pformat          | 1.13 sec                                                                    | 1.15 sec: 1.02x slower                                                  |
| comprehensions          | 12.2 us                                                                     | 12.4 us: 1.02x slower                                                   |
| json_dumps              | 6.64 ms                                                                     | 6.78 ms: 1.02x slower                                                   |
| django_template         | 25.0 ms                                                                     | 25.6 ms: 1.02x slower                                                   |
| scimark_monte_carlo     | 48.0 ms                                                                     | 49.0 ms: 1.02x slower                                                   |
| hexiom                  | 4.51 ms                                                                     | 4.61 ms: 1.02x slower                                                   |
| scimark_lu              | 64.8 ms                                                                     | 66.3 ms: 1.02x slower                                                   |
| deepcopy                | 191 us                                                                      | 195 us: 1.02x slower                                                    |
| json                    | 3.01 ms                                                                     | 3.09 ms: 1.03x slower                                                   |
| dulwich_log             | 42.0 ms                                                                     | 43.1 ms: 1.03x slower                                                   |
| subparsers              | 16.4 ms                                                                     | 16.9 ms: 1.03x slower                                                   |
| deepcopy_memo           | 21.2 us                                                                     | 22.0 us: 1.04x slower                                                   |
| deepcopy_reduce         | 1.95 us                                                                     | 2.03 us: 1.04x slower                                                   |
| Geometric mean          | (ref)                                                                       | 1.00x slower                                                            |

Benchmark hidden because not significant (42): many_optionals, create_gc_cycles, mako, pylint, k_core, generators, async_tree_io_tg, regex_compile, sympy_sum, chaos, bench_mp_pool, xml_etree_iterparse, sqlglot_normalize, typing_runtime_protocols, sympy_str, async_tree_memoization, go, async_tree_none_tg, async_tree_io, pathlib, python_startup_no_site, sqlglot_optimize, async_tree_memoization_tg, pidigits, 2to3, sympy_integrate, coroutines, telco, float, shortest_path, connected_components, async_tree_cpu_io_mixed_tg, genshi_text, pprint_safe_repr, bench_thread_pool, regex_effbot, genshi_xml, sphinx, async_tree_cpu_io_mixed, pycparser, async_tree_none, asyncio_websockets

- Geometric mean (including insignificant results): 1.001x slower
# HPT report

- Reliability score: 91.28% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown