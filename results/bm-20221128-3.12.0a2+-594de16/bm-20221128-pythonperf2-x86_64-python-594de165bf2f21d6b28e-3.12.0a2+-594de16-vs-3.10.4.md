
# Results vs. 3.10.4

- fork: python
- ref: 594de165bf2f21d6b28e
- machine: linux-x86_64
- commit hash: 594de16
- commit date: 2022-11-28
- overall geometric mean: 1.24x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221128-pythonperf2-x86_64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 280 ms: 1.25x faster                                                         |
| chameleon      | 9.72 ms                                                      | 7.65 ms: 1.27x faster                                                        |
| docutils       | 3.40 sec                                                     | 2.77 sec: 1.23x faster                                                       |
| html5lib       | 94.6 ms                                                      | 66.5 ms: 1.42x faster                                                        |
| tornado_http   | 152 ms                                                       | 119 ms: 1.28x faster                                                         |
| Geometric mean | (ref)                                                        | 1.29x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221128-pythonperf2-x86_64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 89.6 ms: 1.53x faster                                                        |
| float          | 110 ms                                                       | 73.9 ms: 1.49x faster                                                        |
| pidigits       | 271 ms                                                       | 252 ms: 1.07x faster                                                         |
| Geometric mean | (ref)                                                        | 1.35x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221128-pythonperf2-x86_64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 149 ms: 1.30x faster                                                         |
| regex_v8       | 26.6 ms                                                      | 23.2 ms: 1.15x faster                                                        |
| regex_dna      | 259 ms                                                       | 229 ms: 1.13x faster                                                         |
| regex_effbot   | 2.99 ms                                                      | 3.36 ms: 1.12x slower                                                        |
| Geometric mean | (ref)                                                        | 1.11x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221128-pythonperf2-x86_64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 219 us: 1.47x faster                                                         |
| pickle_pure_python   | 457 us                                                       | 320 us: 1.43x faster                                                         |
| xml_etree_process    | 76.0 ms                                                      | 55.8 ms: 1.36x faster                                                        |
| json_dumps           | 14.2 ms                                                      | 10.5 ms: 1.36x faster                                                        |
| json_loads           | 30.0 us                                                      | 24.2 us: 1.24x faster                                                        |
| xml_etree_generate   | 94.6 ms                                                      | 79.8 ms: 1.18x faster                                                        |
| xml_etree_parse      | 162 ms                                                       | 141 ms: 1.15x faster                                                         |
| pickle_list          | 4.11 us                                                      | 3.84 us: 1.07x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 104 ms: 1.06x faster                                                         |
| unpickle             | 14.2 us                                                      | 13.5 us: 1.05x faster                                                        |
| pickle               | 9.94 us                                                      | 9.77 us: 1.02x faster                                                        |
| unpickle_list        | 4.49 us                                                      | 4.55 us: 1.01x slower                                                        |
| pickle_dict          | 30.0 us                                                      | 31.7 us: 1.06x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.17x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221128-pythonperf2-x86_64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 10.8 ms: 1.06x faster                                                        |
| python_startup_no_site | 7.32 ms                                                      | 7.85 ms: 1.07x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.00x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221128-pythonperf2-x86_64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.2 ms: 1.44x faster                                                        |
| django_template | 51.5 ms                                                      | 40.1 ms: 1.29x faster                                                        |
| genshi_text     | 31.5 ms                                                      | 24.5 ms: 1.28x faster                                                        |
| genshi_xml      | 64.7 ms                                                      | 52.3 ms: 1.24x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.31x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221128-pythonperf2-x86_64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deltablue               | 7.47 ms                                                      | 3.71 ms: 2.01x faster                                                        |
| logging_silent          | 166 ns                                                       | 101 ns: 1.64x faster                                                         |
| go                      | 259 ms                                                       | 162 ms: 1.60x faster                                                         |
| raytrace                | 488 ms                                                       | 305 ms: 1.60x faster                                                         |
| scimark_lu              | 164 ms                                                       | 103 ms: 1.59x faster                                                         |
| scimark_sor             | 177 ms                                                       | 112 ms: 1.58x faster                                                         |
| pyflate                 | 697 ms                                                       | 447 ms: 1.56x faster                                                         |
| bench_mp_pool           | 7.18 ms                                                      | 4.64 ms: 1.55x faster                                                        |
| nbody                   | 137 ms                                                       | 89.6 ms: 1.53x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                       | 72.0 ms: 1.52x faster                                                        |
| richards                | 74.1 ms                                                      | 48.9 ms: 1.52x faster                                                        |
| float                   | 110 ms                                                       | 73.9 ms: 1.49x faster                                                        |
| chaos                   | 107 ms                                                       | 73.0 ms: 1.47x faster                                                        |
| unpickle_pure_python    | 321 us                                                       | 219 us: 1.47x faster                                                         |
| sqlglot_parse           | 2.26 ms                                                      | 1.55 ms: 1.46x faster                                                        |
| mako                    | 14.7 ms                                                      | 10.2 ms: 1.44x faster                                                        |
| pickle_pure_python      | 457 us                                                       | 320 us: 1.43x faster                                                         |
| html5lib                | 94.6 ms                                                      | 66.5 ms: 1.42x faster                                                        |
| crypto_pyaes            | 118 ms                                                       | 83.7 ms: 1.41x faster                                                        |
| sqlglot_transpile       | 2.71 ms                                                      | 1.92 ms: 1.41x faster                                                        |
| hexiom                  | 9.52 ms                                                      | 6.78 ms: 1.40x faster                                                        |
| async_tree_io           | 1.61 sec                                                     | 1.16 sec: 1.39x faster                                                       |
| spectral_norm           | 136 ms                                                       | 98.7 ms: 1.38x faster                                                        |
| scimark_sparse_mat_mult | 5.19 ms                                                      | 3.77 ms: 1.38x faster                                                        |
| pprint_safe_repr        | 1.05 sec                                                     | 768 ms: 1.37x faster                                                         |
| pprint_pformat          | 2.15 sec                                                     | 1.58 sec: 1.37x faster                                                       |
| xml_etree_process       | 76.0 ms                                                      | 55.8 ms: 1.36x faster                                                        |
| json_dumps              | 14.2 ms                                                      | 10.5 ms: 1.36x faster                                                        |
| async_tree_none         | 700 ms                                                       | 517 ms: 1.35x faster                                                         |
| async_tree_memoization  | 824 ms                                                       | 616 ms: 1.34x faster                                                         |
| aiohttp                 | 1.21 ms                                                      | 904 us: 1.34x faster                                                         |
| gunicorn                | 1.17 ms                                                      | 895 us: 1.31x faster                                                         |
| pycparser               | 1.66 sec                                                     | 1.27 sec: 1.31x faster                                                       |
| unpack_sequence         | 59.5 ns                                                      | 45.6 ns: 1.31x faster                                                        |
| regex_compile           | 194 ms                                                       | 149 ms: 1.30x faster                                                         |
| django_template         | 51.5 ms                                                      | 40.1 ms: 1.29x faster                                                        |
| genshi_text             | 31.5 ms                                                      | 24.5 ms: 1.28x faster                                                        |
| tornado_http            | 152 ms                                                       | 119 ms: 1.28x faster                                                         |
| scimark_fft             | 359 ms                                                       | 282 ms: 1.27x faster                                                         |
| async_generators        | 422 ms                                                       | 332 ms: 1.27x faster                                                         |
| chameleon               | 9.72 ms                                                      | 7.65 ms: 1.27x faster                                                        |
| deepcopy_memo           | 48.9 us                                                      | 38.8 us: 1.26x faster                                                        |
| async_tree_cpu_io_mixed | 952 ms                                                       | 758 ms: 1.26x faster                                                         |
| mypy2                   | 466 ms                                                       | 372 ms: 1.25x faster                                                         |
| 2to3                    | 350 ms                                                       | 280 ms: 1.25x faster                                                         |
| thrift                  | 1.16 ms                                                      | 937 us: 1.24x faster                                                         |
| fannkuch                | 496 ms                                                       | 399 ms: 1.24x faster                                                         |
| json_loads              | 30.0 us                                                      | 24.2 us: 1.24x faster                                                        |
| genshi_xml              | 64.7 ms                                                      | 52.3 ms: 1.24x faster                                                        |
| docutils                | 3.40 sec                                                     | 2.77 sec: 1.23x faster                                                       |
| logging_simple          | 8.90 us                                                      | 7.24 us: 1.23x faster                                                        |
| logging_format          | 9.57 us                                                      | 7.84 us: 1.22x faster                                                        |
| sqlglot_optimize        | 70.3 ms                                                      | 57.9 ms: 1.21x faster                                                        |
| sqlglot_normalize       | 144 ms                                                       | 120 ms: 1.21x faster                                                         |
| dulwich_log             | 80.1 ms                                                      | 67.1 ms: 1.19x faster                                                        |
| xml_etree_generate      | 94.6 ms                                                      | 79.8 ms: 1.18x faster                                                        |
| json                    | 5.96 ms                                                      | 5.08 ms: 1.17x faster                                                        |
| bench_thread_pool       | 1.14 ms                                                      | 970 us: 1.17x faster                                                         |
| create_gc_cycles        | 1.82 ms                                                      | 1.56 ms: 1.17x faster                                                        |
| sqlite_synth            | 2.97 us                                                      | 2.56 us: 1.16x faster                                                        |
| pathlib                 | 21.7 ms                                                      | 18.8 ms: 1.15x faster                                                        |
| xml_etree_parse         | 162 ms                                                       | 141 ms: 1.15x faster                                                         |
| regex_v8                | 26.6 ms                                                      | 23.2 ms: 1.15x faster                                                        |
| nqueens                 | 112 ms                                                       | 99.3 ms: 1.13x faster                                                        |
| regex_dna               | 259 ms                                                       | 229 ms: 1.13x faster                                                         |
| deepcopy_reduce         | 4.03 us                                                      | 3.59 us: 1.12x faster                                                        |
| dask                    | 463 ms                                                       | 415 ms: 1.11x faster                                                         |
| mdp                     | 3.03 sec                                                     | 2.73 sec: 1.11x faster                                                       |
| sympy_expand            | 599 ms                                                       | 543 ms: 1.10x faster                                                         |
| sympy_integrate         | 28.1 ms                                                      | 25.5 ms: 1.10x faster                                                        |
| deepcopy                | 454 us                                                       | 415 us: 1.09x faster                                                         |
| coroutines              | 30.4 ms                                                      | 28.2 ms: 1.08x faster                                                        |
| pidigits                | 271 ms                                                       | 252 ms: 1.07x faster                                                         |
| sympy_str               | 358 ms                                                       | 334 ms: 1.07x faster                                                         |
| pickle_list             | 4.11 us                                                      | 3.84 us: 1.07x faster                                                        |
| telco                   | 7.14 ms                                                      | 6.69 ms: 1.07x faster                                                        |
| meteor_contest          | 137 ms                                                       | 128 ms: 1.06x faster                                                         |
| python_startup          | 11.5 ms                                                      | 10.8 ms: 1.06x faster                                                        |
| xml_etree_iterparse     | 110 ms                                                       | 104 ms: 1.06x faster                                                         |
| asyncio_tcp             | 782 ms                                                       | 745 ms: 1.05x faster                                                         |
| unpickle                | 14.2 us                                                      | 13.5 us: 1.05x faster                                                        |
| sympy_sum               | 193 ms                                                       | 185 ms: 1.04x faster                                                         |
| pickle                  | 9.94 us                                                      | 9.77 us: 1.02x faster                                                        |
| comprehensions          | 26.9 us                                                      | 26.8 us: 1.00x faster                                                        |
| unpickle_list           | 4.49 us                                                      | 4.55 us: 1.01x slower                                                        |
| gc_traversal            | 3.45 ms                                                      | 3.56 ms: 1.03x slower                                                        |
| generators              | 58.0 ms                                                      | 61.1 ms: 1.05x slower                                                        |
| pickle_dict             | 30.0 us                                                      | 31.7 us: 1.06x slower                                                        |
| python_startup_no_site  | 7.32 ms                                                      | 7.85 ms: 1.07x slower                                                        |
| regex_effbot            | 2.99 ms                                                      | 3.36 ms: 1.12x slower                                                        |
| coverage                | 64.0 ms                                                      | 85.4 ms: 1.34x slower                                                        |
| Geometric mean          | (ref)                                                        | 1.24x faster                                                                 |
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.20x
