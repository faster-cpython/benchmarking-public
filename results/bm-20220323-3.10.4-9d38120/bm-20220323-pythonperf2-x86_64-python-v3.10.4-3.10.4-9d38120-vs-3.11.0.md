
# Results vs. 3.11.0

- fork: python
- ref: v3.10.4
- machine: linux-x86_64
- commit hash: 9d38120
- commit date: 2022-03-23
- overall geometric mean: 1.21x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 350 ms: 1.22x slower                                         |
| chameleon      | 7.67 ms                                                      | 9.72 ms: 1.27x slower                                        |
| docutils       | 2.86 sec                                                     | 3.40 sec: 1.19x slower                                       |
| html5lib       | 72.9 ms                                                      | 94.6 ms: 1.30x slower                                        |
| tornado_http   | 122 ms                                                       | 152 ms: 1.25x slower                                         |
| Geometric mean | (ref)                                                        | 1.24x slower                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| pidigits       | 251 ms                                                       | 271 ms: 1.08x slower                                         |
| float          | 74.2 ms                                                      | 110 ms: 1.49x slower                                         |
| nbody          | 90.7 ms                                                      | 137 ms: 1.51x slower                                         |
| Geometric mean | (ref)                                                        | 1.34x slower                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot   | 3.50 ms                                                      | 2.99 ms: 1.17x faster                                        |
| regex_v8       | 23.9 ms                                                      | 26.6 ms: 1.11x slower                                        |
| regex_dna      | 227 ms                                                       | 259 ms: 1.14x slower                                         |
| regex_compile  | 158 ms                                                       | 194 ms: 1.23x slower                                         |
| Geometric mean | (ref)                                                        | 1.08x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_dict          | 30.8 us                                                      | 30.0 us: 1.03x faster                                        |
| unpickle_list        | 4.53 us                                                      | 4.49 us: 1.01x faster                                        |
| xml_etree_parse      | 158 ms                                                       | 162 ms: 1.02x slower                                         |
| pickle               | 9.64 us                                                      | 9.94 us: 1.03x slower                                        |
| json_loads           | 28.7 us                                                      | 30.0 us: 1.04x slower                                        |
| unpickle             | 13.4 us                                                      | 14.2 us: 1.05x slower                                        |
| xml_etree_iterparse  | 104 ms                                                       | 110 ms: 1.06x slower                                         |
| json_dumps           | 13.4 ms                                                      | 14.2 ms: 1.06x slower                                        |
| pickle_list          | 3.83 us                                                      | 4.11 us: 1.07x slower                                        |
| xml_etree_generate   | 80.5 ms                                                      | 94.6 ms: 1.17x slower                                        |
| tomli_loads          | 2.26 sec                                                     | 2.97 sec: 1.31x slower                                       |
| unpickle_pure_python | 241 us                                                       | 321 us: 1.33x slower                                         |
| xml_etree_process    | 56.5 ms                                                      | 76.0 ms: 1.35x slower                                        |
| pickle_pure_python   | 319 us                                                       | 457 us: 1.43x slower                                         |
| Geometric mean       | (ref)                                                        | 1.13x slower                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 7.76 ms                                                      | 7.32 ms: 1.06x faster                                        |
| python_startup         | 10.8 ms                                                      | 11.5 ms: 1.07x slower                                        |
| Geometric mean         | (ref)                                                        | 1.00x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_xml      | 58.5 ms                                                      | 64.7 ms: 1.11x slower                                        |
| genshi_text     | 26.1 ms                                                      | 31.5 ms: 1.20x slower                                        |
| django_template | 40.2 ms                                                      | 51.5 ms: 1.28x slower                                        |
| mako            | 11.0 ms                                                      | 14.7 ms: 1.34x slower                                        |
| Geometric mean  | (ref)                                                        | 1.23x slower                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| coverage                | 84.8 ms                                                      | 64.0 ms: 1.33x faster                                        |
| regex_effbot            | 3.50 ms                                                      | 2.99 ms: 1.17x faster                                        |
| gc_traversal            | 3.85 ms                                                      | 3.45 ms: 1.11x faster                                        |
| python_startup_no_site  | 7.76 ms                                                      | 7.32 ms: 1.06x faster                                        |
| pickle_dict             | 30.8 us                                                      | 30.0 us: 1.03x faster                                        |
| unpickle_list           | 4.53 us                                                      | 4.49 us: 1.01x faster                                        |
| xml_etree_parse         | 158 ms                                                       | 162 ms: 1.02x slower                                         |
| pickle                  | 9.64 us                                                      | 9.94 us: 1.03x slower                                        |
| generators              | 56.0 ms                                                      | 58.0 ms: 1.03x slower                                        |
| asyncio_tcp             | 753 ms                                                       | 782 ms: 1.04x slower                                         |
| telco                   | 6.86 ms                                                      | 7.14 ms: 1.04x slower                                        |
| sympy_sum               | 185 ms                                                       | 193 ms: 1.04x slower                                         |
| json_loads              | 28.7 us                                                      | 30.0 us: 1.04x slower                                        |
| meteor_contest          | 131 ms                                                       | 137 ms: 1.05x slower                                         |
| unpickle                | 13.4 us                                                      | 14.2 us: 1.05x slower                                        |
| json                    | 5.65 ms                                                      | 5.96 ms: 1.06x slower                                        |
| xml_etree_iterparse     | 104 ms                                                       | 110 ms: 1.06x slower                                         |
| sympy_str               | 337 ms                                                       | 358 ms: 1.06x slower                                         |
| json_dumps              | 13.4 ms                                                      | 14.2 ms: 1.06x slower                                        |
| python_startup          | 10.8 ms                                                      | 11.5 ms: 1.07x slower                                        |
| pickle_list             | 3.83 us                                                      | 4.11 us: 1.07x slower                                        |
| pidigits                | 251 ms                                                       | 271 ms: 1.08x slower                                         |
| sympy_expand            | 555 ms                                                       | 599 ms: 1.08x slower                                         |
| sympy_integrate         | 25.8 ms                                                      | 28.1 ms: 1.09x slower                                        |
| pylint                  | 515 ms                                                       | 562 ms: 1.09x slower                                         |
| nqueens                 | 103 ms                                                       | 112 ms: 1.09x slower                                         |
| comprehensions          | 24.6 us                                                      | 26.9 us: 1.09x slower                                        |
| coroutines              | 27.6 ms                                                      | 30.4 ms: 1.10x slower                                        |
| mdp                     | 2.75 sec                                                     | 3.03 sec: 1.10x slower                                       |
| genshi_xml              | 58.5 ms                                                      | 64.7 ms: 1.11x slower                                        |
| regex_v8                | 23.9 ms                                                      | 26.6 ms: 1.11x slower                                        |
| bench_thread_pool       | 1.01 ms                                                      | 1.14 ms: 1.12x slower                                        |
| sqlalchemy_imperative   | 20.1 ms                                                      | 22.6 ms: 1.13x slower                                        |
| dask                    | 410 ms                                                       | 463 ms: 1.13x slower                                         |
| flaskblogging           | 3.88 ms                                                      | 4.39 ms: 1.13x slower                                        |
| create_gc_cycles        | 1.61 ms                                                      | 1.82 ms: 1.13x slower                                        |
| deepcopy                | 399 us                                                       | 454 us: 1.14x slower                                         |
| pathlib                 | 19.1 ms                                                      | 21.7 ms: 1.14x slower                                        |
| regex_dna               | 227 ms                                                       | 259 ms: 1.14x slower                                         |
| sqlglot_normalize       | 126 ms                                                       | 144 ms: 1.15x slower                                         |
| deepcopy_reduce         | 3.51 us                                                      | 4.03 us: 1.15x slower                                        |
| fannkuch                | 429 ms                                                       | 496 ms: 1.16x slower                                         |
| dulwich_log             | 68.4 ms                                                      | 80.1 ms: 1.17x slower                                        |
| xml_etree_generate      | 80.5 ms                                                      | 94.6 ms: 1.17x slower                                        |
| sqlglot_optimize        | 59.8 ms                                                      | 70.3 ms: 1.18x slower                                        |
| logging_format          | 8.11 us                                                      | 9.57 us: 1.18x slower                                        |
| sqlite_synth            | 2.50 us                                                      | 2.97 us: 1.19x slower                                        |
| docutils                | 2.86 sec                                                     | 3.40 sec: 1.19x slower                                       |
| genshi_text             | 26.1 ms                                                      | 31.5 ms: 1.20x slower                                        |
| gunicorn                | 973 us                                                       | 1.17 ms: 1.21x slower                                        |
| sqlalchemy_declarative  | 154 ms                                                       | 187 ms: 1.21x slower                                         |
| 2to3                    | 288 ms                                                       | 350 ms: 1.22x slower                                         |
| aiohttp                 | 985 us                                                       | 1.21 ms: 1.23x slower                                        |
| regex_compile           | 158 ms                                                       | 194 ms: 1.23x slower                                         |
| logging_simple          | 7.19 us                                                      | 8.90 us: 1.24x slower                                        |
| tornado_http            | 122 ms                                                       | 152 ms: 1.25x slower                                         |
| pycparser               | 1.32 sec                                                     | 1.66 sec: 1.26x slower                                       |
| thrift                  | 925 us                                                       | 1.16 ms: 1.26x slower                                        |
| deepcopy_memo           | 38.8 us                                                      | 48.9 us: 1.26x slower                                        |
| scimark_fft             | 285 ms                                                       | 359 ms: 1.26x slower                                         |
| chameleon               | 7.67 ms                                                      | 9.72 ms: 1.27x slower                                        |
| async_tree_cpu_io_mixed | 749 ms                                                       | 952 ms: 1.27x slower                                         |
| django_template         | 40.2 ms                                                      | 51.5 ms: 1.28x slower                                        |
| scimark_sparse_mat_mult | 4.05 ms                                                      | 5.19 ms: 1.28x slower                                        |
| html5lib                | 72.9 ms                                                      | 94.6 ms: 1.30x slower                                        |
| unpack_sequence         | 45.6 ns                                                      | 59.5 ns: 1.30x slower                                        |
| async_tree_memoization  | 630 ms                                                       | 824 ms: 1.31x slower                                         |
| tomli_loads             | 2.26 sec                                                     | 2.97 sec: 1.31x slower                                       |
| pprint_pformat          | 1.63 sec                                                     | 2.15 sec: 1.32x slower                                       |
| chaos                   | 80.9 ms                                                      | 107 ms: 1.32x slower                                         |
| unpickle_pure_python    | 241 us                                                       | 321 us: 1.33x slower                                         |
| hexiom                  | 7.13 ms                                                      | 9.52 ms: 1.33x slower                                        |
| mako                    | 11.0 ms                                                      | 14.7 ms: 1.34x slower                                        |
| async_generators        | 316 ms                                                       | 422 ms: 1.34x slower                                         |
| pprint_safe_repr        | 784 ms                                                       | 1.05 sec: 1.34x slower                                       |
| xml_etree_process       | 56.5 ms                                                      | 76.0 ms: 1.35x slower                                        |
| async_tree_none         | 519 ms                                                       | 700 ms: 1.35x slower                                         |
| async_tree_io           | 1.17 sec                                                     | 1.61 sec: 1.37x slower                                       |
| sqlglot_transpile       | 1.92 ms                                                      | 2.71 ms: 1.41x slower                                        |
| crypto_pyaes            | 83.4 ms                                                      | 118 ms: 1.42x slower                                         |
| scimark_lu              | 115 ms                                                       | 164 ms: 1.43x slower                                         |
| pickle_pure_python      | 319 us                                                       | 457 us: 1.43x slower                                         |
| spectral_norm           | 93.3 ms                                                      | 136 ms: 1.46x slower                                         |
| sqlglot_parse           | 1.53 ms                                                      | 2.26 ms: 1.47x slower                                        |
| float                   | 74.2 ms                                                      | 110 ms: 1.49x slower                                         |
| richards_super          | 61.0 ms                                                      | 90.8 ms: 1.49x slower                                        |
| nbody                   | 90.7 ms                                                      | 137 ms: 1.51x slower                                         |
| richards                | 48.3 ms                                                      | 74.1 ms: 1.53x slower                                        |
| raytrace                | 317 ms                                                       | 488 ms: 1.54x slower                                         |
| bench_mp_pool           | 4.62 ms                                                      | 7.18 ms: 1.55x slower                                        |
| pyflate                 | 449 ms                                                       | 697 ms: 1.55x slower                                         |
| go                      | 164 ms                                                       | 259 ms: 1.58x slower                                         |
| scimark_sor             | 111 ms                                                       | 177 ms: 1.59x slower                                         |
| scimark_monte_carlo     | 68.2 ms                                                      | 109 ms: 1.60x slower                                         |
| logging_silent          | 101 ns                                                       | 166 ns: 1.64x slower                                         |
| deltablue               | 4.00 ms                                                      | 7.47 ms: 1.87x slower                                        |
| Geometric mean          | (ref)                                                        | 1.21x slower                                                 |

Benchmark hidden because not significant (3): typing_runtime_protocols, asyncio_tcp_ssl, mypy2
