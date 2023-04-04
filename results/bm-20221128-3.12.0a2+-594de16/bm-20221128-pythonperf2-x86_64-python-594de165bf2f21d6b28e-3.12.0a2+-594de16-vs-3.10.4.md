
# Results vs. 3.10.4

- fork: python
- ref: 594de165bf2f21d6b28e
- machine: linux-x86_64
- commit hash: 594de16
- commit date: 2022-11-28
- overall geometric mean: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221128-pythonperf2-x86_64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 352 ms                                                       | 280 ms: 1.26x faster                                                         |
| chameleon      | 9.62 ms                                                      | 7.65 ms: 1.26x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.77 sec: 1.23x faster                                                       |
| html5lib       | 96.3 ms                                                      | 66.5 ms: 1.45x faster                                                        |
| tornado_http   | 151 ms                                                       | 119 ms: 1.27x faster                                                         |
| Geometric mean | (ref)                                                        | 1.29x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221128-pythonperf2-x86_64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 109 ms                                                       | 73.9 ms: 1.48x faster                                                        |
| nbody          | 132 ms                                                       | 89.6 ms: 1.48x faster                                                        |
| pidigits       | 271 ms                                                       | 252 ms: 1.08x faster                                                         |
| Geometric mean | (ref)                                                        | 1.33x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221128-pythonperf2-x86_64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 191 ms                                                       | 149 ms: 1.28x faster                                                         |
| regex_dna      | 261 ms                                                       | 229 ms: 1.14x faster                                                         |
| regex_v8       | 26.0 ms                                                      | 23.2 ms: 1.12x faster                                                        |
| regex_effbot   | 2.99 ms                                                      | 3.36 ms: 1.13x slower                                                        |
| Geometric mean | (ref)                                                        | 1.10x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221128-pythonperf2-x86_64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 318 us                                                       | 219 us: 1.45x faster                                                         |
| pickle_pure_python   | 451 us                                                       | 320 us: 1.41x faster                                                         |
| xml_etree_process    | 77.6 ms                                                      | 55.8 ms: 1.39x faster                                                        |
| json_dumps           | 14.3 ms                                                      | 10.5 ms: 1.36x faster                                                        |
| json_loads           | 30.3 us                                                      | 24.2 us: 1.25x faster                                                        |
| xml_etree_generate   | 94.1 ms                                                      | 79.8 ms: 1.18x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 141 ms: 1.14x faster                                                         |
| pickle_list          | 4.11 us                                                      | 3.84 us: 1.07x faster                                                        |
| xml_etree_iterparse  | 109 ms                                                       | 104 ms: 1.05x faster                                                         |
| unpickle_list        | 4.73 us                                                      | 4.55 us: 1.04x faster                                                        |
| pickle               | 10.1 us                                                      | 9.77 us: 1.04x faster                                                        |
| unpickle             | 13.3 us                                                      | 13.5 us: 1.02x slower                                                        |
| pickle_dict          | 29.5 us                                                      | 31.7 us: 1.07x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.16x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221128-pythonperf2-x86_64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 10.8 ms: 1.06x faster                                                        |
| python_startup_no_site | 7.32 ms                                                      | 7.85 ms: 1.07x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.00x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221128-pythonperf2-x86_64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.2 ms: 1.45x faster                                                        |
| django_template | 52.0 ms                                                      | 40.1 ms: 1.30x faster                                                        |
| genshi_text     | 31.7 ms                                                      | 24.5 ms: 1.29x faster                                                        |
| genshi_xml      | 63.5 ms                                                      | 52.3 ms: 1.21x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.31x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221128-pythonperf2-x86_64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deltablue               | 7.54 ms                                                      | 3.71 ms: 2.03x faster                                                        |
| pyflate                 | 731 ms                                                       | 447 ms: 1.64x faster                                                         |
| go                      | 264 ms                                                       | 162 ms: 1.63x faster                                                         |
| logging_silent          | 165 ns                                                       | 101 ns: 1.63x faster                                                         |
| raytrace                | 491 ms                                                       | 305 ms: 1.61x faster                                                         |
| scimark_lu              | 164 ms                                                       | 103 ms: 1.59x faster                                                         |
| scimark_sor             | 177 ms                                                       | 112 ms: 1.58x faster                                                         |
| bench_mp_pool           | 7.10 ms                                                      | 4.64 ms: 1.53x faster                                                        |
| richards                | 73.9 ms                                                      | 48.9 ms: 1.51x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                       | 72.0 ms: 1.51x faster                                                        |
| float                   | 109 ms                                                       | 73.9 ms: 1.48x faster                                                        |
| chaos                   | 108 ms                                                       | 73.0 ms: 1.48x faster                                                        |
| nbody                   | 132 ms                                                       | 89.6 ms: 1.48x faster                                                        |
| unpickle_pure_python    | 318 us                                                       | 219 us: 1.45x faster                                                         |
| mako                    | 14.7 ms                                                      | 10.2 ms: 1.45x faster                                                        |
| html5lib                | 96.3 ms                                                      | 66.5 ms: 1.45x faster                                                        |
| sqlglot_parse           | 2.24 ms                                                      | 1.55 ms: 1.45x faster                                                        |
| crypto_pyaes            | 119 ms                                                       | 83.7 ms: 1.42x faster                                                        |
| pickle_pure_python      | 451 us                                                       | 320 us: 1.41x faster                                                         |
| hexiom                  | 9.54 ms                                                      | 6.78 ms: 1.41x faster                                                        |
| sqlglot_transpile       | 2.69 ms                                                      | 1.92 ms: 1.40x faster                                                        |
| spectral_norm           | 138 ms                                                       | 98.7 ms: 1.40x faster                                                        |
| async_tree_io           | 1.61 sec                                                     | 1.16 sec: 1.39x faster                                                       |
| xml_etree_process       | 77.6 ms                                                      | 55.8 ms: 1.39x faster                                                        |
| json_dumps              | 14.3 ms                                                      | 10.5 ms: 1.36x faster                                                        |
| scimark_sparse_mat_mult | 5.09 ms                                                      | 3.77 ms: 1.35x faster                                                        |
| async_tree_none         | 698 ms                                                       | 517 ms: 1.35x faster                                                         |
| pprint_pformat          | 2.12 sec                                                     | 1.58 sec: 1.35x faster                                                       |
| pprint_safe_repr        | 1.03 sec                                                     | 768 ms: 1.34x faster                                                         |
| async_tree_memoization  | 822 ms                                                       | 616 ms: 1.33x faster                                                         |
| unpack_sequence         | 59.7 ns                                                      | 45.6 ns: 1.31x faster                                                        |
| thrift                  | 1.23 ms                                                      | 937 us: 1.31x faster                                                         |
| aiohttp                 | 1.18 ms                                                      | 904 us: 1.30x faster                                                         |
| pycparser               | 1.66 sec                                                     | 1.27 sec: 1.30x faster                                                       |
| django_template         | 52.0 ms                                                      | 40.1 ms: 1.30x faster                                                        |
| genshi_text             | 31.7 ms                                                      | 24.5 ms: 1.29x faster                                                        |
| gunicorn                | 1.15 ms                                                      | 895 us: 1.28x faster                                                         |
| regex_compile           | 191 ms                                                       | 149 ms: 1.28x faster                                                         |
| logging_simple          | 9.24 us                                                      | 7.24 us: 1.28x faster                                                        |
| scimark_fft             | 359 ms                                                       | 282 ms: 1.27x faster                                                         |
| deepcopy_memo           | 49.2 us                                                      | 38.8 us: 1.27x faster                                                        |
| logging_format          | 9.94 us                                                      | 7.84 us: 1.27x faster                                                        |
| tornado_http            | 151 ms                                                       | 119 ms: 1.27x faster                                                         |
| async_generators        | 419 ms                                                       | 332 ms: 1.26x faster                                                         |
| 2to3                    | 352 ms                                                       | 280 ms: 1.26x faster                                                         |
| chameleon               | 9.62 ms                                                      | 7.65 ms: 1.26x faster                                                        |
| async_tree_cpu_io_mixed | 951 ms                                                       | 758 ms: 1.26x faster                                                         |
| json_loads              | 30.3 us                                                      | 24.2 us: 1.25x faster                                                        |
| mypy2                   | 466 ms                                                       | 372 ms: 1.25x faster                                                         |
| fannkuch                | 496 ms                                                       | 399 ms: 1.24x faster                                                         |
| docutils                | 3.41 sec                                                     | 2.77 sec: 1.23x faster                                                       |
| sqlglot_normalize       | 147 ms                                                       | 120 ms: 1.23x faster                                                         |
| genshi_xml              | 63.5 ms                                                      | 52.3 ms: 1.21x faster                                                        |
| sqlglot_optimize        | 70.1 ms                                                      | 57.9 ms: 1.21x faster                                                        |
| dulwich_log             | 80.5 ms                                                      | 67.1 ms: 1.20x faster                                                        |
| xml_etree_generate      | 94.1 ms                                                      | 79.8 ms: 1.18x faster                                                        |
| bench_thread_pool       | 1.14 ms                                                      | 970 us: 1.18x faster                                                         |
| json                    | 5.94 ms                                                      | 5.08 ms: 1.17x faster                                                        |
| sqlite_synth            | 2.96 us                                                      | 2.56 us: 1.16x faster                                                        |
| create_gc_cycles        | 1.80 ms                                                      | 1.56 ms: 1.16x faster                                                        |
| dask                    | 478 ms                                                       | 415 ms: 1.15x faster                                                         |
| nqueens                 | 114 ms                                                       | 99.3 ms: 1.14x faster                                                        |
| regex_dna               | 261 ms                                                       | 229 ms: 1.14x faster                                                         |
| xml_etree_parse         | 160 ms                                                       | 141 ms: 1.14x faster                                                         |
| pathlib                 | 21.3 ms                                                      | 18.8 ms: 1.13x faster                                                        |
| regex_v8                | 26.0 ms                                                      | 23.2 ms: 1.12x faster                                                        |
| sympy_expand            | 603 ms                                                       | 543 ms: 1.11x faster                                                         |
| meteor_contest          | 142 ms                                                       | 128 ms: 1.10x faster                                                         |
| deepcopy                | 457 us                                                       | 415 us: 1.10x faster                                                         |
| sympy_integrate         | 28.1 ms                                                      | 25.5 ms: 1.10x faster                                                        |
| deepcopy_reduce         | 3.91 us                                                      | 3.59 us: 1.09x faster                                                        |
| coroutines              | 30.6 ms                                                      | 28.2 ms: 1.09x faster                                                        |
| mdp                     | 2.95 sec                                                     | 2.73 sec: 1.08x faster                                                       |
| pidigits                | 271 ms                                                       | 252 ms: 1.08x faster                                                         |
| sympy_str               | 358 ms                                                       | 334 ms: 1.07x faster                                                         |
| pickle_list             | 4.11 us                                                      | 3.84 us: 1.07x faster                                                        |
| telco                   | 7.14 ms                                                      | 6.69 ms: 1.07x faster                                                        |
| python_startup          | 11.5 ms                                                      | 10.8 ms: 1.06x faster                                                        |
| asyncio_tcp             | 787 ms                                                       | 745 ms: 1.06x faster                                                         |
| xml_etree_iterparse     | 109 ms                                                       | 104 ms: 1.05x faster                                                         |
| sympy_sum               | 193 ms                                                       | 185 ms: 1.04x faster                                                         |
| unpickle_list           | 4.73 us                                                      | 4.55 us: 1.04x faster                                                        |
| pickle                  | 10.1 us                                                      | 9.77 us: 1.04x faster                                                        |
| comprehensions          | 27.3 us                                                      | 26.8 us: 1.02x faster                                                        |
| unpickle                | 13.3 us                                                      | 13.5 us: 1.02x slower                                                        |
| gc_traversal            | 3.46 ms                                                      | 3.56 ms: 1.03x slower                                                        |
| generators              | 57.0 ms                                                      | 61.1 ms: 1.07x slower                                                        |
| python_startup_no_site  | 7.32 ms                                                      | 7.85 ms: 1.07x slower                                                        |
| pickle_dict             | 29.5 us                                                      | 31.7 us: 1.07x slower                                                        |
| regex_effbot            | 2.99 ms                                                      | 3.36 ms: 1.13x slower                                                        |
| coverage                | 71.1 ms                                                      | 85.4 ms: 1.20x slower                                                        |
| Geometric mean          | (ref)                                                        | 1.24x faster                                                                 |
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
