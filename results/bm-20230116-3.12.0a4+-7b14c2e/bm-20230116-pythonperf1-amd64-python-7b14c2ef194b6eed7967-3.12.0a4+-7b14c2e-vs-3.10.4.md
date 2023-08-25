
# Results vs. 3.10.4

- fork: python
- ref: 7b14c2ef194b6eed7967
- machine: windows-amd64
- commit hash: 7b14c2e
- commit date: 2023-01-16
- overall geometric mean: 1.23x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-pythonperf1-amd64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 200 ms: 1.19x faster                                                        |
| chameleon      | 5.92 ms                                                     | 4.49 ms: 1.32x faster                                                       |
| docutils       | 1.89 sec                                                    | 1.53 sec: 1.24x faster                                                      |
| html5lib       | 46.5 ms                                                     | 33.0 ms: 1.41x faster                                                       |
| tornado_http   | 109 ms                                                      | 91.4 ms: 1.19x faster                                                       |
| Geometric mean | (ref)                                                       | 1.27x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-pythonperf1-amd64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 47.9 ms: 1.26x faster                                                       |
| nbody          | 69.3 ms                                                     | 58.5 ms: 1.19x faster                                                       |
| pidigits       | 145 ms                                                      | 151 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-pythonperf1-amd64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 78.3 ms: 1.32x faster                                                       |
| regex_v8       | 15.0 ms                                                     | 13.8 ms: 1.09x faster                                                       |
| regex_dna      | 132 ms                                                      | 124 ms: 1.06x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.61 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-pythonperf1-amd64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.24 ms: 1.62x faster                                                       |
| pickle_pure_python   | 257 us                                                      | 173 us: 1.49x faster                                                        |
| unpickle_pure_python | 171 us                                                      | 119 us: 1.44x faster                                                        |
| xml_etree_process    | 43.4 ms                                                     | 33.9 ms: 1.28x faster                                                       |
| xml_etree_parse      | 102 ms                                                      | 89.1 ms: 1.14x faster                                                       |
| xml_etree_generate   | 54.5 ms                                                     | 50.0 ms: 1.09x faster                                                       |
| unpickle             | 9.17 us                                                     | 8.82 us: 1.04x faster                                                       |
| unpickle_list        | 2.81 us                                                     | 2.71 us: 1.04x faster                                                       |
| json_loads           | 14.2 us                                                     | 14.0 us: 1.01x faster                                                       |
| pickle_list          | 2.59 us                                                     | 2.74 us: 1.06x slower                                                       |
| pickle_dict          | 16.9 us                                                     | 19.0 us: 1.12x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.13x faster                                                                |

