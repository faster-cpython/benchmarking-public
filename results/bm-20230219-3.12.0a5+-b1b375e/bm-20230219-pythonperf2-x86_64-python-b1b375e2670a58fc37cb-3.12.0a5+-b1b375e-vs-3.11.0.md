
# Results vs. 3.11.0

- fork: python
- ref: b1b375e2670a58fc37cb
- machine: linux-x86_64
- commit hash: b1b375e
- commit date: 2023-02-19
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230219-pythonperf2-x86_64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 279 ms: 1.03x faster                                                         |
| chameleon      | 7.67 ms                                                      | 7.14 ms: 1.07x faster                                                        |
| docutils       | 2.86 sec                                                     | 2.80 sec: 1.02x faster                                                       |
| html5lib       | 72.9 ms                                                      | 68.0 ms: 1.07x faster                                                        |
| tornado_http   | 122 ms                                                       | 117 ms: 1.04x faster                                                         |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230219-pythonperf2-x86_64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 74.2 ms                                                      | 70.9 ms: 1.05x faster                                                        |
| pidigits       | 251 ms                                                       | 252 ms: 1.00x slower                                                         |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230219-pythonperf2-x86_64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 142 ms: 1.11x faster                                                         |
| regex_v8       | 23.9 ms                                                      | 22.9 ms: 1.04x faster                                                        |
| regex_effbot   | 3.50 ms                                                      | 3.42 ms: 1.02x faster                                                        |
| regex_dna      | 227 ms                                                       | 225 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230219-pythonperf2-x86_64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.2 ms: 1.31x faster                                                        |
| json_loads           | 28.7 us                                                      | 23.9 us: 1.20x faster                                                        |
| unpickle_pure_python | 241 us                                                       | 206 us: 1.17x faster                                                         |
| xml_etree_parse      | 158 ms                                                       | 141 ms: 1.12x faster                                                         |
| pickle_pure_python   | 319 us                                                       | 305 us: 1.04x faster                                                         |
| xml_etree_iterparse  | 104 ms                                                       | 101 ms: 1.03x faster                                                         |
| unpickle_list        | 4.53 us                                                      | 4.44 us: 1.02x faster                                                        |
| unpickle             | 13.4 us                                                      | 13.3 us: 1.01x faster                                                        |
| pickle_list          | 3.83 us                                                      | 3.79 us: 1.01x faster                                                        |
| xml_etree_process    | 56.5 ms                                                      | 57.1 ms: 1.01x slower                                                        |
| xml_etree_generate   | 80.5 ms                                                      | 83.2 ms: 1.03x slower                                                        |
| pickle_dict          | 30.8 us                                                      | 32.3 us: 1.05x slower                                                        |
| pickle               | 9.64 us                                                      | 10.3 us: 1.06x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.05x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230219-pythonperf2-x86_64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.2 ms: 1.04x slower                                                        |
| python_startup_no_site | 7.76 ms                                                      | 8.28 ms: 1.07x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230219-pythonperf2-x86_64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.0 ms                                                      | 9.92 ms: 1.11x faster                                                        |
| genshi_xml      | 58.5 ms                                                      | 53.6 ms: 1.09x faster                                                        |
| genshi_text     | 26.1 ms                                                      | 24.7 ms: 1.06x faster                                                        |
| django_template | 40.2 ms                                                      | 38.3 ms: 1.05x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.08x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230219-pythonperf2-x86_64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| asyncio_tcp             | 753 ms                                                       | 386 ms: 1.95x faster                                                         |
| generators              | 56.0 ms                                                      | 39.9 ms: 1.40x faster                                                        |
| json_dumps              | 13.4 ms                                                      | 10.2 ms: 1.31x faster                                                        |
| mypy2                   | 451 ms                                                       | 368 ms: 1.23x faster                                                         |
| deltablue               | 4.00 ms                                                      | 3.32 ms: 1.20x faster                                                        |
| json_loads              | 28.7 us                                                      | 23.9 us: 1.20x faster                                                        |
| comprehensions          | 24.6 us                                                      | 21.1 us: 1.17x faster                                                        |
| unpickle_pure_python    | 241 us                                                       | 206 us: 1.17x faster                                                         |
| scimark_lu              | 115 ms                                                       | 99.6 ms: 1.15x faster                                                        |
| coroutines              | 27.6 ms                                                      | 24.0 ms: 1.15x faster                                                        |
| json                    | 5.65 ms                                                      | 5.00 ms: 1.13x faster                                                        |
| chaos                   | 80.9 ms                                                      | 71.8 ms: 1.13x faster                                                        |
| xml_etree_parse         | 158 ms                                                       | 141 ms: 1.12x faster                                                         |
| hexiom                  | 7.13 ms                                                      | 6.39 ms: 1.12x faster                                                        |
| deepcopy_memo           | 38.8 us                                                      | 35.0 us: 1.11x faster                                                        |
| mako                    | 11.0 ms                                                      | 9.92 ms: 1.11x faster                                                        |
| regex_compile           | 158 ms                                                       | 142 ms: 1.11x faster                                                         |
| pycparser               | 1.32 sec                                                     | 1.21 sec: 1.10x faster                                                       |
| genshi_xml              | 58.5 ms                                                      | 53.6 ms: 1.09x faster                                                        |
| go                      | 164 ms                                                       | 150 ms: 1.09x faster                                                         |
| logging_silent          | 101 ns                                                       | 92.7 ns: 1.09x faster                                                        |
| raytrace                | 317 ms                                                       | 293 ms: 1.08x faster                                                         |
| richards                | 48.3 ms                                                      | 44.8 ms: 1.08x faster                                                        |
| gc_traversal            | 3.85 ms                                                      | 3.57 ms: 1.08x faster                                                        |
| chameleon               | 7.67 ms                                                      | 7.14 ms: 1.07x faster                                                        |
| html5lib                | 72.9 ms                                                      | 68.0 ms: 1.07x faster                                                        |
| scimark_sparse_mat_mult | 4.05 ms                                                      | 3.78 ms: 1.07x faster                                                        |
| sympy_str               | 337 ms                                                       | 315 ms: 1.07x faster                                                         |
| nqueens                 | 103 ms                                                       | 96.9 ms: 1.06x faster                                                        |
| genshi_text             | 26.1 ms                                                      | 24.7 ms: 1.06x faster                                                        |
| bench_thread_pool       | 1.01 ms                                                      | 956 us: 1.06x faster                                                         |
| scimark_sor             | 111 ms                                                       | 105 ms: 1.05x faster                                                         |
| pprint_pformat          | 1.63 sec                                                     | 1.55 sec: 1.05x faster                                                       |
| sympy_integrate         | 25.8 ms                                                      | 24.5 ms: 1.05x faster                                                        |
| deepcopy_reduce         | 3.51 us                                                      | 3.34 us: 1.05x faster                                                        |
| sympy_sum               | 185 ms                                                       | 176 ms: 1.05x faster                                                         |
| sqlglot_normalize       | 126 ms                                                       | 120 ms: 1.05x faster                                                         |
| dulwich_log             | 68.4 ms                                                      | 65.2 ms: 1.05x faster                                                        |
| mdp                     | 2.75 sec                                                     | 2.62 sec: 1.05x faster                                                       |
| django_template         | 40.2 ms                                                      | 38.3 ms: 1.05x faster                                                        |
| float                   | 74.2 ms                                                      | 70.9 ms: 1.05x faster                                                        |
| pickle_pure_python      | 319 us                                                       | 305 us: 1.04x faster                                                         |
| regex_v8                | 23.9 ms                                                      | 22.9 ms: 1.04x faster                                                        |
| tornado_http            | 122 ms                                                       | 117 ms: 1.04x faster                                                         |
| deepcopy                | 399 us                                                       | 384 us: 1.04x faster                                                         |
| sqlglot_optimize        | 59.8 ms                                                      | 57.6 ms: 1.04x faster                                                        |
| crypto_pyaes            | 83.4 ms                                                      | 80.4 ms: 1.04x faster                                                        |
| logging_format          | 8.11 us                                                      | 7.82 us: 1.04x faster                                                        |
| sympy_expand            | 555 ms                                                       | 535 ms: 1.04x faster                                                         |
| logging_simple          | 7.19 us                                                      | 6.94 us: 1.04x faster                                                        |
| pyflate                 | 449 ms                                                       | 434 ms: 1.03x faster                                                         |
| 2to3                    | 288 ms                                                       | 279 ms: 1.03x faster                                                         |
| pprint_safe_repr        | 784 ms                                                       | 759 ms: 1.03x faster                                                         |
| xml_etree_iterparse     | 104 ms                                                       | 101 ms: 1.03x faster                                                         |
| async_tree_memoization  | 630 ms                                                       | 613 ms: 1.03x faster                                                         |
| unpack_sequence         | 45.6 ns                                                      | 44.4 ns: 1.03x faster                                                        |
| async_tree_none         | 519 ms                                                       | 507 ms: 1.02x faster                                                         |
| regex_effbot            | 3.50 ms                                                      | 3.42 ms: 1.02x faster                                                        |
| scimark_monte_carlo     | 68.2 ms                                                      | 66.8 ms: 1.02x faster                                                        |
| unpickle_list           | 4.53 us                                                      | 4.44 us: 1.02x faster                                                        |
| meteor_contest          | 131 ms                                                       | 128 ms: 1.02x faster                                                         |
| docutils                | 2.86 sec                                                     | 2.80 sec: 1.02x faster                                                       |
| telco                   | 6.86 ms                                                      | 6.73 ms: 1.02x faster                                                        |
| unpickle                | 13.4 us                                                      | 13.3 us: 1.01x faster                                                        |
| thrift                  | 925 us                                                       | 915 us: 1.01x faster                                                         |
| regex_dna               | 227 ms                                                       | 225 ms: 1.01x faster                                                         |
| pickle_list             | 3.83 us                                                      | 3.79 us: 1.01x faster                                                        |
| async_tree_cpu_io_mixed | 749 ms                                                       | 744 ms: 1.01x faster                                                         |
| pidigits                | 251 ms                                                       | 252 ms: 1.00x slower                                                         |
| sqlglot_parse           | 1.53 ms                                                      | 1.55 ms: 1.01x slower                                                        |
| xml_etree_process       | 56.5 ms                                                      | 57.1 ms: 1.01x slower                                                        |
| spectral_norm           | 93.3 ms                                                      | 94.6 ms: 1.01x slower                                                        |
| pathlib                 | 19.1 ms                                                      | 19.4 ms: 1.02x slower                                                        |
| xml_etree_generate      | 80.5 ms                                                      | 83.2 ms: 1.03x slower                                                        |
| python_startup          | 10.8 ms                                                      | 11.2 ms: 1.04x slower                                                        |
| pickle_dict             | 30.8 us                                                      | 32.3 us: 1.05x slower                                                        |
| sqlite_synth            | 2.50 us                                                      | 2.63 us: 1.05x slower                                                        |
| pickle                  | 9.64 us                                                      | 10.3 us: 1.06x slower                                                        |
| python_startup_no_site  | 7.76 ms                                                      | 8.28 ms: 1.07x slower                                                        |
| async_generators        | 316 ms                                                       | 375 ms: 1.19x slower                                                         |
| dask                    | 410 ms                                                       | 558 ms: 1.36x slower                                                         |
| Geometric mean          | (ref)                                                        | 1.05x faster                                                                 |

Benchmark hidden because not significant (8): scimark_fft, fannkuch, async_tree_io, nbody, sqlglot_transpile, coverage, create_gc_cycles, bench_mp_pool
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x
