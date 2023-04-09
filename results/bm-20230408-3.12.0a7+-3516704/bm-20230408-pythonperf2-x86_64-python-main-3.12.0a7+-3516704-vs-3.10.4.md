
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 3516704
- commit date: 2023-04-08
- overall geometric mean: 1.27x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230408-pythonperf2-x86_64-python-main-3.12.0a7+-3516704 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 352 ms                                                       | 284 ms: 1.24x faster                                         |
| chameleon      | 9.62 ms                                                      | 7.03 ms: 1.37x faster                                        |
| docutils       | 3.41 sec                                                     | 2.81 sec: 1.21x faster                                       |
| html5lib       | 96.3 ms                                                      | 67.1 ms: 1.44x faster                                        |
| tornado_http   | 151 ms                                                       | 115 ms: 1.31x faster                                         |
| Geometric mean | (ref)                                                        | 1.31x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230408-pythonperf2-x86_64-python-main-3.12.0a7+-3516704 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 132 ms                                                       | 84.0 ms: 1.57x faster                                        |
| float          | 109 ms                                                       | 72.6 ms: 1.51x faster                                        |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                         |
| Geometric mean | (ref)                                                        | 1.35x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230408-pythonperf2-x86_64-python-main-3.12.0a7+-3516704 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 191 ms                                                       | 149 ms: 1.28x faster                                         |
| regex_dna      | 261 ms                                                       | 235 ms: 1.11x faster                                         |
| regex_v8       | 26.0 ms                                                      | 23.5 ms: 1.11x faster                                        |
| regex_effbot   | 2.99 ms                                                      | 3.48 ms: 1.16x slower                                        |
| Geometric mean | (ref)                                                        | 1.08x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230408-pythonperf2-x86_64-python-main-3.12.0a7+-3516704 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle_pure_python | 318 us                                                       | 205 us: 1.55x faster                                         |
| pickle_pure_python   | 451 us                                                       | 314 us: 1.44x faster                                         |
| xml_etree_process    | 77.6 ms                                                      | 56.8 ms: 1.37x faster                                        |
| json_dumps           | 14.3 ms                                                      | 10.5 ms: 1.36x faster                                        |
| json_loads           | 30.3 us                                                      | 24.2 us: 1.25x faster                                        |
| xml_etree_generate   | 94.1 ms                                                      | 82.6 ms: 1.14x faster                                        |
| xml_etree_parse      | 160 ms                                                       | 145 ms: 1.10x faster                                         |
| pickle_list          | 4.11 us                                                      | 3.76 us: 1.09x faster                                        |
| xml_etree_iterparse  | 109 ms                                                       | 103 ms: 1.06x faster                                         |
| unpickle_list        | 4.73 us                                                      | 4.59 us: 1.03x faster                                        |
| pickle               | 10.1 us                                                      | 9.92 us: 1.02x faster                                        |
| pickle_dict          | 29.5 us                                                      | 30.5 us: 1.03x slower                                        |
| unpickle             | 13.3 us                                                      | 14.0 us: 1.05x slower                                        |
| Geometric mean       | (ref)                                                        | 1.16x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230408-pythonperf2-x86_64-python-main-3.12.0a7+-3516704 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.0 ms: 1.04x faster                                        |
| python_startup_no_site | 7.32 ms                                                      | 8.29 ms: 1.13x slower                                        |
| Geometric mean         | (ref)                                                        | 1.04x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230408-pythonperf2-x86_64-python-main-3.12.0a7+-3516704 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.1 ms: 1.46x faster                                        |
| django_template | 52.0 ms                                                      | 38.9 ms: 1.34x faster                                        |
| genshi_text     | 31.7 ms                                                      | 24.8 ms: 1.28x faster                                        |
| genshi_xml      | 63.5 ms                                                      | 52.7 ms: 1.21x faster                                        |
| Geometric mean  | (ref)                                                        | 1.32x faster                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230408-pythonperf2-x86_64-python-main-3.12.0a7+-3516704 |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| deltablue               | 7.54 ms                                                      | 3.40 ms: 2.22x faster                                        |
| asyncio_tcp             | 787 ms                                                       | 384 ms: 2.05x faster                                         |
| logging_silent          | 165 ns                                                       | 96.0 ns: 1.71x faster                                        |
| raytrace                | 491 ms                                                       | 288 ms: 1.71x faster                                         |
| sqlglot_parse           | 2.24 ms                                                      | 1.35 ms: 1.67x faster                                        |
| go                      | 264 ms                                                       | 160 ms: 1.65x faster                                         |
| pyflate                 | 731 ms                                                       | 446 ms: 1.64x faster                                         |
| scimark_monte_carlo     | 109 ms                                                       | 67.4 ms: 1.61x faster                                        |
| scimark_lu              | 164 ms                                                       | 104 ms: 1.58x faster                                         |
| nbody                   | 132 ms                                                       | 84.0 ms: 1.57x faster                                        |
| scimark_sor             | 177 ms                                                       | 113 ms: 1.57x faster                                         |
| sqlglot_transpile       | 2.69 ms                                                      | 1.71 ms: 1.57x faster                                        |
| richards                | 73.9 ms                                                      | 47.4 ms: 1.56x faster                                        |
| unpickle_pure_python    | 318 us                                                       | 205 us: 1.55x faster                                         |
| generators              | 57.0 ms                                                      | 37.6 ms: 1.52x faster                                        |
| spectral_norm           | 138 ms                                                       | 91.2 ms: 1.51x faster                                        |
| float                   | 109 ms                                                       | 72.6 ms: 1.51x faster                                        |
| chaos                   | 108 ms                                                       | 72.0 ms: 1.50x faster                                        |
| bench_mp_pool           | 7.10 ms                                                      | 4.82 ms: 1.47x faster                                        |
| mako                    | 14.7 ms                                                      | 10.1 ms: 1.46x faster                                        |
| hexiom                  | 9.54 ms                                                      | 6.60 ms: 1.44x faster                                        |
| pickle_pure_python      | 451 us                                                       | 314 us: 1.44x faster                                         |
| html5lib                | 96.3 ms                                                      | 67.1 ms: 1.44x faster                                        |
| async_tree_io           | 1.61 sec                                                     | 1.14 sec: 1.42x faster                                       |
| deepcopy_memo           | 49.2 us                                                      | 34.8 us: 1.41x faster                                        |
| logging_simple          | 9.24 us                                                      | 6.58 us: 1.40x faster                                        |
| async_tree_none         | 698 ms                                                       | 503 ms: 1.39x faster                                         |
| crypto_pyaes            | 119 ms                                                       | 85.9 ms: 1.38x faster                                        |
| thrift                  | 1.23 ms                                                      | 891 us: 1.37x faster                                         |
| logging_format          | 9.94 us                                                      | 7.26 us: 1.37x faster                                        |
| chameleon               | 9.62 ms                                                      | 7.03 ms: 1.37x faster                                        |
| async_tree_memoization  | 822 ms                                                       | 601 ms: 1.37x faster                                         |
| xml_etree_process       | 77.6 ms                                                      | 56.8 ms: 1.37x faster                                        |
| json_dumps              | 14.3 ms                                                      | 10.5 ms: 1.36x faster                                        |
| unpack_sequence         | 59.7 ns                                                      | 44.4 ns: 1.35x faster                                        |
| pycparser               | 1.66 sec                                                     | 1.24 sec: 1.34x faster                                       |
| django_template         | 52.0 ms                                                      | 38.9 ms: 1.34x faster                                        |
| pprint_pformat          | 2.12 sec                                                     | 1.59 sec: 1.34x faster                                       |
| scimark_sparse_mat_mult | 5.09 ms                                                      | 3.81 ms: 1.34x faster                                        |
| scimark_fft             | 359 ms                                                       | 271 ms: 1.33x faster                                         |
| pprint_safe_repr        | 1.03 sec                                                     | 780 ms: 1.32x faster                                         |
| tornado_http            | 151 ms                                                       | 115 ms: 1.31x faster                                         |
| async_tree_cpu_io_mixed | 951 ms                                                       | 735 ms: 1.29x faster                                         |
| regex_compile           | 191 ms                                                       | 149 ms: 1.28x faster                                         |
| genshi_text             | 31.7 ms                                                      | 24.8 ms: 1.28x faster                                        |
| json_loads              | 30.3 us                                                      | 24.2 us: 1.25x faster                                        |
| sqlglot_normalize       | 147 ms                                                       | 118 ms: 1.25x faster                                         |
| dulwich_log             | 80.5 ms                                                      | 64.7 ms: 1.24x faster                                        |
| 2to3                    | 352 ms                                                       | 284 ms: 1.24x faster                                         |
| mypy2                   | 466 ms                                                       | 378 ms: 1.23x faster                                         |
| sqlglot_optimize        | 70.1 ms                                                      | 57.5 ms: 1.22x faster                                        |
| deepcopy                | 457 us                                                       | 376 us: 1.22x faster                                         |
| docutils                | 3.41 sec                                                     | 2.81 sec: 1.21x faster                                       |
| coroutines              | 30.6 ms                                                      | 25.2 ms: 1.21x faster                                        |
| genshi_xml              | 63.5 ms                                                      | 52.7 ms: 1.21x faster                                        |
| bench_thread_pool       | 1.14 ms                                                      | 955 us: 1.19x faster                                         |
| deepcopy_reduce         | 3.91 us                                                      | 3.30 us: 1.19x faster                                        |
| mdp                     | 2.95 sec                                                     | 2.54 sec: 1.16x faster                                       |
| json                    | 5.94 ms                                                      | 5.13 ms: 1.16x faster                                        |
| fannkuch                | 496 ms                                                       | 432 ms: 1.15x faster                                         |
| xml_etree_generate      | 94.1 ms                                                      | 82.6 ms: 1.14x faster                                        |
| create_gc_cycles        | 1.80 ms                                                      | 1.59 ms: 1.13x faster                                        |
| sqlite_synth            | 2.96 us                                                      | 2.62 us: 1.13x faster                                        |
| sympy_integrate         | 28.1 ms                                                      | 25.0 ms: 1.12x faster                                        |
| sympy_expand            | 603 ms                                                       | 538 ms: 1.12x faster                                         |
| nqueens                 | 114 ms                                                       | 102 ms: 1.12x faster                                         |
| regex_dna               | 261 ms                                                       | 235 ms: 1.11x faster                                         |
| regex_v8                | 26.0 ms                                                      | 23.5 ms: 1.11x faster                                        |
| meteor_contest          | 142 ms                                                       | 128 ms: 1.11x faster                                         |
| comprehensions          | 27.3 us                                                      | 24.7 us: 1.10x faster                                        |
| xml_etree_parse         | 160 ms                                                       | 145 ms: 1.10x faster                                         |
| async_generators        | 419 ms                                                       | 381 ms: 1.10x faster                                         |
| pickle_list             | 4.11 us                                                      | 3.76 us: 1.09x faster                                        |
| sympy_str               | 358 ms                                                       | 330 ms: 1.08x faster                                         |
| pathlib                 | 21.3 ms                                                      | 19.8 ms: 1.07x faster                                        |
| xml_etree_iterparse     | 109 ms                                                       | 103 ms: 1.06x faster                                         |
| sympy_sum               | 193 ms                                                       | 183 ms: 1.05x faster                                         |
| telco                   | 7.14 ms                                                      | 6.82 ms: 1.05x faster                                        |
| python_startup          | 11.5 ms                                                      | 11.0 ms: 1.04x faster                                        |
| pidigits                | 271 ms                                                       | 260 ms: 1.04x faster                                         |
| unpickle_list           | 4.73 us                                                      | 4.59 us: 1.03x faster                                        |
| pickle                  | 10.1 us                                                      | 9.92 us: 1.02x faster                                        |
| pickle_dict             | 29.5 us                                                      | 30.5 us: 1.03x slower                                        |
| unpickle                | 13.3 us                                                      | 14.0 us: 1.05x slower                                        |
| gc_traversal            | 3.46 ms                                                      | 3.77 ms: 1.09x slower                                        |
| python_startup_no_site  | 7.32 ms                                                      | 8.29 ms: 1.13x slower                                        |
| coverage                | 71.1 ms                                                      | 81.2 ms: 1.14x slower                                        |
| regex_effbot            | 2.99 ms                                                      | 3.48 ms: 1.16x slower                                        |
| dask                    | 478 ms                                                       | 566 ms: 1.18x slower                                         |
| Geometric mean          | (ref)                                                        | 1.27x faster                                                 |
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative
