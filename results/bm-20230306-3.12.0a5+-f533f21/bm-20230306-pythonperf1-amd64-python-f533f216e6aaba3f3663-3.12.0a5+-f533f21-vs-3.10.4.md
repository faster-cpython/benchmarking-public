
# Results vs. 3.10.4

- fork: python
- ref: f533f216e6aaba3f3663
- machine: windows-amd64
- commit hash: f533f21
- commit date: 2023-03-06
- overall geometric mean: 1.19x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230306-pythonperf1-amd64-python-f533f216e6aaba3f3663-3.12.0a5+-f533f21 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 203 ms: 1.17x faster                                                        |
| chameleon      | 5.92 ms                                                     | 4.82 ms: 1.23x faster                                                       |
| docutils       | 1.89 sec                                                    | 1.56 sec: 1.21x faster                                                      |
| html5lib       | 46.5 ms                                                     | 36.7 ms: 1.27x faster                                                       |
| tornado_http   | 109 ms                                                      | 90.7 ms: 1.20x faster                                                       |
| Geometric mean | (ref)                                                       | 1.21x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230306-pythonperf1-amd64-python-f533f216e6aaba3f3663-3.12.0a5+-f533f21 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 50.4 ms: 1.20x faster                                                       |
| nbody          | 69.3 ms                                                     | 64.6 ms: 1.07x faster                                                       |
| pidigits       | 145 ms                                                      | 150 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230306-pythonperf1-amd64-python-f533f216e6aaba3f3663-3.12.0a5+-f533f21 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 82.1 ms: 1.26x faster                                                       |
| regex_dna      | 132 ms                                                      | 123 ms: 1.07x faster                                                        |
| regex_v8       | 15.0 ms                                                     | 14.3 ms: 1.06x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.65 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230306-pythonperf1-amd64-python-f533f216e6aaba3f3663-3.12.0a5+-f533f21 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.40 ms: 1.58x faster                                                       |
| pickle_pure_python   | 257 us                                                      | 176 us: 1.46x faster                                                        |
| unpickle_pure_python | 171 us                                                      | 126 us: 1.35x faster                                                        |
| xml_etree_process    | 43.4 ms                                                     | 37.7 ms: 1.15x faster                                                       |
| unpickle             | 9.17 us                                                     | 8.04 us: 1.14x faster                                                       |
| json_loads           | 14.2 us                                                     | 12.7 us: 1.11x faster                                                       |
| xml_etree_parse      | 102 ms                                                      | 92.0 ms: 1.11x faster                                                       |
| unpickle_list        | 2.81 us                                                     | 2.74 us: 1.03x faster                                                       |
| xml_etree_iterparse  | 63.5 ms                                                     | 62.4 ms: 1.02x faster                                                       |
| xml_etree_generate   | 54.5 ms                                                     | 53.9 ms: 1.01x faster                                                       |
| pickle               | 6.80 us                                                     | 6.91 us: 1.02x slower                                                       |
| pickle_list          | 2.59 us                                                     | 2.80 us: 1.08x slower                                                       |
| pickle_dict          | 16.9 us                                                     | 18.7 us: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230306-pythonperf1-amd64-python-f533f216e6aaba3f3663-3.12.0a5+-f533f21 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 18.9 ms: 1.06x faster                                                       |
| python_startup_no_site | 15.5 ms                                                     | 16.0 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230306-pythonperf1-amd64-python-f533f216e6aaba3f3663-3.12.0a5+-f533f21 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 8.80 ms                                                     | 6.36 ms: 1.38x faster                                                       |
| genshi_text     | 19.0 ms                                                     | 14.2 ms: 1.35x faster                                                       |
| django_template | 28.2 ms                                                     | 21.9 ms: 1.29x faster                                                       |
| genshi_xml      | 40.5 ms                                                     | 32.1 ms: 1.26x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.32x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230306-pythonperf1-amd64-python-f533f216e6aaba3f3663-3.12.0a5+-f533f21 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 1.99 ms: 2.10x faster                                                       |
| logging_silent          | 96.4 ns                                                     | 56.1 ns: 1.72x faster                                                       |
| mypy2                   | 352 ms                                                      | 216 ms: 1.63x faster                                                        |
| richards                | 41.2 ms                                                     | 25.4 ms: 1.62x faster                                                       |
| json_dumps              | 8.50 ms                                                     | 5.40 ms: 1.58x faster                                                       |
| go                      | 136 ms                                                      | 87.4 ms: 1.56x faster                                                       |
| asyncio_tcp             | 712 ms                                                      | 476 ms: 1.50x faster                                                        |
| raytrace                | 271 ms                                                      | 185 ms: 1.47x faster                                                        |
| scimark_sor             | 105 ms                                                      | 71.7 ms: 1.46x faster                                                       |
| pickle_pure_python      | 257 us                                                      | 176 us: 1.46x faster                                                        |
| generators              | 31.6 ms                                                     | 21.8 ms: 1.45x faster                                                       |
| scimark_lu              | 85.4 ms                                                     | 59.5 ms: 1.44x faster                                                       |
| pyflate                 | 387 ms                                                      | 272 ms: 1.42x faster                                                        |
| chaos                   | 58.9 ms                                                     | 42.5 ms: 1.39x faster                                                       |
| mako                    | 8.80 ms                                                     | 6.36 ms: 1.38x faster                                                       |
| crypto_pyaes            | 62.3 ms                                                     | 45.3 ms: 1.38x faster                                                       |
| hexiom                  | 5.52 ms                                                     | 4.02 ms: 1.37x faster                                                       |
| async_tree_none         | 420 ms                                                      | 306 ms: 1.37x faster                                                        |
| async_tree_io           | 1.07 sec                                                    | 778 ms: 1.37x faster                                                        |
| unpickle_pure_python    | 171 us                                                      | 126 us: 1.35x faster                                                        |
| genshi_text             | 19.0 ms                                                     | 14.2 ms: 1.35x faster                                                       |
| sqlglot_parse           | 1.22 ms                                                     | 908 us: 1.34x faster                                                        |
| async_tree_memoization  | 497 ms                                                      | 372 ms: 1.34x faster                                                        |
| sqlglot_transpile       | 1.46 ms                                                     | 1.10 ms: 1.33x faster                                                       |
| unpack_sequence         | 37.8 ns                                                     | 28.6 ns: 1.32x faster                                                       |
| scimark_monte_carlo     | 55.9 ms                                                     | 42.3 ms: 1.32x faster                                                       |
| django_template         | 28.2 ms                                                     | 21.9 ms: 1.29x faster                                                       |
| thrift                  | 615 us                                                      | 478 us: 1.29x faster                                                        |
| deepcopy_memo           | 28.5 us                                                     | 22.4 us: 1.27x faster                                                       |
| pprint_pformat          | 1.21 sec                                                    | 951 ms: 1.27x faster                                                        |
| html5lib                | 46.5 ms                                                     | 36.7 ms: 1.27x faster                                                       |
| pycparser               | 868 ms                                                      | 686 ms: 1.27x faster                                                        |
| genshi_xml              | 40.5 ms                                                     | 32.1 ms: 1.26x faster                                                       |
| regex_compile           | 103 ms                                                      | 82.1 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed | 609 ms                                                      | 493 ms: 1.24x faster                                                        |
| chameleon               | 5.92 ms                                                     | 4.82 ms: 1.23x faster                                                       |
| pprint_safe_repr        | 589 ms                                                      | 483 ms: 1.22x faster                                                        |
| docutils                | 1.89 sec                                                    | 1.56 sec: 1.21x faster                                                      |
| tornado_http            | 109 ms                                                      | 90.7 ms: 1.20x faster                                                       |
| sqlglot_optimize        | 39.0 ms                                                     | 32.5 ms: 1.20x faster                                                       |
| float                   | 60.2 ms                                                     | 50.4 ms: 1.20x faster                                                       |
| deepcopy                | 255 us                                                      | 218 us: 1.17x faster                                                        |
| sqlglot_normalize       | 202 ms                                                      | 173 ms: 1.17x faster                                                        |
| fannkuch                | 258 ms                                                      | 221 ms: 1.17x faster                                                        |
| 2to3                    | 237 ms                                                      | 203 ms: 1.17x faster                                                        |
| spectral_norm           | 78.0 ms                                                     | 67.4 ms: 1.16x faster                                                       |
| dulwich_log             | 47.6 ms                                                     | 41.2 ms: 1.16x faster                                                       |
| xml_etree_process       | 43.4 ms                                                     | 37.7 ms: 1.15x faster                                                       |
| mdp                     | 1.71 sec                                                    | 1.49 sec: 1.15x faster                                                      |
| nqueens                 | 67.0 ms                                                     | 58.5 ms: 1.15x faster                                                       |
| unpickle                | 9.17 us                                                     | 8.04 us: 1.14x faster                                                       |
| sympy_expand            | 315 ms                                                      | 277 ms: 1.14x faster                                                        |
| sympy_integrate         | 14.8 ms                                                     | 13.1 ms: 1.13x faster                                                       |
| deepcopy_reduce         | 2.16 us                                                     | 1.91 us: 1.13x faster                                                       |
| coroutines              | 15.9 ms                                                     | 14.2 ms: 1.12x faster                                                       |
| create_gc_cycles        | 782 us                                                      | 701 us: 1.11x faster                                                        |
| json_loads              | 14.2 us                                                     | 12.7 us: 1.11x faster                                                       |
| bench_thread_pool       | 946 us                                                      | 852 us: 1.11x faster                                                        |
| xml_etree_parse         | 102 ms                                                      | 92.0 ms: 1.11x faster                                                       |
| json                    | 3.05 ms                                                     | 2.80 ms: 1.09x faster                                                       |
| nbody                   | 69.3 ms                                                     | 64.6 ms: 1.07x faster                                                       |
| regex_dna               | 132 ms                                                      | 123 ms: 1.07x faster                                                        |
| sympy_str               | 188 ms                                                      | 177 ms: 1.07x faster                                                        |
| scimark_fft             | 193 ms                                                      | 182 ms: 1.06x faster                                                        |
| python_startup          | 20.0 ms                                                     | 18.9 ms: 1.06x faster                                                       |
| regex_v8                | 15.0 ms                                                     | 14.3 ms: 1.06x faster                                                       |
| sympy_sum               | 104 ms                                                      | 99.8 ms: 1.04x faster                                                       |
| comprehensions          | 16.0 us                                                     | 15.4 us: 1.04x faster                                                       |
| pathlib                 | 77.4 ms                                                     | 75.0 ms: 1.03x faster                                                       |
| unpickle_list           | 2.81 us                                                     | 2.74 us: 1.03x faster                                                       |
| xml_etree_iterparse     | 63.5 ms                                                     | 62.4 ms: 1.02x faster                                                       |
| logging_format          | 6.66 us                                                     | 6.55 us: 1.02x faster                                                       |
| logging_simple          | 6.20 us                                                     | 6.13 us: 1.01x faster                                                       |
| regex_effbot            | 1.66 ms                                                     | 1.65 ms: 1.01x faster                                                       |
| sqlite_synth            | 1.84 us                                                     | 1.82 us: 1.01x faster                                                       |
| xml_etree_generate      | 54.5 ms                                                     | 53.9 ms: 1.01x faster                                                       |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.64 ms: 1.01x faster                                                       |
| telco                   | 3.78 ms                                                     | 3.81 ms: 1.01x slower                                                       |
| pickle                  | 6.80 us                                                     | 6.91 us: 1.02x slower                                                       |
| pidigits                | 145 ms                                                      | 150 ms: 1.03x slower                                                        |
| python_startup_no_site  | 15.5 ms                                                     | 16.0 ms: 1.03x slower                                                       |
| bench_mp_pool           | 60.7 ms                                                     | 65.7 ms: 1.08x slower                                                       |
| pickle_list             | 2.59 us                                                     | 2.80 us: 1.08x slower                                                       |
| pickle_dict             | 16.9 us                                                     | 18.7 us: 1.11x slower                                                       |
| gc_traversal            | 1.34 ms                                                     | 1.51 ms: 1.12x slower                                                       |
| dask                    | 305 ms                                                      | 356 ms: 1.17x slower                                                        |
| coverage                | 40.0 ms                                                     | 49.1 ms: 1.23x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.19x faster                                                                |

Benchmark hidden because not significant (2): meteor_contest, async_generators
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.13x
