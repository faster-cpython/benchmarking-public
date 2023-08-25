
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: 30a306c
- commit date: 2023-03-25
- overall geometric mean: 1.09x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230325-pythonperf1-amd64-python-main-3.12.0a6+-30a306c |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 198 ms: 1.06x faster                                        |
| chameleon      | 5.11 ms                                                     | 4.57 ms: 1.12x faster                                       |
| docutils       | 1.60 sec                                                    | 1.52 sec: 1.06x faster                                      |
| html5lib       | 37.5 ms                                                     | 35.5 ms: 1.06x faster                                       |
| tornado_http   | 91.8 ms                                                     | 87.7 ms: 1.05x faster                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230325-pythonperf1-amd64-python-main-3.12.0a6+-30a306c |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 56.6 ms: 1.24x faster                                       |
| float          | 54.6 ms                                                     | 48.6 ms: 1.12x faster                                       |
| pidigits       | 148 ms                                                      | 145 ms: 1.03x faster                                        |
| Geometric mean | (ref)                                                       | 1.13x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230325-pythonperf1-amd64-python-main-3.12.0a6+-30a306c |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 82.3 ms: 1.10x faster                                       |
| regex_v8       | 13.8 ms                                                     | 13.6 ms: 1.01x faster                                       |
| regex_dna      | 115 ms                                                      | 119 ms: 1.03x slower                                        |
| regex_effbot   | 1.50 ms                                                     | 1.77 ms: 1.18x slower                                       |
| Geometric mean | (ref)                                                       | 1.02x slower                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230325-pythonperf1-amd64-python-main-3.12.0a6+-30a306c |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.58 ms: 1.36x faster                                       |
| unpickle_pure_python | 152 us                                                      | 122 us: 1.24x faster                                        |
| pickle_pure_python   | 200 us                                                      | 176 us: 1.14x faster                                        |
| xml_etree_parse      | 95.9 ms                                                     | 89.5 ms: 1.07x faster                                       |
| xml_etree_process    | 37.1 ms                                                     | 35.3 ms: 1.05x faster                                       |
| xml_etree_iterparse  | 62.6 ms                                                     | 60.4 ms: 1.04x faster                                       |
| unpickle             | 8.09 us                                                     | 7.97 us: 1.02x faster                                       |
| xml_etree_generate   | 52.2 ms                                                     | 51.7 ms: 1.01x faster                                       |
| json_loads           | 12.9 us                                                     | 13.4 us: 1.04x slower                                       |
| unpickle_list        | 2.55 us                                                     | 2.66 us: 1.05x slower                                       |
| pickle               | 6.61 us                                                     | 7.04 us: 1.07x slower                                       |
| pickle_list          | 2.68 us                                                     | 2.91 us: 1.09x slower                                       |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230325-pythonperf1-amd64-python-main-3.12.0a6+-30a306c |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 15.7 ms: 1.01x faster                                       |
| Geometric mean         | (ref)                                                       | 1.01x faster                                                |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230325-pythonperf1-amd64-python-main-3.12.0a6+-30a306c |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| genshi_text     | 17.0 ms                                                     | 13.6 ms: 1.24x faster                                       |
| genshi_xml      | 37.3 ms                                                     | 30.3 ms: 1.23x faster                                       |
| django_template | 24.1 ms                                                     | 20.6 ms: 1.17x faster                                       |
| mako            | 7.26 ms                                                     | 6.32 ms: 1.15x faster                                       |
| Geometric mean  | (ref)                                                       | 1.20x faster                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230325-pythonperf1-amd64-python-main-3.12.0a6+-30a306c |
|-------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| unpack_sequence         | 46.1 ns                                                     | 27.2 ns: 1.70x faster                                       |
| generators              | 33.8 ms                                                     | 21.0 ms: 1.61x faster                                       |
| asyncio_tcp             | 699 ms                                                      | 467 ms: 1.50x faster                                        |
| json_dumps              | 7.56 ms                                                     | 5.58 ms: 1.36x faster                                       |
| deltablue               | 2.61 ms                                                     | 1.94 ms: 1.34x faster                                       |
| logging_silent          | 69.8 ns                                                     | 54.4 ns: 1.28x faster                                       |
| genshi_text             | 17.0 ms                                                     | 13.6 ms: 1.24x faster                                       |
| unpickle_pure_python    | 152 us                                                      | 122 us: 1.24x faster                                        |
| nbody                   | 70.0 ms                                                     | 56.6 ms: 1.24x faster                                       |
| raytrace                | 211 ms                                                      | 171 ms: 1.24x faster                                        |
| genshi_xml              | 37.3 ms                                                     | 30.3 ms: 1.23x faster                                       |
| mdp                     | 1.67 sec                                                    | 1.37 sec: 1.22x faster                                      |
| richards                | 30.6 ms                                                     | 25.1 ms: 1.22x faster                                       |
| scimark_lu              | 63.5 ms                                                     | 52.6 ms: 1.21x faster                                       |
| hexiom                  | 4.55 ms                                                     | 3.80 ms: 1.20x faster                                       |
| json                    | 3.25 ms                                                     | 2.75 ms: 1.19x faster                                       |
| go                      | 97.3 ms                                                     | 82.6 ms: 1.18x faster                                       |
| chaos                   | 47.1 ms                                                     | 40.2 ms: 1.17x faster                                       |
| deepcopy_memo           | 25.2 us                                                     | 21.5 us: 1.17x faster                                       |
| django_template         | 24.1 ms                                                     | 20.6 ms: 1.17x faster                                       |
| deepcopy                | 246 us                                                      | 212 us: 1.16x faster                                        |
| mako                    | 7.26 ms                                                     | 6.32 ms: 1.15x faster                                       |
| nqueens                 | 64.9 ms                                                     | 56.7 ms: 1.14x faster                                       |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.25 ms: 1.14x faster                                       |
| pickle_pure_python      | 200 us                                                      | 176 us: 1.14x faster                                        |
| scimark_monte_carlo     | 44.6 ms                                                     | 39.5 ms: 1.13x faster                                       |
| deepcopy_reduce         | 2.07 us                                                     | 1.83 us: 1.13x faster                                       |
| float                   | 54.6 ms                                                     | 48.6 ms: 1.12x faster                                       |
| chameleon               | 5.11 ms                                                     | 4.57 ms: 1.12x faster                                       |
| pprint_safe_repr        | 512 ms                                                      | 458 ms: 1.12x faster                                        |
| sqlglot_normalize       | 190 ms                                                      | 171 ms: 1.11x faster                                        |
| fannkuch                | 252 ms                                                      | 227 ms: 1.11x faster                                        |
| sqlglot_transpile       | 1.16 ms                                                     | 1.05 ms: 1.11x faster                                       |
| sqlglot_optimize        | 34.9 ms                                                     | 31.5 ms: 1.11x faster                                       |
| logging_format          | 7.01 us                                                     | 6.35 us: 1.11x faster                                       |
| pprint_pformat          | 1.04 sec                                                    | 941 ms: 1.10x faster                                        |
| logging_simple          | 6.61 us                                                     | 5.99 us: 1.10x faster                                       |
| sqlglot_parse           | 952 us                                                      | 864 us: 1.10x faster                                        |
| regex_compile           | 90.6 ms                                                     | 82.3 ms: 1.10x faster                                       |
| async_tree_none         | 320 ms                                                      | 295 ms: 1.09x faster                                        |
| coverage                | 55.9 ms                                                     | 51.5 ms: 1.08x faster                                       |
| mypy2                   | 229 ms                                                      | 212 ms: 1.08x faster                                        |
| pyflate                 | 304 ms                                                      | 281 ms: 1.08x faster                                        |
| scimark_fft             | 178 ms                                                      | 165 ms: 1.08x faster                                        |
| pycparser               | 691 ms                                                      | 641 ms: 1.08x faster                                        |
| sympy_integrate         | 13.8 ms                                                     | 12.8 ms: 1.07x faster                                       |
| xml_etree_parse         | 95.9 ms                                                     | 89.5 ms: 1.07x faster                                       |
| async_tree_io           | 779 ms                                                      | 731 ms: 1.07x faster                                        |
| thrift                  | 491 us                                                      | 461 us: 1.07x faster                                        |
| sympy_expand            | 295 ms                                                      | 278 ms: 1.06x faster                                        |
| comprehensions          | 15.9 us                                                     | 15.0 us: 1.06x faster                                       |
| html5lib                | 37.5 ms                                                     | 35.5 ms: 1.06x faster                                       |
| crypto_pyaes            | 47.6 ms                                                     | 45.0 ms: 1.06x faster                                       |
| docutils                | 1.60 sec                                                    | 1.52 sec: 1.06x faster                                      |
| 2to3                    | 209 ms                                                      | 198 ms: 1.06x faster                                        |
| meteor_contest          | 74.7 ms                                                     | 70.9 ms: 1.05x faster                                       |
| async_tree_cpu_io_mixed | 501 ms                                                      | 475 ms: 1.05x faster                                        |
| xml_etree_process       | 37.1 ms                                                     | 35.3 ms: 1.05x faster                                       |
| tornado_http            | 91.8 ms                                                     | 87.7 ms: 1.05x faster                                       |
| sympy_str               | 182 ms                                                      | 174 ms: 1.05x faster                                        |
| async_tree_memoization  | 371 ms                                                      | 355 ms: 1.05x faster                                        |
| spectral_norm           | 67.9 ms                                                     | 65.4 ms: 1.04x faster                                       |
| xml_etree_iterparse     | 62.6 ms                                                     | 60.4 ms: 1.04x faster                                       |
| dulwich_log             | 44.5 ms                                                     | 43.0 ms: 1.04x faster                                       |
| create_gc_cycles        | 693 us                                                      | 671 us: 1.03x faster                                        |
| sympy_sum               | 99.9 ms                                                     | 96.8 ms: 1.03x faster                                       |
| pidigits                | 148 ms                                                      | 145 ms: 1.03x faster                                        |
| bench_thread_pool       | 852 us                                                      | 833 us: 1.02x faster                                        |
| telco                   | 3.90 ms                                                     | 3.83 ms: 1.02x faster                                       |
| coroutines              | 14.6 ms                                                     | 14.4 ms: 1.02x faster                                       |
| unpickle                | 8.09 us                                                     | 7.97 us: 1.02x faster                                       |
| regex_v8                | 13.8 ms                                                     | 13.6 ms: 1.01x faster                                       |
| python_startup_no_site  | 15.9 ms                                                     | 15.7 ms: 1.01x faster                                       |
| xml_etree_generate      | 52.2 ms                                                     | 51.7 ms: 1.01x faster                                       |
| gc_traversal            | 1.46 ms                                                     | 1.45 ms: 1.01x faster                                       |
| scimark_sor             | 75.6 ms                                                     | 76.4 ms: 1.01x slower                                       |
| regex_dna               | 115 ms                                                      | 119 ms: 1.03x slower                                        |
| bench_mp_pool           | 62.5 ms                                                     | 64.8 ms: 1.04x slower                                       |
| json_loads              | 12.9 us                                                     | 13.4 us: 1.04x slower                                       |
| unpickle_list           | 2.55 us                                                     | 2.66 us: 1.05x slower                                       |
| sqlite_synth            | 1.68 us                                                     | 1.78 us: 1.06x slower                                       |
| pickle                  | 6.61 us                                                     | 7.04 us: 1.07x slower                                       |
| pickle_list             | 2.68 us                                                     | 2.91 us: 1.09x slower                                       |
| pathlib                 | 71.4 ms                                                     | 84.2 ms: 1.18x slower                                       |
| regex_effbot            | 1.50 ms                                                     | 1.77 ms: 1.18x slower                                       |
| async_generators        | 178 ms                                                      | 213 ms: 1.20x slower                                        |
| dask                    | 264 ms                                                      | 354 ms: 1.34x slower                                        |
| Geometric mean          | (ref)                                                       | 1.09x faster                                                |

Benchmark hidden because not significant (2): python_startup, pickle_dict
Ignored benchmarks (9) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.05x
