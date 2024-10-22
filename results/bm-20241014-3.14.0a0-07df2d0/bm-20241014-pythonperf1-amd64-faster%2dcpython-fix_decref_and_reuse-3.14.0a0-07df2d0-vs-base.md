# Results vs. base

- fork: faster-cpython
- ref: fix_decref_and_reuse
- machine: windows-amd64
- commit hash: 07df2d0
- commit date: 2024-10-14
- overall geometric mean: 1.00x faster
- HPT reliability: 96.75%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241014-pythonperf1-amd64-python-5217328f93f599755bd7-3.14.0a0-5217328 | bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| docutils       | 1.74 sec                                                                   | 1.73 sec: 1.01x faster                                                               |
| Geometric mean | (ref)                                                                      | 1.00x faster                                                                         |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241014-pythonperf1-amd64-python-5217328f93f599755bd7-3.14.0a0-5217328 | bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_generators | 250 ms                                                                     | 247 ms: 1.01x faster                                                                 |
| asyncio_tcp_ssl  | 1.61 sec                                                                   | 1.71 sec: 1.06x slower                                                               |
| Geometric mean   | (ref)                                                                      | 1.01x slower                                                                         |

Benchmark hidden because not significant (2): asyncio_tcp, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241014-pythonperf1-amd64-python-5217328f93f599755bd7-3.14.0a0-5217328 | bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| nbody          | 81.7 ms                                                                    | 74.9 ms: 1.09x faster                                                                |
| float          | 54.8 ms                                                                    | 53.3 ms: 1.03x faster                                                                |
| Geometric mean | (ref)                                                                      | 1.04x faster                                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241014-pythonperf1-amd64-python-5217328f93f599755bd7-3.14.0a0-5217328 | bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_v8       | 15.0 ms                                                                    | 15.6 ms: 1.04x slower                                                                |
| regex_effbot   | 1.58 ms                                                                    | 1.64 ms: 1.04x slower                                                                |
| regex_dna      | 117 ms                                                                     | 123 ms: 1.05x slower                                                                 |
| Geometric mean | (ref)                                                                      | 1.03x slower                                                                         |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241014-pythonperf1-amd64-python-5217328f93f599755bd7-3.14.0a0-5217328 | bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 66.7 ms                                                                    | 65.5 ms: 1.02x faster                                                                |
| xml_etree_generate   | 58.0 ms                                                                    | 57.4 ms: 1.01x faster                                                                |
| unpickle_pure_python | 151 us                                                                     | 149 us: 1.01x faster                                                                 |
| tomli_loads          | 1.63 sec                                                                   | 1.62 sec: 1.01x faster                                                               |
| pickle_pure_python   | 217 us                                                                     | 216 us: 1.01x faster                                                                 |
| pickle               | 7.23 us                                                                    | 7.19 us: 1.01x faster                                                                |
| pickle_dict          | 18.9 us                                                                    | 19.1 us: 1.01x slower                                                                |
| pickle_list          | 2.88 us                                                                    | 2.92 us: 1.01x slower                                                                |
| xml_etree_parse      | 95.6 ms                                                                    | 97.0 ms: 1.01x slower                                                                |
| Geometric mean       | (ref)                                                                      | 1.00x faster                                                                         |

