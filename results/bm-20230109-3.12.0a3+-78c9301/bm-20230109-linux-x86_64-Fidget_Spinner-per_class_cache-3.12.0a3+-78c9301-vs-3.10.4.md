
# Results vs. 3.10.4

- fork: Fidget_Spinner
- ref: per_class_cache
- machine: linux-x86_64
- commit hash: 78c9301
- commit date: 2023-01-09
- overall geometric mean: 1.29x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 254 ms: 1.32x faster                                                      |
| chameleon      | 9.17 ms                                                | 6.26 ms: 1.46x faster                                                     |
| docutils       | 3.18 sec                                               | 2.52 sec: 1.26x faster                                                    |
| html5lib       | 85.9 ms                                                | 60.3 ms: 1.42x faster                                                     |
| Geometric mean | (ref)                                                  | 1.37x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 94.9 ms: 1.52x faster                                                     |
| float          | 109 ms                                                 | 72.8 ms: 1.50x faster                                                     |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                  | 1.31x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 130 ms: 1.37x faster                                                      |
| regex_v8       | 25.0 ms                                                | 22.3 ms: 1.12x faster                                                     |
| regex_dna      | 214 ms                                                 | 209 ms: 1.02x faster                                                      |
| regex_effbot   | 3.19 ms                                                | 3.55 ms: 1.11x slower                                                     |
| Geometric mean | (ref)                                                  | 1.09x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 288 us: 1.57x faster                                                      |
| unpickle_pure_python | 302 us                                                 | 199 us: 1.51x faster                                                      |
| json_dumps           | 13.4 ms                                                | 9.48 ms: 1.42x faster                                                     |
| xml_etree_process    | 74.5 ms                                                | 53.9 ms: 1.38x faster                                                     |
| xml_etree_generate   | 93.8 ms                                                | 77.1 ms: 1.22x faster                                                     |
| json_loads           | 28.7 us                                                | 24.3 us: 1.18x faster                                                     |
| pickle_list          | 4.72 us                                                | 4.15 us: 1.14x faster                                                     |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                                      |
| xml_etree_iterparse  | 111 ms                                                 | 106 ms: 1.05x faster                                                      |
| unpickle             | 14.2 us                                                | 13.7 us: 1.04x faster                                                     |
| pickle               | 10.2 us                                                | 9.89 us: 1.03x faster                                                     |
| pickle_dict          | 27.6 us                                                | 30.2 us: 1.09x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                              |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.48 ms: 1.66x faster                                                     |
| python_startup_no_site | 5.78 ms                                                | 6.07 ms: 1.05x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.26x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.6 ms: 1.48x faster                                                     |
| mako            | 14.7 ms                                                | 9.89 ms: 1.48x faster                                                     |
| django_template | 46.3 ms                                                | 32.5 ms: 1.42x faster                                                     |
| genshi_xml      | 63.7 ms                                                | 46.7 ms: 1.36x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                              |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.71 ms: 1.96x faster                                                     |
| logging_silent          | 176 ns                                                 | 93.9 ns: 1.88x faster                                                     |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.84x faster                                                      |
| go                      | 226 ms                                                 | 135 ms: 1.67x faster                                                      |
| scimark_monte_carlo     | 109 ms                                                 | 65.1 ms: 1.67x faster                                                     |
| python_startup          | 14.1 ms                                                | 8.48 ms: 1.66x faster                                                     |
| pyflate                 | 676 ms                                                 | 409 ms: 1.65x faster                                                      |
| richards                | 75.2 ms                                                | 46.0 ms: 1.63x faster                                                     |
| raytrace                | 467 ms                                                 | 291 ms: 1.60x faster                                                      |
| pickle_pure_python      | 452 us                                                 | 288 us: 1.57x faster                                                      |
| chaos                   | 106 ms                                                 | 67.5 ms: 1.56x faster                                                     |
| crypto_pyaes            | 117 ms                                                 | 75.5 ms: 1.55x faster                                                     |
| spectral_norm           | 150 ms                                                 | 98.0 ms: 1.53x faster                                                     |
| hexiom                  | 9.43 ms                                                | 6.18 ms: 1.52x faster                                                     |
| nbody                   | 144 ms                                                 | 94.9 ms: 1.52x faster                                                     |
| unpickle_pure_python    | 302 us                                                 | 199 us: 1.51x faster                                                      |
| float                   | 109 ms                                                 | 72.8 ms: 1.50x faster                                                     |
| deepcopy_memo           | 51.7 us                                                | 34.7 us: 1.49x faster                                                     |
| genshi_text             | 30.6 ms                                                | 20.6 ms: 1.48x faster                                                     |
| scimark_lu              | 161 ms                                                 | 108 ms: 1.48x faster                                                      |
| mako                    | 14.7 ms                                                | 9.89 ms: 1.48x faster                                                     |
| chameleon               | 9.17 ms                                                | 6.26 ms: 1.46x faster                                                     |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.45x faster                                                     |
| html5lib                | 85.9 ms                                                | 60.3 ms: 1.42x faster                                                     |
| django_template         | 46.3 ms                                                | 32.5 ms: 1.42x faster                                                     |
| sqlglot_transpile       | 2.43 ms                                                | 1.71 ms: 1.42x faster                                                     |
| json_dumps              | 13.4 ms                                                | 9.48 ms: 1.42x faster                                                     |
| pprint_pformat          | 1.98 sec                                               | 1.40 sec: 1.41x faster                                                    |
| pprint_safe_repr        | 953 ms                                                 | 676 ms: 1.41x faster                                                      |
| unpack_sequence         | 59.4 ns                                                | 42.9 ns: 1.38x faster                                                     |
| xml_etree_process       | 74.5 ms                                                | 53.9 ms: 1.38x faster                                                     |
| regex_compile           | 177 ms                                                 | 130 ms: 1.37x faster                                                      |
| genshi_xml              | 63.7 ms                                                | 46.7 ms: 1.36x faster                                                     |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.02 ms: 1.36x faster                                                     |
| thrift                  | 1.03 ms                                                | 765 us: 1.35x faster                                                      |
| logging_simple          | 8.10 us                                                | 6.01 us: 1.35x faster                                                     |
| async_tree_none         | 711 ms                                                 | 531 ms: 1.34x faster                                                      |
| async_tree_io           | 1.78 sec                                               | 1.33 sec: 1.34x faster                                                    |
| logging_format          | 8.85 us                                                | 6.64 us: 1.33x faster                                                     |
| pycparser               | 1.53 sec                                               | 1.15 sec: 1.33x faster                                                    |
| 2to3                    | 335 ms                                                 | 254 ms: 1.32x faster                                                      |
| scimark_fft             | 421 ms                                                 | 319 ms: 1.32x faster                                                      |
| deepcopy                | 438 us                                                 | 335 us: 1.31x faster                                                      |
| fannkuch                | 488 ms                                                 | 375 ms: 1.30x faster                                                      |
| coroutines              | 31.6 ms                                                | 24.7 ms: 1.28x faster                                                     |
| nqueens                 | 100 ms                                                 | 78.4 ms: 1.28x faster                                                     |
| async_tree_memoization  | 855 ms                                                 | 670 ms: 1.28x faster                                                      |
| sqlglot_normalize       | 134 ms                                                 | 106 ms: 1.27x faster                                                      |
| sqlglot_optimize        | 65.2 ms                                                | 51.6 ms: 1.27x faster                                                     |
| docutils                | 3.18 sec                                               | 2.52 sec: 1.26x faster                                                    |
| async_tree_cpu_io_mixed | 949 ms                                                 | 758 ms: 1.25x faster                                                      |
| deepcopy_reduce         | 3.79 us                                                | 3.03 us: 1.25x faster                                                     |
| dulwich_log             | 75.8 ms                                                | 62.0 ms: 1.22x faster                                                     |
| xml_etree_generate      | 93.8 ms                                                | 77.1 ms: 1.22x faster                                                     |
| bench_thread_pool       | 946 us                                                 | 786 us: 1.20x faster                                                      |
| async_generators        | 426 ms                                                 | 356 ms: 1.20x faster                                                      |
| sympy_integrate         | 24.0 ms                                                | 20.3 ms: 1.19x faster                                                     |
| json_loads              | 28.7 us                                                | 24.3 us: 1.18x faster                                                     |
| sympy_expand            | 534 ms                                                 | 457 ms: 1.17x faster                                                      |
| sympy_str               | 325 ms                                                 | 281 ms: 1.16x faster                                                      |
| json                    | 5.35 ms                                                | 4.63 ms: 1.15x faster                                                     |
| djangocms               | 36.9 us                                                | 32.3 us: 1.14x faster                                                     |
| pickle_list             | 4.72 us                                                | 4.15 us: 1.14x faster                                                     |
| sqlite_synth            | 2.92 us                                                | 2.58 us: 1.13x faster                                                     |
| sympy_sum               | 183 ms                                                 | 163 ms: 1.12x faster                                                      |
| regex_v8                | 25.0 ms                                                | 22.3 ms: 1.12x faster                                                     |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                                      |
| pathlib                 | 20.0 ms                                                | 18.3 ms: 1.09x faster                                                     |
| meteor_contest          | 114 ms                                                 | 106 ms: 1.08x faster                                                      |
| telco                   | 6.73 ms                                                | 6.28 ms: 1.07x faster                                                     |
| xml_etree_iterparse     | 111 ms                                                 | 106 ms: 1.05x faster                                                      |
| mdp                     | 2.74 sec                                               | 2.65 sec: 1.04x faster                                                    |
| unpickle                | 14.2 us                                                | 13.7 us: 1.04x faster                                                     |
| pickle                  | 10.2 us                                                | 9.89 us: 1.03x faster                                                     |
| regex_dna               | 214 ms                                                 | 209 ms: 1.02x faster                                                      |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                      |
| generators              | 76.4 ms                                                | 77.4 ms: 1.01x slower                                                     |
| python_startup_no_site  | 5.78 ms                                                | 6.07 ms: 1.05x slower                                                     |
| pickle_dict             | 27.6 us                                                | 30.2 us: 1.09x slower                                                     |
| regex_effbot            | 3.19 ms                                                | 3.55 ms: 1.11x slower                                                     |
| coverage                | 74.7 ms                                                | 96.9 ms: 1.30x slower                                                     |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                              |

Benchmark hidden because not significant (2): bench_mp_pool, unpickle_list
Ignored benchmarks (12) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230109-3.12.0a3+-78c9301/bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301.json: mypy
