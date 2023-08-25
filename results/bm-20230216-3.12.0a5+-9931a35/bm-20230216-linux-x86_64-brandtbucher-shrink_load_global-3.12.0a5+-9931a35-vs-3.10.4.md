
# Results vs. 3.10.4

- fork: brandtbucher
- ref: shrink_load_global
- machine: linux-x86_64
- commit hash: 9931a35
- commit date: 2023-02-16
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230216-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-9931a35 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 246 ms: 1.37x faster                                                       |
| chameleon      | 9.06 ms                                                | 6.52 ms: 1.39x faster                                                      |
| docutils       | 3.17 sec                                               | 2.54 sec: 1.25x faster                                                     |
| html5lib       | 85.9 ms                                                | 60.9 ms: 1.41x faster                                                      |
| tornado_http   | 127 ms                                                 | 95.2 ms: 1.34x faster                                                      |
| Geometric mean | (ref)                                                  | 1.35x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230216-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-9931a35 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 111 ms                                                 | 72.9 ms: 1.52x faster                                                      |
| nbody          | 142 ms                                                 | 94.4 ms: 1.50x faster                                                      |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                  | 1.32x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230216-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-9931a35 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.37x faster                                                       |
| regex_v8       | 25.0 ms                                                | 21.7 ms: 1.15x faster                                                      |
| regex_dna      | 222 ms                                                 | 206 ms: 1.08x faster                                                       |
| regex_effbot   | 3.23 ms                                                | 3.70 ms: 1.15x slower                                                      |
| Geometric mean | (ref)                                                  | 1.10x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230216-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-9931a35 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 283 us: 1.61x faster                                                       |
| unpickle_pure_python | 300 us                                                 | 198 us: 1.52x faster                                                       |
| json_dumps           | 13.5 ms                                                | 9.64 ms: 1.40x faster                                                      |
| xml_etree_process    | 74.9 ms                                                | 56.3 ms: 1.33x faster                                                      |
| json_loads           | 28.8 us                                                | 24.2 us: 1.19x faster                                                      |
| xml_etree_generate   | 94.2 ms                                                | 81.9 ms: 1.15x faster                                                      |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                       |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                                       |
| pickle_list          | 4.56 us                                                | 4.26 us: 1.07x faster                                                      |
| unpickle             | 14.1 us                                                | 13.6 us: 1.04x faster                                                      |
| pickle               | 10.3 us                                                | 10.1 us: 1.02x faster                                                      |
| unpickle_list        | 4.82 us                                                | 5.06 us: 1.05x slower                                                      |
| pickle_dict          | 27.3 us                                                | 31.7 us: 1.16x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230216-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-9931a35 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.96 ms: 1.58x faster                                                      |
| python_startup_no_site | 5.82 ms                                                | 6.49 ms: 1.12x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230216-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-9931a35 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 10.0 ms: 1.47x faster                                                      |
| genshi_text     | 30.3 ms                                                | 21.3 ms: 1.42x faster                                                      |
| django_template | 45.9 ms                                                | 33.1 ms: 1.39x faster                                                      |
| genshi_xml      | 63.3 ms                                                | 48.4 ms: 1.31x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230216-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-9931a35 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 30.6 ms: 2.51x faster                                                      |
| deltablue               | 7.42 ms                                                | 3.20 ms: 2.32x faster                                                      |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.85x faster                                                       |
| asyncio_tcp             | 925 ms                                                 | 504 ms: 1.83x faster                                                       |
| logging_silent          | 175 ns                                                 | 95.8 ns: 1.83x faster                                                      |
| richards                | 74.9 ms                                                | 42.2 ms: 1.77x faster                                                      |
| go                      | 229 ms                                                 | 136 ms: 1.68x faster                                                       |
| pyflate                 | 673 ms                                                 | 401 ms: 1.68x faster                                                       |
| scimark_monte_carlo     | 108 ms                                                 | 66.0 ms: 1.64x faster                                                      |
| raytrace                | 464 ms                                                 | 287 ms: 1.62x faster                                                       |
| crypto_pyaes            | 118 ms                                                 | 73.6 ms: 1.61x faster                                                      |
| pickle_pure_python      | 455 us                                                 | 283 us: 1.61x faster                                                       |
| chaos                   | 106 ms                                                 | 66.7 ms: 1.59x faster                                                      |
| spectral_norm           | 150 ms                                                 | 94.9 ms: 1.58x faster                                                      |
| python_startup          | 14.2 ms                                                | 8.96 ms: 1.58x faster                                                      |
| hexiom                  | 9.53 ms                                                | 6.12 ms: 1.56x faster                                                      |
| unpack_sequence         | 64.7 ns                                                | 41.8 ns: 1.55x faster                                                      |
| unpickle_pure_python    | 300 us                                                 | 198 us: 1.52x faster                                                       |
| float                   | 111 ms                                                 | 72.9 ms: 1.52x faster                                                      |
| nbody                   | 142 ms                                                 | 94.4 ms: 1.50x faster                                                      |
| deepcopy_memo           | 52.3 us                                                | 34.9 us: 1.50x faster                                                      |
| scimark_lu              | 163 ms                                                 | 109 ms: 1.50x faster                                                       |
| mako                    | 14.8 ms                                                | 10.0 ms: 1.47x faster                                                      |
| sqlglot_parse           | 2.06 ms                                                | 1.44 ms: 1.43x faster                                                      |
| genshi_text             | 30.3 ms                                                | 21.3 ms: 1.42x faster                                                      |
| pprint_pformat          | 1.99 sec                                               | 1.40 sec: 1.42x faster                                                     |
| sqlglot_transpile       | 2.45 ms                                                | 1.73 ms: 1.41x faster                                                      |
| html5lib                | 85.9 ms                                                | 60.9 ms: 1.41x faster                                                      |
| coroutines              | 31.8 ms                                                | 22.6 ms: 1.41x faster                                                      |
| json_dumps              | 13.5 ms                                                | 9.64 ms: 1.40x faster                                                      |
| pprint_safe_repr        | 955 ms                                                 | 681 ms: 1.40x faster                                                       |
| logging_format          | 8.91 us                                                | 6.37 us: 1.40x faster                                                      |
| chameleon               | 9.06 ms                                                | 6.52 ms: 1.39x faster                                                      |
| logging_simple          | 8.07 us                                                | 5.82 us: 1.39x faster                                                      |
| django_template         | 45.9 ms                                                | 33.1 ms: 1.39x faster                                                      |
| aiohttp                 | 1.38 ms                                                | 1.00 ms: 1.38x faster                                                      |
| pycparser               | 1.50 sec                                               | 1.09 sec: 1.38x faster                                                     |
| scimark_fft             | 424 ms                                                 | 309 ms: 1.37x faster                                                       |
| 2to3                    | 336 ms                                                 | 246 ms: 1.37x faster                                                       |
| async_tree_none         | 717 ms                                                 | 525 ms: 1.37x faster                                                       |
| regex_compile           | 177 ms                                                 | 129 ms: 1.37x faster                                                       |
| gunicorn                | 1.46 ms                                                | 1.07 ms: 1.36x faster                                                      |
| async_tree_io           | 1.77 sec                                               | 1.31 sec: 1.36x faster                                                     |
| thrift                  | 1.03 ms                                                | 766 us: 1.35x faster                                                       |
| tornado_http            | 127 ms                                                 | 95.2 ms: 1.34x faster                                                      |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.08 ms: 1.34x faster                                                      |
| xml_etree_process       | 74.9 ms                                                | 56.3 ms: 1.33x faster                                                      |
| async_tree_memoization  | 854 ms                                                 | 644 ms: 1.33x faster                                                       |
| deepcopy                | 442 us                                                 | 337 us: 1.31x faster                                                       |
| fannkuch                | 486 ms                                                 | 371 ms: 1.31x faster                                                       |
| genshi_xml              | 63.3 ms                                                | 48.4 ms: 1.31x faster                                                      |
| mypy2                   | 428 ms                                                 | 330 ms: 1.30x faster                                                       |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                                       |
| deepcopy_reduce         | 3.82 us                                                | 2.98 us: 1.29x faster                                                      |
| async_tree_cpu_io_mixed | 951 ms                                                 | 743 ms: 1.28x faster                                                       |
| sqlglot_optimize        | 65.3 ms                                                | 51.1 ms: 1.28x faster                                                      |
| docutils                | 3.17 sec                                               | 2.54 sec: 1.25x faster                                                     |
| nqueens                 | 100 ms                                                 | 80.5 ms: 1.24x faster                                                      |
| sympy_integrate         | 24.3 ms                                                | 19.9 ms: 1.22x faster                                                      |
| sympy_str               | 328 ms                                                 | 271 ms: 1.21x faster                                                       |
| dulwich_log             | 75.9 ms                                                | 62.9 ms: 1.21x faster                                                      |
| sympy_expand            | 545 ms                                                 | 455 ms: 1.20x faster                                                       |
| bench_thread_pool       | 947 us                                                 | 792 us: 1.20x faster                                                       |
| sqlalchemy_declarative  | 165 ms                                                 | 138 ms: 1.19x faster                                                       |
| json_loads              | 28.8 us                                                | 24.2 us: 1.19x faster                                                      |
| json                    | 5.42 ms                                                | 4.60 ms: 1.18x faster                                                      |
| sympy_sum               | 185 ms                                                 | 157 ms: 1.17x faster                                                       |
| sqlalchemy_imperative   | 21.2 ms                                                | 18.1 ms: 1.17x faster                                                      |
| regex_v8                | 25.0 ms                                                | 21.7 ms: 1.15x faster                                                      |
| xml_etree_generate      | 94.2 ms                                                | 81.9 ms: 1.15x faster                                                      |
| create_gc_cycles        | 1.67 ms                                                | 1.47 ms: 1.13x faster                                                      |
| sqlite_synth            | 2.93 us                                                | 2.63 us: 1.11x faster                                                      |
| pathlib                 | 20.0 ms                                                | 18.0 ms: 1.11x faster                                                      |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                       |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.11x faster                                                       |
| djangocms               | 35.9 us                                                | 32.9 us: 1.09x faster                                                      |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                                       |
| regex_dna               | 222 ms                                                 | 206 ms: 1.08x faster                                                       |
| pickle_list             | 4.56 us                                                | 4.26 us: 1.07x faster                                                      |
| mdp                     | 2.82 sec                                               | 2.68 sec: 1.05x faster                                                     |
| gc_traversal            | 3.84 ms                                                | 3.66 ms: 1.05x faster                                                      |
| unpickle                | 14.1 us                                                | 13.6 us: 1.04x faster                                                      |
| async_generators        | 425 ms                                                 | 412 ms: 1.03x faster                                                       |
| telco                   | 6.54 ms                                                | 6.38 ms: 1.03x faster                                                      |
| pickle                  | 10.3 us                                                | 10.1 us: 1.02x faster                                                      |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                       |
| unpickle_list           | 4.82 us                                                | 5.06 us: 1.05x slower                                                      |
| python_startup_no_site  | 5.82 ms                                                | 6.49 ms: 1.12x slower                                                      |
| regex_effbot            | 3.23 ms                                                | 3.70 ms: 1.15x slower                                                      |
| pickle_dict             | 27.3 us                                                | 31.7 us: 1.16x slower                                                      |
| dask                    | 423 ms                                                 | 500 ms: 1.18x slower                                                       |
| coverage                | 72.8 ms                                                | 96.8 ms: 1.33x slower                                                      |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                               |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.25x
