
# Results vs. 3.11.0

- fork: python
- ref: d49409196e0c73c38e3f
- machine: windows-amd64
- commit hash: d494091
- commit date: 2023-03-24
- overall geometric mean: 1.11x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 194 ms: 1.07x faster                                                        |
| chameleon      | 5.11 ms                                                     | 4.30 ms: 1.19x faster                                                       |
| docutils       | 1.60 sec                                                    | 1.51 sec: 1.06x faster                                                      |
| html5lib       | 37.5 ms                                                     | 35.5 ms: 1.06x faster                                                       |
| tornado_http   | 91.8 ms                                                     | 86.7 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 55.6 ms: 1.26x faster                                                       |
| float          | 54.6 ms                                                     | 46.0 ms: 1.19x faster                                                       |
| pidigits       | 148 ms                                                      | 146 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 79.6 ms: 1.14x faster                                                       |
| regex_dna      | 115 ms                                                      | 122 ms: 1.06x slower                                                        |
| regex_effbot   | 1.50 ms                                                     | 1.83 ms: 1.23x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.44 ms: 1.39x faster                                                       |
| unpickle_pure_python | 152 us                                                      | 117 us: 1.30x faster                                                        |
| pickle_pure_python   | 200 us                                                      | 168 us: 1.19x faster                                                        |
| xml_etree_parse      | 95.9 ms                                                     | 87.3 ms: 1.10x faster                                                       |
| xml_etree_process    | 37.1 ms                                                     | 33.9 ms: 1.09x faster                                                       |
| xml_etree_iterparse  | 62.6 ms                                                     | 59.2 ms: 1.06x faster                                                       |
| xml_etree_generate   | 52.2 ms                                                     | 50.0 ms: 1.04x faster                                                       |
| unpickle             | 8.09 us                                                     | 7.96 us: 1.02x faster                                                       |
| pickle_list          | 2.68 us                                                     | 2.78 us: 1.04x slower                                                       |
| json_loads           | 12.9 us                                                     | 13.4 us: 1.04x slower                                                       |
| unpickle_list        | 2.55 us                                                     | 2.70 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.07x faster                                                                |

