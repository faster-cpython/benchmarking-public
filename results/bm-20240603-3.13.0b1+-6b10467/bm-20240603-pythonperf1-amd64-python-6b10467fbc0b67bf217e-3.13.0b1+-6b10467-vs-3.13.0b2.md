# Results vs. 3.13.0b2

- fork: python
- ref: 6b10467fbc0b67bf217e
- machine: windows-amd64
- commit hash: 6b10467
- commit date: 2024-06-03
- overall geometric mean: 1.00x faster
- HPT reliability: 73.30%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240603-pythonperf1-amd64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| chameleon      | 4.80 ms                                                         | 4.70 ms: 1.02x faster                                                       |
| docutils       | 1.63 sec                                                        | 1.61 sec: 1.01x faster                                                      |
| html5lib       | 35.0 ms                                                         | 35.3 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                           | 1.00x faster                                                                |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_io, async_tree_none, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_none_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240603-pythonperf1-amd64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 67.2 ms: 1.01x faster                                                       |
| float          | 49.7 ms                                                         | 50.6 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240603-pythonperf1-amd64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 15.8 ms                                                         | 14.1 ms: 1.12x faster                                                       |
| regex_effbot   | 1.58 ms                                                         | 1.55 ms: 1.02x faster                                                       |
| regex_compile  | 78.0 ms                                                         | 77.0 ms: 1.01x faster                                                       |
| regex_dna      | 119 ms                                                          | 118 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240603-pythonperf1-amd64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_loads           | 14.2 us                                                         | 13.7 us: 1.03x faster                                                       |
| json_dumps           | 5.61 ms                                                         | 5.55 ms: 1.01x faster                                                       |
| xml_etree_iterparse  | 62.3 ms                                                         | 61.8 ms: 1.01x faster                                                       |
| unpickle_pure_python | 122 us                                                          | 123 us: 1.01x slower                                                        |
| pickle               | 7.11 us                                                         | 7.19 us: 1.01x slower                                                       |
| tomli_loads          | 1.35 sec                                                        | 1.37 sec: 1.01x slower                                                      |
| pickle_dict          | 18.1 us                                                         | 18.4 us: 1.02x slower                                                       |
| unpickle_list        | 2.62 us                                                         | 2.68 us: 1.02x slower                                                       |
| pickle_list          | 2.90 us                                                         | 3.03 us: 1.04x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.01x slower                                                                |

