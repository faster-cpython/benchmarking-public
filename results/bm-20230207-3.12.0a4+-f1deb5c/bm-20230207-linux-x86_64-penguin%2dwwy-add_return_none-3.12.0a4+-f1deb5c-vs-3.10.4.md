
# Results vs. 3.10.4

- fork: penguin-wwy
- ref: add_return_none
- machine: linux-x86_64
- commit hash: f1deb5c
- commit date: 2023-02-07
- overall geometric mean: 1.31x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 251 ms: 1.34x faster                                                     |
| chameleon      | 9.06 ms                                                | 6.36 ms: 1.42x faster                                                    |
| docutils       | 3.17 sec                                               | 2.49 sec: 1.28x faster                                                   |
| html5lib       | 85.9 ms                                                | 59.6 ms: 1.44x faster                                                    |
| tornado_http   | 127 ms                                                 | 93.8 ms: 1.36x faster                                                    |
| Geometric mean | (ref)                                                  | 1.37x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 111 ms                                                 | 72.1 ms: 1.53x faster                                                    |
| nbody          | 142 ms                                                 | 95.5 ms: 1.48x faster                                                    |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                  | 1.30x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 127 ms: 1.39x faster                                                     |
| regex_v8       | 25.0 ms                                                | 21.2 ms: 1.18x faster                                                    |
| regex_dna      | 222 ms                                                 | 200 ms: 1.11x faster                                                     |
| regex_effbot   | 3.23 ms                                                | 3.50 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                  | 1.14x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 284 us: 1.60x faster                                                     |
| unpickle_pure_python | 300 us                                                 | 198 us: 1.52x faster                                                     |
| json_dumps           | 13.5 ms                                                | 9.37 ms: 1.44x faster                                                    |
| xml_etree_process    | 74.9 ms                                                | 53.5 ms: 1.40x faster                                                    |
| xml_etree_generate   | 94.2 ms                                                | 77.1 ms: 1.22x faster                                                    |
| json_loads           | 28.8 us                                                | 24.2 us: 1.19x faster                                                    |
| pickle_list          | 4.56 us                                                | 4.07 us: 1.12x faster                                                    |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                                     |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.09x faster                                                     |
| unpickle             | 14.1 us                                                | 13.1 us: 1.08x faster                                                    |
| pickle               | 10.3 us                                                | 9.99 us: 1.03x faster                                                    |
| unpickle_list        | 4.82 us                                                | 5.07 us: 1.05x slower                                                    |
| pickle_dict          | 27.3 us                                                | 30.6 us: 1.12x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.90 ms: 1.59x faster                                                    |
| python_startup_no_site | 5.82 ms                                                | 6.46 ms: 1.11x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.20x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.63 ms: 1.53x faster                                                    |
| genshi_text     | 30.3 ms                                                | 20.5 ms: 1.48x faster                                                    |
| django_template | 45.9 ms                                                | 33.2 ms: 1.38x faster                                                    |
| genshi_xml      | 63.3 ms                                                | 46.6 ms: 1.36x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.16 ms: 2.35x faster                                                    |
| logging_silent          | 175 ns                                                 | 90.7 ns: 1.93x faster                                                    |
| asyncio_tcp             | 925 ms                                                 | 491 ms: 1.88x faster                                                     |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.85x faster                                                     |
| richards                | 74.9 ms                                                | 41.9 ms: 1.79x faster                                                    |
| go                      | 229 ms                                                 | 136 ms: 1.68x faster                                                     |
| pyflate                 | 673 ms                                                 | 406 ms: 1.66x faster                                                     |
| scimark_monte_carlo     | 108 ms                                                 | 65.3 ms: 1.66x faster                                                    |
| chaos                   | 106 ms                                                 | 64.6 ms: 1.65x faster                                                    |
| raytrace                | 464 ms                                                 | 285 ms: 1.63x faster                                                     |
| crypto_pyaes            | 118 ms                                                 | 73.2 ms: 1.62x faster                                                    |
| pickle_pure_python      | 455 us                                                 | 284 us: 1.60x faster                                                     |
| hexiom                  | 9.53 ms                                                | 5.96 ms: 1.60x faster                                                    |
| python_startup          | 14.2 ms                                                | 8.90 ms: 1.59x faster                                                    |
| spectral_norm           | 150 ms                                                 | 94.9 ms: 1.58x faster                                                    |
| scimark_lu              | 163 ms                                                 | 106 ms: 1.54x faster                                                     |
| float                   | 111 ms                                                 | 72.1 ms: 1.53x faster                                                    |
| mako                    | 14.8 ms                                                | 9.63 ms: 1.53x faster                                                    |
| deepcopy_memo           | 52.3 us                                                | 34.5 us: 1.52x faster                                                    |
| unpickle_pure_python    | 300 us                                                 | 198 us: 1.52x faster                                                     |
| unpack_sequence         | 64.7 ns                                                | 43.0 ns: 1.50x faster                                                    |
| nbody                   | 142 ms                                                 | 95.5 ms: 1.48x faster                                                    |
| genshi_text             | 30.3 ms                                                | 20.5 ms: 1.48x faster                                                    |
| sqlglot_parse           | 2.06 ms                                                | 1.40 ms: 1.47x faster                                                    |
| sqlglot_transpile       | 2.45 ms                                                | 1.69 ms: 1.45x faster                                                    |
| pprint_pformat          | 1.99 sec                                               | 1.37 sec: 1.45x faster                                                   |
| json_dumps              | 13.5 ms                                                | 9.37 ms: 1.44x faster                                                    |
| html5lib                | 85.9 ms                                                | 59.6 ms: 1.44x faster                                                    |
| pprint_safe_repr        | 955 ms                                                 | 668 ms: 1.43x faster                                                     |
| chameleon               | 9.06 ms                                                | 6.36 ms: 1.42x faster                                                    |
| logging_simple          | 8.07 us                                                | 5.69 us: 1.42x faster                                                    |
| logging_format          | 8.91 us                                                | 6.29 us: 1.42x faster                                                    |
| xml_etree_process       | 74.9 ms                                                | 53.5 ms: 1.40x faster                                                    |
| thrift                  | 1.03 ms                                                | 739 us: 1.40x faster                                                     |
| scimark_fft             | 424 ms                                                 | 303 ms: 1.40x faster                                                     |
| regex_compile           | 177 ms                                                 | 127 ms: 1.39x faster                                                     |
| aiohttp                 | 1.38 ms                                                | 995 us: 1.39x faster                                                     |
| django_template         | 45.9 ms                                                | 33.2 ms: 1.38x faster                                                    |
| gunicorn                | 1.46 ms                                                | 1.07 ms: 1.37x faster                                                    |
| async_tree_none         | 717 ms                                                 | 524 ms: 1.37x faster                                                     |
| tornado_http            | 127 ms                                                 | 93.8 ms: 1.36x faster                                                    |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.01 ms: 1.36x faster                                                    |
| genshi_xml              | 63.3 ms                                                | 46.6 ms: 1.36x faster                                                    |
| pycparser               | 1.50 sec                                               | 1.11 sec: 1.36x faster                                                   |
| 2to3                    | 336 ms                                                 | 251 ms: 1.34x faster                                                     |
| async_tree_io           | 1.77 sec                                               | 1.33 sec: 1.34x faster                                                   |
| deepcopy                | 442 us                                                 | 332 us: 1.33x faster                                                     |
| fannkuch                | 486 ms                                                 | 370 ms: 1.32x faster                                                     |
| deepcopy_reduce         | 3.82 us                                                | 2.95 us: 1.30x faster                                                    |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                                     |
| nqueens                 | 100 ms                                                 | 77.8 ms: 1.29x faster                                                    |
| async_tree_memoization  | 854 ms                                                 | 667 ms: 1.28x faster                                                     |
| sqlglot_optimize        | 65.3 ms                                                | 51.0 ms: 1.28x faster                                                    |
| docutils                | 3.17 sec                                               | 2.49 sec: 1.28x faster                                                   |
| async_tree_cpu_io_mixed | 951 ms                                                 | 754 ms: 1.26x faster                                                     |
| coroutines              | 31.8 ms                                                | 25.3 ms: 1.26x faster                                                    |
| sympy_integrate         | 24.3 ms                                                | 19.7 ms: 1.23x faster                                                    |
| sympy_str               | 328 ms                                                 | 269 ms: 1.22x faster                                                     |
| xml_etree_generate      | 94.2 ms                                                | 77.1 ms: 1.22x faster                                                    |
| dulwich_log             | 75.9 ms                                                | 62.2 ms: 1.22x faster                                                    |
| async_generators        | 425 ms                                                 | 349 ms: 1.22x faster                                                     |
| bench_thread_pool       | 947 us                                                 | 780 us: 1.21x faster                                                     |
| sqlalchemy_declarative  | 165 ms                                                 | 136 ms: 1.21x faster                                                     |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.5 ms: 1.21x faster                                                    |
| sympy_expand            | 545 ms                                                 | 454 ms: 1.20x faster                                                     |
| json_loads              | 28.8 us                                                | 24.2 us: 1.19x faster                                                    |
| sympy_sum               | 185 ms                                                 | 156 ms: 1.19x faster                                                     |
| regex_v8                | 25.0 ms                                                | 21.2 ms: 1.18x faster                                                    |
| json                    | 5.42 ms                                                | 4.66 ms: 1.16x faster                                                    |
| create_gc_cycles        | 1.67 ms                                                | 1.46 ms: 1.15x faster                                                    |
| sqlite_synth            | 2.93 us                                                | 2.58 us: 1.14x faster                                                    |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                                    |
| pickle_list             | 4.56 us                                                | 4.07 us: 1.12x faster                                                    |
| regex_dna               | 222 ms                                                 | 200 ms: 1.11x faster                                                     |
| djangocms               | 35.9 us                                                | 32.5 us: 1.11x faster                                                    |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                                     |
| gc_traversal            | 3.84 ms                                                | 3.52 ms: 1.09x faster                                                    |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.09x faster                                                     |
| meteor_contest          | 115 ms                                                 | 106 ms: 1.08x faster                                                     |
| mdp                     | 2.82 sec                                               | 2.60 sec: 1.08x faster                                                   |
| unpickle                | 14.1 us                                                | 13.1 us: 1.08x faster                                                    |
| telco                   | 6.54 ms                                                | 6.33 ms: 1.03x faster                                                    |
| pickle                  | 10.3 us                                                | 9.99 us: 1.03x faster                                                    |
| generators              | 76.8 ms                                                | 75.6 ms: 1.02x faster                                                    |
| pidigits                | 190 ms                                                 | 197 ms: 1.04x slower                                                     |
| unpickle_list           | 4.82 us                                                | 5.07 us: 1.05x slower                                                    |
| regex_effbot            | 3.23 ms                                                | 3.50 ms: 1.08x slower                                                    |
| python_startup_no_site  | 5.82 ms                                                | 6.46 ms: 1.11x slower                                                    |
| pickle_dict             | 27.3 us                                                | 30.6 us: 1.12x slower                                                    |
| coverage                | 72.8 ms                                                | 98.4 ms: 1.35x slower                                                    |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                             |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, dask, flaskblogging, mypy2, pylint, richards_super, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230207-3.12.0a4+-f1deb5c/bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.27x