Benchmark hidden because not significant (2): pickle_dict, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 15.3 ms: 1.04x faster                                                       |
| python_startup         | 18.7 ms                                                     | 18.2 ms: 1.03x faster                                                       |
| Geometric mean         | (ref)                                                       | 1.03x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 17.0 ms                                                     | 13.8 ms: 1.22x faster                                                       |
| genshi_xml      | 37.3 ms                                                     | 30.5 ms: 1.22x faster                                                       |
| django_template | 24.1 ms                                                     | 19.9 ms: 1.21x faster                                                       |
| mako            | 7.26 ms                                                     | 6.10 ms: 1.19x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.21x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpack_sequence         | 46.1 ns                                                     | 27.4 ns: 1.68x faster                                                       |
| generators              | 33.8 ms                                                     | 20.9 ms: 1.62x faster                                                       |
| asyncio_tcp             | 699 ms                                                      | 469 ms: 1.49x faster                                                        |
| json_dumps              | 7.56 ms                                                     | 5.44 ms: 1.39x faster                                                       |
| deltablue               | 2.61 ms                                                     | 1.91 ms: 1.36x faster                                                       |
| unpickle_pure_python    | 152 us                                                      | 117 us: 1.30x faster                                                        |
| raytrace                | 211 ms                                                      | 164 ms: 1.29x faster                                                        |
| deepcopy_memo           | 25.2 us                                                     | 19.6 us: 1.28x faster                                                       |
| logging_silent          | 69.8 ns                                                     | 54.5 ns: 1.28x faster                                                       |
| nbody                   | 70.0 ms                                                     | 55.6 ms: 1.26x faster                                                       |
| scimark_lu              | 63.5 ms                                                     | 50.5 ms: 1.26x faster                                                       |
| richards                | 30.6 ms                                                     | 24.3 ms: 1.26x faster                                                       |
| hexiom                  | 4.55 ms                                                     | 3.66 ms: 1.24x faster                                                       |
| mdp                     | 1.67 sec                                                    | 1.36 sec: 1.23x faster                                                      |
| genshi_text             | 17.0 ms                                                     | 13.8 ms: 1.22x faster                                                       |
| genshi_xml              | 37.3 ms                                                     | 30.5 ms: 1.22x faster                                                       |
| django_template         | 24.1 ms                                                     | 19.9 ms: 1.21x faster                                                       |
| go                      | 97.3 ms                                                     | 80.6 ms: 1.21x faster                                                       |
| json                    | 3.25 ms                                                     | 2.71 ms: 1.20x faster                                                       |
| deepcopy                | 246 us                                                      | 204 us: 1.20x faster                                                        |
| nqueens                 | 64.9 ms                                                     | 54.1 ms: 1.20x faster                                                       |
| mako                    | 7.26 ms                                                     | 6.10 ms: 1.19x faster                                                       |
| chaos                   | 47.1 ms                                                     | 39.6 ms: 1.19x faster                                                       |
| chameleon               | 5.11 ms                                                     | 4.30 ms: 1.19x faster                                                       |
| pickle_pure_python      | 200 us                                                      | 168 us: 1.19x faster                                                        |
| float                   | 54.6 ms                                                     | 46.0 ms: 1.19x faster                                                       |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.20 ms: 1.17x faster                                                       |
| pprint_safe_repr        | 512 ms                                                      | 443 ms: 1.15x faster                                                        |
| pprint_pformat          | 1.04 sec                                                    | 902 ms: 1.15x faster                                                        |
| sqlglot_normalize       | 190 ms                                                      | 166 ms: 1.15x faster                                                        |
| deepcopy_reduce         | 2.07 us                                                     | 1.82 us: 1.14x faster                                                       |
| regex_compile           | 90.6 ms                                                     | 79.6 ms: 1.14x faster                                                       |
| fannkuch                | 252 ms                                                      | 222 ms: 1.14x faster                                                        |
| scimark_monte_carlo     | 44.6 ms                                                     | 39.3 ms: 1.13x faster                                                       |
| sqlglot_optimize        | 34.9 ms                                                     | 30.8 ms: 1.13x faster                                                       |
| sqlglot_parse           | 952 us                                                      | 843 us: 1.13x faster                                                        |
| sqlglot_transpile       | 1.16 ms                                                     | 1.03 ms: 1.13x faster                                                       |
| scimark_fft             | 178 ms                                                      | 159 ms: 1.12x faster                                                        |
| pyflate                 | 304 ms                                                      | 271 ms: 1.12x faster                                                        |
| logging_simple          | 6.61 us                                                     | 5.91 us: 1.12x faster                                                       |
| coverage                | 55.9 ms                                                     | 50.1 ms: 1.12x faster                                                       |
| spectral_norm           | 67.9 ms                                                     | 61.1 ms: 1.11x faster                                                       |
| xml_etree_parse         | 95.9 ms                                                     | 87.3 ms: 1.10x faster                                                       |
| logging_format          | 7.01 us                                                     | 6.41 us: 1.09x faster                                                       |
| xml_etree_process       | 37.1 ms                                                     | 33.9 ms: 1.09x faster                                                       |
| mypy2                   | 229 ms                                                      | 209 ms: 1.09x faster                                                        |
| sympy_expand            | 295 ms                                                      | 271 ms: 1.09x faster                                                        |
| async_tree_none         | 320 ms                                                      | 295 ms: 1.09x faster                                                        |
| pycparser               | 691 ms                                                      | 640 ms: 1.08x faster                                                        |
| sympy_integrate         | 13.8 ms                                                     | 12.8 ms: 1.08x faster                                                       |
| comprehensions          | 15.9 us                                                     | 14.8 us: 1.08x faster                                                       |
| async_tree_io           | 779 ms                                                      | 723 ms: 1.08x faster                                                        |
| sympy_str               | 182 ms                                                      | 169 ms: 1.08x faster                                                        |
| 2to3                    | 209 ms                                                      | 194 ms: 1.07x faster                                                        |
| crypto_pyaes            | 47.6 ms                                                     | 44.3 ms: 1.07x faster                                                       |
| scimark_sor             | 75.6 ms                                                     | 70.6 ms: 1.07x faster                                                       |
| thrift                  | 491 us                                                      | 459 us: 1.07x faster                                                        |
| async_tree_memoization  | 371 ms                                                      | 349 ms: 1.06x faster                                                        |
| meteor_contest          | 74.7 ms                                                     | 70.4 ms: 1.06x faster                                                       |
| docutils                | 1.60 sec                                                    | 1.51 sec: 1.06x faster                                                      |
| tornado_http            | 91.8 ms                                                     | 86.7 ms: 1.06x faster                                                       |
| async_tree_cpu_io_mixed | 501 ms                                                      | 473 ms: 1.06x faster                                                        |
| dulwich_log             | 44.5 ms                                                     | 42.1 ms: 1.06x faster                                                       |
| xml_etree_iterparse     | 62.6 ms                                                     | 59.2 ms: 1.06x faster                                                       |
| html5lib                | 37.5 ms                                                     | 35.5 ms: 1.06x faster                                                       |
| coroutines              | 14.6 ms                                                     | 13.9 ms: 1.05x faster                                                       |
| sympy_sum               | 99.9 ms                                                     | 95.6 ms: 1.04x faster                                                       |
| xml_etree_generate      | 52.2 ms                                                     | 50.0 ms: 1.04x faster                                                       |
| bench_thread_pool       | 852 us                                                      | 818 us: 1.04x faster                                                        |
| python_startup_no_site  | 15.9 ms                                                     | 15.3 ms: 1.04x faster                                                       |
| python_startup          | 18.7 ms                                                     | 18.2 ms: 1.03x faster                                                       |
| unpickle                | 8.09 us                                                     | 7.96 us: 1.02x faster                                                       |
| pidigits                | 148 ms                                                      | 146 ms: 1.02x faster                                                        |
| telco                   | 3.90 ms                                                     | 3.85 ms: 1.02x faster                                                       |
| gc_traversal            | 1.46 ms                                                     | 1.47 ms: 1.01x slower                                                       |
| pickle_list             | 2.68 us                                                     | 2.78 us: 1.04x slower                                                       |
| bench_mp_pool           | 62.5 ms                                                     | 64.8 ms: 1.04x slower                                                       |
| json_loads              | 12.9 us                                                     | 13.4 us: 1.04x slower                                                       |
| sqlite_synth            | 1.68 us                                                     | 1.76 us: 1.05x slower                                                       |
| regex_dna               | 115 ms                                                      | 122 ms: 1.06x slower                                                        |
| unpickle_list           | 2.55 us                                                     | 2.70 us: 1.06x slower                                                       |
| async_generators        | 178 ms                                                      | 202 ms: 1.14x slower                                                        |
| pathlib                 | 71.4 ms                                                     | 82.2 ms: 1.15x slower                                                       |
| regex_effbot            | 1.50 ms                                                     | 1.83 ms: 1.23x slower                                                       |
| dask                    | 264 ms                                                      | 353 ms: 1.33x slower                                                        |
| Geometric mean          | (ref)                                                       | 1.11x faster                                                                |

Benchmark hidden because not significant (4): regex_v8, pickle_dict, pickle, create_gc_cycles
Ignored benchmarks (9) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.07x
