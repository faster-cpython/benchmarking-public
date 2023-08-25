
# Results vs. 3.10.4

- fork: python
- ref: affedee8bf2ec00c404f
- machine: linux-x86_64
- commit hash: affedee
- commit date: 2023-04-06
- overall geometric mean: 1.31x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-linux-x86_64-python-affedee8bf2ec00c404f-3.12.0a7+-affedee |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 251 ms: 1.34x faster                                                   |
| chameleon      | 9.06 ms                                                | 6.27 ms: 1.45x faster                                                  |
| docutils       | 3.17 sec                                               | 2.53 sec: 1.25x faster                                                 |
| html5lib       | 85.9 ms                                                | 61.4 ms: 1.40x faster                                                  |
| tornado_http   | 127 ms                                                 | 90.8 ms: 1.40x faster                                                  |
| Geometric mean | (ref)                                                  | 1.37x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-linux-x86_64-python-affedee8bf2ec00c404f-3.12.0a7+-affedee |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 86.9 ms: 1.63x faster                                                  |
| float          | 111 ms                                                 | 73.5 ms: 1.50x faster                                                  |
| pidigits       | 190 ms                                                 | 188 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.35x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-linux-x86_64-python-affedee8bf2ec00c404f-3.12.0a7+-affedee |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 133 ms: 1.33x faster                                                   |
| regex_v8       | 25.0 ms                                                | 22.5 ms: 1.11x faster                                                  |
| regex_dna      | 222 ms                                                 | 204 ms: 1.09x faster                                                   |
| regex_effbot   | 3.23 ms                                                | 3.48 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-linux-x86_64-python-affedee8bf2ec00c404f-3.12.0a7+-affedee |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 289 us: 1.58x faster                                                   |
| unpickle_pure_python | 300 us                                                 | 203 us: 1.48x faster                                                   |
| json_dumps           | 13.5 ms                                                | 9.47 ms: 1.43x faster                                                  |
| xml_etree_process    | 74.9 ms                                                | 55.2 ms: 1.36x faster                                                  |
| json_loads           | 28.8 us                                                | 24.2 us: 1.19x faster                                                  |
| xml_etree_generate   | 94.2 ms                                                | 80.6 ms: 1.17x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                 | 99.3 ms: 1.12x faster                                                  |
| xml_etree_parse      | 163 ms                                                 | 146 ms: 1.12x faster                                                   |
| pickle_list          | 4.56 us                                                | 4.35 us: 1.05x faster                                                  |
| unpickle             | 14.1 us                                                | 13.7 us: 1.04x faster                                                  |
| pickle               | 10.3 us                                                | 10.7 us: 1.04x slower                                                  |
| unpickle_list        | 4.82 us                                                | 5.11 us: 1.06x slower                                                  |
| pickle_dict          | 27.3 us                                                | 32.6 us: 1.20x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-linux-x86_64-python-affedee8bf2ec00c404f-3.12.0a7+-affedee |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.81 ms: 1.61x faster                                                  |
| python_startup_no_site | 5.82 ms                                                | 6.51 ms: 1.12x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.20x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-linux-x86_64-python-affedee8bf2ec00c404f-3.12.0a7+-affedee |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.89 ms: 1.49x faster                                                  |
| django_template | 45.9 ms                                                | 32.7 ms: 1.40x faster                                                  |
| genshi_text     | 30.3 ms                                                | 21.9 ms: 1.38x faster                                                  |
| genshi_xml      | 63.3 ms                                                | 47.0 ms: 1.35x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-linux-x86_64-python-affedee8bf2ec00c404f-3.12.0a7+-affedee |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 29.1 ms: 2.64x faster                                                  |
| deltablue               | 7.42 ms                                                | 3.24 ms: 2.29x faster                                                  |
| logging_silent          | 175 ns                                                 | 94.9 ns: 1.84x faster                                                  |
| asyncio_tcp             | 925 ms                                                 | 507 ms: 1.82x faster                                                   |
| scimark_sor             | 197 ms                                                 | 110 ms: 1.78x faster                                                   |
| richards                | 74.9 ms                                                | 44.4 ms: 1.69x faster                                                  |
| sqlglot_parse           | 2.06 ms                                                | 1.22 ms: 1.68x faster                                                  |
| go                      | 229 ms                                                 | 138 ms: 1.67x faster                                                   |
| spectral_norm           | 150 ms                                                 | 91.3 ms: 1.64x faster                                                  |
| crypto_pyaes            | 118 ms                                                 | 72.2 ms: 1.64x faster                                                  |
| raytrace                | 464 ms                                                 | 284 ms: 1.63x faster                                                   |
| nbody                   | 142 ms                                                 | 86.9 ms: 1.63x faster                                                  |
| scimark_monte_carlo     | 108 ms                                                 | 66.8 ms: 1.62x faster                                                  |
| sqlglot_transpile       | 2.45 ms                                                | 1.51 ms: 1.62x faster                                                  |
| python_startup          | 14.2 ms                                                | 8.81 ms: 1.61x faster                                                  |
| pyflate                 | 673 ms                                                 | 422 ms: 1.60x faster                                                   |
| hexiom                  | 9.53 ms                                                | 5.99 ms: 1.59x faster                                                  |
| chaos                   | 106 ms                                                 | 66.9 ms: 1.59x faster                                                  |
| pickle_pure_python      | 455 us                                                 | 289 us: 1.58x faster                                                   |
| deepcopy_memo           | 52.3 us                                                | 33.9 us: 1.54x faster                                                  |
| scimark_lu              | 163 ms                                                 | 107 ms: 1.53x faster                                                   |
| float                   | 111 ms                                                 | 73.5 ms: 1.50x faster                                                  |
| mako                    | 14.8 ms                                                | 9.89 ms: 1.49x faster                                                  |
| unpickle_pure_python    | 300 us                                                 | 203 us: 1.48x faster                                                   |
| unpack_sequence         | 64.7 ns                                                | 44.6 ns: 1.45x faster                                                  |
| chameleon               | 9.06 ms                                                | 6.27 ms: 1.45x faster                                                  |
| json_dumps              | 13.5 ms                                                | 9.47 ms: 1.43x faster                                                  |
| pprint_pformat          | 1.99 sec                                               | 1.40 sec: 1.42x faster                                                 |
| logging_format          | 8.91 us                                                | 6.33 us: 1.41x faster                                                  |
| logging_simple          | 8.07 us                                                | 5.74 us: 1.41x faster                                                  |
| django_template         | 45.9 ms                                                | 32.7 ms: 1.40x faster                                                  |
| tornado_http            | 127 ms                                                 | 90.8 ms: 1.40x faster                                                  |
| html5lib                | 85.9 ms                                                | 61.4 ms: 1.40x faster                                                  |
| pprint_safe_repr        | 955 ms                                                 | 685 ms: 1.39x faster                                                   |
| genshi_text             | 30.3 ms                                                | 21.9 ms: 1.38x faster                                                  |
| async_tree_none         | 717 ms                                                 | 522 ms: 1.37x faster                                                   |
| async_tree_io           | 1.77 sec                                               | 1.30 sec: 1.37x faster                                                 |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.36x faster                                                  |
| deepcopy                | 442 us                                                 | 324 us: 1.36x faster                                                   |
| scimark_fft             | 424 ms                                                 | 312 ms: 1.36x faster                                                   |
| xml_etree_process       | 74.9 ms                                                | 55.2 ms: 1.36x faster                                                  |
| async_tree_memoization  | 854 ms                                                 | 633 ms: 1.35x faster                                                   |
| genshi_xml              | 63.3 ms                                                | 47.0 ms: 1.35x faster                                                  |
| coroutines              | 31.8 ms                                                | 23.6 ms: 1.35x faster                                                  |
| 2to3                    | 336 ms                                                 | 251 ms: 1.34x faster                                                   |
| regex_compile           | 177 ms                                                 | 133 ms: 1.33x faster                                                   |
| gunicorn                | 1.46 ms                                                | 1.09 ms: 1.33x faster                                                  |
| deepcopy_reduce         | 3.82 us                                                | 2.94 us: 1.30x faster                                                  |
| fannkuch                | 486 ms                                                 | 374 ms: 1.30x faster                                                   |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                                   |
| pycparser               | 1.50 sec                                               | 1.16 sec: 1.30x faster                                                 |
| async_tree_cpu_io_mixed | 951 ms                                                 | 736 ms: 1.29x faster                                                   |
| thrift                  | 1.03 ms                                                | 800 us: 1.29x faster                                                   |
| sqlglot_optimize        | 65.3 ms                                                | 50.9 ms: 1.28x faster                                                  |
| mypy2                   | 428 ms                                                 | 336 ms: 1.28x faster                                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.34 ms: 1.26x faster                                                  |
| nqueens                 | 100 ms                                                 | 79.6 ms: 1.26x faster                                                  |
| docutils                | 3.17 sec                                               | 2.53 sec: 1.25x faster                                                 |
| comprehensions          | 26.8 us                                                | 21.4 us: 1.25x faster                                                  |
| sqlalchemy_declarative  | 165 ms                                                 | 137 ms: 1.21x faster                                                   |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.6 ms: 1.20x faster                                                  |
| dulwich_log             | 75.9 ms                                                | 63.3 ms: 1.20x faster                                                  |
| bench_thread_pool       | 947 us                                                 | 790 us: 1.20x faster                                                   |
| sympy_integrate         | 24.3 ms                                                | 20.3 ms: 1.20x faster                                                  |
| sympy_expand            | 545 ms                                                 | 456 ms: 1.19x faster                                                   |
| json_loads              | 28.8 us                                                | 24.2 us: 1.19x faster                                                  |
| json                    | 5.42 ms                                                | 4.58 ms: 1.18x faster                                                  |
| xml_etree_generate      | 94.2 ms                                                | 80.6 ms: 1.17x faster                                                  |
| sympy_str               | 328 ms                                                 | 282 ms: 1.16x faster                                                   |
| create_gc_cycles        | 1.67 ms                                                | 1.46 ms: 1.15x faster                                                  |
| meteor_contest          | 115 ms                                                 | 102 ms: 1.13x faster                                                   |
| mdp                     | 2.82 sec                                               | 2.51 sec: 1.12x faster                                                 |
| xml_etree_iterparse     | 111 ms                                                 | 99.3 ms: 1.12x faster                                                  |
| djangocms               | 35.9 us                                                | 32.0 us: 1.12x faster                                                  |
| xml_etree_parse         | 163 ms                                                 | 146 ms: 1.12x faster                                                   |
| sympy_sum               | 185 ms                                                 | 165 ms: 1.12x faster                                                   |
| regex_v8                | 25.0 ms                                                | 22.5 ms: 1.11x faster                                                  |
| sqlite_synth            | 2.93 us                                                | 2.64 us: 1.11x faster                                                  |
| pathlib                 | 20.0 ms                                                | 18.3 ms: 1.09x faster                                                  |
| regex_dna               | 222 ms                                                 | 204 ms: 1.09x faster                                                   |
| gc_traversal            | 3.84 ms                                                | 3.65 ms: 1.05x faster                                                  |
| pickle_list             | 4.56 us                                                | 4.35 us: 1.05x faster                                                  |
| unpickle                | 14.1 us                                                | 13.7 us: 1.04x faster                                                  |
| async_generators        | 425 ms                                                 | 414 ms: 1.03x faster                                                   |
| telco                   | 6.54 ms                                                | 6.44 ms: 1.02x faster                                                  |
| pidigits                | 190 ms                                                 | 188 ms: 1.01x faster                                                   |
| pickle                  | 10.3 us                                                | 10.7 us: 1.04x slower                                                  |
| unpickle_list           | 4.82 us                                                | 5.11 us: 1.06x slower                                                  |
| regex_effbot            | 3.23 ms                                                | 3.48 ms: 1.08x slower                                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.51 ms: 1.12x slower                                                  |
| dask                    | 423 ms                                                 | 502 ms: 1.19x slower                                                   |
| pickle_dict             | 27.3 us                                                | 32.6 us: 1.20x slower                                                  |
| coverage                | 72.8 ms                                                | 98.7 ms: 1.36x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x
