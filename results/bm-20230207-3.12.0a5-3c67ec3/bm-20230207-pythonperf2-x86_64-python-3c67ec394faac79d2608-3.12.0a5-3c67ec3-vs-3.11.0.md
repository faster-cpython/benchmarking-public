
# Results vs. 3.11.0

- fork: python
- ref: 3c67ec394faac79d2608
- machine: linux-x86_64
- commit hash: 3c67ec3
- commit date: 2023-02-07
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-pythonperf2-x86_64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 282 ms: 1.02x faster                                                        |
| chameleon      | 7.67 ms                                                      | 7.46 ms: 1.03x faster                                                       |
| docutils       | 2.86 sec                                                     | 2.78 sec: 1.03x faster                                                      |
| html5lib       | 72.9 ms                                                      | 65.3 ms: 1.12x faster                                                       |
| tornado_http   | 122 ms                                                       | 117 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-pythonperf2-x86_64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 74.2 ms                                                      | 71.9 ms: 1.03x faster                                                       |
| nbody          | 90.7 ms                                                      | 101 ms: 1.12x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-pythonperf2-x86_64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 145 ms: 1.09x faster                                                        |
| regex_v8       | 23.9 ms                                                      | 22.7 ms: 1.05x faster                                                       |
| regex_dna      | 227 ms                                                       | 240 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-pythonperf2-x86_64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.0 ms: 1.34x faster                                                       |
| json_loads           | 28.7 us                                                      | 23.8 us: 1.20x faster                                                       |
| unpickle_pure_python | 241 us                                                       | 204 us: 1.18x faster                                                        |
| xml_etree_parse      | 158 ms                                                       | 142 ms: 1.11x faster                                                        |
| unpickle             | 13.4 us                                                      | 12.8 us: 1.05x faster                                                       |
| pickle_pure_python   | 319 us                                                       | 312 us: 1.02x faster                                                        |
| xml_etree_iterparse  | 104 ms                                                       | 103 ms: 1.02x faster                                                        |
| xml_etree_process    | 56.5 ms                                                      | 55.6 ms: 1.01x faster                                                       |
| unpickle_list        | 4.53 us                                                      | 4.50 us: 1.01x faster                                                       |
| pickle               | 9.64 us                                                      | 9.88 us: 1.03x slower                                                       |
| pickle_dict          | 30.8 us                                                      | 31.6 us: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.06x faster                                                                |

