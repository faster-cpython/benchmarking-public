
# Results vs. 3.10.4

- fork: python
- ref: 52bc2e7b9d451821513a
- machine: windows-amd64
- commit hash: 52bc2e7
- commit date: 2023-04-06
- overall geometric mean: 1.21x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-pythonperf1-amd64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 202 ms: 1.17x faster                                                        |
| chameleon      | 5.92 ms                                                     | 4.75 ms: 1.25x faster                                                       |
| docutils       | 1.89 sec                                                    | 1.57 sec: 1.20x faster                                                      |
| html5lib       | 46.5 ms                                                     | 36.4 ms: 1.28x faster                                                       |
| tornado_http   | 109 ms                                                      | 86.4 ms: 1.26x faster                                                       |
| Geometric mean | (ref)                                                       | 1.23x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-pythonperf1-amd64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 48.6 ms: 1.24x faster                                                       |
| nbody          | 69.3 ms                                                     | 57.8 ms: 1.20x faster                                                       |
| pidigits       | 145 ms                                                      | 148 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-pythonperf1-amd64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 82.3 ms: 1.26x faster                                                       |
| regex_dna      | 132 ms                                                      | 117 ms: 1.13x faster                                                        |
| regex_v8       | 15.0 ms                                                     | 13.8 ms: 1.09x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.56 ms: 1.07x faster                                                       |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-pythonperf1-amd64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.36 ms: 1.59x faster                                                       |
| pickle_pure_python   | 257 us                                                      | 176 us: 1.46x faster                                                        |
| unpickle_pure_python | 171 us                                                      | 129 us: 1.33x faster                                                        |
| xml_etree_process    | 43.4 ms                                                     | 36.8 ms: 1.18x faster                                                       |
| unpickle             | 9.17 us                                                     | 8.10 us: 1.13x faster                                                       |
| xml_etree_parse      | 102 ms                                                      | 90.9 ms: 1.12x faster                                                       |
| json_loads           | 14.2 us                                                     | 12.8 us: 1.11x faster                                                       |
| xml_etree_generate   | 54.5 ms                                                     | 51.9 ms: 1.05x faster                                                       |
| xml_etree_iterparse  | 63.5 ms                                                     | 60.9 ms: 1.04x faster                                                       |
| pickle               | 6.80 us                                                     | 6.97 us: 1.02x slower                                                       |
| pickle_list          | 2.59 us                                                     | 2.78 us: 1.07x slower                                                       |
| pickle_dict          | 16.9 us                                                     | 19.1 us: 1.13x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.12x faster                                                                |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-pythonperf1-amd64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 18.9 ms: 1.06x faster                                                       |
| python_startup_no_site | 15.5 ms                                                     | 16.0 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-pythonperf1-amd64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 8.80 ms                                                     | 6.15 ms: 1.43x faster                                                       |
| genshi_text     | 19.0 ms                                                     | 13.7 ms: 1.39x faster                                                       |
| genshi_xml      | 40.5 ms                                                     | 30.8 ms: 1.32x faster                                                       |
| django_template | 28.2 ms                                                     | 21.7 ms: 1.30x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.36x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-pythonperf1-amd64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 1.97 ms: 2.11x faster                                                       |
| logging_silent          | 96.4 ns                                                     | 55.8 ns: 1.73x faster                                                       |
| go                      | 136 ms                                                      | 83.9 ms: 1.62x faster                                                       |
| richards                | 41.2 ms                                                     | 25.5 ms: 1.62x faster                                                       |
| mypy2                   | 352 ms                                                      | 218 ms: 1.61x faster                                                        |
| json_dumps              | 8.50 ms                                                     | 5.36 ms: 1.59x faster                                                       |
| scimark_lu              | 85.4 ms                                                     | 53.9 ms: 1.59x faster                                                       |
| sqlglot_parse           | 1.22 ms                                                     | 773 us: 1.58x faster                                                        |
| raytrace                | 271 ms                                                      | 178 ms: 1.53x faster                                                        |
| sqlglot_transpile       | 1.46 ms                                                     | 964 us: 1.52x faster                                                        |
| generators              | 31.6 ms                                                     | 20.9 ms: 1.51x faster                                                       |
| asyncio_tcp             | 712 ms                                                      | 482 ms: 1.48x faster                                                        |
| pickle_pure_python      | 257 us                                                      | 176 us: 1.46x faster                                                        |
| scimark_sor             | 105 ms                                                      | 73.1 ms: 1.44x faster                                                       |
| hexiom                  | 5.52 ms                                                     | 3.86 ms: 1.43x faster                                                       |
| chaos                   | 58.9 ms                                                     | 41.2 ms: 1.43x faster                                                       |
| mako                    | 8.80 ms                                                     | 6.15 ms: 1.43x faster                                                       |
| async_tree_io           | 1.07 sec                                                    | 762 ms: 1.40x faster                                                        |
| genshi_text             | 19.0 ms                                                     | 13.7 ms: 1.39x faster                                                       |
| async_tree_none         | 420 ms                                                      | 302 ms: 1.39x faster                                                        |
| crypto_pyaes            | 62.3 ms                                                     | 45.0 ms: 1.39x faster                                                       |
| async_tree_memoization  | 497 ms                                                      | 361 ms: 1.38x faster                                                        |
| unpack_sequence         | 37.8 ns                                                     | 27.4 ns: 1.38x faster                                                       |
| pyflate                 | 387 ms                                                      | 285 ms: 1.36x faster                                                        |
| scimark_monte_carlo     | 55.9 ms                                                     | 41.2 ms: 1.35x faster                                                       |
| unpickle_pure_python    | 171 us                                                      | 129 us: 1.33x faster                                                        |
| pycparser               | 868 ms                                                      | 657 ms: 1.32x faster                                                        |
| genshi_xml              | 40.5 ms                                                     | 30.8 ms: 1.32x faster                                                       |
| thrift                  | 615 us                                                      | 469 us: 1.31x faster                                                        |
| spectral_norm           | 78.0 ms                                                     | 59.8 ms: 1.31x faster                                                       |
| django_template         | 28.2 ms                                                     | 21.7 ms: 1.30x faster                                                       |
| deepcopy_memo           | 28.5 us                                                     | 22.2 us: 1.28x faster                                                       |
| html5lib                | 46.5 ms                                                     | 36.4 ms: 1.28x faster                                                       |
| async_tree_cpu_io_mixed | 609 ms                                                      | 482 ms: 1.26x faster                                                        |
| tornado_http            | 109 ms                                                      | 86.4 ms: 1.26x faster                                                       |
| regex_compile           | 103 ms                                                      | 82.3 ms: 1.26x faster                                                       |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.13 ms: 1.25x faster                                                       |
| chameleon               | 5.92 ms                                                     | 4.75 ms: 1.25x faster                                                       |
| mdp                     | 1.71 sec                                                    | 1.37 sec: 1.25x faster                                                      |
| pprint_pformat          | 1.21 sec                                                    | 969 ms: 1.25x faster                                                        |
| sqlglot_optimize        | 39.0 ms                                                     | 31.3 ms: 1.24x faster                                                       |
| float                   | 60.2 ms                                                     | 48.6 ms: 1.24x faster                                                       |
| pprint_safe_repr        | 589 ms                                                      | 478 ms: 1.23x faster                                                        |
| docutils                | 1.89 sec                                                    | 1.57 sec: 1.20x faster                                                      |
| nbody                   | 69.3 ms                                                     | 57.8 ms: 1.20x faster                                                       |
| scimark_fft             | 193 ms                                                      | 162 ms: 1.20x faster                                                        |
| deepcopy                | 255 us                                                      | 215 us: 1.19x faster                                                        |
| sqlglot_normalize       | 202 ms                                                      | 171 ms: 1.18x faster                                                        |
| xml_etree_process       | 43.4 ms                                                     | 36.8 ms: 1.18x faster                                                       |
| 2to3                    | 237 ms                                                      | 202 ms: 1.17x faster                                                        |
| coroutines              | 15.9 ms                                                     | 13.8 ms: 1.16x faster                                                       |
| comprehensions          | 16.0 us                                                     | 13.9 us: 1.15x faster                                                       |
| deepcopy_reduce         | 2.16 us                                                     | 1.90 us: 1.14x faster                                                       |
| unpickle                | 9.17 us                                                     | 8.10 us: 1.13x faster                                                       |
| regex_dna               | 132 ms                                                      | 117 ms: 1.13x faster                                                        |
| sympy_expand            | 315 ms                                                      | 280 ms: 1.13x faster                                                        |
| bench_thread_pool       | 946 us                                                      | 845 us: 1.12x faster                                                        |
| json                    | 3.05 ms                                                     | 2.72 ms: 1.12x faster                                                       |
| xml_etree_parse         | 102 ms                                                      | 90.9 ms: 1.12x faster                                                       |
| dulwich_log             | 47.6 ms                                                     | 42.6 ms: 1.12x faster                                                       |
| create_gc_cycles        | 782 us                                                      | 702 us: 1.11x faster                                                        |
| nqueens                 | 67.0 ms                                                     | 60.3 ms: 1.11x faster                                                       |
| sympy_integrate         | 14.8 ms                                                     | 13.3 ms: 1.11x faster                                                       |
| json_loads              | 14.2 us                                                     | 12.8 us: 1.11x faster                                                       |
| fannkuch                | 258 ms                                                      | 235 ms: 1.10x faster                                                        |
| regex_v8                | 15.0 ms                                                     | 13.8 ms: 1.09x faster                                                       |
| sympy_str               | 188 ms                                                      | 175 ms: 1.08x faster                                                        |
| regex_effbot            | 1.66 ms                                                     | 1.56 ms: 1.07x faster                                                       |
| python_startup          | 20.0 ms                                                     | 18.9 ms: 1.06x faster                                                       |
| sympy_sum               | 104 ms                                                      | 98.5 ms: 1.06x faster                                                       |
| xml_etree_generate      | 54.5 ms                                                     | 51.9 ms: 1.05x faster                                                       |
| async_generators        | 224 ms                                                      | 213 ms: 1.05x faster                                                        |
| xml_etree_iterparse     | 63.5 ms                                                     | 60.9 ms: 1.04x faster                                                       |
| logging_format          | 6.66 us                                                     | 6.52 us: 1.02x faster                                                       |
| meteor_contest          | 72.5 ms                                                     | 72.1 ms: 1.01x faster                                                       |
| pidigits                | 145 ms                                                      | 148 ms: 1.02x slower                                                        |
| pickle                  | 6.80 us                                                     | 6.97 us: 1.02x slower                                                       |
| telco                   | 3.78 ms                                                     | 3.88 ms: 1.03x slower                                                       |
| python_startup_no_site  | 15.5 ms                                                     | 16.0 ms: 1.03x slower                                                       |
| pickle_list             | 2.59 us                                                     | 2.78 us: 1.07x slower                                                       |
| bench_mp_pool           | 60.7 ms                                                     | 66.9 ms: 1.10x slower                                                       |
| gc_traversal            | 1.34 ms                                                     | 1.49 ms: 1.11x slower                                                       |
| pathlib                 | 77.4 ms                                                     | 86.6 ms: 1.12x slower                                                       |
| pickle_dict             | 16.9 us                                                     | 19.1 us: 1.13x slower                                                       |
| dask                    | 305 ms                                                      | 358 ms: 1.18x slower                                                        |
| coverage                | 40.0 ms                                                     | 52.8 ms: 1.32x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.21x faster                                                                |

Benchmark hidden because not significant (3): unpickle_list, logging_simple, sqlite_synth
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.15x
