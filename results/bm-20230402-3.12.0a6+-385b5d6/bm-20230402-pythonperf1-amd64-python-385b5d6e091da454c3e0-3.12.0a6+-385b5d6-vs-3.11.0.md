
# Results vs. 3.11.0

- fork: python
- ref: 385b5d6e091da454c3e0
- machine: windows-amd64
- commit hash: 385b5d6
- commit date: 2023-04-02
- overall geometric mean: 1.10x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230402-pythonperf1-amd64-python-385b5d6e091da454c3e0-3.12.0a6+-385b5d6 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 202 ms: 1.04x faster                                                        |
| chameleon      | 5.11 ms                                                     | 4.50 ms: 1.14x faster                                                       |
| docutils       | 1.60 sec                                                    | 1.58 sec: 1.02x faster                                                      |
| html5lib       | 37.5 ms                                                     | 35.7 ms: 1.05x faster                                                       |
| tornado_http   | 91.8 ms                                                     | 87.7 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230402-pythonperf1-amd64-python-385b5d6e091da454c3e0-3.12.0a6+-385b5d6 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 53.3 ms: 1.31x faster                                                       |
| float          | 54.6 ms                                                     | 47.4 ms: 1.15x faster                                                       |
| pidigits       | 148 ms                                                      | 145 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230402-pythonperf1-amd64-python-385b5d6e091da454c3e0-3.12.0a6+-385b5d6 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 79.5 ms: 1.14x faster                                                       |
| regex_effbot   | 1.50 ms                                                     | 1.55 ms: 1.04x slower                                                       |
| regex_dna      | 115 ms                                                      | 123 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230402-pythonperf1-amd64-python-385b5d6e091da454c3e0-3.12.0a6+-385b5d6 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.30 ms: 1.43x faster                                                       |
| unpickle_pure_python | 152 us                                                      | 121 us: 1.25x faster                                                        |
| pickle_pure_python   | 200 us                                                      | 171 us: 1.17x faster                                                        |
| xml_etree_parse      | 95.9 ms                                                     | 89.7 ms: 1.07x faster                                                       |
| xml_etree_process    | 37.1 ms                                                     | 34.7 ms: 1.07x faster                                                       |
| unpickle             | 8.09 us                                                     | 7.73 us: 1.05x faster                                                       |
| xml_etree_iterparse  | 62.6 ms                                                     | 60.4 ms: 1.04x faster                                                       |
| xml_etree_generate   | 52.2 ms                                                     | 50.7 ms: 1.03x faster                                                       |
| pickle_dict          | 18.5 us                                                     | 18.9 us: 1.02x slower                                                       |
| pickle_list          | 2.68 us                                                     | 2.75 us: 1.03x slower                                                       |
| json_loads           | 12.9 us                                                     | 13.5 us: 1.05x slower                                                       |
| pickle               | 6.61 us                                                     | 7.09 us: 1.07x slower                                                       |
| unpickle_list        | 2.55 us                                                     | 2.76 us: 1.08x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.06x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230402-pythonperf1-amd64-python-385b5d6e091da454c3e0-3.12.0a6+-385b5d6 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 16.2 ms: 1.02x slower                                                       |
| python_startup         | 18.7 ms                                                     | 19.0 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230402-pythonperf1-amd64-python-385b5d6e091da454c3e0-3.12.0a6+-385b5d6 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 17.0 ms                                                     | 13.2 ms: 1.28x faster                                                       |
| genshi_xml      | 37.3 ms                                                     | 29.6 ms: 1.26x faster                                                       |
| mako            | 7.26 ms                                                     | 6.17 ms: 1.18x faster                                                       |
| django_template | 24.1 ms                                                     | 20.7 ms: 1.16x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.22x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230402-pythonperf1-amd64-python-385b5d6e091da454c3e0-3.12.0a6+-385b5d6 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpack_sequence         | 46.1 ns                                                     | 27.4 ns: 1.68x faster                                                       |
| generators              | 33.8 ms                                                     | 20.2 ms: 1.67x faster                                                       |
| asyncio_tcp             | 699 ms                                                      | 481 ms: 1.45x faster                                                        |
| json_dumps              | 7.56 ms                                                     | 5.30 ms: 1.43x faster                                                       |
| deltablue               | 2.61 ms                                                     | 1.95 ms: 1.34x faster                                                       |
| nbody                   | 70.0 ms                                                     | 53.3 ms: 1.31x faster                                                       |
| logging_silent          | 69.8 ns                                                     | 53.8 ns: 1.30x faster                                                       |
| genshi_text             | 17.0 ms                                                     | 13.2 ms: 1.28x faster                                                       |
| richards                | 30.6 ms                                                     | 24.0 ms: 1.27x faster                                                       |
| genshi_xml              | 37.3 ms                                                     | 29.6 ms: 1.26x faster                                                       |
| scimark_lu              | 63.5 ms                                                     | 50.6 ms: 1.26x faster                                                       |
| deepcopy_memo           | 25.2 us                                                     | 20.1 us: 1.26x faster                                                       |
| unpickle_pure_python    | 152 us                                                      | 121 us: 1.25x faster                                                        |
| raytrace                | 211 ms                                                      | 169 ms: 1.24x faster                                                        |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.09 ms: 1.23x faster                                                       |
| json                    | 3.25 ms                                                     | 2.65 ms: 1.23x faster                                                       |
| spectral_norm           | 67.9 ms                                                     | 55.4 ms: 1.23x faster                                                       |
| hexiom                  | 4.55 ms                                                     | 3.78 ms: 1.20x faster                                                       |
| deepcopy                | 246 us                                                      | 205 us: 1.20x faster                                                        |
| mdp                     | 1.67 sec                                                    | 1.40 sec: 1.19x faster                                                      |
| go                      | 97.3 ms                                                     | 82.4 ms: 1.18x faster                                                       |
| mako                    | 7.26 ms                                                     | 6.17 ms: 1.18x faster                                                       |
| scimark_monte_carlo     | 44.6 ms                                                     | 38.0 ms: 1.18x faster                                                       |
| pickle_pure_python      | 200 us                                                      | 171 us: 1.17x faster                                                        |
| django_template         | 24.1 ms                                                     | 20.7 ms: 1.16x faster                                                       |
| scimark_sor             | 75.6 ms                                                     | 65.1 ms: 1.16x faster                                                       |
| scimark_fft             | 178 ms                                                      | 154 ms: 1.16x faster                                                        |
| float                   | 54.6 ms                                                     | 47.4 ms: 1.15x faster                                                       |
| chaos                   | 47.1 ms                                                     | 40.9 ms: 1.15x faster                                                       |
| deepcopy_reduce         | 2.07 us                                                     | 1.80 us: 1.15x faster                                                       |
| sqlglot_normalize       | 190 ms                                                      | 165 ms: 1.15x faster                                                        |
| pprint_pformat          | 1.04 sec                                                    | 906 ms: 1.15x faster                                                        |
| sqlglot_parse           | 952 us                                                      | 832 us: 1.14x faster                                                        |
| sqlglot_transpile       | 1.16 ms                                                     | 1.02 ms: 1.14x faster                                                       |
| regex_compile           | 90.6 ms                                                     | 79.5 ms: 1.14x faster                                                       |
| chameleon               | 5.11 ms                                                     | 4.50 ms: 1.14x faster                                                       |
| sqlglot_optimize        | 34.9 ms                                                     | 30.7 ms: 1.14x faster                                                       |
| nqueens                 | 64.9 ms                                                     | 57.4 ms: 1.13x faster                                                       |
| pprint_safe_repr        | 512 ms                                                      | 453 ms: 1.13x faster                                                        |
| fannkuch                | 252 ms                                                      | 225 ms: 1.12x faster                                                        |
| logging_format          | 7.01 us                                                     | 6.29 us: 1.12x faster                                                       |
| logging_simple          | 6.61 us                                                     | 6.02 us: 1.10x faster                                                       |
| crypto_pyaes            | 47.6 ms                                                     | 43.4 ms: 1.10x faster                                                       |
| pyflate                 | 304 ms                                                      | 278 ms: 1.10x faster                                                        |
| comprehensions          | 15.9 us                                                     | 14.6 us: 1.09x faster                                                       |
| meteor_contest          | 74.7 ms                                                     | 69.1 ms: 1.08x faster                                                       |
| sympy_integrate         | 13.8 ms                                                     | 12.8 ms: 1.08x faster                                                       |
| coverage                | 55.9 ms                                                     | 52.2 ms: 1.07x faster                                                       |
| xml_etree_parse         | 95.9 ms                                                     | 89.7 ms: 1.07x faster                                                       |
| xml_etree_process       | 37.1 ms                                                     | 34.7 ms: 1.07x faster                                                       |
| dulwich_log             | 44.5 ms                                                     | 41.6 ms: 1.07x faster                                                       |
| thrift                  | 491 us                                                      | 460 us: 1.07x faster                                                        |
| sympy_expand            | 295 ms                                                      | 278 ms: 1.06x faster                                                        |
| coroutines              | 14.6 ms                                                     | 13.8 ms: 1.06x faster                                                       |
| mypy2                   | 229 ms                                                      | 217 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed | 501 ms                                                      | 476 ms: 1.05x faster                                                        |
| html5lib                | 37.5 ms                                                     | 35.7 ms: 1.05x faster                                                       |
| async_tree_none         | 320 ms                                                      | 306 ms: 1.05x faster                                                        |
| tornado_http            | 91.8 ms                                                     | 87.7 ms: 1.05x faster                                                       |
| unpickle                | 8.09 us                                                     | 7.73 us: 1.05x faster                                                       |
| sympy_str               | 182 ms                                                      | 175 ms: 1.04x faster                                                        |
| pycparser               | 691 ms                                                      | 665 ms: 1.04x faster                                                        |
| 2to3                    | 209 ms                                                      | 202 ms: 1.04x faster                                                        |
| xml_etree_iterparse     | 62.6 ms                                                     | 60.4 ms: 1.04x faster                                                       |
| xml_etree_generate      | 52.2 ms                                                     | 50.7 ms: 1.03x faster                                                       |
| async_tree_io           | 779 ms                                                      | 757 ms: 1.03x faster                                                        |
| async_tree_memoization  | 371 ms                                                      | 362 ms: 1.02x faster                                                        |
| pidigits                | 148 ms                                                      | 145 ms: 1.02x faster                                                        |
| sympy_sum               | 99.9 ms                                                     | 97.7 ms: 1.02x faster                                                       |
| bench_thread_pool       | 852 us                                                      | 836 us: 1.02x faster                                                        |
| docutils                | 1.60 sec                                                    | 1.58 sec: 1.02x faster                                                      |
| telco                   | 3.90 ms                                                     | 3.92 ms: 1.00x slower                                                       |
| gc_traversal            | 1.46 ms                                                     | 1.47 ms: 1.01x slower                                                       |
| python_startup_no_site  | 15.9 ms                                                     | 16.2 ms: 1.02x slower                                                       |
| python_startup          | 18.7 ms                                                     | 19.0 ms: 1.02x slower                                                       |
| pickle_dict             | 18.5 us                                                     | 18.9 us: 1.02x slower                                                       |
| pickle_list             | 2.68 us                                                     | 2.75 us: 1.03x slower                                                       |
| regex_effbot            | 1.50 ms                                                     | 1.55 ms: 1.04x slower                                                       |
| json_loads              | 12.9 us                                                     | 13.5 us: 1.05x slower                                                       |
| sqlite_synth            | 1.68 us                                                     | 1.78 us: 1.06x slower                                                       |
| regex_dna               | 115 ms                                                      | 123 ms: 1.06x slower                                                        |
| bench_mp_pool           | 62.5 ms                                                     | 66.4 ms: 1.06x slower                                                       |
| pickle                  | 6.61 us                                                     | 7.09 us: 1.07x slower                                                       |
| unpickle_list           | 2.55 us                                                     | 2.76 us: 1.08x slower                                                       |
| async_generators        | 178 ms                                                      | 206 ms: 1.16x slower                                                        |
| pathlib                 | 71.4 ms                                                     | 83.9 ms: 1.18x slower                                                       |
| dask                    | 264 ms                                                      | 355 ms: 1.34x slower                                                        |
| Geometric mean          | (ref)                                                       | 1.10x faster                                                                |

Benchmark hidden because not significant (2): regex_v8, create_gc_cycles
Ignored benchmarks (9) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x
