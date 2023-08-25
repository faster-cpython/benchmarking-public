
# Results vs. 3.10.4

- fork: python
- ref: c4170c36b0b54c10456f
- machine: windows-amd64
- commit hash: c4170c3
- commit date: 2023-01-29
- overall geometric mean: 1.23x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230129-pythonperf1-amd64-python-c4170c36b0b54c10456f-3.12.0a4+-c4170c3 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 199 ms: 1.19x faster                                                        |
| chameleon      | 5.92 ms                                                     | 4.43 ms: 1.34x faster                                                       |
| docutils       | 1.89 sec                                                    | 1.53 sec: 1.24x faster                                                      |
| html5lib       | 46.5 ms                                                     | 35.1 ms: 1.32x faster                                                       |
| tornado_http   | 109 ms                                                      | 91.6 ms: 1.19x faster                                                       |
| Geometric mean | (ref)                                                       | 1.25x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230129-pythonperf1-amd64-python-c4170c36b0b54c10456f-3.12.0a4+-c4170c3 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 48.2 ms: 1.25x faster                                                       |
| nbody          | 69.3 ms                                                     | 61.8 ms: 1.12x faster                                                       |
| pidigits       | 145 ms                                                      | 151 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230129-pythonperf1-amd64-python-c4170c36b0b54c10456f-3.12.0a4+-c4170c3 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 79.7 ms: 1.30x faster                                                       |
| regex_dna      | 132 ms                                                      | 121 ms: 1.09x faster                                                        |
| regex_v8       | 15.0 ms                                                     | 13.8 ms: 1.09x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230129-pythonperf1-amd64-python-c4170c36b0b54c10456f-3.12.0a4+-c4170c3 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.15 ms: 1.65x faster                                                       |
| pickle_pure_python   | 257 us                                                      | 176 us: 1.46x faster                                                        |
| unpickle_pure_python | 171 us                                                      | 120 us: 1.42x faster                                                        |
| xml_etree_process    | 43.4 ms                                                     | 34.3 ms: 1.27x faster                                                       |
| xml_etree_parse      | 102 ms                                                      | 87.3 ms: 1.17x faster                                                       |
| json_loads           | 14.2 us                                                     | 12.8 us: 1.10x faster                                                       |
| xml_etree_generate   | 54.5 ms                                                     | 50.1 ms: 1.09x faster                                                       |
| pickle               | 6.80 us                                                     | 6.73 us: 1.01x faster                                                       |
| pickle_list          | 2.59 us                                                     | 2.78 us: 1.07x slower                                                       |
| pickle_dict          | 16.9 us                                                     | 18.5 us: 1.09x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.14x faster                                                                |

