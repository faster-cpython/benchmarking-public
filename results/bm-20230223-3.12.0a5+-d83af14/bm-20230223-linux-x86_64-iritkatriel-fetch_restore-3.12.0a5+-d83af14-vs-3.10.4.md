
# Results vs. 3.10.4

- fork: iritkatriel
- ref: fetch_restore
- machine: linux-x86_64
- commit hash: d83af14
- commit date: 2023-02-23
- overall geometric mean: 1.31x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-d83af14 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 247 ms: 1.36x faster                                                 |
| chameleon      | 9.06 ms                                                | 6.39 ms: 1.42x faster                                                |
| docutils       | 3.17 sec                                               | 2.52 sec: 1.26x faster                                               |
| html5lib       | 85.9 ms                                                | 61.2 ms: 1.40x faster                                                |
| tornado_http   | 127 ms                                                 | 94.5 ms: 1.35x faster                                                |
| Geometric mean | (ref)                                                  | 1.36x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-d83af14 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 111 ms                                                 | 73.7 ms: 1.50x faster                                                |
| nbody          | 142 ms                                                 | 95.4 ms: 1.48x faster                                                |
| pidigits       | 190 ms                                                 | 193 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.30x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-d83af14 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 132 ms: 1.34x faster                                                 |
| regex_v8       | 25.0 ms                                                | 21.7 ms: 1.15x faster                                                |
| regex_dna      | 222 ms                                                 | 199 ms: 1.11x faster                                                 |
| regex_effbot   | 3.23 ms                                                | 3.58 ms: 1.11x slower                                                |
| Geometric mean | (ref)                                                  | 1.12x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-d83af14 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 281 us: 1.62x faster                                                 |
| unpickle_pure_python | 300 us                                                 | 198 us: 1.52x faster                                                 |
| json_dumps           | 13.5 ms                                                | 9.44 ms: 1.43x faster                                                |
| xml_etree_process    | 74.9 ms                                                | 55.0 ms: 1.36x faster                                                |
| json_loads           | 28.8 us                                                | 24.1 us: 1.20x faster                                                |
| xml_etree_generate   | 94.2 ms                                                | 80.0 ms: 1.18x faster                                                |
| pickle_list          | 4.56 us                                                | 4.03 us: 1.13x faster                                                |
| xml_etree_iterparse  | 111 ms                                                 | 98.8 ms: 1.13x faster                                                |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                 |
| unpickle             | 14.1 us                                                | 13.3 us: 1.06x faster                                                |
| pickle               | 10.3 us                                                | 9.91 us: 1.04x faster                                                |
| unpickle_list        | 4.82 us                                                | 5.08 us: 1.05x slower                                                |
| pickle_dict          | 27.3 us                                                | 30.8 us: 1.13x slower                                                |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-d83af14 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.99 ms: 1.57x faster                                                |
| python_startup_no_site | 5.82 ms                                                | 6.53 ms: 1.12x slower                                                |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-d83af14 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.90 ms: 1.49x faster                                                |
| genshi_text     | 30.3 ms                                                | 20.6 ms: 1.47x faster                                                |
| django_template | 45.9 ms                                                | 32.9 ms: 1.40x faster                                                |
| genshi_xml      | 63.3 ms                                                | 46.5 ms: 1.36x faster                                                |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                         |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-d83af14 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 29.4 ms: 2.61x faster                                                |
| deltablue               | 7.42 ms                                                | 3.15 ms: 2.36x faster                                                |
| logging_silent          | 175 ns                                                 | 91.2 ns: 1.92x faster                                                |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.86x faster                                                 |
| asyncio_tcp             | 925 ms                                                 | 503 ms: 1.84x faster                                                 |
| richards                | 74.9 ms                                                | 41.2 ms: 1.82x faster                                                |
| go                      | 229 ms                                                 | 133 ms: 1.73x faster                                                 |
| pyflate                 | 673 ms                                                 | 408 ms: 1.65x faster                                                 |
| raytrace                | 464 ms                                                 | 281 ms: 1.65x faster                                                 |
| crypto_pyaes            | 118 ms                                                 | 72.5 ms: 1.63x faster                                                |
| pickle_pure_python      | 455 us                                                 | 281 us: 1.62x faster                                                 |
| scimark_monte_carlo     | 108 ms                                                 | 66.9 ms: 1.62x faster                                                |
| spectral_norm           | 150 ms                                                 | 94.5 ms: 1.59x faster                                                |
| python_startup          | 14.2 ms                                                | 8.99 ms: 1.57x faster                                                |
| chaos                   | 106 ms                                                 | 67.6 ms: 1.57x faster                                                |
| hexiom                  | 9.53 ms                                                | 6.07 ms: 1.57x faster                                                |
| unpickle_pure_python    | 300 us                                                 | 198 us: 1.52x faster                                                 |
| deepcopy_memo           | 52.3 us                                                | 34.6 us: 1.51x faster                                                |
| float                   | 111 ms                                                 | 73.7 ms: 1.50x faster                                                |
| mako                    | 14.8 ms                                                | 9.90 ms: 1.49x faster                                                |
| scimark_lu              | 163 ms                                                 | 110 ms: 1.49x faster                                                 |
| nbody                   | 142 ms                                                 | 95.4 ms: 1.48x faster                                                |
| genshi_text             | 30.3 ms                                                | 20.6 ms: 1.47x faster                                                |
| unpack_sequence         | 64.7 ns                                                | 44.3 ns: 1.46x faster                                                |
| sqlglot_parse           | 2.06 ms                                                | 1.42 ms: 1.45x faster                                                |
| json_dumps              | 13.5 ms                                                | 9.44 ms: 1.43x faster                                                |
| sqlglot_transpile       | 2.45 ms                                                | 1.71 ms: 1.43x faster                                                |
| pprint_pformat          | 1.99 sec                                               | 1.39 sec: 1.43x faster                                               |
| chameleon               | 9.06 ms                                                | 6.39 ms: 1.42x faster                                                |
| pprint_safe_repr        | 955 ms                                                 | 676 ms: 1.41x faster                                                 |
| logging_format          | 8.91 us                                                | 6.33 us: 1.41x faster                                                |
| html5lib                | 85.9 ms                                                | 61.2 ms: 1.40x faster                                                |
| django_template         | 45.9 ms                                                | 32.9 ms: 1.40x faster                                                |
| logging_simple          | 8.07 us                                                | 5.79 us: 1.39x faster                                                |
| pycparser               | 1.50 sec                                               | 1.08 sec: 1.39x faster                                               |
| coroutines              | 31.8 ms                                                | 23.0 ms: 1.38x faster                                                |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                                |
| async_tree_io           | 1.77 sec                                               | 1.30 sec: 1.37x faster                                               |
| async_tree_none         | 717 ms                                                 | 525 ms: 1.36x faster                                                 |
| xml_etree_process       | 74.9 ms                                                | 55.0 ms: 1.36x faster                                                |
| genshi_xml              | 63.3 ms                                                | 46.5 ms: 1.36x faster                                                |
| 2to3                    | 336 ms                                                 | 247 ms: 1.36x faster                                                 |
| tornado_http            | 127 ms                                                 | 94.5 ms: 1.35x faster                                                |
| thrift                  | 1.03 ms                                                | 768 us: 1.35x faster                                                 |
| gunicorn                | 1.46 ms                                                | 1.09 ms: 1.34x faster                                                |
| regex_compile           | 177 ms                                                 | 132 ms: 1.34x faster                                                 |
| fannkuch                | 486 ms                                                 | 365 ms: 1.33x faster                                                 |
| scimark_fft             | 424 ms                                                 | 319 ms: 1.33x faster                                                 |
| deepcopy                | 442 us                                                 | 334 us: 1.32x faster                                                 |
| sqlglot_normalize       | 135 ms                                                 | 103 ms: 1.31x faster                                                 |
| async_tree_memoization  | 854 ms                                                 | 654 ms: 1.31x faster                                                 |
| mypy2                   | 428 ms                                                 | 331 ms: 1.29x faster                                                 |
| sqlglot_optimize        | 65.3 ms                                                | 50.5 ms: 1.29x faster                                                |
| async_tree_cpu_io_mixed | 951 ms                                                 | 741 ms: 1.28x faster                                                 |
| deepcopy_reduce         | 3.82 us                                                | 3.01 us: 1.27x faster                                                |
| docutils                | 3.17 sec                                               | 2.52 sec: 1.26x faster                                               |
| nqueens                 | 100 ms                                                 | 80.1 ms: 1.25x faster                                                |
| sqlalchemy_declarative  | 165 ms                                                 | 135 ms: 1.22x faster                                                 |
| dulwich_log             | 75.9 ms                                                | 62.8 ms: 1.21x faster                                                |
| sympy_expand            | 545 ms                                                 | 453 ms: 1.20x faster                                                 |
| bench_thread_pool       | 947 us                                                 | 788 us: 1.20x faster                                                 |
| json_loads              | 28.8 us                                                | 24.1 us: 1.20x faster                                                |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.8 ms: 1.19x faster                                                |
| sympy_integrate         | 24.3 ms                                                | 20.4 ms: 1.19x faster                                                |
| json                    | 5.42 ms                                                | 4.56 ms: 1.19x faster                                                |
| xml_etree_generate      | 94.2 ms                                                | 80.0 ms: 1.18x faster                                                |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.67 ms: 1.17x faster                                                |
| sympy_str               | 328 ms                                                 | 282 ms: 1.16x faster                                                 |
| regex_v8                | 25.0 ms                                                | 21.7 ms: 1.15x faster                                                |
| mdp                     | 2.82 sec                                               | 2.48 sec: 1.14x faster                                               |
| pathlib                 | 20.0 ms                                                | 17.6 ms: 1.13x faster                                                |
| create_gc_cycles        | 1.67 ms                                                | 1.47 ms: 1.13x faster                                                |
| pickle_list             | 4.56 us                                                | 4.03 us: 1.13x faster                                                |
| xml_etree_iterparse     | 111 ms                                                 | 98.8 ms: 1.13x faster                                                |
| meteor_contest          | 115 ms                                                 | 103 ms: 1.12x faster                                                 |
| sympy_sum               | 185 ms                                                 | 166 ms: 1.11x faster                                                 |
| regex_dna               | 222 ms                                                 | 199 ms: 1.11x faster                                                 |
| sqlite_synth            | 2.93 us                                                | 2.64 us: 1.11x faster                                                |
| djangocms               | 35.9 us                                                | 32.4 us: 1.11x faster                                                |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                 |
| unpickle                | 14.1 us                                                | 13.3 us: 1.06x faster                                                |
| gc_traversal            | 3.84 ms                                                | 3.67 ms: 1.05x faster                                                |
| async_generators        | 425 ms                                                 | 408 ms: 1.04x faster                                                 |
| pickle                  | 10.3 us                                                | 9.91 us: 1.04x faster                                                |
| telco                   | 6.54 ms                                                | 6.45 ms: 1.01x faster                                                |
| pidigits                | 190 ms                                                 | 193 ms: 1.01x slower                                                 |
| unpickle_list           | 4.82 us                                                | 5.08 us: 1.05x slower                                                |
| regex_effbot            | 3.23 ms                                                | 3.58 ms: 1.11x slower                                                |
| python_startup_no_site  | 5.82 ms                                                | 6.53 ms: 1.12x slower                                                |
| pickle_dict             | 27.3 us                                                | 30.8 us: 1.13x slower                                                |
| dask                    | 423 ms                                                 | 500 ms: 1.18x slower                                                 |
| coverage                | 72.8 ms                                                | 95.0 ms: 1.31x slower                                                |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                         |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.25x