Benchmark hidden because not significant (5): xml_etree_process, pickle_pure_python, xml_etree_generate, xml_etree_parse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240603-pythonperf1-amd64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                         | 16.5 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                           | 1.01x slower                                                                |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240603-pythonperf1-amd64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text    | 14.4 ms                                                         | 14.7 ms: 1.03x slower                                                       |
| genshi_xml     | 31.6 ms                                                         | 33.1 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark               | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240603-pythonperf1-amd64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|-------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8                | 15.8 ms                                                         | 14.1 ms: 1.12x faster                                                       |
| json                    | 3.19 ms                                                         | 2.97 ms: 1.07x faster                                                       |
| scimark_sparse_mat_mult | 2.50 ms                                                         | 2.39 ms: 1.05x faster                                                       |
| scimark_lu              | 56.6 ms                                                         | 54.1 ms: 1.05x faster                                                       |
| richards                | 26.7 ms                                                         | 25.7 ms: 1.04x faster                                                       |
| json_loads              | 14.2 us                                                         | 13.7 us: 1.03x faster                                                       |
| richards_super          | 30.2 ms                                                         | 29.3 ms: 1.03x faster                                                       |
| regex_effbot            | 1.58 ms                                                         | 1.55 ms: 1.02x faster                                                       |
| scimark_fft             | 171 ms                                                          | 167 ms: 1.02x faster                                                        |
| chameleon               | 4.80 ms                                                         | 4.70 ms: 1.02x faster                                                       |
| spectral_norm           | 63.7 ms                                                         | 62.4 ms: 1.02x faster                                                       |
| chaos                   | 38.4 ms                                                         | 37.6 ms: 1.02x faster                                                       |
| raytrace                | 162 ms                                                          | 159 ms: 1.02x faster                                                        |
| crypto_pyaes            | 45.5 ms                                                         | 44.6 ms: 1.02x faster                                                       |
| scimark_sor             | 75.3 ms                                                         | 74.1 ms: 1.02x faster                                                       |
| logging_format          | 6.22 us                                                         | 6.13 us: 1.02x faster                                                       |
| telco                   | 4.67 ms                                                         | 4.60 ms: 1.02x faster                                                       |
| pathlib                 | 75.9 ms                                                         | 74.8 ms: 1.01x faster                                                       |
| logging_simple          | 5.78 us                                                         | 5.71 us: 1.01x faster                                                       |
| regex_compile           | 78.0 ms                                                         | 77.0 ms: 1.01x faster                                                       |
| json_dumps              | 5.61 ms                                                         | 5.55 ms: 1.01x faster                                                       |
| logging_silent          | 52.9 ns                                                         | 52.4 ns: 1.01x faster                                                       |
| regex_dna               | 119 ms                                                          | 118 ms: 1.01x faster                                                        |
| deepcopy_reduce         | 1.99 us                                                         | 1.98 us: 1.01x faster                                                       |
| xml_etree_iterparse     | 62.3 ms                                                         | 61.8 ms: 1.01x faster                                                       |
| generators              | 19.6 ms                                                         | 19.4 ms: 1.01x faster                                                       |
| docutils                | 1.63 sec                                                        | 1.61 sec: 1.01x faster                                                      |
| deepcopy                | 220 us                                                          | 218 us: 1.01x faster                                                        |
| hexiom                  | 3.72 ms                                                         | 3.70 ms: 1.01x faster                                                       |
| nbody                   | 67.6 ms                                                         | 67.2 ms: 1.01x faster                                                       |
| sqlglot_normalize       | 173 ms                                                          | 174 ms: 1.01x slower                                                        |
| unpickle_pure_python    | 122 us                                                          | 123 us: 1.01x slower                                                        |
| coroutines              | 12.8 ms                                                         | 12.8 ms: 1.01x slower                                                       |
| deepcopy_memo           | 22.1 us                                                         | 22.3 us: 1.01x slower                                                       |
| html5lib                | 35.0 ms                                                         | 35.3 ms: 1.01x slower                                                       |
| scimark_monte_carlo     | 39.1 ms                                                         | 39.4 ms: 1.01x slower                                                       |
| sqlglot_optimize        | 32.7 ms                                                         | 33.0 ms: 1.01x slower                                                       |
| pickle                  | 7.11 us                                                         | 7.19 us: 1.01x slower                                                       |
| dulwich_log             | 38.0 ms                                                         | 38.5 ms: 1.01x slower                                                       |
| sympy_str               | 159 ms                                                          | 161 ms: 1.01x slower                                                        |
| tomli_loads             | 1.35 sec                                                        | 1.37 sec: 1.01x slower                                                      |
| pickle_dict             | 18.1 us                                                         | 18.4 us: 1.02x slower                                                       |
| sqlglot_transpile       | 955 us                                                          | 971 us: 1.02x slower                                                        |
| float                   | 49.7 ms                                                         | 50.6 ms: 1.02x slower                                                       |
| sympy_expand            | 271 ms                                                          | 276 ms: 1.02x slower                                                        |
| pprint_safe_repr        | 474 ms                                                          | 483 ms: 1.02x slower                                                        |
| create_gc_cycles        | 888 us                                                          | 906 us: 1.02x slower                                                        |
| python_startup_no_site  | 16.2 ms                                                         | 16.5 ms: 1.02x slower                                                       |
| pprint_pformat          | 966 ms                                                          | 987 ms: 1.02x slower                                                        |
| mdp                     | 1.31 sec                                                        | 1.34 sec: 1.02x slower                                                      |
| unpickle_list           | 2.62 us                                                         | 2.68 us: 1.02x slower                                                       |
| sqlglot_parse           | 748 us                                                          | 768 us: 1.03x slower                                                        |
| fannkuch                | 243 ms                                                          | 250 ms: 1.03x slower                                                        |
| genshi_text             | 14.4 ms                                                         | 14.7 ms: 1.03x slower                                                       |
| coverage                | 42.1 ms                                                         | 43.2 ms: 1.03x slower                                                       |
| meteor_contest          | 69.9 ms                                                         | 72.0 ms: 1.03x slower                                                       |
| bench_thread_pool       | 768 us                                                          | 794 us: 1.03x slower                                                        |
| pickle_list             | 2.90 us                                                         | 3.03 us: 1.04x slower                                                       |
| genshi_xml              | 31.6 ms                                                         | 33.1 ms: 1.05x slower                                                       |
| Geometric mean          | (ref)                                                           | 1.00x faster                                                                |

Benchmark hidden because not significant (39): pycparser, asyncio_tcp_ssl, async_tree_io, async_tree_none, pylint, async_tree_cpu_io_mixed, async_tree_memoization, django_template, thrift, comprehensions, go, gc_traversal, xml_etree_process, mako, flaskblogging, 2to3, pickle_pure_python, nqueens, async_generators, async_tree_cpu_io_mixed_tg, sympy_integrate, mypy2, pidigits, pyflate, sympy_sum, xml_etree_generate, aiohttp, deltablue, asyncio_tcp, async_tree_io_tg, tornado_http, xml_etree_parse, python_startup, unpickle, bench_mp_pool, typing_runtime_protocols, sqlite_synth, async_tree_none_tg, async_tree_memoization_tg

# HPT report

- Reliability score: 73.30% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown