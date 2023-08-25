
# Results vs. 3.10.4

- fork: iritkatriel
- ref: single_op_exit
- machine: linux-x86_64
- commit hash: 4684fa7
- commit date: 2023-01-27
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 251 ms: 1.34x faster                                                  |
| chameleon      | 9.06 ms                                                | 6.53 ms: 1.39x faster                                                 |
| docutils       | 3.17 sec                                               | 2.50 sec: 1.27x faster                                                |
| html5lib       | 85.9 ms                                                | 60.1 ms: 1.43x faster                                                 |
| tornado_http   | 127 ms                                                 | 93.0 ms: 1.37x faster                                                 |
| Geometric mean | (ref)                                                  | 1.36x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 111 ms                                                 | 72.8 ms: 1.52x faster                                                 |
| nbody          | 142 ms                                                 | 95.1 ms: 1.49x faster                                                 |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.31x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.38x faster                                                  |
| regex_dna      | 222 ms                                                 | 209 ms: 1.06x faster                                                  |
| regex_v8       | 25.0 ms                                                | 25.9 ms: 1.03x slower                                                 |
| regex_effbot   | 3.23 ms                                                | 3.57 ms: 1.11x slower                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 283 us: 1.61x faster                                                  |
| unpickle_pure_python | 300 us                                                 | 197 us: 1.52x faster                                                  |
| json_dumps           | 13.5 ms                                                | 9.28 ms: 1.46x faster                                                 |
| xml_etree_process    | 74.9 ms                                                | 54.1 ms: 1.38x faster                                                 |
| xml_etree_generate   | 94.2 ms                                                | 77.6 ms: 1.21x faster                                                 |
| json_loads           | 28.8 us                                                | 24.1 us: 1.20x faster                                                 |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.10x faster                                                  |
| pickle_list          | 4.56 us                                                | 4.21 us: 1.08x faster                                                 |
| unpickle             | 14.1 us                                                | 13.3 us: 1.06x faster                                                 |
| pickle               | 10.3 us                                                | 10.1 us: 1.02x faster                                                 |
| unpickle_list        | 4.82 us                                                | 4.98 us: 1.03x slower                                                 |
| pickle_dict          | 27.3 us                                                | 31.1 us: 1.14x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.96 ms: 1.58x faster                                                 |
| python_startup_no_site | 5.82 ms                                                | 6.48 ms: 1.11x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.69 ms: 1.52x faster                                                 |
| genshi_text     | 30.3 ms                                                | 20.4 ms: 1.49x faster                                                 |
| django_template | 45.9 ms                                                | 32.5 ms: 1.41x faster                                                 |
| genshi_xml      | 63.3 ms                                                | 46.1 ms: 1.37x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.26 ms: 2.28x faster                                                 |
| logging_silent          | 175 ns                                                 | 92.0 ns: 1.90x faster                                                 |
| asyncio_tcp             | 925 ms                                                 | 496 ms: 1.86x faster                                                  |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.83x faster                                                  |
| richards                | 74.9 ms                                                | 42.1 ms: 1.78x faster                                                 |
| scimark_monte_carlo     | 108 ms                                                 | 64.2 ms: 1.69x faster                                                 |
| pyflate                 | 673 ms                                                 | 399 ms: 1.69x faster                                                  |
| go                      | 229 ms                                                 | 137 ms: 1.68x faster                                                  |
| raytrace                | 464 ms                                                 | 281 ms: 1.65x faster                                                  |
| chaos                   | 106 ms                                                 | 64.8 ms: 1.64x faster                                                 |
| crypto_pyaes            | 118 ms                                                 | 73.3 ms: 1.62x faster                                                 |
| pickle_pure_python      | 455 us                                                 | 283 us: 1.61x faster                                                  |
| hexiom                  | 9.53 ms                                                | 5.94 ms: 1.60x faster                                                 |
| python_startup          | 14.2 ms                                                | 8.96 ms: 1.58x faster                                                 |
| spectral_norm           | 150 ms                                                 | 96.5 ms: 1.55x faster                                                 |
| scimark_lu              | 163 ms                                                 | 106 ms: 1.53x faster                                                  |
| unpickle_pure_python    | 300 us                                                 | 197 us: 1.52x faster                                                  |
| mako                    | 14.8 ms                                                | 9.69 ms: 1.52x faster                                                 |
| float                   | 111 ms                                                 | 72.8 ms: 1.52x faster                                                 |
| unpack_sequence         | 64.7 ns                                                | 42.8 ns: 1.51x faster                                                 |
| deepcopy_memo           | 52.3 us                                                | 34.7 us: 1.51x faster                                                 |
| genshi_text             | 30.3 ms                                                | 20.4 ms: 1.49x faster                                                 |
| nbody                   | 142 ms                                                 | 95.1 ms: 1.49x faster                                                 |
| json_dumps              | 13.5 ms                                                | 9.28 ms: 1.46x faster                                                 |
| sqlglot_parse           | 2.06 ms                                                | 1.41 ms: 1.46x faster                                                 |
| pprint_pformat          | 1.99 sec                                               | 1.38 sec: 1.44x faster                                                |
| sqlglot_transpile       | 2.45 ms                                                | 1.71 ms: 1.43x faster                                                 |
| html5lib                | 85.9 ms                                                | 60.1 ms: 1.43x faster                                                 |
| logging_format          | 8.91 us                                                | 6.25 us: 1.43x faster                                                 |
| pprint_safe_repr        | 955 ms                                                 | 674 ms: 1.42x faster                                                  |
| logging_simple          | 8.07 us                                                | 5.70 us: 1.42x faster                                                 |
| django_template         | 45.9 ms                                                | 32.5 ms: 1.41x faster                                                 |
| scimark_fft             | 424 ms                                                 | 301 ms: 1.41x faster                                                  |
| aiohttp                 | 1.38 ms                                                | 991 us: 1.40x faster                                                  |
| chameleon               | 9.06 ms                                                | 6.53 ms: 1.39x faster                                                 |
| regex_compile           | 177 ms                                                 | 128 ms: 1.38x faster                                                  |
| xml_etree_process       | 74.9 ms                                                | 54.1 ms: 1.38x faster                                                 |
| gunicorn                | 1.46 ms                                                | 1.06 ms: 1.38x faster                                                 |
| genshi_xml              | 63.3 ms                                                | 46.1 ms: 1.37x faster                                                 |
| pycparser               | 1.50 sec                                               | 1.09 sec: 1.37x faster                                                |
| thrift                  | 1.03 ms                                                | 755 us: 1.37x faster                                                  |
| tornado_http            | 127 ms                                                 | 93.0 ms: 1.37x faster                                                 |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.99 ms: 1.37x faster                                                 |
| async_tree_none         | 717 ms                                                 | 525 ms: 1.37x faster                                                  |
| deepcopy                | 442 us                                                 | 327 us: 1.35x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 1.32 sec: 1.35x faster                                                |
| async_tree_memoization  | 854 ms                                                 | 633 ms: 1.35x faster                                                  |
| 2to3                    | 336 ms                                                 | 251 ms: 1.34x faster                                                  |
| deepcopy_reduce         | 3.82 us                                                | 2.93 us: 1.31x faster                                                 |
| nqueens                 | 100 ms                                                 | 76.8 ms: 1.30x faster                                                 |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                                  |
| sqlglot_optimize        | 65.3 ms                                                | 50.6 ms: 1.29x faster                                                 |
| fannkuch                | 486 ms                                                 | 377 ms: 1.29x faster                                                  |
| coroutines              | 31.8 ms                                                | 24.8 ms: 1.28x faster                                                 |
| docutils                | 3.17 sec                                               | 2.50 sec: 1.27x faster                                                |
| async_tree_cpu_io_mixed | 951 ms                                                 | 757 ms: 1.26x faster                                                  |
| sympy_integrate         | 24.3 ms                                                | 19.7 ms: 1.23x faster                                                 |
| bench_thread_pool       | 947 us                                                 | 769 us: 1.23x faster                                                  |
| dulwich_log             | 75.9 ms                                                | 61.8 ms: 1.23x faster                                                 |
| sympy_str               | 328 ms                                                 | 268 ms: 1.23x faster                                                  |
| xml_etree_generate      | 94.2 ms                                                | 77.6 ms: 1.21x faster                                                 |
| sympy_expand            | 545 ms                                                 | 452 ms: 1.21x faster                                                  |
| async_generators        | 425 ms                                                 | 354 ms: 1.20x faster                                                  |
| json_loads              | 28.8 us                                                | 24.1 us: 1.20x faster                                                 |
| sympy_sum               | 185 ms                                                 | 154 ms: 1.20x faster                                                  |
| json                    | 5.42 ms                                                | 4.61 ms: 1.17x faster                                                 |
| sqlite_synth            | 2.93 us                                                | 2.57 us: 1.14x faster                                                 |
| create_gc_cycles        | 1.67 ms                                                | 1.47 ms: 1.14x faster                                                 |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.13x faster                                                 |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                  |
| djangocms               | 35.9 us                                                | 32.7 us: 1.10x faster                                                 |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.10x faster                                                  |
| meteor_contest          | 115 ms                                                 | 105 ms: 1.09x faster                                                  |
| pickle_list             | 4.56 us                                                | 4.21 us: 1.08x faster                                                 |
| unpickle                | 14.1 us                                                | 13.3 us: 1.06x faster                                                 |
| regex_dna               | 222 ms                                                 | 209 ms: 1.06x faster                                                  |
| mdp                     | 2.82 sec                                               | 2.69 sec: 1.05x faster                                                |
| telco                   | 6.54 ms                                                | 6.28 ms: 1.04x faster                                                 |
| generators              | 76.8 ms                                                | 74.9 ms: 1.03x faster                                                 |
| pickle                  | 10.3 us                                                | 10.1 us: 1.02x faster                                                 |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                  |
| unpickle_list           | 4.82 us                                                | 4.98 us: 1.03x slower                                                 |
| regex_v8                | 25.0 ms                                                | 25.9 ms: 1.03x slower                                                 |
| regex_effbot            | 3.23 ms                                                | 3.57 ms: 1.11x slower                                                 |
| python_startup_no_site  | 5.82 ms                                                | 6.48 ms: 1.11x slower                                                 |
| gc_traversal            | 3.84 ms                                                | 4.30 ms: 1.12x slower                                                 |
| pickle_dict             | 27.3 us                                                | 31.1 us: 1.14x slower                                                 |
| dask                    | 423 ms                                                 | 491 ms: 1.16x slower                                                  |
| coverage                | 72.8 ms                                                | 97.8 ms: 1.34x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                          |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230127-3.12.0a4+-4684fa7/bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x
