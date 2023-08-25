
# Results vs. 3.10.4

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: cfb886d
- commit date: 2023-02-10
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-cfb886d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 252 ms: 1.34x faster                                                |
| chameleon      | 9.06 ms                                                | 6.28 ms: 1.44x faster                                               |
| docutils       | 3.17 sec                                               | 2.52 sec: 1.26x faster                                              |
| html5lib       | 85.9 ms                                                | 60.5 ms: 1.42x faster                                               |
| tornado_http   | 127 ms                                                 | 94.2 ms: 1.35x faster                                               |
| Geometric mean | (ref)                                                  | 1.36x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-cfb886d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 111 ms                                                 | 71.9 ms: 1.54x faster                                               |
| nbody          | 142 ms                                                 | 95.4 ms: 1.48x faster                                               |
| pidigits       | 190 ms                                                 | 203 ms: 1.07x slower                                                |
| Geometric mean | (ref)                                                  | 1.29x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-cfb886d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 127 ms: 1.39x faster                                                |
| regex_v8       | 25.0 ms                                                | 21.0 ms: 1.19x faster                                               |
| regex_dna      | 222 ms                                                 | 219 ms: 1.01x faster                                                |
| regex_effbot   | 3.23 ms                                                | 3.43 ms: 1.06x slower                                               |
| Geometric mean | (ref)                                                  | 1.12x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-cfb886d |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 287 us: 1.59x faster                                                |
| unpickle_pure_python | 300 us                                                 | 197 us: 1.52x faster                                                |
| json_dumps           | 13.5 ms                                                | 9.57 ms: 1.41x faster                                               |
| xml_etree_process    | 74.9 ms                                                | 55.7 ms: 1.34x faster                                               |
| json_loads           | 28.8 us                                                | 23.8 us: 1.21x faster                                               |
| xml_etree_generate   | 94.2 ms                                                | 80.8 ms: 1.17x faster                                               |
| pickle_list          | 4.56 us                                                | 4.09 us: 1.11x faster                                               |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                                |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                |
| unpickle             | 14.1 us                                                | 13.2 us: 1.07x faster                                               |
| pickle               | 10.3 us                                                | 10.1 us: 1.02x faster                                               |
| unpickle_list        | 4.82 us                                                | 4.87 us: 1.01x slower                                               |
| pickle_dict          | 27.3 us                                                | 30.9 us: 1.13x slower                                               |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-cfb886d |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.92 ms: 1.59x faster                                               |
| python_startup_no_site | 5.82 ms                                                | 6.48 ms: 1.11x slower                                               |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-cfb886d |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.81 ms: 1.50x faster                                               |
| genshi_text     | 30.3 ms                                                | 20.6 ms: 1.47x faster                                               |
| django_template | 45.9 ms                                                | 33.1 ms: 1.39x faster                                               |
| genshi_xml      | 63.3 ms                                                | 46.9 ms: 1.35x faster                                               |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-cfb886d |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.20 ms: 2.32x faster                                               |
| logging_silent          | 175 ns                                                 | 92.4 ns: 1.89x faster                                               |
| scimark_sor             | 197 ms                                                 | 105 ms: 1.87x faster                                                |
| asyncio_tcp             | 925 ms                                                 | 496 ms: 1.86x faster                                                |
| richards                | 74.9 ms                                                | 43.6 ms: 1.72x faster                                               |
| pyflate                 | 673 ms                                                 | 395 ms: 1.70x faster                                                |
| go                      | 229 ms                                                 | 135 ms: 1.70x faster                                                |
| raytrace                | 464 ms                                                 | 281 ms: 1.65x faster                                                |
| scimark_monte_carlo     | 108 ms                                                 | 66.2 ms: 1.64x faster                                               |
| chaos                   | 106 ms                                                 | 65.9 ms: 1.61x faster                                               |
| hexiom                  | 9.53 ms                                                | 5.96 ms: 1.60x faster                                               |
| pickle_pure_python      | 455 us                                                 | 287 us: 1.59x faster                                                |
| python_startup          | 14.2 ms                                                | 8.92 ms: 1.59x faster                                               |
| crypto_pyaes            | 118 ms                                                 | 76.5 ms: 1.55x faster                                               |
| float                   | 111 ms                                                 | 71.9 ms: 1.54x faster                                               |
| unpickle_pure_python    | 300 us                                                 | 197 us: 1.52x faster                                                |
| spectral_norm           | 150 ms                                                 | 98.6 ms: 1.52x faster                                               |
| deepcopy_memo           | 52.3 us                                                | 34.5 us: 1.52x faster                                               |
| mako                    | 14.8 ms                                                | 9.81 ms: 1.50x faster                                               |
| unpack_sequence         | 64.7 ns                                                | 43.3 ns: 1.49x faster                                               |
| nbody                   | 142 ms                                                 | 95.4 ms: 1.48x faster                                               |
| scimark_lu              | 163 ms                                                 | 110 ms: 1.48x faster                                                |
| genshi_text             | 30.3 ms                                                | 20.6 ms: 1.47x faster                                               |
| sqlglot_parse           | 2.06 ms                                                | 1.41 ms: 1.45x faster                                               |
| chameleon               | 9.06 ms                                                | 6.28 ms: 1.44x faster                                               |
| sqlglot_transpile       | 2.45 ms                                                | 1.71 ms: 1.43x faster                                               |
| pprint_pformat          | 1.99 sec                                               | 1.39 sec: 1.43x faster                                              |
| html5lib                | 85.9 ms                                                | 60.5 ms: 1.42x faster                                               |
| json_dumps              | 13.5 ms                                                | 9.57 ms: 1.41x faster                                               |
| pprint_safe_repr        | 955 ms                                                 | 681 ms: 1.40x faster                                                |
| scimark_fft             | 424 ms                                                 | 303 ms: 1.40x faster                                                |
| logging_simple          | 8.07 us                                                | 5.77 us: 1.40x faster                                               |
| regex_compile           | 177 ms                                                 | 127 ms: 1.39x faster                                                |
| logging_format          | 8.91 us                                                | 6.41 us: 1.39x faster                                               |
| django_template         | 45.9 ms                                                | 33.1 ms: 1.39x faster                                               |
| aiohttp                 | 1.38 ms                                                | 1.00 ms: 1.38x faster                                               |
| thrift                  | 1.03 ms                                                | 758 us: 1.36x faster                                                |
| async_tree_none         | 717 ms                                                 | 526 ms: 1.36x faster                                                |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.02 ms: 1.36x faster                                               |
| gunicorn                | 1.46 ms                                                | 1.08 ms: 1.36x faster                                               |
| tornado_http            | 127 ms                                                 | 94.2 ms: 1.35x faster                                               |
| genshi_xml              | 63.3 ms                                                | 46.9 ms: 1.35x faster                                               |
| async_tree_io           | 1.77 sec                                               | 1.32 sec: 1.35x faster                                              |
| xml_etree_process       | 74.9 ms                                                | 55.7 ms: 1.34x faster                                               |
| deepcopy                | 442 us                                                 | 330 us: 1.34x faster                                                |
| 2to3                    | 336 ms                                                 | 252 ms: 1.34x faster                                                |
| pycparser               | 1.50 sec                                               | 1.13 sec: 1.33x faster                                              |
| fannkuch                | 486 ms                                                 | 368 ms: 1.32x faster                                                |
| deepcopy_reduce         | 3.82 us                                                | 2.93 us: 1.30x faster                                               |
| mypy2                   | 428 ms                                                 | 330 ms: 1.30x faster                                                |
| async_tree_memoization  | 854 ms                                                 | 659 ms: 1.30x faster                                                |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                                |
| sqlglot_optimize        | 65.3 ms                                                | 51.1 ms: 1.28x faster                                               |
| nqueens                 | 100 ms                                                 | 79.1 ms: 1.26x faster                                               |
| async_tree_cpu_io_mixed | 951 ms                                                 | 755 ms: 1.26x faster                                                |
| docutils                | 3.17 sec                                               | 2.52 sec: 1.26x faster                                              |
| coroutines              | 31.8 ms                                                | 25.6 ms: 1.25x faster                                               |
| sympy_integrate         | 24.3 ms                                                | 19.8 ms: 1.23x faster                                               |
| dulwich_log             | 75.9 ms                                                | 62.3 ms: 1.22x faster                                               |
| sympy_str               | 328 ms                                                 | 270 ms: 1.22x faster                                                |
| bench_thread_pool       | 947 us                                                 | 782 us: 1.21x faster                                                |
| json_loads              | 28.8 us                                                | 23.8 us: 1.21x faster                                               |
| sqlalchemy_declarative  | 165 ms                                                 | 137 ms: 1.21x faster                                                |
| regex_v8                | 25.0 ms                                                | 21.0 ms: 1.19x faster                                               |
| sympy_expand            | 545 ms                                                 | 457 ms: 1.19x faster                                                |
| sqlalchemy_imperative   | 21.2 ms                                                | 18.0 ms: 1.18x faster                                               |
| sympy_sum               | 185 ms                                                 | 157 ms: 1.17x faster                                                |
| xml_etree_generate      | 94.2 ms                                                | 80.8 ms: 1.17x faster                                               |
| json                    | 5.42 ms                                                | 4.67 ms: 1.16x faster                                               |
| mdp                     | 2.82 sec                                               | 2.44 sec: 1.16x faster                                              |
| create_gc_cycles        | 1.67 ms                                                | 1.46 ms: 1.14x faster                                               |
| sqlite_synth            | 2.93 us                                                | 2.58 us: 1.14x faster                                               |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                               |
| pickle_list             | 4.56 us                                                | 4.09 us: 1.11x faster                                               |
| djangocms               | 35.9 us                                                | 32.7 us: 1.10x faster                                               |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                                |
| meteor_contest          | 115 ms                                                 | 105 ms: 1.10x faster                                                |
| gc_traversal            | 3.84 ms                                                | 3.53 ms: 1.09x faster                                               |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                                |
| unpickle                | 14.1 us                                                | 13.2 us: 1.07x faster                                               |
| telco                   | 6.54 ms                                                | 6.42 ms: 1.02x faster                                               |
| generators              | 76.8 ms                                                | 75.4 ms: 1.02x faster                                               |
| pickle                  | 10.3 us                                                | 10.1 us: 1.02x faster                                               |
| regex_dna               | 222 ms                                                 | 219 ms: 1.01x faster                                                |
| async_generators        | 425 ms                                                 | 429 ms: 1.01x slower                                                |
| unpickle_list           | 4.82 us                                                | 4.87 us: 1.01x slower                                               |
| regex_effbot            | 3.23 ms                                                | 3.43 ms: 1.06x slower                                               |
| pidigits                | 190 ms                                                 | 203 ms: 1.07x slower                                                |
| python_startup_no_site  | 5.82 ms                                                | 6.48 ms: 1.11x slower                                               |
| pickle_dict             | 27.3 us                                                | 30.9 us: 1.13x slower                                               |
| coverage                | 72.8 ms                                                | 95.9 ms: 1.32x slower                                               |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                        |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, dask, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x
