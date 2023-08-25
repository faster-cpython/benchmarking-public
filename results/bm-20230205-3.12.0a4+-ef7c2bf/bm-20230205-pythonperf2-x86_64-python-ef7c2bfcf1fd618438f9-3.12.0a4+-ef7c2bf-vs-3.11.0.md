
# Results vs. 3.11.0

- fork: python
- ref: ef7c2bfcf1fd618438f9
- machine: linux-x86_64
- commit hash: ef7c2bf
- commit date: 2023-02-05
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230205-pythonperf2-x86_64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 281 ms: 1.02x faster                                                         |
| chameleon      | 7.67 ms                                                      | 7.63 ms: 1.01x faster                                                        |
| docutils       | 2.86 sec                                                     | 2.75 sec: 1.04x faster                                                       |
| html5lib       | 72.9 ms                                                      | 66.2 ms: 1.10x faster                                                        |
| tornado_http   | 122 ms                                                       | 120 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230205-pythonperf2-x86_64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 74.2 ms                                                      | 71.5 ms: 1.04x faster                                                        |
| nbody          | 90.7 ms                                                      | 89.9 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230205-pythonperf2-x86_64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 145 ms: 1.08x faster                                                         |
| regex_v8       | 23.9 ms                                                      | 22.1 ms: 1.08x faster                                                        |
| regex_effbot   | 3.50 ms                                                      | 3.31 ms: 1.06x faster                                                        |
| regex_dna      | 227 ms                                                       | 222 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230205-pythonperf2-x86_64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.0 ms: 1.33x faster                                                        |
| json_loads           | 28.7 us                                                      | 24.1 us: 1.19x faster                                                        |
| unpickle_pure_python | 241 us                                                       | 208 us: 1.16x faster                                                         |
| xml_etree_parse      | 158 ms                                                       | 143 ms: 1.10x faster                                                         |
| unpickle_list        | 4.53 us                                                      | 4.36 us: 1.04x faster                                                        |
| pickle_pure_python   | 319 us                                                       | 307 us: 1.04x faster                                                         |
| xml_etree_process    | 56.5 ms                                                      | 55.7 ms: 1.01x faster                                                        |
| unpickle             | 13.4 us                                                      | 13.5 us: 1.01x slower                                                        |
| xml_etree_generate   | 80.5 ms                                                      | 81.1 ms: 1.01x slower                                                        |
| xml_etree_iterparse  | 104 ms                                                       | 106 ms: 1.02x slower                                                         |
| pickle_list          | 3.83 us                                                      | 3.95 us: 1.03x slower                                                        |
| pickle               | 9.64 us                                                      | 10.1 us: 1.05x slower                                                        |
| pickle_dict          | 30.8 us                                                      | 32.6 us: 1.06x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.05x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230205-pythonperf2-x86_64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.2 ms: 1.04x slower                                                        |
| python_startup_no_site | 7.76 ms                                                      | 8.26 ms: 1.07x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.05x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230205-pythonperf2-x86_64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 58.5 ms                                                      | 54.1 ms: 1.08x faster                                                        |
| mako            | 11.0 ms                                                      | 10.2 ms: 1.08x faster                                                        |
| django_template | 40.2 ms                                                      | 38.3 ms: 1.05x faster                                                        |
| genshi_text     | 26.1 ms                                                      | 24.9 ms: 1.05x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.06x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230205-pythonperf2-x86_64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| asyncio_tcp             | 753 ms                                                       | 387 ms: 1.95x faster                                                         |
| json_dumps              | 13.4 ms                                                      | 10.0 ms: 1.33x faster                                                        |
| mypy2                   | 451 ms                                                       | 374 ms: 1.21x faster                                                         |
| chaos                   | 80.9 ms                                                      | 67.4 ms: 1.20x faster                                                        |
| json_loads              | 28.7 us                                                      | 24.1 us: 1.19x faster                                                        |
| unpickle_pure_python    | 241 us                                                       | 208 us: 1.16x faster                                                         |
| deltablue               | 4.00 ms                                                      | 3.49 ms: 1.14x faster                                                        |
| comprehensions          | 24.6 us                                                      | 21.5 us: 1.14x faster                                                        |
| scimark_sparse_mat_mult | 4.05 ms                                                      | 3.59 ms: 1.13x faster                                                        |
| scimark_lu              | 115 ms                                                       | 102 ms: 1.12x faster                                                         |
| json                    | 5.65 ms                                                      | 5.07 ms: 1.11x faster                                                        |
| hexiom                  | 7.13 ms                                                      | 6.43 ms: 1.11x faster                                                        |
| xml_etree_parse         | 158 ms                                                       | 143 ms: 1.10x faster                                                         |
| html5lib                | 72.9 ms                                                      | 66.2 ms: 1.10x faster                                                        |
| pycparser               | 1.32 sec                                                     | 1.21 sec: 1.09x faster                                                       |
| raytrace                | 317 ms                                                       | 291 ms: 1.09x faster                                                         |
| regex_compile           | 158 ms                                                       | 145 ms: 1.08x faster                                                         |
| sympy_str               | 337 ms                                                       | 311 ms: 1.08x faster                                                         |
| regex_v8                | 23.9 ms                                                      | 22.1 ms: 1.08x faster                                                        |
| genshi_xml              | 58.5 ms                                                      | 54.1 ms: 1.08x faster                                                        |
| mako                    | 11.0 ms                                                      | 10.2 ms: 1.08x faster                                                        |
| sympy_sum               | 185 ms                                                       | 172 ms: 1.07x faster                                                         |
| deepcopy_reduce         | 3.51 us                                                      | 3.28 us: 1.07x faster                                                        |
| logging_format          | 8.11 us                                                      | 7.64 us: 1.06x faster                                                        |
| sympy_integrate         | 25.8 ms                                                      | 24.3 ms: 1.06x faster                                                        |
| fannkuch                | 429 ms                                                       | 404 ms: 1.06x faster                                                         |
| go                      | 164 ms                                                       | 155 ms: 1.06x faster                                                         |
| regex_effbot            | 3.50 ms                                                      | 3.31 ms: 1.06x faster                                                        |
| unpack_sequence         | 45.6 ns                                                      | 43.2 ns: 1.06x faster                                                        |
| sqlglot_normalize       | 126 ms                                                       | 119 ms: 1.06x faster                                                         |
| bench_thread_pool       | 1.01 ms                                                      | 959 us: 1.05x faster                                                         |
| deepcopy_memo           | 38.8 us                                                      | 36.8 us: 1.05x faster                                                        |
| deepcopy                | 399 us                                                       | 380 us: 1.05x faster                                                         |
| logging_silent          | 101 ns                                                       | 95.9 ns: 1.05x faster                                                        |
| django_template         | 40.2 ms                                                      | 38.3 ms: 1.05x faster                                                        |
| scimark_fft             | 285 ms                                                       | 271 ms: 1.05x faster                                                         |
| sympy_expand            | 555 ms                                                       | 528 ms: 1.05x faster                                                         |
| genshi_text             | 26.1 ms                                                      | 24.9 ms: 1.05x faster                                                        |
| dulwich_log             | 68.4 ms                                                      | 65.6 ms: 1.04x faster                                                        |
| crypto_pyaes            | 83.4 ms                                                      | 80.0 ms: 1.04x faster                                                        |
| pyflate                 | 449 ms                                                       | 431 ms: 1.04x faster                                                         |
| unpickle_list           | 4.53 us                                                      | 4.36 us: 1.04x faster                                                        |
| telco                   | 6.86 ms                                                      | 6.61 ms: 1.04x faster                                                        |
| logging_simple          | 7.19 us                                                      | 6.93 us: 1.04x faster                                                        |
| scimark_sor             | 111 ms                                                       | 107 ms: 1.04x faster                                                         |
| richards                | 48.3 ms                                                      | 46.5 ms: 1.04x faster                                                        |
| float                   | 74.2 ms                                                      | 71.5 ms: 1.04x faster                                                        |
| pickle_pure_python      | 319 us                                                       | 307 us: 1.04x faster                                                         |
| docutils                | 2.86 sec                                                     | 2.75 sec: 1.04x faster                                                       |
| thrift                  | 925 us                                                       | 892 us: 1.04x faster                                                         |
| async_tree_memoization  | 630 ms                                                       | 608 ms: 1.04x faster                                                         |
| sqlglot_optimize        | 59.8 ms                                                      | 57.8 ms: 1.04x faster                                                        |
| pprint_pformat          | 1.63 sec                                                     | 1.58 sec: 1.03x faster                                                       |
| coverage                | 84.8 ms                                                      | 82.2 ms: 1.03x faster                                                        |
| nqueens                 | 103 ms                                                       | 100 ms: 1.03x faster                                                         |
| regex_dna               | 227 ms                                                       | 222 ms: 1.02x faster                                                         |
| gc_traversal            | 3.85 ms                                                      | 3.76 ms: 1.02x faster                                                        |
| meteor_contest          | 131 ms                                                       | 128 ms: 1.02x faster                                                         |
| async_tree_none         | 519 ms                                                       | 508 ms: 1.02x faster                                                         |
| pprint_safe_repr        | 784 ms                                                       | 767 ms: 1.02x faster                                                         |
| 2to3                    | 288 ms                                                       | 281 ms: 1.02x faster                                                         |
| scimark_monte_carlo     | 68.2 ms                                                      | 66.9 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed | 749 ms                                                       | 739 ms: 1.01x faster                                                         |
| xml_etree_process       | 56.5 ms                                                      | 55.7 ms: 1.01x faster                                                        |
| tornado_http            | 122 ms                                                       | 120 ms: 1.01x faster                                                         |
| pathlib                 | 19.1 ms                                                      | 18.9 ms: 1.01x faster                                                        |
| nbody                   | 90.7 ms                                                      | 89.9 ms: 1.01x faster                                                        |
| mdp                     | 2.75 sec                                                     | 2.72 sec: 1.01x faster                                                       |
| chameleon               | 7.67 ms                                                      | 7.63 ms: 1.01x faster                                                        |
| unpickle                | 13.4 us                                                      | 13.5 us: 1.01x slower                                                        |
| xml_etree_generate      | 80.5 ms                                                      | 81.1 ms: 1.01x slower                                                        |
| sqlglot_transpile       | 1.92 ms                                                      | 1.95 ms: 1.02x slower                                                        |
| xml_etree_iterparse     | 104 ms                                                       | 106 ms: 1.02x slower                                                         |
| async_generators        | 316 ms                                                       | 322 ms: 1.02x slower                                                         |
| spectral_norm           | 93.3 ms                                                      | 95.3 ms: 1.02x slower                                                        |
| sqlite_synth            | 2.50 us                                                      | 2.56 us: 1.02x slower                                                        |
| sqlglot_parse           | 1.53 ms                                                      | 1.58 ms: 1.03x slower                                                        |
| pickle_list             | 3.83 us                                                      | 3.95 us: 1.03x slower                                                        |
| bench_mp_pool           | 4.62 ms                                                      | 4.80 ms: 1.04x slower                                                        |
| python_startup          | 10.8 ms                                                      | 11.2 ms: 1.04x slower                                                        |
| pickle                  | 9.64 us                                                      | 10.1 us: 1.05x slower                                                        |
| pickle_dict             | 30.8 us                                                      | 32.6 us: 1.06x slower                                                        |
| coroutines              | 27.6 ms                                                      | 29.2 ms: 1.06x slower                                                        |
| python_startup_no_site  | 7.76 ms                                                      | 8.26 ms: 1.07x slower                                                        |
| generators              | 56.0 ms                                                      | 60.8 ms: 1.08x slower                                                        |
| dask                    | 410 ms                                                       | 568 ms: 1.39x slower                                                         |
| Geometric mean          | (ref)                                                        | 1.05x faster                                                                 |

Benchmark hidden because not significant (3): create_gc_cycles, async_tree_io, pidigits
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x
