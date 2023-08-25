
# Results vs. 3.10.4

- fork: itamaro
- ref: defer_task_name_form
- machine: linux-x86_64
- commit hash: db3b8a6
- commit date: 2023-04-24
- overall geometric mean: 1.24x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230424-linux-x86_64-itamaro-defer_task_name_form-3.12.0a7+-db3b8a6 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 267 ms: 1.26x faster                                                    |
| chameleon      | 9.06 ms                                                | 6.82 ms: 1.33x faster                                                   |
| docutils       | 3.17 sec                                               | 2.69 sec: 1.18x faster                                                  |
| html5lib       | 85.9 ms                                                | 65.1 ms: 1.32x faster                                                   |
| tornado_http   | 127 ms                                                 | 104 ms: 1.23x faster                                                    |
| Geometric mean | (ref)                                                  | 1.26x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230424-linux-x86_64-itamaro-defer_task_name_form-3.12.0a7+-db3b8a6 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 89.0 ms: 1.59x faster                                                   |
| float          | 111 ms                                                 | 80.0 ms: 1.38x faster                                                   |
| pidigits       | 190 ms                                                 | 189 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                  | 1.30x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230424-linux-x86_64-itamaro-defer_task_name_form-3.12.0a7+-db3b8a6 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 142 ms: 1.24x faster                                                    |
| regex_v8       | 25.0 ms                                                | 22.0 ms: 1.14x faster                                                   |
| regex_dna      | 222 ms                                                 | 203 ms: 1.09x faster                                                    |
| regex_effbot   | 3.23 ms                                                | 3.66 ms: 1.13x slower                                                   |
| Geometric mean | (ref)                                                  | 1.08x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230424-linux-x86_64-itamaro-defer_task_name_form-3.12.0a7+-db3b8a6 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 313 us: 1.45x faster                                                    |
| json_dumps           | 13.5 ms                                                | 9.68 ms: 1.40x faster                                                   |
| unpickle_pure_python | 300 us                                                 | 218 us: 1.38x faster                                                    |
| xml_etree_process    | 74.9 ms                                                | 57.9 ms: 1.29x faster                                                   |
| json_loads           | 28.8 us                                                | 24.8 us: 1.16x faster                                                   |
| xml_etree_generate   | 94.2 ms                                                | 82.5 ms: 1.14x faster                                                   |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                                    |
| xml_etree_parse      | 163 ms                                                 | 152 ms: 1.07x faster                                                    |
| pickle_list          | 4.56 us                                                | 4.41 us: 1.03x faster                                                   |
| pickle               | 10.3 us                                                | 10.7 us: 1.04x slower                                                   |
| unpickle_list        | 4.82 us                                                | 5.11 us: 1.06x slower                                                   |
| pickle_dict          | 27.3 us                                                | 31.6 us: 1.16x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                            |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230424-linux-x86_64-itamaro-defer_task_name_form-3.12.0a7+-db3b8a6 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.99 ms: 1.57x faster                                                   |
| python_startup_no_site | 5.82 ms                                                | 6.60 ms: 1.13x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230424-linux-x86_64-itamaro-defer_task_name_form-3.12.0a7+-db3b8a6 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 10.8 ms: 1.37x faster                                                   |
| django_template | 45.9 ms                                                | 34.3 ms: 1.34x faster                                                   |
| genshi_text     | 30.3 ms                                                | 23.0 ms: 1.32x faster                                                   |
| genshi_xml      | 63.3 ms                                                | 50.5 ms: 1.25x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                            |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230424-linux-x86_64-itamaro-defer_task_name_form-3.12.0a7+-db3b8a6 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 32.2 ms: 2.38x faster                                                   |
| deltablue               | 7.42 ms                                                | 3.64 ms: 2.04x faster                                                   |
| asyncio_tcp             | 925 ms                                                 | 512 ms: 1.81x faster                                                    |
| logging_silent          | 175 ns                                                 | 98.8 ns: 1.77x faster                                                   |
| richards                | 74.9 ms                                                | 43.2 ms: 1.73x faster                                                   |
| go                      | 229 ms                                                 | 136 ms: 1.68x faster                                                    |
| scimark_sor             | 197 ms                                                 | 122 ms: 1.62x faster                                                    |
| nbody                   | 142 ms                                                 | 89.0 ms: 1.59x faster                                                   |
| python_startup          | 14.2 ms                                                | 8.99 ms: 1.57x faster                                                   |
| sqlglot_parse           | 2.06 ms                                                | 1.32 ms: 1.56x faster                                                   |
| chaos                   | 106 ms                                                 | 68.5 ms: 1.55x faster                                                   |
| raytrace                | 464 ms                                                 | 301 ms: 1.54x faster                                                    |
| crypto_pyaes            | 118 ms                                                 | 76.9 ms: 1.54x faster                                                   |
| scimark_monte_carlo     | 108 ms                                                 | 71.0 ms: 1.52x faster                                                   |
| hexiom                  | 9.53 ms                                                | 6.36 ms: 1.50x faster                                                   |
| sqlglot_transpile       | 2.45 ms                                                | 1.65 ms: 1.48x faster                                                   |
| scimark_lu              | 163 ms                                                 | 111 ms: 1.47x faster                                                    |
| pyflate                 | 673 ms                                                 | 459 ms: 1.47x faster                                                    |
| pickle_pure_python      | 455 us                                                 | 313 us: 1.45x faster                                                    |
| coroutines              | 31.8 ms                                                | 22.0 ms: 1.44x faster                                                   |
| spectral_norm           | 150 ms                                                 | 104 ms: 1.44x faster                                                    |
| async_tree_none         | 717 ms                                                 | 500 ms: 1.43x faster                                                    |
| async_tree_io           | 1.77 sec                                               | 1.25 sec: 1.42x faster                                                  |
| json_dumps              | 13.5 ms                                                | 9.68 ms: 1.40x faster                                                   |
| float                   | 111 ms                                                 | 80.0 ms: 1.38x faster                                                   |
| async_tree_memoization  | 854 ms                                                 | 621 ms: 1.38x faster                                                    |
| unpickle_pure_python    | 300 us                                                 | 218 us: 1.38x faster                                                    |
| mako                    | 14.8 ms                                                | 10.8 ms: 1.37x faster                                                   |
| deepcopy_memo           | 52.3 us                                                | 39.0 us: 1.34x faster                                                   |
| django_template         | 45.9 ms                                                | 34.3 ms: 1.34x faster                                                   |
| pprint_pformat          | 1.99 sec                                               | 1.48 sec: 1.34x faster                                                  |
| chameleon               | 9.06 ms                                                | 6.82 ms: 1.33x faster                                                   |
| pycparser               | 1.50 sec                                               | 1.13 sec: 1.33x faster                                                  |
| async_tree_cpu_io_mixed | 951 ms                                                 | 718 ms: 1.32x faster                                                    |
| genshi_text             | 30.3 ms                                                | 23.0 ms: 1.32x faster                                                   |
| html5lib                | 85.9 ms                                                | 65.1 ms: 1.32x faster                                                   |
| pprint_safe_repr        | 955 ms                                                 | 724 ms: 1.32x faster                                                    |
| unpack_sequence         | 64.7 ns                                                | 49.5 ns: 1.31x faster                                                   |
| thrift                  | 1.03 ms                                                | 795 us: 1.30x faster                                                    |
| logging_format          | 8.91 us                                                | 6.87 us: 1.30x faster                                                   |
| logging_simple          | 8.07 us                                                | 6.23 us: 1.29x faster                                                   |
| xml_etree_process       | 74.9 ms                                                | 57.9 ms: 1.29x faster                                                   |
| fannkuch                | 486 ms                                                 | 383 ms: 1.27x faster                                                    |
| 2to3                    | 336 ms                                                 | 267 ms: 1.26x faster                                                    |
| genshi_xml              | 63.3 ms                                                | 50.5 ms: 1.25x faster                                                   |
| regex_compile           | 177 ms                                                 | 142 ms: 1.24x faster                                                    |
| tornado_http            | 127 ms                                                 | 104 ms: 1.23x faster                                                    |
| deepcopy                | 442 us                                                 | 360 us: 1.23x faster                                                    |
| sqlglot_normalize       | 135 ms                                                 | 111 ms: 1.22x faster                                                    |
| nqueens                 | 100 ms                                                 | 82.0 ms: 1.22x faster                                                   |
| scimark_fft             | 424 ms                                                 | 348 ms: 1.22x faster                                                    |
| deepcopy_reduce         | 3.82 us                                                | 3.18 us: 1.20x faster                                                   |
| sqlglot_optimize        | 65.3 ms                                                | 54.7 ms: 1.19x faster                                                   |
| mypy2                   | 428 ms                                                 | 359 ms: 1.19x faster                                                    |
| docutils                | 3.17 sec                                               | 2.69 sec: 1.18x faster                                                  |
| json_loads              | 28.8 us                                                | 24.8 us: 1.16x faster                                                   |
| comprehensions          | 26.8 us                                                | 23.4 us: 1.15x faster                                                   |
| xml_etree_generate      | 94.2 ms                                                | 82.5 ms: 1.14x faster                                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.78 ms: 1.14x faster                                                   |
| regex_v8                | 25.0 ms                                                | 22.0 ms: 1.14x faster                                                   |
| json                    | 5.42 ms                                                | 4.75 ms: 1.14x faster                                                   |
| create_gc_cycles        | 1.67 ms                                                | 1.47 ms: 1.14x faster                                                   |
| bench_thread_pool       | 947 us                                                 | 835 us: 1.13x faster                                                    |
| sqlalchemy_declarative  | 165 ms                                                 | 147 ms: 1.13x faster                                                    |
| pylint                  | 525 ms                                                 | 467 ms: 1.12x faster                                                    |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                                   |
| dulwich_log             | 75.9 ms                                                | 68.0 ms: 1.12x faster                                                   |
| sympy_integrate         | 24.3 ms                                                | 21.9 ms: 1.11x faster                                                   |
| sqlite_synth            | 2.93 us                                                | 2.67 us: 1.10x faster                                                   |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                                    |
| regex_dna               | 222 ms                                                 | 203 ms: 1.09x faster                                                    |
| sympy_expand            | 545 ms                                                 | 500 ms: 1.09x faster                                                    |
| mdp                     | 2.82 sec                                               | 2.59 sec: 1.09x faster                                                  |
| sqlalchemy_imperative   | 21.2 ms                                                | 19.5 ms: 1.08x faster                                                   |
| djangocms               | 35.9 us                                                | 33.2 us: 1.08x faster                                                   |
| xml_etree_parse         | 163 ms                                                 | 152 ms: 1.07x faster                                                    |
| sympy_str               | 328 ms                                                 | 310 ms: 1.06x faster                                                    |
| pickle_list             | 4.56 us                                                | 4.41 us: 1.03x faster                                                   |
| sympy_sum               | 185 ms                                                 | 180 ms: 1.03x faster                                                    |
| meteor_contest          | 115 ms                                                 | 114 ms: 1.01x faster                                                    |
| pidigits                | 190 ms                                                 | 189 ms: 1.01x faster                                                    |
| bench_mp_pool           | 24.0 ms                                                | 24.0 ms: 1.00x slower                                                   |
| telco                   | 6.54 ms                                                | 6.64 ms: 1.01x slower                                                   |
| async_generators        | 425 ms                                                 | 440 ms: 1.03x slower                                                    |
| pickle                  | 10.3 us                                                | 10.7 us: 1.04x slower                                                   |
| gc_traversal            | 3.84 ms                                                | 4.08 ms: 1.06x slower                                                   |
| unpickle_list           | 4.82 us                                                | 5.11 us: 1.06x slower                                                   |
| python_startup_no_site  | 5.82 ms                                                | 6.60 ms: 1.13x slower                                                   |
| regex_effbot            | 3.23 ms                                                | 3.66 ms: 1.13x slower                                                   |
| pickle_dict             | 27.3 us                                                | 31.6 us: 1.16x slower                                                   |
| dask                    | 423 ms                                                 | 538 ms: 1.27x slower                                                    |
| coverage                | 72.8 ms                                                | 99.8 ms: 1.37x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.24x faster                                                            |

Benchmark hidden because not significant (1): unpickle
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x
