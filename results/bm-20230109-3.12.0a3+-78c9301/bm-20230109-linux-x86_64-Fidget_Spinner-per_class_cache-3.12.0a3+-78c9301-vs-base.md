
# Results vs. base

- fork: Fidget_Spinner
- ref: per_class_cache
- machine: linux-x86_64
- commit hash: 78c9301
- commit date: 2023-01-09
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230107-linux-x86_64-python-7116030a25f7dd2140ef-3.12.0a3+-7116030 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                                 | 254 ms: 1.00x slower                                                      |
| chameleon      | 6.38 ms                                                                | 6.26 ms: 1.02x faster                                                     |
| docutils       | 2.51 sec                                                               | 2.52 sec: 1.00x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230107-linux-x86_64-python-7116030a25f7dd2140ef-3.12.0a3+-7116030 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 71.8 ms                                                                | 72.8 ms: 1.01x slower                                                     |
| pidigits       | 198 ms                                                                 | 189 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230107-linux-x86_64-python-7116030a25f7dd2140ef-3.12.0a3+-7116030 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 133 ms                                                                 | 130 ms: 1.03x faster                                                      |
| regex_dna      | 208 ms                                                                 | 209 ms: 1.00x slower                                                      |
| regex_effbot   | 3.52 ms                                                                | 3.55 ms: 1.01x slower                                                     |
| regex_v8       | 21.7 ms                                                                | 22.3 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20230107-linux-x86_64-python-7116030a25f7dd2140ef-3.12.0a3+-7116030 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|--------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps         | 9.34 ms                                                                | 9.48 ms: 1.02x slower                                                     |
| json_loads         | 24.1 us                                                                | 24.3 us: 1.01x slower                                                     |
| pickle             | 10.2 us                                                                | 9.89 us: 1.03x faster                                                     |
| pickle_dict        | 29.9 us                                                                | 30.2 us: 1.01x slower                                                     |
| pickle_list        | 3.93 us                                                                | 4.15 us: 1.06x slower                                                     |
| pickle_pure_python | 286 us                                                                 | 288 us: 1.01x slower                                                      |
| unpickle           | 13.2 us                                                                | 13.7 us: 1.04x slower                                                     |
| xml_etree_parse    | 147 ms                                                                 | 149 ms: 1.01x slower                                                      |
| xml_etree_generate | 75.8 ms                                                                | 77.1 ms: 1.02x slower                                                     |
| xml_etree_process  | 53.5 ms                                                                | 53.9 ms: 1.01x slower                                                     |
| Geometric mean     | (ref)                                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (3): unpickle_list, unpickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230107-linux-x86_64-python-7116030a25f7dd2140ef-3.12.0a3+-7116030 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 8.47 ms                                                                | 8.48 ms: 1.00x slower                                                     |
| python_startup_no_site | 6.06 ms                                                                | 6.07 ms: 1.00x slower                                                     |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230107-linux-x86_64-python-7116030a25f7dd2140ef-3.12.0a3+-7116030 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 32.1 ms                                                                | 32.5 ms: 1.01x slower                                                     |
| genshi_text     | 20.3 ms                                                                | 20.6 ms: 1.02x slower                                                     |
| mako            | 9.81 ms                                                                | 9.89 ms: 1.01x slower                                                     |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20230107-linux-x86_64-python-7116030a25f7dd2140ef-3.12.0a3+-7116030 | bm-20230109-linux-x86_64-Fidget_Spinner-per_class_cache-3.12.0a3+-78c9301 |
|-------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3                    | 253 ms                                                                 | 254 ms: 1.00x slower                                                      |
| async_tree_io           | 1.32 sec                                                               | 1.33 sec: 1.01x slower                                                    |
| chameleon               | 6.38 ms                                                                | 6.26 ms: 1.02x faster                                                     |
| chaos                   | 67.3 ms                                                                | 67.5 ms: 1.00x slower                                                     |
| bench_thread_pool       | 778 us                                                                 | 786 us: 1.01x slower                                                      |
| coverage                | 100 ms                                                                 | 96.9 ms: 1.03x faster                                                     |
| crypto_pyaes            | 75.0 ms                                                                | 75.5 ms: 1.01x slower                                                     |
| deepcopy                | 339 us                                                                 | 335 us: 1.01x faster                                                      |
| deepcopy_reduce         | 2.95 us                                                                | 3.03 us: 1.02x slower                                                     |
| deepcopy_memo           | 34.2 us                                                                | 34.7 us: 1.02x slower                                                     |
| deltablue               | 3.27 ms                                                                | 3.71 ms: 1.14x slower                                                     |
| django_template         | 32.1 ms                                                                | 32.5 ms: 1.01x slower                                                     |
| docutils                | 2.51 sec                                                               | 2.52 sec: 1.00x slower                                                    |
| dulwich_log             | 62.5 ms                                                                | 62.0 ms: 1.01x faster                                                     |
| fannkuch                | 371 ms                                                                 | 375 ms: 1.01x slower                                                      |
| float                   | 71.8 ms                                                                | 72.8 ms: 1.01x slower                                                     |
| generators              | 76.1 ms                                                                | 77.4 ms: 1.02x slower                                                     |
| genshi_text             | 20.3 ms                                                                | 20.6 ms: 1.02x slower                                                     |
| go                      | 134 ms                                                                 | 135 ms: 1.01x slower                                                      |
| hexiom                  | 6.12 ms                                                                | 6.18 ms: 1.01x slower                                                     |
| json_dumps              | 9.34 ms                                                                | 9.48 ms: 1.02x slower                                                     |
| json_loads              | 24.1 us                                                                | 24.3 us: 1.01x slower                                                     |
| logging_format          | 6.31 us                                                                | 6.64 us: 1.05x slower                                                     |
| logging_simple          | 5.70 us                                                                | 6.01 us: 1.05x slower                                                     |
| mako                    | 9.81 ms                                                                | 9.89 ms: 1.01x slower                                                     |
| mdp                     | 2.72 sec                                                               | 2.65 sec: 1.03x faster                                                    |
| meteor_contest          | 104 ms                                                                 | 106 ms: 1.02x slower                                                      |
| nqueens                 | 78.7 ms                                                                | 78.4 ms: 1.00x faster                                                     |
| pickle                  | 10.2 us                                                                | 9.89 us: 1.03x faster                                                     |
| pickle_dict             | 29.9 us                                                                | 30.2 us: 1.01x slower                                                     |
| pickle_list             | 3.93 us                                                                | 4.15 us: 1.06x slower                                                     |
| pickle_pure_python      | 286 us                                                                 | 288 us: 1.01x slower                                                      |
| pidigits                | 198 ms                                                                 | 189 ms: 1.04x faster                                                      |
| pycparser               | 1.14 sec                                                               | 1.15 sec: 1.01x slower                                                    |
| pyflate                 | 394 ms                                                                 | 409 ms: 1.04x slower                                                      |
| python_startup          | 8.47 ms                                                                | 8.48 ms: 1.00x slower                                                     |
| python_startup_no_site  | 6.06 ms                                                                | 6.07 ms: 1.00x slower                                                     |
| raytrace                | 286 ms                                                                 | 291 ms: 1.02x slower                                                      |
| regex_compile           | 133 ms                                                                 | 130 ms: 1.03x faster                                                      |
| regex_dna               | 208 ms                                                                 | 209 ms: 1.00x slower                                                      |
| regex_effbot            | 3.52 ms                                                                | 3.55 ms: 1.01x slower                                                     |
| regex_v8                | 21.7 ms                                                                | 22.3 ms: 1.03x slower                                                     |
| richards                | 42.1 ms                                                                | 46.0 ms: 1.09x slower                                                     |
| scimark_fft             | 314 ms                                                                 | 319 ms: 1.02x slower                                                      |
| scimark_lu              | 107 ms                                                                 | 108 ms: 1.02x slower                                                      |
| scimark_monte_carlo     | 64.5 ms                                                                | 65.1 ms: 1.01x slower                                                     |
| scimark_sparse_mat_mult | 4.15 ms                                                                | 4.02 ms: 1.03x faster                                                     |
| spectral_norm           | 95.7 ms                                                                | 98.0 ms: 1.02x slower                                                     |
| sqlglot_parse           | 1.40 ms                                                                | 1.41 ms: 1.01x slower                                                     |
| sqlglot_transpile       | 1.69 ms                                                                | 1.71 ms: 1.01x slower                                                     |
| sqlglot_optimize        | 50.6 ms                                                                | 51.6 ms: 1.02x slower                                                     |
| sqlglot_normalize       | 104 ms                                                                 | 106 ms: 1.02x slower                                                      |
| sympy_integrate         | 20.4 ms                                                                | 20.3 ms: 1.01x faster                                                     |
| sympy_sum               | 164 ms                                                                 | 163 ms: 1.00x faster                                                      |
| sympy_str               | 283 ms                                                                 | 281 ms: 1.01x faster                                                      |
| thrift                  | 744 us                                                                 | 765 us: 1.03x slower                                                      |
| unpack_sequence         | 41.8 ns                                                                | 42.9 ns: 1.03x slower                                                     |
| unpickle                | 13.2 us                                                                | 13.7 us: 1.04x slower                                                     |
| xml_etree_parse         | 147 ms                                                                 | 149 ms: 1.01x slower                                                      |
| xml_etree_generate      | 75.8 ms                                                                | 77.1 ms: 1.02x slower                                                     |
| xml_etree_process       | 53.5 ms                                                                | 53.9 ms: 1.01x slower                                                     |
| Geometric mean          | (ref)                                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (23): async_generators, async_tree_none, async_tree_cpu_io_mixed, async_tree_memoization, bench_mp_pool, coroutines, djangocms, genshi_xml, html5lib, json, logging_silent, mypy, nbody, pathlib, pprint_safe_repr, pprint_pformat, scimark_sor, sqlite_synth, sympy_expand, telco, unpickle_list, unpickle_pure_python, xml_etree_iterparse
