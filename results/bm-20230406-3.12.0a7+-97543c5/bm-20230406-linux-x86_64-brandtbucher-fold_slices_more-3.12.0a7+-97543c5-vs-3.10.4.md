
# Results vs. 3.10.4

- fork: brandtbucher
- ref: fold_slices_more
- machine: linux-x86_64
- commit hash: 97543c5
- commit date: 2023-04-06
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7+-97543c5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 250 ms: 1.34x faster                                                     |
| chameleon      | 9.06 ms                                                | 6.41 ms: 1.41x faster                                                    |
| docutils       | 3.17 sec                                               | 2.53 sec: 1.25x faster                                                   |
| html5lib       | 85.9 ms                                                | 61.0 ms: 1.41x faster                                                    |
| tornado_http   | 127 ms                                                 | 90.6 ms: 1.41x faster                                                    |
| Geometric mean | (ref)                                                  | 1.36x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7+-97543c5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 86.9 ms: 1.63x faster                                                    |
| float          | 111 ms                                                 | 74.7 ms: 1.48x faster                                                    |
| pidigits       | 190 ms                                                 | 188 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                  | 1.34x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7+-97543c5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 132 ms: 1.34x faster                                                     |
| regex_v8       | 25.0 ms                                                | 21.6 ms: 1.16x faster                                                    |
| regex_dna      | 222 ms                                                 | 204 ms: 1.08x faster                                                     |
| regex_effbot   | 3.23 ms                                                | 3.41 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                  | 1.12x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7+-97543c5 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 287 us: 1.59x faster                                                     |
| unpickle_pure_python | 300 us                                                 | 202 us: 1.49x faster                                                     |
| json_dumps           | 13.5 ms                                                | 9.37 ms: 1.44x faster                                                    |
| xml_etree_process    | 74.9 ms                                                | 55.3 ms: 1.35x faster                                                    |
| json_loads           | 28.8 us                                                | 24.2 us: 1.19x faster                                                    |
| xml_etree_generate   | 94.2 ms                                                | 80.6 ms: 1.17x faster                                                    |
| xml_etree_iterparse  | 111 ms                                                 | 99.4 ms: 1.12x faster                                                    |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                     |
| pickle_list          | 4.56 us                                                | 4.43 us: 1.03x faster                                                    |
| unpickle             | 14.1 us                                                | 13.8 us: 1.02x faster                                                    |
| pickle               | 10.3 us                                                | 10.6 us: 1.03x slower                                                    |
| unpickle_list        | 4.82 us                                                | 5.05 us: 1.05x slower                                                    |
| pickle_dict          | 27.3 us                                                | 31.9 us: 1.17x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7+-97543c5 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.82 ms: 1.60x faster                                                    |
| python_startup_no_site | 5.82 ms                                                | 6.52 ms: 1.12x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.20x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7+-97543c5 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 10.1 ms: 1.47x faster                                                    |
| genshi_text     | 30.3 ms                                                | 21.1 ms: 1.44x faster                                                    |
| django_template | 45.9 ms                                                | 32.4 ms: 1.42x faster                                                    |
| genshi_xml      | 63.3 ms                                                | 46.9 ms: 1.35x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-linux-x86_64-brandtbucher-fold_slices_more-3.12.0a7+-97543c5 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 29.9 ms: 2.57x faster                                                    |
| deltablue               | 7.42 ms                                                | 3.24 ms: 2.29x faster                                                    |
| asyncio_tcp             | 925 ms                                                 | 500 ms: 1.85x faster                                                     |
| logging_silent          | 175 ns                                                 | 95.0 ns: 1.84x faster                                                    |
| richards                | 74.9 ms                                                | 41.4 ms: 1.81x faster                                                    |
| scimark_sor             | 197 ms                                                 | 113 ms: 1.75x faster                                                     |
| sqlglot_parse           | 2.06 ms                                                | 1.22 ms: 1.68x faster                                                    |
| go                      | 229 ms                                                 | 138 ms: 1.66x faster                                                     |
| raytrace                | 464 ms                                                 | 283 ms: 1.64x faster                                                     |
| sqlglot_transpile       | 2.45 ms                                                | 1.50 ms: 1.63x faster                                                    |
| nbody                   | 142 ms                                                 | 86.9 ms: 1.63x faster                                                    |
| chaos                   | 106 ms                                                 | 65.4 ms: 1.62x faster                                                    |
| hexiom                  | 9.53 ms                                                | 5.92 ms: 1.61x faster                                                    |
| python_startup          | 14.2 ms                                                | 8.82 ms: 1.60x faster                                                    |
| crypto_pyaes            | 118 ms                                                 | 73.9 ms: 1.60x faster                                                    |
| scimark_monte_carlo     | 108 ms                                                 | 68.2 ms: 1.59x faster                                                    |
| pickle_pure_python      | 455 us                                                 | 287 us: 1.59x faster                                                     |
| pyflate                 | 673 ms                                                 | 425 ms: 1.58x faster                                                     |
| spectral_norm           | 150 ms                                                 | 95.1 ms: 1.58x faster                                                    |
| deepcopy_memo           | 52.3 us                                                | 34.3 us: 1.53x faster                                                    |
| scimark_lu              | 163 ms                                                 | 109 ms: 1.50x faster                                                     |
| unpack_sequence         | 64.7 ns                                                | 43.5 ns: 1.49x faster                                                    |
| unpickle_pure_python    | 300 us                                                 | 202 us: 1.49x faster                                                     |
| float                   | 111 ms                                                 | 74.7 ms: 1.48x faster                                                    |
| mako                    | 14.8 ms                                                | 10.1 ms: 1.47x faster                                                    |
| json_dumps              | 13.5 ms                                                | 9.37 ms: 1.44x faster                                                    |
| genshi_text             | 30.3 ms                                                | 21.1 ms: 1.44x faster                                                    |
| django_template         | 45.9 ms                                                | 32.4 ms: 1.42x faster                                                    |
| logging_format          | 8.91 us                                                | 6.30 us: 1.41x faster                                                    |
| logging_simple          | 8.07 us                                                | 5.71 us: 1.41x faster                                                    |
| chameleon               | 9.06 ms                                                | 6.41 ms: 1.41x faster                                                    |
| html5lib                | 85.9 ms                                                | 61.0 ms: 1.41x faster                                                    |
| tornado_http            | 127 ms                                                 | 90.6 ms: 1.41x faster                                                    |
| pprint_pformat          | 1.99 sec                                               | 1.42 sec: 1.40x faster                                                   |
| async_tree_io           | 1.77 sec                                               | 1.29 sec: 1.38x faster                                                   |
| pprint_safe_repr        | 955 ms                                                 | 694 ms: 1.38x faster                                                     |
| async_tree_none         | 717 ms                                                 | 522 ms: 1.37x faster                                                     |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                                    |
| async_tree_memoization  | 854 ms                                                 | 623 ms: 1.37x faster                                                     |
| deepcopy                | 442 us                                                 | 326 us: 1.35x faster                                                     |
| xml_etree_process       | 74.9 ms                                                | 55.3 ms: 1.35x faster                                                    |
| genshi_xml              | 63.3 ms                                                | 46.9 ms: 1.35x faster                                                    |
| scimark_fft             | 424 ms                                                 | 314 ms: 1.35x faster                                                     |
| 2to3                    | 336 ms                                                 | 250 ms: 1.34x faster                                                     |
| gunicorn                | 1.46 ms                                                | 1.09 ms: 1.34x faster                                                    |
| regex_compile           | 177 ms                                                 | 132 ms: 1.34x faster                                                     |
| coroutines              | 31.8 ms                                                | 23.7 ms: 1.34x faster                                                    |
| thrift                  | 1.03 ms                                                | 782 us: 1.32x faster                                                     |
| deepcopy_reduce         | 3.82 us                                                | 2.92 us: 1.31x faster                                                    |
| pycparser               | 1.50 sec                                               | 1.15 sec: 1.31x faster                                                   |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                                     |
| async_tree_cpu_io_mixed | 951 ms                                                 | 733 ms: 1.30x faster                                                     |
| sqlglot_optimize        | 65.3 ms                                                | 50.4 ms: 1.30x faster                                                    |
| mypy2                   | 428 ms                                                 | 334 ms: 1.28x faster                                                     |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.27 ms: 1.28x faster                                                    |
| fannkuch                | 486 ms                                                 | 383 ms: 1.27x faster                                                     |
| docutils                | 3.17 sec                                               | 2.53 sec: 1.25x faster                                                   |
| comprehensions          | 26.8 us                                                | 21.9 us: 1.22x faster                                                    |
| sqlalchemy_declarative  | 165 ms                                                 | 136 ms: 1.22x faster                                                     |
| nqueens                 | 100 ms                                                 | 82.6 ms: 1.21x faster                                                    |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.6 ms: 1.20x faster                                                    |
| dulwich_log             | 75.9 ms                                                | 63.1 ms: 1.20x faster                                                    |
| bench_thread_pool       | 947 us                                                 | 791 us: 1.20x faster                                                     |
| json_loads              | 28.8 us                                                | 24.2 us: 1.19x faster                                                    |
| sympy_integrate         | 24.3 ms                                                | 20.4 ms: 1.19x faster                                                    |
| sympy_expand            | 545 ms                                                 | 460 ms: 1.18x faster                                                     |
| json                    | 5.42 ms                                                | 4.63 ms: 1.17x faster                                                    |
| xml_etree_generate      | 94.2 ms                                                | 80.6 ms: 1.17x faster                                                    |
| sympy_str               | 328 ms                                                 | 284 ms: 1.16x faster                                                     |
| regex_v8                | 25.0 ms                                                | 21.6 ms: 1.16x faster                                                    |
| xml_etree_iterparse     | 111 ms                                                 | 99.4 ms: 1.12x faster                                                    |
| djangocms               | 35.9 us                                                | 32.0 us: 1.12x faster                                                    |
| meteor_contest          | 115 ms                                                 | 103 ms: 1.12x faster                                                     |
| sympy_sum               | 185 ms                                                 | 165 ms: 1.12x faster                                                     |
| mdp                     | 2.82 sec                                               | 2.53 sec: 1.12x faster                                                   |
| sqlite_synth            | 2.93 us                                                | 2.64 us: 1.11x faster                                                    |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                     |
| pathlib                 | 20.0 ms                                                | 18.1 ms: 1.11x faster                                                    |
| create_gc_cycles        | 1.67 ms                                                | 1.52 ms: 1.10x faster                                                    |
| regex_dna               | 222 ms                                                 | 204 ms: 1.08x faster                                                     |
| async_generators        | 425 ms                                                 | 413 ms: 1.03x faster                                                     |
| pickle_list             | 4.56 us                                                | 4.43 us: 1.03x faster                                                    |
| unpickle                | 14.1 us                                                | 13.8 us: 1.02x faster                                                    |
| telco                   | 6.54 ms                                                | 6.47 ms: 1.01x faster                                                    |
| pidigits                | 190 ms                                                 | 188 ms: 1.01x faster                                                     |
| pickle                  | 10.3 us                                                | 10.6 us: 1.03x slower                                                    |
| gc_traversal            | 3.84 ms                                                | 3.97 ms: 1.03x slower                                                    |
| unpickle_list           | 4.82 us                                                | 5.05 us: 1.05x slower                                                    |
| regex_effbot            | 3.23 ms                                                | 3.41 ms: 1.05x slower                                                    |
| python_startup_no_site  | 5.82 ms                                                | 6.52 ms: 1.12x slower                                                    |
| pickle_dict             | 27.3 us                                                | 31.9 us: 1.17x slower                                                    |
| dask                    | 423 ms                                                 | 503 ms: 1.19x slower                                                     |
| coverage                | 72.8 ms                                                | 96.3 ms: 1.32x slower                                                    |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                             |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x
