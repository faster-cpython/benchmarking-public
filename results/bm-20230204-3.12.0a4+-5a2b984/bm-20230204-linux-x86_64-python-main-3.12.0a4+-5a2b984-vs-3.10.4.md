
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 5a2b984
- commit date: 2023-02-04
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-linux-x86_64-python-main-3.12.0a4+-5a2b984 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 253 ms: 1.33x faster                                   |
| chameleon      | 9.06 ms                                                | 6.29 ms: 1.44x faster                                  |
| docutils       | 3.17 sec                                               | 2.51 sec: 1.26x faster                                 |
| html5lib       | 85.9 ms                                                | 60.0 ms: 1.43x faster                                  |
| tornado_http   | 127 ms                                                 | 94.1 ms: 1.35x faster                                  |
| Geometric mean | (ref)                                                  | 1.36x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-linux-x86_64-python-main-3.12.0a4+-5a2b984 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 111 ms                                                 | 72.8 ms: 1.52x faster                                  |
| nbody          | 142 ms                                                 | 93.8 ms: 1.51x faster                                  |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.32x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-linux-x86_64-python-main-3.12.0a4+-5a2b984 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.38x faster                                   |
| regex_v8       | 25.0 ms                                                | 22.4 ms: 1.12x faster                                  |
| regex_dna      | 222 ms                                                 | 216 ms: 1.03x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.64 ms: 1.13x slower                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-linux-x86_64-python-main-3.12.0a4+-5a2b984 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 283 us: 1.61x faster                                   |
| unpickle_pure_python | 300 us                                                 | 197 us: 1.52x faster                                   |
| json_dumps           | 13.5 ms                                                | 9.26 ms: 1.46x faster                                  |
| xml_etree_process    | 74.9 ms                                                | 53.2 ms: 1.41x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 77.3 ms: 1.22x faster                                  |
| json_loads           | 28.8 us                                                | 23.9 us: 1.21x faster                                  |
| pickle_list          | 4.56 us                                                | 4.05 us: 1.13x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 146 ms: 1.12x faster                                   |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.10x faster                                   |
| unpickle             | 14.1 us                                                | 13.0 us: 1.09x faster                                  |
| pickle               | 10.3 us                                                | 10.2 us: 1.01x faster                                  |
| unpickle_list        | 4.82 us                                                | 5.02 us: 1.04x slower                                  |
| pickle_dict          | 27.3 us                                                | 30.8 us: 1.13x slower                                  |
| Geometric mean       | (ref)                                                  | 1.19x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-linux-x86_64-python-main-3.12.0a4+-5a2b984 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.93 ms: 1.58x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.46 ms: 1.11x slower                                  |
| Geometric mean         | (ref)                                                  | 1.19x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-linux-x86_64-python-main-3.12.0a4+-5a2b984 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.70 ms: 1.52x faster                                  |
| genshi_text     | 30.3 ms                                                | 20.6 ms: 1.47x faster                                  |
| django_template | 45.9 ms                                                | 32.8 ms: 1.40x faster                                  |
| genshi_xml      | 63.3 ms                                                | 47.1 ms: 1.34x faster                                  |
| Geometric mean  | (ref)                                                  | 1.43x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-linux-x86_64-python-main-3.12.0a4+-5a2b984 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.22 ms: 2.30x faster                                  |
| logging_silent          | 175 ns                                                 | 92.8 ns: 1.89x faster                                  |
| asyncio_tcp             | 925 ms                                                 | 494 ms: 1.87x faster                                   |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.83x faster                                   |
| richards                | 74.9 ms                                                | 43.2 ms: 1.74x faster                                  |
| go                      | 229 ms                                                 | 136 ms: 1.69x faster                                   |
| pyflate                 | 673 ms                                                 | 405 ms: 1.66x faster                                   |
| chaos                   | 106 ms                                                 | 64.7 ms: 1.64x faster                                  |
| spectral_norm           | 150 ms                                                 | 91.5 ms: 1.64x faster                                  |
| crypto_pyaes            | 118 ms                                                 | 72.3 ms: 1.64x faster                                  |
| scimark_monte_carlo     | 108 ms                                                 | 66.8 ms: 1.62x faster                                  |
| pickle_pure_python      | 455 us                                                 | 283 us: 1.61x faster                                   |
| raytrace                | 464 ms                                                 | 288 ms: 1.61x faster                                   |
| hexiom                  | 9.53 ms                                                | 6.01 ms: 1.59x faster                                  |
| python_startup          | 14.2 ms                                                | 8.93 ms: 1.58x faster                                  |
| deepcopy_memo           | 52.3 us                                                | 34.1 us: 1.53x faster                                  |
| unpickle_pure_python    | 300 us                                                 | 197 us: 1.52x faster                                   |
| mako                    | 14.8 ms                                                | 9.70 ms: 1.52x faster                                  |
| scimark_lu              | 163 ms                                                 | 107 ms: 1.52x faster                                   |
| float                   | 111 ms                                                 | 72.8 ms: 1.52x faster                                  |
| unpack_sequence         | 64.7 ns                                                | 42.7 ns: 1.52x faster                                  |
| nbody                   | 142 ms                                                 | 93.8 ms: 1.51x faster                                  |
| genshi_text             | 30.3 ms                                                | 20.6 ms: 1.47x faster                                  |
| json_dumps              | 13.5 ms                                                | 9.26 ms: 1.46x faster                                  |
| pprint_pformat          | 1.99 sec                                               | 1.37 sec: 1.45x faster                                 |
| sqlglot_parse           | 2.06 ms                                                | 1.42 ms: 1.45x faster                                  |
| chameleon               | 9.06 ms                                                | 6.29 ms: 1.44x faster                                  |
| html5lib                | 85.9 ms                                                | 60.0 ms: 1.43x faster                                  |
| pprint_safe_repr        | 955 ms                                                 | 668 ms: 1.43x faster                                   |
| sqlglot_transpile       | 2.45 ms                                                | 1.71 ms: 1.43x faster                                  |
| logging_format          | 8.91 us                                                | 6.28 us: 1.42x faster                                  |
| scimark_fft             | 424 ms                                                 | 299 ms: 1.42x faster                                   |
| logging_simple          | 8.07 us                                                | 5.70 us: 1.42x faster                                  |
| xml_etree_process       | 74.9 ms                                                | 53.2 ms: 1.41x faster                                  |
| django_template         | 45.9 ms                                                | 32.8 ms: 1.40x faster                                  |
| aiohttp                 | 1.38 ms                                                | 999 us: 1.38x faster                                   |
| thrift                  | 1.03 ms                                                | 747 us: 1.38x faster                                   |
| regex_compile           | 177 ms                                                 | 128 ms: 1.38x faster                                   |
| async_tree_none         | 717 ms                                                 | 524 ms: 1.37x faster                                   |
| gunicorn                | 1.46 ms                                                | 1.08 ms: 1.36x faster                                  |
| tornado_http            | 127 ms                                                 | 94.1 ms: 1.35x faster                                  |
| deepcopy                | 442 us                                                 | 327 us: 1.35x faster                                   |
| async_tree_io           | 1.77 sec                                               | 1.32 sec: 1.35x faster                                 |
| genshi_xml              | 63.3 ms                                                | 47.1 ms: 1.34x faster                                  |
| 2to3                    | 336 ms                                                 | 253 ms: 1.33x faster                                   |
| fannkuch                | 486 ms                                                 | 368 ms: 1.32x faster                                   |
| pycparser               | 1.50 sec                                               | 1.14 sec: 1.32x faster                                 |
| async_tree_memoization  | 854 ms                                                 | 655 ms: 1.30x faster                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.20 ms: 1.30x faster                                  |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                   |
| sqlglot_optimize        | 65.3 ms                                                | 50.7 ms: 1.29x faster                                  |
| deepcopy_reduce         | 3.82 us                                                | 2.97 us: 1.29x faster                                  |
| coroutines              | 31.8 ms                                                | 24.9 ms: 1.28x faster                                  |
| nqueens                 | 100 ms                                                 | 78.8 ms: 1.27x faster                                  |
| docutils                | 3.17 sec                                               | 2.51 sec: 1.26x faster                                 |
| async_tree_cpu_io_mixed | 951 ms                                                 | 755 ms: 1.26x faster                                   |
| sympy_integrate         | 24.3 ms                                                | 19.8 ms: 1.23x faster                                  |
| xml_etree_generate      | 94.2 ms                                                | 77.3 ms: 1.22x faster                                  |
| async_generators        | 425 ms                                                 | 349 ms: 1.22x faster                                   |
| sympy_str               | 328 ms                                                 | 272 ms: 1.21x faster                                   |
| json_loads              | 28.8 us                                                | 23.9 us: 1.21x faster                                  |
| bench_thread_pool       | 947 us                                                 | 785 us: 1.21x faster                                   |
| dulwich_log             | 75.9 ms                                                | 63.2 ms: 1.20x faster                                  |
| sympy_expand            | 545 ms                                                 | 457 ms: 1.19x faster                                   |
| sympy_sum               | 185 ms                                                 | 156 ms: 1.19x faster                                   |
| json                    | 5.42 ms                                                | 4.57 ms: 1.18x faster                                  |
| create_gc_cycles        | 1.67 ms                                                | 1.46 ms: 1.14x faster                                  |
| sqlite_synth            | 2.93 us                                                | 2.59 us: 1.13x faster                                  |
| pickle_list             | 4.56 us                                                | 4.05 us: 1.13x faster                                  |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                  |
| regex_v8                | 25.0 ms                                                | 22.4 ms: 1.12x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 146 ms: 1.12x faster                                   |
| mdp                     | 2.82 sec                                               | 2.53 sec: 1.11x faster                                 |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.10x faster                                   |
| djangocms               | 35.9 us                                                | 32.8 us: 1.09x faster                                  |
| unpickle                | 14.1 us                                                | 13.0 us: 1.09x faster                                  |
| meteor_contest          | 115 ms                                                 | 107 ms: 1.07x faster                                   |
| gc_traversal            | 3.84 ms                                                | 3.65 ms: 1.05x faster                                  |
| telco                   | 6.54 ms                                                | 6.35 ms: 1.03x faster                                  |
| regex_dna               | 222 ms                                                 | 216 ms: 1.03x faster                                   |
| pickle                  | 10.3 us                                                | 10.2 us: 1.01x faster                                  |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                   |
| unpickle_list           | 4.82 us                                                | 5.02 us: 1.04x slower                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.46 ms: 1.11x slower                                  |
| regex_effbot            | 3.23 ms                                                | 3.64 ms: 1.13x slower                                  |
| pickle_dict             | 27.3 us                                                | 30.8 us: 1.13x slower                                  |
| dask                    | 423 ms                                                 | 501 ms: 1.19x slower                                   |
| coverage                | 72.8 ms                                                | 96.2 ms: 1.32x slower                                  |
| Geometric mean          | (ref)                                                  | 1.30x faster                                           |

Benchmark hidden because not significant (2): bench_mp_pool, generators
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230204-3.12.0a4+-5a2b984/bm-20230204-linux-x86_64-python-main-3.12.0a4+-5a2b984.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x
