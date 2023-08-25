
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: 2d526cd
- commit date: 2023-05-01
- overall geometric mean: 1.17x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230501-pythonperf1-amd64-python-main-3.12.0a7+-2d526cd |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 207 ms: 1.14x faster                                        |
| docutils       | 1.89 sec                                                    | 1.60 sec: 1.19x faster                                      |
| html5lib       | 46.5 ms                                                     | 36.1 ms: 1.29x faster                                       |
| tornado_http   | 109 ms                                                      | 87.3 ms: 1.25x faster                                       |
| Geometric mean | (ref)                                                       | 1.21x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230501-pythonperf1-amd64-python-main-3.12.0a7+-2d526cd |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 60.2 ms                                                     | 52.2 ms: 1.15x faster                                       |
| nbody          | 69.3 ms                                                     | 67.3 ms: 1.03x faster                                       |
| pidigits       | 145 ms                                                      | 148 ms: 1.02x slower                                        |
| Geometric mean | (ref)                                                       | 1.05x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230501-pythonperf1-amd64-python-main-3.12.0a7+-2d526cd |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 85.6 ms: 1.21x faster                                       |
| regex_dna      | 132 ms                                                      | 117 ms: 1.13x faster                                        |
| regex_v8       | 15.0 ms                                                     | 13.6 ms: 1.11x faster                                       |
| regex_effbot   | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                       |
| Geometric mean | (ref)                                                       | 1.12x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230501-pythonperf1-amd64-python-main-3.12.0a7+-2d526cd |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.55 ms: 1.53x faster                                       |
| pickle_pure_python   | 257 us                                                      | 191 us: 1.34x faster                                        |
| unpickle_pure_python | 171 us                                                      | 135 us: 1.27x faster                                        |
| xml_etree_process    | 43.4 ms                                                     | 37.8 ms: 1.15x faster                                       |
| xml_etree_parse      | 102 ms                                                      | 91.5 ms: 1.11x faster                                       |
| json_loads           | 14.2 us                                                     | 13.3 us: 1.06x faster                                       |
| unpickle             | 9.17 us                                                     | 8.73 us: 1.05x faster                                       |
| xml_etree_iterparse  | 63.5 ms                                                     | 61.3 ms: 1.04x faster                                       |
| pickle               | 6.80 us                                                     | 7.02 us: 1.03x slower                                       |
| pickle_dict          | 16.9 us                                                     | 18.1 us: 1.07x slower                                       |
| pickle_list          | 2.59 us                                                     | 2.85 us: 1.10x slower                                       |
| Geometric mean       | (ref)                                                       | 1.09x faster                                                |

