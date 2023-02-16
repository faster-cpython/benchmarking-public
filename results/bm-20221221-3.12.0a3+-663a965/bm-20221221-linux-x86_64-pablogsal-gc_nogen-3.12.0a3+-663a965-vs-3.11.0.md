
# Results vs. 3.11.0

- fork: pablogsal
- ref: gc_nogen
- machine: linux-x86_64
- commit hash: 663a965
- commit date: 2022-12-21
- overall geometric mean: 1.08x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 243 ms: 1.07x faster                                          |
| chameleon      | 6.38 ms                                                | 6.29 ms: 1.01x faster                                         |
| docutils       | 2.60 sec                                               | 2.13 sec: 1.22x faster                                        |
| html5lib       | 64.8 ms                                                | 57.4 ms: 1.13x faster                                         |
| Geometric mean | (ref)                                                  | 1.10x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 76.8 ms                                                | 61.8 ms: 1.24x faster                                         |
| pidigits       | 197 ms                                                 | 198 ms: 1.00x slower                                          |
| nbody          | 90.0 ms                                                | 93.2 ms: 1.04x slower                                         |
| Geometric mean | (ref)                                                  | 1.06x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_v8       | 22.2 ms                                                | 21.2 ms: 1.05x faster                                         |
| regex_compile  | 136 ms                                                 | 131 ms: 1.04x faster                                          |
| regex_effbot   | 3.46 ms                                                | 3.35 ms: 1.03x faster                                         |
| regex_dna      | 203 ms                                                 | 201 ms: 1.01x faster                                          |
| Geometric mean | (ref)                                                  | 1.03x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.30 ms: 1.33x faster                                         |
| xml_etree_parse      | 160 ms                                                 | 123 ms: 1.31x faster                                          |
| xml_etree_iterparse  | 104 ms                                                 | 80.8 ms: 1.29x faster                                         |
| unpickle_pure_python | 227 us                                                 | 197 us: 1.15x faster                                          |
| json_loads           | 26.1 us                                                | 23.7 us: 1.10x faster                                         |
| pickle_pure_python   | 308 us                                                 | 282 us: 1.09x faster                                          |
| xml_etree_process    | 53.7 ms                                                | 51.5 ms: 1.04x faster                                         |
| xml_etree_generate   | 75.9 ms                                                | 73.0 ms: 1.04x faster                                         |
| pickle_dict          | 31.2 us                                                | 31.4 us: 1.01x slower                                         |
| unpickle_list        | 4.99 us                                                | 5.03 us: 1.01x slower                                         |
| pickle               | 9.90 us                                                | 10.4 us: 1.05x slower                                         |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                  |

