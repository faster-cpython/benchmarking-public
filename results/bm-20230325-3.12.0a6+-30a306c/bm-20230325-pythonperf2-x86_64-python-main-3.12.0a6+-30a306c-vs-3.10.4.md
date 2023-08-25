
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 30a306c
- commit date: 2023-03-25
- overall geometric mean: 1.26x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-pythonperf2-x86_64-python-main-3.12.0a6+-30a306c |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 285 ms: 1.23x faster                                         |
| chameleon      | 9.72 ms                                                      | 7.46 ms: 1.30x faster                                        |
| docutils       | 3.40 sec                                                     | 2.81 sec: 1.21x faster                                       |
| html5lib       | 94.6 ms                                                      | 68.9 ms: 1.37x faster                                        |
| tornado_http   | 152 ms                                                       | 114 ms: 1.34x faster                                         |
| Geometric mean | (ref)                                                        | 1.29x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-pythonperf2-x86_64-python-main-3.12.0a6+-30a306c |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 84.6 ms: 1.62x faster                                        |
| float          | 110 ms                                                       | 71.4 ms: 1.54x faster                                        |
| pidigits       | 271 ms                                                       | 261 ms: 1.04x faster                                         |
| Geometric mean | (ref)                                                        | 1.38x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-pythonperf2-x86_64-python-main-3.12.0a6+-30a306c |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 147 ms: 1.32x faster                                         |
| regex_v8       | 26.6 ms                                                      | 23.2 ms: 1.15x faster                                        |
| regex_dna      | 259 ms                                                       | 235 ms: 1.10x faster                                         |
| regex_effbot   | 2.99 ms                                                      | 3.43 ms: 1.15x slower                                        |
| Geometric mean | (ref)                                                        | 1.10x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-pythonperf2-x86_64-python-main-3.12.0a6+-30a306c |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 206 us: 1.56x faster                                         |
| pickle_pure_python   | 457 us                                                       | 318 us: 1.44x faster                                         |
| json_dumps           | 14.2 ms                                                      | 10.2 ms: 1.39x faster                                        |
| xml_etree_process    | 76.0 ms                                                      | 57.5 ms: 1.32x faster                                        |
| json_loads           | 30.0 us                                                      | 24.2 us: 1.24x faster                                        |
| xml_etree_parse      | 162 ms                                                       | 142 ms: 1.14x faster                                         |
| xml_etree_generate   | 94.6 ms                                                      | 83.6 ms: 1.13x faster                                        |
| pickle_list          | 4.11 us                                                      | 3.75 us: 1.10x faster                                        |
| xml_etree_iterparse  | 110 ms                                                       | 102 ms: 1.08x faster                                         |
| unpickle             | 14.2 us                                                      | 13.4 us: 1.05x faster                                        |
| unpickle_list        | 4.49 us                                                      | 4.54 us: 1.01x slower                                        |
| pickle               | 9.94 us                                                      | 10.1 us: 1.02x slower                                        |
| pickle_dict          | 30.0 us                                                      | 31.8 us: 1.06x slower                                        |
| Geometric mean       | (ref)                                                        | 1.17x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-pythonperf2-x86_64-python-main-3.12.0a6+-30a306c |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.0 ms: 1.04x faster                                        |
| python_startup_no_site | 7.32 ms                                                      | 8.32 ms: 1.14x slower                                        |
| Geometric mean         | (ref)                                                        | 1.05x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-pythonperf2-x86_64-python-main-3.12.0a6+-30a306c |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.0 ms: 1.46x faster                                        |
| django_template | 51.5 ms                                                      | 40.8 ms: 1.26x faster                                        |
| genshi_text     | 31.5 ms                                                      | 25.2 ms: 1.25x faster                                        |
| genshi_xml      | 64.7 ms                                                      | 55.3 ms: 1.17x faster                                        |
| Geometric mean  | (ref)                                                        | 1.28x faster                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-pythonperf2-x86_64-python-main-3.12.0a6+-30a306c |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| deltablue               | 7.47 ms                                                      | 3.44 ms: 2.17x faster                                        |
| asyncio_tcp             | 782 ms                                                       | 387 ms: 2.02x faster                                         |
| logging_silent          | 166 ns                                                       | 97.9 ns: 1.69x faster                                        |
| raytrace                | 488 ms                                                       | 290 ms: 1.68x faster                                         |
| nbody                   | 137 ms                                                       | 84.6 ms: 1.62x faster                                        |
| scimark_lu              | 164 ms                                                       | 101 ms: 1.62x faster                                         |
| go                      | 259 ms                                                       | 162 ms: 1.60x faster                                         |
| scimark_sor             | 177 ms                                                       | 111 ms: 1.60x faster                                         |
| scimark_monte_carlo     | 109 ms                                                       | 69.1 ms: 1.58x faster                                        |
| richards                | 74.1 ms                                                      | 46.9 ms: 1.58x faster                                        |
| pyflate                 | 697 ms                                                       | 446 ms: 1.56x faster                                         |
| unpickle_pure_python    | 321 us                                                       | 206 us: 1.56x faster                                         |
| float                   | 110 ms                                                       | 71.4 ms: 1.54x faster                                        |
| generators              | 58.0 ms                                                      | 37.9 ms: 1.53x faster                                        |
| chaos                   | 107 ms                                                       | 71.5 ms: 1.50x faster                                        |
| spectral_norm           | 136 ms                                                       | 92.1 ms: 1.48x faster                                        |
| bench_mp_pool           | 7.18 ms                                                      | 4.86 ms: 1.48x faster                                        |
| hexiom                  | 9.52 ms                                                      | 6.50 ms: 1.46x faster                                        |
| mako                    | 14.7 ms                                                      | 10.0 ms: 1.46x faster                                        |
| sqlglot_parse           | 2.26 ms                                                      | 1.55 ms: 1.45x faster                                        |
| pickle_pure_python      | 457 us                                                       | 318 us: 1.44x faster                                         |
| crypto_pyaes            | 118 ms                                                       | 83.6 ms: 1.41x faster                                        |
| deepcopy_memo           | 48.9 us                                                      | 34.6 us: 1.41x faster                                        |
| sqlglot_transpile       | 2.71 ms                                                      | 1.92 ms: 1.41x faster                                        |
| json_dumps              | 14.2 ms                                                      | 10.2 ms: 1.39x faster                                        |
| async_tree_io           | 1.61 sec                                                     | 1.16 sec: 1.38x faster                                       |
| html5lib                | 94.6 ms                                                      | 68.9 ms: 1.37x faster                                        |
| async_tree_none         | 700 ms                                                       | 510 ms: 1.37x faster                                         |
| pprint_safe_repr        | 1.05 sec                                                     | 767 ms: 1.37x faster                                         |
| pprint_pformat          | 2.15 sec                                                     | 1.58 sec: 1.36x faster                                       |
| unpack_sequence         | 59.5 ns                                                      | 43.8 ns: 1.36x faster                                        |
| async_tree_memoization  | 824 ms                                                       | 607 ms: 1.36x faster                                         |
| pycparser               | 1.66 sec                                                     | 1.23 sec: 1.36x faster                                       |
| scimark_sparse_mat_mult | 5.19 ms                                                      | 3.83 ms: 1.36x faster                                        |
| tornado_http            | 152 ms                                                       | 114 ms: 1.34x faster                                         |
| xml_etree_process       | 76.0 ms                                                      | 57.5 ms: 1.32x faster                                        |
| regex_compile           | 194 ms                                                       | 147 ms: 1.32x faster                                         |
| scimark_fft             | 359 ms                                                       | 274 ms: 1.31x faster                                         |
| chameleon               | 9.72 ms                                                      | 7.46 ms: 1.30x faster                                        |
| async_tree_cpu_io_mixed | 952 ms                                                       | 741 ms: 1.28x faster                                         |
| thrift                  | 1.16 ms                                                      | 919 us: 1.27x faster                                         |
| logging_simple          | 8.90 us                                                      | 7.04 us: 1.26x faster                                        |
| django_template         | 51.5 ms                                                      | 40.8 ms: 1.26x faster                                        |
| logging_format          | 9.57 us                                                      | 7.62 us: 1.25x faster                                        |
| genshi_text             | 31.5 ms                                                      | 25.2 ms: 1.25x faster                                        |
| json_loads              | 30.0 us                                                      | 24.2 us: 1.24x faster                                        |
| mypy2                   | 466 ms                                                       | 379 ms: 1.23x faster                                         |
| 2to3                    | 350 ms                                                       | 285 ms: 1.23x faster                                         |
| coroutines              | 30.4 ms                                                      | 24.8 ms: 1.23x faster                                        |
| dulwich_log             | 80.1 ms                                                      | 65.7 ms: 1.22x faster                                        |
| docutils                | 3.40 sec                                                     | 2.81 sec: 1.21x faster                                       |
| sqlglot_optimize        | 70.3 ms                                                      | 58.4 ms: 1.20x faster                                        |
| mdp                     | 3.03 sec                                                     | 2.53 sec: 1.20x faster                                       |
| deepcopy                | 454 us                                                       | 380 us: 1.19x faster                                         |
| sqlglot_normalize       | 144 ms                                                       | 121 ms: 1.19x faster                                         |
| json                    | 5.96 ms                                                      | 5.03 ms: 1.18x faster                                        |
| deepcopy_reduce         | 4.03 us                                                      | 3.42 us: 1.18x faster                                        |
| bench_thread_pool       | 1.14 ms                                                      | 966 us: 1.18x faster                                         |
| genshi_xml              | 64.7 ms                                                      | 55.3 ms: 1.17x faster                                        |
| pathlib                 | 21.7 ms                                                      | 18.7 ms: 1.16x faster                                        |
| nqueens                 | 112 ms                                                       | 97.0 ms: 1.16x faster                                        |
| regex_v8                | 26.6 ms                                                      | 23.2 ms: 1.15x faster                                        |
| xml_etree_parse         | 162 ms                                                       | 142 ms: 1.14x faster                                         |
| xml_etree_generate      | 94.6 ms                                                      | 83.6 ms: 1.13x faster                                        |
| sqlite_synth            | 2.97 us                                                      | 2.63 us: 1.13x faster                                        |
| create_gc_cycles        | 1.82 ms                                                      | 1.62 ms: 1.12x faster                                        |
| fannkuch                | 496 ms                                                       | 442 ms: 1.12x faster                                         |
| async_generators        | 422 ms                                                       | 377 ms: 1.12x faster                                         |
| sympy_integrate         | 28.1 ms                                                      | 25.2 ms: 1.12x faster                                        |
| sympy_expand            | 599 ms                                                       | 538 ms: 1.11x faster                                         |
| regex_dna               | 259 ms                                                       | 235 ms: 1.10x faster                                         |
| pickle_list             | 4.11 us                                                      | 3.75 us: 1.10x faster                                        |
| xml_etree_iterparse     | 110 ms                                                       | 102 ms: 1.08x faster                                         |
| sympy_str               | 358 ms                                                       | 330 ms: 1.08x faster                                         |
| meteor_contest          | 137 ms                                                       | 129 ms: 1.06x faster                                         |
| unpickle                | 14.2 us                                                      | 13.4 us: 1.05x faster                                        |
| telco                   | 7.14 ms                                                      | 6.78 ms: 1.05x faster                                        |
| sympy_sum               | 193 ms                                                       | 185 ms: 1.04x faster                                         |
| python_startup          | 11.5 ms                                                      | 11.0 ms: 1.04x faster                                        |
| pidigits                | 271 ms                                                       | 261 ms: 1.04x faster                                         |
| comprehensions          | 26.9 us                                                      | 26.4 us: 1.02x faster                                        |
| unpickle_list           | 4.49 us                                                      | 4.54 us: 1.01x slower                                        |
| pickle                  | 9.94 us                                                      | 10.1 us: 1.02x slower                                        |
| gc_traversal            | 3.45 ms                                                      | 3.59 ms: 1.04x slower                                        |
| pickle_dict             | 30.0 us                                                      | 31.8 us: 1.06x slower                                        |
| python_startup_no_site  | 7.32 ms                                                      | 8.32 ms: 1.14x slower                                        |
| regex_effbot            | 2.99 ms                                                      | 3.43 ms: 1.15x slower                                        |
| dask                    | 463 ms                                                       | 568 ms: 1.23x slower                                         |
| coverage                | 64.0 ms                                                      | 90.5 ms: 1.42x slower                                        |
| Geometric mean          | (ref)                                                        | 1.26x faster                                                 |
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.20x
