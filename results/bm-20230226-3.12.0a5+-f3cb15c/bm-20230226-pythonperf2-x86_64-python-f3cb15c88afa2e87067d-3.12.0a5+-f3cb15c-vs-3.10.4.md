
# Results vs. 3.10.4

- fork: python
- ref: f3cb15c88afa2e87067d
- machine: linux-x86_64
- commit hash: f3cb15c
- commit date: 2023-02-26
- overall geometric mean: 1.25x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230226-pythonperf2-x86_64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 285 ms: 1.22x faster                                                         |
| chameleon      | 9.72 ms                                                      | 6.83 ms: 1.42x faster                                                        |
| docutils       | 3.40 sec                                                     | 2.82 sec: 1.21x faster                                                       |
| html5lib       | 94.6 ms                                                      | 67.1 ms: 1.41x faster                                                        |
| tornado_http   | 152 ms                                                       | 117 ms: 1.30x faster                                                         |
| Geometric mean | (ref)                                                        | 1.31x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230226-pythonperf2-x86_64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 110 ms                                                       | 72.5 ms: 1.52x faster                                                        |
| nbody          | 137 ms                                                       | 94.5 ms: 1.45x faster                                                        |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                         |
| Geometric mean | (ref)                                                        | 1.33x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230226-pythonperf2-x86_64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 147 ms: 1.31x faster                                                         |
| regex_dna      | 259 ms                                                       | 222 ms: 1.17x faster                                                         |
| regex_v8       | 26.6 ms                                                      | 22.9 ms: 1.16x faster                                                        |
| regex_effbot   | 2.99 ms                                                      | 3.31 ms: 1.11x slower                                                        |
| Geometric mean | (ref)                                                        | 1.13x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230226-pythonperf2-x86_64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 205 us: 1.56x faster                                                         |
| pickle_pure_python   | 457 us                                                       | 310 us: 1.47x faster                                                         |
| json_dumps           | 14.2 ms                                                      | 10.1 ms: 1.41x faster                                                        |
| xml_etree_process    | 76.0 ms                                                      | 58.2 ms: 1.31x faster                                                        |
| json_loads           | 30.0 us                                                      | 24.1 us: 1.24x faster                                                        |
| xml_etree_parse      | 162 ms                                                       | 144 ms: 1.12x faster                                                         |
| xml_etree_generate   | 94.6 ms                                                      | 84.2 ms: 1.12x faster                                                        |
| unpickle             | 14.2 us                                                      | 13.2 us: 1.07x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 103 ms: 1.07x faster                                                         |
| pickle_list          | 4.11 us                                                      | 3.92 us: 1.05x faster                                                        |
| pickle               | 9.94 us                                                      | 9.80 us: 1.01x faster                                                        |
| unpickle_list        | 4.49 us                                                      | 4.43 us: 1.01x faster                                                        |
| pickle_dict          | 30.0 us                                                      | 31.3 us: 1.04x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.17x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230226-pythonperf2-x86_64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.3 ms: 1.01x faster                                                        |
| python_startup_no_site | 7.32 ms                                                      | 8.39 ms: 1.15x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230226-pythonperf2-x86_64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.87 ms: 1.49x faster                                                        |
| django_template | 51.5 ms                                                      | 41.1 ms: 1.25x faster                                                        |
| genshi_text     | 31.5 ms                                                      | 25.1 ms: 1.25x faster                                                        |
| genshi_xml      | 64.7 ms                                                      | 55.8 ms: 1.16x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.28x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230226-pythonperf2-x86_64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deltablue               | 7.47 ms                                                      | 3.35 ms: 2.23x faster                                                        |
| asyncio_tcp             | 782 ms                                                       | 387 ms: 2.02x faster                                                         |
| logging_silent          | 166 ns                                                       | 95.3 ns: 1.74x faster                                                        |
| go                      | 259 ms                                                       | 150 ms: 1.72x faster                                                         |
| scimark_sor             | 177 ms                                                       | 108 ms: 1.64x faster                                                         |
| raytrace                | 488 ms                                                       | 298 ms: 1.64x faster                                                         |
| pyflate                 | 697 ms                                                       | 434 ms: 1.61x faster                                                         |
| richards                | 74.1 ms                                                      | 46.4 ms: 1.60x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                       | 69.4 ms: 1.58x faster                                                        |
| scimark_lu              | 164 ms                                                       | 104 ms: 1.58x faster                                                         |
| unpickle_pure_python    | 321 us                                                       | 205 us: 1.56x faster                                                         |
| float                   | 110 ms                                                       | 72.5 ms: 1.52x faster                                                        |
| chaos                   | 107 ms                                                       | 71.0 ms: 1.51x faster                                                        |
| generators              | 58.0 ms                                                      | 38.6 ms: 1.50x faster                                                        |
| mako                    | 14.7 ms                                                      | 9.87 ms: 1.49x faster                                                        |
| pickle_pure_python      | 457 us                                                       | 310 us: 1.47x faster                                                         |
| hexiom                  | 9.52 ms                                                      | 6.53 ms: 1.46x faster                                                        |
| nbody                   | 137 ms                                                       | 94.5 ms: 1.45x faster                                                        |
| bench_mp_pool           | 7.18 ms                                                      | 4.96 ms: 1.45x faster                                                        |
| sqlglot_parse           | 2.26 ms                                                      | 1.58 ms: 1.42x faster                                                        |
| chameleon               | 9.72 ms                                                      | 6.83 ms: 1.42x faster                                                        |
| spectral_norm           | 136 ms                                                       | 96.4 ms: 1.41x faster                                                        |
| json_dumps              | 14.2 ms                                                      | 10.1 ms: 1.41x faster                                                        |
| html5lib                | 94.6 ms                                                      | 67.1 ms: 1.41x faster                                                        |
| crypto_pyaes            | 118 ms                                                       | 84.8 ms: 1.39x faster                                                        |
| sqlglot_transpile       | 2.71 ms                                                      | 1.95 ms: 1.39x faster                                                        |
| pprint_safe_repr        | 1.05 sec                                                     | 759 ms: 1.38x faster                                                         |
| pprint_pformat          | 2.15 sec                                                     | 1.57 sec: 1.37x faster                                                       |
| async_tree_io           | 1.61 sec                                                     | 1.18 sec: 1.36x faster                                                       |
| async_tree_memoization  | 824 ms                                                       | 615 ms: 1.34x faster                                                         |
| deepcopy_memo           | 48.9 us                                                      | 36.6 us: 1.34x faster                                                        |
| async_tree_none         | 700 ms                                                       | 524 ms: 1.34x faster                                                         |
| unpack_sequence         | 59.5 ns                                                      | 45.0 ns: 1.32x faster                                                        |
| regex_compile           | 194 ms                                                       | 147 ms: 1.31x faster                                                         |
| xml_etree_process       | 76.0 ms                                                      | 58.2 ms: 1.31x faster                                                        |
| pycparser               | 1.66 sec                                                     | 1.27 sec: 1.31x faster                                                       |
| tornado_http            | 152 ms                                                       | 117 ms: 1.30x faster                                                         |
| scimark_fft             | 359 ms                                                       | 281 ms: 1.28x faster                                                         |
| async_tree_cpu_io_mixed | 952 ms                                                       | 756 ms: 1.26x faster                                                         |
| scimark_sparse_mat_mult | 5.19 ms                                                      | 4.13 ms: 1.26x faster                                                        |
| django_template         | 51.5 ms                                                      | 41.1 ms: 1.25x faster                                                        |
| genshi_text             | 31.5 ms                                                      | 25.1 ms: 1.25x faster                                                        |
| logging_simple          | 8.90 us                                                      | 7.11 us: 1.25x faster                                                        |
| coroutines              | 30.4 ms                                                      | 24.4 ms: 1.24x faster                                                        |
| json_loads              | 30.0 us                                                      | 24.1 us: 1.24x faster                                                        |
| thrift                  | 1.16 ms                                                      | 945 us: 1.23x faster                                                         |
| dulwich_log             | 80.1 ms                                                      | 65.0 ms: 1.23x faster                                                        |
| fannkuch                | 496 ms                                                       | 404 ms: 1.23x faster                                                         |
| 2to3                    | 350 ms                                                       | 285 ms: 1.22x faster                                                         |
| mypy2                   | 466 ms                                                       | 381 ms: 1.22x faster                                                         |
| logging_format          | 9.57 us                                                      | 7.89 us: 1.21x faster                                                        |
| sqlglot_optimize        | 70.3 ms                                                      | 58.2 ms: 1.21x faster                                                        |
| docutils                | 3.40 sec                                                     | 2.82 sec: 1.21x faster                                                       |
| sqlglot_normalize       | 144 ms                                                       | 120 ms: 1.21x faster                                                         |
| json                    | 5.96 ms                                                      | 4.98 ms: 1.20x faster                                                        |
| regex_dna               | 259 ms                                                       | 222 ms: 1.17x faster                                                         |
| regex_v8                | 26.6 ms                                                      | 22.9 ms: 1.16x faster                                                        |
| deepcopy_reduce         | 4.03 us                                                      | 3.47 us: 1.16x faster                                                        |
| genshi_xml              | 64.7 ms                                                      | 55.8 ms: 1.16x faster                                                        |
| pathlib                 | 21.7 ms                                                      | 18.8 ms: 1.16x faster                                                        |
| sqlite_synth            | 2.97 us                                                      | 2.57 us: 1.16x faster                                                        |
| bench_thread_pool       | 1.14 ms                                                      | 985 us: 1.15x faster                                                         |
| deepcopy                | 454 us                                                       | 398 us: 1.14x faster                                                         |
| nqueens                 | 112 ms                                                       | 99.1 ms: 1.13x faster                                                        |
| xml_etree_parse         | 162 ms                                                       | 144 ms: 1.12x faster                                                         |
| xml_etree_generate      | 94.6 ms                                                      | 84.2 ms: 1.12x faster                                                        |
| mdp                     | 3.03 sec                                                     | 2.71 sec: 1.12x faster                                                       |
| sympy_integrate         | 28.1 ms                                                      | 25.4 ms: 1.11x faster                                                        |
| sympy_expand            | 599 ms                                                       | 546 ms: 1.10x faster                                                         |
| meteor_contest          | 137 ms                                                       | 126 ms: 1.09x faster                                                         |
| create_gc_cycles        | 1.82 ms                                                      | 1.68 ms: 1.09x faster                                                        |
| pidigits                | 271 ms                                                       | 251 ms: 1.08x faster                                                         |
| unpickle                | 14.2 us                                                      | 13.2 us: 1.07x faster                                                        |
| async_generators        | 422 ms                                                       | 393 ms: 1.07x faster                                                         |
| xml_etree_iterparse     | 110 ms                                                       | 103 ms: 1.07x faster                                                         |
| sympy_str               | 358 ms                                                       | 336 ms: 1.07x faster                                                         |
| pickle_list             | 4.11 us                                                      | 3.92 us: 1.05x faster                                                        |
| telco                   | 7.14 ms                                                      | 6.83 ms: 1.05x faster                                                        |
| sympy_sum               | 193 ms                                                       | 188 ms: 1.02x faster                                                         |
| pickle                  | 9.94 us                                                      | 9.80 us: 1.01x faster                                                        |
| unpickle_list           | 4.49 us                                                      | 4.43 us: 1.01x faster                                                        |
| python_startup          | 11.5 ms                                                      | 11.3 ms: 1.01x faster                                                        |
| comprehensions          | 26.9 us                                                      | 27.4 us: 1.02x slower                                                        |
| pickle_dict             | 30.0 us                                                      | 31.3 us: 1.04x slower                                                        |
| regex_effbot            | 2.99 ms                                                      | 3.31 ms: 1.11x slower                                                        |
| python_startup_no_site  | 7.32 ms                                                      | 8.39 ms: 1.15x slower                                                        |
| gc_traversal            | 3.45 ms                                                      | 3.99 ms: 1.16x slower                                                        |
| dask                    | 463 ms                                                       | 563 ms: 1.21x slower                                                         |
| coverage                | 64.0 ms                                                      | 85.2 ms: 1.33x slower                                                        |
| Geometric mean          | (ref)                                                        | 1.25x faster                                                                 |
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.20x
