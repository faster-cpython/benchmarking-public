
# Results vs. 3.10.4

- fork: JelleZijlstra
- ref: tvobject
- machine: linux-x86_64
- commit hash: 827b9e5
- commit date: 2023-05-02
- overall geometric mean: 1.27x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230502-pythonperf2-x86_64-JelleZijlstra-tvobject-3.12.0a7+-827b9e5 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 352 ms                                                       | 284 ms: 1.24x faster                                                    |
| docutils       | 3.41 sec                                                     | 2.88 sec: 1.18x faster                                                  |
| html5lib       | 96.3 ms                                                      | 69.2 ms: 1.39x faster                                                   |
| tornado_http   | 151 ms                                                       | 113 ms: 1.33x faster                                                    |
| Geometric mean | (ref)                                                        | 1.28x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230502-pythonperf2-x86_64-JelleZijlstra-tvobject-3.12.0a7+-827b9e5 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 132 ms                                                       | 87.7 ms: 1.51x faster                                                   |
| float          | 109 ms                                                       | 78.0 ms: 1.40x faster                                                   |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                                    |
| Geometric mean | (ref)                                                        | 1.30x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230502-pythonperf2-x86_64-JelleZijlstra-tvobject-3.12.0a7+-827b9e5 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 191 ms                                                       | 144 ms: 1.33x faster                                                    |
| regex_dna      | 261 ms                                                       | 234 ms: 1.12x faster                                                    |
| regex_v8       | 26.0 ms                                                      | 23.4 ms: 1.11x faster                                                   |
| regex_effbot   | 2.99 ms                                                      | 3.50 ms: 1.17x slower                                                   |
| Geometric mean | (ref)                                                        | 1.09x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230502-pythonperf2-x86_64-JelleZijlstra-tvobject-3.12.0a7+-827b9e5 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 318 us                                                       | 204 us: 1.56x faster                                                    |
| pickle_pure_python   | 451 us                                                       | 320 us: 1.41x faster                                                    |
| json_dumps           | 14.3 ms                                                      | 10.5 ms: 1.36x faster                                                   |
| xml_etree_process    | 77.6 ms                                                      | 58.5 ms: 1.33x faster                                                   |
| json_loads           | 30.3 us                                                      | 25.1 us: 1.21x faster                                                   |
| xml_etree_parse      | 160 ms                                                       | 145 ms: 1.10x faster                                                    |
| xml_etree_generate   | 94.1 ms                                                      | 86.0 ms: 1.09x faster                                                   |
| xml_etree_iterparse  | 109 ms                                                       | 104 ms: 1.05x faster                                                    |
| pickle               | 10.1 us                                                      | 10.0 us: 1.01x faster                                                   |
| unpickle_list        | 4.73 us                                                      | 4.83 us: 1.02x slower                                                   |
| pickle_list          | 4.11 us                                                      | 4.28 us: 1.04x slower                                                   |
| unpickle             | 13.3 us                                                      | 14.3 us: 1.08x slower                                                   |
| pickle_dict          | 29.5 us                                                      | 31.9 us: 1.08x slower                                                   |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230502-pythonperf2-x86_64-JelleZijlstra-tvobject-3.12.0a7+-827b9e5 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.3 ms: 1.02x faster                                                   |
| python_startup_no_site | 7.32 ms                                                      | 8.47 ms: 1.16x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230502-pythonperf2-x86_64-JelleZijlstra-tvobject-3.12.0a7+-827b9e5 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 14.7 ms                                                      | 10.1 ms: 1.46x faster                                                   |
| genshi_text    | 31.7 ms                                                      | 24.3 ms: 1.30x faster                                                   |
| genshi_xml     | 63.5 ms                                                      | 53.5 ms: 1.19x faster                                                   |
| Geometric mean | (ref)                                                        | 1.31x faster                                                            |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230502-pythonperf2-x86_64-JelleZijlstra-tvobject-3.12.0a7+-827b9e5 |
|-------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deltablue               | 7.54 ms                                                      | 3.25 ms: 2.32x faster                                                   |
| asyncio_tcp             | 787 ms                                                       | 381 ms: 2.07x faster                                                    |
| go                      | 264 ms                                                       | 147 ms: 1.80x faster                                                    |
| logging_silent          | 165 ns                                                       | 94.7 ns: 1.74x faster                                                   |
| richards                | 73.9 ms                                                      | 42.7 ms: 1.73x faster                                                   |
| scimark_lu              | 164 ms                                                       | 96.2 ms: 1.71x faster                                                   |
| pyflate                 | 731 ms                                                       | 439 ms: 1.66x faster                                                    |
| raytrace                | 491 ms                                                       | 300 ms: 1.64x faster                                                    |
| chaos                   | 108 ms                                                       | 66.2 ms: 1.63x faster                                                   |
| sqlglot_parse           | 2.24 ms                                                      | 1.38 ms: 1.63x faster                                                   |
| scimark_sor             | 177 ms                                                       | 110 ms: 1.62x faster                                                    |
| hexiom                  | 9.54 ms                                                      | 5.91 ms: 1.61x faster                                                   |
| generators              | 57.0 ms                                                      | 35.9 ms: 1.59x faster                                                   |
| unpickle_pure_python    | 318 us                                                       | 204 us: 1.56x faster                                                    |
| spectral_norm           | 138 ms                                                       | 88.9 ms: 1.55x faster                                                   |
| scimark_monte_carlo     | 109 ms                                                       | 70.8 ms: 1.54x faster                                                   |
| nbody                   | 132 ms                                                       | 87.7 ms: 1.51x faster                                                   |
| sqlglot_transpile       | 2.69 ms                                                      | 1.79 ms: 1.50x faster                                                   |
| crypto_pyaes            | 119 ms                                                       | 80.3 ms: 1.48x faster                                                   |
| async_tree_io           | 1.61 sec                                                     | 1.10 sec: 1.47x faster                                                  |
| async_tree_none         | 698 ms                                                       | 478 ms: 1.46x faster                                                    |
| mako                    | 14.7 ms                                                      | 10.1 ms: 1.46x faster                                                   |
| fannkuch                | 496 ms                                                       | 346 ms: 1.44x faster                                                    |
| async_tree_memoization  | 822 ms                                                       | 575 ms: 1.43x faster                                                    |
| logging_simple          | 9.24 us                                                      | 6.53 us: 1.41x faster                                                   |
| pickle_pure_python      | 451 us                                                       | 320 us: 1.41x faster                                                    |
| float                   | 109 ms                                                       | 78.0 ms: 1.40x faster                                                   |
| html5lib                | 96.3 ms                                                      | 69.2 ms: 1.39x faster                                                   |
| thrift                  | 1.23 ms                                                      | 896 us: 1.37x faster                                                    |
| json_dumps              | 14.3 ms                                                      | 10.5 ms: 1.36x faster                                                   |
| coroutines              | 30.6 ms                                                      | 22.5 ms: 1.36x faster                                                   |
| pycparser               | 1.66 sec                                                     | 1.22 sec: 1.36x faster                                                  |
| logging_format          | 9.94 us                                                      | 7.34 us: 1.35x faster                                                   |
| regex_compile           | 191 ms                                                       | 144 ms: 1.33x faster                                                    |
| deepcopy_memo           | 49.2 us                                                      | 37.0 us: 1.33x faster                                                   |
| async_tree_cpu_io_mixed | 951 ms                                                       | 716 ms: 1.33x faster                                                    |
| tornado_http            | 151 ms                                                       | 113 ms: 1.33x faster                                                    |
| xml_etree_process       | 77.6 ms                                                      | 58.5 ms: 1.33x faster                                                   |
| genshi_text             | 31.7 ms                                                      | 24.3 ms: 1.30x faster                                                   |
| pprint_pformat          | 2.12 sec                                                     | 1.64 sec: 1.29x faster                                                  |
| bench_mp_pool           | 7.10 ms                                                      | 5.54 ms: 1.28x faster                                                   |
| nqueens                 | 114 ms                                                       | 88.9 ms: 1.28x faster                                                   |
| pprint_safe_repr        | 1.03 sec                                                     | 806 ms: 1.27x faster                                                    |
| dulwich_log             | 80.5 ms                                                      | 63.5 ms: 1.27x faster                                                   |
| unpack_sequence         | 59.7 ns                                                      | 47.6 ns: 1.25x faster                                                   |
| mypy2                   | 466 ms                                                       | 376 ms: 1.24x faster                                                    |
| 2to3                    | 352 ms                                                       | 284 ms: 1.24x faster                                                    |
| sqlglot_normalize       | 147 ms                                                       | 119 ms: 1.24x faster                                                    |
| scimark_fft             | 359 ms                                                       | 291 ms: 1.24x faster                                                    |
| json_loads              | 30.3 us                                                      | 25.1 us: 1.21x faster                                                   |
| sqlglot_optimize        | 70.1 ms                                                      | 58.7 ms: 1.19x faster                                                   |
| bench_thread_pool       | 1.14 ms                                                      | 955 us: 1.19x faster                                                    |
| genshi_xml              | 63.5 ms                                                      | 53.5 ms: 1.19x faster                                                   |
| deepcopy                | 457 us                                                       | 386 us: 1.18x faster                                                    |
| docutils                | 3.41 sec                                                     | 2.88 sec: 1.18x faster                                                  |
| scimark_sparse_mat_mult | 5.09 ms                                                      | 4.37 ms: 1.17x faster                                                   |
| mdp                     | 2.95 sec                                                     | 2.54 sec: 1.16x faster                                                  |
| json                    | 5.94 ms                                                      | 5.12 ms: 1.16x faster                                                   |
| deepcopy_reduce         | 3.91 us                                                      | 3.44 us: 1.14x faster                                                   |
| comprehensions          | 27.3 us                                                      | 24.3 us: 1.12x faster                                                   |
| sqlite_synth            | 2.96 us                                                      | 2.65 us: 1.12x faster                                                   |
| regex_dna               | 261 ms                                                       | 234 ms: 1.12x faster                                                    |
| regex_v8                | 26.0 ms                                                      | 23.4 ms: 1.11x faster                                                   |
| xml_etree_parse         | 160 ms                                                       | 145 ms: 1.10x faster                                                    |
| xml_etree_generate      | 94.1 ms                                                      | 86.0 ms: 1.09x faster                                                   |
| async_generators        | 419 ms                                                       | 384 ms: 1.09x faster                                                    |
| pathlib                 | 21.3 ms                                                      | 19.7 ms: 1.08x faster                                                   |
| create_gc_cycles        | 1.80 ms                                                      | 1.71 ms: 1.06x faster                                                   |
| xml_etree_iterparse     | 109 ms                                                       | 104 ms: 1.05x faster                                                    |
| pidigits                | 271 ms                                                       | 260 ms: 1.04x faster                                                    |
| meteor_contest          | 142 ms                                                       | 137 ms: 1.03x faster                                                    |
| python_startup          | 11.5 ms                                                      | 11.3 ms: 1.02x faster                                                   |
| pickle                  | 10.1 us                                                      | 10.0 us: 1.01x faster                                                   |
| telco                   | 7.14 ms                                                      | 7.19 ms: 1.01x slower                                                   |
| unpickle_list           | 4.73 us                                                      | 4.83 us: 1.02x slower                                                   |
| pickle_list             | 4.11 us                                                      | 4.28 us: 1.04x slower                                                   |
| unpickle                | 13.3 us                                                      | 14.3 us: 1.08x slower                                                   |
| pickle_dict             | 29.5 us                                                      | 31.9 us: 1.08x slower                                                   |
| python_startup_no_site  | 7.32 ms                                                      | 8.47 ms: 1.16x slower                                                   |
| gc_traversal            | 3.46 ms                                                      | 4.02 ms: 1.16x slower                                                   |
| regex_effbot            | 2.99 ms                                                      | 3.50 ms: 1.17x slower                                                   |
| dask                    | 478 ms                                                       | 560 ms: 1.17x slower                                                    |
| coverage                | 71.1 ms                                                      | 96.0 ms: 1.35x slower                                                   |
| Geometric mean          | (ref)                                                        | 1.27x faster                                                            |
Ignored benchmarks (12) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum
