
# Results vs. 3.10.4

- fork: iritkatriel
- ref: const_regs
- machine: linux-x86_64
- commit hash: 80ea135
- commit date: 2023-01-16
- overall geometric mean: 1.27x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-80ea135 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 259 ms: 1.30x faster                                              |
| chameleon      | 9.06 ms                                                | 6.33 ms: 1.43x faster                                             |
| docutils       | 3.17 sec                                               | 2.62 sec: 1.21x faster                                            |
| html5lib       | 85.9 ms                                                | 61.5 ms: 1.40x faster                                             |
| Geometric mean | (ref)                                                  | 1.33x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-80ea135 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 111 ms                                                 | 74.1 ms: 1.49x faster                                             |
| nbody          | 142 ms                                                 | 96.2 ms: 1.47x faster                                             |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                              |
| Geometric mean | (ref)                                                  | 1.28x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-80ea135 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 134 ms: 1.32x faster                                              |
| regex_v8       | 25.0 ms                                                | 22.2 ms: 1.13x faster                                             |
| regex_dna      | 222 ms                                                 | 217 ms: 1.02x faster                                              |
| regex_effbot   | 3.23 ms                                                | 3.63 ms: 1.12x slower                                             |
| Geometric mean | (ref)                                                  | 1.08x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-80ea135 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 297 us: 1.53x faster                                              |
| unpickle_pure_python | 300 us                                                 | 203 us: 1.48x faster                                              |
| json_dumps           | 13.5 ms                                                | 9.44 ms: 1.43x faster                                             |
| xml_etree_process    | 74.9 ms                                                | 54.5 ms: 1.37x faster                                             |
| xml_etree_generate   | 94.2 ms                                                | 78.4 ms: 1.20x faster                                             |
| json_loads           | 28.8 us                                                | 24.1 us: 1.20x faster                                             |
| pickle_list          | 4.56 us                                                | 4.07 us: 1.12x faster                                             |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.09x faster                                              |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.09x faster                                              |
| unpickle             | 14.1 us                                                | 13.2 us: 1.07x faster                                             |
| pickle               | 10.3 us                                                | 10.2 us: 1.01x faster                                             |
| unpickle_list        | 4.82 us                                                | 5.00 us: 1.04x slower                                             |
| pickle_dict          | 27.3 us                                                | 31.1 us: 1.14x slower                                             |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-80ea135 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.57 ms: 1.65x faster                                             |
| python_startup_no_site | 5.82 ms                                                | 6.11 ms: 1.05x slower                                             |
| Geometric mean         | (ref)                                                  | 1.25x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-80ea135 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.60 ms: 1.54x faster                                             |
| genshi_text     | 30.3 ms                                                | 21.2 ms: 1.43x faster                                             |
| django_template | 45.9 ms                                                | 34.3 ms: 1.34x faster                                             |
| genshi_xml      | 63.3 ms                                                | 47.6 ms: 1.33x faster                                             |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                      |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-80ea135 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.39 ms: 2.19x faster                                             |
| asyncio_tcp             | 925 ms                                                 | 504 ms: 1.84x faster                                              |
| scimark_sor             | 197 ms                                                 | 110 ms: 1.78x faster                                              |
| logging_silent          | 175 ns                                                 | 99.3 ns: 1.76x faster                                             |
| richards                | 74.9 ms                                                | 44.3 ms: 1.69x faster                                             |
| pyflate                 | 673 ms                                                 | 402 ms: 1.67x faster                                              |
| scimark_monte_carlo     | 108 ms                                                 | 65.1 ms: 1.66x faster                                             |
| python_startup          | 14.2 ms                                                | 8.57 ms: 1.65x faster                                             |
| go                      | 229 ms                                                 | 141 ms: 1.62x faster                                              |
| raytrace                | 464 ms                                                 | 298 ms: 1.56x faster                                              |
| crypto_pyaes            | 118 ms                                                 | 76.8 ms: 1.54x faster                                             |
| chaos                   | 106 ms                                                 | 69.0 ms: 1.54x faster                                             |
| mako                    | 14.8 ms                                                | 9.60 ms: 1.54x faster                                             |
| pickle_pure_python      | 455 us                                                 | 297 us: 1.53x faster                                              |
| spectral_norm           | 150 ms                                                 | 98.1 ms: 1.53x faster                                             |
| hexiom                  | 9.53 ms                                                | 6.31 ms: 1.51x faster                                             |
| float                   | 111 ms                                                 | 74.1 ms: 1.49x faster                                             |
| unpickle_pure_python    | 300 us                                                 | 203 us: 1.48x faster                                              |
| nbody                   | 142 ms                                                 | 96.2 ms: 1.47x faster                                             |
| deepcopy_memo           | 52.3 us                                                | 35.6 us: 1.47x faster                                             |
| scimark_lu              | 163 ms                                                 | 111 ms: 1.47x faster                                              |
| unpack_sequence         | 64.7 ns                                                | 44.5 ns: 1.45x faster                                             |
| json_dumps              | 13.5 ms                                                | 9.44 ms: 1.43x faster                                             |
| chameleon               | 9.06 ms                                                | 6.33 ms: 1.43x faster                                             |
| genshi_text             | 30.3 ms                                                | 21.2 ms: 1.43x faster                                             |
| pprint_pformat          | 1.99 sec                                               | 1.40 sec: 1.41x faster                                            |
| sqlglot_parse           | 2.06 ms                                                | 1.47 ms: 1.40x faster                                             |
| html5lib                | 85.9 ms                                                | 61.5 ms: 1.40x faster                                             |
| thrift                  | 1.03 ms                                                | 745 us: 1.39x faster                                              |
| pprint_safe_repr        | 955 ms                                                 | 689 ms: 1.39x faster                                              |
| sqlglot_transpile       | 2.45 ms                                                | 1.77 ms: 1.38x faster                                             |
| xml_etree_process       | 74.9 ms                                                | 54.5 ms: 1.37x faster                                             |
| logging_simple          | 8.07 us                                                | 5.89 us: 1.37x faster                                             |
| logging_format          | 8.91 us                                                | 6.51 us: 1.37x faster                                             |
| scimark_fft             | 424 ms                                                 | 311 ms: 1.36x faster                                              |
| async_tree_none         | 717 ms                                                 | 527 ms: 1.36x faster                                              |
| django_template         | 45.9 ms                                                | 34.3 ms: 1.34x faster                                             |
| async_tree_io           | 1.77 sec                                               | 1.33 sec: 1.33x faster                                            |
| genshi_xml              | 63.3 ms                                                | 47.6 ms: 1.33x faster                                             |
| fannkuch                | 486 ms                                                 | 366 ms: 1.33x faster                                              |
| regex_compile           | 177 ms                                                 | 134 ms: 1.32x faster                                              |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.15 ms: 1.31x faster                                             |
| 2to3                    | 336 ms                                                 | 259 ms: 1.30x faster                                              |
| pycparser               | 1.50 sec                                               | 1.16 sec: 1.30x faster                                            |
| deepcopy                | 442 us                                                 | 343 us: 1.29x faster                                              |
| async_tree_memoization  | 854 ms                                                 | 668 ms: 1.28x faster                                              |
| nqueens                 | 100 ms                                                 | 79.3 ms: 1.26x faster                                             |
| deepcopy_reduce         | 3.82 us                                                | 3.05 us: 1.26x faster                                             |
| async_tree_cpu_io_mixed | 951 ms                                                 | 760 ms: 1.25x faster                                              |
| sqlglot_normalize       | 135 ms                                                 | 109 ms: 1.25x faster                                              |
| sqlglot_optimize        | 65.3 ms                                                | 52.7 ms: 1.24x faster                                             |
| coroutines              | 31.8 ms                                                | 25.8 ms: 1.23x faster                                             |
| docutils                | 3.17 sec                                               | 2.62 sec: 1.21x faster                                            |
| xml_etree_generate      | 94.2 ms                                                | 78.4 ms: 1.20x faster                                             |
| json_loads              | 28.8 us                                                | 24.1 us: 1.20x faster                                             |
| dulwich_log             | 75.9 ms                                                | 63.5 ms: 1.20x faster                                             |
| bench_thread_pool       | 947 us                                                 | 794 us: 1.19x faster                                              |
| async_generators        | 425 ms                                                 | 359 ms: 1.18x faster                                              |
| json                    | 5.42 ms                                                | 4.65 ms: 1.17x faster                                             |
| sympy_expand            | 545 ms                                                 | 473 ms: 1.15x faster                                              |
| create_gc_cycles        | 1.67 ms                                                | 1.46 ms: 1.14x faster                                             |
| sqlite_synth            | 2.93 us                                                | 2.59 us: 1.13x faster                                             |
| sympy_str               | 328 ms                                                 | 291 ms: 1.13x faster                                              |
| regex_v8                | 25.0 ms                                                | 22.2 ms: 1.13x faster                                             |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                             |
| pickle_list             | 4.56 us                                                | 4.07 us: 1.12x faster                                             |
| meteor_contest          | 115 ms                                                 | 103 ms: 1.11x faster                                              |
| djangocms               | 35.9 us                                                | 32.5 us: 1.10x faster                                             |
| sympy_sum               | 185 ms                                                 | 168 ms: 1.10x faster                                              |
| sympy_integrate         | 24.3 ms                                                | 22.1 ms: 1.10x faster                                             |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.09x faster                                              |
| mdp                     | 2.82 sec                                               | 2.59 sec: 1.09x faster                                            |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.09x faster                                              |
| unpickle                | 14.1 us                                                | 13.2 us: 1.07x faster                                             |
| telco                   | 6.54 ms                                                | 6.28 ms: 1.04x faster                                             |
| regex_dna               | 222 ms                                                 | 217 ms: 1.02x faster                                              |
| pickle                  | 10.3 us                                                | 10.2 us: 1.01x faster                                             |
| gc_traversal            | 3.84 ms                                                | 3.80 ms: 1.01x faster                                             |
| generators              | 76.8 ms                                                | 76.1 ms: 1.01x faster                                             |
| unpickle_list           | 4.82 us                                                | 5.00 us: 1.04x slower                                             |
| pidigits                | 190 ms                                                 | 198 ms: 1.04x slower                                              |
| python_startup_no_site  | 5.82 ms                                                | 6.11 ms: 1.05x slower                                             |
| regex_effbot            | 3.23 ms                                                | 3.63 ms: 1.12x slower                                             |
| pickle_dict             | 27.3 us                                                | 31.1 us: 1.14x slower                                             |
| dask                    | 423 ms                                                 | 518 ms: 1.23x slower                                              |
| coverage                | 72.8 ms                                                | 97.7 ms: 1.34x slower                                             |
| Geometric mean          | (ref)                                                  | 1.27x faster                                                      |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, comprehensions, flaskblogging, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230116-3.12.0a4+-80ea135/bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-80ea135.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x
