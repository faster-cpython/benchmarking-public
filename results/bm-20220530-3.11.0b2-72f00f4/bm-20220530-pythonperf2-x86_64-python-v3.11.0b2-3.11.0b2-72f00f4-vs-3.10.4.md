
# Results vs. 3.10.4

- fork: python
- ref: v3.11.0b2
- machine: linux-x86_64
- commit hash: 72f00f4
- commit date: 2022-05-30
- overall geometric mean: 1.23x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-pythonperf2-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 282 ms: 1.24x faster                                             |
| chameleon      | 9.72 ms                                                      | 7.52 ms: 1.29x faster                                            |
| docutils       | 3.40 sec                                                     | 2.83 sec: 1.20x faster                                           |
| html5lib       | 94.6 ms                                                      | 70.5 ms: 1.34x faster                                            |
| tornado_http   | 152 ms                                                       | 117 ms: 1.30x faster                                             |
| Geometric mean | (ref)                                                        | 1.27x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-pythonperf2-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 110 ms                                                       | 73.8 ms: 1.49x faster                                            |
| nbody          | 137 ms                                                       | 96.9 ms: 1.42x faster                                            |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                             |
| Geometric mean | (ref)                                                        | 1.32x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-pythonperf2-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 157 ms: 1.24x faster                                             |
| regex_dna      | 259 ms                                                       | 227 ms: 1.14x faster                                             |
| regex_v8       | 26.6 ms                                                      | 24.1 ms: 1.10x faster                                            |
| regex_effbot   | 2.99 ms                                                      | 3.11 ms: 1.04x slower                                            |
| Geometric mean | (ref)                                                        | 1.11x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-pythonperf2-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                       | 320 us: 1.43x faster                                             |
| unpickle_pure_python | 321 us                                                       | 234 us: 1.37x faster                                             |
| xml_etree_process    | 76.0 ms                                                      | 55.8 ms: 1.36x faster                                            |
| xml_etree_generate   | 94.6 ms                                                      | 79.0 ms: 1.20x faster                                            |
| json_loads           | 30.0 us                                                      | 25.1 us: 1.19x faster                                            |
| unpickle             | 14.2 us                                                      | 13.3 us: 1.07x faster                                            |
| json_dumps           | 14.2 ms                                                      | 13.3 ms: 1.07x faster                                            |
| pickle_list          | 4.11 us                                                      | 3.86 us: 1.06x faster                                            |
| xml_etree_parse      | 162 ms                                                       | 153 ms: 1.05x faster                                             |
| xml_etree_iterparse  | 110 ms                                                       | 106 ms: 1.04x faster                                             |
| pickle               | 9.94 us                                                      | 9.77 us: 1.02x faster                                            |
| pickle_dict          | 30.0 us                                                      | 30.4 us: 1.02x slower                                            |
| unpickle_list        | 4.49 us                                                      | 4.57 us: 1.02x slower                                            |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-pythonperf2-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 10.7 ms: 1.08x faster                                            |
| python_startup_no_site | 7.32 ms                                                      | 7.70 ms: 1.05x slower                                            |
| Geometric mean         | (ref)                                                        | 1.01x faster                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-pythonperf2-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.9 ms: 1.34x faster                                            |
| django_template | 51.5 ms                                                      | 39.5 ms: 1.31x faster                                            |
| genshi_text     | 31.5 ms                                                      | 24.4 ms: 1.29x faster                                            |
| genshi_xml      | 64.7 ms                                                      | 56.0 ms: 1.16x faster                                            |
| Geometric mean  | (ref)                                                        | 1.27x faster                                                     |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-pythonperf2-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| deltablue               | 7.47 ms                                                      | 3.98 ms: 1.88x faster                                            |
| go                      | 259 ms                                                       | 154 ms: 1.68x faster                                             |
| logging_silent          | 166 ns                                                       | 98.9 ns: 1.68x faster                                            |
| scimark_sor             | 177 ms                                                       | 108 ms: 1.64x faster                                             |
| scimark_monte_carlo     | 109 ms                                                       | 67.5 ms: 1.62x faster                                            |
| pyflate                 | 697 ms                                                       | 431 ms: 1.62x faster                                             |
| raytrace                | 488 ms                                                       | 305 ms: 1.60x faster                                             |
| bench_mp_pool           | 7.18 ms                                                      | 4.55 ms: 1.58x faster                                            |
| richards                | 74.1 ms                                                      | 48.5 ms: 1.53x faster                                            |
| float                   | 110 ms                                                       | 73.8 ms: 1.49x faster                                            |
| chaos                   | 107 ms                                                       | 72.1 ms: 1.49x faster                                            |
| scimark_lu              | 164 ms                                                       | 111 ms: 1.47x faster                                             |
| spectral_norm           | 136 ms                                                       | 93.4 ms: 1.46x faster                                            |
| pickle_pure_python      | 457 us                                                       | 320 us: 1.43x faster                                             |
| nbody                   | 137 ms                                                       | 96.9 ms: 1.42x faster                                            |
| crypto_pyaes            | 118 ms                                                       | 83.5 ms: 1.42x faster                                            |
| pprint_safe_repr        | 1.05 sec                                                     | 759 ms: 1.38x faster                                             |
| async_tree_io           | 1.61 sec                                                     | 1.16 sec: 1.38x faster                                           |
| pprint_pformat          | 2.15 sec                                                     | 1.57 sec: 1.37x faster                                           |
| async_tree_none         | 700 ms                                                       | 511 ms: 1.37x faster                                             |
| unpickle_pure_python    | 321 us                                                       | 234 us: 1.37x faster                                             |
| hexiom                  | 9.52 ms                                                      | 6.99 ms: 1.36x faster                                            |
| xml_etree_process       | 76.0 ms                                                      | 55.8 ms: 1.36x faster                                            |
| async_tree_memoization  | 824 ms                                                       | 609 ms: 1.35x faster                                             |
| async_generators        | 422 ms                                                       | 313 ms: 1.35x faster                                             |
| mako                    | 14.7 ms                                                      | 10.9 ms: 1.34x faster                                            |
| html5lib                | 94.6 ms                                                      | 70.5 ms: 1.34x faster                                            |
| deepcopy_memo           | 48.9 us                                                      | 36.9 us: 1.32x faster                                            |
| unpack_sequence         | 59.5 ns                                                      | 45.1 ns: 1.32x faster                                            |
| django_template         | 51.5 ms                                                      | 39.5 ms: 1.31x faster                                            |
| tornado_http            | 152 ms                                                       | 117 ms: 1.30x faster                                             |
| chameleon               | 9.72 ms                                                      | 7.52 ms: 1.29x faster                                            |
| genshi_text             | 31.5 ms                                                      | 24.4 ms: 1.29x faster                                            |
| async_tree_cpu_io_mixed | 952 ms                                                       | 740 ms: 1.29x faster                                             |
| scimark_sparse_mat_mult | 5.19 ms                                                      | 4.05 ms: 1.28x faster                                            |
| aiohttp                 | 1.21 ms                                                      | 944 us: 1.28x faster                                             |
| pycparser               | 1.66 sec                                                     | 1.30 sec: 1.28x faster                                           |
| scimark_fft             | 359 ms                                                       | 284 ms: 1.27x faster                                             |
| gunicorn                | 1.17 ms                                                      | 929 us: 1.26x faster                                             |
| thrift                  | 1.16 ms                                                      | 935 us: 1.25x faster                                             |
| 2to3                    | 350 ms                                                       | 282 ms: 1.24x faster                                             |
| regex_compile           | 194 ms                                                       | 157 ms: 1.24x faster                                             |
| logging_simple          | 8.90 us                                                      | 7.21 us: 1.23x faster                                            |
| logging_format          | 9.57 us                                                      | 7.81 us: 1.22x faster                                            |
| sqlalchemy_declarative  | 187 ms                                                       | 153 ms: 1.22x faster                                             |
| docutils                | 3.40 sec                                                     | 2.83 sec: 1.20x faster                                           |
| xml_etree_generate      | 94.6 ms                                                      | 79.0 ms: 1.20x faster                                            |
| json_loads              | 30.0 us                                                      | 25.1 us: 1.19x faster                                            |
| dulwich_log             | 80.1 ms                                                      | 67.2 ms: 1.19x faster                                            |
| sqlglot_transpile       | 2.71 ms                                                      | 2.29 ms: 1.18x faster                                            |
| deepcopy                | 454 us                                                       | 385 us: 1.18x faster                                             |
| sqlglot_optimize        | 70.3 ms                                                      | 59.7 ms: 1.18x faster                                            |
| sqlite_synth            | 2.97 us                                                      | 2.54 us: 1.17x faster                                            |
| sqlalchemy_imperative   | 22.6 ms                                                      | 19.4 ms: 1.17x faster                                            |
| sqlglot_normalize       | 144 ms                                                       | 124 ms: 1.17x faster                                             |
| deepcopy_reduce         | 4.03 us                                                      | 3.47 us: 1.16x faster                                            |
| sqlglot_parse           | 2.26 ms                                                      | 1.95 ms: 1.16x faster                                            |
| genshi_xml              | 64.7 ms                                                      | 56.0 ms: 1.16x faster                                            |
| json                    | 5.96 ms                                                      | 5.16 ms: 1.15x faster                                            |
| nqueens                 | 112 ms                                                       | 97.7 ms: 1.15x faster                                            |
| regex_dna               | 259 ms                                                       | 227 ms: 1.14x faster                                             |
| pathlib                 | 21.7 ms                                                      | 19.1 ms: 1.14x faster                                            |
| bench_thread_pool       | 1.14 ms                                                      | 1.00 ms: 1.13x faster                                            |
| dask                    | 463 ms                                                       | 410 ms: 1.13x faster                                             |
| sympy_expand            | 599 ms                                                       | 533 ms: 1.12x faster                                             |
| sympy_integrate         | 28.1 ms                                                      | 25.0 ms: 1.12x faster                                            |
| fannkuch                | 496 ms                                                       | 447 ms: 1.11x faster                                             |
| create_gc_cycles        | 1.82 ms                                                      | 1.64 ms: 1.11x faster                                            |
| regex_v8                | 26.6 ms                                                      | 24.1 ms: 1.10x faster                                            |
| pylint                  | 562 ms                                                       | 510 ms: 1.10x faster                                             |
| sympy_str               | 358 ms                                                       | 327 ms: 1.10x faster                                             |
| coroutines              | 30.4 ms                                                      | 27.9 ms: 1.09x faster                                            |
| sympy_sum               | 193 ms                                                       | 177 ms: 1.09x faster                                             |
| python_startup          | 11.5 ms                                                      | 10.7 ms: 1.08x faster                                            |
| pidigits                | 271 ms                                                       | 251 ms: 1.08x faster                                             |
| unpickle                | 14.2 us                                                      | 13.3 us: 1.07x faster                                            |
| json_dumps              | 14.2 ms                                                      | 13.3 ms: 1.07x faster                                            |
| mdp                     | 3.03 sec                                                     | 2.85 sec: 1.07x faster                                           |
| pickle_list             | 4.11 us                                                      | 3.86 us: 1.06x faster                                            |
| mypy2                   | 466 ms                                                       | 439 ms: 1.06x faster                                             |
| meteor_contest          | 137 ms                                                       | 129 ms: 1.06x faster                                             |
| xml_etree_parse         | 162 ms                                                       | 153 ms: 1.05x faster                                             |
| generators              | 58.0 ms                                                      | 55.2 ms: 1.05x faster                                            |
| asyncio_tcp             | 782 ms                                                       | 746 ms: 1.05x faster                                             |
| xml_etree_iterparse     | 110 ms                                                       | 106 ms: 1.04x faster                                             |
| telco                   | 7.14 ms                                                      | 6.99 ms: 1.02x faster                                            |
| pickle                  | 9.94 us                                                      | 9.77 us: 1.02x faster                                            |
| pickle_dict             | 30.0 us                                                      | 30.4 us: 1.02x slower                                            |
| unpickle_list           | 4.49 us                                                      | 4.57 us: 1.02x slower                                            |
| comprehensions          | 26.9 us                                                      | 27.9 us: 1.04x slower                                            |
| regex_effbot            | 2.99 ms                                                      | 3.11 ms: 1.04x slower                                            |
| python_startup_no_site  | 7.32 ms                                                      | 7.70 ms: 1.05x slower                                            |
| gc_traversal            | 3.45 ms                                                      | 3.94 ms: 1.14x slower                                            |
| Geometric mean          | (ref)                                                        | 1.23x faster                                                     |
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, coverage, flaskblogging, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.17x
