
# Results vs. 3.10.4

- fork: brandtbucher
- ref: type_cache
- machine: linux-x86_64
- commit hash: 0e21f47
- commit date: 2023-03-23
- overall geometric mean: 1.29x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-0e21f47 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 253 ms: 1.33x faster                                               |
| chameleon      | 9.06 ms                                                | 6.63 ms: 1.37x faster                                              |
| docutils       | 3.17 sec                                               | 2.57 sec: 1.23x faster                                             |
| html5lib       | 85.9 ms                                                | 62.4 ms: 1.38x faster                                              |
| tornado_http   | 127 ms                                                 | 92.3 ms: 1.38x faster                                              |
| Geometric mean | (ref)                                                  | 1.33x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-0e21f47 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 86.8 ms: 1.63x faster                                              |
| float          | 111 ms                                                 | 73.7 ms: 1.50x faster                                              |
| pidigits       | 190 ms                                                 | 188 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                  | 1.35x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-0e21f47 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 134 ms: 1.32x faster                                               |
| regex_v8       | 25.0 ms                                                | 22.4 ms: 1.12x faster                                              |
| regex_dna      | 222 ms                                                 | 208 ms: 1.07x faster                                               |
| regex_effbot   | 3.23 ms                                                | 3.57 ms: 1.11x slower                                              |
| Geometric mean | (ref)                                                  | 1.09x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-0e21f47 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 292 us: 1.56x faster                                               |
| unpickle_pure_python | 300 us                                                 | 200 us: 1.50x faster                                               |
| json_dumps           | 13.5 ms                                                | 9.71 ms: 1.39x faster                                              |
| xml_etree_process    | 74.9 ms                                                | 58.0 ms: 1.29x faster                                              |
| json_loads           | 28.8 us                                                | 24.2 us: 1.19x faster                                              |
| xml_etree_generate   | 94.2 ms                                                | 82.1 ms: 1.15x faster                                              |
| xml_etree_iterparse  | 111 ms                                                 | 101 ms: 1.11x faster                                               |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                               |
| pickle_list          | 4.56 us                                                | 4.33 us: 1.05x faster                                              |
| pickle               | 10.3 us                                                | 10.4 us: 1.01x slower                                              |
| unpickle_list        | 4.82 us                                                | 5.28 us: 1.10x slower                                              |
| pickle_dict          | 27.3 us                                                | 30.7 us: 1.13x slower                                              |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                       |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-0e21f47 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.87 ms: 1.60x faster                                              |
| python_startup_no_site | 5.82 ms                                                | 6.55 ms: 1.13x slower                                              |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-0e21f47 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 10.0 ms: 1.47x faster                                              |
| genshi_text     | 30.3 ms                                                | 22.0 ms: 1.38x faster                                              |
| django_template | 45.9 ms                                                | 34.0 ms: 1.35x faster                                              |
| genshi_xml      | 63.3 ms                                                | 48.9 ms: 1.29x faster                                              |
| Geometric mean  | (ref)                                                  | 1.37x faster                                                       |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-0e21f47 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 29.3 ms: 2.62x faster                                              |
| deltablue               | 7.42 ms                                                | 3.32 ms: 2.24x faster                                              |
| logging_silent          | 175 ns                                                 | 96.1 ns: 1.82x faster                                              |
| scimark_sor             | 197 ms                                                 | 108 ms: 1.82x faster                                               |
| asyncio_tcp             | 925 ms                                                 | 509 ms: 1.82x faster                                               |
| richards                | 74.9 ms                                                | 43.9 ms: 1.71x faster                                              |
| go                      | 229 ms                                                 | 137 ms: 1.67x faster                                               |
| nbody                   | 142 ms                                                 | 86.8 ms: 1.63x faster                                              |
| scimark_monte_carlo     | 108 ms                                                 | 66.7 ms: 1.62x faster                                              |
| crypto_pyaes            | 118 ms                                                 | 73.7 ms: 1.61x faster                                              |
| spectral_norm           | 150 ms                                                 | 93.6 ms: 1.60x faster                                              |
| python_startup          | 14.2 ms                                                | 8.87 ms: 1.60x faster                                              |
| raytrace                | 464 ms                                                 | 293 ms: 1.58x faster                                               |
| chaos                   | 106 ms                                                 | 67.3 ms: 1.58x faster                                              |
| pickle_pure_python      | 455 us                                                 | 292 us: 1.56x faster                                               |
| hexiom                  | 9.53 ms                                                | 6.11 ms: 1.56x faster                                              |
| pyflate                 | 673 ms                                                 | 434 ms: 1.55x faster                                               |
| deepcopy_memo           | 52.3 us                                                | 34.4 us: 1.52x faster                                              |
| scimark_lu              | 163 ms                                                 | 108 ms: 1.52x faster                                               |
| unpickle_pure_python    | 300 us                                                 | 200 us: 1.50x faster                                               |
| float                   | 111 ms                                                 | 73.7 ms: 1.50x faster                                              |
| mako                    | 14.8 ms                                                | 10.0 ms: 1.47x faster                                              |
| unpack_sequence         | 64.7 ns                                                | 44.7 ns: 1.45x faster                                              |
| sqlglot_parse           | 2.06 ms                                                | 1.46 ms: 1.41x faster                                              |
| coroutines              | 31.8 ms                                                | 22.7 ms: 1.40x faster                                              |
| sqlglot_transpile       | 2.45 ms                                                | 1.75 ms: 1.39x faster                                              |
| json_dumps              | 13.5 ms                                                | 9.71 ms: 1.39x faster                                              |
| pprint_pformat          | 1.99 sec                                               | 1.43 sec: 1.39x faster                                             |
| scimark_fft             | 424 ms                                                 | 306 ms: 1.38x faster                                               |
| tornado_http            | 127 ms                                                 | 92.3 ms: 1.38x faster                                              |
| genshi_text             | 30.3 ms                                                | 22.0 ms: 1.38x faster                                              |
| logging_format          | 8.91 us                                                | 6.47 us: 1.38x faster                                              |
| html5lib                | 85.9 ms                                                | 62.4 ms: 1.38x faster                                              |
| pprint_safe_repr        | 955 ms                                                 | 698 ms: 1.37x faster                                               |
| chameleon               | 9.06 ms                                                | 6.63 ms: 1.37x faster                                              |
| logging_simple          | 8.07 us                                                | 5.95 us: 1.36x faster                                              |
| django_template         | 45.9 ms                                                | 34.0 ms: 1.35x faster                                              |
| async_tree_io           | 1.77 sec                                               | 1.32 sec: 1.35x faster                                             |
| async_tree_none         | 717 ms                                                 | 535 ms: 1.34x faster                                               |
| deepcopy                | 442 us                                                 | 331 us: 1.33x faster                                               |
| 2to3                    | 336 ms                                                 | 253 ms: 1.33x faster                                               |
| regex_compile           | 177 ms                                                 | 134 ms: 1.32x faster                                               |
| genshi_xml              | 63.3 ms                                                | 48.9 ms: 1.29x faster                                              |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.21 ms: 1.29x faster                                              |
| xml_etree_process       | 74.9 ms                                                | 58.0 ms: 1.29x faster                                              |
| thrift                  | 1.03 ms                                                | 804 us: 1.28x faster                                               |
| pycparser               | 1.50 sec                                               | 1.18 sec: 1.27x faster                                             |
| mypy2                   | 428 ms                                                 | 337 ms: 1.27x faster                                               |
| async_tree_cpu_io_mixed | 951 ms                                                 | 750 ms: 1.27x faster                                               |
| async_tree_memoization  | 854 ms                                                 | 676 ms: 1.26x faster                                               |
| fannkuch                | 486 ms                                                 | 387 ms: 1.25x faster                                               |
| deepcopy_reduce         | 3.82 us                                                | 3.05 us: 1.25x faster                                              |
| sqlglot_optimize        | 65.3 ms                                                | 52.2 ms: 1.25x faster                                              |
| sqlglot_normalize       | 135 ms                                                 | 108 ms: 1.25x faster                                               |
| docutils                | 3.17 sec                                               | 2.57 sec: 1.23x faster                                             |
| nqueens                 | 100 ms                                                 | 81.2 ms: 1.23x faster                                              |
| json_loads              | 28.8 us                                                | 24.2 us: 1.19x faster                                              |
| bench_thread_pool       | 947 us                                                 | 799 us: 1.19x faster                                               |
| sympy_integrate         | 24.3 ms                                                | 20.6 ms: 1.18x faster                                              |
| dulwich_log             | 75.9 ms                                                | 64.6 ms: 1.18x faster                                              |
| sympy_expand            | 545 ms                                                 | 468 ms: 1.16x faster                                               |
| json                    | 5.42 ms                                                | 4.68 ms: 1.16x faster                                              |
| xml_etree_generate      | 94.2 ms                                                | 82.1 ms: 1.15x faster                                              |
| sympy_str               | 328 ms                                                 | 287 ms: 1.14x faster                                               |
| create_gc_cycles        | 1.67 ms                                                | 1.48 ms: 1.13x faster                                              |
| sqlite_synth            | 2.93 us                                                | 2.62 us: 1.12x faster                                              |
| regex_v8                | 25.0 ms                                                | 22.4 ms: 1.12x faster                                              |
| xml_etree_iterparse     | 111 ms                                                 | 101 ms: 1.11x faster                                               |
| comprehensions          | 26.8 us                                                | 24.2 us: 1.11x faster                                              |
| sympy_sum               | 185 ms                                                 | 167 ms: 1.10x faster                                               |
| pathlib                 | 20.0 ms                                                | 18.2 ms: 1.10x faster                                              |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                               |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.10x faster                                               |
| mdp                     | 2.82 sec                                               | 2.64 sec: 1.07x faster                                             |
| regex_dna               | 222 ms                                                 | 208 ms: 1.07x faster                                               |
| pickle_list             | 4.56 us                                                | 4.33 us: 1.05x faster                                              |
| telco                   | 6.54 ms                                                | 6.40 ms: 1.02x faster                                              |
| async_generators        | 425 ms                                                 | 416 ms: 1.02x faster                                               |
| pidigits                | 190 ms                                                 | 188 ms: 1.01x faster                                               |
| pickle                  | 10.3 us                                                | 10.4 us: 1.01x slower                                              |
| gc_traversal            | 3.84 ms                                                | 4.06 ms: 1.06x slower                                              |
| unpickle_list           | 4.82 us                                                | 5.28 us: 1.10x slower                                              |
| regex_effbot            | 3.23 ms                                                | 3.57 ms: 1.11x slower                                              |
| python_startup_no_site  | 5.82 ms                                                | 6.55 ms: 1.13x slower                                              |
| pickle_dict             | 27.3 us                                                | 30.7 us: 1.13x slower                                              |
| dask                    | 423 ms                                                 | 515 ms: 1.22x slower                                               |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                       |

Benchmark hidden because not significant (2): unpickle, bench_mp_pool
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, coverage, djangocms, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.24x
