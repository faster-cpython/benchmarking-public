
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 2d526cd
- commit date: 2023-05-01
- overall geometric mean: 1.27x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230501-pythonperf2-x86_64-python-main-3.12.0a7+-2d526cd |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 352 ms                                                       | 286 ms: 1.23x faster                                         |
| docutils       | 3.41 sec                                                     | 2.89 sec: 1.18x faster                                       |
| html5lib       | 96.3 ms                                                      | 68.0 ms: 1.42x faster                                        |
| tornado_http   | 151 ms                                                       | 113 ms: 1.33x faster                                         |
| Geometric mean | (ref)                                                        | 1.29x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230501-pythonperf2-x86_64-python-main-3.12.0a7+-2d526cd |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 132 ms                                                       | 89.2 ms: 1.48x faster                                        |
| float          | 109 ms                                                       | 77.8 ms: 1.41x faster                                        |
| pidigits       | 271 ms                                                       | 259 ms: 1.04x faster                                         |
| Geometric mean | (ref)                                                        | 1.30x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230501-pythonperf2-x86_64-python-main-3.12.0a7+-2d526cd |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 191 ms                                                       | 144 ms: 1.32x faster                                         |
| regex_dna      | 261 ms                                                       | 230 ms: 1.13x faster                                         |
| regex_v8       | 26.0 ms                                                      | 23.5 ms: 1.11x faster                                        |
| regex_effbot   | 2.99 ms                                                      | 3.46 ms: 1.16x slower                                        |
| Geometric mean | (ref)                                                        | 1.09x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230501-pythonperf2-x86_64-python-main-3.12.0a7+-2d526cd |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle_pure_python | 318 us                                                       | 208 us: 1.53x faster                                         |
| pickle_pure_python   | 451 us                                                       | 319 us: 1.42x faster                                         |
| json_dumps           | 14.3 ms                                                      | 10.7 ms: 1.34x faster                                        |
| xml_etree_process    | 77.6 ms                                                      | 58.6 ms: 1.32x faster                                        |
| json_loads           | 30.3 us                                                      | 25.4 us: 1.19x faster                                        |
| xml_etree_parse      | 160 ms                                                       | 146 ms: 1.10x faster                                         |
| xml_etree_generate   | 94.1 ms                                                      | 86.2 ms: 1.09x faster                                        |
| xml_etree_iterparse  | 109 ms                                                       | 104 ms: 1.05x faster                                         |
| pickle               | 10.1 us                                                      | 9.94 us: 1.02x faster                                        |
| unpickle_list        | 4.73 us                                                      | 4.83 us: 1.02x slower                                        |
| pickle_list          | 4.11 us                                                      | 4.41 us: 1.07x slower                                        |
| pickle_dict          | 29.5 us                                                      | 31.8 us: 1.08x slower                                        |
| unpickle             | 13.3 us                                                      | 14.6 us: 1.10x slower                                        |
| Geometric mean       | (ref)                                                        | 1.12x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230501-pythonperf2-x86_64-python-main-3.12.0a7+-2d526cd |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.1 ms: 1.03x faster                                        |
| python_startup_no_site | 7.32 ms                                                      | 8.33 ms: 1.14x slower                                        |
| Geometric mean         | (ref)                                                        | 1.05x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230501-pythonperf2-x86_64-python-main-3.12.0a7+-2d526cd |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| mako           | 14.7 ms                                                      | 10.1 ms: 1.46x faster                                        |
| genshi_text    | 31.7 ms                                                      | 24.6 ms: 1.29x faster                                        |
| genshi_xml     | 63.5 ms                                                      | 53.5 ms: 1.19x faster                                        |
| Geometric mean | (ref)                                                        | 1.31x faster                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230501-pythonperf2-x86_64-python-main-3.12.0a7+-2d526cd |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| deltablue               | 7.54 ms                                                      | 3.24 ms: 2.33x faster                                        |
| asyncio_tcp             | 787 ms                                                       | 378 ms: 2.08x faster                                         |
| go                      | 264 ms                                                       | 148 ms: 1.78x faster                                         |
| logging_silent          | 165 ns                                                       | 93.8 ns: 1.75x faster                                        |
| scimark_lu              | 164 ms                                                       | 94.8 ms: 1.73x faster                                        |
| richards                | 73.9 ms                                                      | 43.7 ms: 1.69x faster                                        |
| sqlglot_parse           | 2.24 ms                                                      | 1.38 ms: 1.62x faster                                        |
| chaos                   | 108 ms                                                       | 66.9 ms: 1.61x faster                                        |
| scimark_sor             | 177 ms                                                       | 110 ms: 1.61x faster                                         |
| hexiom                  | 9.54 ms                                                      | 5.94 ms: 1.61x faster                                        |
| pyflate                 | 731 ms                                                       | 456 ms: 1.60x faster                                         |
| scimark_monte_carlo     | 109 ms                                                       | 68.2 ms: 1.59x faster                                        |
| raytrace                | 491 ms                                                       | 311 ms: 1.58x faster                                         |
| generators              | 57.0 ms                                                      | 36.3 ms: 1.57x faster                                        |
| spectral_norm           | 138 ms                                                       | 88.7 ms: 1.55x faster                                        |
| unpickle_pure_python    | 318 us                                                       | 208 us: 1.53x faster                                         |
| sqlglot_transpile       | 2.69 ms                                                      | 1.79 ms: 1.50x faster                                        |
| async_tree_io           | 1.61 sec                                                     | 1.09 sec: 1.49x faster                                       |
| nbody                   | 132 ms                                                       | 89.2 ms: 1.48x faster                                        |
| async_tree_memoization  | 822 ms                                                       | 560 ms: 1.47x faster                                         |
| fannkuch                | 496 ms                                                       | 338 ms: 1.47x faster                                         |
| async_tree_none         | 698 ms                                                       | 476 ms: 1.47x faster                                         |
| mako                    | 14.7 ms                                                      | 10.1 ms: 1.46x faster                                        |
| crypto_pyaes            | 119 ms                                                       | 81.3 ms: 1.46x faster                                        |
| pickle_pure_python      | 451 us                                                       | 319 us: 1.42x faster                                         |
| html5lib                | 96.3 ms                                                      | 68.0 ms: 1.42x faster                                        |
| float                   | 109 ms                                                       | 77.8 ms: 1.41x faster                                        |
| logging_simple          | 9.24 us                                                      | 6.60 us: 1.40x faster                                        |
| bench_mp_pool           | 7.10 ms                                                      | 5.21 ms: 1.36x faster                                        |
| thrift                  | 1.23 ms                                                      | 904 us: 1.36x faster                                         |
| coroutines              | 30.6 ms                                                      | 22.6 ms: 1.36x faster                                        |
| logging_format          | 9.94 us                                                      | 7.34 us: 1.35x faster                                        |
| async_tree_cpu_io_mixed | 951 ms                                                       | 709 ms: 1.34x faster                                         |
| pycparser               | 1.66 sec                                                     | 1.24 sec: 1.34x faster                                       |
| json_dumps              | 14.3 ms                                                      | 10.7 ms: 1.34x faster                                        |
| tornado_http            | 151 ms                                                       | 113 ms: 1.33x faster                                         |
| regex_compile           | 191 ms                                                       | 144 ms: 1.32x faster                                         |
| xml_etree_process       | 77.6 ms                                                      | 58.6 ms: 1.32x faster                                        |
| deepcopy_memo           | 49.2 us                                                      | 37.4 us: 1.31x faster                                        |
| pprint_pformat          | 2.12 sec                                                     | 1.65 sec: 1.29x faster                                       |
| genshi_text             | 31.7 ms                                                      | 24.6 ms: 1.29x faster                                        |
| pprint_safe_repr        | 1.03 sec                                                     | 802 ms: 1.28x faster                                         |
| nqueens                 | 114 ms                                                       | 89.2 ms: 1.27x faster                                        |
| dulwich_log             | 80.5 ms                                                      | 65.1 ms: 1.24x faster                                        |
| mypy2                   | 466 ms                                                       | 377 ms: 1.24x faster                                         |
| 2to3                    | 352 ms                                                       | 286 ms: 1.23x faster                                         |
| sqlglot_normalize       | 147 ms                                                       | 120 ms: 1.22x faster                                         |
| scimark_fft             | 359 ms                                                       | 294 ms: 1.22x faster                                         |
| deepcopy                | 457 us                                                       | 382 us: 1.20x faster                                         |
| json_loads              | 30.3 us                                                      | 25.4 us: 1.19x faster                                        |
| sqlglot_optimize        | 70.1 ms                                                      | 58.9 ms: 1.19x faster                                        |
| scimark_sparse_mat_mult | 5.09 ms                                                      | 4.29 ms: 1.19x faster                                        |
| genshi_xml              | 63.5 ms                                                      | 53.5 ms: 1.19x faster                                        |
| docutils                | 3.41 sec                                                     | 2.89 sec: 1.18x faster                                       |
| bench_thread_pool       | 1.14 ms                                                      | 976 us: 1.17x faster                                         |
| mdp                     | 2.95 sec                                                     | 2.54 sec: 1.16x faster                                       |
| deepcopy_reduce         | 3.91 us                                                      | 3.42 us: 1.14x faster                                        |
| json                    | 5.94 ms                                                      | 5.23 ms: 1.14x faster                                        |
| regex_dna               | 261 ms                                                       | 230 ms: 1.13x faster                                         |
| sqlite_synth            | 2.96 us                                                      | 2.61 us: 1.13x faster                                        |
| pathlib                 | 21.3 ms                                                      | 18.8 ms: 1.13x faster                                        |
| comprehensions          | 27.3 us                                                      | 24.5 us: 1.11x faster                                        |
| regex_v8                | 26.0 ms                                                      | 23.5 ms: 1.11x faster                                        |
| xml_etree_parse         | 160 ms                                                       | 146 ms: 1.10x faster                                         |
| async_generators        | 419 ms                                                       | 382 ms: 1.10x faster                                         |
| create_gc_cycles        | 1.80 ms                                                      | 1.65 ms: 1.09x faster                                        |
| xml_etree_generate      | 94.1 ms                                                      | 86.2 ms: 1.09x faster                                        |
| unpack_sequence         | 59.7 ns                                                      | 55.5 ns: 1.08x faster                                        |
| xml_etree_iterparse     | 109 ms                                                       | 104 ms: 1.05x faster                                         |
| pidigits                | 271 ms                                                       | 259 ms: 1.04x faster                                         |
| python_startup          | 11.5 ms                                                      | 11.1 ms: 1.03x faster                                        |
| pickle                  | 10.1 us                                                      | 9.94 us: 1.02x faster                                        |
| meteor_contest          | 142 ms                                                       | 139 ms: 1.02x faster                                         |
| telco                   | 7.14 ms                                                      | 7.22 ms: 1.01x slower                                        |
| unpickle_list           | 4.73 us                                                      | 4.83 us: 1.02x slower                                        |
| gc_traversal            | 3.46 ms                                                      | 3.59 ms: 1.04x slower                                        |
| pickle_list             | 4.11 us                                                      | 4.41 us: 1.07x slower                                        |
| pickle_dict             | 29.5 us                                                      | 31.8 us: 1.08x slower                                        |
| unpickle                | 13.3 us                                                      | 14.6 us: 1.10x slower                                        |
| python_startup_no_site  | 7.32 ms                                                      | 8.33 ms: 1.14x slower                                        |
| regex_effbot            | 2.99 ms                                                      | 3.46 ms: 1.16x slower                                        |
| dask                    | 478 ms                                                       | 560 ms: 1.17x slower                                         |
| coverage                | 71.1 ms                                                      | 92.8 ms: 1.31x slower                                        |
| Geometric mean          | (ref)                                                        | 1.27x faster                                                 |
Ignored benchmarks (12) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum
