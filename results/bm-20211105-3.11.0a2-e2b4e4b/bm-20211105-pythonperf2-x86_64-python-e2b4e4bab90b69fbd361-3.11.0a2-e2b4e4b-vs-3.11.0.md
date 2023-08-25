
# Results vs. 3.11.0

- fork: python
- ref: e2b4e4bab90b69fbd361
- machine: linux-x86_64
- commit hash: e2b4e4b
- commit date: 2021-11-05
- overall geometric mean: 1.08x slower \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211105-pythonperf2-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 299 ms: 1.04x slower                                                        |
| chameleon      | 7.67 ms                                                      | 9.27 ms: 1.21x slower                                                       |
| docutils       | 2.86 sec                                                     | 3.05 sec: 1.07x slower                                                      |
| html5lib       | 72.9 ms                                                      | 80.0 ms: 1.10x slower                                                       |
| tornado_http   | 122 ms                                                       | 136 ms: 1.11x slower                                                        |
| Geometric mean | (ref)                                                        | 1.10x slower                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211105-pythonperf2-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 251 ms                                                       | 264 ms: 1.05x slower                                                        |
| float          | 74.2 ms                                                      | 86.1 ms: 1.16x slower                                                       |
| nbody          | 90.7 ms                                                      | 113 ms: 1.25x slower                                                        |
| Geometric mean | (ref)                                                        | 1.15x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211105-pythonperf2-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.50 ms                                                      | 3.06 ms: 1.14x faster                                                       |
| regex_v8       | 23.9 ms                                                      | 25.8 ms: 1.08x slower                                                       |
| regex_dna      | 227 ms                                                       | 262 ms: 1.15x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211105-pythonperf2-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_loads           | 28.7 us                                                      | 24.7 us: 1.16x faster                                                       |
| pickle_dict          | 30.8 us                                                      | 30.2 us: 1.02x faster                                                       |
| unpickle             | 13.4 us                                                      | 13.4 us: 1.00x faster                                                       |
| json_dumps           | 13.4 ms                                                      | 13.4 ms: 1.00x slower                                                       |
| xml_etree_iterparse  | 104 ms                                                       | 107 ms: 1.03x slower                                                        |
| pickle               | 9.64 us                                                      | 10.3 us: 1.06x slower                                                       |
| xml_etree_generate   | 80.5 ms                                                      | 85.8 ms: 1.07x slower                                                       |
| pickle_list          | 3.83 us                                                      | 4.17 us: 1.09x slower                                                       |
| xml_etree_process    | 56.5 ms                                                      | 61.7 ms: 1.09x slower                                                       |
| unpickle_pure_python | 241 us                                                       | 277 us: 1.15x slower                                                        |
| pickle_pure_python   | 319 us                                                       | 386 us: 1.21x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.04x slower                                                                |