Benchmark hidden because not significant (5): json_loads, json_dumps, unpickle_list, xml_etree_process, unpickle

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241014-pythonperf1-amd64-python-5217328f93f599755bd7-3.14.0a0-5217328 | bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| genshi_text    | 17.0 ms                                                                    | 17.1 ms: 1.01x slower                                                                |
| genshi_xml     | 37.2 ms                                                                    | 38.1 ms: 1.02x slower                                                                |
| mako           | 6.75 ms                                                                    | 7.01 ms: 1.04x slower                                                                |
| Geometric mean | (ref)                                                                      | 1.02x slower                                                                         |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20241014-pythonperf1-amd64-python-5217328f93f599755bd7-3.14.0a0-5217328 | bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|--------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| nbody                    | 81.7 ms                                                                    | 74.9 ms: 1.09x faster                                                                |
| mdp                      | 1.55 sec                                                                   | 1.46 sec: 1.06x faster                                                               |
| unpack_sequence          | 40.8 ns                                                                    | 38.4 ns: 1.06x faster                                                                |
| chaos                    | 44.4 ms                                                                    | 43.1 ms: 1.03x faster                                                                |
| float                    | 54.8 ms                                                                    | 53.3 ms: 1.03x faster                                                                |
| sqlglot_optimize         | 37.6 ms                                                                    | 36.6 ms: 1.03x faster                                                                |
| logging_format           | 6.96 us                                                                    | 6.79 us: 1.02x faster                                                                |
| sqlglot_normalize        | 199 ms                                                                     | 194 ms: 1.02x faster                                                                 |
| typing_runtime_protocols | 114 us                                                                     | 112 us: 1.02x faster                                                                 |
| raytrace                 | 195 ms                                                                     | 191 ms: 1.02x faster                                                                 |
| sympy_sum                | 91.2 ms                                                                    | 89.3 ms: 1.02x faster                                                                |
| deepcopy_reduce          | 1.99 us                                                                    | 1.95 us: 1.02x faster                                                                |
| xml_etree_iterparse      | 66.7 ms                                                                    | 65.5 ms: 1.02x faster                                                                |
| fannkuch                 | 283 ms                                                                     | 279 ms: 1.01x faster                                                                 |
| async_generators         | 250 ms                                                                     | 247 ms: 1.01x faster                                                                 |
| telco                    | 4.84 ms                                                                    | 4.79 ms: 1.01x faster                                                                |
| deepcopy_memo            | 20.3 us                                                                    | 20.0 us: 1.01x faster                                                                |
| xml_etree_generate       | 58.0 ms                                                                    | 57.4 ms: 1.01x faster                                                                |
| unpickle_pure_python     | 151 us                                                                     | 149 us: 1.01x faster                                                                 |
| scimark_fft              | 199 ms                                                                     | 197 ms: 1.01x faster                                                                 |
| tomli_loads              | 1.63 sec                                                                   | 1.62 sec: 1.01x faster                                                               |
| docutils                 | 1.74 sec                                                                   | 1.73 sec: 1.01x faster                                                               |
| pickle_pure_python       | 217 us                                                                     | 216 us: 1.01x faster                                                                 |
| pprint_safe_repr         | 543 ms                                                                     | 540 ms: 1.01x faster                                                                 |
| sympy_expand             | 308 ms                                                                     | 306 ms: 1.01x faster                                                                 |
| scimark_sor              | 90.2 ms                                                                    | 89.7 ms: 1.01x faster                                                                |
| meteor_contest           | 76.9 ms                                                                    | 76.5 ms: 1.01x faster                                                                |
| pickle                   | 7.23 us                                                                    | 7.19 us: 1.01x faster                                                                |
| pprint_pformat           | 1.12 sec                                                                   | 1.12 sec: 1.01x faster                                                               |
| spectral_norm            | 68.5 ms                                                                    | 68.2 ms: 1.00x faster                                                                |
| scimark_monte_carlo      | 47.3 ms                                                                    | 47.5 ms: 1.00x slower                                                                |
| logging_silent           | 61.4 ns                                                                    | 61.7 ns: 1.00x slower                                                                |
| pyflate                  | 321 ms                                                                     | 323 ms: 1.01x slower                                                                 |
| pickle_dict              | 18.9 us                                                                    | 19.1 us: 1.01x slower                                                                |
| richards                 | 32.5 ms                                                                    | 32.7 ms: 1.01x slower                                                                |
| pycparser                | 733 ms                                                                     | 739 ms: 1.01x slower                                                                 |
| genshi_text              | 17.0 ms                                                                    | 17.1 ms: 1.01x slower                                                                |
| sqlglot_transpile        | 1.12 ms                                                                    | 1.13 ms: 1.01x slower                                                                |
| gc_traversal             | 1.53 ms                                                                    | 1.55 ms: 1.01x slower                                                                |
| pickle_list              | 2.88 us                                                                    | 2.92 us: 1.01x slower                                                                |
| scimark_lu               | 62.1 ms                                                                    | 62.9 ms: 1.01x slower                                                                |
| xml_etree_parse          | 95.6 ms                                                                    | 97.0 ms: 1.01x slower                                                                |
| richards_super           | 36.7 ms                                                                    | 37.3 ms: 1.02x slower                                                                |
| hexiom                   | 4.35 ms                                                                    | 4.43 ms: 1.02x slower                                                                |
| sqlglot_parse            | 902 us                                                                     | 920 us: 1.02x slower                                                                 |
| deltablue                | 2.29 ms                                                                    | 2.34 ms: 1.02x slower                                                                |
| genshi_xml               | 37.2 ms                                                                    | 38.1 ms: 1.02x slower                                                                |
| create_gc_cycles         | 916 us                                                                     | 940 us: 1.03x slower                                                                 |
| regex_v8                 | 15.0 ms                                                                    | 15.6 ms: 1.04x slower                                                                |
| scimark_sparse_mat_mult  | 2.63 ms                                                                    | 2.73 ms: 1.04x slower                                                                |
| regex_effbot             | 1.58 ms                                                                    | 1.64 ms: 1.04x slower                                                                |
| mako                     | 6.75 ms                                                                    | 7.01 ms: 1.04x slower                                                                |
| regex_dna                | 117 ms                                                                     | 123 ms: 1.05x slower                                                                 |
| asyncio_tcp_ssl          | 1.61 sec                                                                   | 1.71 sec: 1.06x slower                                                               |
| Geometric mean           | (ref)                                                                      | 1.00x faster                                                                         |

Benchmark hidden because not significant (33): bench_thread_pool, json, json_loads, tornado_http, generators, html5lib, crypto_pyaes, django_template, bench_mp_pool, dulwich_log, pylint, pathlib, sympy_integrate, thrift, asyncio_tcp, python_startup, regex_compile, json_dumps, nqueens, unpickle_list, deepcopy, coroutines, sympy_str, sqlite_synth, logging_simple, go, pidigits, xml_etree_process, coverage, unpickle, comprehensions, python_startup_no_site, 2to3

# HPT report

- Reliability score: 96.75% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown