
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 660f102
- commit date: 2022-10-15
- overall geometric mean: 1.32x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221015-linux-x86_64-python-main-3.12.0a1+-660f102 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 249 ms: 1.35x faster                                   |
| chameleon      | 9.06 ms                                                | 6.71 ms: 1.35x faster                                  |
| html5lib       | 85.9 ms                                                | 59.2 ms: 1.45x faster                                  |
| tornado_http   | 127 ms                                                 | 92.6 ms: 1.38x faster                                  |
| Geometric mean | (ref)                                                  | 1.38x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221015-linux-x86_64-python-main-3.12.0a1+-660f102 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 111 ms                                                 | 72.2 ms: 1.53x faster                                  |
| nbody          | 142 ms                                                 | 94.2 ms: 1.50x faster                                  |
| pidigits       | 190 ms                                                 | 199 ms: 1.05x slower                                   |
| Geometric mean | (ref)                                                  | 1.30x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221015-linux-x86_64-python-main-3.12.0a1+-660f102 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.37x faster                                   |
| regex_v8       | 25.0 ms                                                | 22.2 ms: 1.13x faster                                  |
| regex_dna      | 222 ms                                                 | 200 ms: 1.11x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.60 ms: 1.12x slower                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221015-linux-x86_64-python-main-3.12.0a1+-660f102 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 293 us: 1.55x faster                                   |
| unpickle_pure_python | 300 us                                                 | 202 us: 1.49x faster                                   |
| json_dumps           | 13.5 ms                                                | 9.60 ms: 1.41x faster                                  |
| xml_etree_process    | 74.9 ms                                                | 53.7 ms: 1.40x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 76.9 ms: 1.22x faster                                  |
| json_loads           | 28.8 us                                                | 23.9 us: 1.21x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 145 ms: 1.12x faster                                   |
| pickle_list          | 4.56 us                                                | 4.14 us: 1.10x faster                                  |
| unpickle             | 14.1 us                                                | 12.9 us: 1.09x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                   |
| unpickle_list        | 4.82 us                                                | 4.96 us: 1.03x slower                                  |
| pickle_dict          | 27.3 us                                                | 31.1 us: 1.14x slower                                  |
| Geometric mean       | (ref)                                                  | 1.18x faster                                           |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221015-linux-x86_64-python-main-3.12.0a1+-660f102 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.41 ms: 1.68x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.09 ms: 1.05x slower                                  |
| Geometric mean         | (ref)                                                  | 1.27x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221015-linux-x86_64-python-main-3.12.0a1+-660f102 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.82 ms: 1.50x faster                                  |
| genshi_text     | 30.3 ms                                                | 21.0 ms: 1.44x faster                                  |
| django_template | 45.9 ms                                                | 32.6 ms: 1.41x faster                                  |
| genshi_xml      | 63.3 ms                                                | 49.2 ms: 1.29x faster                                  |
| Geometric mean  | (ref)                                                  | 1.41x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221015-linux-x86_64-python-main-3.12.0a1+-660f102 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.31 ms: 2.24x faster                                  |
| scimark_sor             | 197 ms                                                 | 104 ms: 1.89x faster                                   |
| logging_silent          | 175 ns                                                 | 92.9 ns: 1.88x faster                                  |
| richards                | 74.9 ms                                                | 43.0 ms: 1.74x faster                                  |
| go                      | 229 ms                                                 | 134 ms: 1.71x faster                                   |
| python_startup          | 14.2 ms                                                | 8.41 ms: 1.68x faster                                  |
| pyflate                 | 673 ms                                                 | 402 ms: 1.67x faster                                   |
| scimark_monte_carlo     | 108 ms                                                 | 65.6 ms: 1.65x faster                                  |
| raytrace                | 464 ms                                                 | 285 ms: 1.63x faster                                   |
| chaos                   | 106 ms                                                 | 66.1 ms: 1.61x faster                                  |
| crypto_pyaes            | 118 ms                                                 | 75.2 ms: 1.58x faster                                  |
| hexiom                  | 9.53 ms                                                | 6.05 ms: 1.58x faster                                  |
| pickle_pure_python      | 455 us                                                 | 293 us: 1.55x faster                                   |
| spectral_norm           | 150 ms                                                 | 96.7 ms: 1.55x faster                                  |
| sqlglot_parse           | 2.06 ms                                                | 1.34 ms: 1.54x faster                                  |
| float                   | 111 ms                                                 | 72.2 ms: 1.53x faster                                  |
| scimark_lu              | 163 ms                                                 | 108 ms: 1.51x faster                                   |
| deepcopy_memo           | 52.3 us                                                | 34.6 us: 1.51x faster                                  |
| sqlglot_transpile       | 2.45 ms                                                | 1.63 ms: 1.50x faster                                  |
| mako                    | 14.8 ms                                                | 9.82 ms: 1.50x faster                                  |
| nbody                   | 142 ms                                                 | 94.2 ms: 1.50x faster                                  |
| unpickle_pure_python    | 300 us                                                 | 202 us: 1.49x faster                                   |
| unpack_sequence         | 64.7 ns                                                | 44.1 ns: 1.47x faster                                  |
| html5lib                | 85.9 ms                                                | 59.2 ms: 1.45x faster                                  |
| pprint_pformat          | 1.99 sec                                               | 1.37 sec: 1.45x faster                                 |
| genshi_text             | 30.3 ms                                                | 21.0 ms: 1.44x faster                                  |
| pprint_safe_repr        | 955 ms                                                 | 669 ms: 1.43x faster                                   |
| json_dumps              | 13.5 ms                                                | 9.60 ms: 1.41x faster                                  |
| logging_simple          | 8.07 us                                                | 5.73 us: 1.41x faster                                  |
| django_template         | 45.9 ms                                                | 32.6 ms: 1.41x faster                                  |
| logging_format          | 8.91 us                                                | 6.38 us: 1.40x faster                                  |
| xml_etree_process       | 74.9 ms                                                | 53.7 ms: 1.40x faster                                  |
| thrift                  | 1.03 ms                                                | 742 us: 1.39x faster                                   |
| aiohttp                 | 1.38 ms                                                | 997 us: 1.39x faster                                   |
| tornado_http            | 127 ms                                                 | 92.6 ms: 1.38x faster                                  |
| pycparser               | 1.50 sec                                               | 1.10 sec: 1.37x faster                                 |
| regex_compile           | 177 ms                                                 | 129 ms: 1.37x faster                                   |
| gunicorn                | 1.46 ms                                                | 1.08 ms: 1.35x faster                                  |
| 2to3                    | 336 ms                                                 | 249 ms: 1.35x faster                                   |
| chameleon               | 9.06 ms                                                | 6.71 ms: 1.35x faster                                  |
| async_tree_none         | 717 ms                                                 | 533 ms: 1.35x faster                                   |
| scimark_fft             | 424 ms                                                 | 315 ms: 1.34x faster                                   |
| async_tree_io           | 1.77 sec                                               | 1.32 sec: 1.34x faster                                 |
| deepcopy                | 442 us                                                 | 332 us: 1.33x faster                                   |
| async_tree_memoization  | 854 ms                                                 | 647 ms: 1.32x faster                                   |
| fannkuch                | 486 ms                                                 | 368 ms: 1.32x faster                                   |
| deepcopy_reduce         | 3.82 us                                                | 2.91 us: 1.32x faster                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.16 ms: 1.31x faster                                  |
| async_tree_cpu_io_mixed | 951 ms                                                 | 730 ms: 1.30x faster                                   |
| coroutines              | 31.8 ms                                                | 24.6 ms: 1.29x faster                                  |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                   |
| genshi_xml              | 63.3 ms                                                | 49.2 ms: 1.29x faster                                  |
| sqlglot_optimize        | 65.3 ms                                                | 51.5 ms: 1.27x faster                                  |
| nqueens                 | 100 ms                                                 | 79.5 ms: 1.26x faster                                  |
| dulwich_log             | 75.9 ms                                                | 60.9 ms: 1.25x faster                                  |
| xml_etree_generate      | 94.2 ms                                                | 76.9 ms: 1.22x faster                                  |
| json_loads              | 28.8 us                                                | 23.9 us: 1.21x faster                                  |
| sympy_integrate         | 24.3 ms                                                | 20.4 ms: 1.19x faster                                  |
| sympy_expand            | 545 ms                                                 | 458 ms: 1.19x faster                                   |
| sympy_str               | 328 ms                                                 | 281 ms: 1.17x faster                                   |
| pylint                  | 525 ms                                                 | 455 ms: 1.15x faster                                   |
| json                    | 5.42 ms                                                | 4.78 ms: 1.13x faster                                  |
| sympy_sum               | 185 ms                                                 | 163 ms: 1.13x faster                                   |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                  |
| regex_v8                | 25.0 ms                                                | 22.2 ms: 1.13x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 145 ms: 1.12x faster                                   |
| sqlite_synth            | 2.93 us                                                | 2.62 us: 1.12x faster                                  |
| mdp                     | 2.82 sec                                               | 2.54 sec: 1.11x faster                                 |
| meteor_contest          | 115 ms                                                 | 103 ms: 1.11x faster                                   |
| regex_dna               | 222 ms                                                 | 200 ms: 1.11x faster                                   |
| pickle_list             | 4.56 us                                                | 4.14 us: 1.10x faster                                  |
| unpickle                | 14.1 us                                                | 12.9 us: 1.09x faster                                  |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                   |
| generators              | 76.8 ms                                                | 71.8 ms: 1.07x faster                                  |
| telco                   | 6.54 ms                                                | 6.46 ms: 1.01x faster                                  |
| unpickle_list           | 4.82 us                                                | 4.96 us: 1.03x slower                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.09 ms: 1.05x slower                                  |
| pidigits                | 190 ms                                                 | 199 ms: 1.05x slower                                   |
| regex_effbot            | 3.23 ms                                                | 3.60 ms: 1.12x slower                                  |
| pickle_dict             | 27.3 us                                                | 31.1 us: 1.14x slower                                  |
| coverage                | 72.8 ms                                                | 98.4 ms: 1.35x slower                                  |
| Geometric mean          | (ref)                                                  | 1.32x faster                                           |

Benchmark hidden because not significant (1): pickle
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: async_generators, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, comprehensions, create_gc_cycles, dask, djangocms, docutils, flaskblogging, gc_traversal, mypy2, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221015-3.12.0a1+-660f102/bm-20221015-linux-x86_64-python-main-3.12.0a1+-660f102.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.27x
