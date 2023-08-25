
# Results vs. 3.10.4

- fork: python
- ref: v3.11.0b2
- machine: windows-amd64
- commit hash: 72f00f4
- commit date: 2022-05-30
- overall geometric mean: 1.06x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-pythonperf1-amd64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 211 ms: 1.12x faster                                            |
| chameleon      | 5.92 ms                                                     | 5.59 ms: 1.06x faster                                           |
| docutils       | 1.89 sec                                                    | 1.66 sec: 1.14x faster                                          |
| html5lib       | 46.5 ms                                                     | 41.4 ms: 1.12x faster                                           |
| tornado_http   | 109 ms                                                      | 95.3 ms: 1.14x faster                                           |
| Geometric mean | (ref)                                                       | 1.12x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-pythonperf1-amd64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 54.5 ms: 1.10x faster                                           |
| nbody          | 69.3 ms                                                     | 70.1 ms: 1.01x slower                                           |
| pidigits       | 145 ms                                                      | 153 ms: 1.05x slower                                            |
| Geometric mean | (ref)                                                       | 1.01x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-pythonperf1-amd64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 1.66 ms                                                     | 1.39 ms: 1.20x faster                                           |
| regex_dna      | 132 ms                                                      | 120 ms: 1.10x faster                                            |
| regex_compile  | 103 ms                                                      | 97.0 ms: 1.07x faster                                           |
| regex_v8       | 15.0 ms                                                     | 14.4 ms: 1.04x faster                                           |
| Geometric mean | (ref)                                                       | 1.10x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-pythonperf1-amd64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| pickle_pure_python   | 257 us                                                      | 216 us: 1.19x faster                                            |
| unpickle             | 9.17 us                                                     | 8.07 us: 1.14x faster                                           |
| xml_etree_process    | 43.4 ms                                                     | 39.1 ms: 1.11x faster                                           |
| xml_etree_parse      | 102 ms                                                      | 96.7 ms: 1.05x faster                                           |
| unpickle_pure_python | 171 us                                                      | 164 us: 1.04x faster                                            |
| json_dumps           | 8.50 ms                                                     | 8.21 ms: 1.04x faster                                           |
| xml_etree_iterparse  | 63.5 ms                                                     | 62.0 ms: 1.02x faster                                           |
| unpickle_list        | 2.81 us                                                     | 2.76 us: 1.02x faster                                           |
| pickle               | 6.80 us                                                     | 6.74 us: 1.01x faster                                           |
| xml_etree_generate   | 54.5 ms                                                     | 54.1 ms: 1.01x faster                                           |
| json_loads           | 14.2 us                                                     | 14.1 us: 1.01x faster                                           |
| pickle_list          | 2.59 us                                                     | 2.64 us: 1.02x slower                                           |
| pickle_dict          | 16.9 us                                                     | 17.4 us: 1.03x slower                                           |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-pythonperf1-amd64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 19.0 ms: 1.05x faster                                           |
| python_startup_no_site | 15.5 ms                                                     | 15.8 ms: 1.02x slower                                           |
| Geometric mean         | (ref)                                                       | 1.01x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-pythonperf1-amd64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 8.80 ms                                                     | 7.62 ms: 1.16x faster                                           |
| django_template | 28.2 ms                                                     | 25.1 ms: 1.13x faster                                           |
| genshi_text     | 19.0 ms                                                     | 17.9 ms: 1.06x faster                                           |
| Geometric mean  | (ref)                                                       | 1.09x faster                                                    |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-pythonperf1-amd64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 2.72 ms: 1.53x faster                                           |
| go                      | 136 ms                                                      | 100 ms: 1.36x faster                                            |
| async_tree_io           | 1.07 sec                                                    | 794 ms: 1.34x faster                                            |
| logging_silent          | 96.4 ns                                                     | 72.2 ns: 1.33x faster                                           |
| scimark_lu              | 85.4 ms                                                     | 64.6 ms: 1.32x faster                                           |
| scimark_sor             | 105 ms                                                      | 80.0 ms: 1.31x faster                                           |
| richards                | 41.2 ms                                                     | 31.6 ms: 1.30x faster                                           |
| raytrace                | 271 ms                                                      | 213 ms: 1.27x faster                                            |
| async_tree_none         | 420 ms                                                      | 336 ms: 1.25x faster                                            |
| async_tree_memoization  | 497 ms                                                      | 400 ms: 1.24x faster                                            |
| pyflate                 | 387 ms                                                      | 314 ms: 1.23x faster                                            |
| scimark_monte_carlo     | 55.9 ms                                                     | 46.0 ms: 1.21x faster                                           |
| crypto_pyaes            | 62.3 ms                                                     | 51.8 ms: 1.20x faster                                           |
| regex_effbot            | 1.66 ms                                                     | 1.39 ms: 1.20x faster                                           |
| async_generators        | 224 ms                                                      | 187 ms: 1.20x faster                                            |
| mypy2                   | 352 ms                                                      | 295 ms: 1.19x faster                                            |
| thrift                  | 615 us                                                      | 516 us: 1.19x faster                                            |
| pickle_pure_python      | 257 us                                                      | 216 us: 1.19x faster                                            |
| async_tree_cpu_io_mixed | 609 ms                                                      | 520 ms: 1.17x faster                                            |
| create_gc_cycles        | 782 us                                                      | 675 us: 1.16x faster                                            |
| pycparser               | 868 ms                                                      | 750 ms: 1.16x faster                                            |
| mako                    | 8.80 ms                                                     | 7.62 ms: 1.16x faster                                           |
| sqlalchemy_declarative  | 95.4 ms                                                     | 83.2 ms: 1.15x faster                                           |
| tornado_http            | 109 ms                                                      | 95.3 ms: 1.14x faster                                           |
| docutils                | 1.89 sec                                                    | 1.66 sec: 1.14x faster                                          |
| hexiom                  | 5.52 ms                                                     | 4.84 ms: 1.14x faster                                           |
| unpickle                | 9.17 us                                                     | 8.07 us: 1.14x faster                                           |
| chaos                   | 58.9 ms                                                     | 51.8 ms: 1.14x faster                                           |
| django_template         | 28.2 ms                                                     | 25.1 ms: 1.13x faster                                           |
| html5lib                | 46.5 ms                                                     | 41.4 ms: 1.12x faster                                           |
| 2to3                    | 237 ms                                                      | 211 ms: 1.12x faster                                            |
| xml_etree_process       | 43.4 ms                                                     | 39.1 ms: 1.11x faster                                           |
| spectral_norm           | 78.0 ms                                                     | 70.6 ms: 1.10x faster                                           |
| float                   | 60.2 ms                                                     | 54.5 ms: 1.10x faster                                           |
| regex_dna               | 132 ms                                                      | 120 ms: 1.10x faster                                            |
| aiohttp                 | 1.01 ms                                                     | 921 us: 1.09x faster                                            |
| deepcopy_memo           | 28.5 us                                                     | 26.1 us: 1.09x faster                                           |
| dask                    | 305 ms                                                      | 280 ms: 1.09x faster                                            |
| pprint_pformat          | 1.21 sec                                                    | 1.11 sec: 1.08x faster                                          |
| pprint_safe_repr        | 589 ms                                                      | 548 ms: 1.08x faster                                            |
| sqlite_synth            | 1.84 us                                                     | 1.71 us: 1.08x faster                                           |
| regex_compile           | 103 ms                                                      | 97.0 ms: 1.07x faster                                           |
| genshi_text             | 19.0 ms                                                     | 17.9 ms: 1.06x faster                                           |
| bench_thread_pool       | 946 us                                                      | 889 us: 1.06x faster                                            |
| chameleon               | 5.92 ms                                                     | 5.59 ms: 1.06x faster                                           |
| xml_etree_parse         | 102 ms                                                      | 96.7 ms: 1.05x faster                                           |
| python_startup          | 20.0 ms                                                     | 19.0 ms: 1.05x faster                                           |
| pylint                  | 347 ms                                                      | 331 ms: 1.05x faster                                            |
| sqlalchemy_imperative   | 11.0 ms                                                     | 10.5 ms: 1.05x faster                                           |
| logging_simple          | 6.20 us                                                     | 5.94 us: 1.04x faster                                           |
| unpickle_pure_python    | 171 us                                                      | 164 us: 1.04x faster                                            |
| sympy_integrate         | 14.8 ms                                                     | 14.2 ms: 1.04x faster                                           |
| logging_format          | 6.66 us                                                     | 6.39 us: 1.04x faster                                           |
| regex_v8                | 15.0 ms                                                     | 14.4 ms: 1.04x faster                                           |
| sqlglot_optimize        | 39.0 ms                                                     | 37.5 ms: 1.04x faster                                           |
| json_dumps              | 8.50 ms                                                     | 8.21 ms: 1.04x faster                                           |
| pathlib                 | 77.4 ms                                                     | 74.8 ms: 1.03x faster                                           |
| dulwich_log             | 47.6 ms                                                     | 46.1 ms: 1.03x faster                                           |
| sqlglot_transpile       | 1.46 ms                                                     | 1.42 ms: 1.03x faster                                           |
| xml_etree_iterparse     | 63.5 ms                                                     | 62.0 ms: 1.02x faster                                           |
| coroutines              | 15.9 ms                                                     | 15.6 ms: 1.02x faster                                           |
| unpickle_list           | 2.81 us                                                     | 2.76 us: 1.02x faster                                           |
| sympy_sum               | 104 ms                                                      | 103 ms: 1.01x faster                                            |
| scimark_fft             | 193 ms                                                      | 191 ms: 1.01x faster                                            |
| sqlglot_parse           | 1.22 ms                                                     | 1.21 ms: 1.01x faster                                           |
| pickle                  | 6.80 us                                                     | 6.74 us: 1.01x faster                                           |
| sympy_expand            | 315 ms                                                      | 312 ms: 1.01x faster                                            |
| xml_etree_generate      | 54.5 ms                                                     | 54.1 ms: 1.01x faster                                           |
| json_loads              | 14.2 us                                                     | 14.1 us: 1.01x faster                                           |
| sympy_str               | 188 ms                                                      | 190 ms: 1.01x slower                                            |
| nbody                   | 69.3 ms                                                     | 70.1 ms: 1.01x slower                                           |
| deepcopy_reduce         | 2.16 us                                                     | 2.19 us: 1.02x slower                                           |
| python_startup_no_site  | 15.5 ms                                                     | 15.8 ms: 1.02x slower                                           |
| pickle_list             | 2.59 us                                                     | 2.64 us: 1.02x slower                                           |
| deepcopy                | 255 us                                                      | 261 us: 1.02x slower                                            |
| mdp                     | 1.71 sec                                                    | 1.75 sec: 1.02x slower                                          |
| nqueens                 | 67.0 ms                                                     | 68.9 ms: 1.03x slower                                           |
| pickle_dict             | 16.9 us                                                     | 17.4 us: 1.03x slower                                           |
| fannkuch                | 258 ms                                                      | 266 ms: 1.03x slower                                            |
| asyncio_tcp             | 712 ms                                                      | 742 ms: 1.04x slower                                            |
| bench_mp_pool           | 60.7 ms                                                     | 63.3 ms: 1.04x slower                                           |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.77 ms: 1.04x slower                                           |
| pidigits                | 145 ms                                                      | 153 ms: 1.05x slower                                            |
| json                    | 3.05 ms                                                     | 3.23 ms: 1.06x slower                                           |
| telco                   | 3.78 ms                                                     | 4.05 ms: 1.07x slower                                           |
| gc_traversal            | 1.34 ms                                                     | 1.46 ms: 1.08x slower                                           |
| meteor_contest          | 72.5 ms                                                     | 78.7 ms: 1.09x slower                                           |
| generators              | 31.6 ms                                                     | 35.7 ms: 1.13x slower                                           |
| comprehensions          | 16.0 us                                                     | 18.2 us: 1.14x slower                                           |
| unpack_sequence         | 37.8 ns                                                     | 44.3 ns: 1.17x slower                                           |
| coverage                | 40.0 ms                                                     | 106 ms: 2.64x slower                                            |
| Geometric mean          | (ref)                                                       | 1.06x faster                                                    |

Benchmark hidden because not significant (2): genshi_xml, sqlglot_normalize
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x
