
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 666c084
- commit date: 2023-01-28
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230128-linux-x86_64-python-main-3.12.0a4+-666c084 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 252 ms: 1.34x faster                                   |
| chameleon      | 9.06 ms                                                | 6.45 ms: 1.41x faster                                  |
| docutils       | 3.17 sec                                               | 2.48 sec: 1.28x faster                                 |
| html5lib       | 85.9 ms                                                | 60.1 ms: 1.43x faster                                  |
| tornado_http   | 127 ms                                                 | 94.4 ms: 1.35x faster                                  |
| Geometric mean | (ref)                                                  | 1.36x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230128-linux-x86_64-python-main-3.12.0a4+-666c084 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 111 ms                                                 | 71.4 ms: 1.55x faster                                  |
| nbody          | 142 ms                                                 | 94.7 ms: 1.50x faster                                  |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.32x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230128-linux-x86_64-python-main-3.12.0a4+-666c084 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.37x faster                                   |
| regex_v8       | 25.0 ms                                                | 21.2 ms: 1.18x faster                                  |
| regex_dna      | 222 ms                                                 | 208 ms: 1.07x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.46 ms: 1.07x slower                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230128-linux-x86_64-python-main-3.12.0a4+-666c084 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 284 us: 1.60x faster                                   |
| unpickle_pure_python | 300 us                                                 | 201 us: 1.49x faster                                   |
| json_dumps           | 13.5 ms                                                | 9.57 ms: 1.41x faster                                  |
| xml_etree_process    | 74.9 ms                                                | 53.5 ms: 1.40x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 77.6 ms: 1.21x faster                                  |
| json_loads           | 28.8 us                                                | 24.1 us: 1.20x faster                                  |
| pickle_list          | 4.56 us                                                | 4.01 us: 1.14x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                   |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                   |
| unpickle             | 14.1 us                                                | 13.4 us: 1.05x faster                                  |
| unpickle_list        | 4.82 us                                                | 4.93 us: 1.02x slower                                  |
| pickle_dict          | 27.3 us                                                | 31.0 us: 1.14x slower                                  |
| Geometric mean       | (ref)                                                  | 1.18x faster                                           |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230128-linux-x86_64-python-main-3.12.0a4+-666c084 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.90 ms: 1.59x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.44 ms: 1.11x slower                                  |
| Geometric mean         | (ref)                                                  | 1.20x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230128-linux-x86_64-python-main-3.12.0a4+-666c084 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.70 ms: 1.52x faster                                  |
| genshi_text     | 30.3 ms                                                | 20.6 ms: 1.47x faster                                  |
| django_template | 45.9 ms                                                | 32.8 ms: 1.40x faster                                  |
| genshi_xml      | 63.3 ms                                                | 47.1 ms: 1.34x faster                                  |
| Geometric mean  | (ref)                                                  | 1.43x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230128-linux-x86_64-python-main-3.12.0a4+-666c084 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.19 ms: 2.32x faster                                  |
| logging_silent          | 175 ns                                                 | 92.4 ns: 1.89x faster                                  |
| asyncio_tcp             | 925 ms                                                 | 494 ms: 1.87x faster                                   |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.84x faster                                   |
| richards                | 74.9 ms                                                | 42.7 ms: 1.75x faster                                  |
| pyflate                 | 673 ms                                                 | 399 ms: 1.69x faster                                   |
| scimark_monte_carlo     | 108 ms                                                 | 65.5 ms: 1.65x faster                                  |
| raytrace                | 464 ms                                                 | 282 ms: 1.65x faster                                   |
| chaos                   | 106 ms                                                 | 64.8 ms: 1.64x faster                                  |
| go                      | 229 ms                                                 | 140 ms: 1.64x faster                                   |
| crypto_pyaes            | 118 ms                                                 | 72.9 ms: 1.62x faster                                  |
| hexiom                  | 9.53 ms                                                | 5.94 ms: 1.60x faster                                  |
| pickle_pure_python      | 455 us                                                 | 284 us: 1.60x faster                                   |
| python_startup          | 14.2 ms                                                | 8.90 ms: 1.59x faster                                  |
| float                   | 111 ms                                                 | 71.4 ms: 1.55x faster                                  |
| unpack_sequence         | 64.7 ns                                                | 41.9 ns: 1.54x faster                                  |
| spectral_norm           | 150 ms                                                 | 97.9 ms: 1.53x faster                                  |
| mako                    | 14.8 ms                                                | 9.70 ms: 1.52x faster                                  |
| scimark_lu              | 163 ms                                                 | 108 ms: 1.52x faster                                   |
| deepcopy_memo           | 52.3 us                                                | 34.7 us: 1.51x faster                                  |
| nbody                   | 142 ms                                                 | 94.7 ms: 1.50x faster                                  |
| unpickle_pure_python    | 300 us                                                 | 201 us: 1.49x faster                                   |
| genshi_text             | 30.3 ms                                                | 20.6 ms: 1.47x faster                                  |
| sqlglot_parse           | 2.06 ms                                                | 1.41 ms: 1.46x faster                                  |
| sqlglot_transpile       | 2.45 ms                                                | 1.70 ms: 1.44x faster                                  |
| pprint_pformat          | 1.99 sec                                               | 1.39 sec: 1.43x faster                                 |
| html5lib                | 85.9 ms                                                | 60.1 ms: 1.43x faster                                  |
| pprint_safe_repr        | 955 ms                                                 | 675 ms: 1.42x faster                                   |
| json_dumps              | 13.5 ms                                                | 9.57 ms: 1.41x faster                                  |
| chameleon               | 9.06 ms                                                | 6.45 ms: 1.41x faster                                  |
| logging_format          | 8.91 us                                                | 6.35 us: 1.40x faster                                  |
| django_template         | 45.9 ms                                                | 32.8 ms: 1.40x faster                                  |
| xml_etree_process       | 74.9 ms                                                | 53.5 ms: 1.40x faster                                  |
| logging_simple          | 8.07 us                                                | 5.79 us: 1.39x faster                                  |
| thrift                  | 1.03 ms                                                | 744 us: 1.39x faster                                   |
| aiohttp                 | 1.38 ms                                                | 998 us: 1.39x faster                                   |
| scimark_fft             | 424 ms                                                 | 308 ms: 1.37x faster                                   |
| regex_compile           | 177 ms                                                 | 129 ms: 1.37x faster                                   |
| gunicorn                | 1.46 ms                                                | 1.07 ms: 1.37x faster                                  |
| async_tree_none         | 717 ms                                                 | 525 ms: 1.36x faster                                   |
| pycparser               | 1.50 sec                                               | 1.10 sec: 1.36x faster                                 |
| async_tree_io           | 1.77 sec                                               | 1.31 sec: 1.36x faster                                 |
| deepcopy                | 442 us                                                 | 327 us: 1.35x faster                                   |
| tornado_http            | 127 ms                                                 | 94.4 ms: 1.35x faster                                  |
| fannkuch                | 486 ms                                                 | 361 ms: 1.35x faster                                   |
| genshi_xml              | 63.3 ms                                                | 47.1 ms: 1.34x faster                                  |
| 2to3                    | 336 ms                                                 | 252 ms: 1.34x faster                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.15 ms: 1.31x faster                                  |
| async_tree_memoization  | 854 ms                                                 | 656 ms: 1.30x faster                                   |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.28x faster                                   |
| sqlglot_optimize        | 65.3 ms                                                | 51.0 ms: 1.28x faster                                  |
| nqueens                 | 100 ms                                                 | 78.1 ms: 1.28x faster                                  |
| coroutines              | 31.8 ms                                                | 24.9 ms: 1.28x faster                                  |
| docutils                | 3.17 sec                                               | 2.48 sec: 1.28x faster                                 |
| deepcopy_reduce         | 3.82 us                                                | 3.00 us: 1.27x faster                                  |
| async_tree_cpu_io_mixed | 951 ms                                                 | 758 ms: 1.26x faster                                   |
| sympy_integrate         | 24.3 ms                                                | 19.9 ms: 1.22x faster                                  |
| async_generators        | 425 ms                                                 | 350 ms: 1.22x faster                                   |
| xml_etree_generate      | 94.2 ms                                                | 77.6 ms: 1.21x faster                                  |
| sympy_str               | 328 ms                                                 | 272 ms: 1.21x faster                                   |
| dulwich_log             | 75.9 ms                                                | 62.9 ms: 1.21x faster                                  |
| bench_thread_pool       | 947 us                                                 | 786 us: 1.20x faster                                   |
| json_loads              | 28.8 us                                                | 24.1 us: 1.20x faster                                  |
| sympy_expand            | 545 ms                                                 | 457 ms: 1.19x faster                                   |
| sympy_sum               | 185 ms                                                 | 155 ms: 1.19x faster                                   |
| regex_v8                | 25.0 ms                                                | 21.2 ms: 1.18x faster                                  |
| json                    | 5.42 ms                                                | 4.66 ms: 1.16x faster                                  |
| create_gc_cycles        | 1.67 ms                                                | 1.45 ms: 1.15x faster                                  |
| pathlib                 | 20.0 ms                                                | 17.6 ms: 1.14x faster                                  |
| sqlite_synth            | 2.93 us                                                | 2.58 us: 1.14x faster                                  |
| pickle_list             | 4.56 us                                                | 4.01 us: 1.14x faster                                  |
| djangocms               | 35.9 us                                                | 31.9 us: 1.13x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                   |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.11x faster                                   |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                   |
| regex_dna               | 222 ms                                                 | 208 ms: 1.07x faster                                   |
| unpickle                | 14.1 us                                                | 13.4 us: 1.05x faster                                  |
| mdp                     | 2.82 sec                                               | 2.68 sec: 1.05x faster                                 |
| telco                   | 6.54 ms                                                | 6.45 ms: 1.01x faster                                  |
| gc_traversal            | 3.84 ms                                                | 3.82 ms: 1.01x faster                                  |
| generators              | 76.8 ms                                                | 76.5 ms: 1.00x faster                                  |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                   |
| unpickle_list           | 4.82 us                                                | 4.93 us: 1.02x slower                                  |
| regex_effbot            | 3.23 ms                                                | 3.46 ms: 1.07x slower                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.44 ms: 1.11x slower                                  |
| pickle_dict             | 27.3 us                                                | 31.0 us: 1.14x slower                                  |
| dask                    | 423 ms                                                 | 500 ms: 1.18x slower                                   |
| coverage                | 72.8 ms                                                | 98.3 ms: 1.35x slower                                  |
| Geometric mean          | (ref)                                                  | 1.30x faster                                           |

Benchmark hidden because not significant (2): bench_mp_pool, pickle
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230128-3.12.0a4+-666c084/bm-20230128-linux-x86_64-python-main-3.12.0a4+-666c084.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.27x
