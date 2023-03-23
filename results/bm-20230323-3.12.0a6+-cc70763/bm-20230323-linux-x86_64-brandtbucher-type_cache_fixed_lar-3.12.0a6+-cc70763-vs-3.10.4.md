
# Results vs. 3.10.4

- fork: brandtbucher
- ref: type_cache_fixed_lar
- machine: linux-x86_64
- commit hash: cc70763
- commit date: 2023-03-23
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed_lar-3.12.0a6+-cc70763 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 251 ms: 1.34x faster                                                         |
| chameleon      | 9.17 ms                                                | 6.38 ms: 1.44x faster                                                        |
| docutils       | 3.18 sec                                               | 2.52 sec: 1.26x faster                                                       |
| html5lib       | 85.9 ms                                                | 61.3 ms: 1.40x faster                                                        |
| tornado_http   | 128 ms                                                 | 91.2 ms: 1.40x faster                                                        |
| Geometric mean | (ref)                                                  | 1.37x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed_lar-3.12.0a6+-cc70763 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 87.7 ms: 1.64x faster                                                        |
| float          | 109 ms                                                 | 72.5 ms: 1.50x faster                                                        |
| pidigits       | 190 ms                                                 | 188 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed_lar-3.12.0a6+-cc70763 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 133 ms: 1.33x faster                                                         |
| regex_v8       | 25.0 ms                                                | 21.3 ms: 1.18x faster                                                        |
| regex_dna      | 214 ms                                                 | 206 ms: 1.04x faster                                                         |
| regex_effbot   | 3.19 ms                                                | 3.42 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed_lar-3.12.0a6+-cc70763 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 286 us: 1.58x faster                                                         |
| unpickle_pure_python | 302 us                                                 | 199 us: 1.52x faster                                                         |
| json_dumps           | 13.4 ms                                                | 9.55 ms: 1.41x faster                                                        |
| xml_etree_process    | 74.5 ms                                                | 56.2 ms: 1.33x faster                                                        |
| json_loads           | 28.7 us                                                | 23.8 us: 1.21x faster                                                        |
| xml_etree_generate   | 93.8 ms                                                | 80.6 ms: 1.16x faster                                                        |
| xml_etree_iterparse  | 111 ms                                                 | 99.9 ms: 1.11x faster                                                        |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                         |
| pickle_list          | 4.72 us                                                | 4.36 us: 1.08x faster                                                        |
| unpickle             | 14.2 us                                                | 13.3 us: 1.06x faster                                                        |
| unpickle_list        | 4.92 us                                                | 5.09 us: 1.03x slower                                                        |
| pickle               | 10.2 us                                                | 10.6 us: 1.04x slower                                                        |
| pickle_dict          | 27.6 us                                                | 31.7 us: 1.15x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed_lar-3.12.0a6+-cc70763 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.85 ms: 1.59x faster                                                        |
| python_startup_no_site | 5.78 ms                                                | 6.55 ms: 1.13x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed_lar-3.12.0a6+-cc70763 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 10.00 ms: 1.47x faster                                                       |
| genshi_text     | 30.6 ms                                                | 21.2 ms: 1.44x faster                                                        |
| django_template | 46.3 ms                                                | 33.1 ms: 1.40x faster                                                        |
| genshi_xml      | 63.7 ms                                                | 47.2 ms: 1.35x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed_lar-3.12.0a6+-cc70763 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators              | 76.4 ms                                                | 29.8 ms: 2.57x faster                                                        |
| deltablue               | 7.28 ms                                                | 3.30 ms: 2.21x faster                                                        |
| scimark_sor             | 197 ms                                                 | 108 ms: 1.82x faster                                                         |
| logging_silent          | 176 ns                                                 | 97.2 ns: 1.82x faster                                                        |
| asyncio_tcp             | 914 ms                                                 | 509 ms: 1.79x faster                                                         |
| richards                | 75.2 ms                                                | 44.2 ms: 1.70x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                 | 65.8 ms: 1.65x faster                                                        |
| nbody                   | 144 ms                                                 | 87.7 ms: 1.64x faster                                                        |
| raytrace                | 467 ms                                                 | 285 ms: 1.63x faster                                                         |
| pyflate                 | 676 ms                                                 | 415 ms: 1.63x faster                                                         |
| go                      | 226 ms                                                 | 140 ms: 1.61x faster                                                         |
| chaos                   | 106 ms                                                 | 66.2 ms: 1.59x faster                                                        |
| python_startup          | 14.1 ms                                                | 8.85 ms: 1.59x faster                                                        |
| pickle_pure_python      | 452 us                                                 | 286 us: 1.58x faster                                                         |
| spectral_norm           | 150 ms                                                 | 95.0 ms: 1.57x faster                                                        |
| crypto_pyaes            | 117 ms                                                 | 75.0 ms: 1.56x faster                                                        |
| hexiom                  | 9.43 ms                                                | 6.09 ms: 1.55x faster                                                        |
| unpickle_pure_python    | 302 us                                                 | 199 us: 1.52x faster                                                         |
| float                   | 109 ms                                                 | 72.5 ms: 1.50x faster                                                        |
| deepcopy_memo           | 51.7 us                                                | 34.6 us: 1.49x faster                                                        |
| scimark_lu              | 161 ms                                                 | 109 ms: 1.47x faster                                                         |
| mako                    | 14.7 ms                                                | 10.00 ms: 1.47x faster                                                       |
| genshi_text             | 30.6 ms                                                | 21.2 ms: 1.44x faster                                                        |
| chameleon               | 9.17 ms                                                | 6.38 ms: 1.44x faster                                                        |
| sqlglot_parse           | 2.04 ms                                                | 1.45 ms: 1.41x faster                                                        |
| json_dumps              | 13.4 ms                                                | 9.55 ms: 1.41x faster                                                        |
| tornado_http            | 128 ms                                                 | 91.2 ms: 1.40x faster                                                        |
| pprint_pformat          | 1.98 sec                                               | 1.41 sec: 1.40x faster                                                       |
| html5lib                | 85.9 ms                                                | 61.3 ms: 1.40x faster                                                        |
| django_template         | 46.3 ms                                                | 33.1 ms: 1.40x faster                                                        |
| sqlglot_transpile       | 2.43 ms                                                | 1.74 ms: 1.40x faster                                                        |
| pycparser               | 1.53 sec                                               | 1.10 sec: 1.39x faster                                                       |
| pprint_safe_repr        | 953 ms                                                 | 691 ms: 1.38x faster                                                         |
| scimark_fft             | 421 ms                                                 | 305 ms: 1.38x faster                                                         |
| async_tree_io           | 1.78 sec                                               | 1.30 sec: 1.37x faster                                                       |
| logging_simple          | 8.10 us                                                | 5.91 us: 1.37x faster                                                        |
| async_tree_none         | 711 ms                                                 | 521 ms: 1.37x faster                                                         |
| logging_format          | 8.85 us                                                | 6.50 us: 1.36x faster                                                        |
| genshi_xml              | 63.7 ms                                                | 47.2 ms: 1.35x faster                                                        |
| deepcopy                | 438 us                                                 | 325 us: 1.35x faster                                                         |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.05 ms: 1.35x faster                                                        |
| 2to3                    | 335 ms                                                 | 251 ms: 1.34x faster                                                         |
| coroutines              | 31.6 ms                                                | 23.7 ms: 1.34x faster                                                        |
| regex_compile           | 177 ms                                                 | 133 ms: 1.33x faster                                                         |
| thrift                  | 1.03 ms                                                | 775 us: 1.33x faster                                                         |
| fannkuch                | 488 ms                                                 | 366 ms: 1.33x faster                                                         |
| xml_etree_process       | 74.5 ms                                                | 56.2 ms: 1.33x faster                                                        |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.32x faster                                                        |
| async_tree_memoization  | 855 ms                                                 | 655 ms: 1.31x faster                                                         |
| unpack_sequence         | 59.4 ns                                                | 45.9 ns: 1.29x faster                                                        |
| mypy2                   | 430 ms                                                 | 333 ms: 1.29x faster                                                         |
| deepcopy_reduce         | 3.79 us                                                | 2.94 us: 1.29x faster                                                        |
| async_tree_cpu_io_mixed | 949 ms                                                 | 738 ms: 1.29x faster                                                         |
| sqlglot_normalize       | 134 ms                                                 | 106 ms: 1.27x faster                                                         |
| sqlglot_optimize        | 65.2 ms                                                | 51.6 ms: 1.26x faster                                                        |
| docutils                | 3.18 sec                                               | 2.52 sec: 1.26x faster                                                       |
| nqueens                 | 100 ms                                                 | 79.9 ms: 1.25x faster                                                        |
| json_loads              | 28.7 us                                                | 23.8 us: 1.21x faster                                                        |
| dulwich_log             | 75.8 ms                                                | 63.0 ms: 1.20x faster                                                        |
| bench_thread_pool       | 946 us                                                 | 789 us: 1.20x faster                                                         |
| sympy_integrate         | 24.0 ms                                                | 20.4 ms: 1.18x faster                                                        |
| regex_v8                | 25.0 ms                                                | 21.3 ms: 1.18x faster                                                        |
| sympy_expand            | 534 ms                                                 | 458 ms: 1.16x faster                                                         |
| xml_etree_generate      | 93.8 ms                                                | 80.6 ms: 1.16x faster                                                        |
| json                    | 5.35 ms                                                | 4.61 ms: 1.16x faster                                                        |
| sympy_str               | 325 ms                                                 | 282 ms: 1.15x faster                                                         |
| djangocms               | 36.9 us                                                | 32.3 us: 1.14x faster                                                        |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                                        |
| create_gc_cycles        | 1.65 ms                                                | 1.47 ms: 1.12x faster                                                        |
| xml_etree_iterparse     | 111 ms                                                 | 99.9 ms: 1.11x faster                                                        |
| sqlite_synth            | 2.92 us                                                | 2.63 us: 1.11x faster                                                        |
| sympy_sum               | 183 ms                                                 | 165 ms: 1.11x faster                                                         |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                         |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.10x faster                                                         |
| pickle_list             | 4.72 us                                                | 4.36 us: 1.08x faster                                                        |
| unpickle                | 14.2 us                                                | 13.3 us: 1.06x faster                                                        |
| telco                   | 6.73 ms                                                | 6.49 ms: 1.04x faster                                                        |
| regex_dna               | 214 ms                                                 | 206 ms: 1.04x faster                                                         |
| async_generators        | 426 ms                                                 | 413 ms: 1.03x faster                                                         |
| mdp                     | 2.74 sec                                               | 2.69 sec: 1.02x faster                                                       |
| pidigits                | 190 ms                                                 | 188 ms: 1.01x faster                                                         |
| unpickle_list           | 4.92 us                                                | 5.09 us: 1.03x slower                                                        |
| pickle                  | 10.2 us                                                | 10.6 us: 1.04x slower                                                        |
| gc_traversal            | 3.53 ms                                                | 3.67 ms: 1.04x slower                                                        |
| regex_effbot            | 3.19 ms                                                | 3.42 ms: 1.07x slower                                                        |
| python_startup_no_site  | 5.78 ms                                                | 6.55 ms: 1.13x slower                                                        |
| pickle_dict             | 27.6 us                                                | 31.7 us: 1.15x slower                                                        |
| dask                    | 436 ms                                                 | 505 ms: 1.16x slower                                                         |
| coverage                | 74.7 ms                                                | 93.0 ms: 1.24x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                                 |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230323-3.12.0a6+-cc70763/bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed_lar-3.12.0a6+-cc70763.json: comprehensions
