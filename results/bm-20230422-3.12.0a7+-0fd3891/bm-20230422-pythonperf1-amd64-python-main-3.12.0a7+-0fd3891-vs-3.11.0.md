
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: 0fd3891
- commit date: 2023-04-22
- overall geometric mean: 1.06x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230422-pythonperf1-amd64-python-main-3.12.0a7+-0fd3891 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 207 ms: 1.01x faster                                        |
| chameleon      | 5.11 ms                                                     | 4.93 ms: 1.04x faster                                       |
| docutils       | 1.60 sec                                                    | 1.54 sec: 1.04x faster                                      |
| html5lib       | 37.5 ms                                                     | 36.6 ms: 1.02x faster                                       |
| tornado_http   | 91.8 ms                                                     | 90.0 ms: 1.02x faster                                       |
| Geometric mean | (ref)                                                       | 1.03x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230422-pythonperf1-amd64-python-main-3.12.0a7+-0fd3891 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 54.6 ms                                                     | 51.4 ms: 1.06x faster                                       |
| nbody          | 70.0 ms                                                     | 73.1 ms: 1.04x slower                                       |
| Geometric mean | (ref)                                                       | 1.01x faster                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230422-pythonperf1-amd64-python-main-3.12.0a7+-0fd3891 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 83.8 ms: 1.08x faster                                       |
| regex_v8       | 13.8 ms                                                     | 13.0 ms: 1.06x faster                                       |
| regex_dna      | 115 ms                                                      | 115 ms: 1.00x faster                                        |
| regex_effbot   | 1.50 ms                                                     | 1.51 ms: 1.01x slower                                       |
| Geometric mean | (ref)                                                       | 1.03x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230422-pythonperf1-amd64-python-main-3.12.0a7+-0fd3891 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.41 ms: 1.40x faster                                       |
| unpickle_pure_python | 152 us                                                      | 135 us: 1.13x faster                                        |
| xml_etree_parse      | 95.9 ms                                                     | 87.5 ms: 1.10x faster                                       |
| pickle_pure_python   | 200 us                                                      | 189 us: 1.06x faster                                        |
| xml_etree_iterparse  | 62.6 ms                                                     | 60.0 ms: 1.04x faster                                       |
| pickle_dict          | 18.5 us                                                     | 18.2 us: 1.02x faster                                       |
| json_loads           | 12.9 us                                                     | 12.8 us: 1.01x faster                                       |
| xml_etree_process    | 37.1 ms                                                     | 37.4 ms: 1.01x slower                                       |
| pickle               | 6.61 us                                                     | 6.77 us: 1.02x slower                                       |
| unpickle_list        | 2.55 us                                                     | 2.63 us: 1.03x slower                                       |
| xml_etree_generate   | 52.2 ms                                                     | 54.4 ms: 1.04x slower                                       |
| unpickle             | 8.09 us                                                     | 8.46 us: 1.05x slower                                       |
| pickle_list          | 2.68 us                                                     | 2.81 us: 1.05x slower                                       |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230422-pythonperf1-amd64-python-main-3.12.0a7+-0fd3891 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 15.4 ms: 1.03x faster                                       |
| python_startup         | 18.7 ms                                                     | 18.2 ms: 1.03x faster                                       |
| Geometric mean         | (ref)                                                       | 1.03x faster                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230422-pythonperf1-amd64-python-main-3.12.0a7+-0fd3891 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| genshi_xml      | 37.3 ms                                                     | 32.5 ms: 1.15x faster                                       |
| genshi_text     | 17.0 ms                                                     | 15.1 ms: 1.12x faster                                       |
| django_template | 24.1 ms                                                     | 21.8 ms: 1.10x faster                                       |
| mako            | 7.26 ms                                                     | 6.66 ms: 1.09x faster                                       |
| Geometric mean  | (ref)                                                       | 1.12x faster                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230422-pythonperf1-amd64-python-main-3.12.0a7+-0fd3891 |
|-------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| generators              | 33.8 ms                                                     | 21.7 ms: 1.56x faster                                       |
| asyncio_tcp             | 699 ms                                                      | 470 ms: 1.49x faster                                        |
| json_dumps              | 7.56 ms                                                     | 5.41 ms: 1.40x faster                                       |
| unpack_sequence         | 46.1 ns                                                     | 37.4 ns: 1.23x faster                                       |
| deltablue               | 2.61 ms                                                     | 2.16 ms: 1.21x faster                                       |
| sqlglot_parse           | 952 us                                                      | 789 us: 1.21x faster                                        |
| pylint                  | 326 ms                                                      | 276 ms: 1.18x faster                                        |
| sqlglot_transpile       | 1.16 ms                                                     | 991 us: 1.17x faster                                        |
| logging_silent          | 69.8 ns                                                     | 59.5 ns: 1.17x faster                                       |
| scimark_lu              | 63.5 ms                                                     | 54.2 ms: 1.17x faster                                       |
| mdp                     | 1.67 sec                                                    | 1.44 sec: 1.16x faster                                      |
| json                    | 3.25 ms                                                     | 2.82 ms: 1.15x faster                                       |
| genshi_xml              | 37.3 ms                                                     | 32.5 ms: 1.15x faster                                       |
| raytrace                | 211 ms                                                      | 185 ms: 1.14x faster                                        |
| nqueens                 | 64.9 ms                                                     | 57.3 ms: 1.13x faster                                       |
| richards                | 30.6 ms                                                     | 27.1 ms: 1.13x faster                                       |
| unpickle_pure_python    | 152 us                                                      | 135 us: 1.13x faster                                        |
| genshi_text             | 17.0 ms                                                     | 15.1 ms: 1.12x faster                                       |
| go                      | 97.3 ms                                                     | 87.4 ms: 1.11x faster                                       |
| hexiom                  | 4.55 ms                                                     | 4.10 ms: 1.11x faster                                       |
| coverage                | 55.9 ms                                                     | 50.5 ms: 1.11x faster                                       |
| django_template         | 24.1 ms                                                     | 21.8 ms: 1.10x faster                                       |
| spectral_norm           | 67.9 ms                                                     | 61.6 ms: 1.10x faster                                       |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.33 ms: 1.10x faster                                       |
| xml_etree_parse         | 95.9 ms                                                     | 87.5 ms: 1.10x faster                                       |
| deepcopy_memo           | 25.2 us                                                     | 23.0 us: 1.09x faster                                       |
| mako                    | 7.26 ms                                                     | 6.66 ms: 1.09x faster                                       |
| chaos                   | 47.1 ms                                                     | 43.3 ms: 1.09x faster                                       |
| sqlglot_normalize       | 190 ms                                                      | 176 ms: 1.08x faster                                        |
| deepcopy                | 246 us                                                      | 227 us: 1.08x faster                                        |
| regex_compile           | 90.6 ms                                                     | 83.8 ms: 1.08x faster                                       |
| async_tree_none         | 320 ms                                                      | 298 ms: 1.08x faster                                        |
| dulwich_log             | 44.5 ms                                                     | 41.3 ms: 1.08x faster                                       |
| sqlglot_optimize        | 34.9 ms                                                     | 32.6 ms: 1.07x faster                                       |
| sympy_str               | 182 ms                                                      | 171 ms: 1.07x faster                                        |
| pyflate                 | 304 ms                                                      | 286 ms: 1.06x faster                                        |
| coroutines              | 14.6 ms                                                     | 13.8 ms: 1.06x faster                                       |
| mypy2                   | 229 ms                                                      | 215 ms: 1.06x faster                                        |
| float                   | 54.6 ms                                                     | 51.4 ms: 1.06x faster                                       |
| comprehensions          | 15.9 us                                                     | 15.0 us: 1.06x faster                                       |
| regex_v8                | 13.8 ms                                                     | 13.0 ms: 1.06x faster                                       |
| sympy_expand            | 295 ms                                                      | 278 ms: 1.06x faster                                        |
| logging_simple          | 6.61 us                                                     | 6.25 us: 1.06x faster                                       |
| pickle_pure_python      | 200 us                                                      | 189 us: 1.06x faster                                        |
| async_tree_cpu_io_mixed | 501 ms                                                      | 474 ms: 1.06x faster                                        |
| deepcopy_reduce         | 2.07 us                                                     | 1.97 us: 1.05x faster                                       |
| logging_format          | 7.01 us                                                     | 6.67 us: 1.05x faster                                       |
| pycparser               | 691 ms                                                      | 658 ms: 1.05x faster                                        |
| bench_thread_pool       | 852 us                                                      | 813 us: 1.05x faster                                        |
| scimark_monte_carlo     | 44.6 ms                                                     | 42.7 ms: 1.04x faster                                       |
| pprint_pformat          | 1.04 sec                                                    | 995 ms: 1.04x faster                                        |
| sympy_integrate         | 13.8 ms                                                     | 13.2 ms: 1.04x faster                                       |
| xml_etree_iterparse     | 62.6 ms                                                     | 60.0 ms: 1.04x faster                                       |
| pprint_safe_repr        | 512 ms                                                      | 491 ms: 1.04x faster                                        |
| async_tree_io           | 779 ms                                                      | 748 ms: 1.04x faster                                        |
| fannkuch                | 252 ms                                                      | 243 ms: 1.04x faster                                        |
| sympy_sum               | 99.9 ms                                                     | 96.1 ms: 1.04x faster                                       |
| async_tree_memoization  | 371 ms                                                      | 357 ms: 1.04x faster                                        |
| docutils                | 1.60 sec                                                    | 1.54 sec: 1.04x faster                                      |
| chameleon               | 5.11 ms                                                     | 4.93 ms: 1.04x faster                                       |
| thrift                  | 491 us                                                      | 474 us: 1.04x faster                                        |
| scimark_fft             | 178 ms                                                      | 172 ms: 1.03x faster                                        |
| python_startup_no_site  | 15.9 ms                                                     | 15.4 ms: 1.03x faster                                       |
| telco                   | 3.90 ms                                                     | 3.80 ms: 1.03x faster                                       |
| python_startup          | 18.7 ms                                                     | 18.2 ms: 1.03x faster                                       |
| html5lib                | 37.5 ms                                                     | 36.6 ms: 1.02x faster                                       |
| crypto_pyaes            | 47.6 ms                                                     | 46.4 ms: 1.02x faster                                       |
| create_gc_cycles        | 693 us                                                      | 677 us: 1.02x faster                                        |
| tornado_http            | 91.8 ms                                                     | 90.0 ms: 1.02x faster                                       |
| pickle_dict             | 18.5 us                                                     | 18.2 us: 1.02x faster                                       |
| json_loads              | 12.9 us                                                     | 12.8 us: 1.01x faster                                       |
| 2to3                    | 209 ms                                                      | 207 ms: 1.01x faster                                        |
| regex_dna               | 115 ms                                                      | 115 ms: 1.00x faster                                        |
| gc_traversal            | 1.46 ms                                                     | 1.47 ms: 1.01x slower                                       |
| xml_etree_process       | 37.1 ms                                                     | 37.4 ms: 1.01x slower                                       |
| regex_effbot            | 1.50 ms                                                     | 1.51 ms: 1.01x slower                                       |
| pickle                  | 6.61 us                                                     | 6.77 us: 1.02x slower                                       |
| unpickle_list           | 2.55 us                                                     | 2.63 us: 1.03x slower                                       |
| meteor_contest          | 74.7 ms                                                     | 77.8 ms: 1.04x slower                                       |
| xml_etree_generate      | 52.2 ms                                                     | 54.4 ms: 1.04x slower                                       |
| nbody                   | 70.0 ms                                                     | 73.1 ms: 1.04x slower                                       |
| unpickle                | 8.09 us                                                     | 8.46 us: 1.05x slower                                       |
| pickle_list             | 2.68 us                                                     | 2.81 us: 1.05x slower                                       |
| bench_mp_pool           | 62.5 ms                                                     | 66.7 ms: 1.07x slower                                       |
| scimark_sor             | 75.6 ms                                                     | 80.8 ms: 1.07x slower                                       |
| sqlite_synth            | 1.68 us                                                     | 1.81 us: 1.07x slower                                       |
| pathlib                 | 71.4 ms                                                     | 82.4 ms: 1.15x slower                                       |
| async_generators        | 178 ms                                                      | 216 ms: 1.21x slower                                        |
| dask                    | 264 ms                                                      | 357 ms: 1.35x slower                                        |
| Geometric mean          | (ref)                                                       | 1.06x faster                                                |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (8) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x
