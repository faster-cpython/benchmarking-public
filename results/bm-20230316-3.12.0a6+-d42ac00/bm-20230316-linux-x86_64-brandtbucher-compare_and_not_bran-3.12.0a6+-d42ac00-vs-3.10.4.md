
# Results vs. 3.10.4

- fork: brandtbucher
- ref: compare_and_not_bran
- machine: linux-x86_64
- commit hash: d42ac00
- commit date: 2023-03-16
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a6+-d42ac00 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 252 ms: 1.34x faster                                                         |
| chameleon      | 9.06 ms                                                | 6.52 ms: 1.39x faster                                                        |
| docutils       | 3.17 sec                                               | 2.54 sec: 1.25x faster                                                       |
| html5lib       | 85.9 ms                                                | 62.0 ms: 1.39x faster                                                        |
| tornado_http   | 127 ms                                                 | 91.9 ms: 1.39x faster                                                        |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a6+-d42ac00 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 87.7 ms: 1.61x faster                                                        |
| float          | 111 ms                                                 | 73.7 ms: 1.50x faster                                                        |
| pidigits       | 190 ms                                                 | 192 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a6+-d42ac00 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 135 ms: 1.31x faster                                                         |
| regex_v8       | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                        |
| regex_dna      | 222 ms                                                 | 208 ms: 1.07x faster                                                         |
| regex_effbot   | 3.23 ms                                                | 3.45 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a6+-d42ac00 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 289 us: 1.58x faster                                                         |
| unpickle_pure_python | 300 us                                                 | 203 us: 1.48x faster                                                         |
| json_dumps           | 13.5 ms                                                | 9.42 ms: 1.44x faster                                                        |
| xml_etree_process    | 74.9 ms                                                | 55.7 ms: 1.35x faster                                                        |
| json_loads           | 28.8 us                                                | 24.4 us: 1.18x faster                                                        |
| xml_etree_generate   | 94.2 ms                                                | 80.3 ms: 1.17x faster                                                        |
| xml_etree_iterparse  | 111 ms                                                 | 100 ms: 1.11x faster                                                         |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                         |
| pickle_list          | 4.56 us                                                | 4.16 us: 1.09x faster                                                        |
| unpickle             | 14.1 us                                                | 13.5 us: 1.05x faster                                                        |
| unpickle_list        | 4.82 us                                                | 5.00 us: 1.04x slower                                                        |
| pickle_dict          | 27.3 us                                                | 30.9 us: 1.13x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                                 |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a6+-d42ac00 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.91 ms: 1.59x faster                                                        |
| python_startup_no_site | 5.82 ms                                                | 6.52 ms: 1.12x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a6+-d42ac00 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.95 ms: 1.48x faster                                                        |
| genshi_text     | 30.3 ms                                                | 21.6 ms: 1.40x faster                                                        |
| django_template | 45.9 ms                                                | 33.4 ms: 1.37x faster                                                        |
| genshi_xml      | 63.3 ms                                                | 47.7 ms: 1.33x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a6+-d42ac00 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 29.4 ms: 2.61x faster                                                        |
| deltablue               | 7.42 ms                                                | 3.21 ms: 2.31x faster                                                        |
| logging_silent          | 175 ns                                                 | 95.2 ns: 1.84x faster                                                        |
| asyncio_tcp             | 925 ms                                                 | 506 ms: 1.83x faster                                                         |
| scimark_sor             | 197 ms                                                 | 109 ms: 1.80x faster                                                         |
| richards                | 74.9 ms                                                | 43.0 ms: 1.74x faster                                                        |
| spectral_norm           | 150 ms                                                 | 90.0 ms: 1.67x faster                                                        |
| go                      | 229 ms                                                 | 139 ms: 1.66x faster                                                         |
| nbody                   | 142 ms                                                 | 87.7 ms: 1.61x faster                                                        |
| raytrace                | 464 ms                                                 | 289 ms: 1.61x faster                                                         |
| scimark_monte_carlo     | 108 ms                                                 | 67.5 ms: 1.60x faster                                                        |
| crypto_pyaes            | 118 ms                                                 | 73.9 ms: 1.60x faster                                                        |
| python_startup          | 14.2 ms                                                | 8.91 ms: 1.59x faster                                                        |
| pyflate                 | 673 ms                                                 | 425 ms: 1.58x faster                                                         |
| pickle_pure_python      | 455 us                                                 | 289 us: 1.58x faster                                                         |
| hexiom                  | 9.53 ms                                                | 6.11 ms: 1.56x faster                                                        |
| chaos                   | 106 ms                                                 | 68.7 ms: 1.55x faster                                                        |
| deepcopy_memo           | 52.3 us                                                | 34.0 us: 1.54x faster                                                        |
| unpack_sequence         | 64.7 ns                                                | 42.3 ns: 1.53x faster                                                        |
| float                   | 111 ms                                                 | 73.7 ms: 1.50x faster                                                        |
| scimark_lu              | 163 ms                                                 | 109 ms: 1.50x faster                                                         |
| mako                    | 14.8 ms                                                | 9.95 ms: 1.48x faster                                                        |
| unpickle_pure_python    | 300 us                                                 | 203 us: 1.48x faster                                                         |
| sqlglot_parse           | 2.06 ms                                                | 1.43 ms: 1.44x faster                                                        |
| json_dumps              | 13.5 ms                                                | 9.42 ms: 1.44x faster                                                        |
| sqlglot_transpile       | 2.45 ms                                                | 1.73 ms: 1.42x faster                                                        |
| pprint_pformat          | 1.99 sec                                               | 1.40 sec: 1.41x faster                                                       |
| logging_format          | 8.91 us                                                | 6.32 us: 1.41x faster                                                        |
| logging_simple          | 8.07 us                                                | 5.73 us: 1.41x faster                                                        |
| genshi_text             | 30.3 ms                                                | 21.6 ms: 1.40x faster                                                        |
| async_tree_none         | 717 ms                                                 | 515 ms: 1.39x faster                                                         |
| async_tree_io           | 1.77 sec                                               | 1.28 sec: 1.39x faster                                                       |
| chameleon               | 9.06 ms                                                | 6.52 ms: 1.39x faster                                                        |
| coroutines              | 31.8 ms                                                | 22.9 ms: 1.39x faster                                                        |
| tornado_http            | 127 ms                                                 | 91.9 ms: 1.39x faster                                                        |
| html5lib                | 85.9 ms                                                | 62.0 ms: 1.39x faster                                                        |
| pprint_safe_repr        | 955 ms                                                 | 691 ms: 1.38x faster                                                         |
| django_template         | 45.9 ms                                                | 33.4 ms: 1.37x faster                                                        |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                                        |
| scimark_fft             | 424 ms                                                 | 311 ms: 1.36x faster                                                         |
| deepcopy                | 442 us                                                 | 327 us: 1.35x faster                                                         |
| xml_etree_process       | 74.9 ms                                                | 55.7 ms: 1.35x faster                                                        |
| gunicorn                | 1.46 ms                                                | 1.08 ms: 1.35x faster                                                        |
| 2to3                    | 336 ms                                                 | 252 ms: 1.34x faster                                                         |
| genshi_xml              | 63.3 ms                                                | 47.7 ms: 1.33x faster                                                        |
| thrift                  | 1.03 ms                                                | 780 us: 1.32x faster                                                         |
| async_tree_memoization  | 854 ms                                                 | 648 ms: 1.32x faster                                                         |
| sqlglot_normalize       | 135 ms                                                 | 103 ms: 1.31x faster                                                         |
| deepcopy_reduce         | 3.82 us                                                | 2.92 us: 1.31x faster                                                        |
| regex_compile           | 177 ms                                                 | 135 ms: 1.31x faster                                                         |
| async_tree_cpu_io_mixed | 951 ms                                                 | 733 ms: 1.30x faster                                                         |
| mypy2                   | 428 ms                                                 | 333 ms: 1.29x faster                                                         |
| sqlglot_optimize        | 65.3 ms                                                | 50.9 ms: 1.28x faster                                                        |
| pycparser               | 1.50 sec                                               | 1.17 sec: 1.28x faster                                                       |
| fannkuch                | 486 ms                                                 | 382 ms: 1.27x faster                                                         |
| docutils                | 3.17 sec                                               | 2.54 sec: 1.25x faster                                                       |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.41 ms: 1.24x faster                                                        |
| nqueens                 | 100 ms                                                 | 80.9 ms: 1.24x faster                                                        |
| sqlalchemy_declarative  | 165 ms                                                 | 136 ms: 1.21x faster                                                         |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.6 ms: 1.21x faster                                                        |
| bench_thread_pool       | 947 us                                                 | 793 us: 1.20x faster                                                         |
| sympy_integrate         | 24.3 ms                                                | 20.4 ms: 1.19x faster                                                        |
| dulwich_log             | 75.9 ms                                                | 63.8 ms: 1.19x faster                                                        |
| sympy_expand            | 545 ms                                                 | 460 ms: 1.19x faster                                                         |
| json_loads              | 28.8 us                                                | 24.4 us: 1.18x faster                                                        |
| json                    | 5.42 ms                                                | 4.62 ms: 1.17x faster                                                        |
| xml_etree_generate      | 94.2 ms                                                | 80.3 ms: 1.17x faster                                                        |
| sympy_str               | 328 ms                                                 | 283 ms: 1.16x faster                                                         |
| regex_v8                | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                        |
| mdp                     | 2.82 sec                                               | 2.47 sec: 1.14x faster                                                       |
| create_gc_cycles        | 1.67 ms                                                | 1.47 ms: 1.14x faster                                                        |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                                        |
| comprehensions          | 26.8 us                                                | 23.8 us: 1.12x faster                                                        |
| sympy_sum               | 185 ms                                                 | 166 ms: 1.11x faster                                                         |
| xml_etree_iterparse     | 111 ms                                                 | 100 ms: 1.11x faster                                                         |
| djangocms               | 35.9 us                                                | 32.4 us: 1.11x faster                                                        |
| sqlite_synth            | 2.93 us                                                | 2.65 us: 1.11x faster                                                        |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.11x faster                                                         |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                         |
| pickle_list             | 4.56 us                                                | 4.16 us: 1.09x faster                                                        |
| regex_dna               | 222 ms                                                 | 208 ms: 1.07x faster                                                         |
| unpickle                | 14.1 us                                                | 13.5 us: 1.05x faster                                                        |
| gc_traversal            | 3.84 ms                                                | 3.66 ms: 1.05x faster                                                        |
| async_generators        | 425 ms                                                 | 414 ms: 1.03x faster                                                         |
| pidigits                | 190 ms                                                 | 192 ms: 1.01x slower                                                         |
| unpickle_list           | 4.82 us                                                | 5.00 us: 1.04x slower                                                        |
| regex_effbot            | 3.23 ms                                                | 3.45 ms: 1.07x slower                                                        |
| python_startup_no_site  | 5.82 ms                                                | 6.52 ms: 1.12x slower                                                        |
| pickle_dict             | 27.3 us                                                | 30.9 us: 1.13x slower                                                        |
| dask                    | 423 ms                                                 | 510 ms: 1.21x slower                                                         |
| coverage                | 72.8 ms                                                | 97.2 ms: 1.34x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                                 |

Benchmark hidden because not significant (3): telco, bench_mp_pool, pickle
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x
