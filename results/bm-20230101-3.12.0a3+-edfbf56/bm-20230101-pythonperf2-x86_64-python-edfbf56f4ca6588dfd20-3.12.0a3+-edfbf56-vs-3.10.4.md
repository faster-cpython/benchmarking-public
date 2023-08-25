
# Results vs. 3.10.4

- fork: python
- ref: edfbf56f4ca6588dfd20
- machine: linux-x86_64
- commit hash: edfbf56
- commit date: 2023-01-01
- overall geometric mean: 1.26x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230101-pythonperf2-x86_64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 284 ms: 1.23x faster                                                         |
| chameleon      | 9.72 ms                                                      | 7.29 ms: 1.33x faster                                                        |
| docutils       | 3.40 sec                                                     | 2.76 sec: 1.23x faster                                                       |
| html5lib       | 94.6 ms                                                      | 66.2 ms: 1.43x faster                                                        |
| Geometric mean | (ref)                                                        | 1.30x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230101-pythonperf2-x86_64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 110 ms                                                       | 72.5 ms: 1.52x faster                                                        |
| nbody          | 137 ms                                                       | 90.4 ms: 1.52x faster                                                        |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                         |
| Geometric mean | (ref)                                                        | 1.36x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230101-pythonperf2-x86_64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 149 ms: 1.30x faster                                                         |
| regex_v8       | 26.6 ms                                                      | 22.9 ms: 1.16x faster                                                        |
| regex_dna      | 259 ms                                                       | 229 ms: 1.13x faster                                                         |
| regex_effbot   | 2.99 ms                                                      | 3.40 ms: 1.13x slower                                                        |
| Geometric mean | (ref)                                                        | 1.11x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230101-pythonperf2-x86_64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 210 us: 1.53x faster                                                         |
| pickle_pure_python   | 457 us                                                       | 313 us: 1.46x faster                                                         |
| xml_etree_process    | 76.0 ms                                                      | 54.1 ms: 1.40x faster                                                        |
| json_dumps           | 14.2 ms                                                      | 10.2 ms: 1.39x faster                                                        |
| json_loads           | 30.0 us                                                      | 24.1 us: 1.25x faster                                                        |
| xml_etree_generate   | 94.6 ms                                                      | 78.0 ms: 1.21x faster                                                        |
| xml_etree_parse      | 162 ms                                                       | 141 ms: 1.14x faster                                                         |
| unpickle             | 14.2 us                                                      | 12.9 us: 1.10x faster                                                        |
| pickle_list          | 4.11 us                                                      | 3.83 us: 1.07x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 104 ms: 1.06x faster                                                         |
| unpickle_list        | 4.49 us                                                      | 4.43 us: 1.01x faster                                                        |
| pickle               | 9.94 us                                                      | 9.84 us: 1.01x faster                                                        |
| pickle_dict          | 30.0 us                                                      | 31.7 us: 1.06x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.19x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230101-pythonperf2-x86_64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 10.7 ms: 1.07x faster                                                        |
| python_startup_no_site | 7.32 ms                                                      | 7.83 ms: 1.07x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.00x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230101-pythonperf2-x86_64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.1 ms: 1.45x faster                                                        |
| django_template | 51.5 ms                                                      | 39.5 ms: 1.30x faster                                                        |
| genshi_text     | 31.5 ms                                                      | 25.1 ms: 1.25x faster                                                        |
| genshi_xml      | 64.7 ms                                                      | 53.9 ms: 1.20x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.30x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230101-pythonperf2-x86_64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deltablue               | 7.47 ms                                                      | 3.64 ms: 2.05x faster                                                        |
| asyncio_tcp             | 782 ms                                                       | 391 ms: 2.00x faster                                                         |
| scimark_monte_carlo     | 109 ms                                                       | 66.1 ms: 1.66x faster                                                        |
| scimark_sor             | 177 ms                                                       | 107 ms: 1.65x faster                                                         |
| logging_silent          | 166 ns                                                       | 101 ns: 1.65x faster                                                         |
| scimark_lu              | 164 ms                                                       | 100 ms: 1.63x faster                                                         |
| raytrace                | 488 ms                                                       | 300 ms: 1.63x faster                                                         |
| go                      | 259 ms                                                       | 159 ms: 1.63x faster                                                         |
| pyflate                 | 697 ms                                                       | 429 ms: 1.62x faster                                                         |
| richards                | 74.1 ms                                                      | 46.3 ms: 1.60x faster                                                        |
| unpickle_pure_python    | 321 us                                                       | 210 us: 1.53x faster                                                         |
| float                   | 110 ms                                                       | 72.5 ms: 1.52x faster                                                        |
| nbody                   | 137 ms                                                       | 90.4 ms: 1.52x faster                                                        |
| bench_mp_pool           | 7.18 ms                                                      | 4.74 ms: 1.51x faster                                                        |
| chaos                   | 107 ms                                                       | 72.8 ms: 1.47x faster                                                        |
| crypto_pyaes            | 118 ms                                                       | 80.5 ms: 1.47x faster                                                        |
| pickle_pure_python      | 457 us                                                       | 313 us: 1.46x faster                                                         |
| mako                    | 14.7 ms                                                      | 10.1 ms: 1.45x faster                                                        |
| spectral_norm           | 136 ms                                                       | 94.2 ms: 1.45x faster                                                        |
| sqlglot_parse           | 2.26 ms                                                      | 1.57 ms: 1.44x faster                                                        |
| html5lib                | 94.6 ms                                                      | 66.2 ms: 1.43x faster                                                        |
| scimark_sparse_mat_mult | 5.19 ms                                                      | 3.66 ms: 1.42x faster                                                        |
| xml_etree_process       | 76.0 ms                                                      | 54.1 ms: 1.40x faster                                                        |
| sqlglot_transpile       | 2.71 ms                                                      | 1.93 ms: 1.40x faster                                                        |
| json_dumps              | 14.2 ms                                                      | 10.2 ms: 1.39x faster                                                        |
| hexiom                  | 9.52 ms                                                      | 6.86 ms: 1.39x faster                                                        |
| pprint_safe_repr        | 1.05 sec                                                     | 758 ms: 1.39x faster                                                         |
| async_tree_io           | 1.61 sec                                                     | 1.16 sec: 1.38x faster                                                       |
| pprint_pformat          | 2.15 sec                                                     | 1.56 sec: 1.38x faster                                                       |
| async_tree_none         | 700 ms                                                       | 510 ms: 1.37x faster                                                         |
| deepcopy_memo           | 48.9 us                                                      | 35.7 us: 1.37x faster                                                        |
| async_tree_memoization  | 824 ms                                                       | 613 ms: 1.34x faster                                                         |
| unpack_sequence         | 59.5 ns                                                      | 44.5 ns: 1.34x faster                                                        |
| chameleon               | 9.72 ms                                                      | 7.29 ms: 1.33x faster                                                        |
| thrift                  | 1.16 ms                                                      | 885 us: 1.32x faster                                                         |
| scimark_fft             | 359 ms                                                       | 275 ms: 1.31x faster                                                         |
| django_template         | 51.5 ms                                                      | 39.5 ms: 1.30x faster                                                        |
| pycparser               | 1.66 sec                                                     | 1.28 sec: 1.30x faster                                                       |
| regex_compile           | 194 ms                                                       | 149 ms: 1.30x faster                                                         |
| async_generators        | 422 ms                                                       | 326 ms: 1.30x faster                                                         |
| async_tree_cpu_io_mixed | 952 ms                                                       | 747 ms: 1.27x faster                                                         |
| logging_simple          | 8.90 us                                                      | 6.98 us: 1.27x faster                                                        |
| fannkuch                | 496 ms                                                       | 392 ms: 1.26x faster                                                         |
| genshi_text             | 31.5 ms                                                      | 25.1 ms: 1.25x faster                                                        |
| json_loads              | 30.0 us                                                      | 24.1 us: 1.25x faster                                                        |
| mypy2                   | 466 ms                                                       | 378 ms: 1.24x faster                                                         |
| docutils                | 3.40 sec                                                     | 2.76 sec: 1.23x faster                                                       |
| 2to3                    | 350 ms                                                       | 284 ms: 1.23x faster                                                         |
| dulwich_log             | 80.1 ms                                                      | 65.1 ms: 1.23x faster                                                        |
| logging_format          | 9.57 us                                                      | 7.80 us: 1.23x faster                                                        |
| sqlglot_optimize        | 70.3 ms                                                      | 57.5 ms: 1.22x faster                                                        |
| sqlglot_normalize       | 144 ms                                                       | 119 ms: 1.21x faster                                                         |
| deepcopy_reduce         | 4.03 us                                                      | 3.32 us: 1.21x faster                                                        |
| xml_etree_generate      | 94.6 ms                                                      | 78.0 ms: 1.21x faster                                                        |
| genshi_xml              | 64.7 ms                                                      | 53.9 ms: 1.20x faster                                                        |
| deepcopy                | 454 us                                                       | 380 us: 1.19x faster                                                         |
| nqueens                 | 112 ms                                                       | 94.4 ms: 1.19x faster                                                        |
| json                    | 5.96 ms                                                      | 5.08 ms: 1.17x faster                                                        |
| bench_thread_pool       | 1.14 ms                                                      | 971 us: 1.17x faster                                                         |
| regex_v8                | 26.6 ms                                                      | 22.9 ms: 1.16x faster                                                        |
| sqlite_synth            | 2.97 us                                                      | 2.57 us: 1.15x faster                                                        |
| create_gc_cycles        | 1.82 ms                                                      | 1.58 ms: 1.15x faster                                                        |
| xml_etree_parse         | 162 ms                                                       | 141 ms: 1.14x faster                                                         |
| regex_dna               | 259 ms                                                       | 229 ms: 1.13x faster                                                         |
| pathlib                 | 21.7 ms                                                      | 19.2 ms: 1.13x faster                                                        |
| sympy_expand            | 599 ms                                                       | 533 ms: 1.12x faster                                                         |
| dask                    | 463 ms                                                       | 413 ms: 1.12x faster                                                         |
| coroutines              | 30.4 ms                                                      | 27.2 ms: 1.12x faster                                                        |
| sympy_integrate         | 28.1 ms                                                      | 25.3 ms: 1.11x faster                                                        |
| unpickle                | 14.2 us                                                      | 12.9 us: 1.10x faster                                                        |
| sympy_str               | 358 ms                                                       | 330 ms: 1.08x faster                                                         |
| pidigits                | 271 ms                                                       | 251 ms: 1.08x faster                                                         |
| pickle_list             | 4.11 us                                                      | 3.83 us: 1.07x faster                                                        |
| mdp                     | 3.03 sec                                                     | 2.83 sec: 1.07x faster                                                       |
| python_startup          | 11.5 ms                                                      | 10.7 ms: 1.07x faster                                                        |
| meteor_contest          | 137 ms                                                       | 129 ms: 1.06x faster                                                         |
| xml_etree_iterparse     | 110 ms                                                       | 104 ms: 1.06x faster                                                         |
| telco                   | 7.14 ms                                                      | 6.76 ms: 1.06x faster                                                        |
| sympy_sum               | 193 ms                                                       | 183 ms: 1.05x faster                                                         |
| unpickle_list           | 4.49 us                                                      | 4.43 us: 1.01x faster                                                        |
| pickle                  | 9.94 us                                                      | 9.84 us: 1.01x faster                                                        |
| comprehensions          | 26.9 us                                                      | 27.2 us: 1.01x slower                                                        |
| generators              | 58.0 ms                                                      | 59.9 ms: 1.03x slower                                                        |
| pickle_dict             | 30.0 us                                                      | 31.7 us: 1.06x slower                                                        |
| python_startup_no_site  | 7.32 ms                                                      | 7.83 ms: 1.07x slower                                                        |
| gc_traversal            | 3.45 ms                                                      | 3.78 ms: 1.09x slower                                                        |
| regex_effbot            | 2.99 ms                                                      | 3.40 ms: 1.13x slower                                                        |
| coverage                | 64.0 ms                                                      | 93.0 ms: 1.45x slower                                                        |
| Geometric mean          | (ref)                                                        | 1.26x faster                                                                 |
Ignored benchmarks (11) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x
