
# Results vs. 3.10.4

- fork: python
- ref: edfbf56f4ca6588dfd20
- machine: linux-x86_64
- commit hash: edfbf56
- commit date: 2023-01-01
- overall geometric mean: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230101-pythonperf2-x86_64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 352 ms                                                       | 284 ms: 1.24x faster                                                         |
| chameleon      | 9.62 ms                                                      | 7.29 ms: 1.32x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.76 sec: 1.24x faster                                                       |
| html5lib       | 96.3 ms                                                      | 66.2 ms: 1.45x faster                                                        |
| Geometric mean | (ref)                                                        | 1.31x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230101-pythonperf2-x86_64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 109 ms                                                       | 72.5 ms: 1.51x faster                                                        |
| nbody          | 132 ms                                                       | 90.4 ms: 1.46x faster                                                        |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                         |
| Geometric mean | (ref)                                                        | 1.33x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230101-pythonperf2-x86_64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 191 ms                                                       | 149 ms: 1.28x faster                                                         |
| regex_dna      | 261 ms                                                       | 229 ms: 1.14x faster                                                         |
| regex_v8       | 26.0 ms                                                      | 22.9 ms: 1.14x faster                                                        |
| regex_effbot   | 2.99 ms                                                      | 3.40 ms: 1.14x slower                                                        |
| Geometric mean | (ref)                                                        | 1.10x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230101-pythonperf2-x86_64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 318 us                                                       | 210 us: 1.52x faster                                                         |
| pickle_pure_python   | 451 us                                                       | 313 us: 1.44x faster                                                         |
| xml_etree_process    | 77.6 ms                                                      | 54.1 ms: 1.43x faster                                                        |
| json_dumps           | 14.3 ms                                                      | 10.2 ms: 1.40x faster                                                        |
| json_loads           | 30.3 us                                                      | 24.1 us: 1.26x faster                                                        |
| xml_etree_generate   | 94.1 ms                                                      | 78.0 ms: 1.21x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 141 ms: 1.13x faster                                                         |
| pickle_list          | 4.11 us                                                      | 3.83 us: 1.07x faster                                                        |
| unpickle_list        | 4.73 us                                                      | 4.43 us: 1.07x faster                                                        |
| xml_etree_iterparse  | 109 ms                                                       | 104 ms: 1.05x faster                                                         |
| unpickle             | 13.3 us                                                      | 12.9 us: 1.03x faster                                                        |
| pickle               | 10.1 us                                                      | 9.84 us: 1.03x faster                                                        |
| pickle_dict          | 29.5 us                                                      | 31.7 us: 1.07x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.18x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230101-pythonperf2-x86_64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 10.7 ms: 1.07x faster                                                        |
| python_startup_no_site | 7.32 ms                                                      | 7.83 ms: 1.07x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.00x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230101-pythonperf2-x86_64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.1 ms: 1.46x faster                                                        |
| django_template | 52.0 ms                                                      | 39.5 ms: 1.32x faster                                                        |
| genshi_text     | 31.7 ms                                                      | 25.1 ms: 1.26x faster                                                        |
| genshi_xml      | 63.5 ms                                                      | 53.9 ms: 1.18x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.30x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230101-pythonperf2-x86_64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deltablue               | 7.54 ms                                                      | 3.64 ms: 2.07x faster                                                        |
| asyncio_tcp             | 787 ms                                                       | 391 ms: 2.01x faster                                                         |
| pyflate                 | 731 ms                                                       | 429 ms: 1.70x faster                                                         |
| go                      | 264 ms                                                       | 159 ms: 1.66x faster                                                         |
| scimark_sor             | 177 ms                                                       | 107 ms: 1.65x faster                                                         |
| scimark_monte_carlo     | 109 ms                                                       | 66.1 ms: 1.64x faster                                                        |
| raytrace                | 491 ms                                                       | 300 ms: 1.64x faster                                                         |
| scimark_lu              | 164 ms                                                       | 100 ms: 1.64x faster                                                         |
| logging_silent          | 165 ns                                                       | 101 ns: 1.63x faster                                                         |
| richards                | 73.9 ms                                                      | 46.3 ms: 1.60x faster                                                        |
| unpickle_pure_python    | 318 us                                                       | 210 us: 1.52x faster                                                         |
| float                   | 109 ms                                                       | 72.5 ms: 1.51x faster                                                        |
| bench_mp_pool           | 7.10 ms                                                      | 4.74 ms: 1.50x faster                                                        |
| chaos                   | 108 ms                                                       | 72.8 ms: 1.48x faster                                                        |
| crypto_pyaes            | 119 ms                                                       | 80.5 ms: 1.47x faster                                                        |
| spectral_norm           | 138 ms                                                       | 94.2 ms: 1.46x faster                                                        |
| nbody                   | 132 ms                                                       | 90.4 ms: 1.46x faster                                                        |
| mako                    | 14.7 ms                                                      | 10.1 ms: 1.46x faster                                                        |
| html5lib                | 96.3 ms                                                      | 66.2 ms: 1.45x faster                                                        |
| pickle_pure_python      | 451 us                                                       | 313 us: 1.44x faster                                                         |
| xml_etree_process       | 77.6 ms                                                      | 54.1 ms: 1.43x faster                                                        |
| sqlglot_parse           | 2.24 ms                                                      | 1.57 ms: 1.43x faster                                                        |
| json_dumps              | 14.3 ms                                                      | 10.2 ms: 1.40x faster                                                        |
| scimark_sparse_mat_mult | 5.09 ms                                                      | 3.66 ms: 1.39x faster                                                        |
| sqlglot_transpile       | 2.69 ms                                                      | 1.93 ms: 1.39x faster                                                        |
| async_tree_io           | 1.61 sec                                                     | 1.16 sec: 1.39x faster                                                       |
| hexiom                  | 9.54 ms                                                      | 6.86 ms: 1.39x faster                                                        |
| thrift                  | 1.23 ms                                                      | 885 us: 1.39x faster                                                         |
| deepcopy_memo           | 49.2 us                                                      | 35.7 us: 1.38x faster                                                        |
| async_tree_none         | 698 ms                                                       | 510 ms: 1.37x faster                                                         |
| pprint_pformat          | 2.12 sec                                                     | 1.56 sec: 1.36x faster                                                       |
| pprint_safe_repr        | 1.03 sec                                                     | 758 ms: 1.35x faster                                                         |
| unpack_sequence         | 59.7 ns                                                      | 44.5 ns: 1.34x faster                                                        |
| async_tree_memoization  | 822 ms                                                       | 613 ms: 1.34x faster                                                         |
| logging_simple          | 9.24 us                                                      | 6.98 us: 1.32x faster                                                        |
| chameleon               | 9.62 ms                                                      | 7.29 ms: 1.32x faster                                                        |
| django_template         | 52.0 ms                                                      | 39.5 ms: 1.32x faster                                                        |
| scimark_fft             | 359 ms                                                       | 275 ms: 1.30x faster                                                         |
| pycparser               | 1.66 sec                                                     | 1.28 sec: 1.30x faster                                                       |
| async_generators        | 419 ms                                                       | 326 ms: 1.29x faster                                                         |
| regex_compile           | 191 ms                                                       | 149 ms: 1.28x faster                                                         |
| async_tree_cpu_io_mixed | 951 ms                                                       | 747 ms: 1.27x faster                                                         |
| logging_format          | 9.94 us                                                      | 7.80 us: 1.27x faster                                                        |
| fannkuch                | 496 ms                                                       | 392 ms: 1.27x faster                                                         |
| genshi_text             | 31.7 ms                                                      | 25.1 ms: 1.26x faster                                                        |
| json_loads              | 30.3 us                                                      | 24.1 us: 1.26x faster                                                        |
| 2to3                    | 352 ms                                                       | 284 ms: 1.24x faster                                                         |
| sqlglot_normalize       | 147 ms                                                       | 119 ms: 1.24x faster                                                         |
| dulwich_log             | 80.5 ms                                                      | 65.1 ms: 1.24x faster                                                        |
| docutils                | 3.41 sec                                                     | 2.76 sec: 1.24x faster                                                       |
| mypy2                   | 466 ms                                                       | 378 ms: 1.23x faster                                                         |
| sqlglot_optimize        | 70.1 ms                                                      | 57.5 ms: 1.22x faster                                                        |
| xml_etree_generate      | 94.1 ms                                                      | 78.0 ms: 1.21x faster                                                        |
| nqueens                 | 114 ms                                                       | 94.4 ms: 1.20x faster                                                        |
| deepcopy                | 457 us                                                       | 380 us: 1.20x faster                                                         |
| deepcopy_reduce         | 3.91 us                                                      | 3.32 us: 1.18x faster                                                        |
| genshi_xml              | 63.5 ms                                                      | 53.9 ms: 1.18x faster                                                        |
| bench_thread_pool       | 1.14 ms                                                      | 971 us: 1.17x faster                                                         |
| json                    | 5.94 ms                                                      | 5.08 ms: 1.17x faster                                                        |
| dask                    | 478 ms                                                       | 413 ms: 1.16x faster                                                         |
| sqlite_synth            | 2.96 us                                                      | 2.57 us: 1.15x faster                                                        |
| regex_dna               | 261 ms                                                       | 229 ms: 1.14x faster                                                         |
| create_gc_cycles        | 1.80 ms                                                      | 1.58 ms: 1.14x faster                                                        |
| regex_v8                | 26.0 ms                                                      | 22.9 ms: 1.14x faster                                                        |
| xml_etree_parse         | 160 ms                                                       | 141 ms: 1.13x faster                                                         |
| sympy_expand            | 603 ms                                                       | 533 ms: 1.13x faster                                                         |
| coroutines              | 30.6 ms                                                      | 27.2 ms: 1.13x faster                                                        |
| sympy_integrate         | 28.1 ms                                                      | 25.3 ms: 1.11x faster                                                        |
| pathlib                 | 21.3 ms                                                      | 19.2 ms: 1.11x faster                                                        |
| meteor_contest          | 142 ms                                                       | 129 ms: 1.10x faster                                                         |
| sympy_str               | 358 ms                                                       | 330 ms: 1.08x faster                                                         |
| pidigits                | 271 ms                                                       | 251 ms: 1.08x faster                                                         |
| pickle_list             | 4.11 us                                                      | 3.83 us: 1.07x faster                                                        |
| python_startup          | 11.5 ms                                                      | 10.7 ms: 1.07x faster                                                        |
| unpickle_list           | 4.73 us                                                      | 4.43 us: 1.07x faster                                                        |
| telco                   | 7.14 ms                                                      | 6.76 ms: 1.06x faster                                                        |
| sympy_sum               | 193 ms                                                       | 183 ms: 1.05x faster                                                         |
| xml_etree_iterparse     | 109 ms                                                       | 104 ms: 1.05x faster                                                         |
| mdp                     | 2.95 sec                                                     | 2.83 sec: 1.04x faster                                                       |
| unpickle                | 13.3 us                                                      | 12.9 us: 1.03x faster                                                        |
| pickle                  | 10.1 us                                                      | 9.84 us: 1.03x faster                                                        |
| generators              | 57.0 ms                                                      | 59.9 ms: 1.05x slower                                                        |
| python_startup_no_site  | 7.32 ms                                                      | 7.83 ms: 1.07x slower                                                        |
| pickle_dict             | 29.5 us                                                      | 31.7 us: 1.07x slower                                                        |
| gc_traversal            | 3.46 ms                                                      | 3.78 ms: 1.09x slower                                                        |
| regex_effbot            | 2.99 ms                                                      | 3.40 ms: 1.14x slower                                                        |
| coverage                | 71.1 ms                                                      | 93.0 ms: 1.31x slower                                                        |
| Geometric mean          | (ref)                                                        | 1.26x faster                                                                 |

Benchmark hidden because not significant (1): comprehensions
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
