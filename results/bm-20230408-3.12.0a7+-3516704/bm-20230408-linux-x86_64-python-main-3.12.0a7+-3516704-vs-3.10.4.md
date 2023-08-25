
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 3516704
- commit date: 2023-04-08
- overall geometric mean: 1.31x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230408-linux-x86_64-python-main-3.12.0a7+-3516704 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 251 ms: 1.34x faster                                   |
| chameleon      | 9.06 ms                                                | 6.51 ms: 1.39x faster                                  |
| docutils       | 3.17 sec                                               | 2.54 sec: 1.25x faster                                 |
| html5lib       | 85.9 ms                                                | 61.4 ms: 1.40x faster                                  |
| tornado_http   | 127 ms                                                 | 94.0 ms: 1.36x faster                                  |
| Geometric mean | (ref)                                                  | 1.35x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230408-linux-x86_64-python-main-3.12.0a7+-3516704 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 142 ms                                                 | 86.6 ms: 1.64x faster                                  |
| float          | 111 ms                                                 | 73.6 ms: 1.50x faster                                  |
| pidigits       | 190 ms                                                 | 188 ms: 1.01x faster                                   |
| Geometric mean | (ref)                                                  | 1.35x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230408-linux-x86_64-python-main-3.12.0a7+-3516704 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 135 ms: 1.31x faster                                   |
| regex_v8       | 25.0 ms                                                | 22.1 ms: 1.13x faster                                  |
| regex_dna      | 222 ms                                                 | 204 ms: 1.09x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.36 ms: 1.04x slower                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230408-linux-x86_64-python-main-3.12.0a7+-3516704 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 288 us: 1.58x faster                                   |
| unpickle_pure_python | 300 us                                                 | 200 us: 1.50x faster                                   |
| json_dumps           | 13.5 ms                                                | 9.54 ms: 1.42x faster                                  |
| xml_etree_process    | 74.9 ms                                                | 55.9 ms: 1.34x faster                                  |
| json_loads           | 28.8 us                                                | 24.3 us: 1.19x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 81.2 ms: 1.16x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                   |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                   |
| pickle_list          | 4.56 us                                                | 4.29 us: 1.06x faster                                  |
| pickle               | 10.3 us                                                | 10.7 us: 1.04x slower                                  |
| unpickle_list        | 4.82 us                                                | 5.07 us: 1.05x slower                                  |
| pickle_dict          | 27.3 us                                                | 31.9 us: 1.17x slower                                  |
| Geometric mean       | (ref)                                                  | 1.15x faster                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230408-linux-x86_64-python-main-3.12.0a7+-3516704 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.82 ms: 1.60x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.51 ms: 1.12x slower                                  |
| Geometric mean         | (ref)                                                  | 1.20x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230408-linux-x86_64-python-main-3.12.0a7+-3516704 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.97 ms: 1.48x faster                                  |
| genshi_text     | 30.3 ms                                                | 21.3 ms: 1.42x faster                                  |
| django_template | 45.9 ms                                                | 33.0 ms: 1.39x faster                                  |
| genshi_xml      | 63.3 ms                                                | 47.8 ms: 1.32x faster                                  |
| Geometric mean  | (ref)                                                  | 1.40x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230408-linux-x86_64-python-main-3.12.0a7+-3516704 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| generators              | 76.8 ms                                                | 29.0 ms: 2.65x faster                                  |
| deltablue               | 7.42 ms                                                | 3.24 ms: 2.29x faster                                  |
| logging_silent          | 175 ns                                                 | 94.3 ns: 1.86x faster                                  |
| asyncio_tcp             | 925 ms                                                 | 506 ms: 1.83x faster                                   |
| scimark_sor             | 197 ms                                                 | 112 ms: 1.76x faster                                   |
| richards                | 74.9 ms                                                | 43.6 ms: 1.72x faster                                  |
| sqlglot_parse           | 2.06 ms                                                | 1.21 ms: 1.70x faster                                  |
| go                      | 229 ms                                                 | 137 ms: 1.67x faster                                   |
| sqlglot_transpile       | 2.45 ms                                                | 1.49 ms: 1.64x faster                                  |
| raytrace                | 464 ms                                                 | 283 ms: 1.64x faster                                   |
| nbody                   | 142 ms                                                 | 86.6 ms: 1.64x faster                                  |
| scimark_monte_carlo     | 108 ms                                                 | 66.7 ms: 1.62x faster                                  |
| chaos                   | 106 ms                                                 | 65.7 ms: 1.62x faster                                  |
| crypto_pyaes            | 118 ms                                                 | 73.7 ms: 1.61x faster                                  |
| python_startup          | 14.2 ms                                                | 8.82 ms: 1.60x faster                                  |
| pyflate                 | 673 ms                                                 | 420 ms: 1.60x faster                                   |
| hexiom                  | 9.53 ms                                                | 5.98 ms: 1.59x faster                                  |
| spectral_norm           | 150 ms                                                 | 94.5 ms: 1.59x faster                                  |
| pickle_pure_python      | 455 us                                                 | 288 us: 1.58x faster                                   |
| scimark_lu              | 163 ms                                                 | 104 ms: 1.57x faster                                   |
| deepcopy_memo           | 52.3 us                                                | 34.1 us: 1.53x faster                                  |
| unpickle_pure_python    | 300 us                                                 | 200 us: 1.50x faster                                   |
| float                   | 111 ms                                                 | 73.6 ms: 1.50x faster                                  |
| unpack_sequence         | 64.7 ns                                                | 43.5 ns: 1.49x faster                                  |
| mako                    | 14.8 ms                                                | 9.97 ms: 1.48x faster                                  |
| logging_simple          | 8.07 us                                                | 5.65 us: 1.43x faster                                  |
| genshi_text             | 30.3 ms                                                | 21.3 ms: 1.42x faster                                  |
| scimark_fft             | 424 ms                                                 | 298 ms: 1.42x faster                                   |
| json_dumps              | 13.5 ms                                                | 9.54 ms: 1.42x faster                                  |
| logging_format          | 8.91 us                                                | 6.32 us: 1.41x faster                                  |
| html5lib                | 85.9 ms                                                | 61.4 ms: 1.40x faster                                  |
| coroutines              | 31.8 ms                                                | 22.8 ms: 1.39x faster                                  |
| chameleon               | 9.06 ms                                                | 6.51 ms: 1.39x faster                                  |
| django_template         | 45.9 ms                                                | 33.0 ms: 1.39x faster                                  |
| pprint_pformat          | 1.99 sec                                               | 1.43 sec: 1.39x faster                                 |
| async_tree_none         | 717 ms                                                 | 523 ms: 1.37x faster                                   |
| pprint_safe_repr        | 955 ms                                                 | 697 ms: 1.37x faster                                   |
| async_tree_io           | 1.77 sec                                               | 1.30 sec: 1.37x faster                                 |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.99 ms: 1.37x faster                                  |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.36x faster                                  |
| deepcopy                | 442 us                                                 | 324 us: 1.36x faster                                   |
| tornado_http            | 127 ms                                                 | 94.0 ms: 1.36x faster                                  |
| pycparser               | 1.50 sec                                               | 1.11 sec: 1.35x faster                                 |
| async_tree_memoization  | 854 ms                                                 | 637 ms: 1.34x faster                                   |
| 2to3                    | 336 ms                                                 | 251 ms: 1.34x faster                                   |
| xml_etree_process       | 74.9 ms                                                | 55.9 ms: 1.34x faster                                  |
| thrift                  | 1.03 ms                                                | 779 us: 1.33x faster                                   |
| genshi_xml              | 63.3 ms                                                | 47.8 ms: 1.32x faster                                  |
| gunicorn                | 1.46 ms                                                | 1.10 ms: 1.32x faster                                  |
| deepcopy_reduce         | 3.82 us                                                | 2.90 us: 1.32x faster                                  |
| regex_compile           | 177 ms                                                 | 135 ms: 1.31x faster                                   |
| fannkuch                | 486 ms                                                 | 375 ms: 1.30x faster                                   |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.29x faster                                   |
| sqlglot_optimize        | 65.3 ms                                                | 50.8 ms: 1.29x faster                                  |
| async_tree_cpu_io_mixed | 951 ms                                                 | 739 ms: 1.29x faster                                   |
| mypy2                   | 428 ms                                                 | 336 ms: 1.28x faster                                   |
| docutils                | 3.17 sec                                               | 2.54 sec: 1.25x faster                                 |
| nqueens                 | 100 ms                                                 | 80.5 ms: 1.24x faster                                  |
| comprehensions          | 26.8 us                                                | 21.8 us: 1.23x faster                                  |
| bench_thread_pool       | 947 us                                                 | 786 us: 1.20x faster                                   |
| sympy_integrate         | 24.3 ms                                                | 20.3 ms: 1.19x faster                                  |
| dulwich_log             | 75.9 ms                                                | 63.6 ms: 1.19x faster                                  |
| sympy_expand            | 545 ms                                                 | 458 ms: 1.19x faster                                   |
| json_loads              | 28.8 us                                                | 24.3 us: 1.19x faster                                  |
| sqlalchemy_declarative  | 165 ms                                                 | 139 ms: 1.19x faster                                   |
| sqlalchemy_imperative   | 21.2 ms                                                | 18.1 ms: 1.17x faster                                  |
| sympy_str               | 328 ms                                                 | 282 ms: 1.16x faster                                   |
| xml_etree_generate      | 94.2 ms                                                | 81.2 ms: 1.16x faster                                  |
| json                    | 5.42 ms                                                | 4.71 ms: 1.15x faster                                  |
| create_gc_cycles        | 1.67 ms                                                | 1.46 ms: 1.14x faster                                  |
| regex_v8                | 25.0 ms                                                | 22.1 ms: 1.13x faster                                  |
| sympy_sum               | 185 ms                                                 | 164 ms: 1.12x faster                                   |
| meteor_contest          | 115 ms                                                 | 102 ms: 1.12x faster                                   |
| sqlite_synth            | 2.93 us                                                | 2.63 us: 1.12x faster                                  |
| djangocms               | 35.9 us                                                | 32.3 us: 1.11x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                   |
| pathlib                 | 20.0 ms                                                | 18.3 ms: 1.09x faster                                  |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                   |
| regex_dna               | 222 ms                                                 | 204 ms: 1.09x faster                                   |
| mdp                     | 2.82 sec                                               | 2.62 sec: 1.08x faster                                 |
| pickle_list             | 4.56 us                                                | 4.29 us: 1.06x faster                                  |
| gc_traversal            | 3.84 ms                                                | 3.65 ms: 1.05x faster                                  |
| async_generators        | 425 ms                                                 | 412 ms: 1.03x faster                                   |
| pidigits                | 190 ms                                                 | 188 ms: 1.01x faster                                   |
| pickle                  | 10.3 us                                                | 10.7 us: 1.04x slower                                  |
| regex_effbot            | 3.23 ms                                                | 3.36 ms: 1.04x slower                                  |
| unpickle_list           | 4.82 us                                                | 5.07 us: 1.05x slower                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.51 ms: 1.12x slower                                  |
| pickle_dict             | 27.3 us                                                | 31.9 us: 1.17x slower                                  |
| dask                    | 423 ms                                                 | 502 ms: 1.19x slower                                   |
| coverage                | 72.8 ms                                                | 97.6 ms: 1.34x slower                                  |
| Geometric mean          | (ref)                                                  | 1.31x faster                                           |

Benchmark hidden because not significant (3): unpickle, telco, bench_mp_pool
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x
