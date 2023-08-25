
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: bb396ee
- commit date: 2023-03-11
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230311-linux-x86_64-python-main-3.12.0a6+-bb396ee |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 250 ms: 1.34x faster                                   |
| chameleon      | 9.06 ms                                                | 6.37 ms: 1.42x faster                                  |
| docutils       | 3.17 sec                                               | 2.55 sec: 1.24x faster                                 |
| html5lib       | 85.9 ms                                                | 61.6 ms: 1.39x faster                                  |
| tornado_http   | 127 ms                                                 | 91.2 ms: 1.40x faster                                  |
| Geometric mean | (ref)                                                  | 1.36x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230311-linux-x86_64-python-main-3.12.0a6+-bb396ee |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 142 ms                                                 | 92.1 ms: 1.54x faster                                  |
| float          | 111 ms                                                 | 74.1 ms: 1.49x faster                                  |
| pidigits       | 190 ms                                                 | 192 ms: 1.01x slower                                   |
| Geometric mean | (ref)                                                  | 1.31x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230311-linux-x86_64-python-main-3.12.0a6+-bb396ee |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 134 ms: 1.32x faster                                   |
| regex_v8       | 25.0 ms                                                | 21.7 ms: 1.15x faster                                  |
| regex_dna      | 222 ms                                                 | 205 ms: 1.08x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.66 ms: 1.13x slower                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230311-linux-x86_64-python-main-3.12.0a6+-bb396ee |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 287 us: 1.59x faster                                   |
| unpickle_pure_python | 300 us                                                 | 201 us: 1.49x faster                                   |
| json_dumps           | 13.5 ms                                                | 9.48 ms: 1.43x faster                                  |
| xml_etree_process    | 74.9 ms                                                | 55.8 ms: 1.34x faster                                  |
| json_loads           | 28.8 us                                                | 24.0 us: 1.20x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 80.6 ms: 1.17x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                   |
| xml_etree_iterparse  | 111 ms                                                 | 101 ms: 1.10x faster                                   |
| pickle_list          | 4.56 us                                                | 4.24 us: 1.07x faster                                  |
| unpickle             | 14.1 us                                                | 13.5 us: 1.05x faster                                  |
| pickle               | 10.3 us                                                | 10.4 us: 1.01x slower                                  |
| unpickle_list        | 4.82 us                                                | 4.98 us: 1.03x slower                                  |
| pickle_dict          | 27.3 us                                                | 31.3 us: 1.15x slower                                  |
| Geometric mean       | (ref)                                                  | 1.16x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230311-linux-x86_64-python-main-3.12.0a6+-bb396ee |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.96 ms: 1.58x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.50 ms: 1.12x slower                                  |
| Geometric mean         | (ref)                                                  | 1.19x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230311-linux-x86_64-python-main-3.12.0a6+-bb396ee |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.8 ms                                                | 10.1 ms: 1.46x faster                                  |
| django_template | 45.9 ms                                                | 32.9 ms: 1.40x faster                                  |
| genshi_text     | 30.3 ms                                                | 21.8 ms: 1.39x faster                                  |
| genshi_xml      | 63.3 ms                                                | 48.2 ms: 1.31x faster                                  |
| Geometric mean  | (ref)                                                  | 1.39x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230311-linux-x86_64-python-main-3.12.0a6+-bb396ee |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| generators              | 76.8 ms                                                | 30.3 ms: 2.53x faster                                  |
| deltablue               | 7.42 ms                                                | 3.22 ms: 2.31x faster                                  |
| asyncio_tcp             | 925 ms                                                 | 502 ms: 1.84x faster                                   |
| logging_silent          | 175 ns                                                 | 95.2 ns: 1.84x faster                                  |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.84x faster                                   |
| richards                | 74.9 ms                                                | 42.9 ms: 1.75x faster                                  |
| go                      | 229 ms                                                 | 135 ms: 1.70x faster                                   |
| pyflate                 | 673 ms                                                 | 403 ms: 1.67x faster                                   |
| raytrace                | 464 ms                                                 | 284 ms: 1.63x faster                                   |
| scimark_monte_carlo     | 108 ms                                                 | 66.5 ms: 1.63x faster                                  |
| spectral_norm           | 150 ms                                                 | 93.3 ms: 1.61x faster                                  |
| crypto_pyaes            | 118 ms                                                 | 73.9 ms: 1.60x faster                                  |
| pickle_pure_python      | 455 us                                                 | 287 us: 1.59x faster                                   |
| python_startup          | 14.2 ms                                                | 8.96 ms: 1.58x faster                                  |
| unpack_sequence         | 64.7 ns                                                | 41.3 ns: 1.57x faster                                  |
| chaos                   | 106 ms                                                 | 67.8 ms: 1.57x faster                                  |
| hexiom                  | 9.53 ms                                                | 6.17 ms: 1.54x faster                                  |
| nbody                   | 142 ms                                                 | 92.1 ms: 1.54x faster                                  |
| deepcopy_memo           | 52.3 us                                                | 34.8 us: 1.51x faster                                  |
| float                   | 111 ms                                                 | 74.1 ms: 1.49x faster                                  |
| unpickle_pure_python    | 300 us                                                 | 201 us: 1.49x faster                                   |
| mako                    | 14.8 ms                                                | 10.1 ms: 1.46x faster                                  |
| sqlglot_parse           | 2.06 ms                                                | 1.42 ms: 1.45x faster                                  |
| scimark_lu              | 163 ms                                                 | 114 ms: 1.43x faster                                   |
| json_dumps              | 13.5 ms                                                | 9.48 ms: 1.43x faster                                  |
| pprint_pformat          | 1.99 sec                                               | 1.39 sec: 1.43x faster                                 |
| sqlglot_transpile       | 2.45 ms                                                | 1.72 ms: 1.42x faster                                  |
| chameleon               | 9.06 ms                                                | 6.37 ms: 1.42x faster                                  |
| pprint_safe_repr        | 955 ms                                                 | 680 ms: 1.40x faster                                   |
| coroutines              | 31.8 ms                                                | 22.7 ms: 1.40x faster                                  |
| logging_format          | 8.91 us                                                | 6.36 us: 1.40x faster                                  |
| logging_simple          | 8.07 us                                                | 5.77 us: 1.40x faster                                  |
| tornado_http            | 127 ms                                                 | 91.2 ms: 1.40x faster                                  |
| django_template         | 45.9 ms                                                | 32.9 ms: 1.40x faster                                  |
| html5lib                | 85.9 ms                                                | 61.6 ms: 1.39x faster                                  |
| genshi_text             | 30.3 ms                                                | 21.8 ms: 1.39x faster                                  |
| async_tree_io           | 1.77 sec                                               | 1.28 sec: 1.39x faster                                 |
| async_tree_none         | 717 ms                                                 | 520 ms: 1.38x faster                                   |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                  |
| fannkuch                | 486 ms                                                 | 355 ms: 1.37x faster                                   |
| scimark_fft             | 424 ms                                                 | 313 ms: 1.35x faster                                   |
| gunicorn                | 1.46 ms                                                | 1.09 ms: 1.34x faster                                  |
| xml_etree_process       | 74.9 ms                                                | 55.8 ms: 1.34x faster                                  |
| 2to3                    | 336 ms                                                 | 250 ms: 1.34x faster                                   |
| pycparser               | 1.50 sec                                               | 1.13 sec: 1.33x faster                                 |
| thrift                  | 1.03 ms                                                | 782 us: 1.32x faster                                   |
| regex_compile           | 177 ms                                                 | 134 ms: 1.32x faster                                   |
| async_tree_memoization  | 854 ms                                                 | 649 ms: 1.32x faster                                   |
| deepcopy                | 442 us                                                 | 336 us: 1.31x faster                                   |
| genshi_xml              | 63.3 ms                                                | 48.2 ms: 1.31x faster                                  |
| async_tree_cpu_io_mixed | 951 ms                                                 | 738 ms: 1.29x faster                                   |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                   |
| mypy2                   | 428 ms                                                 | 333 ms: 1.28x faster                                   |
| sqlglot_optimize        | 65.3 ms                                                | 51.0 ms: 1.28x faster                                  |
| deepcopy_reduce         | 3.82 us                                                | 3.00 us: 1.28x faster                                  |
| docutils                | 3.17 sec                                               | 2.55 sec: 1.24x faster                                 |
| bench_thread_pool       | 947 us                                                 | 789 us: 1.20x faster                                   |
| nqueens                 | 100 ms                                                 | 83.3 ms: 1.20x faster                                  |
| json_loads              | 28.8 us                                                | 24.0 us: 1.20x faster                                  |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.7 ms: 1.20x faster                                  |
| dulwich_log             | 75.9 ms                                                | 63.7 ms: 1.19x faster                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.59 ms: 1.19x faster                                  |
| json                    | 5.42 ms                                                | 4.57 ms: 1.19x faster                                  |
| sympy_integrate         | 24.3 ms                                                | 20.5 ms: 1.19x faster                                  |
| sympy_expand            | 545 ms                                                 | 461 ms: 1.18x faster                                   |
| sqlalchemy_declarative  | 165 ms                                                 | 140 ms: 1.18x faster                                   |
| xml_etree_generate      | 94.2 ms                                                | 80.6 ms: 1.17x faster                                  |
| sympy_str               | 328 ms                                                 | 284 ms: 1.16x faster                                   |
| regex_v8                | 25.0 ms                                                | 21.7 ms: 1.15x faster                                  |
| create_gc_cycles        | 1.67 ms                                                | 1.45 ms: 1.15x faster                                  |
| comprehensions          | 26.8 us                                                | 23.7 us: 1.13x faster                                  |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                  |
| sqlite_synth            | 2.93 us                                                | 2.63 us: 1.11x faster                                  |
| sympy_sum               | 185 ms                                                 | 167 ms: 1.11x faster                                   |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                   |
| mdp                     | 2.82 sec                                               | 2.55 sec: 1.11x faster                                 |
| xml_etree_iterparse     | 111 ms                                                 | 101 ms: 1.10x faster                                   |
| djangocms               | 35.9 us                                                | 32.8 us: 1.10x faster                                  |
| meteor_contest          | 115 ms                                                 | 106 ms: 1.08x faster                                   |
| regex_dna               | 222 ms                                                 | 205 ms: 1.08x faster                                   |
| pickle_list             | 4.56 us                                                | 4.24 us: 1.07x faster                                  |
| gc_traversal            | 3.84 ms                                                | 3.66 ms: 1.05x faster                                  |
| unpickle                | 14.1 us                                                | 13.5 us: 1.05x faster                                  |
| async_generators        | 425 ms                                                 | 415 ms: 1.02x faster                                   |
| telco                   | 6.54 ms                                                | 6.49 ms: 1.01x faster                                  |
| pidigits                | 190 ms                                                 | 192 ms: 1.01x slower                                   |
| pickle                  | 10.3 us                                                | 10.4 us: 1.01x slower                                  |
| unpickle_list           | 4.82 us                                                | 4.98 us: 1.03x slower                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.50 ms: 1.12x slower                                  |
| regex_effbot            | 3.23 ms                                                | 3.66 ms: 1.13x slower                                  |
| pickle_dict             | 27.3 us                                                | 31.3 us: 1.15x slower                                  |
| dask                    | 423 ms                                                 | 499 ms: 1.18x slower                                   |
| coverage                | 72.8 ms                                                | 97.3 ms: 1.34x slower                                  |
| Geometric mean          | (ref)                                                  | 1.30x faster                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.24x
