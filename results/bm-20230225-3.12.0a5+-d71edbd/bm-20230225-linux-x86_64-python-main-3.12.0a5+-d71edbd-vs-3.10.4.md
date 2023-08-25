
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: d71edbd
- commit date: 2023-02-25
- overall geometric mean: 1.31x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230225-linux-x86_64-python-main-3.12.0a5+-d71edbd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 248 ms: 1.36x faster                                   |
| chameleon      | 9.06 ms                                                | 6.39 ms: 1.42x faster                                  |
| docutils       | 3.17 sec                                               | 2.54 sec: 1.25x faster                                 |
| html5lib       | 85.9 ms                                                | 61.1 ms: 1.40x faster                                  |
| tornado_http   | 127 ms                                                 | 94.3 ms: 1.35x faster                                  |
| Geometric mean | (ref)                                                  | 1.35x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230225-linux-x86_64-python-main-3.12.0a5+-d71edbd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 111 ms                                                 | 73.9 ms: 1.50x faster                                  |
| nbody          | 142 ms                                                 | 96.6 ms: 1.47x faster                                  |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.30x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230225-linux-x86_64-python-main-3.12.0a5+-d71edbd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 131 ms: 1.35x faster                                   |
| regex_v8       | 25.0 ms                                                | 21.6 ms: 1.16x faster                                  |
| regex_dna      | 222 ms                                                 | 208 ms: 1.07x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.65 ms: 1.13x slower                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230225-linux-x86_64-python-main-3.12.0a5+-d71edbd |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 282 us: 1.61x faster                                   |
| unpickle_pure_python | 300 us                                                 | 195 us: 1.54x faster                                   |
| json_dumps           | 13.5 ms                                                | 9.45 ms: 1.43x faster                                  |
| xml_etree_process    | 74.9 ms                                                | 55.0 ms: 1.36x faster                                  |
| json_loads           | 28.8 us                                                | 23.9 us: 1.21x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 80.3 ms: 1.17x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 99.3 ms: 1.12x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                   |
| pickle_list          | 4.56 us                                                | 4.19 us: 1.09x faster                                  |
| unpickle             | 14.1 us                                                | 13.2 us: 1.07x faster                                  |
| pickle               | 10.3 us                                                | 10.4 us: 1.01x slower                                  |
| unpickle_list        | 4.82 us                                                | 5.02 us: 1.04x slower                                  |
| pickle_dict          | 27.3 us                                                | 31.7 us: 1.16x slower                                  |
| Geometric mean       | (ref)                                                  | 1.17x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230225-linux-x86_64-python-main-3.12.0a5+-d71edbd |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.01 ms: 1.57x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.54 ms: 1.12x slower                                  |
| Geometric mean         | (ref)                                                  | 1.18x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230225-linux-x86_64-python-main-3.12.0a5+-d71edbd |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.89 ms: 1.49x faster                                  |
| genshi_text     | 30.3 ms                                                | 20.4 ms: 1.49x faster                                  |
| django_template | 45.9 ms                                                | 33.0 ms: 1.39x faster                                  |
| genshi_xml      | 63.3 ms                                                | 46.3 ms: 1.37x faster                                  |
| Geometric mean  | (ref)                                                  | 1.43x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230225-linux-x86_64-python-main-3.12.0a5+-d71edbd |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| generators              | 76.8 ms                                                | 29.6 ms: 2.59x faster                                  |
| deltablue               | 7.42 ms                                                | 3.14 ms: 2.37x faster                                  |
| logging_silent          | 175 ns                                                 | 94.4 ns: 1.85x faster                                  |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.85x faster                                   |
| richards                | 74.9 ms                                                | 40.6 ms: 1.85x faster                                  |
| asyncio_tcp             | 925 ms                                                 | 502 ms: 1.84x faster                                   |
| go                      | 229 ms                                                 | 133 ms: 1.72x faster                                   |
| raytrace                | 464 ms                                                 | 280 ms: 1.66x faster                                   |
| pyflate                 | 673 ms                                                 | 407 ms: 1.65x faster                                   |
| scimark_monte_carlo     | 108 ms                                                 | 66.0 ms: 1.64x faster                                  |
| pickle_pure_python      | 455 us                                                 | 282 us: 1.61x faster                                   |
| chaos                   | 106 ms                                                 | 67.0 ms: 1.59x faster                                  |
| crypto_pyaes            | 118 ms                                                 | 74.7 ms: 1.59x faster                                  |
| hexiom                  | 9.53 ms                                                | 6.01 ms: 1.58x faster                                  |
| python_startup          | 14.2 ms                                                | 9.01 ms: 1.57x faster                                  |
| spectral_norm           | 150 ms                                                 | 96.4 ms: 1.56x faster                                  |
| unpickle_pure_python    | 300 us                                                 | 195 us: 1.54x faster                                   |
| unpack_sequence         | 64.7 ns                                                | 42.4 ns: 1.53x faster                                  |
| deepcopy_memo           | 52.3 us                                                | 34.7 us: 1.51x faster                                  |
| scimark_lu              | 163 ms                                                 | 108 ms: 1.51x faster                                   |
| float                   | 111 ms                                                 | 73.9 ms: 1.50x faster                                  |
| mako                    | 14.8 ms                                                | 9.89 ms: 1.49x faster                                  |
| genshi_text             | 30.3 ms                                                | 20.4 ms: 1.49x faster                                  |
| nbody                   | 142 ms                                                 | 96.6 ms: 1.47x faster                                  |
| sqlglot_parse           | 2.06 ms                                                | 1.41 ms: 1.46x faster                                  |
| sqlglot_transpile       | 2.45 ms                                                | 1.70 ms: 1.44x faster                                  |
| json_dumps              | 13.5 ms                                                | 9.45 ms: 1.43x faster                                  |
| chameleon               | 9.06 ms                                                | 6.39 ms: 1.42x faster                                  |
| pprint_pformat          | 1.99 sec                                               | 1.40 sec: 1.42x faster                                 |
| logging_format          | 8.91 us                                                | 6.31 us: 1.41x faster                                  |
| logging_simple          | 8.07 us                                                | 5.72 us: 1.41x faster                                  |
| html5lib                | 85.9 ms                                                | 61.1 ms: 1.40x faster                                  |
| pprint_safe_repr        | 955 ms                                                 | 681 ms: 1.40x faster                                   |
| django_template         | 45.9 ms                                                | 33.0 ms: 1.39x faster                                  |
| coroutines              | 31.8 ms                                                | 23.0 ms: 1.38x faster                                  |
| pycparser               | 1.50 sec                                               | 1.09 sec: 1.38x faster                                 |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                  |
| async_tree_io           | 1.77 sec                                               | 1.30 sec: 1.37x faster                                 |
| genshi_xml              | 63.3 ms                                                | 46.3 ms: 1.37x faster                                  |
| async_tree_none         | 717 ms                                                 | 526 ms: 1.36x faster                                   |
| xml_etree_process       | 74.9 ms                                                | 55.0 ms: 1.36x faster                                  |
| 2to3                    | 336 ms                                                 | 248 ms: 1.36x faster                                   |
| regex_compile           | 177 ms                                                 | 131 ms: 1.35x faster                                   |
| tornado_http            | 127 ms                                                 | 94.3 ms: 1.35x faster                                  |
| gunicorn                | 1.46 ms                                                | 1.09 ms: 1.34x faster                                  |
| thrift                  | 1.03 ms                                                | 771 us: 1.34x faster                                   |
| scimark_fft             | 424 ms                                                 | 317 ms: 1.34x faster                                   |
| fannkuch                | 486 ms                                                 | 364 ms: 1.34x faster                                   |
| async_tree_memoization  | 854 ms                                                 | 640 ms: 1.34x faster                                   |
| deepcopy                | 442 us                                                 | 332 us: 1.33x faster                                   |
| sqlglot_normalize       | 135 ms                                                 | 103 ms: 1.32x faster                                   |
| sqlglot_optimize        | 65.3 ms                                                | 50.5 ms: 1.29x faster                                  |
| mypy2                   | 428 ms                                                 | 332 ms: 1.29x faster                                   |
| async_tree_cpu_io_mixed | 951 ms                                                 | 739 ms: 1.29x faster                                   |
| deepcopy_reduce         | 3.82 us                                                | 2.99 us: 1.28x faster                                  |
| nqueens                 | 100 ms                                                 | 80.0 ms: 1.25x faster                                  |
| docutils                | 3.17 sec                                               | 2.54 sec: 1.25x faster                                 |
| json_loads              | 28.8 us                                                | 23.9 us: 1.21x faster                                  |
| dulwich_log             | 75.9 ms                                                | 63.1 ms: 1.20x faster                                  |
| bench_thread_pool       | 947 us                                                 | 787 us: 1.20x faster                                   |
| sqlalchemy_declarative  | 165 ms                                                 | 138 ms: 1.20x faster                                   |
| sympy_expand            | 545 ms                                                 | 454 ms: 1.20x faster                                   |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.7 ms: 1.20x faster                                  |
| json                    | 5.42 ms                                                | 4.54 ms: 1.19x faster                                  |
| sympy_integrate         | 24.3 ms                                                | 20.4 ms: 1.19x faster                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.62 ms: 1.18x faster                                  |
| xml_etree_generate      | 94.2 ms                                                | 80.3 ms: 1.17x faster                                  |
| sympy_str               | 328 ms                                                 | 282 ms: 1.17x faster                                   |
| regex_v8                | 25.0 ms                                                | 21.6 ms: 1.16x faster                                  |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                  |
| xml_etree_iterparse     | 111 ms                                                 | 99.3 ms: 1.12x faster                                  |
| sqlite_synth            | 2.93 us                                                | 2.62 us: 1.12x faster                                  |
| create_gc_cycles        | 1.67 ms                                                | 1.50 ms: 1.11x faster                                  |
| sympy_sum               | 185 ms                                                 | 166 ms: 1.11x faster                                   |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.11x faster                                   |
| djangocms               | 35.9 us                                                | 32.5 us: 1.11x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                   |
| pickle_list             | 4.56 us                                                | 4.19 us: 1.09x faster                                  |
| unpickle                | 14.1 us                                                | 13.2 us: 1.07x faster                                  |
| regex_dna               | 222 ms                                                 | 208 ms: 1.07x faster                                   |
| mdp                     | 2.82 sec                                               | 2.66 sec: 1.06x faster                                 |
| async_generators        | 425 ms                                                 | 420 ms: 1.01x faster                                   |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                   |
| gc_traversal            | 3.84 ms                                                | 3.83 ms: 1.00x faster                                  |
| pickle                  | 10.3 us                                                | 10.4 us: 1.01x slower                                  |
| unpickle_list           | 4.82 us                                                | 5.02 us: 1.04x slower                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.54 ms: 1.12x slower                                  |
| regex_effbot            | 3.23 ms                                                | 3.65 ms: 1.13x slower                                  |
| pickle_dict             | 27.3 us                                                | 31.7 us: 1.16x slower                                  |
| dask                    | 423 ms                                                 | 499 ms: 1.18x slower                                   |
| coverage                | 72.8 ms                                                | 96.5 ms: 1.33x slower                                  |
| Geometric mean          | (ref)                                                  | 1.31x faster                                           |

Benchmark hidden because not significant (2): bench_mp_pool, telco
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.25x
