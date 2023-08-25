
# Results vs. 3.10.4

- fork: gaogaotiantian
- ref: pep669_cprofile
- machine: linux-x86_64
- commit hash: 20f4663
- commit date: 2023-04-19
- overall geometric mean: 1.31x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230419-linux-x86_64-gaogaotiantian-pep669_cprofile-3.12.0a7+-20f4663 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 250 ms: 1.35x faster                                                      |
| chameleon      | 9.06 ms                                                | 6.26 ms: 1.45x faster                                                     |
| docutils       | 3.17 sec                                               | 2.53 sec: 1.25x faster                                                    |
| html5lib       | 85.9 ms                                                | 60.6 ms: 1.42x faster                                                     |
| tornado_http   | 127 ms                                                 | 92.7 ms: 1.37x faster                                                     |
| Geometric mean | (ref)                                                  | 1.37x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230419-linux-x86_64-gaogaotiantian-pep669_cprofile-3.12.0a7+-20f4663 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 85.1 ms: 1.66x faster                                                     |
| float          | 111 ms                                                 | 73.1 ms: 1.51x faster                                                     |
| pidigits       | 190 ms                                                 | 188 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.36x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230419-linux-x86_64-gaogaotiantian-pep669_cprofile-3.12.0a7+-20f4663 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 131 ms: 1.35x faster                                                      |
| regex_v8       | 25.0 ms                                                | 21.3 ms: 1.18x faster                                                     |
| regex_dna      | 222 ms                                                 | 207 ms: 1.07x faster                                                      |
| regex_effbot   | 3.23 ms                                                | 3.53 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                  | 1.12x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230419-linux-x86_64-gaogaotiantian-pep669_cprofile-3.12.0a7+-20f4663 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 283 us: 1.61x faster                                                      |
| unpickle_pure_python | 300 us                                                 | 201 us: 1.50x faster                                                      |
| json_dumps           | 13.5 ms                                                | 9.37 ms: 1.44x faster                                                     |
| xml_etree_process    | 74.9 ms                                                | 55.8 ms: 1.34x faster                                                     |
| json_loads           | 28.8 us                                                | 24.1 us: 1.19x faster                                                     |
| xml_etree_generate   | 94.2 ms                                                | 80.7 ms: 1.17x faster                                                     |
| xml_etree_iterparse  | 111 ms                                                 | 98.8 ms: 1.13x faster                                                     |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                      |
| pickle_list          | 4.56 us                                                | 4.24 us: 1.08x faster                                                     |
| unpickle             | 14.1 us                                                | 13.9 us: 1.02x faster                                                     |
| unpickle_list        | 4.82 us                                                | 4.97 us: 1.03x slower                                                     |
| pickle               | 10.3 us                                                | 10.9 us: 1.06x slower                                                     |
| pickle_dict          | 27.3 us                                                | 32.6 us: 1.19x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230419-linux-x86_64-gaogaotiantian-pep669_cprofile-3.12.0a7+-20f4663 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.87 ms: 1.60x faster                                                     |
| python_startup_no_site | 5.82 ms                                                | 6.57 ms: 1.13x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230419-linux-x86_64-gaogaotiantian-pep669_cprofile-3.12.0a7+-20f4663 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.94 ms: 1.48x faster                                                     |
| genshi_text     | 30.3 ms                                                | 21.3 ms: 1.43x faster                                                     |
| django_template | 45.9 ms                                                | 32.6 ms: 1.41x faster                                                     |
| genshi_xml      | 63.3 ms                                                | 46.2 ms: 1.37x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                              |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230419-linux-x86_64-gaogaotiantian-pep669_cprofile-3.12.0a7+-20f4663 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 28.3 ms: 2.71x faster                                                     |
| deltablue               | 7.42 ms                                                | 3.19 ms: 2.33x faster                                                     |
| logging_silent          | 175 ns                                                 | 94.2 ns: 1.86x faster                                                     |
| asyncio_tcp             | 925 ms                                                 | 500 ms: 1.85x faster                                                      |
| richards                | 74.9 ms                                                | 41.3 ms: 1.81x faster                                                     |
| scimark_sor             | 197 ms                                                 | 109 ms: 1.81x faster                                                      |
| sqlglot_parse           | 2.06 ms                                                | 1.20 ms: 1.71x faster                                                     |
| go                      | 229 ms                                                 | 135 ms: 1.70x faster                                                      |
| raytrace                | 464 ms                                                 | 276 ms: 1.68x faster                                                      |
| nbody                   | 142 ms                                                 | 85.1 ms: 1.66x faster                                                     |
| spectral_norm           | 150 ms                                                 | 90.9 ms: 1.65x faster                                                     |
| sqlglot_transpile       | 2.45 ms                                                | 1.49 ms: 1.64x faster                                                     |
| scimark_monte_carlo     | 108 ms                                                 | 66.0 ms: 1.64x faster                                                     |
| chaos                   | 106 ms                                                 | 65.0 ms: 1.64x faster                                                     |
| pyflate                 | 673 ms                                                 | 413 ms: 1.63x faster                                                      |
| pickle_pure_python      | 455 us                                                 | 283 us: 1.61x faster                                                      |
| hexiom                  | 9.53 ms                                                | 5.96 ms: 1.60x faster                                                     |
| python_startup          | 14.2 ms                                                | 8.87 ms: 1.60x faster                                                     |
| crypto_pyaes            | 118 ms                                                 | 74.5 ms: 1.59x faster                                                     |
| scimark_lu              | 163 ms                                                 | 106 ms: 1.54x faster                                                      |
| deepcopy_memo           | 52.3 us                                                | 34.2 us: 1.53x faster                                                     |
| float                   | 111 ms                                                 | 73.1 ms: 1.51x faster                                                     |
| unpack_sequence         | 64.7 ns                                                | 42.8 ns: 1.51x faster                                                     |
| unpickle_pure_python    | 300 us                                                 | 201 us: 1.50x faster                                                      |
| mako                    | 14.8 ms                                                | 9.94 ms: 1.48x faster                                                     |
| chameleon               | 9.06 ms                                                | 6.26 ms: 1.45x faster                                                     |
| json_dumps              | 13.5 ms                                                | 9.37 ms: 1.44x faster                                                     |
| coroutines              | 31.8 ms                                                | 22.1 ms: 1.44x faster                                                     |
| genshi_text             | 30.3 ms                                                | 21.3 ms: 1.43x faster                                                     |
| html5lib                | 85.9 ms                                                | 60.6 ms: 1.42x faster                                                     |
| scimark_fft             | 424 ms                                                 | 300 ms: 1.41x faster                                                      |
| pprint_pformat          | 1.99 sec                                               | 1.41 sec: 1.41x faster                                                    |
| django_template         | 45.9 ms                                                | 32.6 ms: 1.41x faster                                                     |
| logging_simple          | 8.07 us                                                | 5.74 us: 1.41x faster                                                     |
| async_tree_none         | 717 ms                                                 | 514 ms: 1.39x faster                                                      |
| pprint_safe_repr        | 955 ms                                                 | 685 ms: 1.39x faster                                                      |
| logging_format          | 8.91 us                                                | 6.41 us: 1.39x faster                                                     |
| async_tree_memoization  | 854 ms                                                 | 616 ms: 1.39x faster                                                      |
| aiohttp                 | 1.38 ms                                                | 998 us: 1.39x faster                                                      |
| async_tree_io           | 1.77 sec                                               | 1.28 sec: 1.38x faster                                                    |
| tornado_http            | 127 ms                                                 | 92.7 ms: 1.37x faster                                                     |
| genshi_xml              | 63.3 ms                                                | 46.2 ms: 1.37x faster                                                     |
| pycparser               | 1.50 sec                                               | 1.10 sec: 1.37x faster                                                    |
| gunicorn                | 1.46 ms                                                | 1.07 ms: 1.36x faster                                                     |
| regex_compile           | 177 ms                                                 | 131 ms: 1.35x faster                                                      |
| 2to3                    | 336 ms                                                 | 250 ms: 1.35x faster                                                      |
| xml_etree_process       | 74.9 ms                                                | 55.8 ms: 1.34x faster                                                     |
| deepcopy                | 442 us                                                 | 332 us: 1.33x faster                                                      |
| async_tree_cpu_io_mixed | 951 ms                                                 | 718 ms: 1.32x faster                                                      |
| sqlglot_normalize       | 135 ms                                                 | 102 ms: 1.32x faster                                                      |
| thrift                  | 1.03 ms                                                | 791 us: 1.31x faster                                                      |
| mypy2                   | 428 ms                                                 | 329 ms: 1.30x faster                                                      |
| deepcopy_reduce         | 3.82 us                                                | 2.97 us: 1.29x faster                                                     |
| sqlglot_optimize        | 65.3 ms                                                | 50.8 ms: 1.29x faster                                                     |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.25 ms: 1.28x faster                                                     |
| fannkuch                | 486 ms                                                 | 383 ms: 1.27x faster                                                      |
| nqueens                 | 100 ms                                                 | 79.5 ms: 1.26x faster                                                     |
| docutils                | 3.17 sec                                               | 2.53 sec: 1.25x faster                                                    |
| comprehensions          | 26.8 us                                                | 21.6 us: 1.24x faster                                                     |
| sqlalchemy_declarative  | 165 ms                                                 | 135 ms: 1.23x faster                                                      |
| dulwich_log             | 75.9 ms                                                | 62.0 ms: 1.23x faster                                                     |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.4 ms: 1.21x faster                                                     |
| bench_thread_pool       | 947 us                                                 | 781 us: 1.21x faster                                                      |
| pylint                  | 525 ms                                                 | 435 ms: 1.21x faster                                                      |
| sympy_integrate         | 24.3 ms                                                | 20.3 ms: 1.20x faster                                                     |
| sympy_expand            | 545 ms                                                 | 455 ms: 1.20x faster                                                      |
| json_loads              | 28.8 us                                                | 24.1 us: 1.19x faster                                                     |
| pathlib                 | 20.0 ms                                                | 17.0 ms: 1.18x faster                                                     |
| regex_v8                | 25.0 ms                                                | 21.3 ms: 1.18x faster                                                     |
| sympy_str               | 328 ms                                                 | 280 ms: 1.17x faster                                                      |
| xml_etree_generate      | 94.2 ms                                                | 80.7 ms: 1.17x faster                                                     |
| json                    | 5.42 ms                                                | 4.65 ms: 1.16x faster                                                     |
| create_gc_cycles        | 1.67 ms                                                | 1.47 ms: 1.14x faster                                                     |
| sympy_sum               | 185 ms                                                 | 162 ms: 1.14x faster                                                      |
| djangocms               | 35.9 us                                                | 31.7 us: 1.13x faster                                                     |
| sqlite_synth            | 2.93 us                                                | 2.60 us: 1.13x faster                                                     |
| xml_etree_iterparse     | 111 ms                                                 | 98.8 ms: 1.13x faster                                                     |
| meteor_contest          | 115 ms                                                 | 103 ms: 1.12x faster                                                      |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                      |
| mdp                     | 2.82 sec                                               | 2.60 sec: 1.09x faster                                                    |
| pickle_list             | 4.56 us                                                | 4.24 us: 1.08x faster                                                     |
| regex_dna               | 222 ms                                                 | 207 ms: 1.07x faster                                                      |
| unpickle                | 14.1 us                                                | 13.9 us: 1.02x faster                                                     |
| telco                   | 6.54 ms                                                | 6.44 ms: 1.02x faster                                                     |
| pidigits                | 190 ms                                                 | 188 ms: 1.01x faster                                                      |
| bench_mp_pool           | 24.0 ms                                                | 24.0 ms: 1.00x slower                                                     |
| async_generators        | 425 ms                                                 | 431 ms: 1.01x slower                                                      |
| unpickle_list           | 4.82 us                                                | 4.97 us: 1.03x slower                                                     |
| gc_traversal            | 3.84 ms                                                | 4.06 ms: 1.06x slower                                                     |
| pickle                  | 10.3 us                                                | 10.9 us: 1.06x slower                                                     |
| regex_effbot            | 3.23 ms                                                | 3.53 ms: 1.09x slower                                                     |
| python_startup_no_site  | 5.82 ms                                                | 6.57 ms: 1.13x slower                                                     |
| dask                    | 423 ms                                                 | 487 ms: 1.15x slower                                                      |
| pickle_dict             | 27.3 us                                                | 32.6 us: 1.19x slower                                                     |
| coverage                | 72.8 ms                                                | 96.8 ms: 1.33x slower                                                     |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                              |
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x
