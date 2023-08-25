
# Results vs. 3.11.0

- fork: python
- ref: 2e91dba437fe5c56c6f8
- machine: linux-x86_64
- commit hash: 2e91dba
- commit date: 2021-12-08
- overall geometric mean: 1.06x slower \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211208-pythonperf2-x86_64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 293 ms: 1.02x slower                                                        |
| chameleon      | 7.67 ms                                                      | 8.85 ms: 1.15x slower                                                       |
| docutils       | 2.86 sec                                                     | 3.02 sec: 1.06x slower                                                      |
| html5lib       | 72.9 ms                                                      | 75.1 ms: 1.03x slower                                                       |
| tornado_http   | 122 ms                                                       | 135 ms: 1.11x slower                                                        |
| Geometric mean | (ref)                                                        | 1.07x slower                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211208-pythonperf2-x86_64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 251 ms                                                       | 253 ms: 1.01x slower                                                        |
| float          | 74.2 ms                                                      | 80.9 ms: 1.09x slower                                                       |
| nbody          | 90.7 ms                                                      | 109 ms: 1.20x slower                                                        |
| Geometric mean | (ref)                                                        | 1.10x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211208-pythonperf2-x86_64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.50 ms                                                      | 3.10 ms: 1.13x faster                                                       |
| regex_compile  | 158 ms                                                       | 153 ms: 1.03x faster                                                        |
| regex_v8       | 23.9 ms                                                      | 25.7 ms: 1.08x slower                                                       |
| regex_dna      | 227 ms                                                       | 261 ms: 1.15x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211208-pythonperf2-x86_64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_loads           | 28.7 us                                                      | 25.3 us: 1.13x faster                                                       |
| unpickle             | 13.4 us                                                      | 13.2 us: 1.02x faster                                                       |
| xml_etree_parse      | 158 ms                                                       | 155 ms: 1.02x faster                                                        |
| xml_etree_generate   | 80.5 ms                                                      | 82.8 ms: 1.03x slower                                                       |
| json_dumps           | 13.4 ms                                                      | 14.1 ms: 1.05x slower                                                       |
| xml_etree_iterparse  | 104 ms                                                       | 110 ms: 1.05x slower                                                        |
| pickle               | 9.64 us                                                      | 10.2 us: 1.06x slower                                                       |
| pickle_dict          | 30.8 us                                                      | 33.0 us: 1.07x slower                                                       |
| xml_etree_process    | 56.5 ms                                                      | 60.9 ms: 1.08x slower                                                       |
| unpickle_pure_python | 241 us                                                       | 265 us: 1.10x slower                                                        |
| pickle_list          | 3.83 us                                                      | 4.32 us: 1.13x slower                                                       |
| pickle_pure_python   | 319 us                                                       | 366 us: 1.15x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.04x slower                                                                |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211208-pythonperf2-x86_64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.76 ms                                                      | 7.14 ms: 1.09x faster                                                       |
| python_startup         | 10.8 ms                                                      | 10.1 ms: 1.06x faster                                                       |
| Geometric mean         | (ref)                                                        | 1.07x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211208-pythonperf2-x86_64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 58.5 ms                                                      | 59.7 ms: 1.02x slower                                                       |
| genshi_text     | 26.1 ms                                                      | 28.2 ms: 1.08x slower                                                       |
| django_template | 40.2 ms                                                      | 44.9 ms: 1.12x slower                                                       |
| mako            | 11.0 ms                                                      | 12.9 ms: 1.17x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.10x slower                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211208-pythonperf2-x86_64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| coverage                | 84.8 ms                                                      | 72.1 ms: 1.18x faster                                                       |
| json_loads              | 28.7 us                                                      | 25.3 us: 1.13x faster                                                       |
| regex_effbot            | 3.50 ms                                                      | 3.10 ms: 1.13x faster                                                       |
| generators              | 56.0 ms                                                      | 50.1 ms: 1.12x faster                                                       |
| python_startup_no_site  | 7.76 ms                                                      | 7.14 ms: 1.09x faster                                                       |
| json                    | 5.65 ms                                                      | 5.24 ms: 1.08x faster                                                       |
| python_startup          | 10.8 ms                                                      | 10.1 ms: 1.06x faster                                                       |
| logging_format          | 8.11 us                                                      | 7.70 us: 1.05x faster                                                       |
| scimark_lu              | 115 ms                                                       | 110 ms: 1.04x faster                                                        |
| chaos                   | 80.9 ms                                                      | 78.3 ms: 1.03x faster                                                       |
| regex_compile           | 158 ms                                                       | 153 ms: 1.03x faster                                                        |
| logging_simple          | 7.19 us                                                      | 7.04 us: 1.02x faster                                                       |
| coroutines              | 27.6 ms                                                      | 27.0 ms: 1.02x faster                                                       |
| unpickle                | 13.4 us                                                      | 13.2 us: 1.02x faster                                                       |
| xml_etree_parse         | 158 ms                                                       | 155 ms: 1.02x faster                                                        |
| meteor_contest          | 131 ms                                                       | 129 ms: 1.01x faster                                                        |
| pidigits                | 251 ms                                                       | 253 ms: 1.01x slower                                                        |
| mdp                     | 2.75 sec                                                     | 2.76 sec: 1.01x slower                                                      |
| deepcopy_reduce         | 3.51 us                                                      | 3.55 us: 1.01x slower                                                       |
| gc_traversal            | 3.85 ms                                                      | 3.89 ms: 1.01x slower                                                       |
| async_generators        | 316 ms                                                       | 319 ms: 1.01x slower                                                        |
| unpack_sequence         | 45.6 ns                                                      | 46.3 ns: 1.02x slower                                                       |
| pycparser               | 1.32 sec                                                     | 1.35 sec: 1.02x slower                                                      |
| genshi_xml              | 58.5 ms                                                      | 59.7 ms: 1.02x slower                                                       |
| 2to3                    | 288 ms                                                       | 293 ms: 1.02x slower                                                        |
| sympy_sum               | 185 ms                                                       | 189 ms: 1.02x slower                                                        |
| xml_etree_generate      | 80.5 ms                                                      | 82.8 ms: 1.03x slower                                                       |
| sympy_integrate         | 25.8 ms                                                      | 26.5 ms: 1.03x slower                                                       |
| html5lib                | 72.9 ms                                                      | 75.1 ms: 1.03x slower                                                       |
| gunicorn                | 973 us                                                       | 1.00 ms: 1.03x slower                                                       |
| create_gc_cycles        | 1.61 ms                                                      | 1.66 ms: 1.03x slower                                                       |
| telco                   | 6.86 ms                                                      | 7.11 ms: 1.04x slower                                                       |
| scimark_sor             | 111 ms                                                       | 115 ms: 1.04x slower                                                        |
| sympy_str               | 337 ms                                                       | 350 ms: 1.04x slower                                                        |
| hexiom                  | 7.13 ms                                                      | 7.41 ms: 1.04x slower                                                       |
| sympy_expand            | 555 ms                                                       | 579 ms: 1.04x slower                                                        |
| deepcopy                | 399 us                                                       | 418 us: 1.05x slower                                                        |
| pathlib                 | 19.1 ms                                                      | 19.9 ms: 1.05x slower                                                       |
| bench_thread_pool       | 1.01 ms                                                      | 1.06 ms: 1.05x slower                                                       |
| json_dumps              | 13.4 ms                                                      | 14.1 ms: 1.05x slower                                                       |
| async_tree_none         | 519 ms                                                       | 545 ms: 1.05x slower                                                        |
| go                      | 164 ms                                                       | 173 ms: 1.05x slower                                                        |
| sqlglot_normalize       | 126 ms                                                       | 133 ms: 1.05x slower                                                        |
| xml_etree_iterparse     | 104 ms                                                       | 110 ms: 1.05x slower                                                        |
| docutils                | 2.86 sec                                                     | 3.02 sec: 1.06x slower                                                      |
| bench_mp_pool           | 4.62 ms                                                      | 4.90 ms: 1.06x slower                                                       |
| dask                    | 410 ms                                                       | 435 ms: 1.06x slower                                                        |
| pprint_safe_repr        | 784 ms                                                       | 832 ms: 1.06x slower                                                        |
| pickle                  | 9.64 us                                                      | 10.2 us: 1.06x slower                                                       |
| pprint_pformat          | 1.63 sec                                                     | 1.74 sec: 1.07x slower                                                      |
| dulwich_log             | 68.4 ms                                                      | 73.0 ms: 1.07x slower                                                       |
| deepcopy_memo           | 38.8 us                                                      | 41.5 us: 1.07x slower                                                       |
| spectral_norm           | 93.3 ms                                                      | 99.9 ms: 1.07x slower                                                       |
| pickle_dict             | 30.8 us                                                      | 33.0 us: 1.07x slower                                                       |
| regex_v8                | 23.9 ms                                                      | 25.7 ms: 1.08x slower                                                       |
| thrift                  | 925 us                                                       | 995 us: 1.08x slower                                                        |
| xml_etree_process       | 56.5 ms                                                      | 60.9 ms: 1.08x slower                                                       |
| genshi_text             | 26.1 ms                                                      | 28.2 ms: 1.08x slower                                                       |
| sqlite_synth            | 2.50 us                                                      | 2.70 us: 1.08x slower                                                       |
| sqlglot_optimize        | 59.8 ms                                                      | 64.7 ms: 1.08x slower                                                       |
| async_tree_cpu_io_mixed | 749 ms                                                       | 811 ms: 1.08x slower                                                        |
| async_tree_memoization  | 630 ms                                                       | 686 ms: 1.09x slower                                                        |
| float                   | 74.2 ms                                                      | 80.9 ms: 1.09x slower                                                       |
| raytrace                | 317 ms                                                       | 347 ms: 1.10x slower                                                        |
| scimark_fft             | 285 ms                                                       | 314 ms: 1.10x slower                                                        |
| unpickle_pure_python    | 241 us                                                       | 265 us: 1.10x slower                                                        |
| tornado_http            | 122 ms                                                       | 135 ms: 1.11x slower                                                        |
| django_template         | 40.2 ms                                                      | 44.9 ms: 1.12x slower                                                       |
| async_tree_io           | 1.17 sec                                                     | 1.32 sec: 1.12x slower                                                      |
| scimark_monte_carlo     | 68.2 ms                                                      | 76.7 ms: 1.12x slower                                                       |
| pickle_list             | 3.83 us                                                      | 4.32 us: 1.13x slower                                                       |
| scimark_sparse_mat_mult | 4.05 ms                                                      | 4.58 ms: 1.13x slower                                                       |
| crypto_pyaes            | 83.4 ms                                                      | 94.7 ms: 1.14x slower                                                       |
| regex_dna               | 227 ms                                                       | 261 ms: 1.15x slower                                                        |
| pickle_pure_python      | 319 us                                                       | 366 us: 1.15x slower                                                        |
| logging_silent          | 101 ns                                                       | 116 ns: 1.15x slower                                                        |
| chameleon               | 7.67 ms                                                      | 8.85 ms: 1.15x slower                                                       |
| pyflate                 | 449 ms                                                       | 525 ms: 1.17x slower                                                        |
| mako                    | 11.0 ms                                                      | 12.9 ms: 1.17x slower                                                       |
| richards                | 48.3 ms                                                      | 56.7 ms: 1.17x slower                                                       |
| deltablue               | 4.00 ms                                                      | 4.78 ms: 1.20x slower                                                       |
| nbody                   | 90.7 ms                                                      | 109 ms: 1.20x slower                                                        |
| comprehensions          | 24.6 us                                                      | 30.6 us: 1.24x slower                                                       |
| flaskblogging           | 3.88 ms                                                      | 4.95 ms: 1.28x slower                                                       |
| sqlglot_transpile       | 1.92 ms                                                      | 2.60 ms: 1.35x slower                                                       |
| sqlglot_parse           | 1.53 ms                                                      | 2.21 ms: 1.44x slower                                                       |
| Geometric mean          | (ref)                                                        | 1.06x slower                                                                |

Benchmark hidden because not significant (3): fannkuch, unpickle_list, nqueens
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x
