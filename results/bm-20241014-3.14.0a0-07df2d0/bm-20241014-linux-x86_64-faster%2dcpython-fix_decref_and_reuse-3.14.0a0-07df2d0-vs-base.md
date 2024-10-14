# Results vs. base

- fork: faster-cpython
- ref: fix_decref_and_reuse
- machine: linux-x86_64
- commit hash: 07df2d0
- commit date: 2024-10-14
- overall geometric mean: 1.01x slower
- HPT reliability: 99.91%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241014-linux-x86_64-python-5217328f93f599755bd7-3.14.0a0-5217328 | bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                | 255 ms: 1.00x slower                                                            |
| docutils       | 2.63 sec                                                              | 2.62 sec: 1.00x faster                                                          |
| html5lib       | 63.0 ms                                                               | 62.1 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241014-linux-x86_64-python-5217328f93f599755bd7-3.14.0a0-5217328 | bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| coroutines       | 23.8 ms                                                               | 23.4 ms: 1.02x faster                                                           |
| asyncio_tcp      | 483 ms                                                                | 480 ms: 1.01x faster                                                            |
| asyncio_tcp_ssl  | 1.79 sec                                                              | 1.79 sec: 1.00x slower                                                          |
| async_generators | 432 ms                                                                | 438 ms: 1.01x slower                                                            |
| Geometric mean   | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241014-linux-x86_64-python-5217328f93f599755bd7-3.14.0a0-5217328 | bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 192 ms                                                                | 188 ms: 1.02x faster                                                            |
| float          | 77.3 ms                                                               | 78.3 ms: 1.01x slower                                                           |
| nbody          | 91.1 ms                                                               | 94.2 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241014-linux-x86_64-python-5217328f93f599755bd7-3.14.0a0-5217328 | bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 128 ms                                                                | 129 ms: 1.01x slower                                                            |
| regex_effbot   | 3.58 ms                                                               | 3.63 ms: 1.01x slower                                                           |
| regex_dna      | 217 ms                                                                | 221 ms: 1.02x slower                                                            |
| regex_v8       | 24.2 ms                                                               | 25.0 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241014-linux-x86_64-python-5217328f93f599755bd7-3.14.0a0-5217328 | bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 11.5 ms                                                               | 11.2 ms: 1.02x faster                                                           |
| json_loads           | 26.6 us                                                               | 26.8 us: 1.01x slower                                                           |
| xml_etree_process    | 59.3 ms                                                               | 59.8 ms: 1.01x slower                                                           |
| xml_etree_iterparse  | 104 ms                                                                | 105 ms: 1.01x slower                                                            |
| xml_etree_generate   | 85.1 ms                                                               | 86.3 ms: 1.01x slower                                                           |
| unpickle_list        | 5.34 us                                                               | 5.43 us: 1.02x slower                                                           |
| pickle_pure_python   | 307 us                                                                | 313 us: 1.02x slower                                                            |
| unpickle_pure_python | 218 us                                                                | 222 us: 1.02x slower                                                            |
| pickle_dict          | 34.2 us                                                               | 35.0 us: 1.02x slower                                                           |
| pickle               | 11.4 us                                                               | 11.9 us: 1.04x slower                                                           |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (4): xml_etree_parse, pickle_list, tomli_loads, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241014-linux-x86_64-python-5217328f93f599755bd7-3.14.0a0-5217328 | bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 7.03 ms                                                               | 7.02 ms: 1.00x faster                                                           |
| python_startup         | 10.6 ms                                                               | 10.6 ms: 1.00x faster                                                           |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241014-linux-x86_64-python-5217328f93f599755bd7-3.14.0a0-5217328 | bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                               | 11.4 ms: 1.04x faster                                                           |
| django_template | 34.0 ms                                                               | 34.1 ms: 1.00x slower                                                           |
| genshi_text     | 22.8 ms                                                               | 23.0 ms: 1.01x slower                                                           |
| genshi_xml      | 50.9 ms                                                               | 51.9 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20241014-linux-x86_64-python-5217328f93f599755bd7-3.14.0a0-5217328 | bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako                     | 11.9 ms                                                               | 11.4 ms: 1.04x faster                                                           |
| pycparser                | 1.17 sec                                                              | 1.13 sec: 1.04x faster                                                          |
| gc_traversal             | 4.02 ms                                                               | 3.89 ms: 1.03x faster                                                           |
| json_dumps               | 11.5 ms                                                               | 11.2 ms: 1.02x faster                                                           |
| pidigits                 | 192 ms                                                                | 188 ms: 1.02x faster                                                            |
| coroutines               | 23.8 ms                                                               | 23.4 ms: 1.02x faster                                                           |
| html5lib                 | 63.0 ms                                                               | 62.1 ms: 1.02x faster                                                           |
| logging_simple           | 5.68 us                                                               | 5.62 us: 1.01x faster                                                           |
| logging_format           | 6.34 us                                                               | 6.26 us: 1.01x faster                                                           |
| sqlite_synth             | 2.89 us                                                               | 2.85 us: 1.01x faster                                                           |
| pyflate                  | 467 ms                                                                | 462 ms: 1.01x faster                                                            |
| create_gc_cycles         | 1.80 ms                                                               | 1.78 ms: 1.01x faster                                                           |
| sympy_sum                | 148 ms                                                                | 147 ms: 1.01x faster                                                            |
| typing_runtime_protocols | 161 us                                                                | 160 us: 1.01x faster                                                            |
| asyncio_tcp              | 483 ms                                                                | 480 ms: 1.01x faster                                                            |
| docutils                 | 2.63 sec                                                              | 2.62 sec: 1.00x faster                                                          |
| bench_thread_pool        | 842 us                                                                | 838 us: 1.00x faster                                                            |
| sqlglot_optimize         | 53.5 ms                                                               | 53.4 ms: 1.00x faster                                                           |
| python_startup_no_site   | 7.03 ms                                                               | 7.02 ms: 1.00x faster                                                           |
| python_startup           | 10.6 ms                                                               | 10.6 ms: 1.00x faster                                                           |
| asyncio_tcp_ssl          | 1.79 sec                                                              | 1.79 sec: 1.00x slower                                                          |
| sympy_expand             | 453 ms                                                                | 455 ms: 1.00x slower                                                            |
| 2to3                     | 254 ms                                                                | 255 ms: 1.00x slower                                                            |
| sqlglot_transpile        | 1.59 ms                                                               | 1.59 ms: 1.00x slower                                                           |
| django_template          | 34.0 ms                                                               | 34.1 ms: 1.00x slower                                                           |
| sqlglot_normalize        | 106 ms                                                                | 106 ms: 1.00x slower                                                            |
| bench_mp_pool            | 56.0 ms                                                               | 56.2 ms: 1.00x slower                                                           |
| sqlglot_parse            | 1.29 ms                                                               | 1.29 ms: 1.01x slower                                                           |
| hexiom                   | 6.35 ms                                                               | 6.38 ms: 1.01x slower                                                           |
| json_loads               | 26.6 us                                                               | 26.8 us: 1.01x slower                                                           |
| xml_etree_process        | 59.3 ms                                                               | 59.8 ms: 1.01x slower                                                           |
| richards                 | 46.9 ms                                                               | 47.3 ms: 1.01x slower                                                           |
| regex_compile            | 128 ms                                                                | 129 ms: 1.01x slower                                                            |
| richards_super           | 52.5 ms                                                               | 53.0 ms: 1.01x slower                                                           |
| genshi_text              | 22.8 ms                                                               | 23.0 ms: 1.01x slower                                                           |
| deltablue                | 3.28 ms                                                               | 3.31 ms: 1.01x slower                                                           |
| pprint_pformat           | 1.48 sec                                                              | 1.49 sec: 1.01x slower                                                          |
| xml_etree_iterparse      | 104 ms                                                                | 105 ms: 1.01x slower                                                            |
| regex_effbot             | 3.58 ms                                                               | 3.63 ms: 1.01x slower                                                           |
| pprint_safe_repr         | 720 ms                                                                | 729 ms: 1.01x slower                                                            |
| async_generators         | 432 ms                                                                | 438 ms: 1.01x slower                                                            |
| float                    | 77.3 ms                                                               | 78.3 ms: 1.01x slower                                                           |
| xml_etree_generate       | 85.1 ms                                                               | 86.3 ms: 1.01x slower                                                           |
| scimark_lu               | 114 ms                                                                | 116 ms: 1.01x slower                                                            |
| deepcopy                 | 257 us                                                                | 261 us: 1.01x slower                                                            |
| mdp                      | 2.50 sec                                                              | 2.53 sec: 1.02x slower                                                          |
| go                       | 120 ms                                                                | 122 ms: 1.02x slower                                                            |
| unpickle_list            | 5.34 us                                                               | 5.43 us: 1.02x slower                                                           |
| regex_dna                | 217 ms                                                                | 221 ms: 1.02x slower                                                            |
| nqueens                  | 79.9 ms                                                               | 81.4 ms: 1.02x slower                                                           |
| pickle_pure_python       | 307 us                                                                | 313 us: 1.02x slower                                                            |
| deepcopy_reduce          | 2.63 us                                                               | 2.68 us: 1.02x slower                                                           |
| unpickle_pure_python     | 218 us                                                                | 222 us: 1.02x slower                                                            |
| genshi_xml               | 50.9 ms                                                               | 51.9 ms: 1.02x slower                                                           |
| chaos                    | 59.6 ms                                                               | 61.0 ms: 1.02x slower                                                           |
| pickle_dict              | 34.2 us                                                               | 35.0 us: 1.02x slower                                                           |
| deepcopy_memo            | 30.4 us                                                               | 31.2 us: 1.03x slower                                                           |
| crypto_pyaes             | 72.1 ms                                                               | 74.1 ms: 1.03x slower                                                           |
| raytrace                 | 264 ms                                                                | 271 ms: 1.03x slower                                                            |
| regex_v8                 | 24.2 ms                                                               | 25.0 ms: 1.03x slower                                                           |
| generators               | 27.1 ms                                                               | 28.0 ms: 1.03x slower                                                           |
| nbody                    | 91.1 ms                                                               | 94.2 ms: 1.03x slower                                                           |
| scimark_monte_carlo      | 67.1 ms                                                               | 69.7 ms: 1.04x slower                                                           |
| scimark_fft              | 352 ms                                                                | 367 ms: 1.04x slower                                                            |
| pickle                   | 11.4 us                                                               | 11.9 us: 1.04x slower                                                           |
| scimark_sparse_mat_mult  | 4.52 ms                                                               | 4.76 ms: 1.05x slower                                                           |
| logging_silent           | 103 ns                                                                | 109 ns: 1.06x slower                                                            |
| unpack_sequence          | 41.7 ns                                                               | 47.4 ns: 1.14x slower                                                           |
| Geometric mean           | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (21): xml_etree_parse, bpe_tokeniser, thrift, tornado_http, coverage, scimark_sor, json, pylint, sympy_integrate, dulwich_log, meteor_contest, pickle_list, pathlib, telco, asyncio_websockets, sympy_str, comprehensions, tomli_loads, fannkuch, spectral_norm, unpickle

# HPT report

- Reliability score: 99.91% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x