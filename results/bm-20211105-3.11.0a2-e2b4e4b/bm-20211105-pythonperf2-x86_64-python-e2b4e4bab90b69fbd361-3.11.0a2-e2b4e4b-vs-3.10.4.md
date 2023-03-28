
# Results vs. 3.10.4

- fork: python
- ref: e2b4e4bab90b69fbd361
- machine: linux-x86_64
- commit hash: e2b4e4b
- commit date: 2021-11-05
- overall geometric mean: 1.13x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-pythonperf2-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 352 ms                                                       | 299 ms: 1.18x faster                                                        |
| chameleon      | 9.62 ms                                                      | 9.27 ms: 1.04x faster                                                       |
| docutils       | 3.41 sec                                                     | 3.05 sec: 1.12x faster                                                      |
| html5lib       | 96.3 ms                                                      | 80.0 ms: 1.20x faster                                                       |
| tornado_http   | 151 ms                                                       | 136 ms: 1.11x faster                                                        |
| Geometric mean | (ref)                                                        | 1.13x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-pythonperf2-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 109 ms                                                       | 86.1 ms: 1.27x faster                                                       |
| nbody          | 132 ms                                                       | 113 ms: 1.17x faster                                                        |
| pidigits       | 271 ms                                                       | 264 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                        | 1.15x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-pythonperf2-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 191 ms                                                       | 158 ms: 1.21x faster                                                        |
| regex_v8       | 26.0 ms                                                      | 25.8 ms: 1.01x faster                                                       |
| regex_dna      | 261 ms                                                       | 262 ms: 1.00x slower                                                        |
| regex_effbot   | 2.99 ms                                                      | 3.06 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-pythonperf2-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_process    | 77.6 ms                                                      | 61.7 ms: 1.26x faster                                                       |
| json_loads           | 30.3 us                                                      | 24.7 us: 1.23x faster                                                       |
| pickle_pure_python   | 451 us                                                       | 386 us: 1.17x faster                                                        |
| unpickle_pure_python | 318 us                                                       | 277 us: 1.15x faster                                                        |
| xml_etree_generate   | 94.1 ms                                                      | 85.8 ms: 1.10x faster                                                       |
| json_dumps           | 14.3 ms                                                      | 13.4 ms: 1.06x faster                                                       |
| unpickle_list        | 4.73 us                                                      | 4.55 us: 1.04x faster                                                       |
| xml_etree_iterparse  | 109 ms                                                       | 107 ms: 1.02x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 157 ms: 1.02x faster                                                        |
| unpickle             | 13.3 us                                                      | 13.4 us: 1.01x slower                                                       |
| pickle               | 10.1 us                                                      | 10.3 us: 1.01x slower                                                       |
| pickle_list          | 4.11 us                                                      | 4.17 us: 1.01x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 30.2 us: 1.02x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.07x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-pythonperf2-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.2 ms: 1.03x faster                                                       |
| python_startup_no_site | 7.32 ms                                                      | 7.43 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-pythonperf2-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 12.9 ms: 1.14x faster                                                       |
| genshi_text     | 31.7 ms                                                      | 28.2 ms: 1.12x faster                                                       |
| django_template | 52.0 ms                                                      | 47.4 ms: 1.10x faster                                                       |
| genshi_xml      | 63.5 ms                                                      | 57.9 ms: 1.10x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.12x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-pythonperf2-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 7.54 ms                                                      | 5.07 ms: 1.49x faster                                                       |
| bench_mp_pool           | 7.10 ms                                                      | 5.01 ms: 1.42x faster                                                       |
| raytrace                | 491 ms                                                       | 349 ms: 1.41x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                       | 79.5 ms: 1.37x faster                                                       |
| logging_silent          | 165 ns                                                       | 121 ns: 1.36x faster                                                        |
| chaos                   | 108 ms                                                       | 79.2 ms: 1.36x faster                                                       |
| go                      | 264 ms                                                       | 194 ms: 1.36x faster                                                        |
| spectral_norm           | 138 ms                                                       | 104 ms: 1.32x faster                                                        |
| async_tree_none         | 698 ms                                                       | 532 ms: 1.31x faster                                                        |
| unpack_sequence         | 59.7 ns                                                      | 46.0 ns: 1.30x faster                                                       |
| async_generators        | 419 ms                                                       | 325 ms: 1.29x faster                                                        |
| thrift                  | 1.23 ms                                                      | 961 us: 1.27x faster                                                        |
| async_tree_io           | 1.61 sec                                                     | 1.27 sec: 1.27x faster                                                      |
| float                   | 109 ms                                                       | 86.1 ms: 1.27x faster                                                       |
| scimark_sor             | 177 ms                                                       | 140 ms: 1.27x faster                                                        |
| pyflate                 | 731 ms                                                       | 582 ms: 1.26x faster                                                        |
| logging_simple          | 9.24 us                                                      | 7.35 us: 1.26x faster                                                       |
| xml_etree_process       | 77.6 ms                                                      | 61.7 ms: 1.26x faster                                                       |
| richards                | 73.9 ms                                                      | 59.0 ms: 1.25x faster                                                       |
| crypto_pyaes            | 119 ms                                                       | 94.9 ms: 1.25x faster                                                       |
| scimark_lu              | 164 ms                                                       | 132 ms: 1.24x faster                                                        |
| async_tree_memoization  | 822 ms                                                       | 668 ms: 1.23x faster                                                        |
| logging_format          | 9.94 us                                                      | 8.08 us: 1.23x faster                                                       |
| json_loads              | 30.3 us                                                      | 24.7 us: 1.23x faster                                                       |
| hexiom                  | 9.54 ms                                                      | 7.87 ms: 1.21x faster                                                       |
| regex_compile           | 191 ms                                                       | 158 ms: 1.21x faster                                                        |
| html5lib                | 96.3 ms                                                      | 80.0 ms: 1.20x faster                                                       |
| 2to3                    | 352 ms                                                       | 299 ms: 1.18x faster                                                        |
| nbody                   | 132 ms                                                       | 113 ms: 1.17x faster                                                        |
| pprint_safe_repr        | 1.03 sec                                                     | 877 ms: 1.17x faster                                                        |
| gunicorn                | 1.15 ms                                                      | 980 us: 1.17x faster                                                        |
| pickle_pure_python      | 451 us                                                       | 386 us: 1.17x faster                                                        |
| pprint_pformat          | 2.12 sec                                                     | 1.82 sec: 1.17x faster                                                      |
| async_tree_cpu_io_mixed | 951 ms                                                       | 818 ms: 1.16x faster                                                        |
| scimark_fft             | 359 ms                                                       | 311 ms: 1.16x faster                                                        |
| unpickle_pure_python    | 318 us                                                       | 277 us: 1.15x faster                                                        |
| deepcopy_memo           | 49.2 us                                                      | 42.9 us: 1.15x faster                                                       |
| json                    | 5.94 ms                                                      | 5.19 ms: 1.14x faster                                                       |
| mako                    | 14.7 ms                                                      | 12.9 ms: 1.14x faster                                                       |
| genshi_text             | 31.7 ms                                                      | 28.2 ms: 1.12x faster                                                       |
| docutils                | 3.41 sec                                                     | 3.05 sec: 1.12x faster                                                      |
| scimark_sparse_mat_mult | 5.09 ms                                                      | 4.56 ms: 1.12x faster                                                       |
| pycparser               | 1.66 sec                                                     | 1.48 sec: 1.12x faster                                                      |
| nqueens                 | 114 ms                                                       | 102 ms: 1.12x faster                                                        |
| dulwich_log             | 80.5 ms                                                      | 72.4 ms: 1.11x faster                                                       |
| tornado_http            | 151 ms                                                       | 136 ms: 1.11x faster                                                        |
| sqlglot_normalize       | 147 ms                                                       | 132 ms: 1.11x faster                                                        |
| meteor_contest          | 142 ms                                                       | 128 ms: 1.11x faster                                                        |
| django_template         | 52.0 ms                                                      | 47.4 ms: 1.10x faster                                                       |
| xml_etree_generate      | 94.1 ms                                                      | 85.8 ms: 1.10x faster                                                       |
| genshi_xml              | 63.5 ms                                                      | 57.9 ms: 1.10x faster                                                       |
| bench_thread_pool       | 1.14 ms                                                      | 1.05 ms: 1.09x faster                                                       |
| fannkuch                | 496 ms                                                       | 458 ms: 1.08x faster                                                        |
| generators              | 57.0 ms                                                      | 52.7 ms: 1.08x faster                                                       |
| create_gc_cycles        | 1.80 ms                                                      | 1.67 ms: 1.08x faster                                                       |
| sqlglot_optimize        | 70.1 ms                                                      | 64.9 ms: 1.08x faster                                                       |
| sqlite_synth            | 2.96 us                                                      | 2.75 us: 1.08x faster                                                       |
| dask                    | 478 ms                                                       | 445 ms: 1.07x faster                                                        |
| sympy_expand            | 603 ms                                                       | 563 ms: 1.07x faster                                                        |
| deepcopy                | 457 us                                                       | 428 us: 1.07x faster                                                        |
| pathlib                 | 21.3 ms                                                      | 20.0 ms: 1.06x faster                                                       |
| json_dumps              | 14.3 ms                                                      | 13.4 ms: 1.06x faster                                                       |
| sympy_integrate         | 28.1 ms                                                      | 26.5 ms: 1.06x faster                                                       |
| sympy_sum               | 193 ms                                                       | 183 ms: 1.05x faster                                                        |
| sympy_str               | 358 ms                                                       | 340 ms: 1.05x faster                                                        |
| telco                   | 7.14 ms                                                      | 6.81 ms: 1.05x faster                                                       |
| unpickle_list           | 4.73 us                                                      | 4.55 us: 1.04x faster                                                       |
| chameleon               | 9.62 ms                                                      | 9.27 ms: 1.04x faster                                                       |
| coroutines              | 30.6 ms                                                      | 29.5 ms: 1.04x faster                                                       |
| coverage                | 71.1 ms                                                      | 68.7 ms: 1.03x faster                                                       |
| mdp                     | 2.95 sec                                                     | 2.87 sec: 1.03x faster                                                      |
| python_startup          | 11.5 ms                                                      | 11.2 ms: 1.03x faster                                                       |
| deepcopy_reduce         | 3.91 us                                                      | 3.81 us: 1.03x faster                                                       |
| pidigits                | 271 ms                                                       | 264 ms: 1.02x faster                                                        |
| sqlglot_transpile       | 2.69 ms                                                      | 2.63 ms: 1.02x faster                                                       |
| xml_etree_iterparse     | 109 ms                                                       | 107 ms: 1.02x faster                                                        |
| xml_etree_parse         | 160 ms                                                       | 157 ms: 1.02x faster                                                        |
| regex_v8                | 26.0 ms                                                      | 25.8 ms: 1.01x faster                                                       |
| regex_dna               | 261 ms                                                       | 262 ms: 1.00x slower                                                        |
| unpickle                | 13.3 us                                                      | 13.4 us: 1.01x slower                                                       |
| pickle                  | 10.1 us                                                      | 10.3 us: 1.01x slower                                                       |
| pickle_list             | 4.11 us                                                      | 4.17 us: 1.01x slower                                                       |
| python_startup_no_site  | 7.32 ms                                                      | 7.43 ms: 1.01x slower                                                       |
| pickle_dict             | 29.5 us                                                      | 30.2 us: 1.02x slower                                                       |
| regex_effbot            | 2.99 ms                                                      | 3.06 ms: 1.02x slower                                                       |
| comprehensions          | 27.3 us                                                      | 28.8 us: 1.06x slower                                                       |
| gc_traversal            | 3.46 ms                                                      | 3.77 ms: 1.09x slower                                                       |
| flaskblogging           | 4.37 ms                                                      | 4.84 ms: 1.11x slower                                                       |
| Geometric mean          | (ref)                                                        | 1.13x faster                                                                |

Benchmark hidden because not significant (1): sqlglot_parse
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
