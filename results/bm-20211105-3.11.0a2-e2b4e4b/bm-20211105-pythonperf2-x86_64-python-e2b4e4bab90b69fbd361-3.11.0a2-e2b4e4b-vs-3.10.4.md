
# Results vs. 3.10.4

- fork: python
- ref: e2b4e4bab90b69fbd361
- machine: linux-x86_64
- commit hash: e2b4e4b
- commit date: 2021-11-05
- overall geometric mean: 1.13x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-pythonperf2-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 299 ms: 1.17x faster                                                        |
| chameleon      | 9.72 ms                                                      | 9.27 ms: 1.05x faster                                                       |
| docutils       | 3.40 sec                                                     | 3.05 sec: 1.12x faster                                                      |
| html5lib       | 94.6 ms                                                      | 80.0 ms: 1.18x faster                                                       |
| tornado_http   | 152 ms                                                       | 136 ms: 1.12x faster                                                        |
| Geometric mean | (ref)                                                        | 1.13x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-pythonperf2-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 110 ms                                                       | 86.1 ms: 1.28x faster                                                       |
| nbody          | 137 ms                                                       | 113 ms: 1.22x faster                                                        |
| pidigits       | 271 ms                                                       | 264 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                        | 1.17x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-pythonperf2-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 158 ms: 1.23x faster                                                        |
| regex_v8       | 26.6 ms                                                      | 25.8 ms: 1.03x faster                                                       |
| regex_dna      | 259 ms                                                       | 262 ms: 1.01x slower                                                        |
| regex_effbot   | 2.99 ms                                                      | 3.06 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-pythonperf2-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_process    | 76.0 ms                                                      | 61.7 ms: 1.23x faster                                                       |
| json_loads           | 30.0 us                                                      | 24.7 us: 1.22x faster                                                       |
| pickle_pure_python   | 457 us                                                       | 386 us: 1.18x faster                                                        |
| unpickle_pure_python | 321 us                                                       | 277 us: 1.16x faster                                                        |
| xml_etree_generate   | 94.6 ms                                                      | 85.8 ms: 1.10x faster                                                       |
| unpickle             | 14.2 us                                                      | 13.4 us: 1.06x faster                                                       |
| json_dumps           | 14.2 ms                                                      | 13.4 ms: 1.06x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 107 ms: 1.03x faster                                                        |
| xml_etree_parse      | 162 ms                                                       | 157 ms: 1.03x faster                                                        |
| pickle_dict          | 30.0 us                                                      | 30.2 us: 1.01x slower                                                       |
| unpickle_list        | 4.49 us                                                      | 4.55 us: 1.01x slower                                                       |
| pickle_list          | 4.11 us                                                      | 4.17 us: 1.02x slower                                                       |
| pickle               | 9.94 us                                                      | 10.3 us: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.07x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-pythonperf2-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.2 ms: 1.03x faster                                                       |
| python_startup_no_site | 7.32 ms                                                      | 7.43 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-pythonperf2-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 12.9 ms: 1.14x faster                                                       |
| genshi_xml      | 64.7 ms                                                      | 57.9 ms: 1.12x faster                                                       |
| genshi_text     | 31.5 ms                                                      | 28.2 ms: 1.12x faster                                                       |
| django_template | 51.5 ms                                                      | 47.4 ms: 1.09x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.11x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-pythonperf2-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 7.47 ms                                                      | 5.07 ms: 1.47x faster                                                       |
| bench_mp_pool           | 7.18 ms                                                      | 5.01 ms: 1.43x faster                                                       |
| raytrace                | 488 ms                                                       | 349 ms: 1.40x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                       | 79.5 ms: 1.38x faster                                                       |
| logging_silent          | 166 ns                                                       | 121 ns: 1.37x faster                                                        |
| chaos                   | 107 ms                                                       | 79.2 ms: 1.35x faster                                                       |
| go                      | 259 ms                                                       | 194 ms: 1.33x faster                                                        |
| async_tree_none         | 700 ms                                                       | 532 ms: 1.32x faster                                                        |
| spectral_norm           | 136 ms                                                       | 104 ms: 1.31x faster                                                        |
| async_generators        | 422 ms                                                       | 325 ms: 1.30x faster                                                        |
| unpack_sequence         | 59.5 ns                                                      | 46.0 ns: 1.29x faster                                                       |
| float                   | 110 ms                                                       | 86.1 ms: 1.28x faster                                                       |
| async_tree_io           | 1.61 sec                                                     | 1.27 sec: 1.27x faster                                                      |
| scimark_sor             | 177 ms                                                       | 140 ms: 1.27x faster                                                        |
| richards                | 74.1 ms                                                      | 59.0 ms: 1.25x faster                                                       |
| crypto_pyaes            | 118 ms                                                       | 94.9 ms: 1.25x faster                                                       |
| scimark_lu              | 164 ms                                                       | 132 ms: 1.24x faster                                                        |
| async_tree_memoization  | 824 ms                                                       | 668 ms: 1.23x faster                                                        |
| xml_etree_process       | 76.0 ms                                                      | 61.7 ms: 1.23x faster                                                       |
| regex_compile           | 194 ms                                                       | 158 ms: 1.23x faster                                                        |
| json_loads              | 30.0 us                                                      | 24.7 us: 1.22x faster                                                       |
| nbody                   | 137 ms                                                       | 113 ms: 1.22x faster                                                        |
| thrift                  | 1.16 ms                                                      | 961 us: 1.21x faster                                                        |
| logging_simple          | 8.90 us                                                      | 7.35 us: 1.21x faster                                                       |
| hexiom                  | 9.52 ms                                                      | 7.87 ms: 1.21x faster                                                       |
| pyflate                 | 697 ms                                                       | 582 ms: 1.20x faster                                                        |
| gunicorn                | 1.17 ms                                                      | 980 us: 1.20x faster                                                        |
| pprint_safe_repr        | 1.05 sec                                                     | 877 ms: 1.20x faster                                                        |
| logging_format          | 9.57 us                                                      | 8.08 us: 1.18x faster                                                       |
| pickle_pure_python      | 457 us                                                       | 386 us: 1.18x faster                                                        |
| pprint_pformat          | 2.15 sec                                                     | 1.82 sec: 1.18x faster                                                      |
| html5lib                | 94.6 ms                                                      | 80.0 ms: 1.18x faster                                                       |
| 2to3                    | 350 ms                                                       | 299 ms: 1.17x faster                                                        |
| async_tree_cpu_io_mixed | 952 ms                                                       | 818 ms: 1.16x faster                                                        |
| unpickle_pure_python    | 321 us                                                       | 277 us: 1.16x faster                                                        |
| scimark_fft             | 359 ms                                                       | 311 ms: 1.16x faster                                                        |
| json                    | 5.96 ms                                                      | 5.19 ms: 1.15x faster                                                       |
| scimark_sparse_mat_mult | 5.19 ms                                                      | 4.56 ms: 1.14x faster                                                       |
| deepcopy_memo           | 48.9 us                                                      | 42.9 us: 1.14x faster                                                       |
| mako                    | 14.7 ms                                                      | 12.9 ms: 1.14x faster                                                       |
| tornado_http            | 152 ms                                                       | 136 ms: 1.12x faster                                                        |
| pycparser               | 1.66 sec                                                     | 1.48 sec: 1.12x faster                                                      |
| genshi_xml              | 64.7 ms                                                      | 57.9 ms: 1.12x faster                                                       |
| genshi_text             | 31.5 ms                                                      | 28.2 ms: 1.12x faster                                                       |
| docutils                | 3.40 sec                                                     | 3.05 sec: 1.12x faster                                                      |
| nqueens                 | 112 ms                                                       | 102 ms: 1.11x faster                                                        |
| dulwich_log             | 80.1 ms                                                      | 72.4 ms: 1.11x faster                                                       |
| xml_etree_generate      | 94.6 ms                                                      | 85.8 ms: 1.10x faster                                                       |
| generators              | 58.0 ms                                                      | 52.7 ms: 1.10x faster                                                       |
| create_gc_cycles        | 1.82 ms                                                      | 1.67 ms: 1.09x faster                                                       |
| sqlglot_normalize       | 144 ms                                                       | 132 ms: 1.09x faster                                                        |
| django_template         | 51.5 ms                                                      | 47.4 ms: 1.09x faster                                                       |
| pathlib                 | 21.7 ms                                                      | 20.0 ms: 1.08x faster                                                       |
| bench_thread_pool       | 1.14 ms                                                      | 1.05 ms: 1.08x faster                                                       |
| fannkuch                | 496 ms                                                       | 458 ms: 1.08x faster                                                        |
| sqlglot_optimize        | 70.3 ms                                                      | 64.9 ms: 1.08x faster                                                       |
| sqlite_synth            | 2.97 us                                                      | 2.75 us: 1.08x faster                                                       |
| meteor_contest          | 137 ms                                                       | 128 ms: 1.07x faster                                                        |
| sympy_expand            | 599 ms                                                       | 563 ms: 1.06x faster                                                        |
| deepcopy                | 454 us                                                       | 428 us: 1.06x faster                                                        |
| unpickle                | 14.2 us                                                      | 13.4 us: 1.06x faster                                                       |
| json_dumps              | 14.2 ms                                                      | 13.4 ms: 1.06x faster                                                       |
| sympy_integrate         | 28.1 ms                                                      | 26.5 ms: 1.06x faster                                                       |
| deepcopy_reduce         | 4.03 us                                                      | 3.81 us: 1.06x faster                                                       |
| mdp                     | 3.03 sec                                                     | 2.87 sec: 1.06x faster                                                      |
| sympy_sum               | 193 ms                                                       | 183 ms: 1.05x faster                                                        |
| sympy_str               | 358 ms                                                       | 340 ms: 1.05x faster                                                        |
| telco                   | 7.14 ms                                                      | 6.81 ms: 1.05x faster                                                       |
| chameleon               | 9.72 ms                                                      | 9.27 ms: 1.05x faster                                                       |
| dask                    | 463 ms                                                       | 445 ms: 1.04x faster                                                        |
| regex_v8                | 26.6 ms                                                      | 25.8 ms: 1.03x faster                                                       |
| coroutines              | 30.4 ms                                                      | 29.5 ms: 1.03x faster                                                       |
| xml_etree_iterparse     | 110 ms                                                       | 107 ms: 1.03x faster                                                        |
| sqlglot_transpile       | 2.71 ms                                                      | 2.63 ms: 1.03x faster                                                       |
| python_startup          | 11.5 ms                                                      | 11.2 ms: 1.03x faster                                                       |
| xml_etree_parse         | 162 ms                                                       | 157 ms: 1.03x faster                                                        |
| pidigits                | 271 ms                                                       | 264 ms: 1.02x faster                                                        |
| sqlglot_parse           | 2.26 ms                                                      | 2.24 ms: 1.01x faster                                                       |
| pickle_dict             | 30.0 us                                                      | 30.2 us: 1.01x slower                                                       |
| regex_dna               | 259 ms                                                       | 262 ms: 1.01x slower                                                        |
| unpickle_list           | 4.49 us                                                      | 4.55 us: 1.01x slower                                                       |
| python_startup_no_site  | 7.32 ms                                                      | 7.43 ms: 1.02x slower                                                       |
| pickle_list             | 4.11 us                                                      | 4.17 us: 1.02x slower                                                       |
| regex_effbot            | 2.99 ms                                                      | 3.06 ms: 1.02x slower                                                       |
| pickle                  | 9.94 us                                                      | 10.3 us: 1.03x slower                                                       |
| comprehensions          | 26.9 us                                                      | 28.8 us: 1.07x slower                                                       |
| coverage                | 64.0 ms                                                      | 68.7 ms: 1.07x slower                                                       |
| gc_traversal            | 3.45 ms                                                      | 3.77 ms: 1.09x slower                                                       |
| flaskblogging           | 4.39 ms                                                      | 4.84 ms: 1.10x slower                                                       |
| Geometric mean          | (ref)                                                        | 1.13x faster                                                                |
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.08x
