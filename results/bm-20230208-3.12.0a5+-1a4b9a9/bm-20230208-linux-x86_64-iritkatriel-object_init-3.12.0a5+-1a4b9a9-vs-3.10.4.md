
# Results vs. 3.10.4

- fork: iritkatriel
- ref: object_init
- machine: linux-x86_64
- commit hash: 1a4b9a9
- commit date: 2023-02-08
- overall geometric mean: 1.31x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 251 ms: 1.34x faster                                               |
| chameleon      | 9.06 ms                                                | 6.36 ms: 1.42x faster                                              |
| docutils       | 3.17 sec                                               | 2.56 sec: 1.24x faster                                             |
| html5lib       | 85.9 ms                                                | 60.9 ms: 1.41x faster                                              |
| tornado_http   | 127 ms                                                 | 94.0 ms: 1.36x faster                                              |
| Geometric mean | (ref)                                                  | 1.35x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 86.0 ms: 1.65x faster                                              |
| float          | 111 ms                                                 | 72.1 ms: 1.53x faster                                              |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x faster                                               |
| Geometric mean | (ref)                                                  | 1.36x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.38x faster                                               |
| regex_v8       | 25.0 ms                                                | 21.4 ms: 1.17x faster                                              |
| regex_dna      | 222 ms                                                 | 211 ms: 1.05x faster                                               |
| regex_effbot   | 3.23 ms                                                | 3.32 ms: 1.03x slower                                              |
| Geometric mean | (ref)                                                  | 1.14x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 288 us: 1.58x faster                                               |
| unpickle_pure_python | 300 us                                                 | 197 us: 1.52x faster                                               |
| json_dumps           | 13.5 ms                                                | 9.34 ms: 1.45x faster                                              |
| xml_etree_process    | 74.9 ms                                                | 55.6 ms: 1.35x faster                                              |
| json_loads           | 28.8 us                                                | 23.7 us: 1.21x faster                                              |
| xml_etree_generate   | 94.2 ms                                                | 81.3 ms: 1.16x faster                                              |
| pickle_list          | 4.56 us                                                | 4.09 us: 1.11x faster                                              |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                               |
| unpickle             | 14.1 us                                                | 13.1 us: 1.08x faster                                              |
| xml_etree_iterparse  | 111 ms                                                 | 108 ms: 1.03x faster                                               |
| pickle               | 10.3 us                                                | 10.2 us: 1.01x faster                                              |
| unpickle_list        | 4.82 us                                                | 5.04 us: 1.05x slower                                              |
| pickle_dict          | 27.3 us                                                | 30.6 us: 1.12x slower                                              |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.97 ms: 1.58x faster                                              |
| python_startup_no_site | 5.82 ms                                                | 6.51 ms: 1.12x slower                                              |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.65 ms: 1.53x faster                                              |
| genshi_text     | 30.3 ms                                                | 20.7 ms: 1.46x faster                                              |
| django_template | 45.9 ms                                                | 32.4 ms: 1.42x faster                                              |
| genshi_xml      | 63.3 ms                                                | 46.4 ms: 1.37x faster                                              |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                       |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.18 ms: 2.33x faster                                              |
| logging_silent          | 175 ns                                                 | 92.3 ns: 1.90x faster                                              |
| asyncio_tcp             | 925 ms                                                 | 490 ms: 1.89x faster                                               |
| scimark_sor             | 197 ms                                                 | 108 ms: 1.83x faster                                               |
| richards                | 74.9 ms                                                | 42.2 ms: 1.78x faster                                              |
| go                      | 229 ms                                                 | 135 ms: 1.70x faster                                               |
| pyflate                 | 673 ms                                                 | 403 ms: 1.67x faster                                               |
| scimark_monte_carlo     | 108 ms                                                 | 65.0 ms: 1.66x faster                                              |
| crypto_pyaes            | 118 ms                                                 | 71.3 ms: 1.66x faster                                              |
| chaos                   | 106 ms                                                 | 64.1 ms: 1.66x faster                                              |
| raytrace                | 464 ms                                                 | 281 ms: 1.65x faster                                               |
| nbody                   | 142 ms                                                 | 86.0 ms: 1.65x faster                                              |
| hexiom                  | 9.53 ms                                                | 5.95 ms: 1.60x faster                                              |
| pickle_pure_python      | 455 us                                                 | 288 us: 1.58x faster                                               |
| python_startup          | 14.2 ms                                                | 8.97 ms: 1.58x faster                                              |
| spectral_norm           | 150 ms                                                 | 95.9 ms: 1.56x faster                                              |
| deepcopy_memo           | 52.3 us                                                | 33.9 us: 1.54x faster                                              |
| float                   | 111 ms                                                 | 72.1 ms: 1.53x faster                                              |
| scimark_lu              | 163 ms                                                 | 106 ms: 1.53x faster                                               |
| mako                    | 14.8 ms                                                | 9.65 ms: 1.53x faster                                              |
| unpickle_pure_python    | 300 us                                                 | 197 us: 1.52x faster                                               |
| unpack_sequence         | 64.7 ns                                                | 42.6 ns: 1.52x faster                                              |
| genshi_text             | 30.3 ms                                                | 20.7 ms: 1.46x faster                                              |
| sqlglot_parse           | 2.06 ms                                                | 1.41 ms: 1.46x faster                                              |
| json_dumps              | 13.5 ms                                                | 9.34 ms: 1.45x faster                                              |
| sqlglot_transpile       | 2.45 ms                                                | 1.72 ms: 1.43x faster                                              |
| chameleon               | 9.06 ms                                                | 6.36 ms: 1.42x faster                                              |
| pprint_pformat          | 1.99 sec                                               | 1.40 sec: 1.42x faster                                             |
| scimark_fft             | 424 ms                                                 | 298 ms: 1.42x faster                                               |
| django_template         | 45.9 ms                                                | 32.4 ms: 1.42x faster                                              |
| html5lib                | 85.9 ms                                                | 60.9 ms: 1.41x faster                                              |
| logging_format          | 8.91 us                                                | 6.34 us: 1.41x faster                                              |
| pprint_safe_repr        | 955 ms                                                 | 680 ms: 1.40x faster                                               |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.90 ms: 1.40x faster                                              |
| logging_simple          | 8.07 us                                                | 5.79 us: 1.39x faster                                              |
| regex_compile           | 177 ms                                                 | 128 ms: 1.38x faster                                               |
| aiohttp                 | 1.38 ms                                                | 1.00 ms: 1.38x faster                                              |
| async_tree_none         | 717 ms                                                 | 523 ms: 1.37x faster                                               |
| pycparser               | 1.50 sec                                               | 1.10 sec: 1.37x faster                                             |
| genshi_xml              | 63.3 ms                                                | 46.4 ms: 1.37x faster                                              |
| async_tree_io           | 1.77 sec                                               | 1.30 sec: 1.36x faster                                             |
| tornado_http            | 127 ms                                                 | 94.0 ms: 1.36x faster                                              |
| gunicorn                | 1.46 ms                                                | 1.08 ms: 1.35x faster                                              |
| thrift                  | 1.03 ms                                                | 765 us: 1.35x faster                                               |
| xml_etree_process       | 74.9 ms                                                | 55.6 ms: 1.35x faster                                              |
| deepcopy                | 442 us                                                 | 328 us: 1.35x faster                                               |
| async_tree_memoization  | 854 ms                                                 | 635 ms: 1.35x faster                                               |
| 2to3                    | 336 ms                                                 | 251 ms: 1.34x faster                                               |
| fannkuch                | 486 ms                                                 | 369 ms: 1.32x faster                                               |
| deepcopy_reduce         | 3.82 us                                                | 2.92 us: 1.31x faster                                              |
| mypy2                   | 428 ms                                                 | 328 ms: 1.31x faster                                               |
| coroutines              | 31.8 ms                                                | 24.5 ms: 1.30x faster                                              |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                               |
| sqlglot_optimize        | 65.3 ms                                                | 51.0 ms: 1.28x faster                                              |
| nqueens                 | 100 ms                                                 | 78.8 ms: 1.27x faster                                              |
| async_tree_cpu_io_mixed | 951 ms                                                 | 752 ms: 1.26x faster                                               |
| docutils                | 3.17 sec                                               | 2.56 sec: 1.24x faster                                             |
| sympy_integrate         | 24.3 ms                                                | 19.8 ms: 1.22x faster                                              |
| sympy_str               | 328 ms                                                 | 271 ms: 1.21x faster                                               |
| json_loads              | 28.8 us                                                | 23.7 us: 1.21x faster                                              |
| sqlalchemy_declarative  | 165 ms                                                 | 137 ms: 1.21x faster                                               |
| bench_thread_pool       | 947 us                                                 | 786 us: 1.21x faster                                               |
| dulwich_log             | 75.9 ms                                                | 63.1 ms: 1.20x faster                                              |
| sympy_expand            | 545 ms                                                 | 457 ms: 1.19x faster                                               |
| sqlalchemy_imperative   | 21.2 ms                                                | 18.0 ms: 1.18x faster                                              |
| regex_v8                | 25.0 ms                                                | 21.4 ms: 1.17x faster                                              |
| json                    | 5.42 ms                                                | 4.64 ms: 1.17x faster                                              |
| sympy_sum               | 185 ms                                                 | 158 ms: 1.17x faster                                               |
| xml_etree_generate      | 94.2 ms                                                | 81.3 ms: 1.16x faster                                              |
| mdp                     | 2.82 sec                                               | 2.45 sec: 1.15x faster                                             |
| sqlite_synth            | 2.93 us                                                | 2.56 us: 1.14x faster                                              |
| djangocms               | 35.9 us                                                | 31.6 us: 1.14x faster                                              |
| create_gc_cycles        | 1.67 ms                                                | 1.47 ms: 1.13x faster                                              |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                              |
| pickle_list             | 4.56 us                                                | 4.09 us: 1.11x faster                                              |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                               |
| unpickle                | 14.1 us                                                | 13.1 us: 1.08x faster                                              |
| meteor_contest          | 115 ms                                                 | 107 ms: 1.07x faster                                               |
| regex_dna               | 222 ms                                                 | 211 ms: 1.05x faster                                               |
| xml_etree_iterparse     | 111 ms                                                 | 108 ms: 1.03x faster                                               |
| telco                   | 6.54 ms                                                | 6.40 ms: 1.02x faster                                              |
| pickle                  | 10.3 us                                                | 10.2 us: 1.01x faster                                              |
| async_generators        | 425 ms                                                 | 423 ms: 1.00x faster                                               |
| generators              | 76.8 ms                                                | 76.5 ms: 1.00x faster                                              |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x faster                                               |
| regex_effbot            | 3.23 ms                                                | 3.32 ms: 1.03x slower                                              |
| gc_traversal            | 3.84 ms                                                | 3.96 ms: 1.03x slower                                              |
| unpickle_list           | 4.82 us                                                | 5.04 us: 1.05x slower                                              |
| python_startup_no_site  | 5.82 ms                                                | 6.51 ms: 1.12x slower                                              |
| pickle_dict             | 27.3 us                                                | 30.6 us: 1.12x slower                                              |
| coverage                | 72.8 ms                                                | 97.3 ms: 1.34x slower                                              |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                       |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, dask, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x
