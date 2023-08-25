
# Results vs. 3.11.0

- fork: python
- ref: ea2c0016502472aa8baa
- machine: linux-x86_64
- commit hash: ea2c001
- commit date: 2023-04-22
- overall geometric mean: 1.04x faster \*
- HPT reliability: 99.96%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230422-pythonperf2-x86_64-python-ea2c0016502472aa8baa-3.12.0a7+-ea2c001 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 284 ms: 1.01x faster                                                         |
| chameleon      | 7.67 ms                                                      | 7.44 ms: 1.03x faster                                                        |
| docutils       | 2.86 sec                                                     | 2.89 sec: 1.01x slower                                                       |
| html5lib       | 72.9 ms                                                      | 68.9 ms: 1.06x faster                                                        |
| tornado_http   | 122 ms                                                       | 119 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230422-pythonperf2-x86_64-python-ea2c0016502472aa8baa-3.12.0a7+-ea2c001 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 83.7 ms: 1.08x faster                                                        |
| pidigits       | 251 ms                                                       | 260 ms: 1.03x slower                                                         |
| float          | 74.2 ms                                                      | 77.1 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230422-pythonperf2-x86_64-python-ea2c0016502472aa8baa-3.12.0a7+-ea2c001 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 143 ms: 1.11x faster                                                         |
| regex_effbot   | 3.50 ms                                                      | 3.40 ms: 1.03x faster                                                        |
| regex_v8       | 23.9 ms                                                      | 23.6 ms: 1.01x faster                                                        |
| regex_dna      | 227 ms                                                       | 230 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230422-pythonperf2-x86_64-python-ea2c0016502472aa8baa-3.12.0a7+-ea2c001 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.3 ms: 1.30x faster                                                        |
| json_loads           | 28.7 us                                                      | 24.7 us: 1.16x faster                                                        |
| unpickle_pure_python | 241 us                                                       | 209 us: 1.15x faster                                                         |
| xml_etree_parse      | 158 ms                                                       | 151 ms: 1.05x faster                                                         |
| pickle_dict          | 30.8 us                                                      | 30.7 us: 1.00x faster                                                        |
| xml_etree_iterparse  | 104 ms                                                       | 105 ms: 1.01x slower                                                         |
| pickle               | 9.64 us                                                      | 9.91 us: 1.03x slower                                                        |
| pickle_list          | 3.83 us                                                      | 3.95 us: 1.03x slower                                                        |
| xml_etree_process    | 56.5 ms                                                      | 58.5 ms: 1.04x slower                                                        |
| unpickle             | 13.4 us                                                      | 14.2 us: 1.06x slower                                                        |
| xml_etree_generate   | 80.5 ms                                                      | 85.2 ms: 1.06x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.03x faster                                                                 |

