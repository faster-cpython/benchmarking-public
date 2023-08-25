
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 3eb12df
- commit date: 2023-02-11
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230211-linux-x86_64-python-main-3.12.0a5+-3eb12df |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 250 ms: 1.34x faster                                   |
| chameleon      | 9.06 ms                                                | 6.58 ms: 1.38x faster                                  |
| docutils       | 3.17 sec                                               | 2.52 sec: 1.26x faster                                 |
| html5lib       | 85.9 ms                                                | 61.1 ms: 1.41x faster                                  |
| tornado_http   | 127 ms                                                 | 94.5 ms: 1.35x faster                                  |
| Geometric mean | (ref)                                                  | 1.35x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230211-linux-x86_64-python-main-3.12.0a5+-3eb12df |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 111 ms                                                 | 72.1 ms: 1.53x faster                                  |
| nbody          | 142 ms                                                 | 94.8 ms: 1.49x faster                                  |
| pidigits       | 190 ms                                                 | 193 ms: 1.01x slower                                   |
| Geometric mean | (ref)                                                  | 1.31x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230211-linux-x86_64-python-main-3.12.0a5+-3eb12df |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.37x faster                                   |
| regex_v8       | 25.0 ms                                                | 21.2 ms: 1.18x faster                                  |
| regex_dna      | 222 ms                                                 | 199 ms: 1.11x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.56 ms: 1.10x slower                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230211-linux-x86_64-python-main-3.12.0a5+-3eb12df |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 288 us: 1.58x faster                                   |
| unpickle_pure_python | 300 us                                                 | 196 us: 1.53x faster                                   |
| json_dumps           | 13.5 ms                                                | 9.51 ms: 1.42x faster                                  |
| xml_etree_process    | 74.9 ms                                                | 55.2 ms: 1.36x faster                                  |
| json_loads           | 28.8 us                                                | 24.0 us: 1.20x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 80.5 ms: 1.17x faster                                  |
| pickle_list          | 4.56 us                                                | 4.05 us: 1.13x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                   |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                   |
| unpickle             | 14.1 us                                                | 13.4 us: 1.06x faster                                  |
| pickle               | 10.3 us                                                | 10.1 us: 1.02x faster                                  |
| unpickle_list        | 4.82 us                                                | 4.95 us: 1.03x slower                                  |
| pickle_dict          | 27.3 us                                                | 30.8 us: 1.13x slower                                  |
| Geometric mean       | (ref)                                                  | 1.18x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230211-linux-x86_64-python-main-3.12.0a5+-3eb12df |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.92 ms: 1.59x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.47 ms: 1.11x slower                                  |
| Geometric mean         | (ref)                                                  | 1.19x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230211-linux-x86_64-python-main-3.12.0a5+-3eb12df |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.95 ms: 1.48x faster                                  |
| genshi_text     | 30.3 ms                                                | 20.6 ms: 1.48x faster                                  |
| django_template | 45.9 ms                                                | 33.3 ms: 1.38x faster                                  |
| genshi_xml      | 63.3 ms                                                | 46.6 ms: 1.36x faster                                  |
| Geometric mean  | (ref)                                                  | 1.42x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230211-linux-x86_64-python-main-3.12.0a5+-3eb12df |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.11 ms: 2.38x faster                                  |
| logging_silent          | 175 ns                                                 | 91.0 ns: 1.92x faster                                  |
| asyncio_tcp             | 925 ms                                                 | 498 ms: 1.86x faster                                   |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.85x faster                                   |
| richards                | 74.9 ms                                                | 42.3 ms: 1.77x faster                                  |
| go                      | 229 ms                                                 | 133 ms: 1.72x faster                                   |
| pyflate                 | 673 ms                                                 | 398 ms: 1.69x faster                                   |
| raytrace                | 464 ms                                                 | 281 ms: 1.65x faster                                   |
| scimark_monte_carlo     | 108 ms                                                 | 65.8 ms: 1.65x faster                                  |
| hexiom                  | 9.53 ms                                                | 5.91 ms: 1.61x faster                                  |
| chaos                   | 106 ms                                                 | 66.5 ms: 1.60x faster                                  |
| python_startup          | 14.2 ms                                                | 8.92 ms: 1.59x faster                                  |
| pickle_pure_python      | 455 us                                                 | 288 us: 1.58x faster                                   |
| crypto_pyaes            | 118 ms                                                 | 75.6 ms: 1.57x faster                                  |
| float                   | 111 ms                                                 | 72.1 ms: 1.53x faster                                  |
| unpickle_pure_python    | 300 us                                                 | 196 us: 1.53x faster                                   |
| deepcopy_memo           | 52.3 us                                                | 34.3 us: 1.52x faster                                  |
| spectral_norm           | 150 ms                                                 | 98.5 ms: 1.52x faster                                  |
| scimark_lu              | 163 ms                                                 | 108 ms: 1.51x faster                                   |
| nbody                   | 142 ms                                                 | 94.8 ms: 1.49x faster                                  |
| mako                    | 14.8 ms                                                | 9.95 ms: 1.48x faster                                  |
| genshi_text             | 30.3 ms                                                | 20.6 ms: 1.48x faster                                  |
| unpack_sequence         | 64.7 ns                                                | 43.9 ns: 1.47x faster                                  |
| sqlglot_parse           | 2.06 ms                                                | 1.42 ms: 1.45x faster                                  |
| sqlglot_transpile       | 2.45 ms                                                | 1.71 ms: 1.43x faster                                  |
| json_dumps              | 13.5 ms                                                | 9.51 ms: 1.42x faster                                  |
| pprint_pformat          | 1.99 sec                                               | 1.40 sec: 1.42x faster                                 |
| html5lib                | 85.9 ms                                                | 61.1 ms: 1.41x faster                                  |
| pprint_safe_repr        | 955 ms                                                 | 684 ms: 1.40x faster                                   |
| logging_format          | 8.91 us                                                | 6.43 us: 1.39x faster                                  |
| django_template         | 45.9 ms                                                | 33.3 ms: 1.38x faster                                  |
| async_tree_memoization  | 854 ms                                                 | 620 ms: 1.38x faster                                   |
| chameleon               | 9.06 ms                                                | 6.58 ms: 1.38x faster                                  |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.38x faster                                  |
| logging_simple          | 8.07 us                                                | 5.87 us: 1.37x faster                                  |
| regex_compile           | 177 ms                                                 | 129 ms: 1.37x faster                                   |
| async_tree_none         | 717 ms                                                 | 522 ms: 1.37x faster                                   |
| pycparser               | 1.50 sec                                               | 1.10 sec: 1.37x faster                                 |
| thrift                  | 1.03 ms                                                | 761 us: 1.36x faster                                   |
| scimark_fft             | 424 ms                                                 | 312 ms: 1.36x faster                                   |
| xml_etree_process       | 74.9 ms                                                | 55.2 ms: 1.36x faster                                  |
| genshi_xml              | 63.3 ms                                                | 46.6 ms: 1.36x faster                                  |
| async_tree_io           | 1.77 sec                                               | 1.31 sec: 1.35x faster                                 |
| tornado_http            | 127 ms                                                 | 94.5 ms: 1.35x faster                                  |
| gunicorn                | 1.46 ms                                                | 1.09 ms: 1.34x faster                                  |
| 2to3                    | 336 ms                                                 | 250 ms: 1.34x faster                                   |
| deepcopy                | 442 us                                                 | 329 us: 1.34x faster                                   |
| fannkuch                | 486 ms                                                 | 363 ms: 1.34x faster                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.13 ms: 1.32x faster                                  |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.29x faster                                   |
| mypy2                   | 428 ms                                                 | 331 ms: 1.29x faster                                   |
| nqueens                 | 100 ms                                                 | 77.6 ms: 1.29x faster                                  |
| sqlglot_optimize        | 65.3 ms                                                | 50.8 ms: 1.29x faster                                  |
| deepcopy_reduce         | 3.82 us                                                | 2.97 us: 1.29x faster                                  |
| coroutines              | 31.8 ms                                                | 25.2 ms: 1.26x faster                                  |
| async_tree_cpu_io_mixed | 951 ms                                                 | 755 ms: 1.26x faster                                   |
| docutils                | 3.17 sec                                               | 2.52 sec: 1.26x faster                                 |
| sympy_integrate         | 24.3 ms                                                | 19.9 ms: 1.22x faster                                  |
| sqlalchemy_declarative  | 165 ms                                                 | 137 ms: 1.21x faster                                   |
| bench_thread_pool       | 947 us                                                 | 786 us: 1.20x faster                                   |
| dulwich_log             | 75.9 ms                                                | 63.1 ms: 1.20x faster                                  |
| json_loads              | 28.8 us                                                | 24.0 us: 1.20x faster                                  |
| sympy_str               | 328 ms                                                 | 273 ms: 1.20x faster                                   |
| sympy_expand            | 545 ms                                                 | 459 ms: 1.19x faster                                   |
| regex_v8                | 25.0 ms                                                | 21.2 ms: 1.18x faster                                  |
| sqlalchemy_imperative   | 21.2 ms                                                | 18.1 ms: 1.17x faster                                  |
| xml_etree_generate      | 94.2 ms                                                | 80.5 ms: 1.17x faster                                  |
| json                    | 5.42 ms                                                | 4.63 ms: 1.17x faster                                  |
| sympy_sum               | 185 ms                                                 | 159 ms: 1.16x faster                                   |
| create_gc_cycles        | 1.67 ms                                                | 1.45 ms: 1.15x faster                                  |
| mdp                     | 2.82 sec                                               | 2.47 sec: 1.14x faster                                 |
| sqlite_synth            | 2.93 us                                                | 2.59 us: 1.13x faster                                  |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                  |
| pickle_list             | 4.56 us                                                | 4.05 us: 1.13x faster                                  |
| djangocms               | 35.9 us                                                | 32.2 us: 1.12x faster                                  |
| regex_dna               | 222 ms                                                 | 199 ms: 1.11x faster                                   |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                   |
| meteor_contest          | 115 ms                                                 | 105 ms: 1.10x faster                                   |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                   |
| unpickle                | 14.1 us                                                | 13.4 us: 1.06x faster                                  |
| telco                   | 6.54 ms                                                | 6.34 ms: 1.03x faster                                  |
| pickle                  | 10.3 us                                                | 10.1 us: 1.02x faster                                  |
| async_generators        | 425 ms                                                 | 428 ms: 1.01x slower                                   |
| generators              | 76.8 ms                                                | 77.5 ms: 1.01x slower                                  |
| pidigits                | 190 ms                                                 | 193 ms: 1.01x slower                                   |
| unpickle_list           | 4.82 us                                                | 4.95 us: 1.03x slower                                  |
| gc_traversal            | 3.84 ms                                                | 4.16 ms: 1.08x slower                                  |
| regex_effbot            | 3.23 ms                                                | 3.56 ms: 1.10x slower                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.47 ms: 1.11x slower                                  |
| pickle_dict             | 27.3 us                                                | 30.8 us: 1.13x slower                                  |
| coverage                | 72.8 ms                                                | 96.8 ms: 1.33x slower                                  |
| Geometric mean          | (ref)                                                  | 1.30x faster                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, dask, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x
