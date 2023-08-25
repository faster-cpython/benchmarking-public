
# Results vs. 3.10.4

- fork: python
- ref: 7d4cc5aa854fdea4d01a
- machine: windows-amd64
- commit hash: 7d4cc5a
- commit date: 2023-04-04
- overall geometric mean: 1.00x slower \*
- HPT reliability: 87.38%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-pythonperf1-amd64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 233 ms: 1.02x faster                                                      |
| chameleon      | 5.92 ms                                                     | 5.67 ms: 1.05x faster                                                     |
| docutils       | 1.89 sec                                                    | 1.82 sec: 1.04x faster                                                    |
| html5lib       | 46.5 ms                                                     | 45.8 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                       | 1.02x faster                                                              |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-pythonperf1-amd64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 60.7 ms: 1.01x slower                                                     |
| pidigits       | 145 ms                                                      | 147 ms: 1.01x slower                                                      |
| nbody          | 69.3 ms                                                     | 75.5 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                       | 1.03x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-pythonperf1-amd64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                                     |
| regex_v8       | 15.0 ms                                                     | 14.6 ms: 1.03x faster                                                     |
| regex_dna      | 132 ms                                                      | 129 ms: 1.02x faster                                                      |
| regex_compile  | 103 ms                                                      | 102 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                       | 1.02x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-pythonperf1-amd64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_list        | 2.81 us                                                     | 2.66 us: 1.06x faster                                                     |
| xml_etree_parse      | 102 ms                                                      | 96.4 ms: 1.06x faster                                                     |
| json_loads           | 14.2 us                                                     | 13.7 us: 1.03x faster                                                     |
| unpickle_pure_python | 171 us                                                      | 177 us: 1.03x slower                                                      |
| pickle_pure_python   | 257 us                                                      | 266 us: 1.04x slower                                                      |
| json_dumps           | 8.50 ms                                                     | 8.90 ms: 1.05x slower                                                     |
| pickle               | 6.80 us                                                     | 7.34 us: 1.08x slower                                                     |
| pickle_list          | 2.59 us                                                     | 2.86 us: 1.10x slower                                                     |
| pickle_dict          | 16.9 us                                                     | 18.7 us: 1.11x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                              |

