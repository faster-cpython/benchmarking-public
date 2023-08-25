
# Results vs. 3.10.4

- fork: python
- ref: aad5f6a89125ad4529ab
- machine: linux-x86_64
- commit hash: aad5f6a
- commit date: 2023-02-07
- overall geometric mean: 1.01x slower \*
- HPT reliability: 99.44%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-pythonperf2-x86_64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 351 ms: 1.00x slower                                                       |
| chameleon      | 9.72 ms                                                      | 9.41 ms: 1.03x faster                                                      |
| docutils       | 3.40 sec                                                     | 3.45 sec: 1.01x slower                                                     |
| tornado_http   | 152 ms                                                       | 159 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x slower                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-pythonperf2-x86_64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 271 ms                                                       | 271 ms: 1.00x slower                                                       |
| float          | 110 ms                                                       | 111 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x slower                                                               |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-pythonperf2-x86_64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 192 ms: 1.01x faster                                                       |
| regex_v8       | 26.6 ms                                                      | 27.2 ms: 1.02x slower                                                      |
| regex_effbot   | 2.99 ms                                                      | 3.49 ms: 1.17x slower                                                      |
| Geometric mean | (ref)                                                        | 1.04x slower                                                               |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-pythonperf2-x86_64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|---------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle            | 14.2 us                                                      | 13.7 us: 1.04x faster                                                      |
| xml_etree_generate  | 94.6 ms                                                      | 94.0 ms: 1.01x faster                                                      |
| pickle_pure_python  | 457 us                                                       | 461 us: 1.01x slower                                                       |
| xml_etree_parse     | 162 ms                                                       | 164 ms: 1.01x slower                                                       |
| pickle_list         | 4.11 us                                                      | 4.17 us: 1.01x slower                                                      |
| json_dumps          | 14.2 ms                                                      | 14.4 ms: 1.02x slower                                                      |
| pickle              | 9.94 us                                                      | 10.1 us: 1.02x slower                                                      |
| xml_etree_process   | 76.0 ms                                                      | 77.5 ms: 1.02x slower                                                      |
| xml_etree_iterparse | 110 ms                                                       | 113 ms: 1.03x slower                                                       |
| unpickle_list       | 4.49 us                                                      | 4.71 us: 1.05x slower                                                      |
| pickle_dict         | 30.0 us                                                      | 32.1 us: 1.07x slower                                                      |
| Geometric mean      | (ref)                                                        | 1.01x slower                                                               |

