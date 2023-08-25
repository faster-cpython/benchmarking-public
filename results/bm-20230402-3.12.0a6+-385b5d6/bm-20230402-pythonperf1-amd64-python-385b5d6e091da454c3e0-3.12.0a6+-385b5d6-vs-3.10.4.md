
# Results vs. 3.10.4

- fork: python
- ref: 385b5d6e091da454c3e0
- machine: windows-amd64
- commit hash: 385b5d6
- commit date: 2023-04-02
- overall geometric mean: 1.23x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230402-pythonperf1-amd64-python-385b5d6e091da454c3e0-3.12.0a6+-385b5d6 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 202 ms: 1.18x faster                                                        |
| chameleon      | 5.92 ms                                                     | 4.50 ms: 1.32x faster                                                       |
| docutils       | 1.89 sec                                                    | 1.58 sec: 1.20x faster                                                      |
| html5lib       | 46.5 ms                                                     | 35.7 ms: 1.30x faster                                                       |
| tornado_http   | 109 ms                                                      | 87.7 ms: 1.24x faster                                                       |
| Geometric mean | (ref)                                                       | 1.25x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230402-pythonperf1-amd64-python-385b5d6e091da454c3e0-3.12.0a6+-385b5d6 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 69.3 ms                                                     | 53.3 ms: 1.30x faster                                                       |
| float          | 60.2 ms                                                     | 47.4 ms: 1.27x faster                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230402-pythonperf1-amd64-python-385b5d6e091da454c3e0-3.12.0a6+-385b5d6 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 79.5 ms: 1.30x faster                                                       |
| regex_v8       | 15.0 ms                                                     | 13.8 ms: 1.09x faster                                                       |
| regex_dna      | 132 ms                                                      | 123 ms: 1.08x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                       |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230402-pythonperf1-amd64-python-385b5d6e091da454c3e0-3.12.0a6+-385b5d6 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.30 ms: 1.60x faster                                                       |
| pickle_pure_python   | 257 us                                                      | 171 us: 1.51x faster                                                        |
| unpickle_pure_python | 171 us                                                      | 121 us: 1.41x faster                                                        |
| xml_etree_process    | 43.4 ms                                                     | 34.7 ms: 1.25x faster                                                       |
| unpickle             | 9.17 us                                                     | 7.73 us: 1.19x faster                                                       |
| xml_etree_parse      | 102 ms                                                      | 89.7 ms: 1.13x faster                                                       |
| xml_etree_generate   | 54.5 ms                                                     | 50.7 ms: 1.08x faster                                                       |
| xml_etree_iterparse  | 63.5 ms                                                     | 60.4 ms: 1.05x faster                                                       |
| json_loads           | 14.2 us                                                     | 13.5 us: 1.05x faster                                                       |
| unpickle_list        | 2.81 us                                                     | 2.76 us: 1.02x faster                                                       |
| pickle               | 6.80 us                                                     | 7.09 us: 1.04x slower                                                       |
| pickle_list          | 2.59 us                                                     | 2.75 us: 1.06x slower                                                       |
| pickle_dict          | 16.9 us                                                     | 18.9 us: 1.12x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.14x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230402-pythonperf1-amd64-python-385b5d6e091da454c3e0-3.12.0a6+-385b5d6 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 19.0 ms: 1.05x faster                                                       |
| python_startup_no_site | 15.5 ms                                                     | 16.2 ms: 1.04x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.00x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230402-pythonperf1-amd64-python-385b5d6e091da454c3e0-3.12.0a6+-385b5d6 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 19.0 ms                                                     | 13.2 ms: 1.44x faster                                                       |
| mako            | 8.80 ms                                                     | 6.17 ms: 1.43x faster                                                       |
| genshi_xml      | 40.5 ms                                                     | 29.6 ms: 1.37x faster                                                       |
| django_template | 28.2 ms                                                     | 20.7 ms: 1.36x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.40x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230402-pythonperf1-amd64-python-385b5d6e091da454c3e0-3.12.0a6+-385b5d6 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 1.95 ms: 2.13x faster                                                       |
| logging_silent          | 96.4 ns                                                     | 53.8 ns: 1.79x faster                                                       |
| richards                | 41.2 ms                                                     | 24.0 ms: 1.72x faster                                                       |
| scimark_lu              | 85.4 ms                                                     | 50.6 ms: 1.69x faster                                                       |
| go                      | 136 ms                                                      | 82.4 ms: 1.65x faster                                                       |
| mypy2                   | 352 ms                                                      | 217 ms: 1.62x faster                                                        |
| scimark_sor             | 105 ms                                                      | 65.1 ms: 1.61x faster                                                       |
| json_dumps              | 8.50 ms                                                     | 5.30 ms: 1.60x faster                                                       |
| raytrace                | 271 ms                                                      | 169 ms: 1.60x faster                                                        |
| generators              | 31.6 ms                                                     | 20.2 ms: 1.57x faster                                                       |
| pickle_pure_python      | 257 us                                                      | 171 us: 1.51x faster                                                        |
| asyncio_tcp             | 712 ms                                                      | 481 ms: 1.48x faster                                                        |
| scimark_monte_carlo     | 55.9 ms                                                     | 38.0 ms: 1.47x faster                                                       |
| sqlglot_parse           | 1.22 ms                                                     | 832 us: 1.46x faster                                                        |
| hexiom                  | 5.52 ms                                                     | 3.78 ms: 1.46x faster                                                       |
| chaos                   | 58.9 ms                                                     | 40.9 ms: 1.44x faster                                                       |
| genshi_text             | 19.0 ms                                                     | 13.2 ms: 1.44x faster                                                       |
| sqlglot_transpile       | 1.46 ms                                                     | 1.02 ms: 1.44x faster                                                       |
| crypto_pyaes            | 62.3 ms                                                     | 43.4 ms: 1.44x faster                                                       |
| mako                    | 8.80 ms                                                     | 6.17 ms: 1.43x faster                                                       |
| deepcopy_memo           | 28.5 us                                                     | 20.1 us: 1.42x faster                                                       |
| unpickle_pure_python    | 171 us                                                      | 121 us: 1.41x faster                                                        |
| spectral_norm           | 78.0 ms                                                     | 55.4 ms: 1.41x faster                                                       |
| async_tree_io           | 1.07 sec                                                    | 757 ms: 1.41x faster                                                        |
| pyflate                 | 387 ms                                                      | 278 ms: 1.39x faster                                                        |
| unpack_sequence         | 37.8 ns                                                     | 27.4 ns: 1.38x faster                                                       |
| async_tree_memoization  | 497 ms                                                      | 362 ms: 1.37x faster                                                        |
| async_tree_none         | 420 ms                                                      | 306 ms: 1.37x faster                                                        |
| genshi_xml              | 40.5 ms                                                     | 29.6 ms: 1.37x faster                                                       |
| django_template         | 28.2 ms                                                     | 20.7 ms: 1.36x faster                                                       |
| thrift                  | 615 us                                                      | 460 us: 1.34x faster                                                        |
| pprint_pformat          | 1.21 sec                                                    | 906 ms: 1.33x faster                                                        |
| chameleon               | 5.92 ms                                                     | 4.50 ms: 1.32x faster                                                       |
| pycparser               | 868 ms                                                      | 665 ms: 1.30x faster                                                        |
| html5lib                | 46.5 ms                                                     | 35.7 ms: 1.30x faster                                                       |
| regex_compile           | 103 ms                                                      | 79.5 ms: 1.30x faster                                                       |
| pprint_safe_repr        | 589 ms                                                      | 453 ms: 1.30x faster                                                        |
| nbody                   | 69.3 ms                                                     | 53.3 ms: 1.30x faster                                                       |
| async_tree_cpu_io_mixed | 609 ms                                                      | 476 ms: 1.28x faster                                                        |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.09 ms: 1.27x faster                                                       |
| float                   | 60.2 ms                                                     | 47.4 ms: 1.27x faster                                                       |
| sqlglot_optimize        | 39.0 ms                                                     | 30.7 ms: 1.27x faster                                                       |
| scimark_fft             | 193 ms                                                      | 154 ms: 1.25x faster                                                        |
| xml_etree_process       | 43.4 ms                                                     | 34.7 ms: 1.25x faster                                                       |
| deepcopy                | 255 us                                                      | 205 us: 1.24x faster                                                        |
| tornado_http            | 109 ms                                                      | 87.7 ms: 1.24x faster                                                       |
| mdp                     | 1.71 sec                                                    | 1.40 sec: 1.23x faster                                                      |
| sqlglot_normalize       | 202 ms                                                      | 165 ms: 1.22x faster                                                        |
| docutils                | 1.89 sec                                                    | 1.58 sec: 1.20x faster                                                      |
| deepcopy_reduce         | 2.16 us                                                     | 1.80 us: 1.20x faster                                                       |
| unpickle                | 9.17 us                                                     | 7.73 us: 1.19x faster                                                       |
| 2to3                    | 237 ms                                                      | 202 ms: 1.18x faster                                                        |
| nqueens                 | 67.0 ms                                                     | 57.4 ms: 1.17x faster                                                       |
| sympy_integrate         | 14.8 ms                                                     | 12.8 ms: 1.16x faster                                                       |
| coroutines              | 15.9 ms                                                     | 13.8 ms: 1.15x faster                                                       |
| json                    | 3.05 ms                                                     | 2.65 ms: 1.15x faster                                                       |
| fannkuch                | 258 ms                                                      | 225 ms: 1.15x faster                                                        |
| dulwich_log             | 47.6 ms                                                     | 41.6 ms: 1.14x faster                                                       |
| xml_etree_parse         | 102 ms                                                      | 89.7 ms: 1.13x faster                                                       |
| sympy_expand            | 315 ms                                                      | 278 ms: 1.13x faster                                                        |
| bench_thread_pool       | 946 us                                                      | 836 us: 1.13x faster                                                        |
| create_gc_cycles        | 782 us                                                      | 696 us: 1.12x faster                                                        |
| comprehensions          | 16.0 us                                                     | 14.6 us: 1.10x faster                                                       |
| regex_v8                | 15.0 ms                                                     | 13.8 ms: 1.09x faster                                                       |
| async_generators        | 224 ms                                                      | 206 ms: 1.09x faster                                                        |
| sympy_str               | 188 ms                                                      | 175 ms: 1.08x faster                                                        |
| xml_etree_generate      | 54.5 ms                                                     | 50.7 ms: 1.08x faster                                                       |
| regex_dna               | 132 ms                                                      | 123 ms: 1.08x faster                                                        |
| regex_effbot            | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                       |
| sympy_sum               | 104 ms                                                      | 97.7 ms: 1.07x faster                                                       |
| logging_format          | 6.66 us                                                     | 6.29 us: 1.06x faster                                                       |
| xml_etree_iterparse     | 63.5 ms                                                     | 60.4 ms: 1.05x faster                                                       |
| meteor_contest          | 72.5 ms                                                     | 69.1 ms: 1.05x faster                                                       |
| python_startup          | 20.0 ms                                                     | 19.0 ms: 1.05x faster                                                       |
| json_loads              | 14.2 us                                                     | 13.5 us: 1.05x faster                                                       |
| sqlite_synth            | 1.84 us                                                     | 1.78 us: 1.03x faster                                                       |
| logging_simple          | 6.20 us                                                     | 6.02 us: 1.03x faster                                                       |
| unpickle_list           | 2.81 us                                                     | 2.76 us: 1.02x faster                                                       |
| telco                   | 3.78 ms                                                     | 3.92 ms: 1.04x slower                                                       |
| pickle                  | 6.80 us                                                     | 7.09 us: 1.04x slower                                                       |
| python_startup_no_site  | 15.5 ms                                                     | 16.2 ms: 1.04x slower                                                       |
| pickle_list             | 2.59 us                                                     | 2.75 us: 1.06x slower                                                       |
| pathlib                 | 77.4 ms                                                     | 83.9 ms: 1.08x slower                                                       |
| gc_traversal            | 1.34 ms                                                     | 1.47 ms: 1.09x slower                                                       |
| bench_mp_pool           | 60.7 ms                                                     | 66.4 ms: 1.09x slower                                                       |
| pickle_dict             | 16.9 us                                                     | 18.9 us: 1.12x slower                                                       |
| dask                    | 305 ms                                                      | 355 ms: 1.16x slower                                                        |
| coverage                | 40.0 ms                                                     | 52.2 ms: 1.30x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.23x faster                                                                |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.17x
