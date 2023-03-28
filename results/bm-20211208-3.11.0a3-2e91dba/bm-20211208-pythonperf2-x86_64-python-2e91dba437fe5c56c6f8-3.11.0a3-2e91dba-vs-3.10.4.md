
# Results vs. 3.10.4

- fork: python
- ref: 2e91dba437fe5c56c6f8
- machine: linux-x86_64
- commit hash: 2e91dba
- commit date: 2021-12-08
- overall geometric mean: 1.15x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211208-pythonperf2-x86_64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 352 ms                                                       | 293 ms: 1.20x faster                                                        |
| chameleon      | 9.62 ms                                                      | 8.85 ms: 1.09x faster                                                       |
| docutils       | 3.41 sec                                                     | 3.02 sec: 1.13x faster                                                      |
| html5lib       | 96.3 ms                                                      | 75.1 ms: 1.28x faster                                                       |
| tornado_http   | 151 ms                                                       | 135 ms: 1.12x faster                                                        |
| Geometric mean | (ref)                                                        | 1.16x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211208-pythonperf2-x86_64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 109 ms                                                       | 80.9 ms: 1.35x faster                                                       |
| nbody          | 132 ms                                                       | 109 ms: 1.22x faster                                                        |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                        | 1.21x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211208-pythonperf2-x86_64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 191 ms                                                       | 153 ms: 1.25x faster                                                        |
| regex_v8       | 26.0 ms                                                      | 25.7 ms: 1.01x faster                                                       |
| regex_effbot   | 2.99 ms                                                      | 3.10 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211208-pythonperf2-x86_64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_process    | 77.6 ms                                                      | 60.9 ms: 1.27x faster                                                       |
| pickle_pure_python   | 451 us                                                       | 366 us: 1.23x faster                                                        |
| unpickle_pure_python | 318 us                                                       | 265 us: 1.20x faster                                                        |
| json_loads           | 30.3 us                                                      | 25.3 us: 1.20x faster                                                       |
| xml_etree_generate   | 94.1 ms                                                      | 82.8 ms: 1.14x faster                                                       |
| unpickle_list        | 4.73 us                                                      | 4.53 us: 1.04x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 155 ms: 1.03x faster                                                        |
| json_dumps           | 14.3 ms                                                      | 14.1 ms: 1.02x faster                                                       |
| unpickle             | 13.3 us                                                      | 13.2 us: 1.01x faster                                                       |
| xml_etree_iterparse  | 109 ms                                                       | 110 ms: 1.01x slower                                                        |
| pickle               | 10.1 us                                                      | 10.2 us: 1.01x slower                                                       |
| pickle_list          | 4.11 us                                                      | 4.32 us: 1.05x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 33.0 us: 1.12x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.07x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211208-pythonperf2-x86_64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 10.1 ms: 1.13x faster                                                       |
| python_startup_no_site | 7.32 ms                                                      | 7.14 ms: 1.03x faster                                                       |
| Geometric mean         | (ref)                                                        | 1.08x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211208-pythonperf2-x86_64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 52.0 ms                                                      | 44.9 ms: 1.16x faster                                                       |
| mako            | 14.7 ms                                                      | 12.9 ms: 1.15x faster                                                       |
| genshi_text     | 31.7 ms                                                      | 28.2 ms: 1.12x faster                                                       |
| genshi_xml      | 63.5 ms                                                      | 59.7 ms: 1.06x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.12x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211208-pythonperf2-x86_64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 7.54 ms                                                      | 4.78 ms: 1.58x faster                                                       |
| scimark_sor             | 177 ms                                                       | 115 ms: 1.53x faster                                                        |
| go                      | 264 ms                                                       | 173 ms: 1.53x faster                                                        |
| scimark_lu              | 164 ms                                                       | 110 ms: 1.50x faster                                                        |
| bench_mp_pool           | 7.10 ms                                                      | 4.90 ms: 1.45x faster                                                       |
| logging_silent          | 165 ns                                                       | 116 ns: 1.42x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                       | 76.7 ms: 1.42x faster                                                       |
| raytrace                | 491 ms                                                       | 347 ms: 1.42x faster                                                        |
| pyflate                 | 731 ms                                                       | 525 ms: 1.39x faster                                                        |
| spectral_norm           | 138 ms                                                       | 99.9 ms: 1.38x faster                                                       |
| chaos                   | 108 ms                                                       | 78.3 ms: 1.38x faster                                                       |
| float                   | 109 ms                                                       | 80.9 ms: 1.35x faster                                                       |
| logging_simple          | 9.24 us                                                      | 7.04 us: 1.31x faster                                                       |
| async_generators        | 419 ms                                                       | 319 ms: 1.31x faster                                                        |
| richards                | 73.9 ms                                                      | 56.7 ms: 1.30x faster                                                       |
| logging_format          | 9.94 us                                                      | 7.70 us: 1.29x faster                                                       |
| unpack_sequence         | 59.7 ns                                                      | 46.3 ns: 1.29x faster                                                       |
| hexiom                  | 9.54 ms                                                      | 7.41 ms: 1.29x faster                                                       |
| html5lib                | 96.3 ms                                                      | 75.1 ms: 1.28x faster                                                       |
| async_tree_none         | 698 ms                                                       | 545 ms: 1.28x faster                                                        |
| xml_etree_process       | 77.6 ms                                                      | 60.9 ms: 1.27x faster                                                       |
| crypto_pyaes            | 119 ms                                                       | 94.7 ms: 1.25x faster                                                       |
| regex_compile           | 191 ms                                                       | 153 ms: 1.25x faster                                                        |
| pprint_safe_repr        | 1.03 sec                                                     | 832 ms: 1.23x faster                                                        |
| pickle_pure_python      | 451 us                                                       | 366 us: 1.23x faster                                                        |
| thrift                  | 1.23 ms                                                      | 995 us: 1.23x faster                                                        |
| pycparser               | 1.66 sec                                                     | 1.35 sec: 1.23x faster                                                      |
| async_tree_io           | 1.61 sec                                                     | 1.32 sec: 1.22x faster                                                      |
| pprint_pformat          | 2.12 sec                                                     | 1.74 sec: 1.22x faster                                                      |
| nbody                   | 132 ms                                                       | 109 ms: 1.22x faster                                                        |
| 2to3                    | 352 ms                                                       | 293 ms: 1.20x faster                                                        |
| async_tree_memoization  | 822 ms                                                       | 686 ms: 1.20x faster                                                        |
| unpickle_pure_python    | 318 us                                                       | 265 us: 1.20x faster                                                        |
| json_loads              | 30.3 us                                                      | 25.3 us: 1.20x faster                                                       |
| deepcopy_memo           | 49.2 us                                                      | 41.5 us: 1.19x faster                                                       |
| async_tree_cpu_io_mixed | 951 ms                                                       | 811 ms: 1.17x faster                                                        |
| fannkuch                | 496 ms                                                       | 428 ms: 1.16x faster                                                        |
| django_template         | 52.0 ms                                                      | 44.9 ms: 1.16x faster                                                       |
| mako                    | 14.7 ms                                                      | 12.9 ms: 1.15x faster                                                       |
| scimark_fft             | 359 ms                                                       | 314 ms: 1.14x faster                                                        |
| gunicorn                | 1.15 ms                                                      | 1.00 ms: 1.14x faster                                                       |
| generators              | 57.0 ms                                                      | 50.1 ms: 1.14x faster                                                       |
| xml_etree_generate      | 94.1 ms                                                      | 82.8 ms: 1.14x faster                                                       |
| python_startup          | 11.5 ms                                                      | 10.1 ms: 1.13x faster                                                       |
| json                    | 5.94 ms                                                      | 5.24 ms: 1.13x faster                                                       |
| coroutines              | 30.6 ms                                                      | 27.0 ms: 1.13x faster                                                       |
| docutils                | 3.41 sec                                                     | 3.02 sec: 1.13x faster                                                      |
| genshi_text             | 31.7 ms                                                      | 28.2 ms: 1.12x faster                                                       |
| tornado_http            | 151 ms                                                       | 135 ms: 1.12x faster                                                        |
| scimark_sparse_mat_mult | 5.09 ms                                                      | 4.58 ms: 1.11x faster                                                       |
| sqlglot_normalize       | 147 ms                                                       | 133 ms: 1.11x faster                                                        |
| dulwich_log             | 80.5 ms                                                      | 73.0 ms: 1.10x faster                                                       |
| deepcopy_reduce         | 3.91 us                                                      | 3.55 us: 1.10x faster                                                       |
| nqueens                 | 114 ms                                                       | 103 ms: 1.10x faster                                                        |
| dask                    | 478 ms                                                       | 435 ms: 1.10x faster                                                        |
| meteor_contest          | 142 ms                                                       | 129 ms: 1.10x faster                                                        |
| sqlite_synth            | 2.96 us                                                      | 2.70 us: 1.10x faster                                                       |
| deepcopy                | 457 us                                                       | 418 us: 1.10x faster                                                        |
| create_gc_cycles        | 1.80 ms                                                      | 1.66 ms: 1.09x faster                                                       |
| chameleon               | 9.62 ms                                                      | 8.85 ms: 1.09x faster                                                       |
| sqlglot_optimize        | 70.1 ms                                                      | 64.7 ms: 1.08x faster                                                       |
| bench_thread_pool       | 1.14 ms                                                      | 1.06 ms: 1.08x faster                                                       |
| pidigits                | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| mdp                     | 2.95 sec                                                     | 2.76 sec: 1.07x faster                                                      |
| pathlib                 | 21.3 ms                                                      | 19.9 ms: 1.07x faster                                                       |
| genshi_xml              | 63.5 ms                                                      | 59.7 ms: 1.06x faster                                                       |
| sympy_integrate         | 28.1 ms                                                      | 26.5 ms: 1.06x faster                                                       |
| unpickle_list           | 4.73 us                                                      | 4.53 us: 1.04x faster                                                       |
| sympy_expand            | 603 ms                                                       | 579 ms: 1.04x faster                                                        |
| sqlglot_transpile       | 2.69 ms                                                      | 2.60 ms: 1.04x faster                                                       |
| xml_etree_parse         | 160 ms                                                       | 155 ms: 1.03x faster                                                        |
| python_startup_no_site  | 7.32 ms                                                      | 7.14 ms: 1.03x faster                                                       |
| sympy_str               | 358 ms                                                       | 350 ms: 1.02x faster                                                        |
| sympy_sum               | 193 ms                                                       | 189 ms: 1.02x faster                                                        |
| json_dumps              | 14.3 ms                                                      | 14.1 ms: 1.02x faster                                                       |
| sqlglot_parse           | 2.24 ms                                                      | 2.21 ms: 1.02x faster                                                       |
| regex_v8                | 26.0 ms                                                      | 25.7 ms: 1.01x faster                                                       |
| unpickle                | 13.3 us                                                      | 13.2 us: 1.01x faster                                                       |
| xml_etree_iterparse     | 109 ms                                                       | 110 ms: 1.01x slower                                                        |
| pickle                  | 10.1 us                                                      | 10.2 us: 1.01x slower                                                       |
| coverage                | 71.1 ms                                                      | 72.1 ms: 1.01x slower                                                       |
| regex_effbot            | 2.99 ms                                                      | 3.10 ms: 1.04x slower                                                       |
| pickle_list             | 4.11 us                                                      | 4.32 us: 1.05x slower                                                       |
| pickle_dict             | 29.5 us                                                      | 33.0 us: 1.12x slower                                                       |
| comprehensions          | 27.3 us                                                      | 30.6 us: 1.12x slower                                                       |
| gc_traversal            | 3.46 ms                                                      | 3.89 ms: 1.13x slower                                                       |
| flaskblogging           | 4.37 ms                                                      | 4.95 ms: 1.13x slower                                                       |
| Geometric mean          | (ref)                                                        | 1.15x faster                                                                |

Benchmark hidden because not significant (2): telco, regex_dna
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