Benchmark hidden because not significant (2): xml_etree_parse, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211105-pythonperf2-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.76 ms                                                      | 7.43 ms: 1.04x faster                                                       |
| python_startup         | 10.8 ms                                                      | 11.2 ms: 1.04x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.00x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211105-pythonperf2-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 58.5 ms                                                      | 57.9 ms: 1.01x faster                                                       |
| genshi_text     | 26.1 ms                                                      | 28.2 ms: 1.08x slower                                                       |
| mako            | 11.0 ms                                                      | 12.9 ms: 1.18x slower                                                       |
| django_template | 40.2 ms                                                      | 47.4 ms: 1.18x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.10x slower                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211105-pythonperf2-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| coverage                | 84.8 ms                                                      | 68.7 ms: 1.23x faster                                                       |
| json_loads              | 28.7 us                                                      | 24.7 us: 1.16x faster                                                       |
| regex_effbot            | 3.50 ms                                                      | 3.06 ms: 1.14x faster                                                       |
| json                    | 5.65 ms                                                      | 5.19 ms: 1.09x faster                                                       |
| generators              | 56.0 ms                                                      | 52.7 ms: 1.06x faster                                                       |
| python_startup_no_site  | 7.76 ms                                                      | 7.43 ms: 1.04x faster                                                       |
| chaos                   | 80.9 ms                                                      | 79.2 ms: 1.02x faster                                                       |
| gc_traversal            | 3.85 ms                                                      | 3.77 ms: 1.02x faster                                                       |
| meteor_contest          | 131 ms                                                       | 128 ms: 1.02x faster                                                        |
| pickle_dict             | 30.8 us                                                      | 30.2 us: 1.02x faster                                                       |
| nqueens                 | 103 ms                                                       | 102 ms: 1.01x faster                                                        |
| genshi_xml              | 58.5 ms                                                      | 57.9 ms: 1.01x faster                                                       |
| telco                   | 6.86 ms                                                      | 6.81 ms: 1.01x faster                                                       |
| sympy_sum               | 185 ms                                                       | 183 ms: 1.01x faster                                                        |
| unpickle                | 13.4 us                                                      | 13.4 us: 1.00x faster                                                       |
| json_dumps              | 13.4 ms                                                      | 13.4 ms: 1.00x slower                                                       |
| gunicorn                | 973 us                                                       | 980 us: 1.01x slower                                                        |
| sympy_str               | 337 ms                                                       | 340 ms: 1.01x slower                                                        |
| sympy_expand            | 555 ms                                                       | 563 ms: 1.02x slower                                                        |
| logging_simple          | 7.19 us                                                      | 7.35 us: 1.02x slower                                                       |
| async_tree_none         | 519 ms                                                       | 532 ms: 1.02x slower                                                        |
| xml_etree_iterparse     | 104 ms                                                       | 107 ms: 1.03x slower                                                        |
| sympy_integrate         | 25.8 ms                                                      | 26.5 ms: 1.03x slower                                                       |
| async_generators        | 316 ms                                                       | 325 ms: 1.03x slower                                                        |
| create_gc_cycles        | 1.61 ms                                                      | 1.67 ms: 1.04x slower                                                       |
| bench_thread_pool       | 1.01 ms                                                      | 1.05 ms: 1.04x slower                                                       |
| python_startup          | 10.8 ms                                                      | 11.2 ms: 1.04x slower                                                       |
| 2to3                    | 288 ms                                                       | 299 ms: 1.04x slower                                                        |
| thrift                  | 925 us                                                       | 961 us: 1.04x slower                                                        |
| mdp                     | 2.75 sec                                                     | 2.87 sec: 1.05x slower                                                      |
| pathlib                 | 19.1 ms                                                      | 20.0 ms: 1.05x slower                                                       |
| sqlglot_normalize       | 126 ms                                                       | 132 ms: 1.05x slower                                                        |
| pidigits                | 251 ms                                                       | 264 ms: 1.05x slower                                                        |
| dulwich_log             | 68.4 ms                                                      | 72.4 ms: 1.06x slower                                                       |
| async_tree_memoization  | 630 ms                                                       | 668 ms: 1.06x slower                                                        |
| pickle                  | 9.64 us                                                      | 10.3 us: 1.06x slower                                                       |
| xml_etree_generate      | 80.5 ms                                                      | 85.8 ms: 1.07x slower                                                       |
| docutils                | 2.86 sec                                                     | 3.05 sec: 1.07x slower                                                      |
| fannkuch                | 429 ms                                                       | 458 ms: 1.07x slower                                                        |
| coroutines              | 27.6 ms                                                      | 29.5 ms: 1.07x slower                                                       |
| deepcopy                | 399 us                                                       | 428 us: 1.07x slower                                                        |
| genshi_text             | 26.1 ms                                                      | 28.2 ms: 1.08x slower                                                       |
| regex_v8                | 23.9 ms                                                      | 25.8 ms: 1.08x slower                                                       |
| async_tree_io           | 1.17 sec                                                     | 1.27 sec: 1.08x slower                                                      |
| bench_mp_pool           | 4.62 ms                                                      | 5.01 ms: 1.08x slower                                                       |
| dask                    | 410 ms                                                       | 445 ms: 1.09x slower                                                        |
| deepcopy_reduce         | 3.51 us                                                      | 3.81 us: 1.09x slower                                                       |
| sqlglot_optimize        | 59.8 ms                                                      | 64.9 ms: 1.09x slower                                                       |
| pickle_list             | 3.83 us                                                      | 4.17 us: 1.09x slower                                                       |
| scimark_fft             | 285 ms                                                       | 311 ms: 1.09x slower                                                        |
| async_tree_cpu_io_mixed | 749 ms                                                       | 818 ms: 1.09x slower                                                        |
| xml_etree_process       | 56.5 ms                                                      | 61.7 ms: 1.09x slower                                                       |
| html5lib                | 72.9 ms                                                      | 80.0 ms: 1.10x slower                                                       |
| sqlite_synth            | 2.50 us                                                      | 2.75 us: 1.10x slower                                                       |
| hexiom                  | 7.13 ms                                                      | 7.87 ms: 1.10x slower                                                       |
| raytrace                | 317 ms                                                       | 349 ms: 1.10x slower                                                        |
| deepcopy_memo           | 38.8 us                                                      | 42.9 us: 1.11x slower                                                       |
| tornado_http            | 122 ms                                                       | 136 ms: 1.11x slower                                                        |
| spectral_norm           | 93.3 ms                                                      | 104 ms: 1.12x slower                                                        |
| pprint_pformat          | 1.63 sec                                                     | 1.82 sec: 1.12x slower                                                      |
| pprint_safe_repr        | 784 ms                                                       | 877 ms: 1.12x slower                                                        |
| pycparser               | 1.32 sec                                                     | 1.48 sec: 1.12x slower                                                      |
| scimark_sparse_mat_mult | 4.05 ms                                                      | 4.56 ms: 1.13x slower                                                       |
| crypto_pyaes            | 83.4 ms                                                      | 94.9 ms: 1.14x slower                                                       |
| regex_dna               | 227 ms                                                       | 262 ms: 1.15x slower                                                        |
| unpickle_pure_python    | 241 us                                                       | 277 us: 1.15x slower                                                        |
| scimark_lu              | 115 ms                                                       | 132 ms: 1.16x slower                                                        |
| float                   | 74.2 ms                                                      | 86.1 ms: 1.16x slower                                                       |
| scimark_monte_carlo     | 68.2 ms                                                      | 79.5 ms: 1.17x slower                                                       |
| comprehensions          | 24.6 us                                                      | 28.8 us: 1.17x slower                                                       |
| mako                    | 11.0 ms                                                      | 12.9 ms: 1.18x slower                                                       |
| django_template         | 40.2 ms                                                      | 47.4 ms: 1.18x slower                                                       |
| go                      | 164 ms                                                       | 194 ms: 1.18x slower                                                        |
| logging_silent          | 101 ns                                                       | 121 ns: 1.20x slower                                                        |
| chameleon               | 7.67 ms                                                      | 9.27 ms: 1.21x slower                                                       |
| pickle_pure_python      | 319 us                                                       | 386 us: 1.21x slower                                                        |
| richards                | 48.3 ms                                                      | 59.0 ms: 1.22x slower                                                       |
| nbody                   | 90.7 ms                                                      | 113 ms: 1.25x slower                                                        |
| flaskblogging           | 3.88 ms                                                      | 4.84 ms: 1.25x slower                                                       |
| scimark_sor             | 111 ms                                                       | 140 ms: 1.26x slower                                                        |
| deltablue               | 4.00 ms                                                      | 5.07 ms: 1.27x slower                                                       |
| pyflate                 | 449 ms                                                       | 582 ms: 1.30x slower                                                        |
| sqlglot_transpile       | 1.92 ms                                                      | 2.63 ms: 1.37x slower                                                       |
| sqlglot_parse           | 1.53 ms                                                      | 2.24 ms: 1.46x slower                                                       |
| Geometric mean          | (ref)                                                        | 1.08x slower                                                                |

Benchmark hidden because not significant (5): logging_format, xml_etree_parse, regex_compile, unpickle_list, unpack_sequence
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x
