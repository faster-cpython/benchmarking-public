
# Results vs. 3.10.4

- fork: eduardo-elizondo
- ref: immortal_references
- machine: linux-x86_64
- commit hash: a748e80
- commit date: 2023-01-29
- overall geometric mean: 1.23x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230129-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a4+-a748e80 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 269 ms: 1.25x faster                                                              |
| chameleon      | 9.17 ms                                                | 6.91 ms: 1.33x faster                                                             |
| docutils       | 3.18 sec                                               | 2.70 sec: 1.18x faster                                                            |
| html5lib       | 85.9 ms                                                | 64.7 ms: 1.33x faster                                                             |
| tornado_http   | 128 ms                                                 | 106 ms: 1.21x faster                                                              |
| Geometric mean | (ref)                                                  | 1.26x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230129-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a4+-a748e80 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 98.0 ms: 1.47x faster                                                             |
| float          | 109 ms                                                 | 79.1 ms: 1.38x faster                                                             |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x slower                                                              |
| Geometric mean | (ref)                                                  | 1.26x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230129-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a4+-a748e80 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 142 ms: 1.25x faster                                                              |
| regex_v8       | 25.0 ms                                                | 21.9 ms: 1.14x faster                                                             |
| regex_dna      | 214 ms                                                 | 206 ms: 1.04x faster                                                              |
| regex_effbot   | 3.19 ms                                                | 3.68 ms: 1.15x slower                                                             |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230129-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a4+-a748e80 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 311 us: 1.46x faster                                                              |
| unpickle_pure_python | 302 us                                                 | 214 us: 1.41x faster                                                              |
| json_dumps           | 13.4 ms                                                | 9.76 ms: 1.38x faster                                                             |
| xml_etree_process    | 74.5 ms                                                | 57.8 ms: 1.29x faster                                                             |
| xml_etree_generate   | 93.8 ms                                                | 81.6 ms: 1.15x faster                                                             |
| json_loads           | 28.7 us                                                | 26.6 us: 1.08x faster                                                             |
| xml_etree_parse      | 163 ms                                                 | 154 ms: 1.06x faster                                                              |
| unpickle             | 14.2 us                                                | 13.4 us: 1.06x faster                                                             |
| xml_etree_iterparse  | 111 ms                                                 | 107 ms: 1.04x faster                                                              |
| pickle_list          | 4.72 us                                                | 4.57 us: 1.03x faster                                                             |
| unpickle_list        | 4.92 us                                                | 4.83 us: 1.02x faster                                                             |
| pickle               | 10.2 us                                                | 10.4 us: 1.03x slower                                                             |
| pickle_dict          | 27.6 us                                                | 30.6 us: 1.11x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230129-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a4+-a748e80 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 9.13 ms: 1.54x faster                                                             |
| python_startup_no_site | 5.78 ms                                                | 6.56 ms: 1.14x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.17x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230129-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a4+-a748e80 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 10.2 ms: 1.43x faster                                                             |
| genshi_text     | 30.6 ms                                                | 22.5 ms: 1.36x faster                                                             |
| django_template | 46.3 ms                                                | 34.8 ms: 1.33x faster                                                             |
| genshi_xml      | 63.7 ms                                                | 50.5 ms: 1.26x faster                                                             |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230129-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a4+-a748e80 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.51 ms: 2.07x faster                                                             |
| logging_silent          | 176 ns                                                 | 94.6 ns: 1.87x faster                                                             |
| asyncio_tcp             | 914 ms                                                 | 516 ms: 1.77x faster                                                              |
| richards                | 75.2 ms                                                | 43.2 ms: 1.74x faster                                                             |
| go                      | 226 ms                                                 | 133 ms: 1.69x faster                                                              |
| scimark_sor             | 197 ms                                                 | 117 ms: 1.69x faster                                                              |
| pyflate                 | 676 ms                                                 | 423 ms: 1.60x faster                                                              |
| chaos                   | 106 ms                                                 | 67.1 ms: 1.57x faster                                                             |
| python_startup          | 14.1 ms                                                | 9.13 ms: 1.54x faster                                                             |
| hexiom                  | 9.43 ms                                                | 6.12 ms: 1.54x faster                                                             |
| scimark_monte_carlo     | 109 ms                                                 | 70.7 ms: 1.53x faster                                                             |
| raytrace                | 467 ms                                                 | 307 ms: 1.52x faster                                                              |
| crypto_pyaes            | 117 ms                                                 | 76.9 ms: 1.52x faster                                                             |
| nbody                   | 144 ms                                                 | 98.0 ms: 1.47x faster                                                             |
| pickle_pure_python      | 452 us                                                 | 311 us: 1.46x faster                                                              |
| mako                    | 14.7 ms                                                | 10.2 ms: 1.43x faster                                                             |
| spectral_norm           | 150 ms                                                 | 105 ms: 1.42x faster                                                              |
| scimark_lu              | 161 ms                                                 | 113 ms: 1.42x faster                                                              |
| unpickle_pure_python    | 302 us                                                 | 214 us: 1.41x faster                                                              |
| json_dumps              | 13.4 ms                                                | 9.76 ms: 1.38x faster                                                             |
| float                   | 109 ms                                                 | 79.1 ms: 1.38x faster                                                             |
| genshi_text             | 30.6 ms                                                | 22.5 ms: 1.36x faster                                                             |
| thrift                  | 1.03 ms                                                | 761 us: 1.36x faster                                                              |
| deepcopy_memo           | 51.7 us                                                | 38.1 us: 1.36x faster                                                             |
| django_template         | 46.3 ms                                                | 34.8 ms: 1.33x faster                                                             |
| html5lib                | 85.9 ms                                                | 64.7 ms: 1.33x faster                                                             |
| sqlglot_parse           | 2.04 ms                                                | 1.54 ms: 1.33x faster                                                             |
| chameleon               | 9.17 ms                                                | 6.91 ms: 1.33x faster                                                             |
| pycparser               | 1.53 sec                                               | 1.16 sec: 1.32x faster                                                            |
| async_tree_io           | 1.78 sec                                               | 1.35 sec: 1.32x faster                                                            |
| pprint_pformat          | 1.98 sec                                               | 1.50 sec: 1.32x faster                                                            |
| fannkuch                | 488 ms                                                 | 370 ms: 1.32x faster                                                              |
| async_tree_none         | 711 ms                                                 | 540 ms: 1.32x faster                                                              |
| sqlglot_transpile       | 2.43 ms                                                | 1.87 ms: 1.30x faster                                                             |
| pprint_safe_repr        | 953 ms                                                 | 736 ms: 1.30x faster                                                              |
| xml_etree_process       | 74.5 ms                                                | 57.8 ms: 1.29x faster                                                             |
| nqueens                 | 100 ms                                                 | 78.1 ms: 1.28x faster                                                             |
| logging_simple          | 8.10 us                                                | 6.40 us: 1.27x faster                                                             |
| genshi_xml              | 63.7 ms                                                | 50.5 ms: 1.26x faster                                                             |
| logging_format          | 8.85 us                                                | 7.05 us: 1.26x faster                                                             |
| unpack_sequence         | 59.4 ns                                                | 47.3 ns: 1.25x faster                                                             |
| 2to3                    | 335 ms                                                 | 269 ms: 1.25x faster                                                              |
| regex_compile           | 177 ms                                                 | 142 ms: 1.25x faster                                                              |
| async_tree_memoization  | 855 ms                                                 | 687 ms: 1.25x faster                                                              |
| async_tree_cpu_io_mixed | 949 ms                                                 | 770 ms: 1.23x faster                                                              |
| coroutines              | 31.6 ms                                                | 25.9 ms: 1.22x faster                                                             |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.49 ms: 1.22x faster                                                             |
| deepcopy_reduce         | 3.79 us                                                | 3.12 us: 1.21x faster                                                             |
| tornado_http            | 128 ms                                                 | 106 ms: 1.21x faster                                                              |
| deepcopy                | 438 us                                                 | 363 us: 1.20x faster                                                              |
| mypy2                   | 430 ms                                                 | 360 ms: 1.19x faster                                                              |
| docutils                | 3.18 sec                                               | 2.70 sec: 1.18x faster                                                            |
| scimark_fft             | 421 ms                                                 | 357 ms: 1.18x faster                                                              |
| sqlglot_optimize        | 65.2 ms                                                | 55.4 ms: 1.18x faster                                                             |
| async_generators        | 426 ms                                                 | 362 ms: 1.18x faster                                                              |
| sqlglot_normalize       | 134 ms                                                 | 115 ms: 1.17x faster                                                              |
| xml_etree_generate      | 93.8 ms                                                | 81.6 ms: 1.15x faster                                                             |
| regex_v8                | 25.0 ms                                                | 21.9 ms: 1.14x faster                                                             |
| dask                    | 436 ms                                                 | 385 ms: 1.13x faster                                                              |
| sympy_integrate         | 24.0 ms                                                | 21.3 ms: 1.13x faster                                                             |
| bench_thread_pool       | 946 us                                                 | 838 us: 1.13x faster                                                              |
| create_gc_cycles        | 1.65 ms                                                | 1.47 ms: 1.12x faster                                                             |
| sqlite_synth            | 2.92 us                                                | 2.62 us: 1.12x faster                                                             |
| djangocms               | 36.9 us                                                | 33.1 us: 1.11x faster                                                             |
| dulwich_log             | 75.8 ms                                                | 68.4 ms: 1.11x faster                                                             |
| mdp                     | 2.74 sec                                               | 2.54 sec: 1.08x faster                                                            |
| pathlib                 | 20.0 ms                                                | 18.5 ms: 1.08x faster                                                             |
| json_loads              | 28.7 us                                                | 26.6 us: 1.08x faster                                                             |
| sympy_str               | 325 ms                                                 | 302 ms: 1.08x faster                                                              |
| sympy_expand            | 534 ms                                                 | 499 ms: 1.07x faster                                                              |
| sympy_sum               | 183 ms                                                 | 172 ms: 1.06x faster                                                              |
| xml_etree_parse         | 163 ms                                                 | 154 ms: 1.06x faster                                                              |
| unpickle                | 14.2 us                                                | 13.4 us: 1.06x faster                                                             |
| xml_etree_iterparse     | 111 ms                                                 | 107 ms: 1.04x faster                                                              |
| json                    | 5.35 ms                                                | 5.14 ms: 1.04x faster                                                             |
| regex_dna               | 214 ms                                                 | 206 ms: 1.04x faster                                                              |
| pickle_list             | 4.72 us                                                | 4.57 us: 1.03x faster                                                             |
| meteor_contest          | 114 ms                                                 | 111 ms: 1.03x faster                                                              |
| unpickle_list           | 4.92 us                                                | 4.83 us: 1.02x faster                                                             |
| telco                   | 6.73 ms                                                | 6.67 ms: 1.01x faster                                                             |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x slower                                                              |
| generators              | 76.4 ms                                                | 76.8 ms: 1.00x slower                                                             |
| pickle                  | 10.2 us                                                | 10.4 us: 1.03x slower                                                             |
| pickle_dict             | 27.6 us                                                | 30.6 us: 1.11x slower                                                             |
| python_startup_no_site  | 5.78 ms                                                | 6.56 ms: 1.14x slower                                                             |
| regex_effbot            | 3.19 ms                                                | 3.68 ms: 1.15x slower                                                             |
| gc_traversal            | 3.53 ms                                                | 4.29 ms: 1.22x slower                                                             |
| coverage                | 74.7 ms                                                | 102 ms: 1.36x slower                                                              |
| Geometric mean          | (ref)                                                  | 1.23x faster                                                                      |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230129-3.12.0a4+-a748e80/bm-20230129-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a4+-a748e80.json: comprehensions
