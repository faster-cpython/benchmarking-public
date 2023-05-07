
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 42f54d1
- commit date: 2023-05-06
- overall geometric mean: 1.27x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-pythonperf2-x86_64-python-main-3.12.0a7+-42f54d1 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 352 ms                                                       | 284 ms: 1.24x faster                                         |
| docutils       | 3.41 sec                                                     | 2.90 sec: 1.18x faster                                       |
| tornado_http   | 151 ms                                                       | 116 ms: 1.30x faster                                         |
| Geometric mean | (ref)                                                        | 1.24x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-pythonperf2-x86_64-python-main-3.12.0a7+-42f54d1 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 132 ms                                                       | 91.8 ms: 1.44x faster                                        |
| float          | 109 ms                                                       | 77.6 ms: 1.41x faster                                        |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                         |
| Geometric mean | (ref)                                                        | 1.28x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-pythonperf2-x86_64-python-main-3.12.0a7+-42f54d1 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 191 ms                                                       | 146 ms: 1.30x faster                                         |
| regex_dna      | 261 ms                                                       | 234 ms: 1.11x faster                                         |
| regex_v8       | 26.0 ms                                                      | 23.9 ms: 1.09x faster                                        |
| regex_effbot   | 2.99 ms                                                      | 3.42 ms: 1.14x slower                                        |
| Geometric mean | (ref)                                                        | 1.08x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-pythonperf2-x86_64-python-main-3.12.0a7+-42f54d1 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle_pure_python | 318 us                                                       | 206 us: 1.55x faster                                         |
| pickle_pure_python   | 451 us                                                       | 319 us: 1.42x faster                                         |
| json_dumps           | 14.3 ms                                                      | 10.2 ms: 1.39x faster                                        |
| xml_etree_process    | 77.6 ms                                                      | 58.8 ms: 1.32x faster                                        |
| json_loads           | 30.3 us                                                      | 24.2 us: 1.25x faster                                        |
| xml_etree_generate   | 94.1 ms                                                      | 85.2 ms: 1.10x faster                                        |
| xml_etree_parse      | 160 ms                                                       | 146 ms: 1.10x faster                                         |
| xml_etree_iterparse  | 109 ms                                                       | 105 ms: 1.04x faster                                         |
| pickle               | 10.1 us                                                      | 9.94 us: 1.02x faster                                        |
| unpickle_list        | 4.73 us                                                      | 4.81 us: 1.02x slower                                        |
| pickle_list          | 4.11 us                                                      | 4.42 us: 1.07x slower                                        |
| pickle_dict          | 29.5 us                                                      | 31.8 us: 1.08x slower                                        |
| unpickle             | 13.3 us                                                      | 14.6 us: 1.10x slower                                        |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-pythonperf2-x86_64-python-main-3.12.0a7+-42f54d1 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.3 ms: 1.02x faster                                        |
| python_startup_no_site | 7.32 ms                                                      | 8.39 ms: 1.14x slower                                        |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-pythonperf2-x86_64-python-main-3.12.0a7+-42f54d1 |
|-----------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 10.1 ms: 1.46x faster                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-pythonperf2-x86_64-python-main-3.12.0a7+-42f54d1 |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| deltablue               | 7.54 ms                                                      | 3.27 ms: 2.31x faster                                        |
| asyncio_tcp             | 787 ms                                                       | 383 ms: 2.06x faster                                         |
| go                      | 264 ms                                                       | 147 ms: 1.80x faster                                         |
| logging_silent          | 165 ns                                                       | 91.5 ns: 1.80x faster                                        |
| pyflate                 | 731 ms                                                       | 438 ms: 1.67x faster                                         |
| richards                | 73.9 ms                                                      | 45.0 ms: 1.64x faster                                        |
| scimark_lu              | 164 ms                                                       | 100 ms: 1.64x faster                                         |
| hexiom                  | 9.54 ms                                                      | 5.86 ms: 1.63x faster                                        |
| sqlglot_parse           | 2.24 ms                                                      | 1.38 ms: 1.63x faster                                        |
| chaos                   | 108 ms                                                       | 67.4 ms: 1.60x faster                                        |
| raytrace                | 491 ms                                                       | 307 ms: 1.60x faster                                         |
| scimark_sor             | 177 ms                                                       | 112 ms: 1.58x faster                                         |
| generators              | 57.0 ms                                                      | 36.6 ms: 1.56x faster                                        |
| unpickle_pure_python    | 318 us                                                       | 206 us: 1.55x faster                                         |
| scimark_monte_carlo     | 109 ms                                                       | 71.7 ms: 1.52x faster                                        |
| sqlglot_transpile       | 2.69 ms                                                      | 1.78 ms: 1.51x faster                                        |
| spectral_norm           | 138 ms                                                       | 92.6 ms: 1.49x faster                                        |
| async_tree_io           | 1.61 sec                                                     | 1.10 sec: 1.47x faster                                       |
| mako                    | 14.7 ms                                                      | 10.1 ms: 1.46x faster                                        |
| async_tree_none         | 698 ms                                                       | 481 ms: 1.45x faster                                         |
| fannkuch                | 496 ms                                                       | 343 ms: 1.45x faster                                         |
| crypto_pyaes            | 119 ms                                                       | 82.1 ms: 1.44x faster                                        |
| nbody                   | 132 ms                                                       | 91.8 ms: 1.44x faster                                        |
| bench_mp_pool           | 7.10 ms                                                      | 4.98 ms: 1.43x faster                                        |
| async_tree_memoization  | 822 ms                                                       | 578 ms: 1.42x faster                                         |
| pickle_pure_python      | 451 us                                                       | 319 us: 1.42x faster                                         |
| float                   | 109 ms                                                       | 77.6 ms: 1.41x faster                                        |
| json_dumps              | 14.3 ms                                                      | 10.2 ms: 1.39x faster                                        |
| coroutines              | 30.6 ms                                                      | 22.3 ms: 1.37x faster                                        |
| deepcopy_memo           | 49.2 us                                                      | 36.2 us: 1.36x faster                                        |
| logging_simple          | 9.24 us                                                      | 6.87 us: 1.34x faster                                        |
| pycparser               | 1.66 sec                                                     | 1.24 sec: 1.34x faster                                       |
| async_tree_cpu_io_mixed | 951 ms                                                       | 715 ms: 1.33x faster                                         |
| xml_etree_process       | 77.6 ms                                                      | 58.8 ms: 1.32x faster                                        |
| logging_format          | 9.94 us                                                      | 7.56 us: 1.31x faster                                        |
| pprint_pformat          | 2.12 sec                                                     | 1.62 sec: 1.31x faster                                       |
| regex_compile           | 191 ms                                                       | 146 ms: 1.30x faster                                         |
| tornado_http            | 151 ms                                                       | 116 ms: 1.30x faster                                         |
| nqueens                 | 114 ms                                                       | 88.1 ms: 1.29x faster                                        |
| pprint_safe_repr        | 1.03 sec                                                     | 798 ms: 1.29x faster                                         |
| json_loads              | 30.3 us                                                      | 24.2 us: 1.25x faster                                        |
| mypy2                   | 466 ms                                                       | 373 ms: 1.25x faster                                         |
| 2to3                    | 352 ms                                                       | 284 ms: 1.24x faster                                         |
| dulwich_log             | 80.5 ms                                                      | 65.3 ms: 1.23x faster                                        |
| sqlglot_normalize       | 147 ms                                                       | 120 ms: 1.22x faster                                         |
| deepcopy                | 457 us                                                       | 375 us: 1.22x faster                                         |
| bench_thread_pool       | 1.14 ms                                                      | 944 us: 1.21x faster                                         |
| scimark_fft             | 359 ms                                                       | 300 ms: 1.20x faster                                         |
| scimark_sparse_mat_mult | 5.09 ms                                                      | 4.26 ms: 1.20x faster                                        |
| sqlglot_optimize        | 70.1 ms                                                      | 58.8 ms: 1.19x faster                                        |
| unpack_sequence         | 59.7 ns                                                      | 50.1 ns: 1.19x faster                                        |
| docutils                | 3.41 sec                                                     | 2.90 sec: 1.18x faster                                       |
| mdp                     | 2.95 sec                                                     | 2.51 sec: 1.18x faster                                       |
| deepcopy_reduce         | 3.91 us                                                      | 3.37 us: 1.16x faster                                        |
| json                    | 5.94 ms                                                      | 5.21 ms: 1.14x faster                                        |
| sqlite_synth            | 2.96 us                                                      | 2.63 us: 1.13x faster                                        |
| comprehensions          | 27.3 us                                                      | 24.4 us: 1.12x faster                                        |
| regex_dna               | 261 ms                                                       | 234 ms: 1.11x faster                                         |
| create_gc_cycles        | 1.80 ms                                                      | 1.63 ms: 1.11x faster                                        |
| xml_etree_generate      | 94.1 ms                                                      | 85.2 ms: 1.10x faster                                        |
| meteor_contest          | 142 ms                                                       | 129 ms: 1.10x faster                                         |
| xml_etree_parse         | 160 ms                                                       | 146 ms: 1.10x faster                                         |
| regex_v8                | 26.0 ms                                                      | 23.9 ms: 1.09x faster                                        |
| async_generators        | 419 ms                                                       | 392 ms: 1.07x faster                                         |
| pathlib                 | 21.3 ms                                                      | 20.0 ms: 1.06x faster                                        |
| xml_etree_iterparse     | 109 ms                                                       | 105 ms: 1.04x faster                                         |
| pidigits                | 271 ms                                                       | 260 ms: 1.04x faster                                         |
| pickle                  | 10.1 us                                                      | 9.94 us: 1.02x faster                                        |
| python_startup          | 11.5 ms                                                      | 11.3 ms: 1.02x faster                                        |
| unpickle_list           | 4.73 us                                                      | 4.81 us: 1.02x slower                                        |
| telco                   | 7.14 ms                                                      | 7.27 ms: 1.02x slower                                        |
| pickle_list             | 4.11 us                                                      | 4.42 us: 1.07x slower                                        |
| pickle_dict             | 29.5 us                                                      | 31.8 us: 1.08x slower                                        |
| unpickle                | 13.3 us                                                      | 14.6 us: 1.10x slower                                        |
| gc_traversal            | 3.46 ms                                                      | 3.82 ms: 1.10x slower                                        |
| regex_effbot            | 2.99 ms                                                      | 3.42 ms: 1.14x slower                                        |
| python_startup_no_site  | 7.32 ms                                                      | 8.39 ms: 1.14x slower                                        |
| dask                    | 478 ms                                                       | 560 ms: 1.17x slower                                         |
| coverage                | 71.1 ms                                                      | 92.9 ms: 1.31x slower                                        |
| Geometric mean          | (ref)                                                        | 1.27x faster                                                 |
Ignored benchmarks (16) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
