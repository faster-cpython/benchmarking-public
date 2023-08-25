
# Results vs. 3.11.0

- fork: python
- ref: f9774e57d84162ff0cba
- machine: linux-x86_64
- commit hash: f9774e5
- commit date: 2023-03-07
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230307-pythonperf2-x86_64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 284 ms: 1.01x faster                                                        |
| chameleon      | 7.67 ms                                                      | 6.94 ms: 1.11x faster                                                       |
| docutils       | 2.86 sec                                                     | 2.79 sec: 1.02x faster                                                      |
| html5lib       | 72.9 ms                                                      | 65.9 ms: 1.11x faster                                                       |
| tornado_http   | 122 ms                                                       | 115 ms: 1.06x faster                                                        |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                |

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230307-pythonperf2-x86_64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 146 ms: 1.08x faster                                                        |
| regex_v8       | 23.9 ms                                                      | 22.8 ms: 1.05x faster                                                       |
| regex_effbot   | 3.50 ms                                                      | 3.36 ms: 1.04x faster                                                       |
| regex_dna      | 227 ms                                                       | 225 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230307-pythonperf2-x86_64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.2 ms: 1.31x faster                                                       |
| unpickle_pure_python | 241 us                                                       | 202 us: 1.19x faster                                                        |
| json_loads           | 28.7 us                                                      | 24.4 us: 1.18x faster                                                       |
| xml_etree_parse      | 158 ms                                                       | 144 ms: 1.10x faster                                                        |
| pickle_pure_python   | 319 us                                                       | 306 us: 1.04x faster                                                        |
| unpickle_list        | 4.53 us                                                      | 4.44 us: 1.02x faster                                                       |
| xml_etree_iterparse  | 104 ms                                                       | 103 ms: 1.01x faster                                                        |
| pickle_list          | 3.83 us                                                      | 3.80 us: 1.01x faster                                                       |
| xml_etree_process    | 56.5 ms                                                      | 57.3 ms: 1.01x slower                                                       |
| pickle_dict          | 30.8 us                                                      | 31.8 us: 1.03x slower                                                       |
| xml_etree_generate   | 80.5 ms                                                      | 83.5 ms: 1.04x slower                                                       |
| pickle               | 9.64 us                                                      | 10.0 us: 1.04x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.05x faster                                                                |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230307-pythonperf2-x86_64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.3 ms: 1.05x slower                                                       |
| python_startup_no_site | 7.76 ms                                                      | 8.34 ms: 1.07x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230307-pythonperf2-x86_64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 58.5 ms                                                      | 53.0 ms: 1.10x faster                                                       |
| mako            | 11.0 ms                                                      | 10.0 ms: 1.09x faster                                                       |
| genshi_text     | 26.1 ms                                                      | 24.6 ms: 1.06x faster                                                       |
| django_template | 40.2 ms                                                      | 39.1 ms: 1.03x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.07x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230307-pythonperf2-x86_64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_tcp             | 753 ms                                                       | 382 ms: 1.97x faster                                                        |
| generators              | 56.0 ms                                                      | 38.4 ms: 1.46x faster                                                       |
| json_dumps              | 13.4 ms                                                      | 10.2 ms: 1.31x faster                                                       |
| deltablue               | 4.00 ms                                                      | 3.33 ms: 1.20x faster                                                       |
| mypy2                   | 451 ms                                                       | 377 ms: 1.20x faster                                                        |
| unpickle_pure_python    | 241 us                                                       | 202 us: 1.19x faster                                                        |
| json_loads              | 28.7 us                                                      | 24.4 us: 1.18x faster                                                       |
| chaos                   | 80.9 ms                                                      | 70.9 ms: 1.14x faster                                                       |
| json                    | 5.65 ms                                                      | 5.00 ms: 1.13x faster                                                       |
| coroutines              | 27.6 ms                                                      | 24.7 ms: 1.12x faster                                                       |
| html5lib                | 72.9 ms                                                      | 65.9 ms: 1.11x faster                                                       |
| chameleon               | 7.67 ms                                                      | 6.94 ms: 1.11x faster                                                       |
| genshi_xml              | 58.5 ms                                                      | 53.0 ms: 1.10x faster                                                       |
| hexiom                  | 7.13 ms                                                      | 6.46 ms: 1.10x faster                                                       |
| deepcopy_memo           | 38.8 us                                                      | 35.4 us: 1.10x faster                                                       |
| xml_etree_parse         | 158 ms                                                       | 144 ms: 1.10x faster                                                        |
| mako                    | 11.0 ms                                                      | 10.0 ms: 1.09x faster                                                       |
| raytrace                | 317 ms                                                       | 290 ms: 1.09x faster                                                        |
| scimark_lu              | 115 ms                                                       | 105 ms: 1.09x faster                                                        |
| go                      | 164 ms                                                       | 151 ms: 1.09x faster                                                        |
| regex_compile           | 158 ms                                                       | 146 ms: 1.08x faster                                                        |
| mdp                     | 2.75 sec                                                     | 2.54 sec: 1.08x faster                                                      |
| dulwich_log             | 68.4 ms                                                      | 63.7 ms: 1.07x faster                                                       |
| pycparser               | 1.32 sec                                                     | 1.23 sec: 1.07x faster                                                      |
| logging_format          | 8.11 us                                                      | 7.59 us: 1.07x faster                                                       |
| logging_silent          | 101 ns                                                       | 94.5 ns: 1.07x faster                                                       |
| genshi_text             | 26.1 ms                                                      | 24.6 ms: 1.06x faster                                                       |
| nqueens                 | 103 ms                                                       | 96.9 ms: 1.06x faster                                                       |
| deepcopy                | 399 us                                                       | 377 us: 1.06x faster                                                        |
| logging_simple          | 7.19 us                                                      | 6.79 us: 1.06x faster                                                       |
| scimark_sor             | 111 ms                                                       | 105 ms: 1.06x faster                                                        |
| tornado_http            | 122 ms                                                       | 115 ms: 1.06x faster                                                        |
| deepcopy_reduce         | 3.51 us                                                      | 3.33 us: 1.05x faster                                                       |
| fannkuch                | 429 ms                                                       | 408 ms: 1.05x faster                                                        |
| regex_v8                | 23.9 ms                                                      | 22.8 ms: 1.05x faster                                                       |
| pprint_pformat          | 1.63 sec                                                     | 1.55 sec: 1.05x faster                                                      |
| sqlglot_normalize       | 126 ms                                                       | 120 ms: 1.05x faster                                                        |
| pickle_pure_python      | 319 us                                                       | 306 us: 1.04x faster                                                        |
| regex_effbot            | 3.50 ms                                                      | 3.36 ms: 1.04x faster                                                       |
| richards                | 48.3 ms                                                      | 46.4 ms: 1.04x faster                                                       |
| pyflate                 | 449 ms                                                       | 432 ms: 1.04x faster                                                        |
| bench_thread_pool       | 1.01 ms                                                      | 974 us: 1.04x faster                                                        |
| sympy_expand            | 555 ms                                                       | 538 ms: 1.03x faster                                                        |
| async_tree_memoization  | 630 ms                                                       | 611 ms: 1.03x faster                                                        |
| coverage                | 84.8 ms                                                      | 82.2 ms: 1.03x faster                                                       |
| sympy_integrate         | 25.8 ms                                                      | 25.0 ms: 1.03x faster                                                       |
| pprint_safe_repr        | 784 ms                                                       | 762 ms: 1.03x faster                                                        |
| django_template         | 40.2 ms                                                      | 39.1 ms: 1.03x faster                                                       |
| sqlglot_optimize        | 59.8 ms                                                      | 58.2 ms: 1.03x faster                                                       |
| unpack_sequence         | 45.6 ns                                                      | 44.4 ns: 1.03x faster                                                       |
| pathlib                 | 19.1 ms                                                      | 18.5 ms: 1.03x faster                                                       |
| sympy_str               | 337 ms                                                       | 328 ms: 1.03x faster                                                        |
| scimark_fft             | 285 ms                                                       | 278 ms: 1.02x faster                                                        |
| crypto_pyaes            | 83.4 ms                                                      | 81.5 ms: 1.02x faster                                                       |
| docutils                | 2.86 sec                                                     | 2.79 sec: 1.02x faster                                                      |
| unpickle_list           | 4.53 us                                                      | 4.44 us: 1.02x faster                                                       |
| async_tree_none         | 519 ms                                                       | 510 ms: 1.02x faster                                                        |
| meteor_contest          | 131 ms                                                       | 128 ms: 1.02x faster                                                        |
| thrift                  | 925 us                                                       | 909 us: 1.02x faster                                                        |
| 2to3                    | 288 ms                                                       | 284 ms: 1.01x faster                                                        |
| regex_dna               | 227 ms                                                       | 225 ms: 1.01x faster                                                        |
| xml_etree_iterparse     | 104 ms                                                       | 103 ms: 1.01x faster                                                        |
| pickle_list             | 3.83 us                                                      | 3.80 us: 1.01x faster                                                       |
| async_tree_cpu_io_mixed | 749 ms                                                       | 745 ms: 1.01x faster                                                        |
| sympy_sum               | 185 ms                                                       | 184 ms: 1.00x faster                                                        |
| telco                   | 6.86 ms                                                      | 6.90 ms: 1.01x slower                                                       |
| sqlglot_transpile       | 1.92 ms                                                      | 1.94 ms: 1.01x slower                                                       |
| xml_etree_process       | 56.5 ms                                                      | 57.3 ms: 1.01x slower                                                       |
| scimark_monte_carlo     | 68.2 ms                                                      | 69.5 ms: 1.02x slower                                                       |
| scimark_sparse_mat_mult | 4.05 ms                                                      | 4.14 ms: 1.02x slower                                                       |
| spectral_norm           | 93.3 ms                                                      | 95.6 ms: 1.02x slower                                                       |
| sqlglot_parse           | 1.53 ms                                                      | 1.58 ms: 1.03x slower                                                       |
| pickle_dict             | 30.8 us                                                      | 31.8 us: 1.03x slower                                                       |
| xml_etree_generate      | 80.5 ms                                                      | 83.5 ms: 1.04x slower                                                       |
| gc_traversal            | 3.85 ms                                                      | 3.99 ms: 1.04x slower                                                       |
| pickle                  | 9.64 us                                                      | 10.0 us: 1.04x slower                                                       |
| bench_mp_pool           | 4.62 ms                                                      | 4.84 ms: 1.05x slower                                                       |
| python_startup          | 10.8 ms                                                      | 11.3 ms: 1.05x slower                                                       |
| sqlite_synth            | 2.50 us                                                      | 2.63 us: 1.05x slower                                                       |
| python_startup_no_site  | 7.76 ms                                                      | 8.34 ms: 1.07x slower                                                       |
| comprehensions          | 24.6 us                                                      | 26.7 us: 1.09x slower                                                       |
| async_generators        | 316 ms                                                       | 385 ms: 1.22x slower                                                        |
| dask                    | 410 ms                                                       | 560 ms: 1.37x slower                                                        |
| Geometric mean          | (ref)                                                        | 1.05x faster                                                                |

Benchmark hidden because not significant (6): async_tree_io, float, pidigits, unpickle, nbody, create_gc_cycles
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x
