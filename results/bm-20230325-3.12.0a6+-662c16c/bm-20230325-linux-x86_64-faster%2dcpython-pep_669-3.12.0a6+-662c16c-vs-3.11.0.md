
# Results vs. 3.11.0

- fork: faster-cpython
- ref: pep_669
- machine: linux-x86_64
- commit hash: 662c16c
- commit date: 2023-03-25
- overall geometric mean: 1.06x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230325-linux-x86_64-faster%2dcpython-pep_669-3.12.0a6+-662c16c |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 247 ms: 1.05x faster                                                |
| chameleon      | 6.47 ms                                                | 6.20 ms: 1.04x faster                                               |
| docutils       | 2.63 sec                                               | 2.51 sec: 1.05x faster                                              |
| html5lib       | 64.5 ms                                                | 60.5 ms: 1.07x faster                                               |
| tornado_http   | 96.3 ms                                                | 90.0 ms: 1.07x faster                                               |
| Geometric mean | (ref)                                                  | 1.06x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230325-linux-x86_64-faster%2dcpython-pep_669-3.12.0a6+-662c16c |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 84.3 ms: 1.10x faster                                               |
| float          | 77.2 ms                                                | 71.2 ms: 1.09x faster                                               |
| pidigits       | 198 ms                                                 | 188 ms: 1.05x faster                                                |
| Geometric mean | (ref)                                                  | 1.08x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230325-linux-x86_64-faster%2dcpython-pep_669-3.12.0a6+-662c16c |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.47 ms: 1.15x faster                                               |
| regex_compile  | 138 ms                                                 | 129 ms: 1.07x faster                                                |
| regex_dna      | 204 ms                                                 | 203 ms: 1.00x faster                                                |
| regex_v8       | 22.0 ms                                                | 22.2 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                  | 1.05x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230325-linux-x86_64-faster%2dcpython-pep_669-3.12.0a6+-662c16c |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.53 ms: 1.32x faster                                               |
| unpickle_pure_python | 228 us                                                 | 197 us: 1.15x faster                                                |
| json_loads           | 26.5 us                                                | 24.0 us: 1.10x faster                                               |
| pickle_pure_python   | 306 us                                                 | 282 us: 1.09x faster                                                |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                |
| xml_etree_iterparse  | 104 ms                                                 | 99.1 ms: 1.05x faster                                               |
| pickle_dict          | 31.1 us                                                | 30.6 us: 1.02x faster                                               |
| unpickle_list        | 4.91 us                                                | 4.94 us: 1.01x slower                                               |
| xml_etree_process    | 53.9 ms                                                | 54.8 ms: 1.02x slower                                               |
| pickle               | 10.1 us                                                | 10.3 us: 1.02x slower                                               |
| pickle_list          | 4.11 us                                                | 4.22 us: 1.03x slower                                               |
| unpickle             | 13.7 us                                                | 14.1 us: 1.03x slower                                               |
| xml_etree_generate   | 76.2 ms                                                | 79.2 ms: 1.04x slower                                               |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230325-linux-x86_64-faster%2dcpython-pep_669-3.12.0a6+-662c16c |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.86 ms: 1.04x slower                                               |
| python_startup_no_site | 6.01 ms                                                | 6.57 ms: 1.09x slower                                               |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230325-linux-x86_64-faster%2dcpython-pep_669-3.12.0a6+-662c16c |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml     | 51.8 ms                                                | 46.0 ms: 1.13x faster                                               |
| genshi_text    | 21.6 ms                                                | 20.4 ms: 1.06x faster                                               |
| mako           | 10.1 ms                                                | 9.85 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                  | 1.05x faster                                                        |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230325-linux-x86_64-faster%2dcpython-pep_669-3.12.0a6+-662c16c |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 27.5 ms: 2.67x faster                                               |
| asyncio_tcp             | 922 ms                                                 | 501 ms: 1.84x faster                                                |
| json_dumps              | 12.6 ms                                                | 9.53 ms: 1.32x faster                                               |
| mypy2                   | 420 ms                                                 | 326 ms: 1.29x faster                                                |
| deltablue               | 3.67 ms                                                | 3.15 ms: 1.16x faster                                               |
| unpickle_pure_python    | 228 us                                                 | 197 us: 1.15x faster                                                |
| coroutines              | 25.5 ms                                                | 22.1 ms: 1.15x faster                                               |
| regex_effbot            | 3.99 ms                                                | 3.47 ms: 1.15x faster                                               |
| spectral_norm           | 100 ms                                                 | 88.8 ms: 1.13x faster                                               |
| genshi_xml              | 51.8 ms                                                | 46.0 ms: 1.13x faster                                               |
| deepcopy_memo           | 37.0 us                                                | 33.3 us: 1.11x faster                                               |
| aiohttp                 | 1.10 ms                                                | 991 us: 1.11x faster                                                |
| gc_traversal            | 4.02 ms                                                | 3.64 ms: 1.11x faster                                               |
| nbody                   | 93.1 ms                                                | 84.3 ms: 1.10x faster                                               |
| json_loads              | 26.5 us                                                | 24.0 us: 1.10x faster                                               |
| gunicorn                | 1.18 ms                                                | 1.07 ms: 1.10x faster                                               |
| logging_silent          | 101 ns                                                 | 92.5 ns: 1.09x faster                                               |
| scimark_sor             | 118 ms                                                 | 108 ms: 1.09x faster                                                |
| float                   | 77.2 ms                                                | 71.2 ms: 1.09x faster                                               |
| pickle_pure_python      | 306 us                                                 | 282 us: 1.09x faster                                                |
| hexiom                  | 6.37 ms                                                | 5.90 ms: 1.08x faster                                               |
| richards                | 45.7 ms                                                | 42.4 ms: 1.08x faster                                               |
| scimark_fft             | 328 ms                                                 | 306 ms: 1.07x faster                                                |
| json                    | 4.94 ms                                                | 4.61 ms: 1.07x faster                                               |
| logging_format          | 6.68 us                                                | 6.23 us: 1.07x faster                                               |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                |
| deepcopy                | 342 us                                                 | 319 us: 1.07x faster                                                |
| regex_compile           | 138 ms                                                 | 129 ms: 1.07x faster                                                |
| tornado_http            | 96.3 ms                                                | 90.0 ms: 1.07x faster                                               |
| html5lib                | 64.5 ms                                                | 60.5 ms: 1.07x faster                                               |
| raytrace                | 297 ms                                                 | 278 ms: 1.07x faster                                                |
| logging_simple          | 6.03 us                                                | 5.68 us: 1.06x faster                                               |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.24 ms: 1.06x faster                                               |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.06x faster                                              |
| sympy_expand            | 475 ms                                                 | 449 ms: 1.06x faster                                                |
| genshi_text             | 21.6 ms                                                | 20.4 ms: 1.06x faster                                               |
| mdp                     | 2.62 sec                                               | 2.48 sec: 1.05x faster                                              |
| sqlglot_optimize        | 53.1 ms                                                | 50.4 ms: 1.05x faster                                               |
| pidigits                | 198 ms                                                 | 188 ms: 1.05x faster                                                |
| bench_thread_pool       | 819 us                                                 | 779 us: 1.05x faster                                                |
| sympy_integrate         | 21.0 ms                                                | 20.0 ms: 1.05x faster                                               |
| xml_etree_iterparse     | 104 ms                                                 | 99.1 ms: 1.05x faster                                               |
| 2to3                    | 259 ms                                                 | 247 ms: 1.05x faster                                                |
| docutils                | 2.63 sec                                               | 2.51 sec: 1.05x faster                                              |
| sympy_str               | 290 ms                                                 | 277 ms: 1.05x faster                                                |
| pathlib                 | 18.2 ms                                                | 17.4 ms: 1.05x faster                                               |
| sqlalchemy_imperative   | 17.9 ms                                                | 17.1 ms: 1.04x faster                                               |
| chameleon               | 6.47 ms                                                | 6.20 ms: 1.04x faster                                               |
| pycparser               | 1.18 sec                                               | 1.13 sec: 1.04x faster                                              |
| scimark_monte_carlo     | 68.1 ms                                                | 65.2 ms: 1.04x faster                                               |
| pprint_safe_repr        | 701 ms                                                 | 673 ms: 1.04x faster                                                |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                                |
| nqueens                 | 83.4 ms                                                | 80.1 ms: 1.04x faster                                               |
| chaos                   | 69.2 ms                                                | 66.6 ms: 1.04x faster                                               |
| sqlalchemy_declarative  | 138 ms                                                 | 133 ms: 1.04x faster                                                |
| coverage                | 100 ms                                                 | 96.7 ms: 1.03x faster                                               |
| meteor_contest          | 107 ms                                                 | 103 ms: 1.03x faster                                                |
| pyflate                 | 418 ms                                                 | 406 ms: 1.03x faster                                                |
| sympy_sum               | 167 ms                                                 | 162 ms: 1.03x faster                                                |
| telco                   | 6.58 ms                                                | 6.41 ms: 1.03x faster                                               |
| crypto_pyaes            | 74.7 ms                                                | 72.7 ms: 1.03x faster                                               |
| dulwich_log             | 63.7 ms                                                | 62.1 ms: 1.03x faster                                               |
| mako                    | 10.1 ms                                                | 9.85 ms: 1.02x faster                                               |
| scimark_lu              | 110 ms                                                 | 108 ms: 1.02x faster                                                |
| go                      | 140 ms                                                 | 137 ms: 1.02x faster                                                |
| fannkuch                | 388 ms                                                 | 381 ms: 1.02x faster                                                |
| pickle_dict             | 31.1 us                                                | 30.6 us: 1.02x faster                                               |
| async_tree_io           | 1.30 sec                                               | 1.28 sec: 1.02x faster                                              |
| deepcopy_reduce         | 2.94 us                                                | 2.90 us: 1.01x faster                                               |
| sqlglot_transpile       | 1.70 ms                                                | 1.68 ms: 1.01x faster                                               |
| async_tree_none         | 526 ms                                                 | 520 ms: 1.01x faster                                                |
| async_tree_cpu_io_mixed | 739 ms                                                 | 731 ms: 1.01x faster                                                |
| create_gc_cycles        | 1.49 ms                                                | 1.47 ms: 1.01x faster                                               |
| regex_dna               | 204 ms                                                 | 203 ms: 1.00x faster                                                |
| sqlglot_parse           | 1.40 ms                                                | 1.40 ms: 1.00x faster                                               |
| unpickle_list           | 4.91 us                                                | 4.94 us: 1.01x slower                                               |
| regex_v8                | 22.0 ms                                                | 22.2 ms: 1.01x slower                                               |
| xml_etree_process       | 53.9 ms                                                | 54.8 ms: 1.02x slower                                               |
| pickle                  | 10.1 us                                                | 10.3 us: 1.02x slower                                               |
| pickle_list             | 4.11 us                                                | 4.22 us: 1.03x slower                                               |
| unpickle                | 13.7 us                                                | 14.1 us: 1.03x slower                                               |
| thrift                  | 756 us                                                 | 784 us: 1.04x slower                                                |
| sqlite_synth            | 2.52 us                                                | 2.62 us: 1.04x slower                                               |
| xml_etree_generate      | 76.2 ms                                                | 79.2 ms: 1.04x slower                                               |
| python_startup          | 8.52 ms                                                | 8.86 ms: 1.04x slower                                               |
| comprehensions          | 22.4 us                                                | 23.3 us: 1.04x slower                                               |
| python_startup_no_site  | 6.01 ms                                                | 6.57 ms: 1.09x slower                                               |
| async_generators        | 368 ms                                                 | 422 ms: 1.14x slower                                                |
| dask                    | 360 ms                                                 | 490 ms: 1.36x slower                                                |
| Geometric mean          | (ref)                                                  | 1.06x faster                                                        |

Benchmark hidden because not significant (5): async_tree_memoization, djangocms, bench_mp_pool, unpack_sequence, django_template
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x
