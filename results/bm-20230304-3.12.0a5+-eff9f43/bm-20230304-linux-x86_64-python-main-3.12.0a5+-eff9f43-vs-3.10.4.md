
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: eff9f43
- commit date: 2023-03-04
- overall geometric mean: 1.29x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230304-linux-x86_64-python-main-3.12.0a5+-eff9f43 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 250 ms: 1.34x faster                                   |
| chameleon      | 9.06 ms                                                | 6.42 ms: 1.41x faster                                  |
| docutils       | 3.17 sec                                               | 2.56 sec: 1.24x faster                                 |
| html5lib       | 85.9 ms                                                | 61.4 ms: 1.40x faster                                  |
| tornado_http   | 127 ms                                                 | 94.9 ms: 1.34x faster                                  |
| Geometric mean | (ref)                                                  | 1.35x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230304-linux-x86_64-python-main-3.12.0a5+-eff9f43 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 142 ms                                                 | 94.0 ms: 1.51x faster                                  |
| float          | 111 ms                                                 | 74.6 ms: 1.48x faster                                  |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.31x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230304-linux-x86_64-python-main-3.12.0a5+-eff9f43 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 133 ms: 1.33x faster                                   |
| regex_v8       | 25.0 ms                                                | 21.8 ms: 1.15x faster                                  |
| regex_dna      | 222 ms                                                 | 209 ms: 1.06x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.40 ms: 1.05x slower                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230304-linux-x86_64-python-main-3.12.0a5+-eff9f43 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 291 us: 1.56x faster                                   |
| unpickle_pure_python | 300 us                                                 | 199 us: 1.51x faster                                   |
| json_dumps           | 13.5 ms                                                | 9.56 ms: 1.42x faster                                  |
| xml_etree_process    | 74.9 ms                                                | 55.4 ms: 1.35x faster                                  |
| json_loads           | 28.8 us                                                | 23.9 us: 1.21x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 81.3 ms: 1.16x faster                                  |
| pickle_list          | 4.56 us                                                | 4.05 us: 1.13x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                   |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                   |
| unpickle             | 14.1 us                                                | 13.7 us: 1.03x faster                                  |
| pickle               | 10.3 us                                                | 10.2 us: 1.01x faster                                  |
| unpickle_list        | 4.82 us                                                | 5.22 us: 1.08x slower                                  |
| pickle_dict          | 27.3 us                                                | 31.5 us: 1.15x slower                                  |
| Geometric mean       | (ref)                                                  | 1.16x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230304-linux-x86_64-python-main-3.12.0a5+-eff9f43 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.03 ms: 1.57x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.55 ms: 1.13x slower                                  |
| Geometric mean         | (ref)                                                  | 1.18x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230304-linux-x86_64-python-main-3.12.0a5+-eff9f43 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.8 ms                                                | 10.1 ms: 1.46x faster                                  |
| genshi_text     | 30.3 ms                                                | 21.2 ms: 1.43x faster                                  |
| django_template | 45.9 ms                                                | 33.2 ms: 1.38x faster                                  |
| genshi_xml      | 63.3 ms                                                | 48.6 ms: 1.30x faster                                  |
| Geometric mean  | (ref)                                                  | 1.39x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230304-linux-x86_64-python-main-3.12.0a5+-eff9f43 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| generators              | 76.8 ms                                                | 30.6 ms: 2.51x faster                                  |
| deltablue               | 7.42 ms                                                | 3.20 ms: 2.32x faster                                  |
| logging_silent          | 175 ns                                                 | 93.2 ns: 1.88x faster                                  |
| asyncio_tcp             | 925 ms                                                 | 508 ms: 1.82x faster                                   |
| scimark_sor             | 197 ms                                                 | 109 ms: 1.81x faster                                   |
| richards                | 74.9 ms                                                | 42.6 ms: 1.76x faster                                  |
| go                      | 229 ms                                                 | 133 ms: 1.72x faster                                   |
| scimark_monte_carlo     | 108 ms                                                 | 68.0 ms: 1.59x faster                                  |
| pyflate                 | 673 ms                                                 | 424 ms: 1.59x faster                                   |
| crypto_pyaes            | 118 ms                                                 | 75.2 ms: 1.57x faster                                  |
| python_startup          | 14.2 ms                                                | 9.03 ms: 1.57x faster                                  |
| pickle_pure_python      | 455 us                                                 | 291 us: 1.56x faster                                   |
| chaos                   | 106 ms                                                 | 68.1 ms: 1.56x faster                                  |
| raytrace                | 464 ms                                                 | 298 ms: 1.56x faster                                   |
| spectral_norm           | 150 ms                                                 | 97.3 ms: 1.54x faster                                  |
| hexiom                  | 9.53 ms                                                | 6.18 ms: 1.54x faster                                  |
| deepcopy_memo           | 52.3 us                                                | 34.4 us: 1.52x faster                                  |
| unpickle_pure_python    | 300 us                                                 | 199 us: 1.51x faster                                   |
| nbody                   | 142 ms                                                 | 94.0 ms: 1.51x faster                                  |
| unpack_sequence         | 64.7 ns                                                | 43.2 ns: 1.50x faster                                  |
| float                   | 111 ms                                                 | 74.6 ms: 1.48x faster                                  |
| mako                    | 14.8 ms                                                | 10.1 ms: 1.46x faster                                  |
| scimark_lu              | 163 ms                                                 | 112 ms: 1.45x faster                                   |
| genshi_text             | 30.3 ms                                                | 21.2 ms: 1.43x faster                                  |
| sqlglot_parse           | 2.06 ms                                                | 1.45 ms: 1.42x faster                                  |
| json_dumps              | 13.5 ms                                                | 9.56 ms: 1.42x faster                                  |
| pprint_pformat          | 1.99 sec                                               | 1.41 sec: 1.41x faster                                 |
| chameleon               | 9.06 ms                                                | 6.42 ms: 1.41x faster                                  |
| sqlglot_transpile       | 2.45 ms                                                | 1.74 ms: 1.41x faster                                  |
| html5lib                | 85.9 ms                                                | 61.4 ms: 1.40x faster                                  |
| pprint_safe_repr        | 955 ms                                                 | 687 ms: 1.39x faster                                   |
| logging_simple          | 8.07 us                                                | 5.83 us: 1.38x faster                                  |
| django_template         | 45.9 ms                                                | 33.2 ms: 1.38x faster                                  |
| logging_format          | 8.91 us                                                | 6.48 us: 1.38x faster                                  |
| async_tree_none         | 717 ms                                                 | 522 ms: 1.37x faster                                   |
| async_tree_io           | 1.77 sec                                               | 1.30 sec: 1.37x faster                                 |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                  |
| pycparser               | 1.50 sec                                               | 1.10 sec: 1.36x faster                                 |
| coroutines              | 31.8 ms                                                | 23.5 ms: 1.35x faster                                  |
| xml_etree_process       | 74.9 ms                                                | 55.4 ms: 1.35x faster                                  |
| gunicorn                | 1.46 ms                                                | 1.09 ms: 1.34x faster                                  |
| tornado_http            | 127 ms                                                 | 94.9 ms: 1.34x faster                                  |
| 2to3                    | 336 ms                                                 | 250 ms: 1.34x faster                                   |
| deepcopy                | 442 us                                                 | 329 us: 1.34x faster                                   |
| thrift                  | 1.03 ms                                                | 777 us: 1.33x faster                                   |
| regex_compile           | 177 ms                                                 | 133 ms: 1.33x faster                                   |
| scimark_fft             | 424 ms                                                 | 322 ms: 1.32x faster                                   |
| fannkuch                | 486 ms                                                 | 371 ms: 1.31x faster                                   |
| async_tree_memoization  | 854 ms                                                 | 653 ms: 1.31x faster                                   |
| genshi_xml              | 63.3 ms                                                | 48.6 ms: 1.30x faster                                  |
| deepcopy_reduce         | 3.82 us                                                | 2.94 us: 1.30x faster                                  |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                   |
| mypy2                   | 428 ms                                                 | 334 ms: 1.28x faster                                   |
| async_tree_cpu_io_mixed | 951 ms                                                 | 745 ms: 1.28x faster                                   |
| sqlglot_optimize        | 65.3 ms                                                | 51.3 ms: 1.27x faster                                  |
| docutils                | 3.17 sec                                               | 2.56 sec: 1.24x faster                                 |
| nqueens                 | 100 ms                                                 | 82.2 ms: 1.22x faster                                  |
| json_loads              | 28.8 us                                                | 23.9 us: 1.21x faster                                  |
| dulwich_log             | 75.9 ms                                                | 63.2 ms: 1.20x faster                                  |
| sqlalchemy_declarative  | 165 ms                                                 | 138 ms: 1.20x faster                                   |
| bench_thread_pool       | 947 us                                                 | 794 us: 1.19x faster                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.60 ms: 1.19x faster                                  |
| json                    | 5.42 ms                                                | 4.59 ms: 1.18x faster                                  |
| sqlalchemy_imperative   | 21.2 ms                                                | 18.0 ms: 1.18x faster                                  |
| sympy_integrate         | 24.3 ms                                                | 20.7 ms: 1.17x faster                                  |
| sympy_expand            | 545 ms                                                 | 466 ms: 1.17x faster                                   |
| xml_etree_generate      | 94.2 ms                                                | 81.3 ms: 1.16x faster                                  |
| regex_v8                | 25.0 ms                                                | 21.8 ms: 1.15x faster                                  |
| sympy_str               | 328 ms                                                 | 288 ms: 1.14x faster                                   |
| mdp                     | 2.82 sec                                               | 2.49 sec: 1.13x faster                                 |
| pickle_list             | 4.56 us                                                | 4.05 us: 1.13x faster                                  |
| sqlite_synth            | 2.93 us                                                | 2.63 us: 1.11x faster                                  |
| comprehensions          | 26.8 us                                                | 24.1 us: 1.11x faster                                  |
| pathlib                 | 20.0 ms                                                | 18.0 ms: 1.11x faster                                  |
| create_gc_cycles        | 1.67 ms                                                | 1.50 ms: 1.11x faster                                  |
| djangocms               | 35.9 us                                                | 32.5 us: 1.11x faster                                  |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.10x faster                                   |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                   |
| sympy_sum               | 185 ms                                                 | 168 ms: 1.10x faster                                   |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                   |
| regex_dna               | 222 ms                                                 | 209 ms: 1.06x faster                                   |
| unpickle                | 14.1 us                                                | 13.7 us: 1.03x faster                                  |
| pickle                  | 10.3 us                                                | 10.2 us: 1.01x faster                                  |
| async_generators        | 425 ms                                                 | 421 ms: 1.01x faster                                   |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x faster                                   |
| telco                   | 6.54 ms                                                | 6.62 ms: 1.01x slower                                  |
| regex_effbot            | 3.23 ms                                                | 3.40 ms: 1.05x slower                                  |
| unpickle_list           | 4.82 us                                                | 5.22 us: 1.08x slower                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.55 ms: 1.13x slower                                  |
| pickle_dict             | 27.3 us                                                | 31.5 us: 1.15x slower                                  |
| dask                    | 423 ms                                                 | 507 ms: 1.20x slower                                   |
| coverage                | 72.8 ms                                                | 98.3 ms: 1.35x slower                                  |
| Geometric mean          | (ref)                                                  | 1.29x faster                                           |

Benchmark hidden because not significant (2): gc_traversal, bench_mp_pool
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x
