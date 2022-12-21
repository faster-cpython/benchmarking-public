Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 243 ms: 1.06x faster                                          |
| chameleon      | 6.41 ms                                                | 6.29 ms: 1.02x faster                                         |
| docutils       | 2.60 sec                                               | 2.13 sec: 1.22x faster                                        |
| html5lib       | 63.2 ms                                                | 57.4 ms: 1.10x faster                                         |
| Geometric mean | (ref)                                                  | 1.10x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 76.3 ms                                                | 61.8 ms: 1.24x faster                                         |
| nbody          | 95.0 ms                                                | 93.2 ms: 1.02x faster                                         |
| pidigits       | 199 ms                                                 | 198 ms: 1.01x faster                                          |
| Geometric mean | (ref)                                                  | 1.08x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 131 ms: 1.04x faster                                          |
| regex_dna      | 203 ms                                                 | 201 ms: 1.01x faster                                          |
| regex_v8       | 22.3 ms                                                | 21.2 ms: 1.05x faster                                         |
| Geometric mean | (ref)                                                  | 1.03x faster                                                  |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.30 ms: 1.36x faster                                         |
| json_loads           | 26.2 us                                                | 23.7 us: 1.11x faster                                         |
| pickle               | 9.79 us                                                | 10.4 us: 1.06x slower                                         |
| pickle_pure_python   | 304 us                                                 | 282 us: 1.08x faster                                          |
| unpickle_list        | 4.95 us                                                | 5.03 us: 1.02x slower                                         |
| unpickle_pure_python | 225 us                                                 | 197 us: 1.14x faster                                          |
| xml_etree_parse      | 158 ms                                                 | 123 ms: 1.29x faster                                          |
| xml_etree_iterparse  | 103 ms                                                 | 80.8 ms: 1.27x faster                                         |
| xml_etree_generate   | 76.2 ms                                                | 73.0 ms: 1.04x faster                                         |
| xml_etree_process    | 53.8 ms                                                | 51.5 ms: 1.04x faster                                         |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                  |

