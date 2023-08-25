
# Results vs. 3.10.4

- fork: python
- ref: 7d4cc5aa854fdea4d01a
- machine: linux-x86_64
- commit hash: 7d4cc5a
- commit date: 2023-04-04
- overall geometric mean: 1.00x slower \*
- HPT reliability: 74.20%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-pythonperf2-x86_64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| chameleon      | 9.72 ms                                                      | 9.41 ms: 1.03x faster                                                      |
| docutils       | 3.40 sec                                                     | 3.42 sec: 1.01x slower                                                     |
| Geometric mean | (ref)                                                        | 1.01x faster                                                               |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-pythonperf2-x86_64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 271 ms                                                       | 271 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x slower                                                               |

Benchmark hidden because not significant (2): nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-pythonperf2-x86_64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 191 ms: 1.01x faster                                                       |
| regex_dna      | 259 ms                                                       | 259 ms: 1.00x faster                                                       |
| regex_v8       | 26.6 ms                                                      | 27.1 ms: 1.02x slower                                                      |
| regex_effbot   | 2.99 ms                                                      | 3.25 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                        | 1.02x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-pythonperf2-x86_64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 313 us: 1.02x faster                                                       |
| xml_etree_generate   | 94.6 ms                                                      | 92.8 ms: 1.02x faster                                                      |
| pickle_list          | 4.11 us                                                      | 4.04 us: 1.02x faster                                                      |
| xml_etree_iterparse  | 110 ms                                                       | 109 ms: 1.01x faster                                                       |
| xml_etree_parse      | 162 ms                                                       | 160 ms: 1.01x faster                                                       |
| unpickle             | 14.2 us                                                      | 14.1 us: 1.01x faster                                                      |
| pickle_pure_python   | 457 us                                                       | 454 us: 1.01x faster                                                       |
| xml_etree_process    | 76.0 ms                                                      | 76.5 ms: 1.01x slower                                                      |
| json_loads           | 30.0 us                                                      | 30.2 us: 1.01x slower                                                      |
| json_dumps           | 14.2 ms                                                      | 14.4 ms: 1.02x slower                                                      |
| pickle               | 9.94 us                                                      | 10.1 us: 1.02x slower                                                      |
| unpickle_list        | 4.49 us                                                      | 4.61 us: 1.03x slower                                                      |
| pickle_dict          | 30.0 us                                                      | 31.1 us: 1.04x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-pythonperf2-x86_64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 7.32 ms                                                      | 7.35 ms: 1.00x slower                                                      |
| python_startup         | 11.5 ms                                                      | 11.5 ms: 1.01x slower                                                      |
| Geometric mean         | (ref)                                                        | 1.00x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-pythonperf2-x86_64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 64.7 ms                                                      | 63.7 ms: 1.02x faster                                                      |
| genshi_text     | 31.5 ms                                                      | 31.7 ms: 1.01x slower                                                      |
| mako            | 14.7 ms                                                      | 14.9 ms: 1.02x slower                                                      |
| django_template | 51.5 ms                                                      | 53.2 ms: 1.03x slower                                                      |
| Geometric mean  | (ref)                                                        | 1.01x slower                                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-pythonperf2-x86_64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|-------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| aiohttp                 | 1.21 ms                                                      | 1.15 ms: 1.05x faster                                                      |
| gunicorn                | 1.17 ms                                                      | 1.13 ms: 1.04x faster                                                      |
| fannkuch                | 496 ms                                                       | 477 ms: 1.04x faster                                                       |
| pycparser               | 1.66 sec                                                     | 1.61 sec: 1.03x faster                                                     |
| chameleon               | 9.72 ms                                                      | 9.41 ms: 1.03x faster                                                      |
| pathlib                 | 21.7 ms                                                      | 21.0 ms: 1.03x faster                                                      |
| crypto_pyaes            | 118 ms                                                       | 115 ms: 1.03x faster                                                       |
| bench_thread_pool       | 1.14 ms                                                      | 1.10 ms: 1.03x faster                                                      |
| unpickle_pure_python    | 321 us                                                       | 313 us: 1.02x faster                                                       |
| xml_etree_generate      | 94.6 ms                                                      | 92.8 ms: 1.02x faster                                                      |
| chaos                   | 107 ms                                                       | 105 ms: 1.02x faster                                                       |
| pickle_list             | 4.11 us                                                      | 4.04 us: 1.02x faster                                                      |
| sqlglot_optimize        | 70.3 ms                                                      | 69.1 ms: 1.02x faster                                                      |
| genshi_xml              | 64.7 ms                                                      | 63.7 ms: 1.02x faster                                                      |
| scimark_lu              | 164 ms                                                       | 161 ms: 1.01x faster                                                       |
| pprint_safe_repr        | 1.05 sec                                                     | 1.03 sec: 1.01x faster                                                     |
| flaskblogging           | 4.39 ms                                                      | 4.33 ms: 1.01x faster                                                      |
| regex_compile           | 194 ms                                                       | 191 ms: 1.01x faster                                                       |
| xml_etree_iterparse     | 110 ms                                                       | 109 ms: 1.01x faster                                                       |
| xml_etree_parse         | 162 ms                                                       | 160 ms: 1.01x faster                                                       |
| deepcopy_reduce         | 4.03 us                                                      | 3.99 us: 1.01x faster                                                      |
| async_generators        | 422 ms                                                       | 418 ms: 1.01x faster                                                       |
| hexiom                  | 9.52 ms                                                      | 9.43 ms: 1.01x faster                                                      |
| dask                    | 463 ms                                                       | 459 ms: 1.01x faster                                                       |
| unpickle                | 14.2 us                                                      | 14.1 us: 1.01x faster                                                      |
| coroutines              | 30.4 ms                                                      | 30.2 ms: 1.01x faster                                                      |
| sqlglot_transpile       | 2.71 ms                                                      | 2.69 ms: 1.01x faster                                                      |
| coverage                | 64.0 ms                                                      | 63.5 ms: 1.01x faster                                                      |
| pickle_pure_python      | 457 us                                                       | 454 us: 1.01x faster                                                       |
| pyflate                 | 697 ms                                                       | 693 ms: 1.01x faster                                                       |
| pprint_pformat          | 2.15 sec                                                     | 2.14 sec: 1.00x faster                                                     |
| regex_dna               | 259 ms                                                       | 259 ms: 1.00x faster                                                       |
| pidigits                | 271 ms                                                       | 271 ms: 1.00x slower                                                       |
| spectral_norm           | 136 ms                                                       | 137 ms: 1.00x slower                                                       |
| python_startup_no_site  | 7.32 ms                                                      | 7.35 ms: 1.00x slower                                                      |
| scimark_sparse_mat_mult | 5.19 ms                                                      | 5.22 ms: 1.00x slower                                                      |
| python_startup          | 11.5 ms                                                      | 11.5 ms: 1.01x slower                                                      |
| comprehensions          | 26.9 us                                                      | 27.1 us: 1.01x slower                                                      |
| raytrace                | 488 ms                                                       | 491 ms: 1.01x slower                                                       |
| xml_etree_process       | 76.0 ms                                                      | 76.5 ms: 1.01x slower                                                      |
| docutils                | 3.40 sec                                                     | 3.42 sec: 1.01x slower                                                     |
| json_loads              | 30.0 us                                                      | 30.2 us: 1.01x slower                                                      |
| genshi_text             | 31.5 ms                                                      | 31.7 ms: 1.01x slower                                                      |
| mypy2                   | 466 ms                                                       | 470 ms: 1.01x slower                                                       |
| sqlalchemy_declarative  | 187 ms                                                       | 188 ms: 1.01x slower                                                       |
| scimark_monte_carlo     | 109 ms                                                       | 110 ms: 1.01x slower                                                       |
| meteor_contest          | 137 ms                                                       | 139 ms: 1.01x slower                                                       |
| sympy_integrate         | 28.1 ms                                                      | 28.4 ms: 1.01x slower                                                      |
| mako                    | 14.7 ms                                                      | 14.9 ms: 1.02x slower                                                      |
| sqlalchemy_imperative   | 22.6 ms                                                      | 23.0 ms: 1.02x slower                                                      |
| regex_v8                | 26.6 ms                                                      | 27.1 ms: 1.02x slower                                                      |
| json_dumps              | 14.2 ms                                                      | 14.4 ms: 1.02x slower                                                      |
| pylint                  | 562 ms                                                       | 572 ms: 1.02x slower                                                       |
| pickle                  | 9.94 us                                                      | 10.1 us: 1.02x slower                                                      |
| go                      | 259 ms                                                       | 264 ms: 1.02x slower                                                       |
| deepcopy                | 454 us                                                       | 465 us: 1.02x slower                                                       |
| sympy_str               | 358 ms                                                       | 366 ms: 1.02x slower                                                       |
| unpickle_list           | 4.49 us                                                      | 4.61 us: 1.03x slower                                                      |
| sympy_expand            | 599 ms                                                       | 615 ms: 1.03x slower                                                       |
| mdp                     | 3.03 sec                                                     | 3.12 sec: 1.03x slower                                                     |
| sympy_sum               | 193 ms                                                       | 199 ms: 1.03x slower                                                       |
| django_template         | 51.5 ms                                                      | 53.2 ms: 1.03x slower                                                      |
| pickle_dict             | 30.0 us                                                      | 31.1 us: 1.04x slower                                                      |
| deepcopy_memo           | 48.9 us                                                      | 51.1 us: 1.05x slower                                                      |
| gc_traversal            | 3.45 ms                                                      | 3.68 ms: 1.07x slower                                                      |
| regex_effbot            | 2.99 ms                                                      | 3.25 ms: 1.08x slower                                                      |
| Geometric mean          | (ref)                                                        | 1.00x slower                                                               |

Benchmark hidden because not significant (29): bench_mp_pool, tornado_http, html5lib, async_tree_none, deltablue, scimark_sor, generators, nbody, asyncio_tcp, unpack_sequence, float, logging_silent, sqlglot_parse, nqueens, 2to3, async_tree_io, sqlite_synth, create_gc_cycles, logging_format, sqlglot_normalize, async_tree_cpu_io_mixed, scimark_fft, json, dulwich_log, thrift, telco, async_tree_memoization, logging_simple, richards
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 74.20% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
