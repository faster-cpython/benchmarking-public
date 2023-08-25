
# Results vs. 3.10.4

- fork: python
- ref: b724ac2fe7fbb5a7a33d
- machine: linux-x86_64
- commit hash: b724ac2
- commit date: 2023-01-23
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 253 ms: 1.33x faster                                                   |
| chameleon      | 9.06 ms                                                | 6.42 ms: 1.41x faster                                                  |
| docutils       | 3.17 sec                                               | 2.52 sec: 1.26x faster                                                 |
| html5lib       | 85.9 ms                                                | 60.3 ms: 1.42x faster                                                  |
| tornado_http   | 127 ms                                                 | 93.7 ms: 1.36x faster                                                  |
| Geometric mean | (ref)                                                  | 1.36x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 111 ms                                                 | 72.6 ms: 1.52x faster                                                  |
| nbody          | 142 ms                                                 | 93.8 ms: 1.51x faster                                                  |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.30x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.37x faster                                                   |
| regex_v8       | 25.0 ms                                                | 21.0 ms: 1.19x faster                                                  |
| regex_dna      | 222 ms                                                 | 201 ms: 1.10x faster                                                   |
| regex_effbot   | 3.23 ms                                                | 3.44 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                  | 1.14x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 284 us: 1.60x faster                                                   |
| unpickle_pure_python | 300 us                                                 | 197 us: 1.52x faster                                                   |
| json_dumps           | 13.5 ms                                                | 9.38 ms: 1.44x faster                                                  |
| xml_etree_process    | 74.9 ms                                                | 54.4 ms: 1.38x faster                                                  |
| xml_etree_generate   | 94.2 ms                                                | 79.1 ms: 1.19x faster                                                  |
| json_loads           | 28.8 us                                                | 24.3 us: 1.19x faster                                                  |
| pickle_list          | 4.56 us                                                | 4.26 us: 1.07x faster                                                  |
| unpickle             | 14.1 us                                                | 13.4 us: 1.05x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                 | 106 ms: 1.05x faster                                                   |
| xml_etree_parse      | 163 ms                                                 | 156 ms: 1.04x faster                                                   |
| unpickle_list        | 4.82 us                                                | 5.08 us: 1.05x slower                                                  |
| pickle_dict          | 27.3 us                                                | 32.2 us: 1.18x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                           |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.96 ms: 1.58x faster                                                  |
| python_startup_no_site | 5.82 ms                                                | 6.49 ms: 1.12x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.66 ms: 1.53x faster                                                  |
| django_template | 45.9 ms                                                | 32.9 ms: 1.39x faster                                                  |
| genshi_text     | 30.3 ms                                                | 22.1 ms: 1.37x faster                                                  |
| genshi_xml      | 63.3 ms                                                | 46.8 ms: 1.35x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.23 ms: 2.30x faster                                                  |
| asyncio_tcp             | 925 ms                                                 | 490 ms: 1.89x faster                                                   |
| logging_silent          | 175 ns                                                 | 93.3 ns: 1.88x faster                                                  |
| scimark_sor             | 197 ms                                                 | 105 ms: 1.87x faster                                                   |
| richards                | 74.9 ms                                                | 42.9 ms: 1.74x faster                                                  |
| go                      | 229 ms                                                 | 136 ms: 1.69x faster                                                   |
| pyflate                 | 673 ms                                                 | 400 ms: 1.68x faster                                                   |
| chaos                   | 106 ms                                                 | 63.6 ms: 1.67x faster                                                  |
| scimark_monte_carlo     | 108 ms                                                 | 65.2 ms: 1.66x faster                                                  |
| raytrace                | 464 ms                                                 | 280 ms: 1.65x faster                                                   |
| crypto_pyaes            | 118 ms                                                 | 73.3 ms: 1.62x faster                                                  |
| pickle_pure_python      | 455 us                                                 | 284 us: 1.60x faster                                                   |
| hexiom                  | 9.53 ms                                                | 5.95 ms: 1.60x faster                                                  |
| python_startup          | 14.2 ms                                                | 8.96 ms: 1.58x faster                                                  |
| unpack_sequence         | 64.7 ns                                                | 41.6 ns: 1.55x faster                                                  |
| spectral_norm           | 150 ms                                                 | 97.7 ms: 1.54x faster                                                  |
| mako                    | 14.8 ms                                                | 9.66 ms: 1.53x faster                                                  |
| scimark_lu              | 163 ms                                                 | 107 ms: 1.52x faster                                                   |
| unpickle_pure_python    | 300 us                                                 | 197 us: 1.52x faster                                                   |
| float                   | 111 ms                                                 | 72.6 ms: 1.52x faster                                                  |
| deepcopy_memo           | 52.3 us                                                | 34.6 us: 1.51x faster                                                  |
| nbody                   | 142 ms                                                 | 93.8 ms: 1.51x faster                                                  |
| sqlglot_parse           | 2.06 ms                                                | 1.41 ms: 1.46x faster                                                  |
| json_dumps              | 13.5 ms                                                | 9.38 ms: 1.44x faster                                                  |
| sqlglot_transpile       | 2.45 ms                                                | 1.71 ms: 1.43x faster                                                  |
| pprint_pformat          | 1.99 sec                                               | 1.39 sec: 1.43x faster                                                 |
| html5lib                | 85.9 ms                                                | 60.3 ms: 1.42x faster                                                  |
| pprint_safe_repr        | 955 ms                                                 | 674 ms: 1.42x faster                                                   |
| chameleon               | 9.06 ms                                                | 6.42 ms: 1.41x faster                                                  |
| logging_format          | 8.91 us                                                | 6.34 us: 1.40x faster                                                  |
| logging_simple          | 8.07 us                                                | 5.74 us: 1.40x faster                                                  |
| django_template         | 45.9 ms                                                | 32.9 ms: 1.39x faster                                                  |
| aiohttp                 | 1.38 ms                                                | 994 us: 1.39x faster                                                   |
| thrift                  | 1.03 ms                                                | 746 us: 1.38x faster                                                   |
| scimark_fft             | 424 ms                                                 | 306 ms: 1.38x faster                                                   |
| xml_etree_process       | 74.9 ms                                                | 54.4 ms: 1.38x faster                                                  |
| genshi_text             | 30.3 ms                                                | 22.1 ms: 1.37x faster                                                  |
| pycparser               | 1.50 sec                                               | 1.10 sec: 1.37x faster                                                 |
| regex_compile           | 177 ms                                                 | 129 ms: 1.37x faster                                                   |
| gunicorn                | 1.46 ms                                                | 1.07 ms: 1.37x faster                                                  |
| tornado_http            | 127 ms                                                 | 93.7 ms: 1.36x faster                                                  |
| async_tree_none         | 717 ms                                                 | 528 ms: 1.36x faster                                                   |
| genshi_xml              | 63.3 ms                                                | 46.8 ms: 1.35x faster                                                  |
| deepcopy                | 442 us                                                 | 327 us: 1.35x faster                                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.06 ms: 1.34x faster                                                  |
| fannkuch                | 486 ms                                                 | 363 ms: 1.34x faster                                                   |
| async_tree_io           | 1.77 sec                                               | 1.33 sec: 1.34x faster                                                 |
| 2to3                    | 336 ms                                                 | 253 ms: 1.33x faster                                                   |
| nqueens                 | 100 ms                                                 | 76.2 ms: 1.31x faster                                                  |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                                   |
| deepcopy_reduce         | 3.82 us                                                | 2.97 us: 1.29x faster                                                  |
| async_tree_memoization  | 854 ms                                                 | 666 ms: 1.28x faster                                                   |
| sqlglot_optimize        | 65.3 ms                                                | 51.3 ms: 1.27x faster                                                  |
| docutils                | 3.17 sec                                               | 2.52 sec: 1.26x faster                                                 |
| async_tree_cpu_io_mixed | 951 ms                                                 | 755 ms: 1.26x faster                                                   |
| coroutines              | 31.8 ms                                                | 25.6 ms: 1.24x faster                                                  |
| dulwich_log             | 75.9 ms                                                | 62.0 ms: 1.23x faster                                                  |
| bench_thread_pool       | 947 us                                                 | 774 us: 1.22x faster                                                   |
| async_generators        | 425 ms                                                 | 351 ms: 1.21x faster                                                   |
| sympy_integrate         | 24.3 ms                                                | 20.2 ms: 1.20x faster                                                  |
| sympy_expand            | 545 ms                                                 | 456 ms: 1.20x faster                                                   |
| regex_v8                | 25.0 ms                                                | 21.0 ms: 1.19x faster                                                  |
| xml_etree_generate      | 94.2 ms                                                | 79.1 ms: 1.19x faster                                                  |
| json_loads              | 28.8 us                                                | 24.3 us: 1.19x faster                                                  |
| json                    | 5.42 ms                                                | 4.60 ms: 1.18x faster                                                  |
| sympy_str               | 328 ms                                                 | 281 ms: 1.17x faster                                                   |
| mdp                     | 2.82 sec                                               | 2.43 sec: 1.16x faster                                                 |
| sqlite_synth            | 2.93 us                                                | 2.58 us: 1.14x faster                                                  |
| djangocms               | 35.9 us                                                | 31.6 us: 1.14x faster                                                  |
| sympy_sum               | 185 ms                                                 | 164 ms: 1.13x faster                                                   |
| create_gc_cycles        | 1.67 ms                                                | 1.48 ms: 1.13x faster                                                  |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                                  |
| regex_dna               | 222 ms                                                 | 201 ms: 1.10x faster                                                   |
| meteor_contest          | 115 ms                                                 | 105 ms: 1.10x faster                                                   |
| pickle_list             | 4.56 us                                                | 4.26 us: 1.07x faster                                                  |
| unpickle                | 14.1 us                                                | 13.4 us: 1.05x faster                                                  |
| xml_etree_iterparse     | 111 ms                                                 | 106 ms: 1.05x faster                                                   |
| xml_etree_parse         | 163 ms                                                 | 156 ms: 1.04x faster                                                   |
| generators              | 76.8 ms                                                | 74.7 ms: 1.03x faster                                                  |
| telco                   | 6.54 ms                                                | 6.38 ms: 1.03x faster                                                  |
| gc_traversal            | 3.84 ms                                                | 3.96 ms: 1.03x slower                                                  |
| pidigits                | 190 ms                                                 | 197 ms: 1.04x slower                                                   |
| unpickle_list           | 4.82 us                                                | 5.08 us: 1.05x slower                                                  |
| regex_effbot            | 3.23 ms                                                | 3.44 ms: 1.07x slower                                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.49 ms: 1.12x slower                                                  |
| dask                    | 423 ms                                                 | 495 ms: 1.17x slower                                                   |
| pickle_dict             | 27.3 us                                                | 32.2 us: 1.18x slower                                                  |
| coverage                | 72.8 ms                                                | 97.3 ms: 1.34x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                           |

Benchmark hidden because not significant (2): bench_mp_pool, pickle
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230123-3.12.0a4+-b724ac2/bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.26x
