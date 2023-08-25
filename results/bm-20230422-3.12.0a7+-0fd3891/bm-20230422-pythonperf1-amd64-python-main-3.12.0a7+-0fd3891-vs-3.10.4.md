
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: 0fd3891
- commit date: 2023-04-22
- overall geometric mean: 1.19x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230422-pythonperf1-amd64-python-main-3.12.0a7+-0fd3891 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 207 ms: 1.14x faster                                        |
| chameleon      | 5.92 ms                                                     | 4.93 ms: 1.20x faster                                       |
| docutils       | 1.89 sec                                                    | 1.54 sec: 1.23x faster                                      |
| html5lib       | 46.5 ms                                                     | 36.6 ms: 1.27x faster                                       |
| tornado_http   | 109 ms                                                      | 90.0 ms: 1.21x faster                                       |
| Geometric mean | (ref)                                                       | 1.21x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230422-pythonperf1-amd64-python-main-3.12.0a7+-0fd3891 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 60.2 ms                                                     | 51.4 ms: 1.17x faster                                       |
| pidigits       | 145 ms                                                      | 148 ms: 1.02x slower                                        |
| nbody          | 69.3 ms                                                     | 73.1 ms: 1.05x slower                                       |
| Geometric mean | (ref)                                                       | 1.03x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230422-pythonperf1-amd64-python-main-3.12.0a7+-0fd3891 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 83.8 ms: 1.23x faster                                       |
| regex_v8       | 15.0 ms                                                     | 13.0 ms: 1.15x faster                                       |
| regex_dna      | 132 ms                                                      | 115 ms: 1.15x faster                                        |
| regex_effbot   | 1.66 ms                                                     | 1.51 ms: 1.10x faster                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230422-pythonperf1-amd64-python-main-3.12.0a7+-0fd3891 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.41 ms: 1.57x faster                                       |
| pickle_pure_python   | 257 us                                                      | 189 us: 1.36x faster                                        |
| unpickle_pure_python | 171 us                                                      | 135 us: 1.27x faster                                        |
| xml_etree_parse      | 102 ms                                                      | 87.5 ms: 1.16x faster                                       |
| xml_etree_process    | 43.4 ms                                                     | 37.4 ms: 1.16x faster                                       |
| json_loads           | 14.2 us                                                     | 12.8 us: 1.11x faster                                       |
| unpickle             | 9.17 us                                                     | 8.46 us: 1.08x faster                                       |
| unpickle_list        | 2.81 us                                                     | 2.63 us: 1.07x faster                                       |
| xml_etree_iterparse  | 63.5 ms                                                     | 60.0 ms: 1.06x faster                                       |
| pickle               | 6.80 us                                                     | 6.77 us: 1.00x faster                                       |
| pickle_dict          | 16.9 us                                                     | 18.2 us: 1.07x slower                                       |
| pickle_list          | 2.59 us                                                     | 2.81 us: 1.08x slower                                       |
| Geometric mean       | (ref)                                                       | 1.12x faster                                                |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230422-pythonperf1-amd64-python-main-3.12.0a7+-0fd3891 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup | 20.0 ms                                                     | 18.2 ms: 1.10x faster                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230422-pythonperf1-amd64-python-main-3.12.0a7+-0fd3891 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| mako            | 8.80 ms                                                     | 6.66 ms: 1.32x faster                                       |
| django_template | 28.2 ms                                                     | 21.8 ms: 1.29x faster                                       |
| genshi_text     | 19.0 ms                                                     | 15.1 ms: 1.26x faster                                       |
| genshi_xml      | 40.5 ms                                                     | 32.5 ms: 1.25x faster                                       |
| Geometric mean  | (ref)                                                       | 1.28x faster                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230422-pythonperf1-amd64-python-main-3.12.0a7+-0fd3891 |
|-------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 2.16 ms: 1.93x faster                                       |
| mypy2                   | 352 ms                                                      | 215 ms: 1.63x faster                                        |
| logging_silent          | 96.4 ns                                                     | 59.5 ns: 1.62x faster                                       |
| scimark_lu              | 85.4 ms                                                     | 54.2 ms: 1.58x faster                                       |
| json_dumps              | 8.50 ms                                                     | 5.41 ms: 1.57x faster                                       |
| go                      | 136 ms                                                      | 87.4 ms: 1.56x faster                                       |
| sqlglot_parse           | 1.22 ms                                                     | 789 us: 1.55x faster                                        |
| richards                | 41.2 ms                                                     | 27.1 ms: 1.52x faster                                       |
| asyncio_tcp             | 712 ms                                                      | 470 ms: 1.51x faster                                        |
| sqlglot_transpile       | 1.46 ms                                                     | 991 us: 1.48x faster                                        |
| raytrace                | 271 ms                                                      | 185 ms: 1.46x faster                                        |
| generators              | 31.6 ms                                                     | 21.7 ms: 1.46x faster                                       |
| async_tree_io           | 1.07 sec                                                    | 748 ms: 1.42x faster                                        |
| async_tree_none         | 420 ms                                                      | 298 ms: 1.41x faster                                        |
| async_tree_memoization  | 497 ms                                                      | 357 ms: 1.39x faster                                        |
| chaos                   | 58.9 ms                                                     | 43.3 ms: 1.36x faster                                       |
| pickle_pure_python      | 257 us                                                      | 189 us: 1.36x faster                                        |
| pyflate                 | 387 ms                                                      | 286 ms: 1.35x faster                                        |
| hexiom                  | 5.52 ms                                                     | 4.10 ms: 1.34x faster                                       |
| crypto_pyaes            | 62.3 ms                                                     | 46.4 ms: 1.34x faster                                       |
| mako                    | 8.80 ms                                                     | 6.66 ms: 1.32x faster                                       |
| pycparser               | 868 ms                                                      | 658 ms: 1.32x faster                                        |
| scimark_monte_carlo     | 55.9 ms                                                     | 42.7 ms: 1.31x faster                                       |
| thrift                  | 615 us                                                      | 474 us: 1.30x faster                                        |
| scimark_sor             | 105 ms                                                      | 80.8 ms: 1.30x faster                                       |
| django_template         | 28.2 ms                                                     | 21.8 ms: 1.29x faster                                       |
| async_tree_cpu_io_mixed | 609 ms                                                      | 474 ms: 1.28x faster                                        |
| unpickle_pure_python    | 171 us                                                      | 135 us: 1.27x faster                                        |
| html5lib                | 46.5 ms                                                     | 36.6 ms: 1.27x faster                                       |
| spectral_norm           | 78.0 ms                                                     | 61.6 ms: 1.27x faster                                       |
| genshi_text             | 19.0 ms                                                     | 15.1 ms: 1.26x faster                                       |
| pylint                  | 347 ms                                                      | 276 ms: 1.25x faster                                        |
| genshi_xml              | 40.5 ms                                                     | 32.5 ms: 1.25x faster                                       |
| deepcopy_memo           | 28.5 us                                                     | 23.0 us: 1.24x faster                                       |
| regex_compile           | 103 ms                                                      | 83.8 ms: 1.23x faster                                       |
| docutils                | 1.89 sec                                                    | 1.54 sec: 1.23x faster                                      |
| tornado_http            | 109 ms                                                      | 90.0 ms: 1.21x faster                                       |
| pprint_pformat          | 1.21 sec                                                    | 995 ms: 1.21x faster                                        |
| chameleon               | 5.92 ms                                                     | 4.93 ms: 1.20x faster                                       |
| pprint_safe_repr        | 589 ms                                                      | 491 ms: 1.20x faster                                        |
| sqlglot_optimize        | 39.0 ms                                                     | 32.6 ms: 1.19x faster                                       |
| mdp                     | 1.71 sec                                                    | 1.44 sec: 1.19x faster                                      |
| float                   | 60.2 ms                                                     | 51.4 ms: 1.17x faster                                       |
| nqueens                 | 67.0 ms                                                     | 57.3 ms: 1.17x faster                                       |
| bench_thread_pool       | 946 us                                                      | 813 us: 1.16x faster                                        |
| xml_etree_parse         | 102 ms                                                      | 87.5 ms: 1.16x faster                                       |
| xml_etree_process       | 43.4 ms                                                     | 37.4 ms: 1.16x faster                                       |
| coroutines              | 15.9 ms                                                     | 13.8 ms: 1.16x faster                                       |
| create_gc_cycles        | 782 us                                                      | 677 us: 1.16x faster                                        |
| regex_v8                | 15.0 ms                                                     | 13.0 ms: 1.15x faster                                       |
| dulwich_log             | 47.6 ms                                                     | 41.3 ms: 1.15x faster                                       |
| sqlglot_normalize       | 202 ms                                                      | 176 ms: 1.15x faster                                        |
| regex_dna               | 132 ms                                                      | 115 ms: 1.15x faster                                        |
| 2to3                    | 237 ms                                                      | 207 ms: 1.14x faster                                        |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.33 ms: 1.14x faster                                       |
| sympy_expand            | 315 ms                                                      | 278 ms: 1.13x faster                                        |
| deepcopy                | 255 us                                                      | 227 us: 1.12x faster                                        |
| sympy_integrate         | 14.8 ms                                                     | 13.2 ms: 1.12x faster                                       |
| scimark_fft             | 193 ms                                                      | 172 ms: 1.12x faster                                        |
| json_loads              | 14.2 us                                                     | 12.8 us: 1.11x faster                                       |
| sympy_str               | 188 ms                                                      | 171 ms: 1.10x faster                                        |
| regex_effbot            | 1.66 ms                                                     | 1.51 ms: 1.10x faster                                       |
| python_startup          | 20.0 ms                                                     | 18.2 ms: 1.10x faster                                       |
| deepcopy_reduce         | 2.16 us                                                     | 1.97 us: 1.10x faster                                       |
| unpickle                | 9.17 us                                                     | 8.46 us: 1.08x faster                                       |
| sympy_sum               | 104 ms                                                      | 96.1 ms: 1.08x faster                                       |
| json                    | 3.05 ms                                                     | 2.82 ms: 1.08x faster                                       |
| unpickle_list           | 2.81 us                                                     | 2.63 us: 1.07x faster                                       |
| comprehensions          | 16.0 us                                                     | 15.0 us: 1.07x faster                                       |
| fannkuch                | 258 ms                                                      | 243 ms: 1.06x faster                                        |
| xml_etree_iterparse     | 63.5 ms                                                     | 60.0 ms: 1.06x faster                                       |
| async_generators        | 224 ms                                                      | 216 ms: 1.04x faster                                        |
| sqlite_synth            | 1.84 us                                                     | 1.81 us: 1.02x faster                                       |
| unpack_sequence         | 37.8 ns                                                     | 37.4 ns: 1.01x faster                                       |
| pickle                  | 6.80 us                                                     | 6.77 us: 1.00x faster                                       |
| telco                   | 3.78 ms                                                     | 3.80 ms: 1.00x slower                                       |
| logging_simple          | 6.20 us                                                     | 6.25 us: 1.01x slower                                       |
| pidigits                | 145 ms                                                      | 148 ms: 1.02x slower                                        |
| nbody                   | 69.3 ms                                                     | 73.1 ms: 1.05x slower                                       |
| pathlib                 | 77.4 ms                                                     | 82.4 ms: 1.06x slower                                       |
| pickle_dict             | 16.9 us                                                     | 18.2 us: 1.07x slower                                       |
| meteor_contest          | 72.5 ms                                                     | 77.8 ms: 1.07x slower                                       |
| pickle_list             | 2.59 us                                                     | 2.81 us: 1.08x slower                                       |
| gc_traversal            | 1.34 ms                                                     | 1.47 ms: 1.09x slower                                       |
| bench_mp_pool           | 60.7 ms                                                     | 66.7 ms: 1.10x slower                                       |
| dask                    | 305 ms                                                      | 357 ms: 1.17x slower                                        |
| coverage                | 40.0 ms                                                     | 50.5 ms: 1.26x slower                                       |
| Geometric mean          | (ref)                                                       | 1.19x faster                                                |

Benchmark hidden because not significant (3): python_startup_no_site, xml_etree_generate, logging_format
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.15x
