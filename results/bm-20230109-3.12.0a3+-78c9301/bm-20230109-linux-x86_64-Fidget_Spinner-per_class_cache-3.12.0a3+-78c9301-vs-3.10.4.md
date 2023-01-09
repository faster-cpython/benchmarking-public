
# Results vs. 3.10.4

- fork: Fidget_Spinner
- ref: per_class_cache
- machine: linux-x86_64
- commit hash: 78c9301
- commit date: 2023-01-09
- overall geometric mean: 1.29x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 254 ms: 1.31x faster                                                      |
| chameleon      | 8.86 ms                                                | 6.26 ms: 1.41x faster                                                     |
| docutils       | 3.18 sec                                               | 2.52 sec: 1.26x faster                                                    |
| html5lib       | 85.8 ms                                                | 60.3 ms: 1.42x faster                                                     |
| Geometric mean | (ref)                                                  | 1.35x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 108 ms                                                 | 72.8 ms: 1.48x faster                                                     |
| nbody          | 136 ms                                                 | 94.9 ms: 1.43x faster                                                     |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                  | 1.29x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 130 ms: 1.34x faster                                                      |
| regex_dna      | 214 ms                                                 | 209 ms: 1.03x faster                                                      |
| regex_effbot   | 3.21 ms                                                | 3.55 ms: 1.11x slower                                                     |
| regex_v8       | 25.0 ms                                                | 22.3 ms: 1.12x faster                                                     |
| Geometric mean | (ref)                                                  | 1.09x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 13.5 ms                                                | 9.48 ms: 1.42x faster                                                     |
| json_loads           | 28.9 us                                                | 24.3 us: 1.19x faster                                                     |
| pickle               | 10.1 us                                                | 9.89 us: 1.02x faster                                                     |
| pickle_dict          | 28.3 us                                                | 30.2 us: 1.07x slower                                                     |
| pickle_list          | 4.50 us                                                | 4.15 us: 1.09x faster                                                     |
| pickle_pure_python   | 453 us                                                 | 288 us: 1.57x faster                                                      |
| unpickle             | 14.3 us                                                | 13.7 us: 1.04x faster                                                     |
| unpickle_pure_python | 297 us                                                 | 199 us: 1.49x faster                                                      |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                                      |
| xml_etree_iterparse  | 110 ms                                                 | 106 ms: 1.05x faster                                                      |
| xml_etree_generate   | 93.3 ms                                                | 77.1 ms: 1.21x faster                                                     |
| xml_etree_process    | 74.5 ms                                                | 53.9 ms: 1.38x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                              |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.48 ms: 1.64x faster                                                     |
| python_startup_no_site | 5.76 ms                                                | 6.07 ms: 1.05x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.25x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 46.3 ms                                                | 32.5 ms: 1.42x faster                                                     |
| genshi_text     | 30.6 ms                                                | 20.6 ms: 1.48x faster                                                     |
| genshi_xml      | 63.6 ms                                                | 46.7 ms: 1.36x faster                                                     |
| mako            | 14.3 ms                                                | 9.89 ms: 1.44x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                              |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3                    | 332 ms                                                 | 254 ms: 1.31x faster                                                      |
| async_generators        | 428 ms                                                 | 356 ms: 1.20x faster                                                      |
| async_tree_none         | 713 ms                                                 | 531 ms: 1.34x faster                                                      |
| async_tree_cpu_io_mixed | 949 ms                                                 | 758 ms: 1.25x faster                                                      |
| async_tree_io           | 1.78 sec                                               | 1.33 sec: 1.34x faster                                                    |
| async_tree_memoization  | 854 ms                                                 | 670 ms: 1.27x faster                                                      |
| chameleon               | 8.86 ms                                                | 6.26 ms: 1.41x faster                                                     |
| chaos                   | 104 ms                                                 | 67.5 ms: 1.54x faster                                                     |
| bench_thread_pool       | 943 us                                                 | 786 us: 1.20x faster                                                      |
| coroutines              | 31.7 ms                                                | 24.7 ms: 1.28x faster                                                     |
| coverage                | 75.3 ms                                                | 96.9 ms: 1.29x slower                                                     |
| crypto_pyaes            | 118 ms                                                 | 75.5 ms: 1.56x faster                                                     |
| deepcopy                | 429 us                                                 | 335 us: 1.28x faster                                                      |
| deepcopy_reduce         | 3.75 us                                                | 3.03 us: 1.24x faster                                                     |
| deepcopy_memo           | 50.0 us                                                | 34.7 us: 1.44x faster                                                     |
| deltablue               | 7.39 ms                                                | 3.71 ms: 1.99x faster                                                     |
| django_template         | 46.3 ms                                                | 32.5 ms: 1.42x faster                                                     |
| docutils                | 3.18 sec                                               | 2.52 sec: 1.26x faster                                                    |
| dulwich_log             | 75.5 ms                                                | 62.0 ms: 1.22x faster                                                     |
| fannkuch                | 477 ms                                                 | 375 ms: 1.27x faster                                                      |
| float                   | 108 ms                                                 | 72.8 ms: 1.48x faster                                                     |
| generators              | 75.8 ms                                                | 77.4 ms: 1.02x slower                                                     |
| genshi_text             | 30.6 ms                                                | 20.6 ms: 1.48x faster                                                     |
| genshi_xml              | 63.6 ms                                                | 46.7 ms: 1.36x faster                                                     |
| go                      | 226 ms                                                 | 135 ms: 1.67x faster                                                      |
| hexiom                  | 9.42 ms                                                | 6.18 ms: 1.52x faster                                                     |
| html5lib                | 85.8 ms                                                | 60.3 ms: 1.42x faster                                                     |
| json                    | 5.35 ms                                                | 4.63 ms: 1.16x faster                                                     |
| json_dumps              | 13.5 ms                                                | 9.48 ms: 1.42x faster                                                     |
| json_loads              | 28.9 us                                                | 24.3 us: 1.19x faster                                                     |
| logging_format          | 8.92 us                                                | 6.64 us: 1.34x faster                                                     |
| logging_silent          | 173 ns                                                 | 93.9 ns: 1.84x faster                                                     |
| logging_simple          | 8.06 us                                                | 6.01 us: 1.34x faster                                                     |
| mako                    | 14.3 ms                                                | 9.89 ms: 1.44x faster                                                     |
| mdp                     | 2.82 sec                                               | 2.65 sec: 1.07x faster                                                    |
| meteor_contest          | 114 ms                                                 | 106 ms: 1.08x faster                                                      |
| mypy                    | 1.01 sec                                               | 809 ms: 1.25x faster                                                      |
| nbody                   | 136 ms                                                 | 94.9 ms: 1.43x faster                                                     |
| nqueens                 | 99.3 ms                                                | 78.4 ms: 1.27x faster                                                     |
| pathlib                 | 20.0 ms                                                | 18.3 ms: 1.09x faster                                                     |
| pickle                  | 10.1 us                                                | 9.89 us: 1.02x faster                                                     |
| pickle_dict             | 28.3 us                                                | 30.2 us: 1.07x slower                                                     |
| pickle_list             | 4.50 us                                                | 4.15 us: 1.09x faster                                                     |
| pickle_pure_python      | 453 us                                                 | 288 us: 1.57x faster                                                      |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                      |
| pprint_safe_repr        | 943 ms                                                 | 676 ms: 1.40x faster                                                      |
| pprint_pformat          | 1.97 sec                                               | 1.40 sec: 1.41x faster                                                    |
| pycparser               | 1.51 sec                                               | 1.15 sec: 1.31x faster                                                    |
| pyflate                 | 675 ms                                                 | 409 ms: 1.65x faster                                                      |
| python_startup          | 13.9 ms                                                | 8.48 ms: 1.64x faster                                                     |
| python_startup_no_site  | 5.76 ms                                                | 6.07 ms: 1.05x slower                                                     |
| raytrace                | 461 ms                                                 | 291 ms: 1.58x faster                                                      |
| regex_compile           | 174 ms                                                 | 130 ms: 1.34x faster                                                      |
| regex_dna               | 214 ms                                                 | 209 ms: 1.03x faster                                                      |
| regex_effbot            | 3.21 ms                                                | 3.55 ms: 1.11x slower                                                     |
| regex_v8                | 25.0 ms                                                | 22.3 ms: 1.12x faster                                                     |
| richards                | 71.4 ms                                                | 46.0 ms: 1.55x faster                                                     |
| scimark_fft             | 414 ms                                                 | 319 ms: 1.30x faster                                                      |
| scimark_lu              | 158 ms                                                 | 108 ms: 1.46x faster                                                      |
| scimark_monte_carlo     | 105 ms                                                 | 65.1 ms: 1.61x faster                                                     |
| scimark_sor             | 193 ms                                                 | 107 ms: 1.81x faster                                                      |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.02 ms: 1.36x faster                                                     |
| spectral_norm           | 148 ms                                                 | 98.0 ms: 1.51x faster                                                     |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.44x faster                                                     |
| sqlglot_transpile       | 2.42 ms                                                | 1.71 ms: 1.41x faster                                                     |
| sqlglot_optimize        | 65.3 ms                                                | 51.6 ms: 1.27x faster                                                     |
| sqlglot_normalize       | 135 ms                                                 | 106 ms: 1.27x faster                                                      |
| sqlite_synth            | 2.90 us                                                | 2.58 us: 1.12x faster                                                     |
| sympy_expand            | 537 ms                                                 | 457 ms: 1.17x faster                                                      |
| sympy_integrate         | 23.9 ms                                                | 20.3 ms: 1.18x faster                                                     |
| sympy_sum               | 183 ms                                                 | 163 ms: 1.12x faster                                                      |
| sympy_str               | 324 ms                                                 | 281 ms: 1.15x faster                                                      |
| telco                   | 6.68 ms                                                | 6.28 ms: 1.06x faster                                                     |
| thrift                  | 1.03 ms                                                | 765 us: 1.35x faster                                                      |
| unpack_sequence         | 59.5 ns                                                | 42.9 ns: 1.39x faster                                                     |
| unpickle                | 14.3 us                                                | 13.7 us: 1.04x faster                                                     |
| unpickle_pure_python    | 297 us                                                 | 199 us: 1.49x faster                                                      |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                                      |
| xml_etree_iterparse     | 110 ms                                                 | 106 ms: 1.05x faster                                                      |
| xml_etree_generate      | 93.3 ms                                                | 77.1 ms: 1.21x faster                                                     |
| xml_etree_process       | 74.5 ms                                                | 53.9 ms: 1.38x faster                                                     |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                              |

Benchmark hidden because not significant (2): bench_mp_pool, unpickle_list
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230109-3.12.0a3+-78c9301/bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301.json: djangocms
