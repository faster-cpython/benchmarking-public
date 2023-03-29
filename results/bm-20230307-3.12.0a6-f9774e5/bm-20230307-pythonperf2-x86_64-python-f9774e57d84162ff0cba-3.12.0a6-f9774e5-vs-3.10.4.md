
# Results vs. 3.10.4

- fork: python
- ref: f9774e57d84162ff0cba
- machine: linux-x86_64
- commit hash: f9774e5
- commit date: 2023-03-07
- overall geometric mean: 1.27x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-pythonperf2-x86_64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 352 ms                                                       | 284 ms: 1.24x faster                                                        |
| chameleon      | 9.62 ms                                                      | 6.94 ms: 1.39x faster                                                       |
| docutils       | 3.41 sec                                                     | 2.79 sec: 1.22x faster                                                      |
| html5lib       | 96.3 ms                                                      | 65.9 ms: 1.46x faster                                                       |
| tornado_http   | 151 ms                                                       | 115 ms: 1.31x faster                                                        |
| Geometric mean | (ref)                                                        | 1.32x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-pythonperf2-x86_64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 109 ms                                                       | 73.9 ms: 1.48x faster                                                       |
| nbody          | 132 ms                                                       | 91.0 ms: 1.45x faster                                                       |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                        | 1.32x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-pythonperf2-x86_64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 191 ms                                                       | 146 ms: 1.31x faster                                                        |
| regex_dna      | 261 ms                                                       | 225 ms: 1.16x faster                                                        |
| regex_v8       | 26.0 ms                                                      | 22.8 ms: 1.14x faster                                                       |
| regex_effbot   | 2.99 ms                                                      | 3.36 ms: 1.12x slower                                                       |
| Geometric mean | (ref)                                                        | 1.11x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-pythonperf2-x86_64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 318 us                                                       | 202 us: 1.57x faster                                                        |
| pickle_pure_python   | 451 us                                                       | 306 us: 1.48x faster                                                        |
| json_dumps           | 14.3 ms                                                      | 10.2 ms: 1.39x faster                                                       |
| xml_etree_process    | 77.6 ms                                                      | 57.3 ms: 1.35x faster                                                       |
| json_loads           | 30.3 us                                                      | 24.4 us: 1.24x faster                                                       |
| xml_etree_generate   | 94.1 ms                                                      | 83.5 ms: 1.13x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 144 ms: 1.11x faster                                                        |
| pickle_list          | 4.11 us                                                      | 3.80 us: 1.08x faster                                                       |
| unpickle_list        | 4.73 us                                                      | 4.44 us: 1.07x faster                                                       |
| xml_etree_iterparse  | 109 ms                                                       | 103 ms: 1.05x faster                                                        |
| pickle               | 10.1 us                                                      | 10.0 us: 1.01x faster                                                       |
| unpickle             | 13.3 us                                                      | 13.4 us: 1.01x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 31.8 us: 1.08x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.17x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-pythonperf2-x86_64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.3 ms: 1.02x faster                                                       |
| python_startup_no_site | 7.32 ms                                                      | 8.34 ms: 1.14x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-pythonperf2-x86_64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.0 ms: 1.47x faster                                                       |
| django_template | 52.0 ms                                                      | 39.1 ms: 1.33x faster                                                       |
| genshi_text     | 31.7 ms                                                      | 24.6 ms: 1.29x faster                                                       |
| genshi_xml      | 63.5 ms                                                      | 53.0 ms: 1.20x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.32x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-pythonperf2-x86_64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 7.54 ms                                                      | 3.33 ms: 2.26x faster                                                       |
| asyncio_tcp             | 787 ms                                                       | 382 ms: 2.06x faster                                                        |
| go                      | 264 ms                                                       | 151 ms: 1.75x faster                                                        |
| logging_silent          | 165 ns                                                       | 94.5 ns: 1.74x faster                                                       |
| raytrace                | 491 ms                                                       | 290 ms: 1.70x faster                                                        |
| pyflate                 | 731 ms                                                       | 432 ms: 1.69x faster                                                        |
| scimark_sor             | 177 ms                                                       | 105 ms: 1.69x faster                                                        |
| richards                | 73.9 ms                                                      | 46.4 ms: 1.59x faster                                                       |
| unpickle_pure_python    | 318 us                                                       | 202 us: 1.57x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                       | 69.5 ms: 1.56x faster                                                       |
| scimark_lu              | 164 ms                                                       | 105 ms: 1.56x faster                                                        |
| chaos                   | 108 ms                                                       | 70.9 ms: 1.52x faster                                                       |
| generators              | 57.0 ms                                                      | 38.4 ms: 1.49x faster                                                       |
| float                   | 109 ms                                                       | 73.9 ms: 1.48x faster                                                       |
| hexiom                  | 9.54 ms                                                      | 6.46 ms: 1.48x faster                                                       |
| pickle_pure_python      | 451 us                                                       | 306 us: 1.48x faster                                                        |
| mako                    | 14.7 ms                                                      | 10.0 ms: 1.47x faster                                                       |
| bench_mp_pool           | 7.10 ms                                                      | 4.84 ms: 1.47x faster                                                       |
| html5lib                | 96.3 ms                                                      | 65.9 ms: 1.46x faster                                                       |
| crypto_pyaes            | 119 ms                                                       | 81.5 ms: 1.45x faster                                                       |
| nbody                   | 132 ms                                                       | 91.0 ms: 1.45x faster                                                       |
| spectral_norm           | 138 ms                                                       | 95.6 ms: 1.44x faster                                                       |
| sqlglot_parse           | 2.24 ms                                                      | 1.58 ms: 1.42x faster                                                       |
| json_dumps              | 14.3 ms                                                      | 10.2 ms: 1.39x faster                                                       |
| deepcopy_memo           | 49.2 us                                                      | 35.4 us: 1.39x faster                                                       |
| sqlglot_transpile       | 2.69 ms                                                      | 1.94 ms: 1.39x faster                                                       |
| chameleon               | 9.62 ms                                                      | 6.94 ms: 1.39x faster                                                       |
| async_tree_io           | 1.61 sec                                                     | 1.17 sec: 1.38x faster                                                      |
| async_tree_none         | 698 ms                                                       | 510 ms: 1.37x faster                                                        |
| pprint_pformat          | 2.12 sec                                                     | 1.55 sec: 1.37x faster                                                      |
| logging_simple          | 9.24 us                                                      | 6.79 us: 1.36x faster                                                       |
| xml_etree_process       | 77.6 ms                                                      | 57.3 ms: 1.35x faster                                                       |
| thrift                  | 1.23 ms                                                      | 909 us: 1.35x faster                                                        |
| pprint_safe_repr        | 1.03 sec                                                     | 762 ms: 1.35x faster                                                        |
| async_tree_memoization  | 822 ms                                                       | 611 ms: 1.35x faster                                                        |
| unpack_sequence         | 59.7 ns                                                      | 44.4 ns: 1.35x faster                                                       |
| pycparser               | 1.66 sec                                                     | 1.23 sec: 1.34x faster                                                      |
| django_template         | 52.0 ms                                                      | 39.1 ms: 1.33x faster                                                       |
| tornado_http            | 151 ms                                                       | 115 ms: 1.31x faster                                                        |
| logging_format          | 9.94 us                                                      | 7.59 us: 1.31x faster                                                       |
| regex_compile           | 191 ms                                                       | 146 ms: 1.31x faster                                                        |
| scimark_fft             | 359 ms                                                       | 278 ms: 1.29x faster                                                        |
| genshi_text             | 31.7 ms                                                      | 24.6 ms: 1.29x faster                                                       |
| async_tree_cpu_io_mixed | 951 ms                                                       | 745 ms: 1.28x faster                                                        |
| dulwich_log             | 80.5 ms                                                      | 63.7 ms: 1.26x faster                                                       |
| json_loads              | 30.3 us                                                      | 24.4 us: 1.24x faster                                                       |
| 2to3                    | 352 ms                                                       | 284 ms: 1.24x faster                                                        |
| coroutines              | 30.6 ms                                                      | 24.7 ms: 1.24x faster                                                       |
| mypy2                   | 466 ms                                                       | 377 ms: 1.24x faster                                                        |
| scimark_sparse_mat_mult | 5.09 ms                                                      | 4.14 ms: 1.23x faster                                                       |
| sqlglot_normalize       | 147 ms                                                       | 120 ms: 1.23x faster                                                        |
| docutils                | 3.41 sec                                                     | 2.79 sec: 1.22x faster                                                      |
| fannkuch                | 496 ms                                                       | 408 ms: 1.22x faster                                                        |
| deepcopy                | 457 us                                                       | 377 us: 1.21x faster                                                        |
| sqlglot_optimize        | 70.1 ms                                                      | 58.2 ms: 1.20x faster                                                       |
| genshi_xml              | 63.5 ms                                                      | 53.0 ms: 1.20x faster                                                       |
| json                    | 5.94 ms                                                      | 5.00 ms: 1.19x faster                                                       |
| deepcopy_reduce         | 3.91 us                                                      | 3.33 us: 1.17x faster                                                       |
| nqueens                 | 114 ms                                                       | 96.9 ms: 1.17x faster                                                       |
| bench_thread_pool       | 1.14 ms                                                      | 974 us: 1.17x faster                                                        |
| regex_dna               | 261 ms                                                       | 225 ms: 1.16x faster                                                        |
| mdp                     | 2.95 sec                                                     | 2.54 sec: 1.16x faster                                                      |
| pathlib                 | 21.3 ms                                                      | 18.5 ms: 1.15x faster                                                       |
| regex_v8                | 26.0 ms                                                      | 22.8 ms: 1.14x faster                                                       |
| sqlite_synth            | 2.96 us                                                      | 2.63 us: 1.13x faster                                                       |
| xml_etree_generate      | 94.1 ms                                                      | 83.5 ms: 1.13x faster                                                       |
| sympy_integrate         | 28.1 ms                                                      | 25.0 ms: 1.12x faster                                                       |
| sympy_expand            | 603 ms                                                       | 538 ms: 1.12x faster                                                        |
| xml_etree_parse         | 160 ms                                                       | 144 ms: 1.11x faster                                                        |
| create_gc_cycles        | 1.80 ms                                                      | 1.63 ms: 1.11x faster                                                       |
| meteor_contest          | 142 ms                                                       | 128 ms: 1.10x faster                                                        |
| sympy_str               | 358 ms                                                       | 328 ms: 1.09x faster                                                        |
| async_generators        | 419 ms                                                       | 385 ms: 1.09x faster                                                        |
| pickle_list             | 4.11 us                                                      | 3.80 us: 1.08x faster                                                       |
| pidigits                | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| unpickle_list           | 4.73 us                                                      | 4.44 us: 1.07x faster                                                       |
| xml_etree_iterparse     | 109 ms                                                       | 103 ms: 1.05x faster                                                        |
| sympy_sum               | 193 ms                                                       | 184 ms: 1.05x faster                                                        |
| telco                   | 7.14 ms                                                      | 6.90 ms: 1.03x faster                                                       |
| comprehensions          | 27.3 us                                                      | 26.7 us: 1.02x faster                                                       |
| python_startup          | 11.5 ms                                                      | 11.3 ms: 1.02x faster                                                       |
| pickle                  | 10.1 us                                                      | 10.0 us: 1.01x faster                                                       |
| unpickle                | 13.3 us                                                      | 13.4 us: 1.01x slower                                                       |
| pickle_dict             | 29.5 us                                                      | 31.8 us: 1.08x slower                                                       |
| regex_effbot            | 2.99 ms                                                      | 3.36 ms: 1.12x slower                                                       |
| python_startup_no_site  | 7.32 ms                                                      | 8.34 ms: 1.14x slower                                                       |
| gc_traversal            | 3.46 ms                                                      | 3.99 ms: 1.15x slower                                                       |
| coverage                | 71.1 ms                                                      | 82.2 ms: 1.16x slower                                                       |
| dask                    | 478 ms                                                       | 560 ms: 1.17x slower                                                        |
| Geometric mean          | (ref)                                                        | 1.27x faster                                                                |
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative
