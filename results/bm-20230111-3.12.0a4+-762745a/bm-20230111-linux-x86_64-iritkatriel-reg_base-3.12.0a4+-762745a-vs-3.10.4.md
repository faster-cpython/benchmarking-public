
# Results vs. 3.10.4

- fork: iritkatriel
- ref: reg_base
- machine: linux-x86_64
- commit hash: 762745a
- commit date: 2023-01-11
- overall geometric mean: 1.29x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230111-linux-x86_64-iritkatriel-reg_base-3.12.0a4+-762745a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 254 ms: 1.31x faster                                            |
| chameleon      | 8.86 ms                                                | 6.22 ms: 1.42x faster                                           |
| docutils       | 3.18 sec                                               | 2.52 sec: 1.26x faster                                          |
| html5lib       | 85.8 ms                                                | 59.7 ms: 1.44x faster                                           |
| Geometric mean | (ref)                                                  | 1.36x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230111-linux-x86_64-iritkatriel-reg_base-3.12.0a4+-762745a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 108 ms                                                 | 72.2 ms: 1.49x faster                                           |
| nbody          | 136 ms                                                 | 94.4 ms: 1.44x faster                                           |
| pidigits       | 190 ms                                                 | 193 ms: 1.01x slower                                            |
| Geometric mean | (ref)                                                  | 1.29x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230111-linux-x86_64-iritkatriel-reg_base-3.12.0a4+-762745a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 129 ms: 1.35x faster                                            |
| regex_v8       | 25.0 ms                                                | 21.9 ms: 1.14x faster                                           |
| regex_dna      | 214 ms                                                 | 217 ms: 1.01x slower                                            |
| regex_effbot   | 3.21 ms                                                | 3.76 ms: 1.17x slower                                           |
| Geometric mean | (ref)                                                  | 1.07x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230111-linux-x86_64-iritkatriel-reg_base-3.12.0a4+-762745a |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 284 us: 1.60x faster                                            |
| unpickle_pure_python | 297 us                                                 | 202 us: 1.47x faster                                            |
| json_dumps           | 13.5 ms                                                | 9.38 ms: 1.44x faster                                           |
| xml_etree_process    | 74.5 ms                                                | 54.2 ms: 1.37x faster                                           |
| json_loads           | 28.9 us                                                | 23.8 us: 1.21x faster                                           |
| xml_etree_generate   | 93.3 ms                                                | 77.5 ms: 1.20x faster                                           |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                            |
| unpickle             | 14.3 us                                                | 13.4 us: 1.07x faster                                           |
| pickle_list          | 4.50 us                                                | 4.25 us: 1.06x faster                                           |
| xml_etree_iterparse  | 110 ms                                                 | 106 ms: 1.04x faster                                            |
| unpickle_list        | 4.99 us                                                | 4.85 us: 1.03x faster                                           |
| pickle               | 10.1 us                                                | 10.7 us: 1.06x slower                                           |
| pickle_dict          | 28.3 us                                                | 32.0 us: 1.13x slower                                           |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230111-linux-x86_64-iritkatriel-reg_base-3.12.0a4+-762745a |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.54 ms: 1.63x faster                                           |
| python_startup_no_site | 5.76 ms                                                | 6.08 ms: 1.05x slower                                           |
| Geometric mean         | (ref)                                                  | 1.24x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230111-linux-x86_64-iritkatriel-reg_base-3.12.0a4+-762745a |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.5 ms: 1.49x faster                                           |
| mako            | 14.3 ms                                                | 9.75 ms: 1.46x faster                                           |
| django_template | 46.3 ms                                                | 32.9 ms: 1.41x faster                                           |
| genshi_xml      | 63.6 ms                                                | 46.6 ms: 1.36x faster                                           |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                    |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230111-linux-x86_64-iritkatriel-reg_base-3.12.0a4+-762745a |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.27 ms: 2.26x faster                                           |
| logging_silent          | 173 ns                                                 | 93.4 ns: 1.85x faster                                           |
| scimark_sor             | 193 ms                                                 | 108 ms: 1.79x faster                                            |
| pyflate                 | 675 ms                                                 | 391 ms: 1.73x faster                                            |
| richards                | 71.4 ms                                                | 42.2 ms: 1.69x faster                                           |
| go                      | 226 ms                                                 | 135 ms: 1.67x faster                                            |
| raytrace                | 461 ms                                                 | 281 ms: 1.64x faster                                            |
| python_startup          | 13.9 ms                                                | 8.54 ms: 1.63x faster                                           |
| scimark_monte_carlo     | 105 ms                                                 | 64.3 ms: 1.63x faster                                           |
| pickle_pure_python      | 453 us                                                 | 284 us: 1.60x faster                                            |
| crypto_pyaes            | 118 ms                                                 | 74.8 ms: 1.57x faster                                           |
| hexiom                  | 9.42 ms                                                | 6.09 ms: 1.55x faster                                           |
| chaos                   | 104 ms                                                 | 67.4 ms: 1.54x faster                                           |
| spectral_norm           | 148 ms                                                 | 96.2 ms: 1.54x faster                                           |
| float                   | 108 ms                                                 | 72.2 ms: 1.49x faster                                           |
| genshi_text             | 30.6 ms                                                | 20.5 ms: 1.49x faster                                           |
| unpickle_pure_python    | 297 us                                                 | 202 us: 1.47x faster                                            |
| deepcopy_memo           | 50.0 us                                                | 34.0 us: 1.47x faster                                           |
| mako                    | 14.3 ms                                                | 9.75 ms: 1.46x faster                                           |
| sqlglot_parse           | 2.04 ms                                                | 1.40 ms: 1.46x faster                                           |
| scimark_lu              | 158 ms                                                 | 110 ms: 1.44x faster                                            |
| pprint_pformat          | 1.97 sec                                               | 1.37 sec: 1.44x faster                                          |
| nbody                   | 136 ms                                                 | 94.4 ms: 1.44x faster                                           |
| json_dumps              | 13.5 ms                                                | 9.38 ms: 1.44x faster                                           |
| html5lib                | 85.8 ms                                                | 59.7 ms: 1.44x faster                                           |
| logging_simple          | 8.06 us                                                | 5.62 us: 1.43x faster                                           |
| sqlglot_transpile       | 2.42 ms                                                | 1.69 ms: 1.43x faster                                           |
| logging_format          | 8.92 us                                                | 6.24 us: 1.43x faster                                           |
| chameleon               | 8.86 ms                                                | 6.22 ms: 1.42x faster                                           |
| pprint_safe_repr        | 943 ms                                                 | 667 ms: 1.41x faster                                            |
| django_template         | 46.3 ms                                                | 32.9 ms: 1.41x faster                                           |
| unpack_sequence         | 59.5 ns                                                | 43.1 ns: 1.38x faster                                           |
| xml_etree_process       | 74.5 ms                                                | 54.2 ms: 1.37x faster                                           |
| genshi_xml              | 63.6 ms                                                | 46.6 ms: 1.36x faster                                           |
| thrift                  | 1.03 ms                                                | 757 us: 1.36x faster                                            |
| async_tree_none         | 713 ms                                                 | 529 ms: 1.35x faster                                            |
| regex_compile           | 174 ms                                                 | 129 ms: 1.35x faster                                            |
| async_tree_io           | 1.78 sec                                               | 1.33 sec: 1.33x faster                                          |
| pycparser               | 1.51 sec                                               | 1.15 sec: 1.32x faster                                          |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.17 ms: 1.32x faster                                           |
| 2to3                    | 332 ms                                                 | 254 ms: 1.31x faster                                            |
| scimark_fft             | 414 ms                                                 | 319 ms: 1.30x faster                                            |
| coroutines              | 31.7 ms                                                | 24.4 ms: 1.29x faster                                           |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                            |
| deepcopy                | 429 us                                                 | 334 us: 1.29x faster                                            |
| sqlglot_optimize        | 65.3 ms                                                | 50.8 ms: 1.29x faster                                           |
| fannkuch                | 477 ms                                                 | 373 ms: 1.28x faster                                            |
| async_tree_memoization  | 854 ms                                                 | 670 ms: 1.28x faster                                            |
| deepcopy_reduce         | 3.75 us                                                | 2.95 us: 1.27x faster                                           |
| docutils                | 3.18 sec                                               | 2.52 sec: 1.26x faster                                          |
| mypy                    | 1.01 sec                                               | 809 ms: 1.25x faster                                            |
| async_tree_cpu_io_mixed | 949 ms                                                 | 758 ms: 1.25x faster                                            |
| nqueens                 | 99.3 ms                                                | 80.6 ms: 1.23x faster                                           |
| dulwich_log             | 75.5 ms                                                | 62.1 ms: 1.22x faster                                           |
| json_loads              | 28.9 us                                                | 23.8 us: 1.21x faster                                           |
| bench_thread_pool       | 943 us                                                 | 781 us: 1.21x faster                                            |
| async_generators        | 428 ms                                                 | 354 ms: 1.21x faster                                            |
| xml_etree_generate      | 93.3 ms                                                | 77.5 ms: 1.20x faster                                           |
| sympy_integrate         | 23.9 ms                                                | 20.3 ms: 1.18x faster                                           |
| sympy_expand            | 537 ms                                                 | 460 ms: 1.17x faster                                            |
| json                    | 5.35 ms                                                | 4.66 ms: 1.15x faster                                           |
| sympy_str               | 324 ms                                                 | 283 ms: 1.15x faster                                            |
| regex_v8                | 25.0 ms                                                | 21.9 ms: 1.14x faster                                           |
| sqlite_synth            | 2.90 us                                                | 2.57 us: 1.13x faster                                           |
| sympy_sum               | 183 ms                                                 | 163 ms: 1.13x faster                                            |
| mdp                     | 2.82 sec                                               | 2.51 sec: 1.12x faster                                          |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                           |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                            |
| telco                   | 6.68 ms                                                | 6.24 ms: 1.07x faster                                           |
| unpickle                | 14.3 us                                                | 13.4 us: 1.07x faster                                           |
| pickle_list             | 4.50 us                                                | 4.25 us: 1.06x faster                                           |
| meteor_contest          | 114 ms                                                 | 108 ms: 1.05x faster                                            |
| xml_etree_iterparse     | 110 ms                                                 | 106 ms: 1.04x faster                                            |
| unpickle_list           | 4.99 us                                                | 4.85 us: 1.03x faster                                           |
| generators              | 75.8 ms                                                | 75.4 ms: 1.01x faster                                           |
| pidigits                | 190 ms                                                 | 193 ms: 1.01x slower                                            |
| regex_dna               | 214 ms                                                 | 217 ms: 1.01x slower                                            |
| python_startup_no_site  | 5.76 ms                                                | 6.08 ms: 1.05x slower                                           |
| pickle                  | 10.1 us                                                | 10.7 us: 1.06x slower                                           |
| pickle_dict             | 28.3 us                                                | 32.0 us: 1.13x slower                                           |
| regex_effbot            | 3.21 ms                                                | 3.76 ms: 1.17x slower                                           |
| coverage                | 75.3 ms                                                | 95.1 ms: 1.26x slower                                           |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                    |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (7) of /home/mdboom/Work/builds/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20230111-3.12.0a4+-762745a/bm-20230111-linux-x86_64-iritkatriel-reg_base-3.12.0a4+-762745a.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
