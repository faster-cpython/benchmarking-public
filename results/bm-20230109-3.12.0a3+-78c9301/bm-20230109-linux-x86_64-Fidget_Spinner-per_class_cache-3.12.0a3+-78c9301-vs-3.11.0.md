
# Results vs. 3.11.0

- fork: Fidget_Spinner
- ref: per_class_cache
- machine: linux-x86_64
- commit hash: 78c9301
- commit date: 2023-01-09
- overall geometric mean: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 254 ms: 1.02x faster                                                      |
| chameleon      | 6.41 ms                                                | 6.26 ms: 1.02x faster                                                     |
| docutils       | 2.60 sec                                               | 2.52 sec: 1.03x faster                                                    |
| html5lib       | 63.2 ms                                                | 60.3 ms: 1.05x faster                                                     |
| Geometric mean | (ref)                                                  | 1.03x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 76.3 ms                                                | 72.8 ms: 1.05x faster                                                     |
| pidigits       | 199 ms                                                 | 189 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                                              |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 130 ms: 1.05x faster                                                      |
| regex_dna      | 203 ms                                                 | 209 ms: 1.03x slower                                                      |
| regex_effbot   | 3.36 ms                                                | 3.55 ms: 1.06x slower                                                     |
| regex_v8       | 22.3 ms                                                | 22.3 ms: 1.00x slower                                                     |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.48 ms: 1.34x faster                                                     |
| json_loads           | 26.2 us                                                | 24.3 us: 1.08x faster                                                     |
| pickle               | 9.79 us                                                | 9.89 us: 1.01x slower                                                     |
| pickle_dict          | 31.4 us                                                | 30.2 us: 1.04x faster                                                     |
| pickle_list          | 4.17 us                                                | 4.15 us: 1.01x faster                                                     |
| pickle_pure_python   | 304 us                                                 | 288 us: 1.05x faster                                                      |
| unpickle             | 13.3 us                                                | 13.7 us: 1.03x slower                                                     |
| unpickle_pure_python | 225 us                                                 | 199 us: 1.13x faster                                                      |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.06x faster                                                      |
| xml_etree_iterparse  | 103 ms                                                 | 106 ms: 1.03x slower                                                      |
| xml_etree_generate   | 76.2 ms                                                | 77.1 ms: 1.01x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                              |

