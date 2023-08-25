
# Results vs. 3.10.4

- fork: iritkatriel
- ref: fetch_restore
- machine: linux-x86_64
- commit hash: 19b61a7
- commit date: 2023-02-23
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-19b61a7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 251 ms: 1.34x faster                                                 |
| chameleon      | 9.06 ms                                                | 6.48 ms: 1.40x faster                                                |
| docutils       | 3.17 sec                                               | 2.55 sec: 1.24x faster                                               |
| html5lib       | 85.9 ms                                                | 62.4 ms: 1.38x faster                                                |
| tornado_http   | 127 ms                                                 | 95.3 ms: 1.34x faster                                                |
| Geometric mean | (ref)                                                  | 1.34x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-19b61a7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 93.6 ms: 1.51x faster                                                |
| float          | 111 ms                                                 | 73.5 ms: 1.50x faster                                                |
| pidigits       | 190 ms                                                 | 193 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.31x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-19b61a7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 133 ms: 1.33x faster                                                 |
| regex_v8       | 25.0 ms                                                | 22.1 ms: 1.13x faster                                                |
| regex_dna      | 222 ms                                                 | 210 ms: 1.05x faster                                                 |
| regex_effbot   | 3.23 ms                                                | 3.27 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                  | 1.12x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-19b61a7 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 293 us: 1.55x faster                                                 |
| unpickle_pure_python | 300 us                                                 | 203 us: 1.48x faster                                                 |
| json_dumps           | 13.5 ms                                                | 9.34 ms: 1.45x faster                                                |
| xml_etree_process    | 74.9 ms                                                | 55.8 ms: 1.34x faster                                                |
| json_loads           | 28.8 us                                                | 23.8 us: 1.21x faster                                                |
| pickle_list          | 4.56 us                                                | 3.92 us: 1.16x faster                                                |
| xml_etree_generate   | 94.2 ms                                                | 81.5 ms: 1.16x faster                                                |
| xml_etree_iterparse  | 111 ms                                                 | 98.5 ms: 1.13x faster                                                |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                 |
| unpickle             | 14.1 us                                                | 13.6 us: 1.04x faster                                                |
| pickle               | 10.3 us                                                | 9.95 us: 1.03x faster                                                |
| unpickle_list        | 4.82 us                                                | 4.91 us: 1.02x slower                                                |
| pickle_dict          | 27.3 us                                                | 30.1 us: 1.10x slower                                                |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-19b61a7 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.97 ms: 1.58x faster                                                |
| python_startup_no_site | 5.82 ms                                                | 6.51 ms: 1.12x slower                                                |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-19b61a7 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.93 ms: 1.49x faster                                                |
| genshi_text     | 30.3 ms                                                | 21.5 ms: 1.41x faster                                                |
| django_template | 45.9 ms                                                | 33.5 ms: 1.37x faster                                                |
| genshi_xml      | 63.3 ms                                                | 48.1 ms: 1.32x faster                                                |
| Geometric mean  | (ref)                                                  | 1.39x faster                                                         |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-19b61a7 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 30.5 ms: 2.52x faster                                                |
| deltablue               | 7.42 ms                                                | 3.24 ms: 2.29x faster                                                |
| logging_silent          | 175 ns                                                 | 95.4 ns: 1.84x faster                                                |
| asyncio_tcp             | 925 ms                                                 | 505 ms: 1.83x faster                                                 |
| scimark_sor             | 197 ms                                                 | 109 ms: 1.80x faster                                                 |
| richards                | 74.9 ms                                                | 43.4 ms: 1.72x faster                                                |
| go                      | 229 ms                                                 | 136 ms: 1.68x faster                                                 |
| pyflate                 | 673 ms                                                 | 411 ms: 1.64x faster                                                 |
| scimark_monte_carlo     | 108 ms                                                 | 66.2 ms: 1.64x faster                                                |
| crypto_pyaes            | 118 ms                                                 | 73.8 ms: 1.61x faster                                                |
| raytrace                | 464 ms                                                 | 289 ms: 1.60x faster                                                 |
| python_startup          | 14.2 ms                                                | 8.97 ms: 1.58x faster                                                |
| spectral_norm           | 150 ms                                                 | 95.9 ms: 1.56x faster                                                |
| pickle_pure_python      | 455 us                                                 | 293 us: 1.55x faster                                                 |
| chaos                   | 106 ms                                                 | 68.5 ms: 1.55x faster                                                |
| unpack_sequence         | 64.7 ns                                                | 41.9 ns: 1.54x faster                                                |
| hexiom                  | 9.53 ms                                                | 6.22 ms: 1.53x faster                                                |
| nbody                   | 142 ms                                                 | 93.6 ms: 1.51x faster                                                |
| float                   | 111 ms                                                 | 73.5 ms: 1.50x faster                                                |
| mako                    | 14.8 ms                                                | 9.93 ms: 1.49x faster                                                |
| scimark_lu              | 163 ms                                                 | 110 ms: 1.48x faster                                                 |
| unpickle_pure_python    | 300 us                                                 | 203 us: 1.48x faster                                                 |
| deepcopy_memo           | 52.3 us                                                | 35.6 us: 1.47x faster                                                |
| json_dumps              | 13.5 ms                                                | 9.34 ms: 1.45x faster                                                |
| sqlglot_parse           | 2.06 ms                                                | 1.44 ms: 1.42x faster                                                |
| coroutines              | 31.8 ms                                                | 22.3 ms: 1.42x faster                                                |
| pprint_pformat          | 1.99 sec                                               | 1.41 sec: 1.41x faster                                               |
| genshi_text             | 30.3 ms                                                | 21.5 ms: 1.41x faster                                                |
| sqlglot_transpile       | 2.45 ms                                                | 1.74 ms: 1.40x faster                                                |
| chameleon               | 9.06 ms                                                | 6.48 ms: 1.40x faster                                                |
| pprint_safe_repr        | 955 ms                                                 | 686 ms: 1.39x faster                                                 |
| html5lib                | 85.9 ms                                                | 62.4 ms: 1.38x faster                                                |
| async_tree_io           | 1.77 sec                                               | 1.29 sec: 1.37x faster                                               |
| async_tree_none         | 717 ms                                                 | 522 ms: 1.37x faster                                                 |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                                |
| django_template         | 45.9 ms                                                | 33.5 ms: 1.37x faster                                                |
| logging_format          | 8.91 us                                                | 6.51 us: 1.37x faster                                                |
| logging_simple          | 8.07 us                                                | 5.93 us: 1.36x faster                                                |
| scimark_fft             | 424 ms                                                 | 312 ms: 1.36x faster                                                 |
| xml_etree_process       | 74.9 ms                                                | 55.8 ms: 1.34x faster                                                |
| pycparser               | 1.50 sec                                               | 1.12 sec: 1.34x faster                                               |
| 2to3                    | 336 ms                                                 | 251 ms: 1.34x faster                                                 |
| tornado_http            | 127 ms                                                 | 95.3 ms: 1.34x faster                                                |
| gunicorn                | 1.46 ms                                                | 1.09 ms: 1.33x faster                                                |
| thrift                  | 1.03 ms                                                | 779 us: 1.33x faster                                                 |
| regex_compile           | 177 ms                                                 | 133 ms: 1.33x faster                                                 |
| fannkuch                | 486 ms                                                 | 367 ms: 1.32x faster                                                 |
| genshi_xml              | 63.3 ms                                                | 48.1 ms: 1.32x faster                                                |
| deepcopy                | 442 us                                                 | 341 us: 1.30x faster                                                 |
| async_tree_memoization  | 854 ms                                                 | 662 ms: 1.29x faster                                                 |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                                 |
| async_tree_cpu_io_mixed | 951 ms                                                 | 738 ms: 1.29x faster                                                 |
| mypy2                   | 428 ms                                                 | 334 ms: 1.28x faster                                                 |
| sqlglot_optimize        | 65.3 ms                                                | 51.2 ms: 1.28x faster                                                |
| docutils                | 3.17 sec                                               | 2.55 sec: 1.24x faster                                               |
| deepcopy_reduce         | 3.82 us                                                | 3.08 us: 1.24x faster                                                |
| nqueens                 | 100 ms                                                 | 81.6 ms: 1.23x faster                                                |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.51 ms: 1.21x faster                                                |
| json_loads              | 28.8 us                                                | 23.8 us: 1.21x faster                                                |
| sqlalchemy_declarative  | 165 ms                                                 | 137 ms: 1.21x faster                                                 |
| dulwich_log             | 75.9 ms                                                | 63.3 ms: 1.20x faster                                                |
| bench_thread_pool       | 947 us                                                 | 794 us: 1.19x faster                                                 |
| json                    | 5.42 ms                                                | 4.55 ms: 1.19x faster                                                |
| sympy_integrate         | 24.3 ms                                                | 20.7 ms: 1.17x faster                                                |
| sympy_expand            | 545 ms                                                 | 465 ms: 1.17x faster                                                 |
| sqlalchemy_imperative   | 21.2 ms                                                | 18.2 ms: 1.16x faster                                                |
| pickle_list             | 4.56 us                                                | 3.92 us: 1.16x faster                                                |
| xml_etree_generate      | 94.2 ms                                                | 81.5 ms: 1.16x faster                                                |
| sympy_str               | 328 ms                                                 | 287 ms: 1.14x faster                                                 |
| create_gc_cycles        | 1.67 ms                                                | 1.47 ms: 1.14x faster                                                |
| pathlib                 | 20.0 ms                                                | 17.6 ms: 1.13x faster                                                |
| regex_v8                | 25.0 ms                                                | 22.1 ms: 1.13x faster                                                |
| xml_etree_iterparse     | 111 ms                                                 | 98.5 ms: 1.13x faster                                                |
| sqlite_synth            | 2.93 us                                                | 2.60 us: 1.13x faster                                                |
| mdp                     | 2.82 sec                                               | 2.53 sec: 1.11x faster                                               |
| meteor_contest          | 115 ms                                                 | 103 ms: 1.11x faster                                                 |
| djangocms               | 35.9 us                                                | 32.5 us: 1.10x faster                                                |
| sympy_sum               | 185 ms                                                 | 168 ms: 1.10x faster                                                 |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                 |
| regex_dna               | 222 ms                                                 | 210 ms: 1.05x faster                                                 |
| unpickle                | 14.1 us                                                | 13.6 us: 1.04x faster                                                |
| pickle                  | 10.3 us                                                | 9.95 us: 1.03x faster                                                |
| async_generators        | 425 ms                                                 | 411 ms: 1.03x faster                                                 |
| telco                   | 6.54 ms                                                | 6.42 ms: 1.02x faster                                                |
| regex_effbot            | 3.23 ms                                                | 3.27 ms: 1.01x slower                                                |
| pidigits                | 190 ms                                                 | 193 ms: 1.01x slower                                                 |
| unpickle_list           | 4.82 us                                                | 4.91 us: 1.02x slower                                                |
| gc_traversal            | 3.84 ms                                                | 4.07 ms: 1.06x slower                                                |
| pickle_dict             | 27.3 us                                                | 30.1 us: 1.10x slower                                                |
| python_startup_no_site  | 5.82 ms                                                | 6.51 ms: 1.12x slower                                                |
| dask                    | 423 ms                                                 | 509 ms: 1.20x slower                                                 |
| coverage                | 72.8 ms                                                | 95.9 ms: 1.32x slower                                                |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                         |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x
