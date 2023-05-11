
# Results vs. 3.10.4

- fork: python
- ref: v3.11.0
- machine: linux-x86_64
- commit hash: deaf509
- commit date: 2022-10-24
- overall geometric mean: 1.21x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 352 ms                                                       | 288 ms: 1.22x faster                                         |
| chameleon      | 9.62 ms                                                      | 7.67 ms: 1.25x faster                                        |
| docutils       | 3.41 sec                                                     | 2.86 sec: 1.19x faster                                       |
| html5lib       | 96.3 ms                                                      | 72.9 ms: 1.32x faster                                        |
| tornado_http   | 151 ms                                                       | 122 ms: 1.24x faster                                         |
| Geometric mean | (ref)                                                        | 1.25x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 109 ms                                                       | 74.2 ms: 1.48x faster                                        |
| nbody          | 132 ms                                                       | 90.7 ms: 1.46x faster                                        |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                         |
| Geometric mean | (ref)                                                        | 1.32x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 191 ms                                                       | 158 ms: 1.21x faster                                         |
| regex_dna      | 261 ms                                                       | 227 ms: 1.15x faster                                         |
| regex_v8       | 26.0 ms                                                      | 23.9 ms: 1.09x faster                                        |
| regex_effbot   | 2.99 ms                                                      | 3.50 ms: 1.17x slower                                        |
| Geometric mean | (ref)                                                        | 1.07x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python   | 451 us                                                       | 319 us: 1.41x faster                                         |
| xml_etree_process    | 77.6 ms                                                      | 56.5 ms: 1.37x faster                                        |
| unpickle_pure_python | 318 us                                                       | 241 us: 1.32x faster                                         |
| xml_etree_generate   | 94.1 ms                                                      | 80.5 ms: 1.17x faster                                        |
| pickle_list          | 4.11 us                                                      | 3.83 us: 1.07x faster                                        |
| json_dumps           | 14.3 ms                                                      | 13.4 ms: 1.07x faster                                        |
| json_loads           | 30.3 us                                                      | 28.7 us: 1.06x faster                                        |
| pickle               | 10.1 us                                                      | 9.64 us: 1.05x faster                                        |
| xml_etree_iterparse  | 109 ms                                                       | 104 ms: 1.05x faster                                         |
| unpickle_list        | 4.73 us                                                      | 4.53 us: 1.04x faster                                        |
| xml_etree_parse      | 160 ms                                                       | 158 ms: 1.01x faster                                         |
| unpickle             | 13.3 us                                                      | 13.4 us: 1.01x slower                                        |
| pickle_dict          | 29.5 us                                                      | 30.8 us: 1.04x slower                                        |
| Geometric mean       | (ref)                                                        | 1.11x faster                                                 |

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
| django_template | 52.0 ms                                                      | 40.2 ms: 1.29x faster                                        |
| genshi_text     | 31.7 ms                                                      | 26.1 ms: 1.21x faster                                        |
| genshi_xml      | 63.5 ms                                                      | 58.5 ms: 1.09x faster                                        |
| Geometric mean  | (ref)                                                        | 1.23x faster                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| deltablue               | 7.54 ms                                                      | 4.00 ms: 1.89x faster                                        |
| logging_silent          | 165 ns                                                       | 101 ns: 1.63x faster                                         |
| pyflate                 | 731 ms                                                       | 449 ms: 1.63x faster                                         |
| go                      | 264 ms                                                       | 164 ms: 1.61x faster                                         |
| scimark_sor             | 177 ms                                                       | 111 ms: 1.59x faster                                         |
| scimark_monte_carlo     | 109 ms                                                       | 68.2 ms: 1.59x faster                                        |
| raytrace                | 491 ms                                                       | 317 ms: 1.55x faster                                         |
| bench_mp_pool           | 7.10 ms                                                      | 4.62 ms: 1.54x faster                                        |
| richards                | 73.9 ms                                                      | 48.3 ms: 1.53x faster                                        |
| spectral_norm           | 138 ms                                                       | 93.3 ms: 1.48x faster                                        |
| float                   | 109 ms                                                       | 74.2 ms: 1.48x faster                                        |
| sqlglot_parse           | 2.24 ms                                                      | 1.53 ms: 1.46x faster                                        |
| nbody                   | 132 ms                                                       | 90.7 ms: 1.46x faster                                        |
| scimark_lu              | 164 ms                                                       | 115 ms: 1.43x faster                                         |
| crypto_pyaes            | 119 ms                                                       | 83.4 ms: 1.42x faster                                        |
| pickle_pure_python      | 451 us                                                       | 319 us: 1.41x faster                                         |
| sqlglot_transpile       | 2.69 ms                                                      | 1.92 ms: 1.40x faster                                        |
| async_tree_io           | 1.61 sec                                                     | 1.17 sec: 1.38x faster                                       |
| xml_etree_process       | 77.6 ms                                                      | 56.5 ms: 1.37x faster                                        |
| async_tree_none         | 698 ms                                                       | 519 ms: 1.34x faster                                         |
| mako                    | 14.7 ms                                                      | 11.0 ms: 1.34x faster                                        |
| hexiom                  | 9.54 ms                                                      | 7.13 ms: 1.34x faster                                        |
| chaos                   | 108 ms                                                       | 80.9 ms: 1.33x faster                                        |
| async_generators        | 419 ms                                                       | 316 ms: 1.33x faster                                         |
| thrift                  | 1.23 ms                                                      | 925 us: 1.32x faster                                         |
| unpickle_pure_python    | 318 us                                                       | 241 us: 1.32x faster                                         |
| html5lib                | 96.3 ms                                                      | 72.9 ms: 1.32x faster                                        |
| pprint_safe_repr        | 1.03 sec                                                     | 784 ms: 1.31x faster                                         |
| unpack_sequence         | 59.7 ns                                                      | 45.6 ns: 1.31x faster                                        |
| async_tree_memoization  | 822 ms                                                       | 630 ms: 1.31x faster                                         |
| pprint_pformat          | 2.12 sec                                                     | 1.63 sec: 1.30x faster                                       |
| django_template         | 52.0 ms                                                      | 40.2 ms: 1.29x faster                                        |
| logging_simple          | 9.24 us                                                      | 7.19 us: 1.28x faster                                        |
| async_tree_cpu_io_mixed | 951 ms                                                       | 749 ms: 1.27x faster                                         |
| deepcopy_memo           | 49.2 us                                                      | 38.8 us: 1.27x faster                                        |
| scimark_fft             | 359 ms                                                       | 285 ms: 1.26x faster                                         |
| scimark_sparse_mat_mult | 5.09 ms                                                      | 4.05 ms: 1.26x faster                                        |
| chameleon               | 9.62 ms                                                      | 7.67 ms: 1.25x faster                                        |
| pycparser               | 1.66 sec                                                     | 1.32 sec: 1.25x faster                                       |
| tornado_http            | 151 ms                                                       | 122 ms: 1.24x faster                                         |
| logging_format          | 9.94 us                                                      | 8.11 us: 1.22x faster                                        |
| 2to3                    | 352 ms                                                       | 288 ms: 1.22x faster                                         |
| sqlalchemy_declarative  | 188 ms                                                       | 154 ms: 1.22x faster                                         |
| genshi_text             | 31.7 ms                                                      | 26.1 ms: 1.21x faster                                        |
| regex_compile           | 191 ms                                                       | 158 ms: 1.21x faster                                         |
| aiohttp                 | 1.18 ms                                                      | 985 us: 1.20x faster                                         |
| docutils                | 3.41 sec                                                     | 2.86 sec: 1.19x faster                                       |
| sqlite_synth            | 2.96 us                                                      | 2.50 us: 1.19x faster                                        |
| gunicorn                | 1.15 ms                                                      | 973 us: 1.18x faster                                         |
| dulwich_log             | 80.5 ms                                                      | 68.4 ms: 1.18x faster                                        |
| sqlglot_optimize        | 70.1 ms                                                      | 59.8 ms: 1.17x faster                                        |
| sqlglot_normalize       | 147 ms                                                       | 126 ms: 1.17x faster                                         |
| xml_etree_generate      | 94.1 ms                                                      | 80.5 ms: 1.17x faster                                        |
| dask                    | 478 ms                                                       | 410 ms: 1.17x faster                                         |
| fannkuch                | 496 ms                                                       | 429 ms: 1.16x faster                                         |
| regex_dna               | 261 ms                                                       | 227 ms: 1.15x faster                                         |
| deepcopy                | 457 us                                                       | 399 us: 1.15x faster                                         |
| sqlalchemy_imperative   | 22.9 ms                                                      | 20.1 ms: 1.14x faster                                        |
| flaskblogging           | 4.37 ms                                                      | 3.88 ms: 1.13x faster                                        |
| bench_thread_pool       | 1.14 ms                                                      | 1.01 ms: 1.13x faster                                        |
| create_gc_cycles        | 1.80 ms                                                      | 1.61 ms: 1.12x faster                                        |
| pathlib                 | 21.3 ms                                                      | 19.1 ms: 1.12x faster                                        |
| deepcopy_reduce         | 3.91 us                                                      | 3.51 us: 1.11x faster                                        |
| coroutines              | 30.6 ms                                                      | 27.6 ms: 1.11x faster                                        |
| comprehensions          | 27.3 us                                                      | 24.6 us: 1.11x faster                                        |
| nqueens                 | 114 ms                                                       | 103 ms: 1.11x faster                                         |
| sympy_integrate         | 28.1 ms                                                      | 25.8 ms: 1.09x faster                                        |
| pylint                  | 562 ms                                                       | 515 ms: 1.09x faster                                         |
| sympy_expand            | 603 ms                                                       | 555 ms: 1.09x faster                                         |
| regex_v8                | 26.0 ms                                                      | 23.9 ms: 1.09x faster                                        |
| genshi_xml              | 63.5 ms                                                      | 58.5 ms: 1.09x faster                                        |
| meteor_contest          | 142 ms                                                       | 131 ms: 1.08x faster                                         |
| pidigits                | 271 ms                                                       | 251 ms: 1.08x faster                                         |
| mdp                     | 2.95 sec                                                     | 2.75 sec: 1.08x faster                                       |
| pickle_list             | 4.11 us                                                      | 3.83 us: 1.07x faster                                        |
| python_startup          | 11.5 ms                                                      | 10.8 ms: 1.07x faster                                        |
| json_dumps              | 14.3 ms                                                      | 13.4 ms: 1.07x faster                                        |
| sympy_str               | 358 ms                                                       | 337 ms: 1.06x faster                                         |
| json_loads              | 30.3 us                                                      | 28.7 us: 1.06x faster                                        |
| pickle                  | 10.1 us                                                      | 9.64 us: 1.05x faster                                        |
| json                    | 5.94 ms                                                      | 5.65 ms: 1.05x faster                                        |
| xml_etree_iterparse     | 109 ms                                                       | 104 ms: 1.05x faster                                         |
| asyncio_tcp             | 787 ms                                                       | 753 ms: 1.05x faster                                         |
| sympy_sum               | 193 ms                                                       | 185 ms: 1.04x faster                                         |
| unpickle_list           | 4.73 us                                                      | 4.53 us: 1.04x faster                                        |
| telco                   | 7.14 ms                                                      | 6.86 ms: 1.04x faster                                        |
| generators              | 57.0 ms                                                      | 56.0 ms: 1.02x faster                                        |
| xml_etree_parse         | 160 ms                                                       | 158 ms: 1.01x faster                                         |
| unpickle                | 13.3 us                                                      | 13.4 us: 1.01x slower                                        |
| pickle_dict             | 29.5 us                                                      | 30.8 us: 1.04x slower                                        |
| python_startup_no_site  | 7.32 ms                                                      | 7.76 ms: 1.06x slower                                        |
| gc_traversal            | 3.46 ms                                                      | 3.85 ms: 1.11x slower                                        |
| regex_effbot            | 2.99 ms                                                      | 3.50 ms: 1.17x slower                                        |
| coverage                | 71.1 ms                                                      | 84.8 ms: 1.19x slower                                        |
| Geometric mean          | (ref)                                                        | 1.21x faster                                                 |

Benchmark hidden because not significant (1): mypy2
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, richards_super, tomli_loads, typing_runtime_protocols
