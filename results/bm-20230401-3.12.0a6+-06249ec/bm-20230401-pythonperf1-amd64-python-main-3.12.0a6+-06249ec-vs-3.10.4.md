
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: 06249ec
- commit date: 2023-04-01
- overall geometric mean: 1.20x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-pythonperf1-amd64-python-main-3.12.0a6+-06249ec |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 208 ms: 1.14x faster                                        |
| chameleon      | 5.92 ms                                                     | 4.75 ms: 1.25x faster                                       |
| docutils       | 1.89 sec                                                    | 1.55 sec: 1.22x faster                                      |
| html5lib       | 46.5 ms                                                     | 36.4 ms: 1.28x faster                                       |
| tornado_http   | 109 ms                                                      | 88.0 ms: 1.24x faster                                       |
| Geometric mean | (ref)                                                       | 1.23x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-pythonperf1-amd64-python-main-3.12.0a6+-06249ec |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 60.2 ms                                                     | 50.0 ms: 1.20x faster                                       |
| nbody          | 69.3 ms                                                     | 61.6 ms: 1.13x faster                                       |
| pidigits       | 145 ms                                                      | 146 ms: 1.01x slower                                        |
| Geometric mean | (ref)                                                       | 1.10x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-pythonperf1-amd64-python-main-3.12.0a6+-06249ec |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 84.0 ms: 1.23x faster                                       |
| regex_v8       | 15.0 ms                                                     | 13.2 ms: 1.14x faster                                       |
| regex_dna      | 132 ms                                                      | 118 ms: 1.11x faster                                        |
| regex_effbot   | 1.66 ms                                                     | 1.52 ms: 1.09x faster                                       |
| Geometric mean | (ref)                                                       | 1.14x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-pythonperf1-amd64-python-main-3.12.0a6+-06249ec |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.27 ms: 1.61x faster                                       |
| pickle_pure_python   | 257 us                                                      | 185 us: 1.39x faster                                        |
| unpickle_pure_python | 171 us                                                      | 126 us: 1.36x faster                                        |
| xml_etree_process    | 43.4 ms                                                     | 35.9 ms: 1.21x faster                                       |
| unpickle             | 9.17 us                                                     | 8.01 us: 1.14x faster                                       |
| xml_etree_parse      | 102 ms                                                      | 91.4 ms: 1.11x faster                                       |
| xml_etree_iterparse  | 63.5 ms                                                     | 61.3 ms: 1.04x faster                                       |
| json_loads           | 14.2 us                                                     | 13.7 us: 1.03x faster                                       |
| xml_etree_generate   | 54.5 ms                                                     | 52.7 ms: 1.03x faster                                       |
| pickle               | 6.80 us                                                     | 7.08 us: 1.04x slower                                       |
| pickle_list          | 2.59 us                                                     | 2.89 us: 1.12x slower                                       |
| pickle_dict          | 16.9 us                                                     | 19.1 us: 1.13x slower                                       |
| Geometric mean       | (ref)                                                       | 1.11x faster                                                |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-pythonperf1-amd64-python-main-3.12.0a6+-06249ec |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 18.9 ms: 1.06x faster                                       |
| python_startup_no_site | 15.5 ms                                                     | 15.7 ms: 1.01x slower                                       |
| Geometric mean         | (ref)                                                       | 1.02x faster                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-pythonperf1-amd64-python-main-3.12.0a6+-06249ec |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| mako            | 8.80 ms                                                     | 6.19 ms: 1.42x faster                                       |
| genshi_text     | 19.0 ms                                                     | 14.0 ms: 1.37x faster                                       |
| django_template | 28.2 ms                                                     | 21.4 ms: 1.32x faster                                       |
| genshi_xml      | 40.5 ms                                                     | 30.7 ms: 1.32x faster                                       |
| Geometric mean  | (ref)                                                       | 1.36x faster                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-pythonperf1-amd64-python-main-3.12.0a6+-06249ec |
|-------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 1.95 ms: 2.14x faster                                       |
| logging_silent          | 96.4 ns                                                     | 54.3 ns: 1.78x faster                                       |
| go                      | 136 ms                                                      | 81.9 ms: 1.66x faster                                       |
| scimark_lu              | 85.4 ms                                                     | 52.6 ms: 1.63x faster                                       |
| richards                | 41.2 ms                                                     | 25.5 ms: 1.62x faster                                       |
| json_dumps              | 8.50 ms                                                     | 5.27 ms: 1.61x faster                                       |
| mypy2                   | 352 ms                                                      | 220 ms: 1.60x faster                                        |
| raytrace                | 271 ms                                                      | 174 ms: 1.56x faster                                        |
| generators              | 31.6 ms                                                     | 21.2 ms: 1.49x faster                                       |
| asyncio_tcp             | 712 ms                                                      | 495 ms: 1.44x faster                                        |
| mako                    | 8.80 ms                                                     | 6.19 ms: 1.42x faster                                       |
| chaos                   | 58.9 ms                                                     | 41.5 ms: 1.42x faster                                       |
| hexiom                  | 5.52 ms                                                     | 3.90 ms: 1.42x faster                                       |
| sqlglot_parse           | 1.22 ms                                                     | 869 us: 1.40x faster                                        |
| scimark_monte_carlo     | 55.9 ms                                                     | 39.9 ms: 1.40x faster                                       |
| pickle_pure_python      | 257 us                                                      | 185 us: 1.39x faster                                        |
| crypto_pyaes            | 62.3 ms                                                     | 44.9 ms: 1.39x faster                                       |
| async_tree_io           | 1.07 sec                                                    | 773 ms: 1.38x faster                                        |
| scimark_sor             | 105 ms                                                      | 76.7 ms: 1.37x faster                                       |
| genshi_text             | 19.0 ms                                                     | 14.0 ms: 1.37x faster                                       |
| spectral_norm           | 78.0 ms                                                     | 57.2 ms: 1.36x faster                                       |
| sqlglot_transpile       | 1.46 ms                                                     | 1.07 ms: 1.36x faster                                       |
| unpickle_pure_python    | 171 us                                                      | 126 us: 1.36x faster                                        |
| pyflate                 | 387 ms                                                      | 286 ms: 1.35x faster                                        |
| async_tree_memoization  | 497 ms                                                      | 369 ms: 1.35x faster                                        |
| unpack_sequence         | 37.8 ns                                                     | 28.1 ns: 1.34x faster                                       |
| deepcopy_memo           | 28.5 us                                                     | 21.6 us: 1.32x faster                                       |
| django_template         | 28.2 ms                                                     | 21.4 ms: 1.32x faster                                       |
| async_tree_none         | 420 ms                                                      | 318 ms: 1.32x faster                                        |
| genshi_xml              | 40.5 ms                                                     | 30.7 ms: 1.32x faster                                       |
| pycparser               | 868 ms                                                      | 672 ms: 1.29x faster                                        |
| html5lib                | 46.5 ms                                                     | 36.4 ms: 1.28x faster                                       |
| async_tree_cpu_io_mixed | 609 ms                                                      | 480 ms: 1.27x faster                                        |
| thrift                  | 615 us                                                      | 487 us: 1.26x faster                                        |
| pprint_pformat          | 1.21 sec                                                    | 966 ms: 1.25x faster                                        |
| chameleon               | 5.92 ms                                                     | 4.75 ms: 1.25x faster                                       |
| tornado_http            | 109 ms                                                      | 88.0 ms: 1.24x faster                                       |
| pprint_safe_repr        | 589 ms                                                      | 477 ms: 1.24x faster                                        |
| regex_compile           | 103 ms                                                      | 84.0 ms: 1.23x faster                                       |
| sqlglot_optimize        | 39.0 ms                                                     | 31.7 ms: 1.23x faster                                       |
| docutils                | 1.89 sec                                                    | 1.55 sec: 1.22x faster                                      |
| xml_etree_process       | 43.4 ms                                                     | 35.9 ms: 1.21x faster                                       |
| float                   | 60.2 ms                                                     | 50.0 ms: 1.20x faster                                       |
| mdp                     | 1.71 sec                                                    | 1.43 sec: 1.20x faster                                      |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.24 ms: 1.19x faster                                       |
| deepcopy                | 255 us                                                      | 218 us: 1.17x faster                                        |
| sqlglot_normalize       | 202 ms                                                      | 173 ms: 1.17x faster                                        |
| scimark_fft             | 193 ms                                                      | 165 ms: 1.17x faster                                        |
| nqueens                 | 67.0 ms                                                     | 57.4 ms: 1.17x faster                                       |
| coroutines              | 15.9 ms                                                     | 13.8 ms: 1.16x faster                                       |
| sympy_integrate         | 14.8 ms                                                     | 12.9 ms: 1.15x faster                                       |
| unpickle                | 9.17 us                                                     | 8.01 us: 1.14x faster                                       |
| 2to3                    | 237 ms                                                      | 208 ms: 1.14x faster                                        |
| regex_v8                | 15.0 ms                                                     | 13.2 ms: 1.14x faster                                       |
| sympy_expand            | 315 ms                                                      | 278 ms: 1.13x faster                                        |
| deepcopy_reduce         | 2.16 us                                                     | 1.91 us: 1.13x faster                                       |
| dulwich_log             | 47.6 ms                                                     | 42.3 ms: 1.13x faster                                       |
| create_gc_cycles        | 782 us                                                      | 695 us: 1.13x faster                                        |
| nbody                   | 69.3 ms                                                     | 61.6 ms: 1.13x faster                                       |
| bench_thread_pool       | 946 us                                                      | 845 us: 1.12x faster                                        |
| regex_dna               | 132 ms                                                      | 118 ms: 1.11x faster                                        |
| xml_etree_parse         | 102 ms                                                      | 91.4 ms: 1.11x faster                                       |
| fannkuch                | 258 ms                                                      | 232 ms: 1.11x faster                                        |
| json                    | 3.05 ms                                                     | 2.77 ms: 1.10x faster                                       |
| regex_effbot            | 1.66 ms                                                     | 1.52 ms: 1.09x faster                                       |
| sympy_str               | 188 ms                                                      | 177 ms: 1.06x faster                                        |
| python_startup          | 20.0 ms                                                     | 18.9 ms: 1.06x faster                                       |
| comprehensions          | 16.0 us                                                     | 15.2 us: 1.05x faster                                       |
| sympy_sum               | 104 ms                                                      | 99.7 ms: 1.04x faster                                       |
| async_generators        | 224 ms                                                      | 215 ms: 1.04x faster                                        |
| xml_etree_iterparse     | 63.5 ms                                                     | 61.3 ms: 1.04x faster                                       |
| json_loads              | 14.2 us                                                     | 13.7 us: 1.03x faster                                       |
| xml_etree_generate      | 54.5 ms                                                     | 52.7 ms: 1.03x faster                                       |
| meteor_contest          | 72.5 ms                                                     | 71.4 ms: 1.02x faster                                       |
| logging_simple          | 6.20 us                                                     | 6.11 us: 1.01x faster                                       |
| pidigits                | 145 ms                                                      | 146 ms: 1.01x slower                                        |
| python_startup_no_site  | 15.5 ms                                                     | 15.7 ms: 1.01x slower                                       |
| sqlite_synth            | 1.84 us                                                     | 1.87 us: 1.02x slower                                       |
| telco                   | 3.78 ms                                                     | 3.91 ms: 1.03x slower                                       |
| pickle                  | 6.80 us                                                     | 7.08 us: 1.04x slower                                       |
| bench_mp_pool           | 60.7 ms                                                     | 67.0 ms: 1.10x slower                                       |
| pathlib                 | 77.4 ms                                                     | 86.3 ms: 1.11x slower                                       |
| pickle_list             | 2.59 us                                                     | 2.89 us: 1.12x slower                                       |
| gc_traversal            | 1.34 ms                                                     | 1.51 ms: 1.12x slower                                       |
| pickle_dict             | 16.9 us                                                     | 19.1 us: 1.13x slower                                       |
| dask                    | 305 ms                                                      | 362 ms: 1.19x slower                                        |
| coverage                | 40.0 ms                                                     | 52.8 ms: 1.32x slower                                       |
| Geometric mean          | (ref)                                                       | 1.20x faster                                                |

Benchmark hidden because not significant (2): logging_format, unpickle_list
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.15x
