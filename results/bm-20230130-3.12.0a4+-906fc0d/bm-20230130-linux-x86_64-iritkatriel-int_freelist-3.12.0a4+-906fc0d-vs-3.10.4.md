
# Results vs. 3.10.4

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 906fc0d
- commit date: 2023-01-30
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 253 ms: 1.33x faster                                                |
| chameleon      | 9.06 ms                                                | 6.31 ms: 1.44x faster                                               |
| docutils       | 3.17 sec                                               | 2.49 sec: 1.27x faster                                              |
| html5lib       | 85.9 ms                                                | 60.3 ms: 1.42x faster                                               |
| tornado_http   | 127 ms                                                 | 93.9 ms: 1.36x faster                                               |
| Geometric mean | (ref)                                                  | 1.36x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 111 ms                                                 | 72.1 ms: 1.53x faster                                               |
| nbody          | 142 ms                                                 | 95.5 ms: 1.48x faster                                               |
| pidigits       | 190 ms                                                 | 199 ms: 1.05x slower                                                |
| Geometric mean | (ref)                                                  | 1.29x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.38x faster                                                |
| regex_v8       | 25.0 ms                                                | 21.7 ms: 1.15x faster                                               |
| regex_dna      | 222 ms                                                 | 209 ms: 1.06x faster                                                |
| regex_effbot   | 3.23 ms                                                | 3.63 ms: 1.12x slower                                               |
| Geometric mean | (ref)                                                  | 1.11x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 287 us: 1.58x faster                                                |
| unpickle_pure_python | 300 us                                                 | 197 us: 1.52x faster                                                |
| json_dumps           | 13.5 ms                                                | 9.58 ms: 1.41x faster                                               |
| xml_etree_process    | 74.9 ms                                                | 53.5 ms: 1.40x faster                                               |
| xml_etree_generate   | 94.2 ms                                                | 77.6 ms: 1.21x faster                                               |
| json_loads           | 28.8 us                                                | 24.2 us: 1.19x faster                                               |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                                |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.09x faster                                                |
| pickle_list          | 4.56 us                                                | 4.24 us: 1.08x faster                                               |
| unpickle             | 14.1 us                                                | 13.2 us: 1.07x faster                                               |
| pickle               | 10.3 us                                                | 10.2 us: 1.01x faster                                               |
| unpickle_list        | 4.82 us                                                | 4.89 us: 1.01x slower                                               |
| pickle_dict          | 27.3 us                                                | 31.2 us: 1.14x slower                                               |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.98 ms: 1.58x faster                                               |
| python_startup_no_site | 5.82 ms                                                | 6.49 ms: 1.12x slower                                               |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.87 ms: 1.50x faster                                               |
| genshi_text     | 30.3 ms                                                | 21.0 ms: 1.45x faster                                               |
| django_template | 45.9 ms                                                | 33.1 ms: 1.39x faster                                               |
| genshi_xml      | 63.3 ms                                                | 47.6 ms: 1.33x faster                                               |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.20 ms: 2.32x faster                                               |
| logging_silent          | 175 ns                                                 | 92.2 ns: 1.90x faster                                               |
| asyncio_tcp             | 925 ms                                                 | 494 ms: 1.87x faster                                                |
| richards                | 74.9 ms                                                | 41.6 ms: 1.80x faster                                               |
| scimark_sor             | 197 ms                                                 | 111 ms: 1.77x faster                                                |
| go                      | 229 ms                                                 | 134 ms: 1.70x faster                                                |
| pyflate                 | 673 ms                                                 | 396 ms: 1.70x faster                                                |
| chaos                   | 106 ms                                                 | 63.9 ms: 1.66x faster                                               |
| scimark_monte_carlo     | 108 ms                                                 | 66.7 ms: 1.62x faster                                               |
| raytrace                | 464 ms                                                 | 289 ms: 1.61x faster                                                |
| hexiom                  | 9.53 ms                                                | 5.97 ms: 1.60x faster                                               |
| pickle_pure_python      | 455 us                                                 | 287 us: 1.58x faster                                                |
| python_startup          | 14.2 ms                                                | 8.98 ms: 1.58x faster                                               |
| crypto_pyaes            | 118 ms                                                 | 76.0 ms: 1.56x faster                                               |
| scimark_lu              | 163 ms                                                 | 106 ms: 1.54x faster                                                |
| float                   | 111 ms                                                 | 72.1 ms: 1.53x faster                                               |
| unpickle_pure_python    | 300 us                                                 | 197 us: 1.52x faster                                                |
| deepcopy_memo           | 52.3 us                                                | 34.6 us: 1.51x faster                                               |
| unpack_sequence         | 64.7 ns                                                | 43.3 ns: 1.50x faster                                               |
| mako                    | 14.8 ms                                                | 9.87 ms: 1.50x faster                                               |
| nbody                   | 142 ms                                                 | 95.5 ms: 1.48x faster                                               |
| sqlglot_parse           | 2.06 ms                                                | 1.41 ms: 1.46x faster                                               |
| genshi_text             | 30.3 ms                                                | 21.0 ms: 1.45x faster                                               |
| pprint_pformat          | 1.99 sec                                               | 1.38 sec: 1.44x faster                                              |
| chameleon               | 9.06 ms                                                | 6.31 ms: 1.44x faster                                               |
| sqlglot_transpile       | 2.45 ms                                                | 1.71 ms: 1.43x faster                                               |
| spectral_norm           | 150 ms                                                 | 105 ms: 1.43x faster                                                |
| pprint_safe_repr        | 955 ms                                                 | 669 ms: 1.43x faster                                                |
| html5lib                | 85.9 ms                                                | 60.3 ms: 1.42x faster                                               |
| logging_simple          | 8.07 us                                                | 5.68 us: 1.42x faster                                               |
| logging_format          | 8.91 us                                                | 6.30 us: 1.41x faster                                               |
| json_dumps              | 13.5 ms                                                | 9.58 ms: 1.41x faster                                               |
| xml_etree_process       | 74.9 ms                                                | 53.5 ms: 1.40x faster                                               |
| thrift                  | 1.03 ms                                                | 742 us: 1.39x faster                                                |
| aiohttp                 | 1.38 ms                                                | 997 us: 1.39x faster                                                |
| django_template         | 45.9 ms                                                | 33.1 ms: 1.39x faster                                               |
| regex_compile           | 177 ms                                                 | 128 ms: 1.38x faster                                                |
| async_tree_none         | 717 ms                                                 | 525 ms: 1.37x faster                                                |
| scimark_fft             | 424 ms                                                 | 311 ms: 1.36x faster                                                |
| gunicorn                | 1.46 ms                                                | 1.07 ms: 1.36x faster                                               |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.02 ms: 1.36x faster                                               |
| tornado_http            | 127 ms                                                 | 93.9 ms: 1.36x faster                                               |
| fannkuch                | 486 ms                                                 | 358 ms: 1.36x faster                                                |
| async_tree_io           | 1.77 sec                                               | 1.31 sec: 1.35x faster                                              |
| pycparser               | 1.50 sec                                               | 1.12 sec: 1.35x faster                                              |
| deepcopy                | 442 us                                                 | 330 us: 1.34x faster                                                |
| genshi_xml              | 63.3 ms                                                | 47.6 ms: 1.33x faster                                               |
| 2to3                    | 336 ms                                                 | 253 ms: 1.33x faster                                                |
| deepcopy_reduce         | 3.82 us                                                | 2.94 us: 1.30x faster                                               |
| async_tree_memoization  | 854 ms                                                 | 658 ms: 1.30x faster                                                |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.28x faster                                                |
| sqlglot_optimize        | 65.3 ms                                                | 51.2 ms: 1.28x faster                                               |
| docutils                | 3.17 sec                                               | 2.49 sec: 1.27x faster                                              |
| coroutines              | 31.8 ms                                                | 25.1 ms: 1.27x faster                                               |
| async_tree_cpu_io_mixed | 951 ms                                                 | 752 ms: 1.26x faster                                                |
| nqueens                 | 100 ms                                                 | 79.5 ms: 1.26x faster                                               |
| sympy_integrate         | 24.3 ms                                                | 19.8 ms: 1.23x faster                                               |
| sympy_str               | 328 ms                                                 | 270 ms: 1.22x faster                                                |
| xml_etree_generate      | 94.2 ms                                                | 77.6 ms: 1.21x faster                                               |
| dulwich_log             | 75.9 ms                                                | 62.8 ms: 1.21x faster                                               |
| async_generators        | 425 ms                                                 | 353 ms: 1.20x faster                                                |
| sympy_expand            | 545 ms                                                 | 453 ms: 1.20x faster                                                |
| bench_thread_pool       | 947 us                                                 | 790 us: 1.20x faster                                                |
| json_loads              | 28.8 us                                                | 24.2 us: 1.19x faster                                               |
| sympy_sum               | 185 ms                                                 | 156 ms: 1.19x faster                                                |
| json                    | 5.42 ms                                                | 4.67 ms: 1.16x faster                                               |
| regex_v8                | 25.0 ms                                                | 21.7 ms: 1.15x faster                                               |
| create_gc_cycles        | 1.67 ms                                                | 1.46 ms: 1.14x faster                                               |
| sqlite_synth            | 2.93 us                                                | 2.60 us: 1.13x faster                                               |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                               |
| djangocms               | 35.9 us                                                | 32.1 us: 1.12x faster                                               |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                                |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.09x faster                                                |
| mdp                     | 2.82 sec                                               | 2.62 sec: 1.08x faster                                              |
| pickle_list             | 4.56 us                                                | 4.24 us: 1.08x faster                                               |
| unpickle                | 14.1 us                                                | 13.2 us: 1.07x faster                                               |
| meteor_contest          | 115 ms                                                 | 107 ms: 1.07x faster                                                |
| regex_dna               | 222 ms                                                 | 209 ms: 1.06x faster                                                |
| telco                   | 6.54 ms                                                | 6.38 ms: 1.03x faster                                               |
| pickle                  | 10.3 us                                                | 10.2 us: 1.01x faster                                               |
| gc_traversal            | 3.84 ms                                                | 3.82 ms: 1.01x faster                                               |
| unpickle_list           | 4.82 us                                                | 4.89 us: 1.01x slower                                               |
| generators              | 76.8 ms                                                | 78.0 ms: 1.02x slower                                               |
| pidigits                | 190 ms                                                 | 199 ms: 1.05x slower                                                |
| python_startup_no_site  | 5.82 ms                                                | 6.49 ms: 1.12x slower                                               |
| regex_effbot            | 3.23 ms                                                | 3.63 ms: 1.12x slower                                               |
| pickle_dict             | 27.3 us                                                | 31.2 us: 1.14x slower                                               |
| dask                    | 423 ms                                                 | 498 ms: 1.18x slower                                                |
| coverage                | 72.8 ms                                                | 96.0 ms: 1.32x slower                                               |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                        |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230130-3.12.0a4+-906fc0d/bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.26x
