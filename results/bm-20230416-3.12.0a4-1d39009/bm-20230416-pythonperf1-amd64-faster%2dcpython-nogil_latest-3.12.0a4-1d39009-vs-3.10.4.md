
# Results vs. 3.10.4

- fork: faster-cpython
- ref: nogil_latest
- machine: windows-amd64
- commit hash: 1d39009
- commit date: 2023-04-16
- overall geometric mean: 1.07x faster \*
- HPT reliability: 99.88%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230416-pythonperf1-amd64-faster%2dcpython-nogil_latest-3.12.0a4-1d39009 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 224 ms: 1.06x faster                                                         |
| chameleon      | 5.92 ms                                                     | 5.66 ms: 1.05x faster                                                        |
| html5lib       | 46.5 ms                                                     | 39.3 ms: 1.18x faster                                                        |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                 |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230416-pythonperf1-amd64-faster%2dcpython-nogil_latest-3.12.0a4-1d39009 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 49.6 ms: 1.21x faster                                                        |
| pidigits       | 145 ms                                                      | 141 ms: 1.03x faster                                                         |
| nbody          | 69.3 ms                                                     | 89.9 ms: 1.30x slower                                                        |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230416-pythonperf1-amd64-faster%2dcpython-nogil_latest-3.12.0a4-1d39009 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 132 ms                                                      | 110 ms: 1.20x faster                                                         |
| regex_v8       | 15.0 ms                                                     | 13.2 ms: 1.14x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.53 ms: 1.09x faster                                                        |
| regex_compile  | 103 ms                                                      | 96.4 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230416-pythonperf1-amd64-faster%2dcpython-nogil_latest-3.12.0a4-1d39009 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 6.50 ms: 1.31x faster                                                        |
| xml_etree_parse      | 102 ms                                                      | 82.9 ms: 1.23x faster                                                        |
| pickle_pure_python   | 257 us                                                      | 218 us: 1.18x faster                                                         |
| unpickle_pure_python | 171 us                                                      | 159 us: 1.07x faster                                                         |
| xml_etree_process    | 43.4 ms                                                     | 41.7 ms: 1.04x faster                                                        |
| unpickle_list        | 2.81 us                                                     | 2.86 us: 1.02x slower                                                        |
| json_loads           | 14.2 us                                                     | 14.6 us: 1.03x slower                                                        |
| pickle               | 6.80 us                                                     | 7.14 us: 1.05x slower                                                        |
| xml_etree_generate   | 54.5 ms                                                     | 57.5 ms: 1.05x slower                                                        |
| pickle_list          | 2.59 us                                                     | 2.81 us: 1.08x slower                                                        |
| xml_etree_iterparse  | 63.5 ms                                                     | 74.7 ms: 1.18x slower                                                        |
| pickle_dict          | 16.9 us                                                     | 21.8 us: 1.29x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230416-pythonperf1-amd64-faster%2dcpython-nogil_latest-3.12.0a4-1d39009 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 18.2 ms: 1.10x faster                                                        |
| python_startup_no_site | 15.5 ms                                                     | 15.4 ms: 1.01x faster                                                        |
| Geometric mean         | (ref)                                                       | 1.05x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230416-pythonperf1-amd64-faster%2dcpython-nogil_latest-3.12.0a4-1d39009 |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 40.5 ms                                                     | 35.3 ms: 1.15x faster                                                        |
| django_template | 28.2 ms                                                     | 25.5 ms: 1.11x faster                                                        |
| genshi_text     | 19.0 ms                                                     | 17.7 ms: 1.08x faster                                                        |
| mako            | 8.80 ms                                                     | 8.95 ms: 1.02x slower                                                        |
| Geometric mean  | (ref)                                                       | 1.08x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230416-pythonperf1-amd64-faster%2dcpython-nogil_latest-3.12.0a4-1d39009 |
|-------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.07 sec                                                    | 405 ms: 2.63x faster                                                         |
| async_tree_none         | 420 ms                                                      | 189 ms: 2.22x faster                                                         |
| async_tree_memoization  | 497 ms                                                      | 240 ms: 2.07x faster                                                         |
| async_tree_cpu_io_mixed | 609 ms                                                      | 371 ms: 1.64x faster                                                         |
| deltablue               | 4.17 ms                                                     | 2.71 ms: 1.54x faster                                                        |
| asyncio_tcp             | 712 ms                                                      | 489 ms: 1.46x faster                                                         |
| sqlite_synth            | 1.84 us                                                     | 1.35 us: 1.36x faster                                                        |
| go                      | 136 ms                                                      | 103 ms: 1.32x faster                                                         |
| json_dumps              | 8.50 ms                                                     | 6.50 ms: 1.31x faster                                                        |
| logging_silent          | 96.4 ns                                                     | 75.0 ns: 1.28x faster                                                        |
| pyflate                 | 387 ms                                                      | 302 ms: 1.28x faster                                                         |
| richards                | 41.2 ms                                                     | 32.3 ms: 1.27x faster                                                        |
| xml_etree_parse         | 102 ms                                                      | 82.9 ms: 1.23x faster                                                        |
| pycparser               | 868 ms                                                      | 713 ms: 1.22x faster                                                         |
| float                   | 60.2 ms                                                     | 49.6 ms: 1.21x faster                                                        |
| mypy2                   | 352 ms                                                      | 291 ms: 1.21x faster                                                         |
| regex_dna               | 132 ms                                                      | 110 ms: 1.20x faster                                                         |
| crypto_pyaes            | 62.3 ms                                                     | 52.7 ms: 1.18x faster                                                        |
| html5lib                | 46.5 ms                                                     | 39.3 ms: 1.18x faster                                                        |
| pickle_pure_python      | 257 us                                                      | 218 us: 1.18x faster                                                         |
| scimark_sor             | 105 ms                                                      | 89.1 ms: 1.18x faster                                                        |
| scimark_lu              | 85.4 ms                                                     | 73.1 ms: 1.17x faster                                                        |
| genshi_xml              | 40.5 ms                                                     | 35.3 ms: 1.15x faster                                                        |
| regex_v8                | 15.0 ms                                                     | 13.2 ms: 1.14x faster                                                        |
| thrift                  | 615 us                                                      | 542 us: 1.14x faster                                                         |
| raytrace                | 271 ms                                                      | 241 ms: 1.12x faster                                                         |
| hexiom                  | 5.52 ms                                                     | 4.97 ms: 1.11x faster                                                        |
| django_template         | 28.2 ms                                                     | 25.5 ms: 1.11x faster                                                        |
| sqlglot_transpile       | 1.46 ms                                                     | 1.33 ms: 1.10x faster                                                        |
| python_startup          | 20.0 ms                                                     | 18.2 ms: 1.10x faster                                                        |
| chaos                   | 58.9 ms                                                     | 53.7 ms: 1.10x faster                                                        |
| dulwich_log             | 47.6 ms                                                     | 43.6 ms: 1.09x faster                                                        |
| async_generators        | 224 ms                                                      | 205 ms: 1.09x faster                                                         |
| scimark_monte_carlo     | 55.9 ms                                                     | 51.2 ms: 1.09x faster                                                        |
| sqlglot_parse           | 1.22 ms                                                     | 1.12 ms: 1.09x faster                                                        |
| regex_effbot            | 1.66 ms                                                     | 1.53 ms: 1.09x faster                                                        |
| genshi_text             | 19.0 ms                                                     | 17.7 ms: 1.08x faster                                                        |
| unpickle_pure_python    | 171 us                                                      | 159 us: 1.07x faster                                                         |
| regex_compile           | 103 ms                                                      | 96.4 ms: 1.07x faster                                                        |
| sqlglot_optimize        | 39.0 ms                                                     | 36.8 ms: 1.06x faster                                                        |
| 2to3                    | 237 ms                                                      | 224 ms: 1.06x faster                                                         |
| pathlib                 | 77.4 ms                                                     | 73.6 ms: 1.05x faster                                                        |
| mdp                     | 1.71 sec                                                    | 1.63 sec: 1.05x faster                                                       |
| chameleon               | 5.92 ms                                                     | 5.66 ms: 1.05x faster                                                        |
| create_gc_cycles        | 782 us                                                      | 748 us: 1.04x faster                                                         |
| xml_etree_process       | 43.4 ms                                                     | 41.7 ms: 1.04x faster                                                        |
| json                    | 3.05 ms                                                     | 2.94 ms: 1.04x faster                                                        |
| pidigits                | 145 ms                                                      | 141 ms: 1.03x faster                                                         |
| nqueens                 | 67.0 ms                                                     | 65.6 ms: 1.02x faster                                                        |
| sqlglot_normalize       | 202 ms                                                      | 199 ms: 1.02x faster                                                         |
| python_startup_no_site  | 15.5 ms                                                     | 15.4 ms: 1.01x faster                                                        |
| pprint_safe_repr        | 589 ms                                                      | 586 ms: 1.01x faster                                                         |
| spectral_norm           | 78.0 ms                                                     | 78.8 ms: 1.01x slower                                                        |
| unpickle_list           | 2.81 us                                                     | 2.86 us: 1.02x slower                                                        |
| sympy_expand            | 315 ms                                                      | 320 ms: 1.02x slower                                                         |
| mako                    | 8.80 ms                                                     | 8.95 ms: 1.02x slower                                                        |
| json_loads              | 14.2 us                                                     | 14.6 us: 1.03x slower                                                        |
| deepcopy_memo           | 28.5 us                                                     | 29.5 us: 1.03x slower                                                        |
| sympy_sum               | 104 ms                                                      | 109 ms: 1.05x slower                                                         |
| pickle                  | 6.80 us                                                     | 7.14 us: 1.05x slower                                                        |
| sympy_str               | 188 ms                                                      | 198 ms: 1.05x slower                                                         |
| bench_mp_pool           | 60.7 ms                                                     | 63.9 ms: 1.05x slower                                                        |
| xml_etree_generate      | 54.5 ms                                                     | 57.5 ms: 1.05x slower                                                        |
| coroutines              | 15.9 ms                                                     | 16.8 ms: 1.05x slower                                                        |
| deepcopy                | 255 us                                                      | 272 us: 1.06x slower                                                         |
| pickle_list             | 2.59 us                                                     | 2.81 us: 1.08x slower                                                        |
| bench_thread_pool       | 946 us                                                      | 1.03 ms: 1.09x slower                                                        |
| fannkuch                | 258 ms                                                      | 285 ms: 1.10x slower                                                         |
| logging_format          | 6.66 us                                                     | 7.40 us: 1.11x slower                                                        |
| deepcopy_reduce         | 2.16 us                                                     | 2.40 us: 1.11x slower                                                        |
| logging_simple          | 6.20 us                                                     | 6.92 us: 1.12x slower                                                        |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.98 ms: 1.12x slower                                                        |
| scimark_fft             | 193 ms                                                      | 220 ms: 1.14x slower                                                         |
| gc_traversal            | 1.34 ms                                                     | 1.56 ms: 1.16x slower                                                        |
| telco                   | 3.78 ms                                                     | 4.41 ms: 1.17x slower                                                        |
| xml_etree_iterparse     | 63.5 ms                                                     | 74.7 ms: 1.18x slower                                                        |
| generators              | 31.6 ms                                                     | 37.5 ms: 1.19x slower                                                        |
| meteor_contest          | 72.5 ms                                                     | 86.5 ms: 1.19x slower                                                        |
| comprehensions          | 16.0 us                                                     | 19.1 us: 1.19x slower                                                        |
| pickle_dict             | 16.9 us                                                     | 21.8 us: 1.29x slower                                                        |
| nbody                   | 69.3 ms                                                     | 89.9 ms: 1.30x slower                                                        |
| unpack_sequence         | 37.8 ns                                                     | 55.2 ns: 1.46x slower                                                        |
| coverage                | 40.0 ms                                                     | 59.9 ms: 1.50x slower                                                        |
| Geometric mean          | (ref)                                                       | 1.07x faster                                                                 |

Benchmark hidden because not significant (4): docutils, sympy_integrate, pprint_pformat, unpickle
Ignored benchmarks (11) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, dask, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols


# HPT report

- Reliability score: 99.88% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.00x
