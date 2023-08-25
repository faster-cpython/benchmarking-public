
# Results vs. 3.10.4

- fork: python
- ref: 8d32a5c8c4e9c90b0a21
- machine: linux-x86_64
- commit hash: 8d32a5c
- commit date: 2022-05-06
- overall geometric mean: 1.23x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-pythonperf2-x86_64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 281 ms: 1.24x faster                                                        |
| chameleon      | 9.72 ms                                                      | 7.53 ms: 1.29x faster                                                       |
| docutils       | 3.40 sec                                                     | 2.82 sec: 1.21x faster                                                      |
| html5lib       | 94.6 ms                                                      | 69.0 ms: 1.37x faster                                                       |
| tornado_http   | 152 ms                                                       | 121 ms: 1.26x faster                                                        |
| Geometric mean | (ref)                                                        | 1.27x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-pythonperf2-x86_64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 110 ms                                                       | 74.7 ms: 1.48x faster                                                       |
| nbody          | 137 ms                                                       | 100 ms: 1.37x faster                                                        |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                        | 1.30x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-pythonperf2-x86_64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 153 ms: 1.27x faster                                                        |
| regex_v8       | 26.6 ms                                                      | 22.8 ms: 1.17x faster                                                       |
| regex_dna      | 259 ms                                                       | 232 ms: 1.12x faster                                                        |
| regex_effbot   | 2.99 ms                                                      | 2.97 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                        | 1.14x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-pythonperf2-x86_64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                       | 320 us: 1.43x faster                                                        |
| unpickle_pure_python | 321 us                                                       | 233 us: 1.38x faster                                                        |
| xml_etree_process    | 76.0 ms                                                      | 56.1 ms: 1.35x faster                                                       |
| json_loads           | 30.0 us                                                      | 24.6 us: 1.22x faster                                                       |
| xml_etree_generate   | 94.6 ms                                                      | 80.3 ms: 1.18x faster                                                       |
| pickle_list          | 4.11 us                                                      | 3.81 us: 1.08x faster                                                       |
| unpickle             | 14.2 us                                                      | 13.3 us: 1.07x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 105 ms: 1.05x faster                                                        |
| json_dumps           | 14.2 ms                                                      | 13.5 ms: 1.05x faster                                                       |
| xml_etree_parse      | 162 ms                                                       | 155 ms: 1.04x faster                                                        |
| pickle               | 9.94 us                                                      | 9.62 us: 1.03x faster                                                       |
| pickle_dict          | 30.0 us                                                      | 29.9 us: 1.00x faster                                                       |
| unpickle_list        | 4.49 us                                                      | 4.56 us: 1.02x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-pythonperf2-x86_64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 10.5 ms: 1.09x faster                                                       |
| python_startup_no_site | 7.32 ms                                                      | 7.68 ms: 1.05x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-pythonperf2-x86_64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.9 ms: 1.35x faster                                                       |
| django_template | 51.5 ms                                                      | 41.3 ms: 1.25x faster                                                       |
| genshi_text     | 31.5 ms                                                      | 25.4 ms: 1.24x faster                                                       |
| genshi_xml      | 64.7 ms                                                      | 56.7 ms: 1.14x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.24x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-pythonperf2-x86_64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 7.47 ms                                                      | 3.93 ms: 1.90x faster                                                       |
| logging_silent          | 166 ns                                                       | 99.8 ns: 1.66x faster                                                       |
| go                      | 259 ms                                                       | 156 ms: 1.66x faster                                                        |
| pyflate                 | 697 ms                                                       | 433 ms: 1.61x faster                                                        |
| scimark_sor             | 177 ms                                                       | 110 ms: 1.61x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                       | 69.2 ms: 1.58x faster                                                       |
| raytrace                | 488 ms                                                       | 309 ms: 1.58x faster                                                        |
| bench_mp_pool           | 7.18 ms                                                      | 4.56 ms: 1.58x faster                                                       |
| chaos                   | 107 ms                                                       | 72.4 ms: 1.48x faster                                                       |
| richards                | 74.1 ms                                                      | 50.1 ms: 1.48x faster                                                       |
| float                   | 110 ms                                                       | 74.7 ms: 1.48x faster                                                       |
| spectral_norm           | 136 ms                                                       | 93.1 ms: 1.46x faster                                                       |
| crypto_pyaes            | 118 ms                                                       | 82.3 ms: 1.44x faster                                                       |
| scimark_lu              | 164 ms                                                       | 114 ms: 1.44x faster                                                        |
| pickle_pure_python      | 457 us                                                       | 320 us: 1.43x faster                                                        |
| pprint_safe_repr        | 1.05 sec                                                     | 755 ms: 1.39x faster                                                        |
| hexiom                  | 9.52 ms                                                      | 6.91 ms: 1.38x faster                                                       |
| unpickle_pure_python    | 321 us                                                       | 233 us: 1.38x faster                                                        |
| async_tree_io           | 1.61 sec                                                     | 1.17 sec: 1.38x faster                                                      |
| pprint_pformat          | 2.15 sec                                                     | 1.57 sec: 1.37x faster                                                      |
| nbody                   | 137 ms                                                       | 100 ms: 1.37x faster                                                        |
| html5lib                | 94.6 ms                                                      | 69.0 ms: 1.37x faster                                                       |
| async_tree_none         | 700 ms                                                       | 516 ms: 1.36x faster                                                        |
| xml_etree_process       | 76.0 ms                                                      | 56.1 ms: 1.35x faster                                                       |
| mako                    | 14.7 ms                                                      | 10.9 ms: 1.35x faster                                                       |
| async_generators        | 422 ms                                                       | 318 ms: 1.33x faster                                                        |
| pycparser               | 1.66 sec                                                     | 1.26 sec: 1.32x faster                                                      |
| async_tree_memoization  | 824 ms                                                       | 624 ms: 1.32x faster                                                        |
| deepcopy_memo           | 48.9 us                                                      | 37.6 us: 1.30x faster                                                       |
| chameleon               | 9.72 ms                                                      | 7.53 ms: 1.29x faster                                                       |
| logging_simple          | 8.90 us                                                      | 6.90 us: 1.29x faster                                                       |
| unpack_sequence         | 59.5 ns                                                      | 46.2 ns: 1.29x faster                                                       |
| scimark_sparse_mat_mult | 5.19 ms                                                      | 4.06 ms: 1.28x faster                                                       |
| aiohttp                 | 1.21 ms                                                      | 945 us: 1.28x faster                                                        |
| thrift                  | 1.16 ms                                                      | 913 us: 1.28x faster                                                        |
| async_tree_cpu_io_mixed | 952 ms                                                       | 748 ms: 1.27x faster                                                        |
| regex_compile           | 194 ms                                                       | 153 ms: 1.27x faster                                                        |
| gunicorn                | 1.17 ms                                                      | 928 us: 1.26x faster                                                        |
| tornado_http            | 152 ms                                                       | 121 ms: 1.26x faster                                                        |
| django_template         | 51.5 ms                                                      | 41.3 ms: 1.25x faster                                                       |
| logging_format          | 9.57 us                                                      | 7.67 us: 1.25x faster                                                       |
| 2to3                    | 350 ms                                                       | 281 ms: 1.24x faster                                                        |
| genshi_text             | 31.5 ms                                                      | 25.4 ms: 1.24x faster                                                       |
| scimark_fft             | 359 ms                                                       | 294 ms: 1.22x faster                                                        |
| json_loads              | 30.0 us                                                      | 24.6 us: 1.22x faster                                                       |
| sqlalchemy_declarative  | 187 ms                                                       | 153 ms: 1.22x faster                                                        |
| sqlglot_normalize       | 144 ms                                                       | 119 ms: 1.21x faster                                                        |
| docutils                | 3.40 sec                                                     | 2.82 sec: 1.21x faster                                                      |
| sqlglot_optimize        | 70.3 ms                                                      | 58.9 ms: 1.19x faster                                                       |
| fannkuch                | 496 ms                                                       | 418 ms: 1.19x faster                                                        |
| sqlite_synth            | 2.97 us                                                      | 2.51 us: 1.18x faster                                                       |
| dulwich_log             | 80.1 ms                                                      | 68.0 ms: 1.18x faster                                                       |
| deepcopy_reduce         | 4.03 us                                                      | 3.42 us: 1.18x faster                                                       |
| xml_etree_generate      | 94.6 ms                                                      | 80.3 ms: 1.18x faster                                                       |
| sqlglot_transpile       | 2.71 ms                                                      | 2.30 ms: 1.18x faster                                                       |
| nqueens                 | 112 ms                                                       | 95.8 ms: 1.17x faster                                                       |
| regex_v8                | 26.6 ms                                                      | 22.8 ms: 1.17x faster                                                       |
| sqlalchemy_imperative   | 22.6 ms                                                      | 19.5 ms: 1.16x faster                                                       |
| sqlglot_parse           | 2.26 ms                                                      | 1.95 ms: 1.16x faster                                                       |
| json                    | 5.96 ms                                                      | 5.14 ms: 1.16x faster                                                       |
| pathlib                 | 21.7 ms                                                      | 18.8 ms: 1.15x faster                                                       |
| deepcopy                | 454 us                                                       | 394 us: 1.15x faster                                                        |
| flaskblogging           | 4.39 ms                                                      | 3.82 ms: 1.15x faster                                                       |
| genshi_xml              | 64.7 ms                                                      | 56.7 ms: 1.14x faster                                                       |
| regex_dna               | 259 ms                                                       | 232 ms: 1.12x faster                                                        |
| sympy_integrate         | 28.1 ms                                                      | 25.2 ms: 1.11x faster                                                       |
| bench_thread_pool       | 1.14 ms                                                      | 1.02 ms: 1.11x faster                                                       |
| pylint                  | 562 ms                                                       | 505 ms: 1.11x faster                                                        |
| sympy_expand            | 599 ms                                                       | 540 ms: 1.11x faster                                                        |
| create_gc_cycles        | 1.82 ms                                                      | 1.64 ms: 1.11x faster                                                       |
| dask                    | 463 ms                                                       | 418 ms: 1.11x faster                                                        |
| mdp                     | 3.03 sec                                                     | 2.78 sec: 1.09x faster                                                      |
| python_startup          | 11.5 ms                                                      | 10.5 ms: 1.09x faster                                                       |
| sympy_str               | 358 ms                                                       | 329 ms: 1.09x faster                                                        |
| coroutines              | 30.4 ms                                                      | 28.0 ms: 1.09x faster                                                       |
| sympy_sum               | 193 ms                                                       | 178 ms: 1.08x faster                                                        |
| pickle_list             | 4.11 us                                                      | 3.81 us: 1.08x faster                                                       |
| pidigits                | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| unpickle                | 14.2 us                                                      | 13.3 us: 1.07x faster                                                       |
| mypy2                   | 466 ms                                                       | 438 ms: 1.07x faster                                                        |
| xml_etree_iterparse     | 110 ms                                                       | 105 ms: 1.05x faster                                                        |
| json_dumps              | 14.2 ms                                                      | 13.5 ms: 1.05x faster                                                       |
| asyncio_tcp             | 782 ms                                                       | 749 ms: 1.05x faster                                                        |
| generators              | 58.0 ms                                                      | 55.5 ms: 1.04x faster                                                       |
| meteor_contest          | 137 ms                                                       | 131 ms: 1.04x faster                                                        |
| xml_etree_parse         | 162 ms                                                       | 155 ms: 1.04x faster                                                        |
| pickle                  | 9.94 us                                                      | 9.62 us: 1.03x faster                                                       |
| telco                   | 7.14 ms                                                      | 6.99 ms: 1.02x faster                                                       |
| regex_effbot            | 2.99 ms                                                      | 2.97 ms: 1.01x faster                                                       |
| pickle_dict             | 30.0 us                                                      | 29.9 us: 1.00x faster                                                       |
| unpickle_list           | 4.49 us                                                      | 4.56 us: 1.02x slower                                                       |
| comprehensions          | 26.9 us                                                      | 28.2 us: 1.05x slower                                                       |
| python_startup_no_site  | 7.32 ms                                                      | 7.68 ms: 1.05x slower                                                       |
| gc_traversal            | 3.45 ms                                                      | 3.85 ms: 1.11x slower                                                       |
| Geometric mean          | (ref)                                                        | 1.23x faster                                                                |
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, coverage, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.17x
