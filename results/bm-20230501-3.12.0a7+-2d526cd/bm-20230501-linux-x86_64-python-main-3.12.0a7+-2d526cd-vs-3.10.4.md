
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 2d526cd
- commit date: 2023-05-01
- overall geometric mean: 1.25x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230501-linux-x86_64-python-main-3.12.0a7+-2d526cd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 268 ms: 1.26x faster                                   |
| docutils       | 3.17 sec                                               | 2.73 sec: 1.16x faster                                 |
| html5lib       | 85.9 ms                                                | 65.2 ms: 1.32x faster                                  |
| tornado_http   | 127 ms                                                 | 99.2 ms: 1.28x faster                                  |
| Geometric mean | (ref)                                                  | 1.25x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230501-linux-x86_64-python-main-3.12.0a7+-2d526cd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 142 ms                                                 | 88.6 ms: 1.60x faster                                  |
| float          | 111 ms                                                 | 81.3 ms: 1.36x faster                                  |
| pidigits       | 190 ms                                                 | 189 ms: 1.01x faster                                   |
| Geometric mean | (ref)                                                  | 1.30x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230501-linux-x86_64-python-main-3.12.0a7+-2d526cd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 145 ms: 1.22x faster                                   |
| regex_v8       | 25.0 ms                                                | 22.0 ms: 1.14x faster                                  |
| regex_dna      | 222 ms                                                 | 200 ms: 1.11x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.67 ms: 1.14x slower                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230501-linux-x86_64-python-main-3.12.0a7+-2d526cd |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 314 us: 1.45x faster                                   |
| unpickle_pure_python | 300 us                                                 | 216 us: 1.39x faster                                   |
| json_dumps           | 13.5 ms                                                | 9.99 ms: 1.36x faster                                  |
| xml_etree_process    | 74.9 ms                                                | 59.1 ms: 1.27x faster                                  |
| json_loads           | 28.8 us                                                | 25.8 us: 1.12x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 84.6 ms: 1.11x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                   |
| xml_etree_parse      | 163 ms                                                 | 151 ms: 1.08x faster                                   |
| pickle_list          | 4.56 us                                                | 4.51 us: 1.01x faster                                  |
| unpickle_list        | 4.82 us                                                | 4.93 us: 1.02x slower                                  |
| pickle               | 10.3 us                                                | 10.6 us: 1.03x slower                                  |
| unpickle             | 14.1 us                                                | 14.7 us: 1.04x slower                                  |
| pickle_dict          | 27.3 us                                                | 31.8 us: 1.17x slower                                  |
| Geometric mean       | (ref)                                                  | 1.11x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230501-linux-x86_64-python-main-3.12.0a7+-2d526cd |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.07 ms: 1.56x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.65 ms: 1.14x slower                                  |
| Geometric mean         | (ref)                                                  | 1.17x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230501-linux-x86_64-python-main-3.12.0a7+-2d526cd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako           | 14.8 ms                                                | 10.8 ms: 1.37x faster                                  |
| genshi_text    | 30.3 ms                                                | 22.4 ms: 1.35x faster                                  |
| genshi_xml     | 63.3 ms                                                | 50.2 ms: 1.26x faster                                  |
| Geometric mean | (ref)                                                  | 1.33x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230501-linux-x86_64-python-main-3.12.0a7+-2d526cd |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| generators              | 76.8 ms                                                | 30.7 ms: 2.50x faster                                  |
| deltablue               | 7.42 ms                                                | 3.57 ms: 2.08x faster                                  |
| asyncio_tcp             | 925 ms                                                 | 509 ms: 1.82x faster                                   |
| richards                | 74.9 ms                                                | 43.7 ms: 1.71x faster                                  |
| logging_silent          | 175 ns                                                 | 104 ns: 1.69x faster                                   |
| go                      | 229 ms                                                 | 137 ms: 1.68x faster                                   |
| nbody                   | 142 ms                                                 | 88.6 ms: 1.60x faster                                  |
| scimark_sor             | 197 ms                                                 | 123 ms: 1.59x faster                                   |
| python_startup          | 14.2 ms                                                | 9.07 ms: 1.56x faster                                  |
| sqlglot_parse           | 2.06 ms                                                | 1.33 ms: 1.55x faster                                  |
| chaos                   | 106 ms                                                 | 69.4 ms: 1.53x faster                                  |
| hexiom                  | 9.53 ms                                                | 6.22 ms: 1.53x faster                                  |
| raytrace                | 464 ms                                                 | 303 ms: 1.53x faster                                   |
| pyflate                 | 673 ms                                                 | 450 ms: 1.50x faster                                   |
| scimark_monte_carlo     | 108 ms                                                 | 72.6 ms: 1.49x faster                                  |
| crypto_pyaes            | 118 ms                                                 | 79.7 ms: 1.49x faster                                  |
| sqlglot_transpile       | 2.45 ms                                                | 1.65 ms: 1.48x faster                                  |
| spectral_norm           | 150 ms                                                 | 101 ms: 1.48x faster                                   |
| scimark_lu              | 163 ms                                                 | 112 ms: 1.46x faster                                   |
| async_tree_io           | 1.77 sec                                               | 1.22 sec: 1.45x faster                                 |
| pickle_pure_python      | 455 us                                                 | 314 us: 1.45x faster                                   |
| async_tree_none         | 717 ms                                                 | 495 ms: 1.45x faster                                   |
| coroutines              | 31.8 ms                                                | 22.1 ms: 1.44x faster                                  |
| async_tree_memoization  | 854 ms                                                 | 611 ms: 1.40x faster                                   |
| unpickle_pure_python    | 300 us                                                 | 216 us: 1.39x faster                                   |
| mako                    | 14.8 ms                                                | 10.8 ms: 1.37x faster                                  |
| deepcopy_memo           | 52.3 us                                                | 38.4 us: 1.36x faster                                  |
| float                   | 111 ms                                                 | 81.3 ms: 1.36x faster                                  |
| json_dumps              | 13.5 ms                                                | 9.99 ms: 1.36x faster                                  |
| genshi_text             | 30.3 ms                                                | 22.4 ms: 1.35x faster                                  |
| unpack_sequence         | 64.7 ns                                                | 47.9 ns: 1.35x faster                                  |
| async_tree_cpu_io_mixed | 951 ms                                                 | 718 ms: 1.32x faster                                   |
| pycparser               | 1.50 sec                                               | 1.14 sec: 1.32x faster                                 |
| pprint_pformat          | 1.99 sec                                               | 1.51 sec: 1.32x faster                                 |
| html5lib                | 85.9 ms                                                | 65.2 ms: 1.32x faster                                  |
| logging_simple          | 8.07 us                                                | 6.22 us: 1.30x faster                                  |
| thrift                  | 1.03 ms                                                | 797 us: 1.30x faster                                   |
| pprint_safe_repr        | 955 ms                                                 | 738 ms: 1.29x faster                                   |
| fannkuch                | 486 ms                                                 | 377 ms: 1.29x faster                                   |
| logging_format          | 8.91 us                                                | 6.93 us: 1.29x faster                                  |
| tornado_http            | 127 ms                                                 | 99.2 ms: 1.28x faster                                  |
| xml_etree_process       | 74.9 ms                                                | 59.1 ms: 1.27x faster                                  |
| genshi_xml              | 63.3 ms                                                | 50.2 ms: 1.26x faster                                  |
| 2to3                    | 336 ms                                                 | 268 ms: 1.26x faster                                   |
| mypy2                   | 428 ms                                                 | 351 ms: 1.22x faster                                   |
| regex_compile           | 177 ms                                                 | 145 ms: 1.22x faster                                   |
| deepcopy                | 442 us                                                 | 364 us: 1.22x faster                                   |
| sqlglot_normalize       | 135 ms                                                 | 112 ms: 1.21x faster                                   |
| nqueens                 | 100 ms                                                 | 83.4 ms: 1.20x faster                                  |
| sqlglot_optimize        | 65.3 ms                                                | 54.7 ms: 1.19x faster                                  |
| deepcopy_reduce         | 3.82 us                                                | 3.21 us: 1.19x faster                                  |
| scimark_fft             | 424 ms                                                 | 357 ms: 1.19x faster                                   |
| docutils                | 3.17 sec                                               | 2.73 sec: 1.16x faster                                 |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.71 ms: 1.16x faster                                  |
| comprehensions          | 26.8 us                                                | 23.4 us: 1.15x faster                                  |
| create_gc_cycles        | 1.67 ms                                                | 1.46 ms: 1.14x faster                                  |
| regex_v8                | 25.0 ms                                                | 22.0 ms: 1.14x faster                                  |
| bench_thread_pool       | 947 us                                                 | 836 us: 1.13x faster                                   |
| sqlalchemy_declarative  | 165 ms                                                 | 147 ms: 1.13x faster                                   |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                  |
| json_loads              | 28.8 us                                                | 25.8 us: 1.12x faster                                  |
| xml_etree_generate      | 94.2 ms                                                | 84.6 ms: 1.11x faster                                  |
| dulwich_log             | 75.9 ms                                                | 68.3 ms: 1.11x faster                                  |
| sqlalchemy_imperative   | 21.2 ms                                                | 19.1 ms: 1.11x faster                                  |
| regex_dna               | 222 ms                                                 | 200 ms: 1.11x faster                                   |
| json                    | 5.42 ms                                                | 4.93 ms: 1.10x faster                                  |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                   |
| mdp                     | 2.82 sec                                               | 2.59 sec: 1.09x faster                                 |
| sqlite_synth            | 2.93 us                                                | 2.70 us: 1.09x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 151 ms: 1.08x faster                                   |
| pickle_list             | 4.56 us                                                | 4.51 us: 1.01x faster                                  |
| pidigits                | 190 ms                                                 | 189 ms: 1.01x faster                                   |
| async_generators        | 425 ms                                                 | 434 ms: 1.02x slower                                   |
| unpickle_list           | 4.82 us                                                | 4.93 us: 1.02x slower                                  |
| pickle                  | 10.3 us                                                | 10.6 us: 1.03x slower                                  |
| unpickle                | 14.1 us                                                | 14.7 us: 1.04x slower                                  |
| telco                   | 6.54 ms                                                | 6.88 ms: 1.05x slower                                  |
| gc_traversal            | 3.84 ms                                                | 4.06 ms: 1.06x slower                                  |
| regex_effbot            | 3.23 ms                                                | 3.67 ms: 1.14x slower                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.65 ms: 1.14x slower                                  |
| pickle_dict             | 27.3 us                                                | 31.8 us: 1.17x slower                                  |
| dask                    | 423 ms                                                 | 539 ms: 1.28x slower                                   |
| coverage                | 72.8 ms                                                | 100 ms: 1.38x slower                                   |
| Geometric mean          | (ref)                                                  | 1.25x faster                                           |

Benchmark hidden because not significant (2): bench_mp_pool, meteor_contest
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, djangocms, flaskblogging, gunicorn, pylint, richards_super, sympy_expand, sympy_integrate, sympy_str, sympy_sum, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.19x