Benchmark hidden because not significant (2): xml_etree_iterparse, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-pythonperf1-amd64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 18.7 ms: 1.07x faster                                                       |
| python_startup_no_site | 15.5 ms                                                     | 15.8 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.03x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-pythonperf1-amd64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 8.80 ms                                                     | 6.12 ms: 1.44x faster                                                       |
| django_template | 28.2 ms                                                     | 20.4 ms: 1.39x faster                                                       |
| genshi_text     | 19.0 ms                                                     | 13.9 ms: 1.38x faster                                                       |
| genshi_xml      | 40.5 ms                                                     | 31.0 ms: 1.31x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.38x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-pythonperf1-amd64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 1.93 ms: 2.16x faster                                                       |
| logging_silent          | 96.4 ns                                                     | 54.9 ns: 1.76x faster                                                       |
| scimark_sor             | 105 ms                                                      | 61.1 ms: 1.72x faster                                                       |
| richards                | 41.2 ms                                                     | 24.1 ms: 1.71x faster                                                       |
| go                      | 136 ms                                                      | 81.1 ms: 1.68x faster                                                       |
| mypy2                   | 352 ms                                                      | 216 ms: 1.63x faster                                                        |
| json_dumps              | 8.50 ms                                                     | 5.24 ms: 1.62x faster                                                       |
| raytrace                | 271 ms                                                      | 168 ms: 1.61x faster                                                        |
| scimark_lu              | 85.4 ms                                                     | 55.8 ms: 1.53x faster                                                       |
| hexiom                  | 5.52 ms                                                     | 3.67 ms: 1.50x faster                                                       |
| asyncio_tcp             | 712 ms                                                      | 475 ms: 1.50x faster                                                        |
| scimark_monte_carlo     | 55.9 ms                                                     | 37.3 ms: 1.50x faster                                                       |
| pickle_pure_python      | 257 us                                                      | 173 us: 1.49x faster                                                        |
| pyflate                 | 387 ms                                                      | 265 ms: 1.46x faster                                                        |
| deepcopy_memo           | 28.5 us                                                     | 19.7 us: 1.45x faster                                                       |
| unpickle_pure_python    | 171 us                                                      | 119 us: 1.44x faster                                                        |
| mako                    | 8.80 ms                                                     | 6.12 ms: 1.44x faster                                                       |
| unpack_sequence         | 37.8 ns                                                     | 26.4 ns: 1.43x faster                                                       |
| sqlglot_parse           | 1.22 ms                                                     | 858 us: 1.42x faster                                                        |
| async_tree_memoization  | 497 ms                                                      | 351 ms: 1.42x faster                                                        |
| chaos                   | 58.9 ms                                                     | 41.8 ms: 1.41x faster                                                       |
| html5lib                | 46.5 ms                                                     | 33.0 ms: 1.41x faster                                                       |
| async_tree_io           | 1.07 sec                                                    | 768 ms: 1.39x faster                                                        |
| django_template         | 28.2 ms                                                     | 20.4 ms: 1.39x faster                                                       |
| sqlglot_transpile       | 1.46 ms                                                     | 1.06 ms: 1.39x faster                                                       |
| genshi_text             | 19.0 ms                                                     | 13.9 ms: 1.38x faster                                                       |
| pycparser               | 868 ms                                                      | 634 ms: 1.37x faster                                                        |
| async_tree_none         | 420 ms                                                      | 307 ms: 1.37x faster                                                        |
| crypto_pyaes            | 62.3 ms                                                     | 46.0 ms: 1.36x faster                                                       |
| chameleon               | 5.92 ms                                                     | 4.49 ms: 1.32x faster                                                       |
| regex_compile           | 103 ms                                                      | 78.3 ms: 1.32x faster                                                       |
| spectral_norm           | 78.0 ms                                                     | 59.2 ms: 1.32x faster                                                       |
| pprint_safe_repr        | 589 ms                                                      | 450 ms: 1.31x faster                                                        |
| genshi_xml              | 40.5 ms                                                     | 31.0 ms: 1.31x faster                                                       |
| thrift                  | 615 us                                                      | 474 us: 1.30x faster                                                        |
| pprint_pformat          | 1.21 sec                                                    | 933 ms: 1.29x faster                                                        |
| async_generators        | 224 ms                                                      | 173 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed | 609 ms                                                      | 474 ms: 1.28x faster                                                        |
| xml_etree_process       | 43.4 ms                                                     | 33.9 ms: 1.28x faster                                                       |
| deepcopy                | 255 us                                                      | 201 us: 1.27x faster                                                        |
| float                   | 60.2 ms                                                     | 47.9 ms: 1.26x faster                                                       |
| sqlglot_optimize        | 39.0 ms                                                     | 31.5 ms: 1.24x faster                                                       |
| docutils                | 1.89 sec                                                    | 1.53 sec: 1.24x faster                                                      |
| sqlglot_normalize       | 202 ms                                                      | 167 ms: 1.21x faster                                                        |
| nqueens                 | 67.0 ms                                                     | 55.3 ms: 1.21x faster                                                       |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.21 ms: 1.20x faster                                                       |
| fannkuch                | 258 ms                                                      | 214 ms: 1.20x faster                                                        |
| deepcopy_reduce         | 2.16 us                                                     | 1.80 us: 1.20x faster                                                       |
| scimark_fft             | 193 ms                                                      | 161 ms: 1.20x faster                                                        |
| tornado_http            | 109 ms                                                      | 91.4 ms: 1.19x faster                                                       |
| dask                    | 305 ms                                                      | 256 ms: 1.19x faster                                                        |
| nbody                   | 69.3 ms                                                     | 58.5 ms: 1.19x faster                                                       |
| 2to3                    | 237 ms                                                      | 200 ms: 1.19x faster                                                        |
| create_gc_cycles        | 782 us                                                      | 670 us: 1.17x faster                                                        |
| sympy_expand            | 315 ms                                                      | 273 ms: 1.15x faster                                                        |
| xml_etree_parse         | 102 ms                                                      | 89.1 ms: 1.14x faster                                                       |
| dulwich_log             | 47.6 ms                                                     | 41.9 ms: 1.13x faster                                                       |
| sympy_integrate         | 14.8 ms                                                     | 13.1 ms: 1.13x faster                                                       |
| bench_thread_pool       | 946 us                                                      | 839 us: 1.13x faster                                                        |
| mdp                     | 1.71 sec                                                    | 1.53 sec: 1.12x faster                                                      |
| json                    | 3.05 ms                                                     | 2.74 ms: 1.11x faster                                                       |
| sympy_str               | 188 ms                                                      | 172 ms: 1.10x faster                                                        |
| sympy_sum               | 104 ms                                                      | 95.0 ms: 1.10x faster                                                       |
| regex_v8                | 15.0 ms                                                     | 13.8 ms: 1.09x faster                                                       |
| xml_etree_generate      | 54.5 ms                                                     | 50.0 ms: 1.09x faster                                                       |
| coroutines              | 15.9 ms                                                     | 14.6 ms: 1.09x faster                                                       |
| python_startup          | 20.0 ms                                                     | 18.7 ms: 1.07x faster                                                       |
| logging_simple          | 6.20 us                                                     | 5.80 us: 1.07x faster                                                       |
| regex_dna               | 132 ms                                                      | 124 ms: 1.06x faster                                                        |
| comprehensions          | 16.0 us                                                     | 15.1 us: 1.06x faster                                                       |
| meteor_contest          | 72.5 ms                                                     | 69.2 ms: 1.05x faster                                                       |
| sqlite_synth            | 1.84 us                                                     | 1.76 us: 1.04x faster                                                       |
| unpickle                | 9.17 us                                                     | 8.82 us: 1.04x faster                                                       |
| unpickle_list           | 2.81 us                                                     | 2.71 us: 1.04x faster                                                       |
| regex_effbot            | 1.66 ms                                                     | 1.61 ms: 1.04x faster                                                       |
| logging_format          | 6.66 us                                                     | 6.44 us: 1.03x faster                                                       |
| pathlib                 | 77.4 ms                                                     | 74.9 ms: 1.03x faster                                                       |
| json_loads              | 14.2 us                                                     | 14.0 us: 1.01x faster                                                       |
| telco                   | 3.78 ms                                                     | 3.75 ms: 1.01x faster                                                       |
| python_startup_no_site  | 15.5 ms                                                     | 15.8 ms: 1.02x slower                                                       |
| pidigits                | 145 ms                                                      | 151 ms: 1.04x slower                                                        |
| bench_mp_pool           | 60.7 ms                                                     | 63.1 ms: 1.04x slower                                                       |
| pickle_list             | 2.59 us                                                     | 2.74 us: 1.06x slower                                                       |
| gc_traversal            | 1.34 ms                                                     | 1.43 ms: 1.06x slower                                                       |
| generators              | 31.6 ms                                                     | 34.2 ms: 1.08x slower                                                       |
| pickle_dict             | 16.9 us                                                     | 19.0 us: 1.12x slower                                                       |
| coverage                | 40.0 ms                                                     | 53.1 ms: 1.33x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.23x faster                                                                |

Benchmark hidden because not significant (2): xml_etree_iterparse, pickle
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.18x