Benchmark hidden because not significant (3): pickle_dict, pickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.06 ms: 1.04x faster                                         |
| python_startup_no_site | 5.96 ms                                                | 5.88 ms: 1.02x faster                                         |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| django_template | 32.5 ms                                                | 32.8 ms: 1.01x slower                                         |
| genshi_text     | 22.1 ms                                                | 20.4 ms: 1.08x faster                                         |
| genshi_xml      | 52.1 ms                                                | 46.2 ms: 1.13x faster                                         |
| mako            | 9.85 ms                                                | 9.50 ms: 1.04x faster                                         |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                  |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3                    | 257 ms                                                 | 243 ms: 1.06x faster                                          |
| async_generators        | 359 ms                                                 | 334 ms: 1.08x faster                                          |
| async_tree_none         | 529 ms                                                 | 269 ms: 1.97x faster                                          |
| async_tree_cpu_io_mixed | 752 ms                                                 | 474 ms: 1.59x faster                                          |
| async_tree_io           | 1.31 sec                                               | 537 ms: 2.43x faster                                          |
| async_tree_memoization  | 625 ms                                                 | 324 ms: 1.93x faster                                          |
| chameleon               | 6.41 ms                                                | 6.29 ms: 1.02x faster                                         |
| chaos                   | 68.6 ms                                                | 67.6 ms: 1.02x faster                                         |
| bench_thread_pool       | 810 us                                                 | 783 us: 1.03x faster                                          |
| coverage                | 101 ms                                                 | 103 ms: 1.02x slower                                          |
| crypto_pyaes            | 73.9 ms                                                | 75.3 ms: 1.02x slower                                         |
| deepcopy                | 344 us                                                 | 331 us: 1.04x faster                                          |
| deepcopy_reduce         | 2.97 us                                                | 2.95 us: 1.01x faster                                         |
| deepcopy_memo           | 36.4 us                                                | 33.9 us: 1.07x faster                                         |
| deltablue               | 3.64 ms                                                | 3.11 ms: 1.17x faster                                         |
| django_template         | 32.5 ms                                                | 32.8 ms: 1.01x slower                                         |
| docutils                | 2.60 sec                                               | 2.13 sec: 1.22x faster                                        |
| dulwich_log             | 63.9 ms                                                | 63.1 ms: 1.01x faster                                         |
| fannkuch                | 388 ms                                                 | 372 ms: 1.04x faster                                          |
| float                   | 76.3 ms                                                | 61.8 ms: 1.24x faster                                         |
| generators              | 72.2 ms                                                | 78.4 ms: 1.09x slower                                         |
| genshi_text             | 22.1 ms                                                | 20.4 ms: 1.08x faster                                         |
| genshi_xml              | 52.1 ms                                                | 46.2 ms: 1.13x faster                                         |
| go                      | 143 ms                                                 | 137 ms: 1.05x faster                                          |
| hexiom                  | 6.35 ms                                                | 6.18 ms: 1.03x faster                                         |
| html5lib                | 63.2 ms                                                | 57.4 ms: 1.10x faster                                         |
| json                    | 4.95 ms                                                | 4.60 ms: 1.08x faster                                         |
| json_dumps              | 12.7 ms                                                | 9.30 ms: 1.36x faster                                         |
| json_loads              | 26.2 us                                                | 23.7 us: 1.11x faster                                         |
| logging_format          | 6.62 us                                                | 6.33 us: 1.04x faster                                         |
| logging_silent          | 98.5 ns                                                | 91.2 ns: 1.08x faster                                         |
| logging_simple          | 6.06 us                                                | 5.73 us: 1.06x faster                                         |
| mako                    | 9.85 ms                                                | 9.50 ms: 1.04x faster                                         |
| mdp                     | 2.62 sec                                               | 2.72 sec: 1.04x slower                                        |
| meteor_contest          | 105 ms                                                 | 104 ms: 1.01x faster                                          |
| mypy                    | 669 ms                                                 | 610 ms: 1.10x faster                                          |
| nbody                   | 95.0 ms                                                | 93.2 ms: 1.02x faster                                         |
| nqueens                 | 85.0 ms                                                | 78.2 ms: 1.09x faster                                         |
| pathlib                 | 18.2 ms                                                | 17.4 ms: 1.04x faster                                         |
| pickle                  | 9.79 us                                                | 10.4 us: 1.06x slower                                         |
| pickle_pure_python      | 304 us                                                 | 282 us: 1.08x faster                                          |
| pidigits                | 199 ms                                                 | 198 ms: 1.01x faster                                          |
| pprint_safe_repr        | 691 ms                                                 | 686 ms: 1.01x faster                                          |
| pprint_pformat          | 1.44 sec                                               | 1.40 sec: 1.03x faster                                        |
| pycparser               | 1.17 sec                                               | 983 ms: 1.19x faster                                          |
| pyflate                 | 417 ms                                                 | 399 ms: 1.05x faster                                          |
| python_startup          | 8.36 ms                                                | 8.06 ms: 1.04x faster                                         |
| python_startup_no_site  | 5.96 ms                                                | 5.88 ms: 1.02x faster                                         |
| raytrace                | 290 ms                                                 | 282 ms: 1.03x faster                                          |
| regex_compile           | 136 ms                                                 | 131 ms: 1.04x faster                                          |
| regex_dna               | 203 ms                                                 | 201 ms: 1.01x faster                                          |
| regex_v8                | 22.3 ms                                                | 21.2 ms: 1.05x faster                                         |
| richards                | 46.2 ms                                                | 41.1 ms: 1.12x faster                                         |
| scimark_fft             | 329 ms                                                 | 302 ms: 1.09x faster                                          |
| scimark_lu              | 107 ms                                                 | 106 ms: 1.01x faster                                          |
| scimark_monte_carlo     | 68.3 ms                                                | 65.7 ms: 1.04x faster                                         |
| scimark_sor             | 115 ms                                                 | 104 ms: 1.11x faster                                          |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.01 ms: 1.10x faster                                         |
| spectral_norm           | 99.9 ms                                                | 93.6 ms: 1.07x faster                                         |
| sqlglot_parse           | 1.37 ms                                                | 1.36 ms: 1.01x faster                                         |
| sqlglot_transpile       | 1.66 ms                                                | 1.65 ms: 1.01x faster                                         |
| sqlglot_optimize        | 53.0 ms                                                | 50.8 ms: 1.04x faster                                         |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.01x faster                                          |
| sqlite_synth            | 2.49 us                                                | 2.61 us: 1.05x slower                                         |
| sympy_expand            | 472 ms                                                 | 451 ms: 1.05x faster                                          |
| sympy_integrate         | 20.9 ms                                                | 20.2 ms: 1.03x faster                                         |
| sympy_sum               | 166 ms                                                 | 162 ms: 1.03x faster                                          |
| sympy_str               | 287 ms                                                 | 279 ms: 1.03x faster                                          |
| telco                   | 6.62 ms                                                | 6.41 ms: 1.03x faster                                         |
| thrift                  | 752 us                                                 | 747 us: 1.01x faster                                          |
| unpack_sequence         | 43.4 ns                                                | 42.8 ns: 1.02x faster                                         |
| unpickle_list           | 4.95 us                                                | 5.03 us: 1.02x slower                                         |
| unpickle_pure_python    | 225 us                                                 | 197 us: 1.14x faster                                          |
| xml_etree_parse         | 158 ms                                                 | 123 ms: 1.29x faster                                          |
| xml_etree_iterparse     | 103 ms                                                 | 80.8 ms: 1.27x faster                                         |
| xml_etree_generate      | 76.2 ms                                                | 73.0 ms: 1.04x faster                                         |
| xml_etree_process       | 53.8 ms                                                | 51.5 ms: 1.04x faster                                         |
| Geometric mean          | (ref)                                                  | 1.08x faster                                                  |

Benchmark hidden because not significant (6): bench_mp_pool, coroutines, pickle_dict, pickle_list, regex_effbot, unpickle
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
