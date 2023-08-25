
# Results vs. 3.10.4

- fork: python
- ref: v3.11.0
- machine: linux-x86_64
- commit hash: deaf509
- commit date: 2022-10-24
- overall geometric mean: 1.21x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 288 ms: 1.22x faster                                         |
| chameleon      | 9.72 ms                                                      | 7.67 ms: 1.27x faster                                        |
| docutils       | 3.40 sec                                                     | 2.86 sec: 1.19x faster                                       |
| html5lib       | 94.6 ms                                                      | 72.9 ms: 1.30x faster                                        |
| tornado_http   | 152 ms                                                       | 122 ms: 1.25x faster                                         |
| Geometric mean | (ref)                                                        | 1.24x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 90.7 ms: 1.51x faster                                        |
| float          | 110 ms                                                       | 74.2 ms: 1.49x faster                                        |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                         |
| Geometric mean | (ref)                                                        | 1.34x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 158 ms: 1.23x faster                                         |
| regex_dna      | 259 ms                                                       | 227 ms: 1.14x faster                                         |
| regex_v8       | 26.6 ms                                                      | 23.9 ms: 1.11x faster                                        |
| regex_effbot   | 2.99 ms                                                      | 3.50 ms: 1.17x slower                                        |
| Geometric mean | (ref)                                                        | 1.08x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                       | 319 us: 1.43x faster                                         |
| xml_etree_process    | 76.0 ms                                                      | 56.5 ms: 1.35x faster                                        |
| unpickle_pure_python | 321 us                                                       | 241 us: 1.33x faster                                         |
| tomli_loads          | 2.97 sec                                                     | 2.26 sec: 1.31x faster                                       |
| xml_etree_generate   | 94.6 ms                                                      | 80.5 ms: 1.17x faster                                        |
| pickle_list          | 4.11 us                                                      | 3.83 us: 1.07x faster                                        |
| json_dumps           | 14.2 ms                                                      | 13.4 ms: 1.06x faster                                        |
| xml_etree_iterparse  | 110 ms                                                       | 104 ms: 1.06x faster                                         |
| unpickle             | 14.2 us                                                      | 13.4 us: 1.05x faster                                        |
| json_loads           | 30.0 us                                                      | 28.7 us: 1.04x faster                                        |
| pickle               | 9.94 us                                                      | 9.64 us: 1.03x faster                                        |
| xml_etree_parse      | 162 ms                                                       | 158 ms: 1.02x faster                                         |
| unpickle_list        | 4.49 us                                                      | 4.53 us: 1.01x slower                                        |
| pickle_dict          | 30.0 us                                                      | 30.8 us: 1.03x slower                                        |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 10.8 ms: 1.07x faster                                        |
| python_startup_no_site | 7.32 ms                                                      | 7.76 ms: 1.06x slower                                        |
| Geometric mean         | (ref)                                                        | 1.00x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 11.0 ms: 1.34x faster                                        |
| django_template | 51.5 ms                                                      | 40.2 ms: 1.28x faster                                        |
| genshi_text     | 31.5 ms                                                      | 26.1 ms: 1.20x faster                                        |
| genshi_xml      | 64.7 ms                                                      | 58.5 ms: 1.11x faster                                        |
| Geometric mean  | (ref)                                                        | 1.23x faster                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| deltablue               | 7.47 ms                                                      | 4.00 ms: 1.87x faster                                        |
| logging_silent          | 166 ns                                                       | 101 ns: 1.64x faster                                         |
| scimark_monte_carlo     | 109 ms                                                       | 68.2 ms: 1.60x faster                                        |
| scimark_sor             | 177 ms                                                       | 111 ms: 1.59x faster                                         |
| go                      | 259 ms                                                       | 164 ms: 1.58x faster                                         |
| pyflate                 | 697 ms                                                       | 449 ms: 1.55x faster                                         |
| bench_mp_pool           | 7.18 ms                                                      | 4.62 ms: 1.55x faster                                        |
| raytrace                | 488 ms                                                       | 317 ms: 1.54x faster                                         |
| richards                | 74.1 ms                                                      | 48.3 ms: 1.53x faster                                        |
| nbody                   | 137 ms                                                       | 90.7 ms: 1.51x faster                                        |
| richards_super          | 90.8 ms                                                      | 61.0 ms: 1.49x faster                                        |
| float                   | 110 ms                                                       | 74.2 ms: 1.49x faster                                        |
| sqlglot_parse           | 2.26 ms                                                      | 1.53 ms: 1.47x faster                                        |
| spectral_norm           | 136 ms                                                       | 93.3 ms: 1.46x faster                                        |
| pickle_pure_python      | 457 us                                                       | 319 us: 1.43x faster                                         |
| scimark_lu              | 164 ms                                                       | 115 ms: 1.43x faster                                         |
| crypto_pyaes            | 118 ms                                                       | 83.4 ms: 1.42x faster                                        |
| sqlglot_transpile       | 2.71 ms                                                      | 1.92 ms: 1.41x faster                                        |
| async_tree_io           | 1.61 sec                                                     | 1.17 sec: 1.37x faster                                       |
| async_tree_none         | 700 ms                                                       | 519 ms: 1.35x faster                                         |
| xml_etree_process       | 76.0 ms                                                      | 56.5 ms: 1.35x faster                                        |
| pprint_safe_repr        | 1.05 sec                                                     | 784 ms: 1.34x faster                                         |
| async_generators        | 422 ms                                                       | 316 ms: 1.34x faster                                         |
| mako                    | 14.7 ms                                                      | 11.0 ms: 1.34x faster                                        |
| hexiom                  | 9.52 ms                                                      | 7.13 ms: 1.33x faster                                        |
| unpickle_pure_python    | 321 us                                                       | 241 us: 1.33x faster                                         |
| chaos                   | 107 ms                                                       | 80.9 ms: 1.32x faster                                        |
| pprint_pformat          | 2.15 sec                                                     | 1.63 sec: 1.32x faster                                       |
| tomli_loads             | 2.97 sec                                                     | 2.26 sec: 1.31x faster                                       |
| async_tree_memoization  | 824 ms                                                       | 630 ms: 1.31x faster                                         |
| unpack_sequence         | 59.5 ns                                                      | 45.6 ns: 1.30x faster                                        |
| html5lib                | 94.6 ms                                                      | 72.9 ms: 1.30x faster                                        |
| scimark_sparse_mat_mult | 5.19 ms                                                      | 4.05 ms: 1.28x faster                                        |
| django_template         | 51.5 ms                                                      | 40.2 ms: 1.28x faster                                        |
| async_tree_cpu_io_mixed | 952 ms                                                       | 749 ms: 1.27x faster                                         |
| chameleon               | 9.72 ms                                                      | 7.67 ms: 1.27x faster                                        |
| scimark_fft             | 359 ms                                                       | 285 ms: 1.26x faster                                         |
| deepcopy_memo           | 48.9 us                                                      | 38.8 us: 1.26x faster                                        |
| thrift                  | 1.16 ms                                                      | 925 us: 1.26x faster                                         |
| pycparser               | 1.66 sec                                                     | 1.32 sec: 1.26x faster                                       |
| tornado_http            | 152 ms                                                       | 122 ms: 1.25x faster                                         |
| logging_simple          | 8.90 us                                                      | 7.19 us: 1.24x faster                                        |
| regex_compile           | 194 ms                                                       | 158 ms: 1.23x faster                                         |
| aiohttp                 | 1.21 ms                                                      | 985 us: 1.23x faster                                         |
| 2to3                    | 350 ms                                                       | 288 ms: 1.22x faster                                         |
| sqlalchemy_declarative  | 187 ms                                                       | 154 ms: 1.21x faster                                         |
| gunicorn                | 1.17 ms                                                      | 973 us: 1.21x faster                                         |
| genshi_text             | 31.5 ms                                                      | 26.1 ms: 1.20x faster                                        |
| docutils                | 3.40 sec                                                     | 2.86 sec: 1.19x faster                                       |
| sqlite_synth            | 2.97 us                                                      | 2.50 us: 1.19x faster                                        |
| logging_format          | 9.57 us                                                      | 8.11 us: 1.18x faster                                        |
| sqlglot_optimize        | 70.3 ms                                                      | 59.8 ms: 1.18x faster                                        |
| xml_etree_generate      | 94.6 ms                                                      | 80.5 ms: 1.17x faster                                        |
| dulwich_log             | 80.1 ms                                                      | 68.4 ms: 1.17x faster                                        |
| fannkuch                | 496 ms                                                       | 429 ms: 1.16x faster                                         |
| deepcopy_reduce         | 4.03 us                                                      | 3.51 us: 1.15x faster                                        |
| sqlglot_normalize       | 144 ms                                                       | 126 ms: 1.15x faster                                         |
| regex_dna               | 259 ms                                                       | 227 ms: 1.14x faster                                         |
| pathlib                 | 21.7 ms                                                      | 19.1 ms: 1.14x faster                                        |
| deepcopy                | 454 us                                                       | 399 us: 1.14x faster                                         |
| create_gc_cycles        | 1.82 ms                                                      | 1.61 ms: 1.13x faster                                        |
| flaskblogging           | 4.39 ms                                                      | 3.88 ms: 1.13x faster                                        |
| dask                    | 463 ms                                                       | 410 ms: 1.13x faster                                         |
| sqlalchemy_imperative   | 22.6 ms                                                      | 20.1 ms: 1.13x faster                                        |
| bench_thread_pool       | 1.14 ms                                                      | 1.01 ms: 1.12x faster                                        |
| regex_v8                | 26.6 ms                                                      | 23.9 ms: 1.11x faster                                        |
| genshi_xml              | 64.7 ms                                                      | 58.5 ms: 1.11x faster                                        |
| mdp                     | 3.03 sec                                                     | 2.75 sec: 1.10x faster                                       |
| coroutines              | 30.4 ms                                                      | 27.6 ms: 1.10x faster                                        |
| comprehensions          | 26.9 us                                                      | 24.6 us: 1.09x faster                                        |
| nqueens                 | 112 ms                                                       | 103 ms: 1.09x faster                                         |
| pylint                  | 562 ms                                                       | 515 ms: 1.09x faster                                         |
| sympy_integrate         | 28.1 ms                                                      | 25.8 ms: 1.09x faster                                        |
| sympy_expand            | 599 ms                                                       | 555 ms: 1.08x faster                                         |
| pidigits                | 271 ms                                                       | 251 ms: 1.08x faster                                         |
| pickle_list             | 4.11 us                                                      | 3.83 us: 1.07x faster                                        |
| python_startup          | 11.5 ms                                                      | 10.8 ms: 1.07x faster                                        |
| json_dumps              | 14.2 ms                                                      | 13.4 ms: 1.06x faster                                        |
| sympy_str               | 358 ms                                                       | 337 ms: 1.06x faster                                         |
| xml_etree_iterparse     | 110 ms                                                       | 104 ms: 1.06x faster                                         |
| json                    | 5.96 ms                                                      | 5.65 ms: 1.06x faster                                        |
| unpickle                | 14.2 us                                                      | 13.4 us: 1.05x faster                                        |
| meteor_contest          | 137 ms                                                       | 131 ms: 1.05x faster                                         |
| json_loads              | 30.0 us                                                      | 28.7 us: 1.04x faster                                        |
| sympy_sum               | 193 ms                                                       | 185 ms: 1.04x faster                                         |
| telco                   | 7.14 ms                                                      | 6.86 ms: 1.04x faster                                        |
| asyncio_tcp             | 782 ms                                                       | 753 ms: 1.04x faster                                         |
| generators              | 58.0 ms                                                      | 56.0 ms: 1.03x faster                                        |
| pickle                  | 9.94 us                                                      | 9.64 us: 1.03x faster                                        |
| xml_etree_parse         | 162 ms                                                       | 158 ms: 1.02x faster                                         |
| unpickle_list           | 4.49 us                                                      | 4.53 us: 1.01x slower                                        |
| pickle_dict             | 30.0 us                                                      | 30.8 us: 1.03x slower                                        |
| python_startup_no_site  | 7.32 ms                                                      | 7.76 ms: 1.06x slower                                        |
| gc_traversal            | 3.45 ms                                                      | 3.85 ms: 1.11x slower                                        |
| regex_effbot            | 2.99 ms                                                      | 3.50 ms: 1.17x slower                                        |
| coverage                | 64.0 ms                                                      | 84.8 ms: 1.33x slower                                        |
| Geometric mean          | (ref)                                                        | 1.21x faster                                                 |

Benchmark hidden because not significant (3): mypy2, asyncio_tcp_ssl, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.15x