Benchmark hidden because not significant (2): unpickle, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.06 ms: 1.06x faster                                         |
| python_startup_no_site | 6.04 ms                                                | 5.88 ms: 1.03x faster                                         |
| Geometric mean         | (ref)                                                  | 1.05x faster                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 46.2 ms: 1.11x faster                                         |
| genshi_text     | 21.5 ms                                                | 20.4 ms: 1.05x faster                                         |
| mako            | 9.83 ms                                                | 9.50 ms: 1.03x faster                                         |
| django_template | 32.3 ms                                                | 32.8 ms: 1.01x slower                                         |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                  |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_io           | 1.30 sec                                               | 537 ms: 2.42x faster                                          |
| async_tree_none         | 526 ms                                                 | 269 ms: 1.96x faster                                          |
| async_tree_memoization  | 624 ms                                                 | 324 ms: 1.92x faster                                          |
| async_tree_cpu_io_mixed | 736 ms                                                 | 474 ms: 1.55x faster                                          |
| json_dumps              | 12.4 ms                                                | 9.30 ms: 1.33x faster                                         |
| xml_etree_parse         | 160 ms                                                 | 123 ms: 1.31x faster                                          |
| xml_etree_iterparse     | 104 ms                                                 | 80.8 ms: 1.29x faster                                         |
| float                   | 76.8 ms                                                | 61.8 ms: 1.24x faster                                         |
| docutils                | 2.60 sec                                               | 2.13 sec: 1.22x faster                                        |
| pycparser               | 1.19 sec                                               | 983 ms: 1.21x faster                                          |
| deltablue               | 3.66 ms                                                | 3.11 ms: 1.18x faster                                         |
| unpickle_pure_python    | 227 us                                                 | 197 us: 1.15x faster                                          |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.01 ms: 1.14x faster                                         |
| html5lib                | 64.8 ms                                                | 57.4 ms: 1.13x faster                                         |
| richards                | 46.1 ms                                                | 41.1 ms: 1.12x faster                                         |
| genshi_xml              | 51.4 ms                                                | 46.2 ms: 1.11x faster                                         |
| scimark_sor             | 115 ms                                                 | 104 ms: 1.11x faster                                          |
| json_loads              | 26.1 us                                                | 23.7 us: 1.10x faster                                         |
| pickle_pure_python      | 308 us                                                 | 282 us: 1.09x faster                                          |
| scimark_fft             | 325 ms                                                 | 302 ms: 1.08x faster                                          |
| logging_silent          | 98.0 ns                                                | 91.2 ns: 1.07x faster                                         |
| nqueens                 | 83.8 ms                                                | 78.2 ms: 1.07x faster                                         |
| async_generators        | 356 ms                                                 | 334 ms: 1.07x faster                                          |
| 2to3                    | 259 ms                                                 | 243 ms: 1.07x faster                                          |
| python_startup          | 8.58 ms                                                | 8.06 ms: 1.06x faster                                         |
| json                    | 4.87 ms                                                | 4.60 ms: 1.06x faster                                         |
| deepcopy_memo           | 35.8 us                                                | 33.9 us: 1.06x faster                                         |
| sympy_expand            | 475 ms                                                 | 451 ms: 1.05x faster                                          |
| genshi_text             | 21.5 ms                                                | 20.4 ms: 1.05x faster                                         |
| pyflate                 | 419 ms                                                 | 399 ms: 1.05x faster                                          |
| logging_simple          | 6.02 us                                                | 5.73 us: 1.05x faster                                         |
| spectral_norm           | 98.1 ms                                                | 93.6 ms: 1.05x faster                                         |
| regex_v8                | 22.2 ms                                                | 21.2 ms: 1.05x faster                                         |
| regex_compile           | 136 ms                                                 | 131 ms: 1.04x faster                                          |
| bench_thread_pool       | 817 us                                                 | 783 us: 1.04x faster                                          |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                        |
| xml_etree_process       | 53.7 ms                                                | 51.5 ms: 1.04x faster                                         |
| sympy_str               | 291 ms                                                 | 279 ms: 1.04x faster                                          |
| unpack_sequence         | 44.5 ns                                                | 42.8 ns: 1.04x faster                                         |
| xml_etree_generate      | 75.9 ms                                                | 73.0 ms: 1.04x faster                                         |
| sqlglot_optimize        | 52.7 ms                                                | 50.8 ms: 1.04x faster                                         |
| sympy_integrate         | 21.0 ms                                                | 20.2 ms: 1.04x faster                                         |
| pathlib                 | 18.1 ms                                                | 17.4 ms: 1.04x faster                                         |
| mako                    | 9.83 ms                                                | 9.50 ms: 1.03x faster                                         |
| scimark_monte_carlo     | 68.0 ms                                                | 65.7 ms: 1.03x faster                                         |
| raytrace                | 291 ms                                                 | 282 ms: 1.03x faster                                          |
| fannkuch                | 384 ms                                                 | 372 ms: 1.03x faster                                          |
| deepcopy                | 341 us                                                 | 331 us: 1.03x faster                                          |
| regex_effbot            | 3.46 ms                                                | 3.35 ms: 1.03x faster                                         |
| pprint_safe_repr        | 706 ms                                                 | 686 ms: 1.03x faster                                          |
| python_startup_no_site  | 6.04 ms                                                | 5.88 ms: 1.03x faster                                         |
| go                      | 140 ms                                                 | 137 ms: 1.03x faster                                          |
| hexiom                  | 6.34 ms                                                | 6.18 ms: 1.03x faster                                         |
| sympy_sum               | 166 ms                                                 | 162 ms: 1.03x faster                                          |
| deepcopy_reduce         | 3.02 us                                                | 2.95 us: 1.02x faster                                         |
| logging_format          | 6.48 us                                                | 6.33 us: 1.02x faster                                         |
| scimark_lu              | 108 ms                                                 | 106 ms: 1.02x faster                                          |
| thrift                  | 760 us                                                 | 747 us: 1.02x faster                                          |
| chaos                   | 68.7 ms                                                | 67.6 ms: 1.02x faster                                         |
| chameleon               | 6.38 ms                                                | 6.29 ms: 1.01x faster                                         |
| dulwich_log             | 64.0 ms                                                | 63.1 ms: 1.01x faster                                         |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.01x faster                                          |
| regex_dna               | 203 ms                                                 | 201 ms: 1.01x faster                                          |
| crypto_pyaes            | 75.7 ms                                                | 75.3 ms: 1.01x faster                                         |
| pidigits                | 197 ms                                                 | 198 ms: 1.00x slower                                          |
| pickle_dict             | 31.2 us                                                | 31.4 us: 1.01x slower                                         |
| unpickle_list           | 4.99 us                                                | 5.03 us: 1.01x slower                                         |
| django_template         | 32.3 ms                                                | 32.8 ms: 1.01x slower                                         |
| mdp                     | 2.63 sec                                               | 2.72 sec: 1.03x slower                                        |
| nbody                   | 90.0 ms                                                | 93.2 ms: 1.04x slower                                         |
| coverage                | 99.3 ms                                                | 103 ms: 1.04x slower                                          |
| pickle                  | 9.90 us                                                | 10.4 us: 1.05x slower                                         |
| sqlite_synth            | 2.48 us                                                | 2.61 us: 1.05x slower                                         |
| generators              | 73.5 ms                                                | 78.4 ms: 1.07x slower                                         |
| Geometric mean          | (ref)                                                  | 1.08x faster                                                  |

Benchmark hidden because not significant (8): meteor_contest, telco, sqlglot_transpile, coroutines, sqlglot_parse, bench_mp_pool, unpickle, pickle_list
Ignored benchmarks (13) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, create_gc_cycles, dask, djangocms, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221221-3.12.0a3+-663a965/bm-20221221-linux-x86_64-pablogsal-gc_nogen-3.12.0a3+-663a965.json: mypy
