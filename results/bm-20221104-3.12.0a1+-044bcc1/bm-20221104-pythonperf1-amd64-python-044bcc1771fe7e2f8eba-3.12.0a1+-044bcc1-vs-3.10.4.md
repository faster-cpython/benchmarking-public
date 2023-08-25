
# Results vs. 3.10.4

- fork: python
- ref: 044bcc1771fe7e2f8eba
- machine: windows-amd64
- commit hash: 044bcc1
- commit date: 2022-11-04
- overall geometric mean: 1.12x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221104-pythonperf1-amd64-python-044bcc1771fe7e2f8eba-3.12.0a1+-044bcc1 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 207 ms: 1.14x faster                                                        |
| chameleon      | 5.92 ms                                                     | 5.21 ms: 1.14x faster                                                       |
| docutils       | 1.89 sec                                                    | 1.62 sec: 1.17x faster                                                      |
| html5lib       | 46.5 ms                                                     | 36.7 ms: 1.26x faster                                                       |
| tornado_http   | 109 ms                                                      | 92.6 ms: 1.18x faster                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221104-pythonperf1-amd64-python-044bcc1771fe7e2f8eba-3.12.0a1+-044bcc1 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 55.8 ms: 1.08x faster                                                       |
| nbody          | 69.3 ms                                                     | 65.2 ms: 1.06x faster                                                       |
| pidigits       | 145 ms                                                      | 149 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221104-pythonperf1-amd64-python-044bcc1771fe7e2f8eba-3.12.0a1+-044bcc1 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 86.9 ms: 1.19x faster                                                       |
| regex_dna      | 132 ms                                                      | 123 ms: 1.07x faster                                                        |
| regex_v8       | 15.0 ms                                                     | 14.2 ms: 1.06x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.62 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221104-pythonperf1-amd64-python-044bcc1771fe7e2f8eba-3.12.0a1+-044bcc1 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.56 ms: 1.53x faster                                                       |
| pickle_pure_python   | 257 us                                                      | 205 us: 1.25x faster                                                        |
| unpickle_pure_python | 171 us                                                      | 143 us: 1.20x faster                                                        |
| xml_etree_process    | 43.4 ms                                                     | 37.4 ms: 1.16x faster                                                       |
| xml_etree_parse      | 102 ms                                                      | 89.9 ms: 1.13x faster                                                       |
| json_loads           | 14.2 us                                                     | 13.3 us: 1.07x faster                                                       |
| unpickle_list        | 2.81 us                                                     | 2.63 us: 1.07x faster                                                       |
| xml_etree_generate   | 54.5 ms                                                     | 52.4 ms: 1.04x faster                                                       |
| pickle               | 6.80 us                                                     | 6.92 us: 1.02x slower                                                       |
| xml_etree_iterparse  | 63.5 ms                                                     | 66.0 ms: 1.04x slower                                                       |
| pickle_list          | 2.59 us                                                     | 2.89 us: 1.12x slower                                                       |
| pickle_dict          | 16.9 us                                                     | 18.9 us: 1.12x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.08x faster                                                                |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221104-pythonperf1-amd64-python-044bcc1771fe7e2f8eba-3.12.0a1+-044bcc1 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 18.6 ms: 1.07x faster                                                       |
| python_startup_no_site | 15.5 ms                                                     | 15.8 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.03x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221104-pythonperf1-amd64-python-044bcc1771fe7e2f8eba-3.12.0a1+-044bcc1 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 8.80 ms                                                     | 7.05 ms: 1.25x faster                                                       |
| django_template | 28.2 ms                                                     | 22.9 ms: 1.23x faster                                                       |
| genshi_text     | 19.0 ms                                                     | 17.5 ms: 1.09x faster                                                       |
| genshi_xml      | 40.5 ms                                                     | 37.7 ms: 1.08x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.16x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221104-pythonperf1-amd64-python-044bcc1771fe7e2f8eba-3.12.0a1+-044bcc1 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 2.57 ms: 1.62x faster                                                       |
| mypy2                   | 352 ms                                                      | 225 ms: 1.57x faster                                                        |
| json_dumps              | 8.50 ms                                                     | 5.56 ms: 1.53x faster                                                       |
| go                      | 136 ms                                                      | 95.5 ms: 1.43x faster                                                       |
| richards                | 41.2 ms                                                     | 29.8 ms: 1.38x faster                                                       |
| scimark_sor             | 105 ms                                                      | 76.2 ms: 1.38x faster                                                       |
| scimark_lu              | 85.4 ms                                                     | 62.9 ms: 1.36x faster                                                       |
| logging_silent          | 96.4 ns                                                     | 71.3 ns: 1.35x faster                                                       |
| raytrace                | 271 ms                                                      | 204 ms: 1.33x faster                                                        |
| async_tree_io           | 1.07 sec                                                    | 803 ms: 1.33x faster                                                        |
| pyflate                 | 387 ms                                                      | 298 ms: 1.30x faster                                                        |
| scimark_monte_carlo     | 55.9 ms                                                     | 43.0 ms: 1.30x faster                                                       |
| sqlglot_parse           | 1.22 ms                                                     | 961 us: 1.27x faster                                                        |
| html5lib                | 46.5 ms                                                     | 36.7 ms: 1.26x faster                                                       |
| thrift                  | 615 us                                                      | 487 us: 1.26x faster                                                        |
| crypto_pyaes            | 62.3 ms                                                     | 49.7 ms: 1.25x faster                                                       |
| sqlglot_transpile       | 1.46 ms                                                     | 1.17 ms: 1.25x faster                                                       |
| pickle_pure_python      | 257 us                                                      | 205 us: 1.25x faster                                                        |
| async_tree_none         | 420 ms                                                      | 336 ms: 1.25x faster                                                        |
| mako                    | 8.80 ms                                                     | 7.05 ms: 1.25x faster                                                       |
| hexiom                  | 5.52 ms                                                     | 4.44 ms: 1.24x faster                                                       |
| async_tree_memoization  | 497 ms                                                      | 403 ms: 1.23x faster                                                        |
| django_template         | 28.2 ms                                                     | 22.9 ms: 1.23x faster                                                       |
| pycparser               | 868 ms                                                      | 709 ms: 1.22x faster                                                        |
| async_generators        | 224 ms                                                      | 183 ms: 1.22x faster                                                        |
| pylint                  | 347 ms                                                      | 286 ms: 1.21x faster                                                        |
| chaos                   | 58.9 ms                                                     | 48.8 ms: 1.21x faster                                                       |
| unpickle_pure_python    | 171 us                                                      | 143 us: 1.20x faster                                                        |
| regex_compile           | 103 ms                                                      | 86.9 ms: 1.19x faster                                                       |
| async_tree_cpu_io_mixed | 609 ms                                                      | 514 ms: 1.19x faster                                                        |
| tornado_http            | 109 ms                                                      | 92.6 ms: 1.18x faster                                                       |
| pprint_pformat          | 1.21 sec                                                    | 1.03 sec: 1.17x faster                                                      |
| docutils                | 1.89 sec                                                    | 1.62 sec: 1.17x faster                                                      |
| xml_etree_process       | 43.4 ms                                                     | 37.4 ms: 1.16x faster                                                       |
| pprint_safe_repr        | 589 ms                                                      | 509 ms: 1.16x faster                                                        |
| 2to3                    | 237 ms                                                      | 207 ms: 1.14x faster                                                        |
| create_gc_cycles        | 782 us                                                      | 683 us: 1.14x faster                                                        |
| chameleon               | 5.92 ms                                                     | 5.21 ms: 1.14x faster                                                       |
| xml_etree_parse         | 102 ms                                                      | 89.9 ms: 1.13x faster                                                       |
| dask                    | 305 ms                                                      | 269 ms: 1.13x faster                                                        |
| deepcopy_memo           | 28.5 us                                                     | 25.4 us: 1.12x faster                                                       |
| sqlglot_optimize        | 39.0 ms                                                     | 35.0 ms: 1.11x faster                                                       |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.39 ms: 1.11x faster                                                       |
| dulwich_log             | 47.6 ms                                                     | 42.9 ms: 1.11x faster                                                       |
| genshi_text             | 19.0 ms                                                     | 17.5 ms: 1.09x faster                                                       |
| sympy_integrate         | 14.8 ms                                                     | 13.7 ms: 1.08x faster                                                       |
| bench_thread_pool       | 946 us                                                      | 875 us: 1.08x faster                                                        |
| float                   | 60.2 ms                                                     | 55.8 ms: 1.08x faster                                                       |
| mdp                     | 1.71 sec                                                    | 1.59 sec: 1.08x faster                                                      |
| genshi_xml              | 40.5 ms                                                     | 37.7 ms: 1.08x faster                                                       |
| python_startup          | 20.0 ms                                                     | 18.6 ms: 1.07x faster                                                       |
| regex_dna               | 132 ms                                                      | 123 ms: 1.07x faster                                                        |
| spectral_norm           | 78.0 ms                                                     | 72.7 ms: 1.07x faster                                                       |
| json_loads              | 14.2 us                                                     | 13.3 us: 1.07x faster                                                       |
| unpickle_list           | 2.81 us                                                     | 2.63 us: 1.07x faster                                                       |
| sqlglot_normalize       | 202 ms                                                      | 190 ms: 1.07x faster                                                        |
| nbody                   | 69.3 ms                                                     | 65.2 ms: 1.06x faster                                                       |
| regex_v8                | 15.0 ms                                                     | 14.2 ms: 1.06x faster                                                       |
| deepcopy                | 255 us                                                      | 242 us: 1.05x faster                                                        |
| sympy_expand            | 315 ms                                                      | 299 ms: 1.05x faster                                                        |
| coroutines              | 15.9 ms                                                     | 15.2 ms: 1.05x faster                                                       |
| sympy_str               | 188 ms                                                      | 180 ms: 1.04x faster                                                        |
| xml_etree_generate      | 54.5 ms                                                     | 52.4 ms: 1.04x faster                                                       |
| pathlib                 | 77.4 ms                                                     | 74.4 ms: 1.04x faster                                                       |
| sympy_sum               | 104 ms                                                      | 100 ms: 1.04x faster                                                        |
| json                    | 3.05 ms                                                     | 2.94 ms: 1.04x faster                                                       |
| fannkuch                | 258 ms                                                      | 248 ms: 1.04x faster                                                        |
| nqueens                 | 67.0 ms                                                     | 64.6 ms: 1.04x faster                                                       |
| deepcopy_reduce         | 2.16 us                                                     | 2.09 us: 1.03x faster                                                       |
| sqlite_synth            | 1.84 us                                                     | 1.79 us: 1.03x faster                                                       |
| scimark_fft             | 193 ms                                                      | 188 ms: 1.03x faster                                                        |
| regex_effbot            | 1.66 ms                                                     | 1.62 ms: 1.03x faster                                                       |
| pickle                  | 6.80 us                                                     | 6.92 us: 1.02x slower                                                       |
| python_startup_no_site  | 15.5 ms                                                     | 15.8 ms: 1.02x slower                                                       |
| pidigits                | 145 ms                                                      | 149 ms: 1.03x slower                                                        |
| unpack_sequence         | 37.8 ns                                                     | 38.9 ns: 1.03x slower                                                       |
| xml_etree_iterparse     | 63.5 ms                                                     | 66.0 ms: 1.04x slower                                                       |
| telco                   | 3.78 ms                                                     | 3.94 ms: 1.04x slower                                                       |
| meteor_contest          | 72.5 ms                                                     | 75.9 ms: 1.05x slower                                                       |
| bench_mp_pool           | 60.7 ms                                                     | 63.7 ms: 1.05x slower                                                       |
| logging_simple          | 6.20 us                                                     | 6.63 us: 1.07x slower                                                       |
| comprehensions          | 16.0 us                                                     | 17.2 us: 1.08x slower                                                       |
| logging_format          | 6.66 us                                                     | 7.21 us: 1.08x slower                                                       |
| gc_traversal            | 1.34 ms                                                     | 1.50 ms: 1.12x slower                                                       |
| pickle_list             | 2.59 us                                                     | 2.89 us: 1.12x slower                                                       |
| pickle_dict             | 16.9 us                                                     | 18.9 us: 1.12x slower                                                       |
| generators              | 31.6 ms                                                     | 36.1 ms: 1.14x slower                                                       |
| coverage                | 40.0 ms                                                     | 54.4 ms: 1.36x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.12x faster                                                                |

Benchmark hidden because not significant (2): unpickle, asyncio_tcp
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x
