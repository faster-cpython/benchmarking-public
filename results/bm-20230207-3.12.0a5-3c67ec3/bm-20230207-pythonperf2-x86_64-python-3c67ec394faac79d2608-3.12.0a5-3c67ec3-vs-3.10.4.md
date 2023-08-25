
# Results vs. 3.10.4

- fork: python
- ref: 3c67ec394faac79d2608
- machine: linux-x86_64
- commit hash: 3c67ec3
- commit date: 2023-02-07
- overall geometric mean: 1.26x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-pythonperf2-x86_64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 282 ms: 1.24x faster                                                        |
| chameleon      | 9.72 ms                                                      | 7.46 ms: 1.30x faster                                                       |
| docutils       | 3.40 sec                                                     | 2.78 sec: 1.22x faster                                                      |
| html5lib       | 94.6 ms                                                      | 65.3 ms: 1.45x faster                                                       |
| tornado_http   | 152 ms                                                       | 117 ms: 1.30x faster                                                        |
| Geometric mean | (ref)                                                        | 1.30x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-pythonperf2-x86_64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 110 ms                                                       | 71.9 ms: 1.53x faster                                                       |
| nbody          | 137 ms                                                       | 101 ms: 1.36x faster                                                        |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                        | 1.31x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-pythonperf2-x86_64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 145 ms: 1.34x faster                                                        |
| regex_v8       | 26.6 ms                                                      | 22.7 ms: 1.17x faster                                                       |
| regex_dna      | 259 ms                                                       | 240 ms: 1.08x faster                                                        |
| regex_effbot   | 2.99 ms                                                      | 3.50 ms: 1.17x slower                                                       |
| Geometric mean | (ref)                                                        | 1.10x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-pythonperf2-x86_64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 204 us: 1.57x faster                                                        |
| pickle_pure_python   | 457 us                                                       | 312 us: 1.47x faster                                                        |
| json_dumps           | 14.2 ms                                                      | 10.0 ms: 1.42x faster                                                       |
| xml_etree_process    | 76.0 ms                                                      | 55.6 ms: 1.37x faster                                                       |
| json_loads           | 30.0 us                                                      | 23.8 us: 1.26x faster                                                       |
| xml_etree_generate   | 94.6 ms                                                      | 80.6 ms: 1.17x faster                                                       |
| xml_etree_parse      | 162 ms                                                       | 142 ms: 1.14x faster                                                        |
| unpickle             | 14.2 us                                                      | 12.8 us: 1.11x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 103 ms: 1.08x faster                                                        |
| pickle_list          | 4.11 us                                                      | 3.84 us: 1.07x faster                                                       |
| pickle               | 9.94 us                                                      | 9.88 us: 1.01x faster                                                       |
| pickle_dict          | 30.0 us                                                      | 31.6 us: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.18x faster                                                                |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-pythonperf2-x86_64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.2 ms: 1.03x faster                                                       |
| python_startup_no_site | 7.32 ms                                                      | 8.25 ms: 1.13x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.05x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-pythonperf2-x86_64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.3 ms: 1.43x faster                                                       |
| genshi_text     | 31.5 ms                                                      | 24.6 ms: 1.28x faster                                                       |
| django_template | 51.5 ms                                                      | 40.5 ms: 1.27x faster                                                       |
| genshi_xml      | 64.7 ms                                                      | 53.4 ms: 1.21x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.30x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-pythonperf2-x86_64-python-3c67ec394faac79d2608-3.12.0a5-3c67ec3 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 7.47 ms                                                      | 3.60 ms: 2.08x faster                                                       |
| asyncio_tcp             | 782 ms                                                       | 388 ms: 2.01x faster                                                        |
| logging_silent          | 166 ns                                                       | 96.5 ns: 1.72x faster                                                       |
| go                      | 259 ms                                                       | 152 ms: 1.70x faster                                                        |
| scimark_sor             | 177 ms                                                       | 105 ms: 1.69x faster                                                        |
| pyflate                 | 697 ms                                                       | 428 ms: 1.63x faster                                                        |
| raytrace                | 488 ms                                                       | 301 ms: 1.62x faster                                                        |
| richards                | 74.1 ms                                                      | 46.1 ms: 1.61x faster                                                       |
| scimark_lu              | 164 ms                                                       | 104 ms: 1.57x faster                                                        |
| unpickle_pure_python    | 321 us                                                       | 204 us: 1.57x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                       | 70.2 ms: 1.56x faster                                                       |
| chaos                   | 107 ms                                                       | 69.6 ms: 1.54x faster                                                       |
| float                   | 110 ms                                                       | 71.9 ms: 1.53x faster                                                       |
| bench_mp_pool           | 7.18 ms                                                      | 4.71 ms: 1.53x faster                                                       |
| hexiom                  | 9.52 ms                                                      | 6.49 ms: 1.47x faster                                                       |
| pickle_pure_python      | 457 us                                                       | 312 us: 1.47x faster                                                        |
| html5lib                | 94.6 ms                                                      | 65.3 ms: 1.45x faster                                                       |
| sqlglot_parse           | 2.26 ms                                                      | 1.56 ms: 1.45x faster                                                       |
| crypto_pyaes            | 118 ms                                                       | 81.8 ms: 1.44x faster                                                       |
| scimark_sparse_mat_mult | 5.19 ms                                                      | 3.61 ms: 1.44x faster                                                       |
| mako                    | 14.7 ms                                                      | 10.3 ms: 1.43x faster                                                       |
| spectral_norm           | 136 ms                                                       | 95.4 ms: 1.43x faster                                                       |
| json_dumps              | 14.2 ms                                                      | 10.0 ms: 1.42x faster                                                       |
| pprint_safe_repr        | 1.05 sec                                                     | 744 ms: 1.41x faster                                                        |
| pprint_pformat          | 2.15 sec                                                     | 1.53 sec: 1.41x faster                                                      |
| sqlglot_transpile       | 2.71 ms                                                      | 1.93 ms: 1.41x faster                                                       |
| async_tree_none         | 700 ms                                                       | 503 ms: 1.39x faster                                                        |
| async_tree_io           | 1.61 sec                                                     | 1.17 sec: 1.38x faster                                                      |
| unpack_sequence         | 59.5 ns                                                      | 43.3 ns: 1.38x faster                                                       |
| async_tree_memoization  | 824 ms                                                       | 601 ms: 1.37x faster                                                        |
| xml_etree_process       | 76.0 ms                                                      | 55.6 ms: 1.37x faster                                                       |
| deepcopy_memo           | 48.9 us                                                      | 35.8 us: 1.36x faster                                                       |
| nbody                   | 137 ms                                                       | 101 ms: 1.36x faster                                                        |
| regex_compile           | 194 ms                                                       | 145 ms: 1.34x faster                                                        |
| logging_simple          | 8.90 us                                                      | 6.67 us: 1.33x faster                                                       |
| pycparser               | 1.66 sec                                                     | 1.28 sec: 1.30x faster                                                      |
| chameleon               | 9.72 ms                                                      | 7.46 ms: 1.30x faster                                                       |
| tornado_http            | 152 ms                                                       | 117 ms: 1.30x faster                                                        |
| async_generators        | 422 ms                                                       | 325 ms: 1.30x faster                                                        |
| async_tree_cpu_io_mixed | 952 ms                                                       | 737 ms: 1.29x faster                                                        |
| scimark_fft             | 359 ms                                                       | 278 ms: 1.29x faster                                                        |
| logging_format          | 9.57 us                                                      | 7.43 us: 1.29x faster                                                       |
| genshi_text             | 31.5 ms                                                      | 24.6 ms: 1.28x faster                                                       |
| django_template         | 51.5 ms                                                      | 40.5 ms: 1.27x faster                                                       |
| comprehensions          | 26.9 us                                                      | 21.3 us: 1.26x faster                                                       |
| json_loads              | 30.0 us                                                      | 23.8 us: 1.26x faster                                                       |
| thrift                  | 1.16 ms                                                      | 935 us: 1.25x faster                                                        |
| 2to3                    | 350 ms                                                       | 282 ms: 1.24x faster                                                        |
| mypy2                   | 466 ms                                                       | 379 ms: 1.23x faster                                                        |
| docutils                | 3.40 sec                                                     | 2.78 sec: 1.22x faster                                                      |
| deepcopy_reduce         | 4.03 us                                                      | 3.30 us: 1.22x faster                                                       |
| sqlglot_optimize        | 70.3 ms                                                      | 57.7 ms: 1.22x faster                                                       |
| fannkuch                | 496 ms                                                       | 409 ms: 1.21x faster                                                        |
| genshi_xml              | 64.7 ms                                                      | 53.4 ms: 1.21x faster                                                       |
| json                    | 5.96 ms                                                      | 4.94 ms: 1.21x faster                                                       |
| dulwich_log             | 80.1 ms                                                      | 66.6 ms: 1.20x faster                                                       |
| sqlglot_normalize       | 144 ms                                                       | 120 ms: 1.20x faster                                                        |
| nqueens                 | 112 ms                                                       | 94.2 ms: 1.19x faster                                                       |
| deepcopy                | 454 us                                                       | 383 us: 1.18x faster                                                        |
| xml_etree_generate      | 94.6 ms                                                      | 80.6 ms: 1.17x faster                                                       |
| regex_v8                | 26.6 ms                                                      | 22.7 ms: 1.17x faster                                                       |
| bench_thread_pool       | 1.14 ms                                                      | 971 us: 1.17x faster                                                        |
| sympy_integrate         | 28.1 ms                                                      | 24.3 ms: 1.15x faster                                                       |
| sqlite_synth            | 2.97 us                                                      | 2.58 us: 1.15x faster                                                       |
| sympy_str               | 358 ms                                                       | 313 ms: 1.14x faster                                                        |
| sympy_expand            | 599 ms                                                       | 526 ms: 1.14x faster                                                        |
| mdp                     | 3.03 sec                                                     | 2.66 sec: 1.14x faster                                                      |
| xml_etree_parse         | 162 ms                                                       | 142 ms: 1.14x faster                                                        |
| pathlib                 | 21.7 ms                                                      | 19.1 ms: 1.13x faster                                                       |
| sympy_sum               | 193 ms                                                       | 172 ms: 1.12x faster                                                        |
| create_gc_cycles        | 1.82 ms                                                      | 1.64 ms: 1.11x faster                                                       |
| unpickle                | 14.2 us                                                      | 12.8 us: 1.11x faster                                                       |
| telco                   | 7.14 ms                                                      | 6.59 ms: 1.08x faster                                                       |
| regex_dna               | 259 ms                                                       | 240 ms: 1.08x faster                                                        |
| pidigits                | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| xml_etree_iterparse     | 110 ms                                                       | 103 ms: 1.08x faster                                                        |
| pickle_list             | 4.11 us                                                      | 3.84 us: 1.07x faster                                                       |
| meteor_contest          | 137 ms                                                       | 128 ms: 1.07x faster                                                        |
| coroutines              | 30.4 ms                                                      | 29.1 ms: 1.05x faster                                                       |
| python_startup          | 11.5 ms                                                      | 11.2 ms: 1.03x faster                                                       |
| pickle                  | 9.94 us                                                      | 9.88 us: 1.01x faster                                                       |
| gc_traversal            | 3.45 ms                                                      | 3.55 ms: 1.03x slower                                                       |
| generators              | 58.0 ms                                                      | 60.4 ms: 1.04x slower                                                       |
| pickle_dict             | 30.0 us                                                      | 31.6 us: 1.05x slower                                                       |
| python_startup_no_site  | 7.32 ms                                                      | 8.25 ms: 1.13x slower                                                       |
| regex_effbot            | 2.99 ms                                                      | 3.50 ms: 1.17x slower                                                       |
| dask                    | 463 ms                                                       | 562 ms: 1.21x slower                                                        |
| coverage                | 64.0 ms                                                      | 86.0 ms: 1.34x slower                                                       |
| Geometric mean          | (ref)                                                        | 1.26x faster                                                                |

Benchmark hidden because not significant (1): unpickle_list
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.21x
