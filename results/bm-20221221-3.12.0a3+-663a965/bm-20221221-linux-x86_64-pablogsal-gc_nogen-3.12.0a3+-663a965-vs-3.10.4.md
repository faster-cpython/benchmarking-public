
# Results vs. 3.10.4

- fork: pablogsal
- ref: gc_nogen
- machine: linux-x86_64
- commit hash: 663a965
- commit date: 2022-12-21
- overall geometric mean: 1.37x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 243 ms: 1.38x faster                                          |
| chameleon      | 9.17 ms                                                | 6.29 ms: 1.46x faster                                         |
| docutils       | 3.18 sec                                               | 2.13 sec: 1.49x faster                                        |
| html5lib       | 85.9 ms                                                | 57.4 ms: 1.50x faster                                         |
| Geometric mean | (ref)                                                  | 1.45x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 109 ms                                                 | 61.8 ms: 1.76x faster                                         |
| nbody          | 144 ms                                                 | 93.2 ms: 1.54x faster                                         |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                          |
| Geometric mean | (ref)                                                  | 1.38x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 131 ms: 1.36x faster                                          |
| regex_v8       | 25.0 ms                                                | 21.2 ms: 1.18x faster                                         |
| regex_dna      | 214 ms                                                 | 201 ms: 1.06x faster                                          |
| regex_effbot   | 3.19 ms                                                | 3.35 ms: 1.05x slower                                         |
| Geometric mean | (ref)                                                  | 1.13x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 282 us: 1.60x faster                                          |
| unpickle_pure_python | 302 us                                                 | 197 us: 1.53x faster                                          |
| xml_etree_process    | 74.5 ms                                                | 51.5 ms: 1.45x faster                                         |
| json_dumps           | 13.4 ms                                                | 9.30 ms: 1.45x faster                                         |
| xml_etree_iterparse  | 111 ms                                                 | 80.8 ms: 1.37x faster                                         |
| xml_etree_parse      | 163 ms                                                 | 123 ms: 1.33x faster                                          |
| xml_etree_generate   | 93.8 ms                                                | 73.0 ms: 1.28x faster                                         |
| json_loads           | 28.7 us                                                | 23.7 us: 1.21x faster                                         |
| pickle_list          | 4.72 us                                                | 4.16 us: 1.13x faster                                         |
| unpickle             | 14.2 us                                                | 13.3 us: 1.07x faster                                         |
| unpickle_list        | 4.92 us                                                | 5.03 us: 1.02x slower                                         |
| pickle               | 10.2 us                                                | 10.4 us: 1.02x slower                                         |
| pickle_dict          | 27.6 us                                                | 31.4 us: 1.14x slower                                         |
| Geometric mean       | (ref)                                                  | 1.23x faster                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.06 ms: 1.75x faster                                         |
| python_startup_no_site | 5.78 ms                                                | 5.88 ms: 1.02x slower                                         |
| Geometric mean         | (ref)                                                  | 1.31x faster                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.50 ms: 1.54x faster                                         |
| genshi_text     | 30.6 ms                                                | 20.4 ms: 1.50x faster                                         |
| django_template | 46.3 ms                                                | 32.8 ms: 1.41x faster                                         |
| genshi_xml      | 63.7 ms                                                | 46.2 ms: 1.38x faster                                         |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                  |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_io           | 1.78 sec                                               | 537 ms: 3.31x faster                                          |
| async_tree_none         | 711 ms                                                 | 269 ms: 2.65x faster                                          |
| async_tree_memoization  | 855 ms                                                 | 324 ms: 2.64x faster                                          |
| deltablue               | 7.28 ms                                                | 3.11 ms: 2.34x faster                                         |
| async_tree_cpu_io_mixed | 949 ms                                                 | 474 ms: 2.00x faster                                          |
| logging_silent          | 176 ns                                                 | 91.2 ns: 1.94x faster                                         |
| scimark_sor             | 197 ms                                                 | 104 ms: 1.90x faster                                          |
| richards                | 75.2 ms                                                | 41.1 ms: 1.83x faster                                         |
| float                   | 109 ms                                                 | 61.8 ms: 1.76x faster                                         |
| python_startup          | 14.1 ms                                                | 8.06 ms: 1.75x faster                                         |
| pyflate                 | 676 ms                                                 | 399 ms: 1.70x faster                                          |
| raytrace                | 467 ms                                                 | 282 ms: 1.66x faster                                          |
| scimark_monte_carlo     | 109 ms                                                 | 65.7 ms: 1.65x faster                                         |
| go                      | 226 ms                                                 | 137 ms: 1.65x faster                                          |
| pickle_pure_python      | 452 us                                                 | 282 us: 1.60x faster                                          |
| spectral_norm           | 150 ms                                                 | 93.6 ms: 1.60x faster                                         |
| chaos                   | 106 ms                                                 | 67.6 ms: 1.56x faster                                         |
| pycparser               | 1.53 sec                                               | 983 ms: 1.56x faster                                          |
| crypto_pyaes            | 117 ms                                                 | 75.3 ms: 1.55x faster                                         |
| nbody                   | 144 ms                                                 | 93.2 ms: 1.54x faster                                         |
| mako                    | 14.7 ms                                                | 9.50 ms: 1.54x faster                                         |
| unpickle_pure_python    | 302 us                                                 | 197 us: 1.53x faster                                          |
| hexiom                  | 9.43 ms                                                | 6.18 ms: 1.53x faster                                         |
| deepcopy_memo           | 51.7 us                                                | 33.9 us: 1.52x faster                                         |
| scimark_lu              | 161 ms                                                 | 106 ms: 1.52x faster                                          |
| sqlglot_parse           | 2.04 ms                                                | 1.36 ms: 1.50x faster                                         |
| genshi_text             | 30.6 ms                                                | 20.4 ms: 1.50x faster                                         |
| html5lib                | 85.9 ms                                                | 57.4 ms: 1.50x faster                                         |
| docutils                | 3.18 sec                                               | 2.13 sec: 1.49x faster                                        |
| sqlglot_transpile       | 2.43 ms                                                | 1.65 ms: 1.47x faster                                         |
| chameleon               | 9.17 ms                                                | 6.29 ms: 1.46x faster                                         |
| xml_etree_process       | 74.5 ms                                                | 51.5 ms: 1.45x faster                                         |
| json_dumps              | 13.4 ms                                                | 9.30 ms: 1.45x faster                                         |
| pprint_pformat          | 1.98 sec                                               | 1.40 sec: 1.42x faster                                        |
| logging_simple          | 8.10 us                                                | 5.73 us: 1.41x faster                                         |
| django_template         | 46.3 ms                                                | 32.8 ms: 1.41x faster                                         |
| logging_format          | 8.85 us                                                | 6.33 us: 1.40x faster                                         |
| scimark_fft             | 421 ms                                                 | 302 ms: 1.39x faster                                          |
| pprint_safe_repr        | 953 ms                                                 | 686 ms: 1.39x faster                                          |
| unpack_sequence         | 59.4 ns                                                | 42.8 ns: 1.39x faster                                         |
| thrift                  | 1.03 ms                                                | 747 us: 1.38x faster                                          |
| 2to3                    | 335 ms                                                 | 243 ms: 1.38x faster                                          |
| genshi_xml              | 63.7 ms                                                | 46.2 ms: 1.38x faster                                         |
| xml_etree_iterparse     | 111 ms                                                 | 80.8 ms: 1.37x faster                                         |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.01 ms: 1.36x faster                                         |
| regex_compile           | 177 ms                                                 | 131 ms: 1.36x faster                                          |
| xml_etree_parse         | 163 ms                                                 | 123 ms: 1.33x faster                                          |
| deepcopy                | 438 us                                                 | 331 us: 1.32x faster                                          |
| fannkuch                | 488 ms                                                 | 372 ms: 1.31x faster                                          |
| deepcopy_reduce         | 3.79 us                                                | 2.95 us: 1.29x faster                                         |
| sqlglot_optimize        | 65.2 ms                                                | 50.8 ms: 1.29x faster                                         |
| xml_etree_generate      | 93.8 ms                                                | 73.0 ms: 1.28x faster                                         |
| nqueens                 | 100 ms                                                 | 78.2 ms: 1.28x faster                                         |
| async_generators        | 426 ms                                                 | 334 ms: 1.28x faster                                          |
| sqlglot_normalize       | 134 ms                                                 | 106 ms: 1.26x faster                                          |
| json_loads              | 28.7 us                                                | 23.7 us: 1.21x faster                                         |
| coroutines              | 31.6 ms                                                | 26.1 ms: 1.21x faster                                         |
| bench_thread_pool       | 946 us                                                 | 783 us: 1.21x faster                                          |
| dulwich_log             | 75.8 ms                                                | 63.1 ms: 1.20x faster                                         |
| sympy_integrate         | 24.0 ms                                                | 20.2 ms: 1.19x faster                                         |
| sympy_expand            | 534 ms                                                 | 451 ms: 1.18x faster                                          |
| regex_v8                | 25.0 ms                                                | 21.2 ms: 1.18x faster                                         |
| sympy_str               | 325 ms                                                 | 279 ms: 1.16x faster                                          |
| json                    | 5.35 ms                                                | 4.60 ms: 1.16x faster                                         |
| pathlib                 | 20.0 ms                                                | 17.4 ms: 1.15x faster                                         |
| pickle_list             | 4.72 us                                                | 4.16 us: 1.13x faster                                         |
| sympy_sum               | 183 ms                                                 | 162 ms: 1.13x faster                                          |
| sqlite_synth            | 2.92 us                                                | 2.61 us: 1.12x faster                                         |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.10x faster                                          |
| unpickle                | 14.2 us                                                | 13.3 us: 1.07x faster                                         |
| regex_dna               | 214 ms                                                 | 201 ms: 1.06x faster                                          |
| telco                   | 6.73 ms                                                | 6.41 ms: 1.05x faster                                         |
| mdp                     | 2.74 sec                                               | 2.72 sec: 1.01x faster                                        |
| python_startup_no_site  | 5.78 ms                                                | 5.88 ms: 1.02x slower                                         |
| unpickle_list           | 4.92 us                                                | 5.03 us: 1.02x slower                                         |
| pickle                  | 10.2 us                                                | 10.4 us: 1.02x slower                                         |
| generators              | 76.4 ms                                                | 78.4 ms: 1.03x slower                                         |
| pidigits                | 190 ms                                                 | 198 ms: 1.04x slower                                          |
| regex_effbot            | 3.19 ms                                                | 3.35 ms: 1.05x slower                                         |
| pickle_dict             | 27.6 us                                                | 31.4 us: 1.14x slower                                         |
| coverage                | 74.7 ms                                                | 103 ms: 1.38x slower                                          |
| Geometric mean          | (ref)                                                  | 1.37x faster                                                  |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (13) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, create_gc_cycles, dask, djangocms, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221221-3.12.0a3+-663a965/bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965.json: mypy
