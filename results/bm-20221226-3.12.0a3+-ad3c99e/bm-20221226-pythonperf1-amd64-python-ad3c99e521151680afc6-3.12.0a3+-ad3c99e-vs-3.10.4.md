
# Results vs. 3.10.4

- fork: python
- ref: ad3c99e521151680afc6
- machine: windows-amd64
- commit hash: ad3c99e
- commit date: 2022-12-26
- overall geometric mean: 1.17x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221226-pythonperf1-amd64-python-ad3c99e521151680afc6-3.12.0a3+-ad3c99e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 203 ms: 1.17x faster                                                        |
| chameleon      | 5.92 ms                                                     | 4.75 ms: 1.25x faster                                                       |
| docutils       | 1.89 sec                                                    | 1.56 sec: 1.21x faster                                                      |
| html5lib       | 46.5 ms                                                     | 34.7 ms: 1.34x faster                                                       |
| Geometric mean | (ref)                                                       | 1.24x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221226-pythonperf1-amd64-python-ad3c99e521151680afc6-3.12.0a3+-ad3c99e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 51.1 ms: 1.18x faster                                                       |
| nbody          | 69.3 ms                                                     | 66.0 ms: 1.05x faster                                                       |
| pidigits       | 145 ms                                                      | 153 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221226-pythonperf1-amd64-python-ad3c99e521151680afc6-3.12.0a3+-ad3c99e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 83.8 ms: 1.23x faster                                                       |
| regex_v8       | 15.0 ms                                                     | 14.0 ms: 1.08x faster                                                       |
| regex_dna      | 132 ms                                                      | 125 ms: 1.05x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.65 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221226-pythonperf1-amd64-python-ad3c99e521151680afc6-3.12.0a3+-ad3c99e |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.43 ms: 1.57x faster                                                       |
| pickle_pure_python   | 257 us                                                      | 186 us: 1.38x faster                                                        |
| unpickle_pure_python | 171 us                                                      | 127 us: 1.35x faster                                                        |
| xml_etree_process    | 43.4 ms                                                     | 35.7 ms: 1.22x faster                                                       |
| xml_etree_parse      | 102 ms                                                      | 90.4 ms: 1.13x faster                                                       |
| unpickle             | 9.17 us                                                     | 8.20 us: 1.12x faster                                                       |
| json_loads           | 14.2 us                                                     | 12.9 us: 1.10x faster                                                       |
| unpickle_list        | 2.81 us                                                     | 2.62 us: 1.07x faster                                                       |
| xml_etree_generate   | 54.5 ms                                                     | 51.7 ms: 1.05x faster                                                       |
| pickle               | 6.80 us                                                     | 7.29 us: 1.07x slower                                                       |
| pickle_list          | 2.59 us                                                     | 2.83 us: 1.10x slower                                                       |
| pickle_dict          | 16.9 us                                                     | 19.0 us: 1.12x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.12x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221226-pythonperf1-amd64-python-ad3c99e521151680afc6-3.12.0a3+-ad3c99e |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 18.9 ms: 1.06x faster                                                       |
| python_startup_no_site | 15.5 ms                                                     | 15.7 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221226-pythonperf1-amd64-python-ad3c99e521151680afc6-3.12.0a3+-ad3c99e |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 8.80 ms                                                     | 6.35 ms: 1.39x faster                                                       |
| genshi_text     | 19.0 ms                                                     | 14.6 ms: 1.30x faster                                                       |
| django_template | 28.2 ms                                                     | 21.9 ms: 1.29x faster                                                       |
| genshi_xml      | 40.5 ms                                                     | 33.9 ms: 1.19x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.29x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221226-pythonperf1-amd64-python-ad3c99e521151680afc6-3.12.0a3+-ad3c99e |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 2.25 ms: 1.86x faster                                                       |
| richards                | 41.2 ms                                                     | 25.6 ms: 1.61x faster                                                       |
| logging_silent          | 96.4 ns                                                     | 60.9 ns: 1.58x faster                                                       |
| json_dumps              | 8.50 ms                                                     | 5.43 ms: 1.57x faster                                                       |
| mypy2                   | 352 ms                                                      | 228 ms: 1.54x faster                                                        |
| scimark_sor             | 105 ms                                                      | 70.3 ms: 1.49x faster                                                       |
| go                      | 136 ms                                                      | 91.7 ms: 1.48x faster                                                       |
| asyncio_tcp             | 712 ms                                                      | 482 ms: 1.48x faster                                                        |
| scimark_lu              | 85.4 ms                                                     | 59.0 ms: 1.45x faster                                                       |
| raytrace                | 271 ms                                                      | 190 ms: 1.43x faster                                                        |
| pyflate                 | 387 ms                                                      | 279 ms: 1.39x faster                                                        |
| mako                    | 8.80 ms                                                     | 6.35 ms: 1.39x faster                                                       |
| pickle_pure_python      | 257 us                                                      | 186 us: 1.38x faster                                                        |
| scimark_monte_carlo     | 55.9 ms                                                     | 40.7 ms: 1.37x faster                                                       |
| async_tree_io           | 1.07 sec                                                    | 788 ms: 1.35x faster                                                        |
| unpickle_pure_python    | 171 us                                                      | 127 us: 1.35x faster                                                        |
| sqlglot_transpile       | 1.46 ms                                                     | 1.09 ms: 1.34x faster                                                       |
| html5lib                | 46.5 ms                                                     | 34.7 ms: 1.34x faster                                                       |
| hexiom                  | 5.52 ms                                                     | 4.12 ms: 1.34x faster                                                       |
| crypto_pyaes            | 62.3 ms                                                     | 46.7 ms: 1.33x faster                                                       |
| pycparser               | 868 ms                                                      | 661 ms: 1.31x faster                                                        |
| thrift                  | 615 us                                                      | 470 us: 1.31x faster                                                        |
| sqlglot_parse           | 1.22 ms                                                     | 932 us: 1.31x faster                                                        |
| async_tree_none         | 420 ms                                                      | 322 ms: 1.31x faster                                                        |
| async_tree_memoization  | 497 ms                                                      | 381 ms: 1.30x faster                                                        |
| genshi_text             | 19.0 ms                                                     | 14.6 ms: 1.30x faster                                                       |
| chaos                   | 58.9 ms                                                     | 45.6 ms: 1.29x faster                                                       |
| django_template         | 28.2 ms                                                     | 21.9 ms: 1.29x faster                                                       |
| unpack_sequence         | 37.8 ns                                                     | 29.9 ns: 1.27x faster                                                       |
| deepcopy_memo           | 28.5 us                                                     | 22.6 us: 1.26x faster                                                       |
| spectral_norm           | 78.0 ms                                                     | 62.4 ms: 1.25x faster                                                       |
| chameleon               | 5.92 ms                                                     | 4.75 ms: 1.25x faster                                                       |
| async_generators        | 224 ms                                                      | 180 ms: 1.24x faster                                                        |
| async_tree_cpu_io_mixed | 609 ms                                                      | 492 ms: 1.24x faster                                                        |
| regex_compile           | 103 ms                                                      | 83.8 ms: 1.23x faster                                                       |
| pprint_pformat          | 1.21 sec                                                    | 987 ms: 1.22x faster                                                        |
| sqlglot_optimize        | 39.0 ms                                                     | 32.0 ms: 1.22x faster                                                       |
| xml_etree_process       | 43.4 ms                                                     | 35.7 ms: 1.22x faster                                                       |
| pprint_safe_repr        | 589 ms                                                      | 484 ms: 1.22x faster                                                        |
| docutils                | 1.89 sec                                                    | 1.56 sec: 1.21x faster                                                      |
| genshi_xml              | 40.5 ms                                                     | 33.9 ms: 1.19x faster                                                       |
| nqueens                 | 67.0 ms                                                     | 56.9 ms: 1.18x faster                                                       |
| float                   | 60.2 ms                                                     | 51.1 ms: 1.18x faster                                                       |
| 2to3                    | 237 ms                                                      | 203 ms: 1.17x faster                                                        |
| dask                    | 305 ms                                                      | 262 ms: 1.17x faster                                                        |
| create_gc_cycles        | 782 us                                                      | 681 us: 1.15x faster                                                        |
| deepcopy                | 255 us                                                      | 223 us: 1.14x faster                                                        |
| json                    | 3.05 ms                                                     | 2.69 ms: 1.13x faster                                                       |
| xml_etree_parse         | 102 ms                                                      | 90.4 ms: 1.13x faster                                                       |
| bench_thread_pool       | 946 us                                                      | 845 us: 1.12x faster                                                        |
| unpickle                | 9.17 us                                                     | 8.20 us: 1.12x faster                                                       |
| dulwich_log             | 47.6 ms                                                     | 42.6 ms: 1.12x faster                                                       |
| sqlglot_normalize       | 202 ms                                                      | 181 ms: 1.12x faster                                                        |
| sympy_integrate         | 14.8 ms                                                     | 13.4 ms: 1.11x faster                                                       |
| sympy_expand            | 315 ms                                                      | 284 ms: 1.11x faster                                                        |
| json_loads              | 14.2 us                                                     | 12.9 us: 1.10x faster                                                       |
| deepcopy_reduce         | 2.16 us                                                     | 1.97 us: 1.10x faster                                                       |
| scimark_fft             | 193 ms                                                      | 176 ms: 1.09x faster                                                        |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.45 ms: 1.08x faster                                                       |
| fannkuch                | 258 ms                                                      | 238 ms: 1.08x faster                                                        |
| regex_v8                | 15.0 ms                                                     | 14.0 ms: 1.08x faster                                                       |
| coroutines              | 15.9 ms                                                     | 14.9 ms: 1.07x faster                                                       |
| unpickle_list           | 2.81 us                                                     | 2.62 us: 1.07x faster                                                       |
| sympy_sum               | 104 ms                                                      | 97.7 ms: 1.07x faster                                                       |
| python_startup          | 20.0 ms                                                     | 18.9 ms: 1.06x faster                                                       |
| xml_etree_generate      | 54.5 ms                                                     | 51.7 ms: 1.05x faster                                                       |
| regex_dna               | 132 ms                                                      | 125 ms: 1.05x faster                                                        |
| nbody                   | 69.3 ms                                                     | 66.0 ms: 1.05x faster                                                       |
| mdp                     | 1.71 sec                                                    | 1.63 sec: 1.05x faster                                                      |
| sympy_str               | 188 ms                                                      | 180 ms: 1.05x faster                                                        |
| sqlite_synth            | 1.84 us                                                     | 1.78 us: 1.03x faster                                                       |
| pathlib                 | 77.4 ms                                                     | 76.4 ms: 1.01x faster                                                       |
| regex_effbot            | 1.66 ms                                                     | 1.65 ms: 1.01x faster                                                       |
| meteor_contest          | 72.5 ms                                                     | 71.8 ms: 1.01x faster                                                       |
| telco                   | 3.78 ms                                                     | 3.80 ms: 1.00x slower                                                       |
| python_startup_no_site  | 15.5 ms                                                     | 15.7 ms: 1.01x slower                                                       |
| logging_format          | 6.66 us                                                     | 6.84 us: 1.03x slower                                                       |
| bench_mp_pool           | 60.7 ms                                                     | 62.6 ms: 1.03x slower                                                       |
| logging_simple          | 6.20 us                                                     | 6.51 us: 1.05x slower                                                       |
| pidigits                | 145 ms                                                      | 153 ms: 1.05x slower                                                        |
| pickle                  | 6.80 us                                                     | 7.29 us: 1.07x slower                                                       |
| pickle_list             | 2.59 us                                                     | 2.83 us: 1.10x slower                                                       |
| gc_traversal            | 1.34 ms                                                     | 1.49 ms: 1.11x slower                                                       |
| pickle_dict             | 16.9 us                                                     | 19.0 us: 1.12x slower                                                       |
| generators              | 31.6 ms                                                     | 37.8 ms: 1.20x slower                                                       |
| coverage                | 40.0 ms                                                     | 53.4 ms: 1.33x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.17x faster                                                                |

Benchmark hidden because not significant (2): xml_etree_iterparse, comprehensions
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x
