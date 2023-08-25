
# Results vs. 3.10.4

- fork: python
- ref: 6dedf42527fddbed8ef6
- machine: windows-amd64
- commit hash: 6dedf42
- commit date: 2022-11-10
- overall geometric mean: 1.17x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221110-pythonperf1-amd64-python-6dedf42527fddbed8ef6-3.12.0a1+-6dedf42 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 198 ms: 1.20x faster                                                        |
| chameleon      | 5.92 ms                                                     | 4.64 ms: 1.28x faster                                                       |
| docutils       | 1.89 sec                                                    | 1.60 sec: 1.19x faster                                                      |
| html5lib       | 46.5 ms                                                     | 35.4 ms: 1.31x faster                                                       |
| tornado_http   | 109 ms                                                      | 93.3 ms: 1.17x faster                                                       |
| Geometric mean | (ref)                                                       | 1.23x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221110-pythonperf1-amd64-python-6dedf42527fddbed8ef6-3.12.0a1+-6dedf42 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 51.1 ms: 1.18x faster                                                       |
| nbody          | 69.3 ms                                                     | 63.7 ms: 1.09x faster                                                       |
| pidigits       | 145 ms                                                      | 151 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221110-pythonperf1-amd64-python-6dedf42527fddbed8ef6-3.12.0a1+-6dedf42 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 85.8 ms: 1.21x faster                                                       |
| regex_dna      | 132 ms                                                      | 124 ms: 1.06x faster                                                        |
| regex_v8       | 15.0 ms                                                     | 14.4 ms: 1.05x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.64 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221110-pythonperf1-amd64-python-6dedf42527fddbed8ef6-3.12.0a1+-6dedf42 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.26 ms: 1.62x faster                                                       |
| pickle_pure_python   | 257 us                                                      | 188 us: 1.37x faster                                                        |
| unpickle_pure_python | 171 us                                                      | 128 us: 1.33x faster                                                        |
| xml_etree_process    | 43.4 ms                                                     | 35.4 ms: 1.23x faster                                                       |
| unpickle             | 9.17 us                                                     | 8.11 us: 1.13x faster                                                       |
| xml_etree_parse      | 102 ms                                                      | 90.3 ms: 1.13x faster                                                       |
| json_loads           | 14.2 us                                                     | 13.0 us: 1.09x faster                                                       |
| unpickle_list        | 2.81 us                                                     | 2.59 us: 1.09x faster                                                       |
| xml_etree_generate   | 54.5 ms                                                     | 51.3 ms: 1.06x faster                                                       |
| pickle               | 6.80 us                                                     | 6.74 us: 1.01x faster                                                       |
| pickle_list          | 2.59 us                                                     | 2.76 us: 1.07x slower                                                       |
| pickle_dict          | 16.9 us                                                     | 18.9 us: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.13x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221110-pythonperf1-amd64-python-6dedf42527fddbed8ef6-3.12.0a1+-6dedf42 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 18.6 ms: 1.07x faster                                                       |
| python_startup_no_site | 15.5 ms                                                     | 15.8 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.03x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221110-pythonperf1-amd64-python-6dedf42527fddbed8ef6-3.12.0a1+-6dedf42 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 8.80 ms                                                     | 6.40 ms: 1.38x faster                                                       |
| django_template | 28.2 ms                                                     | 21.9 ms: 1.29x faster                                                       |
| genshi_text     | 19.0 ms                                                     | 14.9 ms: 1.28x faster                                                       |
| genshi_xml      | 40.5 ms                                                     | 34.0 ms: 1.19x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.28x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221110-pythonperf1-amd64-python-6dedf42527fddbed8ef6-3.12.0a1+-6dedf42 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 2.31 ms: 1.81x faster                                                       |
| json_dumps              | 8.50 ms                                                     | 5.26 ms: 1.62x faster                                                       |
| mypy2                   | 352 ms                                                      | 223 ms: 1.58x faster                                                        |
| logging_silent          | 96.4 ns                                                     | 61.2 ns: 1.58x faster                                                       |
| go                      | 136 ms                                                      | 88.7 ms: 1.53x faster                                                       |
| richards                | 41.2 ms                                                     | 27.1 ms: 1.52x faster                                                       |
| scimark_sor             | 105 ms                                                      | 70.5 ms: 1.49x faster                                                       |
| scimark_lu              | 85.4 ms                                                     | 58.4 ms: 1.46x faster                                                       |
| scimark_monte_carlo     | 55.9 ms                                                     | 39.0 ms: 1.43x faster                                                       |
| raytrace                | 271 ms                                                      | 192 ms: 1.41x faster                                                        |
| pyflate                 | 387 ms                                                      | 275 ms: 1.41x faster                                                        |
| mako                    | 8.80 ms                                                     | 6.40 ms: 1.38x faster                                                       |
| pickle_pure_python      | 257 us                                                      | 188 us: 1.37x faster                                                        |
| crypto_pyaes            | 62.3 ms                                                     | 45.7 ms: 1.36x faster                                                       |
| async_tree_io           | 1.07 sec                                                    | 790 ms: 1.35x faster                                                        |
| unpickle_pure_python    | 171 us                                                      | 128 us: 1.33x faster                                                        |
| sqlglot_parse           | 1.22 ms                                                     | 918 us: 1.33x faster                                                        |
| sqlglot_transpile       | 1.46 ms                                                     | 1.10 ms: 1.33x faster                                                       |
| hexiom                  | 5.52 ms                                                     | 4.17 ms: 1.32x faster                                                       |
| async_tree_none         | 420 ms                                                      | 319 ms: 1.32x faster                                                        |
| html5lib                | 46.5 ms                                                     | 35.4 ms: 1.31x faster                                                       |
| pycparser               | 868 ms                                                      | 665 ms: 1.30x faster                                                        |
| chaos                   | 58.9 ms                                                     | 45.5 ms: 1.29x faster                                                       |
| thrift                  | 615 us                                                      | 478 us: 1.29x faster                                                        |
| django_template         | 28.2 ms                                                     | 21.9 ms: 1.29x faster                                                       |
| genshi_text             | 19.0 ms                                                     | 14.9 ms: 1.28x faster                                                       |
| chameleon               | 5.92 ms                                                     | 4.64 ms: 1.28x faster                                                       |
| async_tree_memoization  | 497 ms                                                      | 391 ms: 1.27x faster                                                        |
| deepcopy_memo           | 28.5 us                                                     | 22.6 us: 1.26x faster                                                       |
| pprint_safe_repr        | 589 ms                                                      | 476 ms: 1.24x faster                                                        |
| pprint_pformat          | 1.21 sec                                                    | 979 ms: 1.23x faster                                                        |
| xml_etree_process       | 43.4 ms                                                     | 35.4 ms: 1.23x faster                                                       |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.17 ms: 1.22x faster                                                       |
| spectral_norm           | 78.0 ms                                                     | 63.8 ms: 1.22x faster                                                       |
| async_generators        | 224 ms                                                      | 183 ms: 1.22x faster                                                        |
| regex_compile           | 103 ms                                                      | 85.8 ms: 1.21x faster                                                       |
| 2to3                    | 237 ms                                                      | 198 ms: 1.20x faster                                                        |
| genshi_xml              | 40.5 ms                                                     | 34.0 ms: 1.19x faster                                                       |
| async_tree_cpu_io_mixed | 609 ms                                                      | 511 ms: 1.19x faster                                                        |
| docutils                | 1.89 sec                                                    | 1.60 sec: 1.19x faster                                                      |
| unpack_sequence         | 37.8 ns                                                     | 32.0 ns: 1.18x faster                                                       |
| float                   | 60.2 ms                                                     | 51.1 ms: 1.18x faster                                                       |
| tornado_http            | 109 ms                                                      | 93.3 ms: 1.17x faster                                                       |
| sqlglot_optimize        | 39.0 ms                                                     | 33.6 ms: 1.16x faster                                                       |
| dask                    | 305 ms                                                      | 263 ms: 1.16x faster                                                        |
| create_gc_cycles        | 782 us                                                      | 684 us: 1.14x faster                                                        |
| fannkuch                | 258 ms                                                      | 228 ms: 1.13x faster                                                        |
| unpickle                | 9.17 us                                                     | 8.11 us: 1.13x faster                                                       |
| dulwich_log             | 47.6 ms                                                     | 42.1 ms: 1.13x faster                                                       |
| bench_thread_pool       | 946 us                                                      | 838 us: 1.13x faster                                                        |
| json                    | 3.05 ms                                                     | 2.70 ms: 1.13x faster                                                       |
| scimark_fft             | 193 ms                                                      | 171 ms: 1.13x faster                                                        |
| xml_etree_parse         | 102 ms                                                      | 90.3 ms: 1.13x faster                                                       |
| sqlglot_normalize       | 202 ms                                                      | 182 ms: 1.11x faster                                                        |
| nqueens                 | 67.0 ms                                                     | 60.6 ms: 1.11x faster                                                       |
| deepcopy                | 255 us                                                      | 231 us: 1.11x faster                                                        |
| sympy_integrate         | 14.8 ms                                                     | 13.4 ms: 1.10x faster                                                       |
| mdp                     | 1.71 sec                                                    | 1.55 sec: 1.10x faster                                                      |
| json_loads              | 14.2 us                                                     | 13.0 us: 1.09x faster                                                       |
| deepcopy_reduce         | 2.16 us                                                     | 1.97 us: 1.09x faster                                                       |
| nbody                   | 69.3 ms                                                     | 63.7 ms: 1.09x faster                                                       |
| unpickle_list           | 2.81 us                                                     | 2.59 us: 1.09x faster                                                       |
| sympy_expand            | 315 ms                                                      | 292 ms: 1.08x faster                                                        |
| python_startup          | 20.0 ms                                                     | 18.6 ms: 1.07x faster                                                       |
| sympy_str               | 188 ms                                                      | 176 ms: 1.07x faster                                                        |
| sqlite_synth            | 1.84 us                                                     | 1.72 us: 1.07x faster                                                       |
| regex_dna               | 132 ms                                                      | 124 ms: 1.06x faster                                                        |
| xml_etree_generate      | 54.5 ms                                                     | 51.3 ms: 1.06x faster                                                       |
| coroutines              | 15.9 ms                                                     | 15.0 ms: 1.06x faster                                                       |
| sympy_sum               | 104 ms                                                      | 99.0 ms: 1.05x faster                                                       |
| pathlib                 | 77.4 ms                                                     | 73.7 ms: 1.05x faster                                                       |
| regex_v8                | 15.0 ms                                                     | 14.4 ms: 1.05x faster                                                       |
| telco                   | 3.78 ms                                                     | 3.70 ms: 1.02x faster                                                       |
| regex_effbot            | 1.66 ms                                                     | 1.64 ms: 1.01x faster                                                       |
| pickle                  | 6.80 us                                                     | 6.74 us: 1.01x faster                                                       |
| meteor_contest          | 72.5 ms                                                     | 73.4 ms: 1.01x slower                                                       |
| logging_simple          | 6.20 us                                                     | 6.29 us: 1.02x slower                                                       |
| python_startup_no_site  | 15.5 ms                                                     | 15.8 ms: 1.02x slower                                                       |
| comprehensions          | 16.0 us                                                     | 16.3 us: 1.02x slower                                                       |
| logging_format          | 6.66 us                                                     | 6.81 us: 1.02x slower                                                       |
| bench_mp_pool           | 60.7 ms                                                     | 62.8 ms: 1.03x slower                                                       |
| pidigits                | 145 ms                                                      | 151 ms: 1.04x slower                                                        |
| pickle_list             | 2.59 us                                                     | 2.76 us: 1.07x slower                                                       |
| gc_traversal            | 1.34 ms                                                     | 1.47 ms: 1.10x slower                                                       |
| pickle_dict             | 16.9 us                                                     | 18.9 us: 1.11x slower                                                       |
| generators              | 31.6 ms                                                     | 37.0 ms: 1.17x slower                                                       |
| coverage                | 40.0 ms                                                     | 54.4 ms: 1.36x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.17x faster                                                                |

Benchmark hidden because not significant (2): xml_etree_iterparse, asyncio_tcp
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.12x