Benchmark hidden because not significant (3): unpickle, unpickle_list, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230129-pythonperf1-amd64-python-c4170c36b0b54c10456f-3.12.0a4+-c4170c3 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 19.0 ms: 1.05x faster                                                       |
| python_startup_no_site | 15.5 ms                                                     | 16.3 ms: 1.05x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230129-pythonperf1-amd64-python-c4170c36b0b54c10456f-3.12.0a4+-c4170c3 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 8.80 ms                                                     | 6.16 ms: 1.43x faster                                                       |
| genshi_text     | 19.0 ms                                                     | 14.0 ms: 1.36x faster                                                       |
| django_template | 28.2 ms                                                     | 20.9 ms: 1.35x faster                                                       |
| genshi_xml      | 40.5 ms                                                     | 30.8 ms: 1.32x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.36x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230129-pythonperf1-amd64-python-c4170c36b0b54c10456f-3.12.0a4+-c4170c3 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 1.99 ms: 2.10x faster                                                       |
| richards                | 41.2 ms                                                     | 23.1 ms: 1.78x faster                                                       |
| logging_silent          | 96.4 ns                                                     | 55.7 ns: 1.73x faster                                                       |
| scimark_sor             | 105 ms                                                      | 61.9 ms: 1.69x faster                                                       |
| go                      | 136 ms                                                      | 80.6 ms: 1.69x faster                                                       |
| json_dumps              | 8.50 ms                                                     | 5.15 ms: 1.65x faster                                                       |
| mypy2                   | 352 ms                                                      | 216 ms: 1.63x faster                                                        |
| raytrace                | 271 ms                                                      | 171 ms: 1.59x faster                                                        |
| scimark_lu              | 85.4 ms                                                     | 56.7 ms: 1.51x faster                                                       |
| scimark_monte_carlo     | 55.9 ms                                                     | 37.0 ms: 1.51x faster                                                       |
| pyflate                 | 387 ms                                                      | 260 ms: 1.49x faster                                                        |
| hexiom                  | 5.52 ms                                                     | 3.76 ms: 1.47x faster                                                       |
| asyncio_tcp             | 712 ms                                                      | 489 ms: 1.46x faster                                                        |
| pickle_pure_python      | 257 us                                                      | 176 us: 1.46x faster                                                        |
| unpack_sequence         | 37.8 ns                                                     | 26.2 ns: 1.44x faster                                                       |
| mako                    | 8.80 ms                                                     | 6.16 ms: 1.43x faster                                                       |
| unpickle_pure_python    | 171 us                                                      | 120 us: 1.42x faster                                                        |
| chaos                   | 58.9 ms                                                     | 41.6 ms: 1.42x faster                                                       |
| sqlglot_parse           | 1.22 ms                                                     | 874 us: 1.39x faster                                                        |
| sqlglot_transpile       | 1.46 ms                                                     | 1.05 ms: 1.39x faster                                                       |
| async_tree_io           | 1.07 sec                                                    | 768 ms: 1.39x faster                                                        |
| crypto_pyaes            | 62.3 ms                                                     | 45.0 ms: 1.39x faster                                                       |
| deepcopy_memo           | 28.5 us                                                     | 20.8 us: 1.37x faster                                                       |
| genshi_text             | 19.0 ms                                                     | 14.0 ms: 1.36x faster                                                       |
| pycparser               | 868 ms                                                      | 641 ms: 1.35x faster                                                        |
| django_template         | 28.2 ms                                                     | 20.9 ms: 1.35x faster                                                       |
| thrift                  | 615 us                                                      | 460 us: 1.34x faster                                                        |
| chameleon               | 5.92 ms                                                     | 4.43 ms: 1.34x faster                                                       |
| comprehensions          | 16.0 us                                                     | 12.0 us: 1.33x faster                                                       |
| async_tree_none         | 420 ms                                                      | 315 ms: 1.33x faster                                                        |
| html5lib                | 46.5 ms                                                     | 35.1 ms: 1.32x faster                                                       |
| genshi_xml              | 40.5 ms                                                     | 30.8 ms: 1.32x faster                                                       |
| async_tree_memoization  | 497 ms                                                      | 378 ms: 1.32x faster                                                        |
| regex_compile           | 103 ms                                                      | 79.7 ms: 1.30x faster                                                       |
| pprint_pformat          | 1.21 sec                                                    | 935 ms: 1.29x faster                                                        |
| spectral_norm           | 78.0 ms                                                     | 60.8 ms: 1.28x faster                                                       |
| async_generators        | 224 ms                                                      | 176 ms: 1.27x faster                                                        |
| pprint_safe_repr        | 589 ms                                                      | 465 ms: 1.27x faster                                                        |
| xml_etree_process       | 43.4 ms                                                     | 34.3 ms: 1.27x faster                                                       |
| float                   | 60.2 ms                                                     | 48.2 ms: 1.25x faster                                                       |
| docutils                | 1.89 sec                                                    | 1.53 sec: 1.24x faster                                                      |
| deepcopy                | 255 us                                                      | 208 us: 1.23x faster                                                        |
| async_tree_cpu_io_mixed | 609 ms                                                      | 498 ms: 1.22x faster                                                        |
| sqlglot_optimize        | 39.0 ms                                                     | 32.0 ms: 1.22x faster                                                       |
| sqlglot_normalize       | 202 ms                                                      | 170 ms: 1.19x faster                                                        |
| 2to3                    | 237 ms                                                      | 199 ms: 1.19x faster                                                        |
| tornado_http            | 109 ms                                                      | 91.6 ms: 1.19x faster                                                       |
| nqueens                 | 67.0 ms                                                     | 56.4 ms: 1.19x faster                                                       |
| sympy_str               | 188 ms                                                      | 159 ms: 1.19x faster                                                        |
| dulwich_log             | 47.6 ms                                                     | 40.3 ms: 1.18x faster                                                       |
| sympy_integrate         | 14.8 ms                                                     | 12.6 ms: 1.18x faster                                                       |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.27 ms: 1.17x faster                                                       |
| xml_etree_parse         | 102 ms                                                      | 87.3 ms: 1.17x faster                                                       |
| sympy_expand            | 315 ms                                                      | 271 ms: 1.16x faster                                                        |
| dask                    | 305 ms                                                      | 263 ms: 1.16x faster                                                        |
| scimark_fft             | 193 ms                                                      | 167 ms: 1.16x faster                                                        |
| deepcopy_reduce         | 2.16 us                                                     | 1.87 us: 1.16x faster                                                       |
| sympy_sum               | 104 ms                                                      | 90.8 ms: 1.15x faster                                                       |
| bench_thread_pool       | 946 us                                                      | 833 us: 1.14x faster                                                        |
| mdp                     | 1.71 sec                                                    | 1.52 sec: 1.13x faster                                                      |
| json                    | 3.05 ms                                                     | 2.70 ms: 1.13x faster                                                       |
| create_gc_cycles        | 782 us                                                      | 695 us: 1.12x faster                                                        |
| nbody                   | 69.3 ms                                                     | 61.8 ms: 1.12x faster                                                       |
| json_loads              | 14.2 us                                                     | 12.8 us: 1.10x faster                                                       |
| regex_dna               | 132 ms                                                      | 121 ms: 1.09x faster                                                        |
| regex_v8                | 15.0 ms                                                     | 13.8 ms: 1.09x faster                                                       |
| xml_etree_generate      | 54.5 ms                                                     | 50.1 ms: 1.09x faster                                                       |
| sqlite_synth            | 1.84 us                                                     | 1.70 us: 1.08x faster                                                       |
| coroutines              | 15.9 ms                                                     | 14.8 ms: 1.08x faster                                                       |
| fannkuch                | 258 ms                                                      | 242 ms: 1.07x faster                                                        |
| regex_effbot            | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                       |
| python_startup          | 20.0 ms                                                     | 19.0 ms: 1.05x faster                                                       |
| telco                   | 3.78 ms                                                     | 3.62 ms: 1.05x faster                                                       |
| meteor_contest          | 72.5 ms                                                     | 69.6 ms: 1.04x faster                                                       |
| pathlib                 | 77.4 ms                                                     | 74.2 ms: 1.04x faster                                                       |
| logging_format          | 6.66 us                                                     | 6.54 us: 1.02x faster                                                       |
| pickle                  | 6.80 us                                                     | 6.73 us: 1.01x faster                                                       |
| pidigits                | 145 ms                                                      | 151 ms: 1.04x slower                                                        |
| bench_mp_pool           | 60.7 ms                                                     | 63.3 ms: 1.04x slower                                                       |
| python_startup_no_site  | 15.5 ms                                                     | 16.3 ms: 1.05x slower                                                       |
| pickle_list             | 2.59 us                                                     | 2.78 us: 1.07x slower                                                       |
| generators              | 31.6 ms                                                     | 34.4 ms: 1.09x slower                                                       |
| gc_traversal            | 1.34 ms                                                     | 1.47 ms: 1.09x slower                                                       |
| pickle_dict             | 16.9 us                                                     | 18.5 us: 1.09x slower                                                       |
| coverage                | 40.0 ms                                                     | 54.1 ms: 1.35x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.23x faster                                                                |

Benchmark hidden because not significant (4): unpickle, unpickle_list, logging_simple, xml_etree_iterparse
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.17x
