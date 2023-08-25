
# Results vs. 3.10.4

- fork: python
- ref: 4ae1a0ecaffe4320fe97
- machine: linux-x86_64
- commit hash: 4ae1a0e
- commit date: 2022-10-25
- overall geometric mean: 1.25x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221025-pythonperf2-x86_64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 278 ms: 1.26x faster                                                        |
| chameleon      | 9.72 ms                                                      | 7.62 ms: 1.28x faster                                                       |
| docutils       | 3.40 sec                                                     | 2.79 sec: 1.22x faster                                                      |
| html5lib       | 94.6 ms                                                      | 66.2 ms: 1.43x faster                                                       |
| tornado_http   | 152 ms                                                       | 114 ms: 1.33x faster                                                        |
| Geometric mean | (ref)                                                        | 1.30x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221025-pythonperf2-x86_64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 110 ms                                                       | 73.2 ms: 1.51x faster                                                       |
| nbody          | 137 ms                                                       | 98.1 ms: 1.40x faster                                                       |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                        | 1.31x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221025-pythonperf2-x86_64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 146 ms: 1.33x faster                                                        |
| regex_v8       | 26.6 ms                                                      | 22.9 ms: 1.16x faster                                                       |
| regex_dna      | 259 ms                                                       | 232 ms: 1.12x faster                                                        |
| regex_effbot   | 2.99 ms                                                      | 3.34 ms: 1.12x slower                                                       |
| Geometric mean | (ref)                                                        | 1.12x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221025-pythonperf2-x86_64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 208 us: 1.54x faster                                                        |
| pickle_pure_python   | 457 us                                                       | 313 us: 1.46x faster                                                        |
| xml_etree_process    | 76.0 ms                                                      | 54.1 ms: 1.40x faster                                                       |
| json_dumps           | 14.2 ms                                                      | 10.4 ms: 1.37x faster                                                       |
| json_loads           | 30.0 us                                                      | 24.3 us: 1.24x faster                                                       |
| xml_etree_generate   | 94.6 ms                                                      | 77.6 ms: 1.22x faster                                                       |
| xml_etree_parse      | 162 ms                                                       | 138 ms: 1.17x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 103 ms: 1.08x faster                                                        |
| pickle_list          | 4.11 us                                                      | 3.84 us: 1.07x faster                                                       |
| unpickle             | 14.2 us                                                      | 13.3 us: 1.07x faster                                                       |
| pickle               | 9.94 us                                                      | 10.1 us: 1.02x slower                                                       |
| pickle_dict          | 30.0 us                                                      | 31.9 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.18x faster                                                                |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221025-pythonperf2-x86_64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 10.6 ms: 1.08x faster                                                       |
| python_startup_no_site | 7.32 ms                                                      | 7.62 ms: 1.04x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221025-pythonperf2-x86_64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.4 ms: 1.41x faster                                                       |
| genshi_text     | 31.5 ms                                                      | 24.7 ms: 1.27x faster                                                       |
| django_template | 51.5 ms                                                      | 40.6 ms: 1.27x faster                                                       |
| genshi_xml      | 64.7 ms                                                      | 55.5 ms: 1.17x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.28x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221025-pythonperf2-x86_64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 7.47 ms                                                      | 3.65 ms: 2.04x faster                                                       |
| logging_silent          | 166 ns                                                       | 95.5 ns: 1.73x faster                                                       |
| go                      | 259 ms                                                       | 155 ms: 1.67x faster                                                        |
| raytrace                | 488 ms                                                       | 298 ms: 1.64x faster                                                        |
| scimark_sor             | 177 ms                                                       | 108 ms: 1.63x faster                                                        |
| pyflate                 | 697 ms                                                       | 431 ms: 1.62x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                       | 67.8 ms: 1.61x faster                                                       |
| bench_mp_pool           | 7.18 ms                                                      | 4.56 ms: 1.58x faster                                                       |
| richards                | 74.1 ms                                                      | 47.6 ms: 1.56x faster                                                       |
| unpickle_pure_python    | 321 us                                                       | 208 us: 1.54x faster                                                        |
| float                   | 110 ms                                                       | 73.2 ms: 1.51x faster                                                       |
| sqlglot_parse           | 2.26 ms                                                      | 1.51 ms: 1.49x faster                                                       |
| scimark_lu              | 164 ms                                                       | 111 ms: 1.48x faster                                                        |
| pickle_pure_python      | 457 us                                                       | 313 us: 1.46x faster                                                        |
| chaos                   | 107 ms                                                       | 73.4 ms: 1.46x faster                                                       |
| scimark_sparse_mat_mult | 5.19 ms                                                      | 3.58 ms: 1.45x faster                                                       |
| hexiom                  | 9.52 ms                                                      | 6.61 ms: 1.44x faster                                                       |
| html5lib                | 94.6 ms                                                      | 66.2 ms: 1.43x faster                                                       |
| sqlglot_transpile       | 2.71 ms                                                      | 1.90 ms: 1.43x faster                                                       |
| crypto_pyaes            | 118 ms                                                       | 83.2 ms: 1.42x faster                                                       |
| spectral_norm           | 136 ms                                                       | 96.1 ms: 1.42x faster                                                       |
| mako                    | 14.7 ms                                                      | 10.4 ms: 1.41x faster                                                       |
| xml_etree_process       | 76.0 ms                                                      | 54.1 ms: 1.40x faster                                                       |
| nbody                   | 137 ms                                                       | 98.1 ms: 1.40x faster                                                       |
| async_tree_io           | 1.61 sec                                                     | 1.16 sec: 1.39x faster                                                      |
| pprint_safe_repr        | 1.05 sec                                                     | 761 ms: 1.38x faster                                                        |
| pprint_pformat          | 2.15 sec                                                     | 1.57 sec: 1.37x faster                                                      |
| json_dumps              | 14.2 ms                                                      | 10.4 ms: 1.37x faster                                                       |
| async_tree_none         | 700 ms                                                       | 516 ms: 1.36x faster                                                        |
| aiohttp                 | 1.21 ms                                                      | 894 us: 1.35x faster                                                        |
| deepcopy_memo           | 48.9 us                                                      | 36.4 us: 1.34x faster                                                       |
| async_tree_memoization  | 824 ms                                                       | 618 ms: 1.33x faster                                                        |
| tornado_http            | 152 ms                                                       | 114 ms: 1.33x faster                                                        |
| regex_compile           | 194 ms                                                       | 146 ms: 1.33x faster                                                        |
| pycparser               | 1.66 sec                                                     | 1.25 sec: 1.33x faster                                                      |
| unpack_sequence         | 59.5 ns                                                      | 45.0 ns: 1.32x faster                                                       |
| gunicorn                | 1.17 ms                                                      | 888 us: 1.32x faster                                                        |
| async_generators        | 422 ms                                                       | 321 ms: 1.32x faster                                                        |
| chameleon               | 9.72 ms                                                      | 7.62 ms: 1.28x faster                                                       |
| genshi_text             | 31.5 ms                                                      | 24.7 ms: 1.27x faster                                                       |
| django_template         | 51.5 ms                                                      | 40.6 ms: 1.27x faster                                                       |
| logging_simple          | 8.90 us                                                      | 7.06 us: 1.26x faster                                                       |
| 2to3                    | 350 ms                                                       | 278 ms: 1.26x faster                                                        |
| async_tree_cpu_io_mixed | 952 ms                                                       | 756 ms: 1.26x faster                                                        |
| mypy2                   | 466 ms                                                       | 372 ms: 1.25x faster                                                        |
| scimark_fft             | 359 ms                                                       | 288 ms: 1.25x faster                                                        |
| json_loads              | 30.0 us                                                      | 24.3 us: 1.24x faster                                                       |
| logging_format          | 9.57 us                                                      | 7.77 us: 1.23x faster                                                       |
| fannkuch                | 496 ms                                                       | 405 ms: 1.22x faster                                                        |
| thrift                  | 1.16 ms                                                      | 953 us: 1.22x faster                                                        |
| docutils                | 3.40 sec                                                     | 2.79 sec: 1.22x faster                                                      |
| xml_etree_generate      | 94.6 ms                                                      | 77.6 ms: 1.22x faster                                                       |
| dulwich_log             | 80.1 ms                                                      | 65.9 ms: 1.21x faster                                                       |
| sqlglot_optimize        | 70.3 ms                                                      | 58.2 ms: 1.21x faster                                                       |
| deepcopy_reduce         | 4.03 us                                                      | 3.35 us: 1.20x faster                                                       |
| sqlglot_normalize       | 144 ms                                                       | 120 ms: 1.20x faster                                                        |
| json                    | 5.96 ms                                                      | 5.05 ms: 1.18x faster                                                       |
| bench_thread_pool       | 1.14 ms                                                      | 966 us: 1.18x faster                                                        |
| genshi_xml              | 64.7 ms                                                      | 55.5 ms: 1.17x faster                                                       |
| xml_etree_parse         | 162 ms                                                       | 138 ms: 1.17x faster                                                        |
| sqlite_synth            | 2.97 us                                                      | 2.54 us: 1.17x faster                                                       |
| regex_v8                | 26.6 ms                                                      | 22.9 ms: 1.16x faster                                                       |
| nqueens                 | 112 ms                                                       | 97.1 ms: 1.16x faster                                                       |
| deepcopy                | 454 us                                                       | 394 us: 1.15x faster                                                        |
| pathlib                 | 21.7 ms                                                      | 19.0 ms: 1.14x faster                                                       |
| sympy_expand            | 599 ms                                                       | 527 ms: 1.14x faster                                                        |
| pylint                  | 562 ms                                                       | 496 ms: 1.13x faster                                                        |
| create_gc_cycles        | 1.82 ms                                                      | 1.61 ms: 1.13x faster                                                       |
| dask                    | 463 ms                                                       | 409 ms: 1.13x faster                                                        |
| mdp                     | 3.03 sec                                                     | 2.71 sec: 1.12x faster                                                      |
| regex_dna               | 259 ms                                                       | 232 ms: 1.12x faster                                                        |
| comprehensions          | 26.9 us                                                      | 24.2 us: 1.11x faster                                                       |
| coroutines              | 30.4 ms                                                      | 27.4 ms: 1.11x faster                                                       |
| sympy_integrate         | 28.1 ms                                                      | 25.4 ms: 1.11x faster                                                       |
| sympy_str               | 358 ms                                                       | 326 ms: 1.10x faster                                                        |
| meteor_contest          | 137 ms                                                       | 126 ms: 1.09x faster                                                        |
| python_startup          | 11.5 ms                                                      | 10.6 ms: 1.08x faster                                                       |
| telco                   | 7.14 ms                                                      | 6.64 ms: 1.08x faster                                                       |
| pidigits                | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| xml_etree_iterparse     | 110 ms                                                       | 103 ms: 1.08x faster                                                        |
| pickle_list             | 4.11 us                                                      | 3.84 us: 1.07x faster                                                       |
| unpickle                | 14.2 us                                                      | 13.3 us: 1.07x faster                                                       |
| sympy_sum               | 193 ms                                                       | 181 ms: 1.06x faster                                                        |
| generators              | 58.0 ms                                                      | 54.6 ms: 1.06x faster                                                       |
| asyncio_tcp             | 782 ms                                                       | 747 ms: 1.05x faster                                                        |
| pickle                  | 9.94 us                                                      | 10.1 us: 1.02x slower                                                       |
| gc_traversal            | 3.45 ms                                                      | 3.54 ms: 1.02x slower                                                       |
| python_startup_no_site  | 7.32 ms                                                      | 7.62 ms: 1.04x slower                                                       |
| pickle_dict             | 30.0 us                                                      | 31.9 us: 1.06x slower                                                       |
| regex_effbot            | 2.99 ms                                                      | 3.34 ms: 1.12x slower                                                       |
| coverage                | 64.0 ms                                                      | 81.5 ms: 1.27x slower                                                       |
| Geometric mean          | (ref)                                                        | 1.25x faster                                                                |

Benchmark hidden because not significant (1): unpickle_list
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.20x
