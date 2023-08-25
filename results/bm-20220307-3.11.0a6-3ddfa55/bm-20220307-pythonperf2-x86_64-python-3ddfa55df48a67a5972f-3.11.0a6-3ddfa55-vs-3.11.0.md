
# Results vs. 3.11.0

- fork: python
- ref: 3ddfa55df48a67a5972f
- machine: linux-x86_64
- commit hash: 3ddfa55
- commit date: 2022-03-07
- overall geometric mean: 1.06x slower \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220307-pythonperf2-x86_64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 300 ms: 1.04x slower                                                        |
| chameleon      | 7.67 ms                                                      | 8.43 ms: 1.10x slower                                                       |
| docutils       | 2.86 sec                                                     | 2.98 sec: 1.04x slower                                                      |
| html5lib       | 72.9 ms                                                      | 75.6 ms: 1.04x slower                                                       |
| tornado_http   | 122 ms                                                       | 130 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                        | 1.06x slower                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220307-pythonperf2-x86_64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 251 ms                                                       | 253 ms: 1.01x slower                                                        |
| float          | 74.2 ms                                                      | 79.1 ms: 1.07x slower                                                       |
| nbody          | 90.7 ms                                                      | 98.0 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220307-pythonperf2-x86_64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.50 ms                                                      | 3.49 ms: 1.00x faster                                                       |
| regex_compile  | 158 ms                                                       | 161 ms: 1.02x slower                                                        |
| regex_v8       | 23.9 ms                                                      | 26.4 ms: 1.10x slower                                                       |
| regex_dna      | 227 ms                                                       | 257 ms: 1.13x slower                                                        |
| Geometric mean | (ref)                                                        | 1.06x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220307-pythonperf2-x86_64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_loads           | 28.7 us                                                      | 23.9 us: 1.20x faster                                                       |
| xml_etree_parse      | 158 ms                                                       | 154 ms: 1.02x faster                                                        |
| unpickle             | 13.4 us                                                      | 13.5 us: 1.01x slower                                                       |
| json_dumps           | 13.4 ms                                                      | 13.6 ms: 1.02x slower                                                       |
| unpickle_list        | 4.53 us                                                      | 4.68 us: 1.03x slower                                                       |
| pickle               | 9.64 us                                                      | 9.96 us: 1.03x slower                                                       |
| xml_etree_generate   | 80.5 ms                                                      | 83.5 ms: 1.04x slower                                                       |
| pickle_dict          | 30.8 us                                                      | 32.2 us: 1.05x slower                                                       |
| xml_etree_process    | 56.5 ms                                                      | 59.4 ms: 1.05x slower                                                       |
| pickle_pure_python   | 319 us                                                       | 352 us: 1.10x slower                                                        |
| pickle_list          | 3.83 us                                                      | 4.28 us: 1.12x slower                                                       |
| unpickle_pure_python | 241 us                                                       | 273 us: 1.13x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.03x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220307-pythonperf2-x86_64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 10.4 ms: 1.03x faster                                                       |
| python_startup_no_site | 7.76 ms                                                      | 7.55 ms: 1.03x faster                                                       |
| Geometric mean         | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220307-pythonperf2-x86_64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.1 ms                                                      | 26.5 ms: 1.01x slower                                                       |
| genshi_xml      | 58.5 ms                                                      | 60.7 ms: 1.04x slower                                                       |
| mako            | 11.0 ms                                                      | 11.4 ms: 1.04x slower                                                       |
| django_template | 40.2 ms                                                      | 43.8 ms: 1.09x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.05x slower                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220307-pythonperf2-x86_64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_loads              | 28.7 us                                                      | 23.9 us: 1.20x faster                                                       |
| json                    | 5.65 ms                                                      | 5.04 ms: 1.12x faster                                                       |
| logging_format          | 8.11 us                                                      | 7.75 us: 1.05x faster                                                       |
| chaos                   | 80.9 ms                                                      | 77.5 ms: 1.04x faster                                                       |
| python_startup          | 10.8 ms                                                      | 10.4 ms: 1.03x faster                                                       |
| python_startup_no_site  | 7.76 ms                                                      | 7.55 ms: 1.03x faster                                                       |
| xml_etree_parse         | 158 ms                                                       | 154 ms: 1.02x faster                                                        |
| nqueens                 | 103 ms                                                       | 100 ms: 1.02x faster                                                        |
| generators              | 56.0 ms                                                      | 54.8 ms: 1.02x faster                                                       |
| logging_simple          | 7.19 us                                                      | 7.08 us: 1.02x faster                                                       |
| coverage                | 84.8 ms                                                      | 84.1 ms: 1.01x faster                                                       |
| sympy_sum               | 185 ms                                                       | 184 ms: 1.00x faster                                                        |
| regex_effbot            | 3.50 ms                                                      | 3.49 ms: 1.00x faster                                                       |
| unpickle                | 13.4 us                                                      | 13.5 us: 1.01x slower                                                       |
| telco                   | 6.86 ms                                                      | 6.90 ms: 1.01x slower                                                       |
| asyncio_tcp             | 753 ms                                                       | 757 ms: 1.01x slower                                                        |
| pidigits                | 251 ms                                                       | 253 ms: 1.01x slower                                                        |
| sympy_integrate         | 25.8 ms                                                      | 25.9 ms: 1.01x slower                                                       |
| async_tree_io           | 1.17 sec                                                     | 1.19 sec: 1.01x slower                                                      |
| meteor_contest          | 131 ms                                                       | 133 ms: 1.01x slower                                                        |
| async_generators        | 316 ms                                                       | 320 ms: 1.01x slower                                                        |
| genshi_text             | 26.1 ms                                                      | 26.5 ms: 1.01x slower                                                       |
| pathlib                 | 19.1 ms                                                      | 19.3 ms: 1.01x slower                                                       |
| sqlite_synth            | 2.50 us                                                      | 2.54 us: 1.02x slower                                                       |
| json_dumps              | 13.4 ms                                                      | 13.6 ms: 1.02x slower                                                       |
| sympy_str               | 337 ms                                                       | 343 ms: 1.02x slower                                                        |
| aiohttp                 | 985 us                                                       | 1.00 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed | 749 ms                                                       | 763 ms: 1.02x slower                                                        |
| regex_compile           | 158 ms                                                       | 161 ms: 1.02x slower                                                        |
| gunicorn                | 973 us                                                       | 994 us: 1.02x slower                                                        |
| async_tree_none         | 519 ms                                                       | 532 ms: 1.02x slower                                                        |
| flaskblogging           | 3.88 ms                                                      | 3.99 ms: 1.03x slower                                                       |
| bench_thread_pool       | 1.01 ms                                                      | 1.04 ms: 1.03x slower                                                       |
| unpickle_list           | 4.53 us                                                      | 4.68 us: 1.03x slower                                                       |
| async_tree_memoization  | 630 ms                                                       | 651 ms: 1.03x slower                                                        |
| deepcopy                | 399 us                                                       | 413 us: 1.03x slower                                                        |
| sympy_expand            | 555 ms                                                       | 573 ms: 1.03x slower                                                        |
| pickle                  | 9.64 us                                                      | 9.96 us: 1.03x slower                                                       |
| html5lib                | 72.9 ms                                                      | 75.6 ms: 1.04x slower                                                       |
| genshi_xml              | 58.5 ms                                                      | 60.7 ms: 1.04x slower                                                       |
| xml_etree_generate      | 80.5 ms                                                      | 83.5 ms: 1.04x slower                                                       |
| bench_mp_pool           | 4.62 ms                                                      | 4.80 ms: 1.04x slower                                                       |
| sqlglot_normalize       | 126 ms                                                       | 131 ms: 1.04x slower                                                        |
| mako                    | 11.0 ms                                                      | 11.4 ms: 1.04x slower                                                       |
| 2to3                    | 288 ms                                                       | 300 ms: 1.04x slower                                                        |
| docutils                | 2.86 sec                                                     | 2.98 sec: 1.04x slower                                                      |
| sqlalchemy_imperative   | 20.1 ms                                                      | 21.0 ms: 1.05x slower                                                       |
| pickle_dict             | 30.8 us                                                      | 32.2 us: 1.05x slower                                                       |
| gc_traversal            | 3.85 ms                                                      | 4.03 ms: 1.05x slower                                                       |
| xml_etree_process       | 56.5 ms                                                      | 59.4 ms: 1.05x slower                                                       |
| fannkuch                | 429 ms                                                       | 453 ms: 1.06x slower                                                        |
| mdp                     | 2.75 sec                                                     | 2.91 sec: 1.06x slower                                                      |
| scimark_lu              | 115 ms                                                       | 122 ms: 1.06x slower                                                        |
| sqlalchemy_declarative  | 154 ms                                                       | 164 ms: 1.06x slower                                                        |
| deepcopy_reduce         | 3.51 us                                                      | 3.73 us: 1.06x slower                                                       |
| sqlglot_optimize        | 59.8 ms                                                      | 63.7 ms: 1.07x slower                                                       |
| float                   | 74.2 ms                                                      | 79.1 ms: 1.07x slower                                                       |
| tornado_http            | 122 ms                                                       | 130 ms: 1.07x slower                                                        |
| scimark_fft             | 285 ms                                                       | 305 ms: 1.07x slower                                                        |
| thrift                  | 925 us                                                       | 991 us: 1.07x slower                                                        |
| deepcopy_memo           | 38.8 us                                                      | 41.7 us: 1.07x slower                                                       |
| dask                    | 410 ms                                                       | 442 ms: 1.08x slower                                                        |
| dulwich_log             | 68.4 ms                                                      | 73.8 ms: 1.08x slower                                                       |
| pycparser               | 1.32 sec                                                     | 1.43 sec: 1.08x slower                                                      |
| nbody                   | 90.7 ms                                                      | 98.0 ms: 1.08x slower                                                       |
| go                      | 164 ms                                                       | 178 ms: 1.08x slower                                                        |
| raytrace                | 317 ms                                                       | 343 ms: 1.08x slower                                                        |
| hexiom                  | 7.13 ms                                                      | 7.74 ms: 1.08x slower                                                       |
| scimark_sor             | 111 ms                                                       | 121 ms: 1.09x slower                                                        |
| pprint_pformat          | 1.63 sec                                                     | 1.77 sec: 1.09x slower                                                      |
| pprint_safe_repr        | 784 ms                                                       | 853 ms: 1.09x slower                                                        |
| django_template         | 40.2 ms                                                      | 43.8 ms: 1.09x slower                                                       |
| scimark_monte_carlo     | 68.2 ms                                                      | 74.4 ms: 1.09x slower                                                       |
| coroutines              | 27.6 ms                                                      | 30.1 ms: 1.09x slower                                                       |
| chameleon               | 7.67 ms                                                      | 8.43 ms: 1.10x slower                                                       |
| regex_v8                | 23.9 ms                                                      | 26.4 ms: 1.10x slower                                                       |
| pyflate                 | 449 ms                                                       | 494 ms: 1.10x slower                                                        |
| pickle_pure_python      | 319 us                                                       | 352 us: 1.10x slower                                                        |
| scimark_sparse_mat_mult | 4.05 ms                                                      | 4.53 ms: 1.12x slower                                                       |
| pickle_list             | 3.83 us                                                      | 4.28 us: 1.12x slower                                                       |
| crypto_pyaes            | 83.4 ms                                                      | 93.5 ms: 1.12x slower                                                       |
| deltablue               | 4.00 ms                                                      | 4.49 ms: 1.12x slower                                                       |
| regex_dna               | 227 ms                                                       | 257 ms: 1.13x slower                                                        |
| unpickle_pure_python    | 241 us                                                       | 273 us: 1.13x slower                                                        |
| logging_silent          | 101 ns                                                       | 115 ns: 1.14x slower                                                        |
| richards                | 48.3 ms                                                      | 55.9 ms: 1.16x slower                                                       |
| spectral_norm           | 93.3 ms                                                      | 111 ms: 1.19x slower                                                        |
| comprehensions          | 24.6 us                                                      | 29.6 us: 1.20x slower                                                       |
| sqlglot_transpile       | 1.92 ms                                                      | 2.50 ms: 1.30x slower                                                       |
| sqlglot_parse           | 1.53 ms                                                      | 2.13 ms: 1.39x slower                                                       |
| unpack_sequence         | 45.6 ns                                                      | 152 ns: 3.33x slower                                                        |
| Geometric mean          | (ref)                                                        | 1.06x slower                                                                |

Benchmark hidden because not significant (2): xml_etree_iterparse, create_gc_cycles
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, mypy2, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x
