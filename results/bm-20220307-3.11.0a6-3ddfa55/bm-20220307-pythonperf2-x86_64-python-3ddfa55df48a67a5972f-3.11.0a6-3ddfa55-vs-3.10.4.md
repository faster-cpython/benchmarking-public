
# Results vs. 3.10.4

- fork: python
- ref: 3ddfa55df48a67a5972f
- machine: linux-x86_64
- commit hash: 3ddfa55
- commit date: 2022-03-07
- overall geometric mean: 1.14x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220307-pythonperf2-x86_64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 352 ms                                                       | 300 ms: 1.17x faster                                                        |
| chameleon      | 9.62 ms                                                      | 8.43 ms: 1.14x faster                                                       |
| docutils       | 3.41 sec                                                     | 2.98 sec: 1.14x faster                                                      |
| html5lib       | 96.3 ms                                                      | 75.6 ms: 1.27x faster                                                       |
| tornado_http   | 151 ms                                                       | 130 ms: 1.16x faster                                                        |
| Geometric mean | (ref)                                                        | 1.18x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220307-pythonperf2-x86_64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 109 ms                                                       | 79.1 ms: 1.38x faster                                                       |
| nbody          | 132 ms                                                       | 98.0 ms: 1.35x faster                                                       |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                        | 1.26x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220307-pythonperf2-x86_64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 191 ms                                                       | 161 ms: 1.19x faster                                                        |
| regex_dna      | 261 ms                                                       | 257 ms: 1.02x faster                                                        |
| regex_v8       | 26.0 ms                                                      | 26.4 ms: 1.01x slower                                                       |
| regex_effbot   | 2.99 ms                                                      | 3.49 ms: 1.17x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220307-pythonperf2-x86_64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_process    | 77.6 ms                                                      | 59.4 ms: 1.31x faster                                                       |
| pickle_pure_python   | 451 us                                                       | 352 us: 1.28x faster                                                        |
| json_loads           | 30.3 us                                                      | 23.9 us: 1.27x faster                                                       |
| unpickle_pure_python | 318 us                                                       | 273 us: 1.17x faster                                                        |
| xml_etree_generate   | 94.1 ms                                                      | 83.5 ms: 1.13x faster                                                       |
| json_dumps           | 14.3 ms                                                      | 13.6 ms: 1.05x faster                                                       |
| xml_etree_iterparse  | 109 ms                                                       | 104 ms: 1.04x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 154 ms: 1.04x faster                                                        |
| pickle               | 10.1 us                                                      | 9.96 us: 1.02x faster                                                       |
| unpickle             | 13.3 us                                                      | 13.5 us: 1.02x slower                                                       |
| pickle_list          | 4.11 us                                                      | 4.28 us: 1.04x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 32.2 us: 1.09x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.08x faster                                                                |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220307-pythonperf2-x86_64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 10.4 ms: 1.10x faster                                                       |
| python_startup_no_site | 7.32 ms                                                      | 7.55 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220307-pythonperf2-x86_64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 11.4 ms: 1.29x faster                                                       |
| genshi_text     | 31.7 ms                                                      | 26.5 ms: 1.19x faster                                                       |
| django_template | 52.0 ms                                                      | 43.8 ms: 1.19x faster                                                       |
| genshi_xml      | 63.5 ms                                                      | 60.7 ms: 1.05x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.18x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220307-pythonperf2-x86_64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 7.54 ms                                                      | 4.49 ms: 1.68x faster                                                       |
| go                      | 264 ms                                                       | 178 ms: 1.48x faster                                                        |
| pyflate                 | 731 ms                                                       | 494 ms: 1.48x faster                                                        |
| bench_mp_pool           | 7.10 ms                                                      | 4.80 ms: 1.48x faster                                                       |
| scimark_sor             | 177 ms                                                       | 121 ms: 1.47x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                       | 74.4 ms: 1.46x faster                                                       |
| raytrace                | 491 ms                                                       | 343 ms: 1.43x faster                                                        |
| logging_silent          | 165 ns                                                       | 115 ns: 1.43x faster                                                        |
| chaos                   | 108 ms                                                       | 77.5 ms: 1.39x faster                                                       |
| float                   | 109 ms                                                       | 79.1 ms: 1.38x faster                                                       |
| async_tree_io           | 1.61 sec                                                     | 1.19 sec: 1.36x faster                                                      |
| nbody                   | 132 ms                                                       | 98.0 ms: 1.35x faster                                                       |
| scimark_lu              | 164 ms                                                       | 122 ms: 1.35x faster                                                        |
| richards                | 73.9 ms                                                      | 55.9 ms: 1.32x faster                                                       |
| async_tree_none         | 698 ms                                                       | 532 ms: 1.31x faster                                                        |
| async_generators        | 419 ms                                                       | 320 ms: 1.31x faster                                                        |
| xml_etree_process       | 77.6 ms                                                      | 59.4 ms: 1.31x faster                                                       |
| logging_simple          | 9.24 us                                                      | 7.08 us: 1.30x faster                                                       |
| mako                    | 14.7 ms                                                      | 11.4 ms: 1.29x faster                                                       |
| logging_format          | 9.94 us                                                      | 7.75 us: 1.28x faster                                                       |
| pickle_pure_python      | 451 us                                                       | 352 us: 1.28x faster                                                        |
| html5lib                | 96.3 ms                                                      | 75.6 ms: 1.27x faster                                                       |
| crypto_pyaes            | 119 ms                                                       | 93.5 ms: 1.27x faster                                                       |
| json_loads              | 30.3 us                                                      | 23.9 us: 1.27x faster                                                       |
| async_tree_memoization  | 822 ms                                                       | 651 ms: 1.26x faster                                                        |
| spectral_norm           | 138 ms                                                       | 111 ms: 1.25x faster                                                        |
| async_tree_cpu_io_mixed | 951 ms                                                       | 763 ms: 1.25x faster                                                        |
| thrift                  | 1.23 ms                                                      | 991 us: 1.24x faster                                                        |
| hexiom                  | 9.54 ms                                                      | 7.74 ms: 1.23x faster                                                       |
| pprint_safe_repr        | 1.03 sec                                                     | 853 ms: 1.20x faster                                                        |
| pprint_pformat          | 2.12 sec                                                     | 1.77 sec: 1.20x faster                                                      |
| genshi_text             | 31.7 ms                                                      | 26.5 ms: 1.19x faster                                                       |
| regex_compile           | 191 ms                                                       | 161 ms: 1.19x faster                                                        |
| django_template         | 52.0 ms                                                      | 43.8 ms: 1.19x faster                                                       |
| deepcopy_memo           | 49.2 us                                                      | 41.7 us: 1.18x faster                                                       |
| json                    | 5.94 ms                                                      | 5.04 ms: 1.18x faster                                                       |
| scimark_fft             | 359 ms                                                       | 305 ms: 1.18x faster                                                        |
| aiohttp                 | 1.18 ms                                                      | 1.00 ms: 1.17x faster                                                       |
| 2to3                    | 352 ms                                                       | 300 ms: 1.17x faster                                                        |
| sqlite_synth            | 2.96 us                                                      | 2.54 us: 1.17x faster                                                       |
| unpickle_pure_python    | 318 us                                                       | 273 us: 1.17x faster                                                        |
| pycparser               | 1.66 sec                                                     | 1.43 sec: 1.16x faster                                                      |
| tornado_http            | 151 ms                                                       | 130 ms: 1.16x faster                                                        |
| gunicorn                | 1.15 ms                                                      | 994 us: 1.15x faster                                                        |
| sqlalchemy_declarative  | 188 ms                                                       | 164 ms: 1.15x faster                                                        |
| docutils                | 3.41 sec                                                     | 2.98 sec: 1.14x faster                                                      |
| chameleon               | 9.62 ms                                                      | 8.43 ms: 1.14x faster                                                       |
| nqueens                 | 114 ms                                                       | 100 ms: 1.13x faster                                                        |
| xml_etree_generate      | 94.1 ms                                                      | 83.5 ms: 1.13x faster                                                       |
| scimark_sparse_mat_mult | 5.09 ms                                                      | 4.53 ms: 1.12x faster                                                       |
| sqlglot_normalize       | 147 ms                                                       | 131 ms: 1.12x faster                                                        |
| deepcopy                | 457 us                                                       | 413 us: 1.11x faster                                                        |
| create_gc_cycles        | 1.80 ms                                                      | 1.63 ms: 1.11x faster                                                       |
| pathlib                 | 21.3 ms                                                      | 19.3 ms: 1.10x faster                                                       |
| python_startup          | 11.5 ms                                                      | 10.4 ms: 1.10x faster                                                       |
| sqlglot_optimize        | 70.1 ms                                                      | 63.7 ms: 1.10x faster                                                       |
| fannkuch                | 496 ms                                                       | 453 ms: 1.10x faster                                                        |
| flaskblogging           | 4.37 ms                                                      | 3.99 ms: 1.10x faster                                                       |
| bench_thread_pool       | 1.14 ms                                                      | 1.04 ms: 1.09x faster                                                       |
| dulwich_log             | 80.5 ms                                                      | 73.8 ms: 1.09x faster                                                       |
| sqlalchemy_imperative   | 22.9 ms                                                      | 21.0 ms: 1.09x faster                                                       |
| sympy_integrate         | 28.1 ms                                                      | 25.9 ms: 1.08x faster                                                       |
| dask                    | 478 ms                                                       | 442 ms: 1.08x faster                                                        |
| sqlglot_transpile       | 2.69 ms                                                      | 2.50 ms: 1.07x faster                                                       |
| pidigits                | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| meteor_contest          | 142 ms                                                       | 133 ms: 1.07x faster                                                        |
| sqlglot_parse           | 2.24 ms                                                      | 2.13 ms: 1.05x faster                                                       |
| sympy_expand            | 603 ms                                                       | 573 ms: 1.05x faster                                                        |
| deepcopy_reduce         | 3.91 us                                                      | 3.73 us: 1.05x faster                                                       |
| json_dumps              | 14.3 ms                                                      | 13.6 ms: 1.05x faster                                                       |
| sympy_sum               | 193 ms                                                       | 184 ms: 1.05x faster                                                        |
| genshi_xml              | 63.5 ms                                                      | 60.7 ms: 1.05x faster                                                       |
| xml_etree_iterparse     | 109 ms                                                       | 104 ms: 1.04x faster                                                        |
| sympy_str               | 358 ms                                                       | 343 ms: 1.04x faster                                                        |
| generators              | 57.0 ms                                                      | 54.8 ms: 1.04x faster                                                       |
| xml_etree_parse         | 160 ms                                                       | 154 ms: 1.04x faster                                                        |
| asyncio_tcp             | 787 ms                                                       | 757 ms: 1.04x faster                                                        |
| telco                   | 7.14 ms                                                      | 6.90 ms: 1.03x faster                                                       |
| pickle                  | 10.1 us                                                      | 9.96 us: 1.02x faster                                                       |
| regex_dna               | 261 ms                                                       | 257 ms: 1.02x faster                                                        |
| coroutines              | 30.6 ms                                                      | 30.1 ms: 1.02x faster                                                       |
| mdp                     | 2.95 sec                                                     | 2.91 sec: 1.01x faster                                                      |
| regex_v8                | 26.0 ms                                                      | 26.4 ms: 1.01x slower                                                       |
| unpickle                | 13.3 us                                                      | 13.5 us: 1.02x slower                                                       |
| python_startup_no_site  | 7.32 ms                                                      | 7.55 ms: 1.03x slower                                                       |
| pickle_list             | 4.11 us                                                      | 4.28 us: 1.04x slower                                                       |
| comprehensions          | 27.3 us                                                      | 29.6 us: 1.09x slower                                                       |
| pickle_dict             | 29.5 us                                                      | 32.2 us: 1.09x slower                                                       |
| gc_traversal            | 3.46 ms                                                      | 4.03 ms: 1.17x slower                                                       |
| regex_effbot            | 2.99 ms                                                      | 3.49 ms: 1.17x slower                                                       |
| coverage                | 71.1 ms                                                      | 84.1 ms: 1.18x slower                                                       |
| unpack_sequence         | 59.7 ns                                                      | 152 ns: 2.54x slower                                                        |
| Geometric mean          | (ref)                                                        | 1.14x faster                                                                |

Benchmark hidden because not significant (1): unpickle_list
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: mypy2, pylint