Benchmark hidden because not significant (2): unpickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-pythonperf2-x86_64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 7.32 ms                                                      | 7.34 ms: 1.00x slower                                                      |
| python_startup         | 11.5 ms                                                      | 11.5 ms: 1.00x slower                                                      |
| Geometric mean         | (ref)                                                        | 1.00x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-pythonperf2-x86_64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 64.7 ms                                                      | 62.5 ms: 1.04x faster                                                      |
| genshi_text     | 31.5 ms                                                      | 32.0 ms: 1.02x slower                                                      |
| django_template | 51.5 ms                                                      | 53.6 ms: 1.04x slower                                                      |
| Geometric mean  | (ref)                                                        | 1.00x slower                                                               |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-pythonperf2-x86_64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|-------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| fannkuch                | 496 ms                                                       | 470 ms: 1.06x faster                                                       |
| aiohttp                 | 1.21 ms                                                      | 1.15 ms: 1.05x faster                                                      |
| gunicorn                | 1.17 ms                                                      | 1.13 ms: 1.04x faster                                                      |
| unpickle                | 14.2 us                                                      | 13.7 us: 1.04x faster                                                      |
| genshi_xml              | 64.7 ms                                                      | 62.5 ms: 1.04x faster                                                      |
| chameleon               | 9.72 ms                                                      | 9.41 ms: 1.03x faster                                                      |
| bench_thread_pool       | 1.14 ms                                                      | 1.11 ms: 1.03x faster                                                      |
| pprint_pformat          | 2.15 sec                                                     | 2.11 sec: 1.02x faster                                                     |
| pprint_safe_repr        | 1.05 sec                                                     | 1.03 sec: 1.02x faster                                                     |
| coroutines              | 30.4 ms                                                      | 29.9 ms: 1.02x faster                                                      |
| pathlib                 | 21.7 ms                                                      | 21.3 ms: 1.02x faster                                                      |
| richards                | 74.1 ms                                                      | 72.9 ms: 1.02x faster                                                      |
| generators              | 58.0 ms                                                      | 57.0 ms: 1.02x faster                                                      |
| async_generators        | 422 ms                                                       | 417 ms: 1.01x faster                                                       |
| coverage                | 64.0 ms                                                      | 63.3 ms: 1.01x faster                                                      |
| sqlglot_optimize        | 70.3 ms                                                      | 69.6 ms: 1.01x faster                                                      |
| json                    | 5.96 ms                                                      | 5.91 ms: 1.01x faster                                                      |
| regex_compile           | 194 ms                                                       | 192 ms: 1.01x faster                                                       |
| xml_etree_generate      | 94.6 ms                                                      | 94.0 ms: 1.01x faster                                                      |
| asyncio_tcp             | 782 ms                                                       | 779 ms: 1.00x faster                                                       |
| pidigits                | 271 ms                                                       | 271 ms: 1.00x slower                                                       |
| 2to3                    | 350 ms                                                       | 351 ms: 1.00x slower                                                       |
| python_startup_no_site  | 7.32 ms                                                      | 7.34 ms: 1.00x slower                                                      |
| python_startup          | 11.5 ms                                                      | 11.5 ms: 1.00x slower                                                      |
| float                   | 110 ms                                                       | 111 ms: 1.00x slower                                                       |
| mypy2                   | 466 ms                                                       | 469 ms: 1.01x slower                                                       |
| mdp                     | 3.03 sec                                                     | 3.05 sec: 1.01x slower                                                     |
| logging_simple          | 8.90 us                                                      | 8.96 us: 1.01x slower                                                      |
| sqlglot_normalize       | 144 ms                                                       | 146 ms: 1.01x slower                                                       |
| pickle_pure_python      | 457 us                                                       | 461 us: 1.01x slower                                                       |
| async_tree_io           | 1.61 sec                                                     | 1.62 sec: 1.01x slower                                                     |
| async_tree_memoization  | 824 ms                                                       | 832 ms: 1.01x slower                                                       |
| logging_format          | 9.57 us                                                      | 9.67 us: 1.01x slower                                                      |
| spectral_norm           | 136 ms                                                       | 138 ms: 1.01x slower                                                       |
| dulwich_log             | 80.1 ms                                                      | 81.1 ms: 1.01x slower                                                      |
| sqlalchemy_imperative   | 22.6 ms                                                      | 22.9 ms: 1.01x slower                                                      |
| xml_etree_parse         | 162 ms                                                       | 164 ms: 1.01x slower                                                       |
| docutils                | 3.40 sec                                                     | 3.45 sec: 1.01x slower                                                     |
| pickle_list             | 4.11 us                                                      | 4.17 us: 1.01x slower                                                      |
| sympy_expand            | 599 ms                                                       | 608 ms: 1.01x slower                                                       |
| raytrace                | 488 ms                                                       | 495 ms: 1.01x slower                                                       |
| sympy_integrate         | 28.1 ms                                                      | 28.5 ms: 1.01x slower                                                      |
| telco                   | 7.14 ms                                                      | 7.25 ms: 1.01x slower                                                      |
| async_tree_none         | 700 ms                                                       | 711 ms: 1.02x slower                                                       |
| genshi_text             | 31.5 ms                                                      | 32.0 ms: 1.02x slower                                                      |
| chaos                   | 107 ms                                                       | 109 ms: 1.02x slower                                                       |
| meteor_contest          | 137 ms                                                       | 139 ms: 1.02x slower                                                       |
| json_dumps              | 14.2 ms                                                      | 14.4 ms: 1.02x slower                                                      |
| sympy_str               | 358 ms                                                       | 364 ms: 1.02x slower                                                       |
| scimark_sparse_mat_mult | 5.19 ms                                                      | 5.28 ms: 1.02x slower                                                      |
| pylint                  | 562 ms                                                       | 572 ms: 1.02x slower                                                       |
| pickle                  | 9.94 us                                                      | 10.1 us: 1.02x slower                                                      |
| xml_etree_process       | 76.0 ms                                                      | 77.5 ms: 1.02x slower                                                      |
| regex_v8                | 26.6 ms                                                      | 27.2 ms: 1.02x slower                                                      |
| deepcopy_memo           | 48.9 us                                                      | 50.0 us: 1.02x slower                                                      |
| xml_etree_iterparse     | 110 ms                                                       | 113 ms: 1.03x slower                                                       |
| deepcopy                | 454 us                                                       | 466 us: 1.03x slower                                                       |
| sympy_sum               | 193 ms                                                       | 199 ms: 1.03x slower                                                       |
| thrift                  | 1.16 ms                                                      | 1.21 ms: 1.04x slower                                                      |
| scimark_lu              | 164 ms                                                       | 170 ms: 1.04x slower                                                       |
| django_template         | 51.5 ms                                                      | 53.6 ms: 1.04x slower                                                      |
| tornado_http            | 152 ms                                                       | 159 ms: 1.05x slower                                                       |
| dask                    | 463 ms                                                       | 484 ms: 1.05x slower                                                       |
| unpickle_list           | 4.49 us                                                      | 4.71 us: 1.05x slower                                                      |
| scimark_fft             | 359 ms                                                       | 383 ms: 1.06x slower                                                       |
| pickle_dict             | 30.0 us                                                      | 32.1 us: 1.07x slower                                                      |
| regex_effbot            | 2.99 ms                                                      | 3.49 ms: 1.17x slower                                                      |
| gc_traversal            | 3.45 ms                                                      | 4.12 ms: 1.19x slower                                                      |
| Geometric mean          | (ref)                                                        | 1.01x slower                                                               |

Benchmark hidden because not significant (27): unpack_sequence, create_gc_cycles, deltablue, hexiom, unpickle_pure_python, html5lib, sqlglot_parse, sqlglot_transpile, pyflate, logging_silent, mako, crypto_pyaes, json_loads, scimark_sor, regex_dna, flaskblogging, nbody, nqueens, pycparser, comprehensions, scimark_monte_carlo, async_tree_cpu_io_mixed, sqlalchemy_declarative, sqlite_synth, go, deepcopy_reduce, bench_mp_pool
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 99.44% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