Benchmark hidden because not significant (2): unpickle_list, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.48 ms: 1.02x slower                                                     |
| python_startup_no_site | 5.96 ms                                                | 6.07 ms: 1.02x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text    | 22.1 ms                                                | 20.6 ms: 1.07x faster                                                     |
| genshi_xml     | 52.1 ms                                                | 46.7 ms: 1.11x faster                                                     |
| mako           | 9.85 ms                                                | 9.89 ms: 1.00x slower                                                     |
| Geometric mean | (ref)                                                  | 1.04x faster                                                              |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3                    | 257 ms                                                 | 254 ms: 1.02x faster                                                      |
| async_generators        | 359 ms                                                 | 356 ms: 1.01x faster                                                      |
| async_tree_cpu_io_mixed | 752 ms                                                 | 758 ms: 1.01x slower                                                      |
| async_tree_io           | 1.31 sec                                               | 1.33 sec: 1.02x slower                                                    |
| async_tree_memoization  | 625 ms                                                 | 670 ms: 1.07x slower                                                      |
| chameleon               | 6.41 ms                                                | 6.26 ms: 1.02x faster                                                     |
| chaos                   | 68.6 ms                                                | 67.5 ms: 1.02x faster                                                     |
| bench_thread_pool       | 810 us                                                 | 786 us: 1.03x faster                                                      |
| coroutines              | 26.1 ms                                                | 24.7 ms: 1.05x faster                                                     |
| coverage                | 101 ms                                                 | 96.9 ms: 1.04x faster                                                     |
| crypto_pyaes            | 73.9 ms                                                | 75.5 ms: 1.02x slower                                                     |
| deepcopy                | 344 us                                                 | 335 us: 1.03x faster                                                      |
| deepcopy_reduce         | 2.97 us                                                | 3.03 us: 1.02x slower                                                     |
| deepcopy_memo           | 36.4 us                                                | 34.7 us: 1.05x faster                                                     |
| deltablue               | 3.64 ms                                                | 3.71 ms: 1.02x slower                                                     |
| docutils                | 2.60 sec                                               | 2.52 sec: 1.03x faster                                                    |
| dulwich_log             | 63.9 ms                                                | 62.0 ms: 1.03x faster                                                     |
| fannkuch                | 388 ms                                                 | 375 ms: 1.03x faster                                                      |
| float                   | 76.3 ms                                                | 72.8 ms: 1.05x faster                                                     |
| generators              | 72.2 ms                                                | 77.4 ms: 1.07x slower                                                     |
| genshi_text             | 22.1 ms                                                | 20.6 ms: 1.07x faster                                                     |
| genshi_xml              | 52.1 ms                                                | 46.7 ms: 1.11x faster                                                     |
| go                      | 143 ms                                                 | 135 ms: 1.06x faster                                                      |
| hexiom                  | 6.35 ms                                                | 6.18 ms: 1.03x faster                                                     |
| html5lib                | 63.2 ms                                                | 60.3 ms: 1.05x faster                                                     |
| json                    | 4.95 ms                                                | 4.63 ms: 1.07x faster                                                     |
| json_dumps              | 12.7 ms                                                | 9.48 ms: 1.34x faster                                                     |
| json_loads              | 26.2 us                                                | 24.3 us: 1.08x faster                                                     |
| logging_silent          | 98.5 ns                                                | 93.9 ns: 1.05x faster                                                     |
| logging_simple          | 6.06 us                                                | 6.01 us: 1.01x faster                                                     |
| mako                    | 9.85 ms                                                | 9.89 ms: 1.00x slower                                                     |
| mdp                     | 2.62 sec                                               | 2.65 sec: 1.01x slower                                                    |
| mypy                    | 669 ms                                                 | 809 ms: 1.21x slower                                                      |
| nqueens                 | 85.0 ms                                                | 78.4 ms: 1.09x faster                                                     |
| pathlib                 | 18.2 ms                                                | 18.3 ms: 1.01x slower                                                     |
| pickle                  | 9.79 us                                                | 9.89 us: 1.01x slower                                                     |
| pickle_dict             | 31.4 us                                                | 30.2 us: 1.04x faster                                                     |
| pickle_list             | 4.17 us                                                | 4.15 us: 1.01x faster                                                     |
| pickle_pure_python      | 304 us                                                 | 288 us: 1.05x faster                                                      |
| pidigits                | 199 ms                                                 | 189 ms: 1.05x faster                                                      |
| pprint_safe_repr        | 691 ms                                                 | 676 ms: 1.02x faster                                                      |
| pprint_pformat          | 1.44 sec                                               | 1.40 sec: 1.03x faster                                                    |
| pycparser               | 1.17 sec                                               | 1.15 sec: 1.02x faster                                                    |
| pyflate                 | 417 ms                                                 | 409 ms: 1.02x faster                                                      |
| python_startup          | 8.36 ms                                                | 8.48 ms: 1.02x slower                                                     |
| python_startup_no_site  | 5.96 ms                                                | 6.07 ms: 1.02x slower                                                     |
| regex_compile           | 136 ms                                                 | 130 ms: 1.05x faster                                                      |
| regex_dna               | 203 ms                                                 | 209 ms: 1.03x slower                                                      |
| regex_effbot            | 3.36 ms                                                | 3.55 ms: 1.06x slower                                                     |
| regex_v8                | 22.3 ms                                                | 22.3 ms: 1.00x slower                                                     |
| scimark_fft             | 329 ms                                                 | 319 ms: 1.03x faster                                                      |
| scimark_monte_carlo     | 68.3 ms                                                | 65.1 ms: 1.05x faster                                                     |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.08x faster                                                      |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.02 ms: 1.10x faster                                                     |
| spectral_norm           | 99.9 ms                                                | 98.0 ms: 1.02x faster                                                     |
| sqlglot_parse           | 1.37 ms                                                | 1.41 ms: 1.03x slower                                                     |
| sqlglot_transpile       | 1.66 ms                                                | 1.71 ms: 1.03x slower                                                     |
| sqlglot_optimize        | 53.0 ms                                                | 51.6 ms: 1.03x faster                                                     |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.02x faster                                                      |
| sqlite_synth            | 2.49 us                                                | 2.58 us: 1.04x slower                                                     |
| sympy_expand            | 472 ms                                                 | 457 ms: 1.03x faster                                                      |
| sympy_integrate         | 20.9 ms                                                | 20.3 ms: 1.03x faster                                                     |
| sympy_sum               | 166 ms                                                 | 163 ms: 1.02x faster                                                      |
| sympy_str               | 287 ms                                                 | 281 ms: 1.02x faster                                                      |
| telco                   | 6.62 ms                                                | 6.28 ms: 1.05x faster                                                     |
| thrift                  | 752 us                                                 | 765 us: 1.02x slower                                                      |
| unpack_sequence         | 43.4 ns                                                | 42.9 ns: 1.01x faster                                                     |
| unpickle                | 13.3 us                                                | 13.7 us: 1.03x slower                                                     |
| unpickle_pure_python    | 225 us                                                 | 199 us: 1.13x faster                                                      |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.06x faster                                                      |
| xml_etree_iterparse     | 103 ms                                                 | 106 ms: 1.03x slower                                                      |
| xml_etree_generate      | 76.2 ms                                                | 77.1 ms: 1.01x slower                                                     |
| Geometric mean          | (ref)                                                  | 1.02x faster                                                              |

Benchmark hidden because not significant (11): async_tree_none, bench_mp_pool, django_template, logging_format, meteor_contest, nbody, raytrace, richards, scimark_lu, unpickle_list, xml_etree_process
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230109-3.12.0a3+-78c9301/bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301.json: djangocms