Benchmark hidden because not significant (2): pickle_pure_python, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230422-pythonperf2-x86_64-python-ea2c0016502472aa8baa-3.12.0a7+-ea2c001 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.1 ms: 1.04x slower                                                        |
| python_startup_no_site | 7.76 ms                                                      | 8.37 ms: 1.08x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230422-pythonperf2-x86_64-python-ea2c0016502472aa8baa-3.12.0a7+-ea2c001 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.0 ms                                                      | 10.0 ms: 1.10x faster                                                        |
| genshi_xml      | 58.5 ms                                                      | 53.9 ms: 1.09x faster                                                        |
| django_template | 40.2 ms                                                      | 38.3 ms: 1.05x faster                                                        |
| genshi_text     | 26.1 ms                                                      | 25.0 ms: 1.05x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.07x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230422-pythonperf2-x86_64-python-ea2c0016502472aa8baa-3.12.0a7+-ea2c001 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| asyncio_tcp             | 753 ms                                                       | 379 ms: 1.99x faster                                                         |
| generators              | 56.0 ms                                                      | 36.6 ms: 1.53x faster                                                        |
| json_dumps              | 13.4 ms                                                      | 10.3 ms: 1.30x faster                                                        |
| fannkuch                | 429 ms                                                       | 351 ms: 1.22x faster                                                         |
| chaos                   | 80.9 ms                                                      | 66.3 ms: 1.22x faster                                                        |
| coroutines              | 27.6 ms                                                      | 22.7 ms: 1.21x faster                                                        |
| deltablue               | 4.00 ms                                                      | 3.30 ms: 1.21x faster                                                        |
| hexiom                  | 7.13 ms                                                      | 5.92 ms: 1.21x faster                                                        |
| scimark_lu              | 115 ms                                                       | 95.5 ms: 1.20x faster                                                        |
| mypy2                   | 451 ms                                                       | 388 ms: 1.16x faster                                                         |
| json_loads              | 28.7 us                                                      | 24.7 us: 1.16x faster                                                        |
| unpickle_pure_python    | 241 us                                                       | 209 us: 1.15x faster                                                         |
| nqueens                 | 103 ms                                                       | 90.1 ms: 1.14x faster                                                        |
| go                      | 164 ms                                                       | 146 ms: 1.12x faster                                                         |
| sqlglot_parse           | 1.53 ms                                                      | 1.38 ms: 1.11x faster                                                        |
| logging_format          | 8.11 us                                                      | 7.32 us: 1.11x faster                                                        |
| regex_compile           | 158 ms                                                       | 143 ms: 1.11x faster                                                         |
| json                    | 5.65 ms                                                      | 5.13 ms: 1.10x faster                                                        |
| richards                | 48.3 ms                                                      | 43.9 ms: 1.10x faster                                                        |
| mako                    | 11.0 ms                                                      | 10.0 ms: 1.10x faster                                                        |
| logging_simple          | 7.19 us                                                      | 6.60 us: 1.09x faster                                                        |
| genshi_xml              | 58.5 ms                                                      | 53.9 ms: 1.09x faster                                                        |
| spectral_norm           | 93.3 ms                                                      | 86.0 ms: 1.09x faster                                                        |
| nbody                   | 90.7 ms                                                      | 83.7 ms: 1.08x faster                                                        |
| mdp                     | 2.75 sec                                                     | 2.54 sec: 1.08x faster                                                       |
| logging_silent          | 101 ns                                                       | 93.5 ns: 1.08x faster                                                        |
| sqlglot_transpile       | 1.92 ms                                                      | 1.78 ms: 1.08x faster                                                        |
| async_tree_memoization  | 630 ms                                                       | 594 ms: 1.06x faster                                                         |
| html5lib                | 72.9 ms                                                      | 68.9 ms: 1.06x faster                                                        |
| raytrace                | 317 ms                                                       | 299 ms: 1.06x faster                                                         |
| crypto_pyaes            | 83.4 ms                                                      | 79.0 ms: 1.06x faster                                                        |
| dulwich_log             | 68.4 ms                                                      | 65.0 ms: 1.05x faster                                                        |
| pycparser               | 1.32 sec                                                     | 1.26 sec: 1.05x faster                                                       |
| django_template         | 40.2 ms                                                      | 38.3 ms: 1.05x faster                                                        |
| sympy_expand            | 555 ms                                                       | 529 ms: 1.05x faster                                                         |
| bench_thread_pool       | 1.01 ms                                                      | 966 us: 1.05x faster                                                         |
| xml_etree_parse         | 158 ms                                                       | 151 ms: 1.05x faster                                                         |
| genshi_text             | 26.1 ms                                                      | 25.0 ms: 1.05x faster                                                        |
| sqlglot_normalize       | 126 ms                                                       | 121 ms: 1.05x faster                                                         |
| thrift                  | 925 us                                                       | 887 us: 1.04x faster                                                         |
| deepcopy                | 399 us                                                       | 383 us: 1.04x faster                                                         |
| sympy_str               | 337 ms                                                       | 325 ms: 1.04x faster                                                         |
| pylint                  | 515 ms                                                       | 498 ms: 1.04x faster                                                         |
| deepcopy_memo           | 38.8 us                                                      | 37.5 us: 1.03x faster                                                        |
| chameleon               | 7.67 ms                                                      | 7.44 ms: 1.03x faster                                                        |
| async_tree_none         | 519 ms                                                       | 505 ms: 1.03x faster                                                         |
| regex_effbot            | 3.50 ms                                                      | 3.40 ms: 1.03x faster                                                        |
| pathlib                 | 19.1 ms                                                      | 18.6 ms: 1.02x faster                                                        |
| async_tree_io           | 1.17 sec                                                     | 1.15 sec: 1.02x faster                                                       |
| tornado_http            | 122 ms                                                       | 119 ms: 1.02x faster                                                         |
| deepcopy_reduce         | 3.51 us                                                      | 3.45 us: 1.02x faster                                                        |
| sympy_integrate         | 25.8 ms                                                      | 25.3 ms: 1.02x faster                                                        |
| sympy_sum               | 185 ms                                                       | 182 ms: 1.02x faster                                                         |
| async_tree_cpu_io_mixed | 749 ms                                                       | 739 ms: 1.01x faster                                                         |
| sqlglot_optimize        | 59.8 ms                                                      | 59.0 ms: 1.01x faster                                                        |
| comprehensions          | 24.6 us                                                      | 24.3 us: 1.01x faster                                                        |
| regex_v8                | 23.9 ms                                                      | 23.6 ms: 1.01x faster                                                        |
| 2to3                    | 288 ms                                                       | 284 ms: 1.01x faster                                                         |
| scimark_sor             | 111 ms                                                       | 110 ms: 1.01x faster                                                         |
| scimark_sparse_mat_mult | 4.05 ms                                                      | 4.01 ms: 1.01x faster                                                        |
| scimark_monte_carlo     | 68.2 ms                                                      | 68.0 ms: 1.00x faster                                                        |
| pickle_dict             | 30.8 us                                                      | 30.7 us: 1.00x faster                                                        |
| docutils                | 2.86 sec                                                     | 2.89 sec: 1.01x slower                                                       |
| xml_etree_iterparse     | 104 ms                                                       | 105 ms: 1.01x slower                                                         |
| regex_dna               | 227 ms                                                       | 230 ms: 1.01x slower                                                         |
| pprint_pformat          | 1.63 sec                                                     | 1.65 sec: 1.01x slower                                                       |
| pyflate                 | 449 ms                                                       | 458 ms: 1.02x slower                                                         |
| scimark_fft             | 285 ms                                                       | 292 ms: 1.02x slower                                                         |
| telco                   | 6.86 ms                                                      | 7.04 ms: 1.03x slower                                                        |
| pickle                  | 9.64 us                                                      | 9.91 us: 1.03x slower                                                        |
| pickle_list             | 3.83 us                                                      | 3.95 us: 1.03x slower                                                        |
| pprint_safe_repr        | 784 ms                                                       | 811 ms: 1.03x slower                                                         |
| pidigits                | 251 ms                                                       | 260 ms: 1.03x slower                                                         |
| python_startup          | 10.8 ms                                                      | 11.1 ms: 1.04x slower                                                        |
| xml_etree_process       | 56.5 ms                                                      | 58.5 ms: 1.04x slower                                                        |
| float                   | 74.2 ms                                                      | 77.1 ms: 1.04x slower                                                        |
| create_gc_cycles        | 1.61 ms                                                      | 1.68 ms: 1.04x slower                                                        |
| gc_traversal            | 3.85 ms                                                      | 4.02 ms: 1.04x slower                                                        |
| coverage                | 84.8 ms                                                      | 89.2 ms: 1.05x slower                                                        |
| meteor_contest          | 131 ms                                                       | 138 ms: 1.06x slower                                                         |
| unpickle                | 13.4 us                                                      | 14.2 us: 1.06x slower                                                        |
| xml_etree_generate      | 80.5 ms                                                      | 85.2 ms: 1.06x slower                                                        |
| sqlite_synth            | 2.50 us                                                      | 2.66 us: 1.07x slower                                                        |
| python_startup_no_site  | 7.76 ms                                                      | 8.37 ms: 1.08x slower                                                        |
| unpack_sequence         | 45.6 ns                                                      | 52.8 ns: 1.16x slower                                                        |
| async_generators        | 316 ms                                                       | 386 ms: 1.22x slower                                                         |
| bench_mp_pool           | 4.62 ms                                                      | 6.08 ms: 1.32x slower                                                        |
| dask                    | 410 ms                                                       | 563 ms: 1.37x slower                                                         |
| Geometric mean          | (ref)                                                        | 1.04x faster                                                                 |

Benchmark hidden because not significant (2): pickle_pure_python, unpickle_list
Ignored benchmarks (9) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x
