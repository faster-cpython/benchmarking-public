
# Results vs. 3.10.4

- fork: python
- ref: 3b9d793efcfd2c00c14f
- machine: linux-x86_64
- commit hash: 3b9d793
- commit date: 2022-11-14
- overall geometric mean: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221114-pythonperf2-x86_64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 352 ms                                                       | 282 ms: 1.25x faster                                                        |
| chameleon      | 9.62 ms                                                      | 7.19 ms: 1.34x faster                                                       |
| docutils       | 3.41 sec                                                     | 2.77 sec: 1.23x faster                                                      |
| html5lib       | 96.3 ms                                                      | 66.7 ms: 1.44x faster                                                       |
| tornado_http   | 151 ms                                                       | 115 ms: 1.31x faster                                                        |
| Geometric mean | (ref)                                                        | 1.31x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221114-pythonperf2-x86_64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 109 ms                                                       | 73.2 ms: 1.49x faster                                                       |
| nbody          | 132 ms                                                       | 90.9 ms: 1.45x faster                                                       |
| pidigits       | 271 ms                                                       | 252 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                        | 1.33x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221114-pythonperf2-x86_64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 191 ms                                                       | 147 ms: 1.30x faster                                                        |
| regex_dna      | 261 ms                                                       | 227 ms: 1.15x faster                                                        |
| regex_v8       | 26.0 ms                                                      | 23.2 ms: 1.12x faster                                                       |
| regex_effbot   | 2.99 ms                                                      | 3.45 ms: 1.15x slower                                                       |
| Geometric mean | (ref)                                                        | 1.10x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221114-pythonperf2-x86_64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 318 us                                                       | 209 us: 1.52x faster                                                        |
| pickle_pure_python   | 451 us                                                       | 314 us: 1.44x faster                                                        |
| xml_etree_process    | 77.6 ms                                                      | 54.8 ms: 1.42x faster                                                       |
| json_dumps           | 14.3 ms                                                      | 10.2 ms: 1.40x faster                                                       |
| json_loads           | 30.3 us                                                      | 23.7 us: 1.28x faster                                                       |
| xml_etree_generate   | 94.1 ms                                                      | 79.3 ms: 1.19x faster                                                       |
| pickle_list          | 4.11 us                                                      | 3.65 us: 1.13x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 143 ms: 1.12x faster                                                        |
| unpickle             | 13.3 us                                                      | 12.6 us: 1.05x faster                                                       |
| unpickle_list        | 4.73 us                                                      | 4.51 us: 1.05x faster                                                       |
| xml_etree_iterparse  | 109 ms                                                       | 108 ms: 1.01x faster                                                        |
| pickle               | 10.1 us                                                      | 10.1 us: 1.01x faster                                                       |
| pickle_dict          | 29.5 us                                                      | 33.4 us: 1.13x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.18x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221114-pythonperf2-x86_64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 10.8 ms: 1.06x faster                                                       |
| python_startup_no_site | 7.32 ms                                                      | 7.87 ms: 1.08x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221114-pythonperf2-x86_64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.2 ms: 1.44x faster                                                       |
| django_template | 52.0 ms                                                      | 39.7 ms: 1.31x faster                                                       |
| genshi_text     | 31.7 ms                                                      | 25.2 ms: 1.26x faster                                                       |
| genshi_xml      | 63.5 ms                                                      | 54.0 ms: 1.18x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.29x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221114-pythonperf2-x86_64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 7.54 ms                                                      | 3.64 ms: 2.07x faster                                                       |
| pyflate                 | 731 ms                                                       | 436 ms: 1.68x faster                                                        |
| scimark_sor             | 177 ms                                                       | 106 ms: 1.66x faster                                                        |
| logging_silent          | 165 ns                                                       | 99.2 ns: 1.66x faster                                                       |
| go                      | 264 ms                                                       | 160 ms: 1.65x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                       | 66.4 ms: 1.64x faster                                                       |
| richards                | 73.9 ms                                                      | 45.4 ms: 1.63x faster                                                       |
| raytrace                | 491 ms                                                       | 305 ms: 1.61x faster                                                        |
| bench_mp_pool           | 7.10 ms                                                      | 4.59 ms: 1.55x faster                                                       |
| unpickle_pure_python    | 318 us                                                       | 209 us: 1.52x faster                                                        |
| float                   | 109 ms                                                       | 73.2 ms: 1.49x faster                                                       |
| sqlglot_parse           | 2.24 ms                                                      | 1.50 ms: 1.49x faster                                                       |
| spectral_norm           | 138 ms                                                       | 93.2 ms: 1.48x faster                                                       |
| chaos                   | 108 ms                                                       | 72.9 ms: 1.48x faster                                                       |
| scimark_lu              | 164 ms                                                       | 111 ms: 1.48x faster                                                        |
| crypto_pyaes            | 119 ms                                                       | 80.7 ms: 1.47x faster                                                       |
| nbody                   | 132 ms                                                       | 90.9 ms: 1.45x faster                                                       |
| html5lib                | 96.3 ms                                                      | 66.7 ms: 1.44x faster                                                       |
| mako                    | 14.7 ms                                                      | 10.2 ms: 1.44x faster                                                       |
| pickle_pure_python      | 451 us                                                       | 314 us: 1.44x faster                                                        |
| sqlglot_transpile       | 2.69 ms                                                      | 1.87 ms: 1.44x faster                                                       |
| xml_etree_process       | 77.6 ms                                                      | 54.8 ms: 1.42x faster                                                       |
| hexiom                  | 9.54 ms                                                      | 6.76 ms: 1.41x faster                                                       |
| json_dumps              | 14.3 ms                                                      | 10.2 ms: 1.40x faster                                                       |
| async_tree_io           | 1.61 sec                                                     | 1.17 sec: 1.38x faster                                                      |
| pprint_pformat          | 2.12 sec                                                     | 1.55 sec: 1.37x faster                                                      |
| pprint_safe_repr        | 1.03 sec                                                     | 752 ms: 1.37x faster                                                        |
| scimark_sparse_mat_mult | 5.09 ms                                                      | 3.74 ms: 1.36x faster                                                       |
| logging_simple          | 9.24 us                                                      | 6.78 us: 1.36x faster                                                       |
| async_tree_none         | 698 ms                                                       | 520 ms: 1.34x faster                                                        |
| thrift                  | 1.23 ms                                                      | 913 us: 1.34x faster                                                        |
| deepcopy_memo           | 49.2 us                                                      | 36.7 us: 1.34x faster                                                       |
| chameleon               | 9.62 ms                                                      | 7.19 ms: 1.34x faster                                                       |
| pycparser               | 1.66 sec                                                     | 1.24 sec: 1.33x faster                                                      |
| async_tree_memoization  | 822 ms                                                       | 621 ms: 1.33x faster                                                        |
| scimark_fft             | 359 ms                                                       | 273 ms: 1.31x faster                                                        |
| django_template         | 52.0 ms                                                      | 39.7 ms: 1.31x faster                                                       |
| tornado_http            | 151 ms                                                       | 115 ms: 1.31x faster                                                        |
| logging_format          | 9.94 us                                                      | 7.60 us: 1.31x faster                                                       |
| unpack_sequence         | 59.7 ns                                                      | 45.8 ns: 1.30x faster                                                       |
| async_generators        | 419 ms                                                       | 321 ms: 1.30x faster                                                        |
| aiohttp                 | 1.18 ms                                                      | 904 us: 1.30x faster                                                        |
| regex_compile           | 191 ms                                                       | 147 ms: 1.30x faster                                                        |
| gunicorn                | 1.15 ms                                                      | 886 us: 1.29x faster                                                        |
| json_loads              | 30.3 us                                                      | 23.7 us: 1.28x faster                                                       |
| fannkuch                | 496 ms                                                       | 391 ms: 1.27x faster                                                        |
| genshi_text             | 31.7 ms                                                      | 25.2 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed | 951 ms                                                       | 762 ms: 1.25x faster                                                        |
| 2to3                    | 352 ms                                                       | 282 ms: 1.25x faster                                                        |
| mypy2                   | 466 ms                                                       | 374 ms: 1.25x faster                                                        |
| docutils                | 3.41 sec                                                     | 2.77 sec: 1.23x faster                                                      |
| sqlglot_normalize       | 147 ms                                                       | 122 ms: 1.20x faster                                                        |
| sqlglot_optimize        | 70.1 ms                                                      | 58.2 ms: 1.20x faster                                                       |
| json                    | 5.94 ms                                                      | 4.95 ms: 1.20x faster                                                       |
| dulwich_log             | 80.5 ms                                                      | 67.2 ms: 1.20x faster                                                       |
| xml_etree_generate      | 94.1 ms                                                      | 79.3 ms: 1.19x faster                                                       |
| deepcopy                | 457 us                                                       | 387 us: 1.18x faster                                                        |
| genshi_xml              | 63.5 ms                                                      | 54.0 ms: 1.18x faster                                                       |
| bench_thread_pool       | 1.14 ms                                                      | 969 us: 1.18x faster                                                        |
| dask                    | 478 ms                                                       | 410 ms: 1.16x faster                                                        |
| deepcopy_reduce         | 3.91 us                                                      | 3.39 us: 1.15x faster                                                       |
| sqlite_synth            | 2.96 us                                                      | 2.57 us: 1.15x faster                                                       |
| regex_dna               | 261 ms                                                       | 227 ms: 1.15x faster                                                        |
| create_gc_cycles        | 1.80 ms                                                      | 1.60 ms: 1.13x faster                                                       |
| pickle_list             | 4.11 us                                                      | 3.65 us: 1.13x faster                                                       |
| regex_v8                | 26.0 ms                                                      | 23.2 ms: 1.12x faster                                                       |
| xml_etree_parse         | 160 ms                                                       | 143 ms: 1.12x faster                                                        |
| nqueens                 | 114 ms                                                       | 103 ms: 1.11x faster                                                        |
| meteor_contest          | 142 ms                                                       | 129 ms: 1.10x faster                                                        |
| sympy_integrate         | 28.1 ms                                                      | 25.5 ms: 1.10x faster                                                       |
| pathlib                 | 21.3 ms                                                      | 19.3 ms: 1.10x faster                                                       |
| sympy_expand            | 603 ms                                                       | 550 ms: 1.10x faster                                                        |
| coroutines              | 30.6 ms                                                      | 27.9 ms: 1.10x faster                                                       |
| telco                   | 7.14 ms                                                      | 6.58 ms: 1.09x faster                                                       |
| mdp                     | 2.95 sec                                                     | 2.73 sec: 1.08x faster                                                      |
| pidigits                | 271 ms                                                       | 252 ms: 1.08x faster                                                        |
| python_startup          | 11.5 ms                                                      | 10.8 ms: 1.06x faster                                                       |
| sympy_str               | 358 ms                                                       | 337 ms: 1.06x faster                                                        |
| unpickle                | 13.3 us                                                      | 12.6 us: 1.05x faster                                                       |
| asyncio_tcp             | 787 ms                                                       | 749 ms: 1.05x faster                                                        |
| unpickle_list           | 4.73 us                                                      | 4.51 us: 1.05x faster                                                       |
| sympy_sum               | 193 ms                                                       | 184 ms: 1.05x faster                                                        |
| xml_etree_iterparse     | 109 ms                                                       | 108 ms: 1.01x faster                                                        |
| comprehensions          | 27.3 us                                                      | 26.9 us: 1.01x faster                                                       |
| pickle                  | 10.1 us                                                      | 10.1 us: 1.01x faster                                                       |
| generators              | 57.0 ms                                                      | 61.2 ms: 1.07x slower                                                       |
| python_startup_no_site  | 7.32 ms                                                      | 7.87 ms: 1.08x slower                                                       |
| pickle_dict             | 29.5 us                                                      | 33.4 us: 1.13x slower                                                       |
| gc_traversal            | 3.46 ms                                                      | 3.92 ms: 1.13x slower                                                       |
| regex_effbot            | 2.99 ms                                                      | 3.45 ms: 1.15x slower                                                       |
| coverage                | 71.1 ms                                                      | 86.9 ms: 1.22x slower                                                       |
| Geometric mean          | (ref)                                                        | 1.25x faster                                                                |
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
