
# Results vs. 3.10.4

- fork: python
- ref: 702a5bc4637c82dc011e
- machine: windows-amd64
- commit hash: 702a5bc
- commit date: 2022-12-19
- overall geometric mean: 1.18x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221219-pythonperf1-amd64-python-702a5bc4637c82dc011e-3.12.0a3+-702a5bc |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 204 ms: 1.16x faster                                                        |
| chameleon      | 5.92 ms                                                     | 4.63 ms: 1.28x faster                                                       |
| docutils       | 1.89 sec                                                    | 1.59 sec: 1.19x faster                                                      |
| html5lib       | 46.5 ms                                                     | 35.6 ms: 1.30x faster                                                       |
| Geometric mean | (ref)                                                       | 1.23x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221219-pythonperf1-amd64-python-702a5bc4637c82dc011e-3.12.0a3+-702a5bc |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 50.3 ms: 1.20x faster                                                       |
| nbody          | 69.3 ms                                                     | 63.8 ms: 1.09x faster                                                       |
| pidigits       | 145 ms                                                      | 146 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221219-pythonperf1-amd64-python-702a5bc4637c82dc011e-3.12.0a3+-702a5bc |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 85.6 ms: 1.21x faster                                                       |
| regex_v8       | 15.0 ms                                                     | 13.1 ms: 1.15x faster                                                       |
| regex_dna      | 132 ms                                                      | 115 ms: 1.14x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.52 ms: 1.10x faster                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221219-pythonperf1-amd64-python-702a5bc4637c82dc011e-3.12.0a3+-702a5bc |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.48 ms: 1.55x faster                                                       |
| pickle_pure_python   | 257 us                                                      | 183 us: 1.40x faster                                                        |
| unpickle_pure_python | 171 us                                                      | 128 us: 1.34x faster                                                        |
| xml_etree_process    | 43.4 ms                                                     | 35.5 ms: 1.22x faster                                                       |
| unpickle             | 9.17 us                                                     | 8.02 us: 1.14x faster                                                       |
| xml_etree_parse      | 102 ms                                                      | 90.6 ms: 1.12x faster                                                       |
| xml_etree_generate   | 54.5 ms                                                     | 50.0 ms: 1.09x faster                                                       |
| unpickle_list        | 2.81 us                                                     | 2.62 us: 1.07x faster                                                       |
| json_loads           | 14.2 us                                                     | 13.4 us: 1.06x faster                                                       |
| xml_etree_iterparse  | 63.5 ms                                                     | 64.5 ms: 1.02x slower                                                       |
| pickle               | 6.80 us                                                     | 6.99 us: 1.03x slower                                                       |
| pickle_list          | 2.59 us                                                     | 2.79 us: 1.08x slower                                                       |
| pickle_dict          | 16.9 us                                                     | 19.0 us: 1.12x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221219-pythonperf1-amd64-python-702a5bc4637c82dc011e-3.12.0a3+-702a5bc |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 18.9 ms: 1.06x faster                                                       |
| python_startup_no_site | 15.5 ms                                                     | 15.7 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221219-pythonperf1-amd64-python-702a5bc4637c82dc011e-3.12.0a3+-702a5bc |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 8.80 ms                                                     | 6.31 ms: 1.40x faster                                                       |
| genshi_text     | 19.0 ms                                                     | 14.3 ms: 1.33x faster                                                       |
| django_template | 28.2 ms                                                     | 21.8 ms: 1.30x faster                                                       |
| genshi_xml      | 40.5 ms                                                     | 34.2 ms: 1.18x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.30x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221219-pythonperf1-amd64-python-702a5bc4637c82dc011e-3.12.0a3+-702a5bc |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 2.18 ms: 1.91x faster                                                       |
| logging_silent          | 96.4 ns                                                     | 59.1 ns: 1.63x faster                                                       |
| mypy2                   | 352 ms                                                      | 223 ms: 1.58x faster                                                        |
| richards                | 41.2 ms                                                     | 26.4 ms: 1.56x faster                                                       |
| json_dumps              | 8.50 ms                                                     | 5.48 ms: 1.55x faster                                                       |
| go                      | 136 ms                                                      | 88.8 ms: 1.53x faster                                                       |
| scimark_sor             | 105 ms                                                      | 69.9 ms: 1.50x faster                                                       |
| scimark_lu              | 85.4 ms                                                     | 57.7 ms: 1.48x faster                                                       |
| asyncio_tcp             | 712 ms                                                      | 486 ms: 1.47x faster                                                        |
| raytrace                | 271 ms                                                      | 190 ms: 1.42x faster                                                        |
| pickle_pure_python      | 257 us                                                      | 183 us: 1.40x faster                                                        |
| mako                    | 8.80 ms                                                     | 6.31 ms: 1.40x faster                                                       |
| scimark_monte_carlo     | 55.9 ms                                                     | 40.1 ms: 1.39x faster                                                       |
| pyflate                 | 387 ms                                                      | 281 ms: 1.38x faster                                                        |
| sqlglot_parse           | 1.22 ms                                                     | 900 us: 1.35x faster                                                        |
| unpickle_pure_python    | 171 us                                                      | 128 us: 1.34x faster                                                        |
| hexiom                  | 5.52 ms                                                     | 4.13 ms: 1.34x faster                                                       |
| crypto_pyaes            | 62.3 ms                                                     | 46.8 ms: 1.33x faster                                                       |
| genshi_text             | 19.0 ms                                                     | 14.3 ms: 1.33x faster                                                       |
| sqlglot_transpile       | 1.46 ms                                                     | 1.10 ms: 1.33x faster                                                       |
| async_tree_io           | 1.07 sec                                                    | 807 ms: 1.32x faster                                                        |
| deepcopy_memo           | 28.5 us                                                     | 21.7 us: 1.31x faster                                                       |
| html5lib                | 46.5 ms                                                     | 35.6 ms: 1.30x faster                                                       |
| thrift                  | 615 us                                                      | 473 us: 1.30x faster                                                        |
| django_template         | 28.2 ms                                                     | 21.8 ms: 1.30x faster                                                       |
| async_tree_memoization  | 497 ms                                                      | 386 ms: 1.29x faster                                                        |
| pycparser               | 868 ms                                                      | 675 ms: 1.29x faster                                                        |
| unpack_sequence         | 37.8 ns                                                     | 29.5 ns: 1.28x faster                                                       |
| chameleon               | 5.92 ms                                                     | 4.63 ms: 1.28x faster                                                       |
| spectral_norm           | 78.0 ms                                                     | 61.3 ms: 1.27x faster                                                       |
| chaos                   | 58.9 ms                                                     | 46.5 ms: 1.27x faster                                                       |
| pprint_pformat          | 1.21 sec                                                    | 953 ms: 1.27x faster                                                        |
| async_tree_none         | 420 ms                                                      | 334 ms: 1.26x faster                                                        |
| pprint_safe_repr        | 589 ms                                                      | 469 ms: 1.26x faster                                                        |
| async_generators        | 224 ms                                                      | 181 ms: 1.23x faster                                                        |
| xml_etree_process       | 43.4 ms                                                     | 35.5 ms: 1.22x faster                                                       |
| async_tree_cpu_io_mixed | 609 ms                                                      | 499 ms: 1.22x faster                                                        |
| regex_compile           | 103 ms                                                      | 85.6 ms: 1.21x faster                                                       |
| float                   | 60.2 ms                                                     | 50.3 ms: 1.20x faster                                                       |
| deepcopy                | 255 us                                                      | 215 us: 1.19x faster                                                        |
| docutils                | 1.89 sec                                                    | 1.59 sec: 1.19x faster                                                      |
| genshi_xml              | 40.5 ms                                                     | 34.2 ms: 1.18x faster                                                       |
| dask                    | 305 ms                                                      | 261 ms: 1.17x faster                                                        |
| sqlglot_optimize        | 39.0 ms                                                     | 33.5 ms: 1.16x faster                                                       |
| 2to3                    | 237 ms                                                      | 204 ms: 1.16x faster                                                        |
| create_gc_cycles        | 782 us                                                      | 677 us: 1.15x faster                                                        |
| regex_v8                | 15.0 ms                                                     | 13.1 ms: 1.15x faster                                                       |
| unpickle                | 9.17 us                                                     | 8.02 us: 1.14x faster                                                       |
| regex_dna               | 132 ms                                                      | 115 ms: 1.14x faster                                                        |
| dulwich_log             | 47.6 ms                                                     | 42.0 ms: 1.13x faster                                                       |
| deepcopy_reduce         | 2.16 us                                                     | 1.92 us: 1.12x faster                                                       |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.37 ms: 1.12x faster                                                       |
| xml_etree_parse         | 102 ms                                                      | 90.6 ms: 1.12x faster                                                       |
| sympy_integrate         | 14.8 ms                                                     | 13.3 ms: 1.12x faster                                                       |
| nqueens                 | 67.0 ms                                                     | 60.1 ms: 1.12x faster                                                       |
| sqlglot_normalize       | 202 ms                                                      | 182 ms: 1.11x faster                                                        |
| bench_thread_pool       | 946 us                                                      | 855 us: 1.11x faster                                                        |
| mdp                     | 1.71 sec                                                    | 1.55 sec: 1.11x faster                                                      |
| fannkuch                | 258 ms                                                      | 233 ms: 1.10x faster                                                        |
| sympy_expand            | 315 ms                                                      | 286 ms: 1.10x faster                                                        |
| regex_effbot            | 1.66 ms                                                     | 1.52 ms: 1.10x faster                                                       |
| xml_etree_generate      | 54.5 ms                                                     | 50.0 ms: 1.09x faster                                                       |
| json                    | 3.05 ms                                                     | 2.80 ms: 1.09x faster                                                       |
| nbody                   | 69.3 ms                                                     | 63.8 ms: 1.09x faster                                                       |
| scimark_fft             | 193 ms                                                      | 179 ms: 1.08x faster                                                        |
| unpickle_list           | 2.81 us                                                     | 2.62 us: 1.07x faster                                                       |
| json_loads              | 14.2 us                                                     | 13.4 us: 1.06x faster                                                       |
| python_startup          | 20.0 ms                                                     | 18.9 ms: 1.06x faster                                                       |
| coroutines              | 15.9 ms                                                     | 15.1 ms: 1.05x faster                                                       |
| sympy_str               | 188 ms                                                      | 179 ms: 1.05x faster                                                        |
| sympy_sum               | 104 ms                                                      | 99.7 ms: 1.04x faster                                                       |
| sqlite_synth            | 1.84 us                                                     | 1.78 us: 1.03x faster                                                       |
| pathlib                 | 77.4 ms                                                     | 75.7 ms: 1.02x faster                                                       |
| pidigits                | 145 ms                                                      | 146 ms: 1.01x slower                                                        |
| meteor_contest          | 72.5 ms                                                     | 73.1 ms: 1.01x slower                                                       |
| python_startup_no_site  | 15.5 ms                                                     | 15.7 ms: 1.01x slower                                                       |
| xml_etree_iterparse     | 63.5 ms                                                     | 64.5 ms: 1.02x slower                                                       |
| telco                   | 3.78 ms                                                     | 3.86 ms: 1.02x slower                                                       |
| logging_format          | 6.66 us                                                     | 6.82 us: 1.02x slower                                                       |
| pickle                  | 6.80 us                                                     | 6.99 us: 1.03x slower                                                       |
| bench_mp_pool           | 60.7 ms                                                     | 63.2 ms: 1.04x slower                                                       |
| pickle_list             | 2.59 us                                                     | 2.79 us: 1.08x slower                                                       |
| gc_traversal            | 1.34 ms                                                     | 1.48 ms: 1.10x slower                                                       |
| pickle_dict             | 16.9 us                                                     | 19.0 us: 1.12x slower                                                       |
| generators              | 31.6 ms                                                     | 38.7 ms: 1.23x slower                                                       |
| coverage                | 40.0 ms                                                     | 54.0 ms: 1.35x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.18x faster                                                                |

Benchmark hidden because not significant (2): comprehensions, logging_simple
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x
