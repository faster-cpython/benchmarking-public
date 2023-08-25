
# Results vs. 3.10.4

- fork: faster-cpython
- ref: restrict_for_iter_sp
- machine: linux-x86_64
- commit hash: fb5f321
- commit date: 2023-02-17
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230217-linux-x86_64-faster%2dcpython-restrict_for_iter_sp-3.12.0a5+-fb5f321 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 247 ms: 1.36x faster                                                             |
| chameleon      | 9.06 ms                                                | 6.39 ms: 1.42x faster                                                            |
| docutils       | 3.17 sec                                               | 2.53 sec: 1.25x faster                                                           |
| html5lib       | 85.9 ms                                                | 61.2 ms: 1.40x faster                                                            |
| tornado_http   | 127 ms                                                 | 94.8 ms: 1.34x faster                                                            |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230217-linux-x86_64-faster%2dcpython-restrict_for_iter_sp-3.12.0a5+-fb5f321 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 111 ms                                                 | 73.7 ms: 1.50x faster                                                            |
| nbody          | 142 ms                                                 | 95.5 ms: 1.48x faster                                                            |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                                             |
| Geometric mean | (ref)                                                  | 1.29x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230217-linux-x86_64-faster%2dcpython-restrict_for_iter_sp-3.12.0a5+-fb5f321 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 132 ms: 1.34x faster                                                             |
| regex_v8       | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                            |
| regex_dna      | 222 ms                                                 | 199 ms: 1.12x faster                                                             |
| regex_effbot   | 3.23 ms                                                | 3.65 ms: 1.13x slower                                                            |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230217-linux-x86_64-faster%2dcpython-restrict_for_iter_sp-3.12.0a5+-fb5f321 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 281 us: 1.62x faster                                                             |
| unpickle_pure_python | 300 us                                                 | 197 us: 1.53x faster                                                             |
| json_dumps           | 13.5 ms                                                | 9.50 ms: 1.42x faster                                                            |
| xml_etree_process    | 74.9 ms                                                | 55.7 ms: 1.35x faster                                                            |
| json_loads           | 28.8 us                                                | 24.0 us: 1.20x faster                                                            |
| xml_etree_generate   | 94.2 ms                                                | 81.2 ms: 1.16x faster                                                            |
| pickle_list          | 4.56 us                                                | 4.01 us: 1.14x faster                                                            |
| xml_etree_iterparse  | 111 ms                                                 | 99.7 ms: 1.12x faster                                                            |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                             |
| pickle               | 10.3 us                                                | 9.98 us: 1.03x faster                                                            |
| unpickle_list        | 4.82 us                                                | 5.04 us: 1.05x slower                                                            |
| pickle_dict          | 27.3 us                                                | 30.2 us: 1.11x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                                     |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230217-linux-x86_64-faster%2dcpython-restrict_for_iter_sp-3.12.0a5+-fb5f321 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.92 ms: 1.59x faster                                                            |
| python_startup_no_site | 5.82 ms                                                | 6.47 ms: 1.11x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.20x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230217-linux-x86_64-faster%2dcpython-restrict_for_iter_sp-3.12.0a5+-fb5f321 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.89 ms: 1.49x faster                                                            |
| genshi_text     | 30.3 ms                                                | 21.2 ms: 1.43x faster                                                            |
| django_template | 45.9 ms                                                | 33.0 ms: 1.39x faster                                                            |
| genshi_xml      | 63.3 ms                                                | 48.4 ms: 1.31x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                                     |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230217-linux-x86_64-faster%2dcpython-restrict_for_iter_sp-3.12.0a5+-fb5f321 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 30.6 ms: 2.51x faster                                                            |
| deltablue               | 7.42 ms                                                | 3.19 ms: 2.33x faster                                                            |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.84x faster                                                             |
| asyncio_tcp             | 925 ms                                                 | 504 ms: 1.84x faster                                                             |
| logging_silent          | 175 ns                                                 | 95.7 ns: 1.83x faster                                                            |
| richards                | 74.9 ms                                                | 42.2 ms: 1.77x faster                                                            |
| go                      | 229 ms                                                 | 134 ms: 1.71x faster                                                             |
| pyflate                 | 673 ms                                                 | 402 ms: 1.68x faster                                                             |
| pickle_pure_python      | 455 us                                                 | 281 us: 1.62x faster                                                             |
| scimark_monte_carlo     | 108 ms                                                 | 67.1 ms: 1.61x faster                                                            |
| raytrace                | 464 ms                                                 | 290 ms: 1.60x faster                                                             |
| crypto_pyaes            | 118 ms                                                 | 74.2 ms: 1.60x faster                                                            |
| spectral_norm           | 150 ms                                                 | 94.1 ms: 1.59x faster                                                            |
| python_startup          | 14.2 ms                                                | 8.92 ms: 1.59x faster                                                            |
| chaos                   | 106 ms                                                 | 68.0 ms: 1.56x faster                                                            |
| unpack_sequence         | 64.7 ns                                                | 41.9 ns: 1.55x faster                                                            |
| unpickle_pure_python    | 300 us                                                 | 197 us: 1.53x faster                                                             |
| hexiom                  | 9.53 ms                                                | 6.27 ms: 1.52x faster                                                            |
| deepcopy_memo           | 52.3 us                                                | 34.6 us: 1.51x faster                                                            |
| float                   | 111 ms                                                 | 73.7 ms: 1.50x faster                                                            |
| mako                    | 14.8 ms                                                | 9.89 ms: 1.49x faster                                                            |
| scimark_lu              | 163 ms                                                 | 110 ms: 1.49x faster                                                             |
| nbody                   | 142 ms                                                 | 95.5 ms: 1.48x faster                                                            |
| coroutines              | 31.8 ms                                                | 22.1 ms: 1.44x faster                                                            |
| genshi_text             | 30.3 ms                                                | 21.2 ms: 1.43x faster                                                            |
| sqlglot_parse           | 2.06 ms                                                | 1.44 ms: 1.43x faster                                                            |
| json_dumps              | 13.5 ms                                                | 9.50 ms: 1.42x faster                                                            |
| chameleon               | 9.06 ms                                                | 6.39 ms: 1.42x faster                                                            |
| sqlglot_transpile       | 2.45 ms                                                | 1.73 ms: 1.41x faster                                                            |
| pprint_pformat          | 1.99 sec                                               | 1.41 sec: 1.41x faster                                                           |
| logging_simple          | 8.07 us                                                | 5.74 us: 1.41x faster                                                            |
| pprint_safe_repr        | 955 ms                                                 | 680 ms: 1.40x faster                                                             |
| html5lib                | 85.9 ms                                                | 61.2 ms: 1.40x faster                                                            |
| logging_format          | 8.91 us                                                | 6.37 us: 1.40x faster                                                            |
| django_template         | 45.9 ms                                                | 33.0 ms: 1.39x faster                                                            |
| pycparser               | 1.50 sec                                               | 1.10 sec: 1.37x faster                                                           |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                                            |
| 2to3                    | 336 ms                                                 | 247 ms: 1.36x faster                                                             |
| async_tree_none         | 717 ms                                                 | 529 ms: 1.35x faster                                                             |
| scimark_fft             | 424 ms                                                 | 314 ms: 1.35x faster                                                             |
| async_tree_io           | 1.77 sec                                               | 1.32 sec: 1.35x faster                                                           |
| xml_etree_process       | 74.9 ms                                                | 55.7 ms: 1.35x faster                                                            |
| thrift                  | 1.03 ms                                                | 769 us: 1.34x faster                                                             |
| tornado_http            | 127 ms                                                 | 94.8 ms: 1.34x faster                                                            |
| fannkuch                | 486 ms                                                 | 362 ms: 1.34x faster                                                             |
| regex_compile           | 177 ms                                                 | 132 ms: 1.34x faster                                                             |
| gunicorn                | 1.46 ms                                                | 1.10 ms: 1.33x faster                                                            |
| deepcopy                | 442 us                                                 | 333 us: 1.33x faster                                                             |
| genshi_xml              | 63.3 ms                                                | 48.4 ms: 1.31x faster                                                            |
| deepcopy_reduce         | 3.82 us                                                | 2.94 us: 1.30x faster                                                            |
| mypy2                   | 428 ms                                                 | 331 ms: 1.29x faster                                                             |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                                             |
| sqlglot_optimize        | 65.3 ms                                                | 51.1 ms: 1.28x faster                                                            |
| async_tree_cpu_io_mixed | 951 ms                                                 | 752 ms: 1.26x faster                                                             |
| async_tree_memoization  | 854 ms                                                 | 677 ms: 1.26x faster                                                             |
| docutils                | 3.17 sec                                               | 2.53 sec: 1.25x faster                                                           |
| nqueens                 | 100 ms                                                 | 81.7 ms: 1.22x faster                                                            |
| sympy_integrate         | 24.3 ms                                                | 20.0 ms: 1.21x faster                                                            |
| dulwich_log             | 75.9 ms                                                | 62.8 ms: 1.21x faster                                                            |
| sqlalchemy_declarative  | 165 ms                                                 | 137 ms: 1.21x faster                                                             |
| sympy_str               | 328 ms                                                 | 273 ms: 1.20x faster                                                             |
| json_loads              | 28.8 us                                                | 24.0 us: 1.20x faster                                                            |
| bench_thread_pool       | 947 us                                                 | 791 us: 1.20x faster                                                             |
| sympy_expand            | 545 ms                                                 | 455 ms: 1.20x faster                                                             |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.60 ms: 1.19x faster                                                            |
| sqlalchemy_imperative   | 21.2 ms                                                | 18.0 ms: 1.18x faster                                                            |
| json                    | 5.42 ms                                                | 4.60 ms: 1.18x faster                                                            |
| xml_etree_generate      | 94.2 ms                                                | 81.2 ms: 1.16x faster                                                            |
| sympy_sum               | 185 ms                                                 | 159 ms: 1.16x faster                                                             |
| regex_v8                | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                            |
| pickle_list             | 4.56 us                                                | 4.01 us: 1.14x faster                                                            |
| create_gc_cycles        | 1.67 ms                                                | 1.48 ms: 1.13x faster                                                            |
| xml_etree_iterparse     | 111 ms                                                 | 99.7 ms: 1.12x faster                                                            |
| regex_dna               | 222 ms                                                 | 199 ms: 1.12x faster                                                             |
| meteor_contest          | 115 ms                                                 | 103 ms: 1.11x faster                                                             |
| djangocms               | 35.9 us                                                | 32.4 us: 1.11x faster                                                            |
| sqlite_synth            | 2.93 us                                                | 2.66 us: 1.10x faster                                                            |
| pathlib                 | 20.0 ms                                                | 18.1 ms: 1.10x faster                                                            |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                             |
| gc_traversal            | 3.84 ms                                                | 3.53 ms: 1.09x faster                                                            |
| mdp                     | 2.82 sec                                               | 2.66 sec: 1.06x faster                                                           |
| async_generators        | 425 ms                                                 | 410 ms: 1.04x faster                                                             |
| pickle                  | 10.3 us                                                | 9.98 us: 1.03x faster                                                            |
| bench_mp_pool           | 24.0 ms                                                | 24.0 ms: 1.00x slower                                                            |
| pidigits                | 190 ms                                                 | 198 ms: 1.04x slower                                                             |
| unpickle_list           | 4.82 us                                                | 5.04 us: 1.05x slower                                                            |
| pickle_dict             | 27.3 us                                                | 30.2 us: 1.11x slower                                                            |
| python_startup_no_site  | 5.82 ms                                                | 6.47 ms: 1.11x slower                                                            |
| regex_effbot            | 3.23 ms                                                | 3.65 ms: 1.13x slower                                                            |
| dask                    | 423 ms                                                 | 502 ms: 1.19x slower                                                             |
| coverage                | 72.8 ms                                                | 97.9 ms: 1.35x slower                                                            |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                                     |

Benchmark hidden because not significant (2): unpickle, telco
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.25x
