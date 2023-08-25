
# Results vs. 3.10.4

- fork: python
- ref: 3b9d793efcfd2c00c14f
- machine: linux-x86_64
- commit hash: 3b9d793
- commit date: 2022-11-14
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221114-linux-x86_64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 245 ms: 1.37x faster                                                  |
| chameleon      | 9.06 ms                                                | 6.30 ms: 1.44x faster                                                 |
| docutils       | 3.17 sec                                               | 2.50 sec: 1.27x faster                                                |
| html5lib       | 85.9 ms                                                | 58.9 ms: 1.46x faster                                                 |
| tornado_http   | 127 ms                                                 | 93.1 ms: 1.37x faster                                                 |
| Geometric mean | (ref)                                                  | 1.38x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221114-linux-x86_64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 111 ms                                                 | 72.0 ms: 1.53x faster                                                 |
| nbody          | 142 ms                                                 | 93.9 ms: 1.51x faster                                                 |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.32x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221114-linux-x86_64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 127 ms: 1.39x faster                                                  |
| regex_v8       | 25.0 ms                                                | 21.1 ms: 1.19x faster                                                 |
| regex_dna      | 222 ms                                                 | 208 ms: 1.07x faster                                                  |
| regex_effbot   | 3.23 ms                                                | 3.47 ms: 1.08x slower                                                 |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221114-linux-x86_64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 283 us: 1.61x faster                                                  |
| unpickle_pure_python | 300 us                                                 | 200 us: 1.50x faster                                                  |
| json_dumps           | 13.5 ms                                                | 9.66 ms: 1.40x faster                                                 |
| xml_etree_process    | 74.9 ms                                                | 53.9 ms: 1.39x faster                                                 |
| xml_etree_generate   | 94.2 ms                                                | 77.2 ms: 1.22x faster                                                 |
| json_loads           | 28.8 us                                                | 23.9 us: 1.21x faster                                                 |
| pickle_list          | 4.56 us                                                | 4.06 us: 1.12x faster                                                 |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                                  |
| unpickle             | 14.1 us                                                | 12.9 us: 1.09x faster                                                 |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                  |
| pickle               | 10.3 us                                                | 9.88 us: 1.04x faster                                                 |
| unpickle_list        | 4.82 us                                                | 4.98 us: 1.03x slower                                                 |
| pickle_dict          | 27.3 us                                                | 30.8 us: 1.13x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221114-linux-x86_64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.58 ms: 1.65x faster                                                 |
| python_startup_no_site | 5.82 ms                                                | 6.12 ms: 1.05x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.25x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221114-linux-x86_64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.39 ms: 1.57x faster                                                 |
| genshi_text     | 30.3 ms                                                | 20.2 ms: 1.50x faster                                                 |
| django_template | 45.9 ms                                                | 32.8 ms: 1.40x faster                                                 |
| genshi_xml      | 63.3 ms                                                | 47.0 ms: 1.35x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221114-linux-x86_64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.22 ms: 2.30x faster                                                 |
| logging_silent          | 175 ns                                                 | 93.4 ns: 1.87x faster                                                 |
| scimark_sor             | 197 ms                                                 | 105 ms: 1.87x faster                                                  |
| richards                | 74.9 ms                                                | 41.8 ms: 1.79x faster                                                 |
| go                      | 229 ms                                                 | 135 ms: 1.70x faster                                                  |
| raytrace                | 464 ms                                                 | 277 ms: 1.68x faster                                                  |
| pyflate                 | 673 ms                                                 | 402 ms: 1.67x faster                                                  |
| python_startup          | 14.2 ms                                                | 8.58 ms: 1.65x faster                                                 |
| chaos                   | 106 ms                                                 | 65.8 ms: 1.61x faster                                                 |
| pickle_pure_python      | 455 us                                                 | 283 us: 1.61x faster                                                  |
| scimark_monte_carlo     | 108 ms                                                 | 68.0 ms: 1.59x faster                                                 |
| crypto_pyaes            | 118 ms                                                 | 74.6 ms: 1.59x faster                                                 |
| spectral_norm           | 150 ms                                                 | 94.9 ms: 1.58x faster                                                 |
| hexiom                  | 9.53 ms                                                | 6.04 ms: 1.58x faster                                                 |
| mako                    | 14.8 ms                                                | 9.39 ms: 1.57x faster                                                 |
| deepcopy_memo           | 52.3 us                                                | 33.6 us: 1.56x faster                                                 |
| sqlglot_parse           | 2.06 ms                                                | 1.33 ms: 1.55x faster                                                 |
| float                   | 111 ms                                                 | 72.0 ms: 1.53x faster                                                 |
| sqlglot_transpile       | 2.45 ms                                                | 1.62 ms: 1.51x faster                                                 |
| scimark_lu              | 163 ms                                                 | 108 ms: 1.51x faster                                                  |
| nbody                   | 142 ms                                                 | 93.9 ms: 1.51x faster                                                 |
| unpickle_pure_python    | 300 us                                                 | 200 us: 1.50x faster                                                  |
| genshi_text             | 30.3 ms                                                | 20.2 ms: 1.50x faster                                                 |
| html5lib                | 85.9 ms                                                | 58.9 ms: 1.46x faster                                                 |
| chameleon               | 9.06 ms                                                | 6.30 ms: 1.44x faster                                                 |
| pprint_pformat          | 1.99 sec                                               | 1.39 sec: 1.43x faster                                                |
| unpack_sequence         | 64.7 ns                                                | 45.7 ns: 1.42x faster                                                 |
| logging_simple          | 8.07 us                                                | 5.70 us: 1.42x faster                                                 |
| logging_format          | 8.91 us                                                | 6.30 us: 1.41x faster                                                 |
| json_dumps              | 13.5 ms                                                | 9.66 ms: 1.40x faster                                                 |
| django_template         | 45.9 ms                                                | 32.8 ms: 1.40x faster                                                 |
| pycparser               | 1.50 sec                                               | 1.08 sec: 1.40x faster                                                |
| pprint_safe_repr        | 955 ms                                                 | 685 ms: 1.39x faster                                                  |
| regex_compile           | 177 ms                                                 | 127 ms: 1.39x faster                                                  |
| xml_etree_process       | 74.9 ms                                                | 53.9 ms: 1.39x faster                                                 |
| aiohttp                 | 1.38 ms                                                | 999 us: 1.38x faster                                                  |
| thrift                  | 1.03 ms                                                | 748 us: 1.38x faster                                                  |
| scimark_fft             | 424 ms                                                 | 309 ms: 1.37x faster                                                  |
| 2to3                    | 336 ms                                                 | 245 ms: 1.37x faster                                                  |
| tornado_http            | 127 ms                                                 | 93.1 ms: 1.37x faster                                                 |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.00 ms: 1.36x faster                                                 |
| async_tree_none         | 717 ms                                                 | 527 ms: 1.36x faster                                                  |
| gunicorn                | 1.46 ms                                                | 1.08 ms: 1.35x faster                                                 |
| deepcopy                | 442 us                                                 | 328 us: 1.35x faster                                                  |
| genshi_xml              | 63.3 ms                                                | 47.0 ms: 1.35x faster                                                 |
| async_tree_io           | 1.77 sec                                               | 1.32 sec: 1.34x faster                                                |
| deepcopy_reduce         | 3.82 us                                                | 2.89 us: 1.32x faster                                                 |
| fannkuch                | 486 ms                                                 | 369 ms: 1.32x faster                                                  |
| mypy2                   | 428 ms                                                 | 325 ms: 1.32x faster                                                  |
| async_tree_memoization  | 854 ms                                                 | 653 ms: 1.31x faster                                                  |
| async_tree_cpu_io_mixed | 951 ms                                                 | 730 ms: 1.30x faster                                                  |
| coroutines              | 31.8 ms                                                | 24.7 ms: 1.29x faster                                                 |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.28x faster                                                  |
| sqlglot_optimize        | 65.3 ms                                                | 51.0 ms: 1.28x faster                                                 |
| docutils                | 3.17 sec                                               | 2.50 sec: 1.27x faster                                                |
| nqueens                 | 100 ms                                                 | 81.1 ms: 1.23x faster                                                 |
| dulwich_log             | 75.9 ms                                                | 61.8 ms: 1.23x faster                                                 |
| xml_etree_generate      | 94.2 ms                                                | 77.2 ms: 1.22x faster                                                 |
| bench_thread_pool       | 947 us                                                 | 780 us: 1.21x faster                                                  |
| json_loads              | 28.8 us                                                | 23.9 us: 1.21x faster                                                 |
| async_generators        | 425 ms                                                 | 355 ms: 1.20x faster                                                  |
| sympy_expand            | 545 ms                                                 | 456 ms: 1.19x faster                                                  |
| sympy_integrate         | 24.3 ms                                                | 20.4 ms: 1.19x faster                                                 |
| regex_v8                | 25.0 ms                                                | 21.1 ms: 1.19x faster                                                 |
| dask                    | 423 ms                                                 | 360 ms: 1.17x faster                                                  |
| sympy_str               | 328 ms                                                 | 282 ms: 1.16x faster                                                  |
| json                    | 5.42 ms                                                | 4.65 ms: 1.16x faster                                                 |
| create_gc_cycles        | 1.67 ms                                                | 1.46 ms: 1.15x faster                                                 |
| comprehensions          | 26.8 us                                                | 23.4 us: 1.14x faster                                                 |
| mdp                     | 2.82 sec                                               | 2.48 sec: 1.14x faster                                                |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                                 |
| sqlite_synth            | 2.93 us                                                | 2.60 us: 1.13x faster                                                 |
| meteor_contest          | 115 ms                                                 | 102 ms: 1.13x faster                                                  |
| pickle_list             | 4.56 us                                                | 4.06 us: 1.12x faster                                                 |
| sympy_sum               | 185 ms                                                 | 165 ms: 1.12x faster                                                  |
| djangocms               | 35.9 us                                                | 32.5 us: 1.11x faster                                                 |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                                  |
| unpickle                | 14.1 us                                                | 12.9 us: 1.09x faster                                                 |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                                  |
| regex_dna               | 222 ms                                                 | 208 ms: 1.07x faster                                                  |
| asyncio_tcp             | 925 ms                                                 | 884 ms: 1.05x faster                                                  |
| pickle                  | 10.3 us                                                | 9.88 us: 1.04x faster                                                 |
| telco                   | 6.54 ms                                                | 6.38 ms: 1.03x faster                                                 |
| gc_traversal            | 3.84 ms                                                | 3.77 ms: 1.02x faster                                                 |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                  |
| generators              | 76.8 ms                                                | 77.4 ms: 1.01x slower                                                 |
| unpickle_list           | 4.82 us                                                | 4.98 us: 1.03x slower                                                 |
| python_startup_no_site  | 5.82 ms                                                | 6.12 ms: 1.05x slower                                                 |
| regex_effbot            | 3.23 ms                                                | 3.47 ms: 1.08x slower                                                 |
| pickle_dict             | 27.3 us                                                | 30.8 us: 1.13x slower                                                 |
| coverage                | 72.8 ms                                                | 101 ms: 1.38x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                          |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x