Benchmark hidden because not significant (4): xml_etree_generate, xml_etree_iterparse, xml_etree_process, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-pythonperf1-amd64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup | 20.0 ms                                                     | 21.1 ms: 1.05x slower                                                     |
| Geometric mean | (ref)                                                       | 1.03x slower                                                              |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-pythonperf1-amd64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_xml      | 40.5 ms                                                     | 39.1 ms: 1.04x faster                                                     |
| genshi_text     | 19.0 ms                                                     | 18.8 ms: 1.01x faster                                                     |
| django_template | 28.2 ms                                                     | 28.9 ms: 1.02x slower                                                     |
| Geometric mean  | (ref)                                                       | 1.01x faster                                                              |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-pythonperf1-amd64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|-------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_list           | 2.81 us                                                     | 2.66 us: 1.06x faster                                                     |
| xml_etree_parse         | 102 ms                                                      | 96.4 ms: 1.06x faster                                                     |
| aiohttp                 | 1.01 ms                                                     | 962 us: 1.05x faster                                                      |
| chameleon               | 5.92 ms                                                     | 5.67 ms: 1.05x faster                                                     |
| pathlib                 | 77.4 ms                                                     | 74.4 ms: 1.04x faster                                                     |
| docutils                | 1.89 sec                                                    | 1.82 sec: 1.04x faster                                                    |
| regex_effbot            | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                                     |
| genshi_xml              | 40.5 ms                                                     | 39.1 ms: 1.04x faster                                                     |
| pycparser               | 868 ms                                                      | 839 ms: 1.03x faster                                                      |
| async_tree_memoization  | 497 ms                                                      | 481 ms: 1.03x faster                                                      |
| json_loads              | 14.2 us                                                     | 13.7 us: 1.03x faster                                                     |
| sqlglot_transpile       | 1.46 ms                                                     | 1.42 ms: 1.03x faster                                                     |
| async_tree_io           | 1.07 sec                                                    | 1.04 sec: 1.03x faster                                                    |
| sqlglot_parse           | 1.22 ms                                                     | 1.19 ms: 1.03x faster                                                     |
| regex_v8                | 15.0 ms                                                     | 14.6 ms: 1.03x faster                                                     |
| async_generators        | 224 ms                                                      | 218 ms: 1.03x faster                                                      |
| comprehensions          | 16.0 us                                                     | 15.6 us: 1.03x faster                                                     |
| regex_dna               | 132 ms                                                      | 129 ms: 1.02x faster                                                      |
| coverage                | 40.0 ms                                                     | 39.2 ms: 1.02x faster                                                     |
| hexiom                  | 5.52 ms                                                     | 5.40 ms: 1.02x faster                                                     |
| bench_thread_pool       | 946 us                                                      | 928 us: 1.02x faster                                                      |
| async_tree_cpu_io_mixed | 609 ms                                                      | 598 ms: 1.02x faster                                                      |
| pylint                  | 347 ms                                                      | 341 ms: 1.02x faster                                                      |
| 2to3                    | 237 ms                                                      | 233 ms: 1.02x faster                                                      |
| coroutines              | 15.9 ms                                                     | 15.7 ms: 1.02x faster                                                     |
| deltablue               | 4.17 ms                                                     | 4.11 ms: 1.02x faster                                                     |
| html5lib                | 46.5 ms                                                     | 45.8 ms: 1.01x faster                                                     |
| regex_compile           | 103 ms                                                      | 102 ms: 1.01x faster                                                      |
| genshi_text             | 19.0 ms                                                     | 18.8 ms: 1.01x faster                                                     |
| scimark_lu              | 85.4 ms                                                     | 84.5 ms: 1.01x faster                                                     |
| sqlglot_optimize        | 39.0 ms                                                     | 38.5 ms: 1.01x faster                                                     |
| deepcopy_reduce         | 2.16 us                                                     | 2.13 us: 1.01x faster                                                     |
| pprint_pformat          | 1.21 sec                                                    | 1.19 sec: 1.01x faster                                                    |
| sympy_expand            | 315 ms                                                      | 312 ms: 1.01x faster                                                      |
| json                    | 3.05 ms                                                     | 3.02 ms: 1.01x faster                                                     |
| pprint_safe_repr        | 589 ms                                                      | 584 ms: 1.01x faster                                                      |
| meteor_contest          | 72.5 ms                                                     | 72.1 ms: 1.01x faster                                                     |
| richards                | 41.2 ms                                                     | 40.9 ms: 1.01x faster                                                     |
| bench_mp_pool           | 60.7 ms                                                     | 60.4 ms: 1.01x faster                                                     |
| sqlglot_normalize       | 202 ms                                                      | 202 ms: 1.00x faster                                                      |
| flaskblogging           | 2.04 sec                                                    | 2.05 sec: 1.00x slower                                                    |
| chaos                   | 58.9 ms                                                     | 59.2 ms: 1.01x slower                                                     |
| nqueens                 | 67.0 ms                                                     | 67.5 ms: 1.01x slower                                                     |
| float                   | 60.2 ms                                                     | 60.7 ms: 1.01x slower                                                     |
| pidigits                | 145 ms                                                      | 147 ms: 1.01x slower                                                      |
| pyflate                 | 387 ms                                                      | 391 ms: 1.01x slower                                                      |
| logging_simple          | 6.20 us                                                     | 6.28 us: 1.01x slower                                                     |
| crypto_pyaes            | 62.3 ms                                                     | 63.2 ms: 1.01x slower                                                     |
| logging_format          | 6.66 us                                                     | 6.76 us: 1.01x slower                                                     |
| generators              | 31.6 ms                                                     | 32.1 ms: 1.01x slower                                                     |
| sqlalchemy_imperative   | 11.0 ms                                                     | 11.1 ms: 1.02x slower                                                     |
| deepcopy                | 255 us                                                      | 260 us: 1.02x slower                                                      |
| thrift                  | 615 us                                                      | 629 us: 1.02x slower                                                      |
| scimark_sor             | 105 ms                                                      | 107 ms: 1.02x slower                                                      |
| django_template         | 28.2 ms                                                     | 28.9 ms: 1.02x slower                                                     |
| unpickle_pure_python    | 171 us                                                      | 177 us: 1.03x slower                                                      |
| pickle_pure_python      | 257 us                                                      | 266 us: 1.04x slower                                                      |
| telco                   | 3.78 ms                                                     | 3.93 ms: 1.04x slower                                                     |
| spectral_norm           | 78.0 ms                                                     | 81.4 ms: 1.04x slower                                                     |
| json_dumps              | 8.50 ms                                                     | 8.90 ms: 1.05x slower                                                     |
| scimark_fft             | 193 ms                                                      | 203 ms: 1.05x slower                                                      |
| gc_traversal            | 1.34 ms                                                     | 1.42 ms: 1.05x slower                                                     |
| python_startup          | 20.0 ms                                                     | 21.1 ms: 1.05x slower                                                     |
| scimark_monte_carlo     | 55.9 ms                                                     | 58.9 ms: 1.05x slower                                                     |
| asyncio_tcp             | 712 ms                                                      | 755 ms: 1.06x slower                                                      |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.83 ms: 1.06x slower                                                     |
| fannkuch                | 258 ms                                                      | 276 ms: 1.07x slower                                                      |
| pickle                  | 6.80 us                                                     | 7.34 us: 1.08x slower                                                     |
| nbody                   | 69.3 ms                                                     | 75.5 ms: 1.09x slower                                                     |
| pickle_list             | 2.59 us                                                     | 2.86 us: 1.10x slower                                                     |
| pickle_dict             | 16.9 us                                                     | 18.7 us: 1.11x slower                                                     |
| unpack_sequence         | 37.8 ns                                                     | 42.1 ns: 1.11x slower                                                     |
| Geometric mean          | (ref)                                                       | 1.00x slower                                                              |

Benchmark hidden because not significant (22): mypy2, async_tree_none, tornado_http, dask, create_gc_cycles, mako, xml_etree_generate, sympy_integrate, xml_etree_iterparse, raytrace, dulwich_log, mdp, sympy_str, deepcopy_memo, xml_etree_process, sqlite_synth, sympy_sum, sqlalchemy_declarative, go, python_startup_no_site, logging_silent, unpickle
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 87.38% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
