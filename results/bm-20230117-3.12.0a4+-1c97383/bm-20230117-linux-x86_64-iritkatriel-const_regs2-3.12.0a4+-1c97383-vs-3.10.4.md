
# Results vs. 3.10.4

- fork: iritkatriel
- ref: const_regs2
- machine: linux-x86_64
- commit hash: 1c97383
- commit date: 2023-01-17
- overall geometric mean: 1.27x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 259 ms: 1.30x faster                                               |
| chameleon      | 9.06 ms                                                | 6.47 ms: 1.40x faster                                              |
| docutils       | 3.17 sec                                               | 2.61 sec: 1.21x faster                                             |
| html5lib       | 85.9 ms                                                | 60.7 ms: 1.41x faster                                              |
| Geometric mean | (ref)                                                  | 1.33x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 111 ms                                                 | 74.9 ms: 1.47x faster                                              |
| nbody          | 142 ms                                                 | 96.2 ms: 1.47x faster                                              |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                  | 1.28x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 134 ms: 1.32x faster                                               |
| regex_v8       | 25.0 ms                                                | 22.6 ms: 1.11x faster                                              |
| regex_dna      | 222 ms                                                 | 210 ms: 1.06x faster                                               |
| regex_effbot   | 3.23 ms                                                | 3.47 ms: 1.08x slower                                              |
| Geometric mean | (ref)                                                  | 1.09x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 299 us: 1.52x faster                                               |
| unpickle_pure_python | 300 us                                                 | 205 us: 1.47x faster                                               |
| json_dumps           | 13.5 ms                                                | 9.51 ms: 1.42x faster                                              |
| xml_etree_process    | 74.9 ms                                                | 54.9 ms: 1.36x faster                                              |
| xml_etree_generate   | 94.2 ms                                                | 78.8 ms: 1.19x faster                                              |
| json_loads           | 28.8 us                                                | 24.2 us: 1.19x faster                                              |
| pickle_list          | 4.56 us                                                | 4.17 us: 1.09x faster                                              |
| xml_etree_parse      | 163 ms                                                 | 150 ms: 1.09x faster                                               |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                               |
| unpickle             | 14.1 us                                                | 13.5 us: 1.05x faster                                              |
| pickle               | 10.3 us                                                | 10.1 us: 1.02x faster                                              |
| unpickle_list        | 4.82 us                                                | 4.88 us: 1.01x slower                                              |
| pickle_dict          | 27.3 us                                                | 30.7 us: 1.13x slower                                              |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.60 ms: 1.65x faster                                              |
| python_startup_no_site | 5.82 ms                                                | 6.13 ms: 1.05x slower                                              |
| Geometric mean         | (ref)                                                  | 1.25x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.85 ms: 1.50x faster                                              |
| genshi_text     | 30.3 ms                                                | 20.8 ms: 1.46x faster                                              |
| django_template | 45.9 ms                                                | 34.5 ms: 1.33x faster                                              |
| genshi_xml      | 63.3 ms                                                | 47.8 ms: 1.33x faster                                              |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                       |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.42 ms: 2.17x faster                                              |
| asyncio_tcp             | 925 ms                                                 | 505 ms: 1.83x faster                                               |
| logging_silent          | 175 ns                                                 | 98.6 ns: 1.78x faster                                              |
| scimark_sor             | 197 ms                                                 | 111 ms: 1.77x faster                                               |
| richards                | 74.9 ms                                                | 44.4 ms: 1.69x faster                                              |
| python_startup          | 14.2 ms                                                | 8.60 ms: 1.65x faster                                              |
| pyflate                 | 673 ms                                                 | 409 ms: 1.64x faster                                               |
| scimark_monte_carlo     | 108 ms                                                 | 66.1 ms: 1.64x faster                                              |
| go                      | 229 ms                                                 | 141 ms: 1.62x faster                                               |
| crypto_pyaes            | 118 ms                                                 | 75.9 ms: 1.56x faster                                              |
| unpack_sequence         | 64.7 ns                                                | 41.7 ns: 1.55x faster                                              |
| raytrace                | 464 ms                                                 | 301 ms: 1.54x faster                                               |
| chaos                   | 106 ms                                                 | 69.0 ms: 1.54x faster                                              |
| pickle_pure_python      | 455 us                                                 | 299 us: 1.52x faster                                               |
| hexiom                  | 9.53 ms                                                | 6.31 ms: 1.51x faster                                              |
| mako                    | 14.8 ms                                                | 9.85 ms: 1.50x faster                                              |
| spectral_norm           | 150 ms                                                 | 100 ms: 1.50x faster                                               |
| scimark_lu              | 163 ms                                                 | 110 ms: 1.48x faster                                               |
| float                   | 111 ms                                                 | 74.9 ms: 1.47x faster                                              |
| nbody                   | 142 ms                                                 | 96.2 ms: 1.47x faster                                              |
| unpickle_pure_python    | 300 us                                                 | 205 us: 1.47x faster                                               |
| deepcopy_memo           | 52.3 us                                                | 35.8 us: 1.46x faster                                              |
| genshi_text             | 30.3 ms                                                | 20.8 ms: 1.46x faster                                              |
| json_dumps              | 13.5 ms                                                | 9.51 ms: 1.42x faster                                              |
| html5lib                | 85.9 ms                                                | 60.7 ms: 1.41x faster                                              |
| chameleon               | 9.06 ms                                                | 6.47 ms: 1.40x faster                                              |
| sqlglot_parse           | 2.06 ms                                                | 1.48 ms: 1.39x faster                                              |
| pprint_pformat          | 1.99 sec                                               | 1.43 sec: 1.39x faster                                             |
| sqlglot_transpile       | 2.45 ms                                                | 1.78 ms: 1.38x faster                                              |
| thrift                  | 1.03 ms                                                | 753 us: 1.37x faster                                               |
| pprint_safe_repr        | 955 ms                                                 | 697 ms: 1.37x faster                                               |
| xml_etree_process       | 74.9 ms                                                | 54.9 ms: 1.36x faster                                              |
| logging_format          | 8.91 us                                                | 6.57 us: 1.36x faster                                              |
| scimark_fft             | 424 ms                                                 | 315 ms: 1.34x faster                                               |
| async_tree_none         | 717 ms                                                 | 534 ms: 1.34x faster                                               |
| logging_simple          | 8.07 us                                                | 6.01 us: 1.34x faster                                              |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.07 ms: 1.34x faster                                              |
| async_tree_io           | 1.77 sec                                               | 1.33 sec: 1.33x faster                                             |
| django_template         | 45.9 ms                                                | 34.5 ms: 1.33x faster                                              |
| fannkuch                | 486 ms                                                 | 366 ms: 1.33x faster                                               |
| genshi_xml              | 63.3 ms                                                | 47.8 ms: 1.33x faster                                              |
| regex_compile           | 177 ms                                                 | 134 ms: 1.32x faster                                               |
| pycparser               | 1.50 sec                                               | 1.15 sec: 1.30x faster                                             |
| 2to3                    | 336 ms                                                 | 259 ms: 1.30x faster                                               |
| async_tree_memoization  | 854 ms                                                 | 667 ms: 1.28x faster                                               |
| nqueens                 | 100 ms                                                 | 78.9 ms: 1.27x faster                                              |
| deepcopy                | 442 us                                                 | 350 us: 1.26x faster                                               |
| async_tree_cpu_io_mixed | 951 ms                                                 | 765 ms: 1.24x faster                                               |
| sqlglot_normalize       | 135 ms                                                 | 109 ms: 1.24x faster                                               |
| sqlglot_optimize        | 65.3 ms                                                | 53.0 ms: 1.23x faster                                              |
| coroutines              | 31.8 ms                                                | 26.0 ms: 1.22x faster                                              |
| deepcopy_reduce         | 3.82 us                                                | 3.12 us: 1.22x faster                                              |
| docutils                | 3.17 sec                                               | 2.61 sec: 1.21x faster                                             |
| xml_etree_generate      | 94.2 ms                                                | 78.8 ms: 1.19x faster                                              |
| async_generators        | 425 ms                                                 | 356 ms: 1.19x faster                                               |
| json_loads              | 28.8 us                                                | 24.2 us: 1.19x faster                                              |
| bench_thread_pool       | 947 us                                                 | 801 us: 1.18x faster                                               |
| dulwich_log             | 75.9 ms                                                | 64.3 ms: 1.18x faster                                              |
| sympy_expand            | 545 ms                                                 | 470 ms: 1.16x faster                                               |
| json                    | 5.42 ms                                                | 4.74 ms: 1.14x faster                                              |
| create_gc_cycles        | 1.67 ms                                                | 1.46 ms: 1.14x faster                                              |
| sqlite_synth            | 2.93 us                                                | 2.59 us: 1.13x faster                                              |
| sympy_str               | 328 ms                                                 | 291 ms: 1.13x faster                                               |
| meteor_contest          | 115 ms                                                 | 103 ms: 1.11x faster                                               |
| regex_v8                | 25.0 ms                                                | 22.6 ms: 1.11x faster                                              |
| mdp                     | 2.82 sec                                               | 2.55 sec: 1.11x faster                                             |
| djangocms               | 35.9 us                                                | 32.6 us: 1.10x faster                                              |
| sympy_sum               | 185 ms                                                 | 168 ms: 1.10x faster                                               |
| sympy_integrate         | 24.3 ms                                                | 22.1 ms: 1.10x faster                                              |
| pathlib                 | 20.0 ms                                                | 18.3 ms: 1.09x faster                                              |
| pickle_list             | 4.56 us                                                | 4.17 us: 1.09x faster                                              |
| xml_etree_parse         | 163 ms                                                 | 150 ms: 1.09x faster                                               |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                               |
| regex_dna               | 222 ms                                                 | 210 ms: 1.06x faster                                               |
| unpickle                | 14.1 us                                                | 13.5 us: 1.05x faster                                              |
| pickle                  | 10.3 us                                                | 10.1 us: 1.02x faster                                              |
| telco                   | 6.54 ms                                                | 6.41 ms: 1.02x faster                                              |
| unpickle_list           | 4.82 us                                                | 4.88 us: 1.01x slower                                              |
| pidigits                | 190 ms                                                 | 198 ms: 1.04x slower                                               |
| generators              | 76.8 ms                                                | 79.9 ms: 1.04x slower                                              |
| python_startup_no_site  | 5.82 ms                                                | 6.13 ms: 1.05x slower                                              |
| regex_effbot            | 3.23 ms                                                | 3.47 ms: 1.08x slower                                              |
| gc_traversal            | 3.84 ms                                                | 4.29 ms: 1.12x slower                                              |
| pickle_dict             | 27.3 us                                                | 30.7 us: 1.13x slower                                              |
| dask                    | 423 ms                                                 | 519 ms: 1.23x slower                                               |
| coverage                | 72.8 ms                                                | 101 ms: 1.39x slower                                               |
| Geometric mean          | (ref)                                                  | 1.27x faster                                                       |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, comprehensions, flaskblogging, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230117-3.12.0a4+-1c97383/bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x