Benchmark hidden because not significant (2): xml_etree_generate, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-pythonperf2-x86_64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.2 ms: 1.04x slower                                                       |
| python_startup_no_site | 7.76 ms                                                      | 8.25 ms: 1.06x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.05x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-pythonperf2-x86_64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml     | 58.5 ms                                                      | 53.4 ms: 1.10x faster                                                       |
| mako           | 11.0 ms                                                      | 10.3 ms: 1.07x faster                                                       |
| genshi_text    | 26.1 ms                                                      | 24.6 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-pythonperf2-x86_64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_tcp             | 753 ms                                                       | 388 ms: 1.94x faster                                                        |
| json_dumps              | 13.4 ms                                                      | 10.0 ms: 1.34x faster                                                       |
| json_loads              | 28.7 us                                                      | 23.8 us: 1.20x faster                                                       |
| mypy2                   | 451 ms                                                       | 379 ms: 1.19x faster                                                        |
| unpickle_pure_python    | 241 us                                                       | 204 us: 1.18x faster                                                        |
| chaos                   | 80.9 ms                                                      | 69.6 ms: 1.16x faster                                                       |
| comprehensions          | 24.6 us                                                      | 21.3 us: 1.15x faster                                                       |
| json                    | 5.65 ms                                                      | 4.94 ms: 1.14x faster                                                       |
| scimark_sparse_mat_mult | 4.05 ms                                                      | 3.61 ms: 1.12x faster                                                       |
| html5lib                | 72.9 ms                                                      | 65.3 ms: 1.12x faster                                                       |
| deltablue               | 4.00 ms                                                      | 3.60 ms: 1.11x faster                                                       |
| xml_etree_parse         | 158 ms                                                       | 142 ms: 1.11x faster                                                        |
| scimark_lu              | 115 ms                                                       | 104 ms: 1.10x faster                                                        |
| hexiom                  | 7.13 ms                                                      | 6.49 ms: 1.10x faster                                                       |
| genshi_xml              | 58.5 ms                                                      | 53.4 ms: 1.10x faster                                                       |
| logging_format          | 8.11 us                                                      | 7.43 us: 1.09x faster                                                       |
| nqueens                 | 103 ms                                                       | 94.2 ms: 1.09x faster                                                       |
| regex_compile           | 158 ms                                                       | 145 ms: 1.09x faster                                                        |
| gc_traversal            | 3.85 ms                                                      | 3.55 ms: 1.08x faster                                                       |
| deepcopy_memo           | 38.8 us                                                      | 35.8 us: 1.08x faster                                                       |
| logging_simple          | 7.19 us                                                      | 6.67 us: 1.08x faster                                                       |
| go                      | 164 ms                                                       | 152 ms: 1.08x faster                                                        |
| sympy_str               | 337 ms                                                       | 313 ms: 1.08x faster                                                        |
| sympy_sum               | 185 ms                                                       | 172 ms: 1.07x faster                                                        |
| mako                    | 11.0 ms                                                      | 10.3 ms: 1.07x faster                                                       |
| pprint_pformat          | 1.63 sec                                                     | 1.53 sec: 1.06x faster                                                      |
| deepcopy_reduce         | 3.51 us                                                      | 3.30 us: 1.06x faster                                                       |
| genshi_text             | 26.1 ms                                                      | 24.6 ms: 1.06x faster                                                       |
| sympy_integrate         | 25.8 ms                                                      | 24.3 ms: 1.06x faster                                                       |
| scimark_sor             | 111 ms                                                       | 105 ms: 1.06x faster                                                        |
| unpack_sequence         | 45.6 ns                                                      | 43.3 ns: 1.05x faster                                                       |
| sympy_expand            | 555 ms                                                       | 526 ms: 1.05x faster                                                        |
| pprint_safe_repr        | 784 ms                                                       | 744 ms: 1.05x faster                                                        |
| regex_v8                | 23.9 ms                                                      | 22.7 ms: 1.05x faster                                                       |
| raytrace                | 317 ms                                                       | 301 ms: 1.05x faster                                                        |
| fannkuch                | 429 ms                                                       | 409 ms: 1.05x faster                                                        |
| unpickle                | 13.4 us                                                      | 12.8 us: 1.05x faster                                                       |
| async_tree_memoization  | 630 ms                                                       | 601 ms: 1.05x faster                                                        |
| pyflate                 | 449 ms                                                       | 428 ms: 1.05x faster                                                        |
| sqlglot_normalize       | 126 ms                                                       | 120 ms: 1.05x faster                                                        |
| richards                | 48.3 ms                                                      | 46.1 ms: 1.05x faster                                                       |
| logging_silent          | 101 ns                                                       | 96.5 ns: 1.04x faster                                                       |
| deepcopy                | 399 us                                                       | 383 us: 1.04x faster                                                        |
| tornado_http            | 122 ms                                                       | 117 ms: 1.04x faster                                                        |
| telco                   | 6.86 ms                                                      | 6.59 ms: 1.04x faster                                                       |
| bench_thread_pool       | 1.01 ms                                                      | 971 us: 1.04x faster                                                        |
| pycparser               | 1.32 sec                                                     | 1.28 sec: 1.04x faster                                                      |
| sqlglot_optimize        | 59.8 ms                                                      | 57.7 ms: 1.04x faster                                                       |
| async_tree_none         | 519 ms                                                       | 503 ms: 1.03x faster                                                        |
| float                   | 74.2 ms                                                      | 71.9 ms: 1.03x faster                                                       |
| mdp                     | 2.75 sec                                                     | 2.66 sec: 1.03x faster                                                      |
| chameleon               | 7.67 ms                                                      | 7.46 ms: 1.03x faster                                                       |
| dulwich_log             | 68.4 ms                                                      | 66.6 ms: 1.03x faster                                                       |
| docutils                | 2.86 sec                                                     | 2.78 sec: 1.03x faster                                                      |
| scimark_fft             | 285 ms                                                       | 278 ms: 1.02x faster                                                        |
| pickle_pure_python      | 319 us                                                       | 312 us: 1.02x faster                                                        |
| 2to3                    | 288 ms                                                       | 282 ms: 1.02x faster                                                        |
| crypto_pyaes            | 83.4 ms                                                      | 81.8 ms: 1.02x faster                                                       |
| meteor_contest          | 131 ms                                                       | 128 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed | 749 ms                                                       | 737 ms: 1.02x faster                                                        |
| xml_etree_iterparse     | 104 ms                                                       | 103 ms: 1.02x faster                                                        |
| xml_etree_process       | 56.5 ms                                                      | 55.6 ms: 1.01x faster                                                       |
| unpickle_list           | 4.53 us                                                      | 4.50 us: 1.01x faster                                                       |
| async_tree_io           | 1.17 sec                                                     | 1.17 sec: 1.01x faster                                                      |
| pathlib                 | 19.1 ms                                                      | 19.1 ms: 1.00x slower                                                       |
| thrift                  | 925 us                                                       | 935 us: 1.01x slower                                                        |
| coverage                | 84.8 ms                                                      | 86.0 ms: 1.01x slower                                                       |
| sqlglot_parse           | 1.53 ms                                                      | 1.56 ms: 1.02x slower                                                       |
| create_gc_cycles        | 1.61 ms                                                      | 1.64 ms: 1.02x slower                                                       |
| spectral_norm           | 93.3 ms                                                      | 95.4 ms: 1.02x slower                                                       |
| pickle                  | 9.64 us                                                      | 9.88 us: 1.03x slower                                                       |
| pickle_dict             | 30.8 us                                                      | 31.6 us: 1.03x slower                                                       |
| scimark_monte_carlo     | 68.2 ms                                                      | 70.2 ms: 1.03x slower                                                       |
| async_generators        | 316 ms                                                       | 325 ms: 1.03x slower                                                        |
| sqlite_synth            | 2.50 us                                                      | 2.58 us: 1.03x slower                                                       |
| python_startup          | 10.8 ms                                                      | 11.2 ms: 1.04x slower                                                       |
| coroutines              | 27.6 ms                                                      | 29.1 ms: 1.05x slower                                                       |
| regex_dna               | 227 ms                                                       | 240 ms: 1.06x slower                                                        |
| python_startup_no_site  | 7.76 ms                                                      | 8.25 ms: 1.06x slower                                                       |
| generators              | 56.0 ms                                                      | 60.4 ms: 1.08x slower                                                       |
| nbody                   | 90.7 ms                                                      | 101 ms: 1.12x slower                                                        |
| dask                    | 410 ms                                                       | 562 ms: 1.37x slower                                                        |
| Geometric mean          | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (7): pidigits, regex_effbot, xml_etree_generate, pickle_list, sqlglot_transpile, django_template, bench_mp_pool
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x