Benchmark hidden because not significant (2): unpickle_list, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230501-pythonperf1-amd64-python-main-3.12.0a7+-2d526cd |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup | 20.0 ms                                                     | 18.3 ms: 1.09x faster                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230501-pythonperf1-amd64-python-main-3.12.0a7+-2d526cd |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| mako           | 8.80 ms                                                     | 6.67 ms: 1.32x faster                                       |
| genshi_text    | 19.0 ms                                                     | 14.9 ms: 1.27x faster                                       |
| genshi_xml     | 40.5 ms                                                     | 32.5 ms: 1.25x faster                                       |
| Geometric mean | (ref)                                                       | 1.28x faster                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230501-pythonperf1-amd64-python-main-3.12.0a7+-2d526cd |
|-------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 2.12 ms: 1.97x faster                                       |
| mypy2                   | 352 ms                                                      | 215 ms: 1.64x faster                                        |
| richards                | 41.2 ms                                                     | 25.6 ms: 1.61x faster                                       |
| logging_silent          | 96.4 ns                                                     | 60.2 ns: 1.60x faster                                       |
| go                      | 136 ms                                                      | 86.6 ms: 1.57x faster                                       |
| sqlglot_parse           | 1.22 ms                                                     | 791 us: 1.54x faster                                        |
| asyncio_tcp             | 712 ms                                                      | 463 ms: 1.54x faster                                        |
| json_dumps              | 8.50 ms                                                     | 5.55 ms: 1.53x faster                                       |
| scimark_lu              | 85.4 ms                                                     | 56.8 ms: 1.51x faster                                       |
| async_tree_io           | 1.07 sec                                                    | 724 ms: 1.47x faster                                        |
| generators              | 31.6 ms                                                     | 21.6 ms: 1.47x faster                                       |
| sqlglot_transpile       | 1.46 ms                                                     | 1.01 ms: 1.45x faster                                       |
| async_tree_memoization  | 497 ms                                                      | 350 ms: 1.42x faster                                        |
| raytrace                | 271 ms                                                      | 191 ms: 1.42x faster                                        |
| async_tree_none         | 420 ms                                                      | 297 ms: 1.41x faster                                        |
| hexiom                  | 5.52 ms                                                     | 4.06 ms: 1.36x faster                                       |
| pickle_pure_python      | 257 us                                                      | 191 us: 1.34x faster                                        |
| scimark_sor             | 105 ms                                                      | 79.1 ms: 1.33x faster                                       |
| chaos                   | 58.9 ms                                                     | 44.6 ms: 1.32x faster                                       |
| mako                    | 8.80 ms                                                     | 6.67 ms: 1.32x faster                                       |
| pyflate                 | 387 ms                                                      | 295 ms: 1.31x faster                                        |
| pycparser               | 868 ms                                                      | 665 ms: 1.30x faster                                        |
| crypto_pyaes            | 62.3 ms                                                     | 48.1 ms: 1.30x faster                                       |
| async_tree_cpu_io_mixed | 609 ms                                                      | 473 ms: 1.29x faster                                        |
| html5lib                | 46.5 ms                                                     | 36.1 ms: 1.29x faster                                       |
| genshi_text             | 19.0 ms                                                     | 14.9 ms: 1.27x faster                                       |
| unpickle_pure_python    | 171 us                                                      | 135 us: 1.27x faster                                        |
| tornado_http            | 109 ms                                                      | 87.3 ms: 1.25x faster                                       |
| genshi_xml              | 40.5 ms                                                     | 32.5 ms: 1.25x faster                                       |
| scimark_monte_carlo     | 55.9 ms                                                     | 45.1 ms: 1.24x faster                                       |
| thrift                  | 615 us                                                      | 508 us: 1.21x faster                                        |
| regex_compile           | 103 ms                                                      | 85.6 ms: 1.21x faster                                       |
| mdp                     | 1.71 sec                                                    | 1.43 sec: 1.20x faster                                      |
| deepcopy_memo           | 28.5 us                                                     | 23.9 us: 1.19x faster                                       |
| spectral_norm           | 78.0 ms                                                     | 65.4 ms: 1.19x faster                                       |
| docutils                | 1.89 sec                                                    | 1.60 sec: 1.19x faster                                      |
| pprint_pformat          | 1.21 sec                                                    | 1.02 sec: 1.18x faster                                      |
| pprint_safe_repr        | 589 ms                                                      | 505 ms: 1.17x faster                                        |
| create_gc_cycles        | 782 us                                                      | 675 us: 1.16x faster                                        |
| float                   | 60.2 ms                                                     | 52.2 ms: 1.15x faster                                       |
| sqlglot_optimize        | 39.0 ms                                                     | 33.8 ms: 1.15x faster                                       |
| xml_etree_process       | 43.4 ms                                                     | 37.8 ms: 1.15x faster                                       |
| bench_thread_pool       | 946 us                                                      | 827 us: 1.14x faster                                        |
| 2to3                    | 237 ms                                                      | 207 ms: 1.14x faster                                        |
| regex_dna               | 132 ms                                                      | 117 ms: 1.13x faster                                        |
| coroutines              | 15.9 ms                                                     | 14.2 ms: 1.12x faster                                       |
| dulwich_log             | 47.6 ms                                                     | 42.7 ms: 1.12x faster                                       |
| xml_etree_parse         | 102 ms                                                      | 91.5 ms: 1.11x faster                                       |
| regex_v8                | 15.0 ms                                                     | 13.6 ms: 1.11x faster                                       |
| nqueens                 | 67.0 ms                                                     | 60.6 ms: 1.11x faster                                       |
| python_startup          | 20.0 ms                                                     | 18.3 ms: 1.09x faster                                       |
| deepcopy                | 255 us                                                      | 233 us: 1.09x faster                                        |
| sqlglot_normalize       | 202 ms                                                      | 185 ms: 1.09x faster                                        |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.45 ms: 1.09x faster                                       |
| scimark_fft             | 193 ms                                                      | 179 ms: 1.08x faster                                        |
| sqlite_synth            | 1.84 us                                                     | 1.71 us: 1.07x faster                                       |
| fannkuch                | 258 ms                                                      | 240 ms: 1.07x faster                                        |
| json_loads              | 14.2 us                                                     | 13.3 us: 1.06x faster                                       |
| regex_effbot            | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                       |
| unpickle                | 9.17 us                                                     | 8.73 us: 1.05x faster                                       |
| deepcopy_reduce         | 2.16 us                                                     | 2.07 us: 1.04x faster                                       |
| xml_etree_iterparse     | 63.5 ms                                                     | 61.3 ms: 1.04x faster                                       |
| nbody                   | 69.3 ms                                                     | 67.3 ms: 1.03x faster                                       |
| comprehensions          | 16.0 us                                                     | 15.7 us: 1.02x faster                                       |
| json                    | 3.05 ms                                                     | 3.02 ms: 1.01x faster                                       |
| async_generators        | 224 ms                                                      | 227 ms: 1.02x slower                                        |
| pidigits                | 145 ms                                                      | 148 ms: 1.02x slower                                        |
| unpack_sequence         | 37.8 ns                                                     | 38.7 ns: 1.02x slower                                       |
| pickle                  | 6.80 us                                                     | 7.02 us: 1.03x slower                                       |
| logging_format          | 6.66 us                                                     | 6.89 us: 1.03x slower                                       |
| logging_simple          | 6.20 us                                                     | 6.52 us: 1.05x slower                                       |
| meteor_contest          | 72.5 ms                                                     | 77.0 ms: 1.06x slower                                       |
| pickle_dict             | 16.9 us                                                     | 18.1 us: 1.07x slower                                       |
| pathlib                 | 77.4 ms                                                     | 83.1 ms: 1.07x slower                                       |
| telco                   | 3.78 ms                                                     | 4.07 ms: 1.08x slower                                       |
| gc_traversal            | 1.34 ms                                                     | 1.46 ms: 1.09x slower                                       |
| pickle_list             | 2.59 us                                                     | 2.85 us: 1.10x slower                                       |
| bench_mp_pool           | 60.7 ms                                                     | 67.2 ms: 1.11x slower                                       |
| dask                    | 305 ms                                                      | 360 ms: 1.18x slower                                        |
| coverage                | 40.0 ms                                                     | 52.3 ms: 1.31x slower                                       |
| Geometric mean          | (ref)                                                       | 1.17x faster                                                |

Benchmark hidden because not significant (3): python_startup_no_site, unpickle_list, xml_etree_generate
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x
