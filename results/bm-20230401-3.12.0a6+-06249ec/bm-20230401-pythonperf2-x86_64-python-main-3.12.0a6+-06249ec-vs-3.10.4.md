
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 06249ec
- commit date: 2023-04-01
- overall geometric mean: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-pythonperf2-x86_64-python-main-3.12.0a6+-06249ec |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 352 ms                                                       | 288 ms: 1.22x faster                                         |
| chameleon      | 9.62 ms                                                      | 7.16 ms: 1.34x faster                                        |
| docutils       | 3.41 sec                                                     | 2.82 sec: 1.21x faster                                       |
| html5lib       | 96.3 ms                                                      | 70.9 ms: 1.36x faster                                        |
| tornado_http   | 151 ms                                                       | 113 ms: 1.33x faster                                         |
| Geometric mean | (ref)                                                        | 1.29x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-pythonperf2-x86_64-python-main-3.12.0a6+-06249ec |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 132 ms                                                       | 86.8 ms: 1.52x faster                                        |
| float          | 109 ms                                                       | 73.7 ms: 1.48x faster                                        |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                         |
| Geometric mean | (ref)                                                        | 1.33x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-pythonperf2-x86_64-python-main-3.12.0a6+-06249ec |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 191 ms                                                       | 150 ms: 1.27x faster                                         |
| regex_dna      | 261 ms                                                       | 231 ms: 1.13x faster                                         |
| regex_v8       | 26.0 ms                                                      | 23.4 ms: 1.11x faster                                        |
| regex_effbot   | 2.99 ms                                                      | 3.38 ms: 1.13x slower                                        |
| Geometric mean | (ref)                                                        | 1.09x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-pythonperf2-x86_64-python-main-3.12.0a6+-06249ec |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle_pure_python | 318 us                                                       | 215 us: 1.48x faster                                         |
| pickle_pure_python   | 451 us                                                       | 319 us: 1.42x faster                                         |
| json_dumps           | 14.3 ms                                                      | 10.4 ms: 1.37x faster                                        |
| xml_etree_process    | 77.6 ms                                                      | 60.0 ms: 1.29x faster                                        |
| json_loads           | 30.3 us                                                      | 23.9 us: 1.27x faster                                        |
| xml_etree_parse      | 160 ms                                                       | 143 ms: 1.12x faster                                         |
| xml_etree_generate   | 94.1 ms                                                      | 86.2 ms: 1.09x faster                                        |
| xml_etree_iterparse  | 109 ms                                                       | 103 ms: 1.06x faster                                         |
| pickle_list          | 4.11 us                                                      | 3.90 us: 1.05x faster                                        |
| unpickle_list        | 4.73 us                                                      | 4.51 us: 1.05x faster                                        |
| unpickle             | 13.3 us                                                      | 13.0 us: 1.02x faster                                        |
| pickle               | 10.1 us                                                      | 10.3 us: 1.01x slower                                        |
| pickle_dict          | 29.5 us                                                      | 31.5 us: 1.07x slower                                        |
| Geometric mean       | (ref)                                                        | 1.15x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-pythonperf2-x86_64-python-main-3.12.0a6+-06249ec |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.0 ms: 1.04x faster                                        |
| python_startup_no_site | 7.32 ms                                                      | 8.31 ms: 1.13x slower                                        |
| Geometric mean         | (ref)                                                        | 1.05x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-pythonperf2-x86_64-python-main-3.12.0a6+-06249ec |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.1 ms: 1.46x faster                                        |
| django_template | 52.0 ms                                                      | 39.9 ms: 1.30x faster                                        |
| genshi_text     | 31.7 ms                                                      | 26.4 ms: 1.20x faster                                        |
| genshi_xml      | 63.5 ms                                                      | 56.5 ms: 1.12x faster                                        |
| Geometric mean  | (ref)                                                        | 1.27x faster                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-pythonperf2-x86_64-python-main-3.12.0a6+-06249ec |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| deltablue               | 7.54 ms                                                      | 3.63 ms: 2.08x faster                                        |
| asyncio_tcp             | 787 ms                                                       | 385 ms: 2.04x faster                                         |
| logging_silent          | 165 ns                                                       | 94.8 ns: 1.74x faster                                        |
| raytrace                | 491 ms                                                       | 296 ms: 1.66x faster                                         |
| scimark_lu              | 164 ms                                                       | 101 ms: 1.63x faster                                         |
| scimark_monte_carlo     | 109 ms                                                       | 67.5 ms: 1.61x faster                                        |
| pyflate                 | 731 ms                                                       | 459 ms: 1.59x faster                                         |
| scimark_sor             | 177 ms                                                       | 114 ms: 1.55x faster                                         |
| bench_mp_pool           | 7.10 ms                                                      | 4.65 ms: 1.53x faster                                        |
| go                      | 264 ms                                                       | 173 ms: 1.53x faster                                         |
| nbody                   | 132 ms                                                       | 86.8 ms: 1.52x faster                                        |
| chaos                   | 108 ms                                                       | 71.4 ms: 1.51x faster                                        |
| richards                | 73.9 ms                                                      | 49.1 ms: 1.50x faster                                        |
| float                   | 109 ms                                                       | 73.7 ms: 1.48x faster                                        |
| unpickle_pure_python    | 318 us                                                       | 215 us: 1.48x faster                                         |
| generators              | 57.0 ms                                                      | 38.7 ms: 1.47x faster                                        |
| spectral_norm           | 138 ms                                                       | 94.1 ms: 1.47x faster                                        |
| mako                    | 14.7 ms                                                      | 10.1 ms: 1.46x faster                                        |
| crypto_pyaes            | 119 ms                                                       | 83.5 ms: 1.42x faster                                        |
| pickle_pure_python      | 451 us                                                       | 319 us: 1.42x faster                                         |
| hexiom                  | 9.54 ms                                                      | 6.77 ms: 1.41x faster                                        |
| sqlglot_parse           | 2.24 ms                                                      | 1.60 ms: 1.40x faster                                        |
| async_tree_io           | 1.61 sec                                                     | 1.17 sec: 1.38x faster                                       |
| sqlglot_transpile       | 2.69 ms                                                      | 1.96 ms: 1.37x faster                                        |
| json_dumps              | 14.3 ms                                                      | 10.4 ms: 1.37x faster                                        |
| scimark_fft             | 359 ms                                                       | 264 ms: 1.36x faster                                         |
| deepcopy_memo           | 49.2 us                                                      | 36.2 us: 1.36x faster                                        |
| html5lib                | 96.3 ms                                                      | 70.9 ms: 1.36x faster                                        |
| unpack_sequence         | 59.7 ns                                                      | 44.0 ns: 1.36x faster                                        |
| async_tree_none         | 698 ms                                                       | 516 ms: 1.35x faster                                         |
| pprint_pformat          | 2.12 sec                                                     | 1.57 sec: 1.35x faster                                       |
| scimark_sparse_mat_mult | 5.09 ms                                                      | 3.78 ms: 1.35x faster                                        |
| chameleon               | 9.62 ms                                                      | 7.16 ms: 1.34x faster                                        |
| async_tree_memoization  | 822 ms                                                       | 614 ms: 1.34x faster                                         |
| pprint_safe_repr        | 1.03 sec                                                     | 771 ms: 1.33x faster                                         |
| tornado_http            | 151 ms                                                       | 113 ms: 1.33x faster                                         |
| pycparser               | 1.66 sec                                                     | 1.26 sec: 1.32x faster                                       |
| logging_simple          | 9.24 us                                                      | 7.03 us: 1.31x faster                                        |
| django_template         | 52.0 ms                                                      | 39.9 ms: 1.30x faster                                        |
| thrift                  | 1.23 ms                                                      | 942 us: 1.30x faster                                         |
| xml_etree_process       | 77.6 ms                                                      | 60.0 ms: 1.29x faster                                        |
| regex_compile           | 191 ms                                                       | 150 ms: 1.27x faster                                         |
| json_loads              | 30.3 us                                                      | 23.9 us: 1.27x faster                                        |
| async_tree_cpu_io_mixed | 951 ms                                                       | 756 ms: 1.26x faster                                         |
| logging_format          | 9.94 us                                                      | 8.05 us: 1.23x faster                                        |
| 2to3                    | 352 ms                                                       | 288 ms: 1.22x faster                                         |
| sqlglot_normalize       | 147 ms                                                       | 121 ms: 1.21x faster                                         |
| dulwich_log             | 80.5 ms                                                      | 66.4 ms: 1.21x faster                                        |
| docutils                | 3.41 sec                                                     | 2.82 sec: 1.21x faster                                       |
| mypy2                   | 466 ms                                                       | 386 ms: 1.21x faster                                         |
| genshi_text             | 31.7 ms                                                      | 26.4 ms: 1.20x faster                                        |
| sqlglot_optimize        | 70.1 ms                                                      | 58.8 ms: 1.19x faster                                        |
| json                    | 5.94 ms                                                      | 5.05 ms: 1.18x faster                                        |
| coroutines              | 30.6 ms                                                      | 26.2 ms: 1.17x faster                                        |
| bench_thread_pool       | 1.14 ms                                                      | 987 us: 1.15x faster                                         |
| mdp                     | 2.95 sec                                                     | 2.57 sec: 1.15x faster                                       |
| deepcopy                | 457 us                                                       | 398 us: 1.15x faster                                         |
| sqlite_synth            | 2.96 us                                                      | 2.62 us: 1.13x faster                                        |
| regex_dna               | 261 ms                                                       | 231 ms: 1.13x faster                                         |
| genshi_xml              | 63.5 ms                                                      | 56.5 ms: 1.12x faster                                        |
| deepcopy_reduce         | 3.91 us                                                      | 3.50 us: 1.12x faster                                        |
| xml_etree_parse         | 160 ms                                                       | 143 ms: 1.12x faster                                         |
| fannkuch                | 496 ms                                                       | 445 ms: 1.11x faster                                         |
| sympy_expand            | 603 ms                                                       | 541 ms: 1.11x faster                                         |
| regex_v8                | 26.0 ms                                                      | 23.4 ms: 1.11x faster                                        |
| meteor_contest          | 142 ms                                                       | 128 ms: 1.10x faster                                         |
| sympy_integrate         | 28.1 ms                                                      | 25.6 ms: 1.10x faster                                        |
| xml_etree_generate      | 94.1 ms                                                      | 86.2 ms: 1.09x faster                                        |
| pathlib                 | 21.3 ms                                                      | 19.7 ms: 1.08x faster                                        |
| create_gc_cycles        | 1.80 ms                                                      | 1.68 ms: 1.07x faster                                        |
| async_generators        | 419 ms                                                       | 391 ms: 1.07x faster                                         |
| nqueens                 | 114 ms                                                       | 106 ms: 1.07x faster                                         |
| sympy_str               | 358 ms                                                       | 334 ms: 1.07x faster                                         |
| xml_etree_iterparse     | 109 ms                                                       | 103 ms: 1.06x faster                                         |
| pickle_list             | 4.11 us                                                      | 3.90 us: 1.05x faster                                        |
| unpickle_list           | 4.73 us                                                      | 4.51 us: 1.05x faster                                        |
| pidigits                | 271 ms                                                       | 260 ms: 1.04x faster                                         |
| python_startup          | 11.5 ms                                                      | 11.0 ms: 1.04x faster                                        |
| telco                   | 7.14 ms                                                      | 6.93 ms: 1.03x faster                                        |
| sympy_sum               | 193 ms                                                       | 188 ms: 1.03x faster                                         |
| unpickle                | 13.3 us                                                      | 13.0 us: 1.02x faster                                        |
| pickle                  | 10.1 us                                                      | 10.3 us: 1.01x slower                                        |
| comprehensions          | 27.3 us                                                      | 27.7 us: 1.02x slower                                        |
| pickle_dict             | 29.5 us                                                      | 31.5 us: 1.07x slower                                        |
| regex_effbot            | 2.99 ms                                                      | 3.38 ms: 1.13x slower                                        |
| python_startup_no_site  | 7.32 ms                                                      | 8.31 ms: 1.13x slower                                        |
| gc_traversal            | 3.46 ms                                                      | 4.04 ms: 1.17x slower                                        |
| coverage                | 71.1 ms                                                      | 84.4 ms: 1.19x slower                                        |
| dask                    | 478 ms                                                       | 577 ms: 1.21x slower                                         |
| Geometric mean          | (ref)                                                        | 1.24x faster                                                 |
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative
