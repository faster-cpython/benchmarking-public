
# Results vs. 3.10.4

- fork: python
- ref: v3.11.1
- machine: linux-x86_64
- commit hash: a7a450f
- commit date: 2022-12-06
- overall geometric mean: 1.25x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 258 ms: 1.30x faster                                   |
| chameleon      | 9.06 ms                                                | 6.63 ms: 1.37x faster                                  |
| docutils       | 3.17 sec                                               | 2.57 sec: 1.24x faster                                 |
| html5lib       | 85.9 ms                                                | 63.4 ms: 1.35x faster                                  |
| tornado_http   | 127 ms                                                 | 99.8 ms: 1.28x faster                                  |
| Geometric mean | (ref)                                                  | 1.31x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 142 ms                                                 | 95.4 ms: 1.48x faster                                  |
| float          | 111 ms                                                 | 76.0 ms: 1.45x faster                                  |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.29x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 137 ms: 1.29x faster                                   |
| regex_v8       | 25.0 ms                                                | 22.3 ms: 1.12x faster                                  |
| regex_dna      | 222 ms                                                 | 200 ms: 1.11x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.31 ms: 1.03x slower                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 310 us: 1.47x faster                                   |
| xml_etree_process    | 74.9 ms                                                | 53.7 ms: 1.39x faster                                  |
| unpickle_pure_python | 300 us                                                 | 229 us: 1.31x faster                                   |
| xml_etree_generate   | 94.2 ms                                                | 76.6 ms: 1.23x faster                                  |
| json_loads           | 28.8 us                                                | 24.0 us: 1.20x faster                                  |
| pickle_list          | 4.56 us                                                | 4.17 us: 1.09x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                   |
| json_dumps           | 13.5 ms                                                | 12.6 ms: 1.07x faster                                  |
| pickle               | 10.3 us                                                | 9.72 us: 1.06x faster                                  |
| unpickle             | 14.1 us                                                | 13.4 us: 1.06x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 158 ms: 1.03x faster                                   |
| unpickle_list        | 4.82 us                                                | 4.95 us: 1.03x slower                                  |
| pickle_dict          | 27.3 us                                                | 31.1 us: 1.14x slower                                  |
| Geometric mean       | (ref)                                                  | 1.13x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.49 ms: 1.67x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 5.98 ms: 1.03x slower                                  |
| Geometric mean         | (ref)                                                  | 1.27x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.92 ms: 1.49x faster                                  |
| django_template | 45.9 ms                                                | 33.2 ms: 1.38x faster                                  |
| genshi_text     | 30.3 ms                                                | 22.1 ms: 1.37x faster                                  |
| genshi_xml      | 63.3 ms                                                | 52.5 ms: 1.21x faster                                  |
| Geometric mean  | (ref)                                                  | 1.36x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.67 ms: 2.02x faster                                  |
| logging_silent          | 175 ns                                                 | 102 ns: 1.72x faster                                   |
| scimark_sor             | 197 ms                                                 | 116 ms: 1.70x faster                                   |
| python_startup          | 14.2 ms                                                | 8.49 ms: 1.67x faster                                  |
| go                      | 229 ms                                                 | 140 ms: 1.64x faster                                   |
| crypto_pyaes            | 118 ms                                                 | 72.6 ms: 1.63x faster                                  |
| pyflate                 | 673 ms                                                 | 415 ms: 1.62x faster                                   |
| richards                | 74.9 ms                                                | 46.9 ms: 1.60x faster                                  |
| scimark_monte_carlo     | 108 ms                                                 | 68.4 ms: 1.58x faster                                  |
| raytrace                | 464 ms                                                 | 294 ms: 1.58x faster                                   |
| chaos                   | 106 ms                                                 | 69.6 ms: 1.53x faster                                  |
| scimark_lu              | 163 ms                                                 | 107 ms: 1.52x faster                                   |
| sqlglot_parse           | 2.06 ms                                                | 1.38 ms: 1.49x faster                                  |
| mako                    | 14.8 ms                                                | 9.92 ms: 1.49x faster                                  |
| nbody                   | 142 ms                                                 | 95.4 ms: 1.48x faster                                  |
| spectral_norm           | 150 ms                                                 | 101 ms: 1.48x faster                                   |
| hexiom                  | 9.53 ms                                                | 6.46 ms: 1.48x faster                                  |
| pickle_pure_python      | 455 us                                                 | 310 us: 1.47x faster                                   |
| sqlglot_transpile       | 2.45 ms                                                | 1.68 ms: 1.46x faster                                  |
| float                   | 111 ms                                                 | 76.0 ms: 1.45x faster                                  |
| unpack_sequence         | 64.7 ns                                                | 44.6 ns: 1.45x faster                                  |
| deepcopy_memo           | 52.3 us                                                | 37.2 us: 1.41x faster                                  |
| xml_etree_process       | 74.9 ms                                                | 53.7 ms: 1.39x faster                                  |
| django_template         | 45.9 ms                                                | 33.2 ms: 1.38x faster                                  |
| pprint_pformat          | 1.99 sec                                               | 1.44 sec: 1.38x faster                                 |
| async_tree_none         | 717 ms                                                 | 523 ms: 1.37x faster                                   |
| genshi_text             | 30.3 ms                                                | 22.1 ms: 1.37x faster                                  |
| chameleon               | 9.06 ms                                                | 6.63 ms: 1.37x faster                                  |
| pprint_safe_repr        | 955 ms                                                 | 700 ms: 1.36x faster                                   |
| logging_format          | 8.91 us                                                | 6.54 us: 1.36x faster                                  |
| async_tree_memoization  | 854 ms                                                 | 627 ms: 1.36x faster                                   |
| async_tree_io           | 1.77 sec                                               | 1.31 sec: 1.36x faster                                 |
| logging_simple          | 8.07 us                                                | 5.95 us: 1.36x faster                                  |
| html5lib                | 85.9 ms                                                | 63.4 ms: 1.35x faster                                  |
| thrift                  | 1.03 ms                                                | 765 us: 1.35x faster                                   |
| aiohttp                 | 1.38 ms                                                | 1.05 ms: 1.32x faster                                  |
| unpickle_pure_python    | 300 us                                                 | 229 us: 1.31x faster                                   |
| 2to3                    | 336 ms                                                 | 258 ms: 1.30x faster                                   |
| gunicorn                | 1.46 ms                                                | 1.13 ms: 1.30x faster                                  |
| scimark_fft             | 424 ms                                                 | 327 ms: 1.29x faster                                   |
| regex_compile           | 177 ms                                                 | 137 ms: 1.29x faster                                   |
| pycparser               | 1.50 sec                                               | 1.16 sec: 1.29x faster                                 |
| async_tree_cpu_io_mixed | 951 ms                                                 | 742 ms: 1.28x faster                                   |
| tornado_http            | 127 ms                                                 | 99.8 ms: 1.28x faster                                  |
| deepcopy                | 442 us                                                 | 349 us: 1.27x faster                                   |
| fannkuch                | 486 ms                                                 | 384 ms: 1.27x faster                                   |
| coroutines              | 31.8 ms                                                | 25.3 ms: 1.26x faster                                  |
| sqlglot_normalize       | 135 ms                                                 | 108 ms: 1.25x faster                                   |
| deepcopy_reduce         | 3.82 us                                                | 3.09 us: 1.24x faster                                  |
| docutils                | 3.17 sec                                               | 2.57 sec: 1.24x faster                                 |
| xml_etree_generate      | 94.2 ms                                                | 76.6 ms: 1.23x faster                                  |
| sqlglot_optimize        | 65.3 ms                                                | 53.3 ms: 1.23x faster                                  |
| genshi_xml              | 63.3 ms                                                | 52.5 ms: 1.21x faster                                  |
| json_loads              | 28.8 us                                                | 24.0 us: 1.20x faster                                  |
| dulwich_log             | 75.9 ms                                                | 63.5 ms: 1.20x faster                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.59 ms: 1.19x faster                                  |
| sqlite_synth            | 2.93 us                                                | 2.47 us: 1.19x faster                                  |
| async_generators        | 425 ms                                                 | 358 ms: 1.19x faster                                   |
| nqueens                 | 100 ms                                                 | 85.0 ms: 1.18x faster                                  |
| sqlalchemy_imperative   | 21.2 ms                                                | 18.0 ms: 1.18x faster                                  |
| sqlalchemy_declarative  | 165 ms                                                 | 141 ms: 1.17x faster                                   |
| json                    | 5.42 ms                                                | 4.63 ms: 1.17x faster                                  |
| flaskblogging           | 8.27 ms                                                | 7.07 ms: 1.17x faster                                  |
| bench_thread_pool       | 947 us                                                 | 813 us: 1.17x faster                                   |
| sympy_integrate         | 24.3 ms                                                | 21.0 ms: 1.16x faster                                  |
| dask                    | 423 ms                                                 | 365 ms: 1.16x faster                                   |
| sympy_expand            | 545 ms                                                 | 472 ms: 1.15x faster                                   |
| pylint                  | 525 ms                                                 | 461 ms: 1.14x faster                                   |
| sympy_str               | 328 ms                                                 | 289 ms: 1.14x faster                                   |
| create_gc_cycles        | 1.67 ms                                                | 1.48 ms: 1.13x faster                                  |
| regex_v8                | 25.0 ms                                                | 22.3 ms: 1.12x faster                                  |
| sympy_sum               | 185 ms                                                 | 166 ms: 1.11x faster                                   |
| regex_dna               | 222 ms                                                 | 200 ms: 1.11x faster                                   |
| pathlib                 | 20.0 ms                                                | 18.1 ms: 1.11x faster                                  |
| pickle_list             | 4.56 us                                                | 4.17 us: 1.09x faster                                  |
| djangocms               | 35.9 us                                                | 33.1 us: 1.09x faster                                  |
| meteor_contest          | 115 ms                                                 | 106 ms: 1.08x faster                                   |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                   |
| json_dumps              | 13.5 ms                                                | 12.6 ms: 1.07x faster                                  |
| mdp                     | 2.82 sec                                               | 2.64 sec: 1.07x faster                                 |
| pickle                  | 10.3 us                                                | 9.72 us: 1.06x faster                                  |
| unpickle                | 14.1 us                                                | 13.4 us: 1.06x faster                                  |
| generators              | 76.8 ms                                                | 73.3 ms: 1.05x faster                                  |
| asyncio_tcp             | 925 ms                                                 | 889 ms: 1.04x faster                                   |
| xml_etree_parse         | 163 ms                                                 | 158 ms: 1.03x faster                                   |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x faster                                   |
| telco                   | 6.54 ms                                                | 6.66 ms: 1.02x slower                                  |
| regex_effbot            | 3.23 ms                                                | 3.31 ms: 1.03x slower                                  |
| unpickle_list           | 4.82 us                                                | 4.95 us: 1.03x slower                                  |
| python_startup_no_site  | 5.82 ms                                                | 5.98 ms: 1.03x slower                                  |
| gc_traversal            | 3.84 ms                                                | 4.26 ms: 1.11x slower                                  |
| pickle_dict             | 27.3 us                                                | 31.1 us: 1.14x slower                                  |
| coverage                | 72.8 ms                                                | 104 ms: 1.43x slower                                   |
| Geometric mean          | (ref)                                                  | 1.25x faster                                           |

Benchmark hidden because not significant (2): mypy2, bench_mp_pool
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.19x
