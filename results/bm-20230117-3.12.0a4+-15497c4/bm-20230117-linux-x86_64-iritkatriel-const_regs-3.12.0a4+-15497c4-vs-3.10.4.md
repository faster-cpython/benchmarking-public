
# Results vs. 3.10.4

- fork: iritkatriel
- ref: const_regs
- machine: linux-x86_64
- commit hash: 15497c4
- commit date: 2023-01-17
- overall geometric mean: 1.27x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 258 ms: 1.30x faster                                              |
| chameleon      | 9.06 ms                                                | 6.52 ms: 1.39x faster                                             |
| docutils       | 3.17 sec                                               | 2.60 sec: 1.22x faster                                            |
| html5lib       | 85.9 ms                                                | 60.9 ms: 1.41x faster                                             |
| Geometric mean | (ref)                                                  | 1.33x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 111 ms                                                 | 73.5 ms: 1.50x faster                                             |
| nbody          | 142 ms                                                 | 95.6 ms: 1.48x faster                                             |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x faster                                              |
| Geometric mean | (ref)                                                  | 1.31x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 135 ms: 1.31x faster                                              |
| regex_v8       | 25.0 ms                                                | 22.4 ms: 1.12x faster                                             |
| regex_dna      | 222 ms                                                 | 219 ms: 1.01x faster                                              |
| regex_effbot   | 3.23 ms                                                | 3.60 ms: 1.12x slower                                             |
| Geometric mean | (ref)                                                  | 1.07x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 295 us: 1.54x faster                                              |
| unpickle_pure_python | 300 us                                                 | 207 us: 1.45x faster                                              |
| json_dumps           | 13.5 ms                                                | 9.59 ms: 1.41x faster                                             |
| xml_etree_process    | 74.9 ms                                                | 54.7 ms: 1.37x faster                                             |
| xml_etree_generate   | 94.2 ms                                                | 78.3 ms: 1.20x faster                                             |
| json_loads           | 28.8 us                                                | 24.5 us: 1.18x faster                                             |
| pickle_list          | 4.56 us                                                | 4.06 us: 1.12x faster                                             |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.09x faster                                              |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                              |
| unpickle             | 14.1 us                                                | 13.3 us: 1.06x faster                                             |
| pickle               | 10.3 us                                                | 10.2 us: 1.01x faster                                             |
| unpickle_list        | 4.82 us                                                | 4.92 us: 1.02x slower                                             |
| pickle_dict          | 27.3 us                                                | 30.8 us: 1.13x slower                                             |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.59 ms: 1.65x faster                                             |
| python_startup_no_site | 5.82 ms                                                | 6.10 ms: 1.05x slower                                             |
| Geometric mean         | (ref)                                                  | 1.25x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.77 ms: 1.51x faster                                             |
| genshi_text     | 30.3 ms                                                | 20.9 ms: 1.45x faster                                             |
| django_template | 45.9 ms                                                | 33.9 ms: 1.35x faster                                             |
| genshi_xml      | 63.3 ms                                                | 48.4 ms: 1.31x faster                                             |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                      |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.38 ms: 2.20x faster                                             |
| asyncio_tcp             | 925 ms                                                 | 504 ms: 1.83x faster                                              |
| scimark_sor             | 197 ms                                                 | 109 ms: 1.80x faster                                              |
| logging_silent          | 175 ns                                                 | 97.7 ns: 1.79x faster                                             |
| richards                | 74.9 ms                                                | 43.8 ms: 1.71x faster                                             |
| python_startup          | 14.2 ms                                                | 8.59 ms: 1.65x faster                                             |
| go                      | 229 ms                                                 | 139 ms: 1.65x faster                                              |
| pyflate                 | 673 ms                                                 | 411 ms: 1.64x faster                                              |
| scimark_monte_carlo     | 108 ms                                                 | 68.1 ms: 1.59x faster                                             |
| crypto_pyaes            | 118 ms                                                 | 74.7 ms: 1.59x faster                                             |
| chaos                   | 106 ms                                                 | 67.2 ms: 1.58x faster                                             |
| unpack_sequence         | 64.7 ns                                                | 41.9 ns: 1.54x faster                                             |
| raytrace                | 464 ms                                                 | 301 ms: 1.54x faster                                              |
| pickle_pure_python      | 455 us                                                 | 295 us: 1.54x faster                                              |
| spectral_norm           | 150 ms                                                 | 97.9 ms: 1.53x faster                                             |
| hexiom                  | 9.53 ms                                                | 6.25 ms: 1.52x faster                                             |
| mako                    | 14.8 ms                                                | 9.77 ms: 1.51x faster                                             |
| float                   | 111 ms                                                 | 73.5 ms: 1.50x faster                                             |
| deepcopy_memo           | 52.3 us                                                | 35.2 us: 1.49x faster                                             |
| scimark_lu              | 163 ms                                                 | 110 ms: 1.49x faster                                              |
| nbody                   | 142 ms                                                 | 95.6 ms: 1.48x faster                                             |
| unpickle_pure_python    | 300 us                                                 | 207 us: 1.45x faster                                              |
| genshi_text             | 30.3 ms                                                | 20.9 ms: 1.45x faster                                             |
| json_dumps              | 13.5 ms                                                | 9.59 ms: 1.41x faster                                             |
| html5lib                | 85.9 ms                                                | 60.9 ms: 1.41x faster                                             |
| sqlglot_parse           | 2.06 ms                                                | 1.46 ms: 1.41x faster                                             |
| pprint_pformat          | 1.99 sec                                               | 1.42 sec: 1.40x faster                                            |
| chameleon               | 9.06 ms                                                | 6.52 ms: 1.39x faster                                             |
| sqlglot_transpile       | 2.45 ms                                                | 1.76 ms: 1.39x faster                                             |
| thrift                  | 1.03 ms                                                | 751 us: 1.38x faster                                              |
| pprint_safe_repr        | 955 ms                                                 | 695 ms: 1.37x faster                                              |
| xml_etree_process       | 74.9 ms                                                | 54.7 ms: 1.37x faster                                             |
| logging_simple          | 8.07 us                                                | 5.92 us: 1.36x faster                                             |
| async_tree_none         | 717 ms                                                 | 528 ms: 1.36x faster                                              |
| django_template         | 45.9 ms                                                | 33.9 ms: 1.35x faster                                             |
| logging_format          | 8.91 us                                                | 6.59 us: 1.35x faster                                             |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.06 ms: 1.34x faster                                             |
| scimark_fft             | 424 ms                                                 | 316 ms: 1.34x faster                                              |
| async_tree_io           | 1.77 sec                                               | 1.33 sec: 1.33x faster                                            |
| regex_compile           | 177 ms                                                 | 135 ms: 1.31x faster                                              |
| genshi_xml              | 63.3 ms                                                | 48.4 ms: 1.31x faster                                             |
| pycparser               | 1.50 sec                                               | 1.15 sec: 1.31x faster                                            |
| 2to3                    | 336 ms                                                 | 258 ms: 1.30x faster                                              |
| deepcopy                | 442 us                                                 | 345 us: 1.28x faster                                              |
| fannkuch                | 486 ms                                                 | 380 ms: 1.28x faster                                              |
| async_tree_memoization  | 854 ms                                                 | 670 ms: 1.28x faster                                              |
| deepcopy_reduce         | 3.82 us                                                | 3.02 us: 1.27x faster                                             |
| nqueens                 | 100 ms                                                 | 79.9 ms: 1.25x faster                                             |
| async_tree_cpu_io_mixed | 951 ms                                                 | 762 ms: 1.25x faster                                              |
| sqlglot_optimize        | 65.3 ms                                                | 53.0 ms: 1.23x faster                                             |
| sqlglot_normalize       | 135 ms                                                 | 110 ms: 1.22x faster                                              |
| docutils                | 3.17 sec                                               | 2.60 sec: 1.22x faster                                            |
| async_generators        | 425 ms                                                 | 353 ms: 1.20x faster                                              |
| xml_etree_generate      | 94.2 ms                                                | 78.3 ms: 1.20x faster                                             |
| bench_thread_pool       | 947 us                                                 | 795 us: 1.19x faster                                              |
| coroutines              | 31.8 ms                                                | 26.8 ms: 1.19x faster                                             |
| dulwich_log             | 75.9 ms                                                | 64.1 ms: 1.18x faster                                             |
| json_loads              | 28.8 us                                                | 24.5 us: 1.18x faster                                             |
| create_gc_cycles        | 1.67 ms                                                | 1.43 ms: 1.17x faster                                             |
| json                    | 5.42 ms                                                | 4.67 ms: 1.16x faster                                             |
| sympy_expand            | 545 ms                                                 | 475 ms: 1.15x faster                                              |
| sqlite_synth            | 2.93 us                                                | 2.59 us: 1.13x faster                                             |
| mdp                     | 2.82 sec                                               | 2.50 sec: 1.13x faster                                            |
| sympy_str               | 328 ms                                                 | 291 ms: 1.13x faster                                              |
| pickle_list             | 4.56 us                                                | 4.06 us: 1.12x faster                                             |
| regex_v8                | 25.0 ms                                                | 22.4 ms: 1.12x faster                                             |
| pathlib                 | 20.0 ms                                                | 18.0 ms: 1.11x faster                                             |
| sympy_integrate         | 24.3 ms                                                | 22.1 ms: 1.10x faster                                             |
| sympy_sum               | 185 ms                                                 | 168 ms: 1.10x faster                                              |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.09x faster                                              |
| djangocms               | 35.9 us                                                | 32.8 us: 1.09x faster                                             |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                              |
| meteor_contest          | 115 ms                                                 | 107 ms: 1.07x faster                                              |
| unpickle                | 14.1 us                                                | 13.3 us: 1.06x faster                                             |
| telco                   | 6.54 ms                                                | 6.35 ms: 1.03x faster                                             |
| regex_dna               | 222 ms                                                 | 219 ms: 1.01x faster                                              |
| pickle                  | 10.3 us                                                | 10.2 us: 1.01x faster                                             |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x faster                                              |
| generators              | 76.8 ms                                                | 77.6 ms: 1.01x slower                                             |
| unpickle_list           | 4.82 us                                                | 4.92 us: 1.02x slower                                             |
| python_startup_no_site  | 5.82 ms                                                | 6.10 ms: 1.05x slower                                             |
| gc_traversal            | 3.84 ms                                                | 4.15 ms: 1.08x slower                                             |
| regex_effbot            | 3.23 ms                                                | 3.60 ms: 1.12x slower                                             |
| pickle_dict             | 27.3 us                                                | 30.8 us: 1.13x slower                                             |
| dask                    | 423 ms                                                 | 516 ms: 1.22x slower                                              |
| coverage                | 72.8 ms                                                | 99.1 ms: 1.36x slower                                             |
| Geometric mean          | (ref)                                                  | 1.27x faster                                                      |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, comprehensions, flaskblogging, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230117-3.12.0a4+-15497c4/bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x
