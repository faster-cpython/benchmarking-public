
# Results vs. 3.11.0

- fork: python
- ref: aad5f6a89125ad4529ab
- machine: linux-x86_64
- commit hash: aad5f6a
- commit date: 2023-02-07
- overall geometric mean: 1.22x slower \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-pythonperf2-x86_64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 351 ms: 1.22x slower                                                       |
| chameleon      | 7.67 ms                                                      | 9.41 ms: 1.23x slower                                                      |
| docutils       | 2.86 sec                                                     | 3.45 sec: 1.21x slower                                                     |
| html5lib       | 72.9 ms                                                      | 94.4 ms: 1.29x slower                                                      |
| tornado_http   | 122 ms                                                       | 159 ms: 1.31x slower                                                       |
| Geometric mean | (ref)                                                        | 1.25x slower                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-pythonperf2-x86_64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 251 ms                                                       | 271 ms: 1.08x slower                                                       |
| float          | 74.2 ms                                                      | 111 ms: 1.49x slower                                                       |
| nbody          | 90.7 ms                                                      | 138 ms: 1.52x slower                                                       |
| Geometric mean | (ref)                                                        | 1.35x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-pythonperf2-x86_64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.50 ms                                                      | 3.49 ms: 1.00x faster                                                      |
| regex_v8       | 23.9 ms                                                      | 27.2 ms: 1.14x slower                                                      |
| regex_dna      | 227 ms                                                       | 260 ms: 1.14x slower                                                       |
| regex_compile  | 158 ms                                                       | 192 ms: 1.22x slower                                                       |
| Geometric mean | (ref)                                                        | 1.12x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-pythonperf2-x86_64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle             | 13.4 us                                                      | 13.7 us: 1.02x slower                                                      |
| xml_etree_parse      | 158 ms                                                       | 164 ms: 1.04x slower                                                       |
| unpickle_list        | 4.53 us                                                      | 4.71 us: 1.04x slower                                                      |
| pickle_dict          | 30.8 us                                                      | 32.1 us: 1.04x slower                                                      |
| json_loads           | 28.7 us                                                      | 30.0 us: 1.04x slower                                                      |
| pickle               | 9.64 us                                                      | 10.1 us: 1.05x slower                                                      |
| json_dumps           | 13.4 ms                                                      | 14.4 ms: 1.08x slower                                                      |
| xml_etree_iterparse  | 104 ms                                                       | 113 ms: 1.09x slower                                                       |
| pickle_list          | 3.83 us                                                      | 4.17 us: 1.09x slower                                                      |
| xml_etree_generate   | 80.5 ms                                                      | 94.0 ms: 1.17x slower                                                      |
| unpickle_pure_python | 241 us                                                       | 320 us: 1.33x slower                                                       |
| xml_etree_process    | 56.5 ms                                                      | 77.5 ms: 1.37x slower                                                      |
| pickle_pure_python   | 319 us                                                       | 461 us: 1.44x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.13x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-pythonperf2-x86_64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 7.76 ms                                                      | 7.34 ms: 1.06x faster                                                      |
| python_startup         | 10.8 ms                                                      | 11.5 ms: 1.07x slower                                                      |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-pythonperf2-x86_64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 58.5 ms                                                      | 62.5 ms: 1.07x slower                                                      |
| genshi_text     | 26.1 ms                                                      | 32.0 ms: 1.22x slower                                                      |
| django_template | 40.2 ms                                                      | 53.6 ms: 1.33x slower                                                      |
| mako            | 11.0 ms                                                      | 14.7 ms: 1.34x slower                                                      |
| Geometric mean  | (ref)                                                        | 1.23x slower                                                               |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-pythonperf2-x86_64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|-------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| coverage                | 84.8 ms                                                      | 63.3 ms: 1.34x faster                                                      |
| python_startup_no_site  | 7.76 ms                                                      | 7.34 ms: 1.06x faster                                                      |
| regex_effbot            | 3.50 ms                                                      | 3.49 ms: 1.00x faster                                                      |
| generators              | 56.0 ms                                                      | 57.0 ms: 1.02x slower                                                      |
| unpickle                | 13.4 us                                                      | 13.7 us: 1.02x slower                                                      |
| asyncio_tcp             | 753 ms                                                       | 779 ms: 1.03x slower                                                       |
| xml_etree_parse         | 158 ms                                                       | 164 ms: 1.04x slower                                                       |
| unpickle_list           | 4.53 us                                                      | 4.71 us: 1.04x slower                                                      |
| pickle_dict             | 30.8 us                                                      | 32.1 us: 1.04x slower                                                      |
| json_loads              | 28.7 us                                                      | 30.0 us: 1.04x slower                                                      |
| json                    | 5.65 ms                                                      | 5.91 ms: 1.05x slower                                                      |
| pickle                  | 9.64 us                                                      | 10.1 us: 1.05x slower                                                      |
| telco                   | 6.86 ms                                                      | 7.25 ms: 1.06x slower                                                      |
| meteor_contest          | 131 ms                                                       | 139 ms: 1.06x slower                                                       |
| genshi_xml              | 58.5 ms                                                      | 62.5 ms: 1.07x slower                                                      |
| gc_traversal            | 3.85 ms                                                      | 4.12 ms: 1.07x slower                                                      |
| python_startup          | 10.8 ms                                                      | 11.5 ms: 1.07x slower                                                      |
| sympy_sum               | 185 ms                                                       | 199 ms: 1.08x slower                                                       |
| sympy_str               | 337 ms                                                       | 364 ms: 1.08x slower                                                       |
| json_dumps              | 13.4 ms                                                      | 14.4 ms: 1.08x slower                                                      |
| pidigits                | 251 ms                                                       | 271 ms: 1.08x slower                                                       |
| coroutines              | 27.6 ms                                                      | 29.9 ms: 1.08x slower                                                      |
| xml_etree_iterparse     | 104 ms                                                       | 113 ms: 1.09x slower                                                       |
| pickle_list             | 3.83 us                                                      | 4.17 us: 1.09x slower                                                      |
| bench_thread_pool       | 1.01 ms                                                      | 1.11 ms: 1.09x slower                                                      |
| fannkuch                | 429 ms                                                       | 470 ms: 1.10x slower                                                       |
| sympy_expand            | 555 ms                                                       | 608 ms: 1.10x slower                                                       |
| nqueens                 | 103 ms                                                       | 113 ms: 1.10x slower                                                       |
| comprehensions          | 24.6 us                                                      | 27.0 us: 1.10x slower                                                      |
| sympy_integrate         | 25.8 ms                                                      | 28.5 ms: 1.10x slower                                                      |
| pylint                  | 515 ms                                                       | 572 ms: 1.11x slower                                                       |
| mdp                     | 2.75 sec                                                     | 3.05 sec: 1.11x slower                                                     |
| pathlib                 | 19.1 ms                                                      | 21.3 ms: 1.12x slower                                                      |
| create_gc_cycles        | 1.61 ms                                                      | 1.81 ms: 1.13x slower                                                      |
| flaskblogging           | 3.88 ms                                                      | 4.40 ms: 1.13x slower                                                      |
| regex_v8                | 23.9 ms                                                      | 27.2 ms: 1.14x slower                                                      |
| sqlalchemy_imperative   | 20.1 ms                                                      | 22.9 ms: 1.14x slower                                                      |
| regex_dna               | 227 ms                                                       | 260 ms: 1.14x slower                                                       |
| deepcopy_reduce         | 3.51 us                                                      | 4.05 us: 1.15x slower                                                      |
| sqlglot_normalize       | 126 ms                                                       | 146 ms: 1.16x slower                                                       |
| gunicorn                | 973 us                                                       | 1.13 ms: 1.16x slower                                                      |
| sqlglot_optimize        | 59.8 ms                                                      | 69.6 ms: 1.16x slower                                                      |
| aiohttp                 | 985 us                                                       | 1.15 ms: 1.16x slower                                                      |
| xml_etree_generate      | 80.5 ms                                                      | 94.0 ms: 1.17x slower                                                      |
| deepcopy                | 399 us                                                       | 466 us: 1.17x slower                                                       |
| dask                    | 410 ms                                                       | 484 ms: 1.18x slower                                                       |
| dulwich_log             | 68.4 ms                                                      | 81.1 ms: 1.18x slower                                                      |
| logging_format          | 8.11 us                                                      | 9.67 us: 1.19x slower                                                      |
| sqlite_synth            | 2.50 us                                                      | 2.98 us: 1.19x slower                                                      |
| docutils                | 2.86 sec                                                     | 3.45 sec: 1.21x slower                                                     |
| sqlalchemy_declarative  | 154 ms                                                       | 187 ms: 1.22x slower                                                       |
| regex_compile           | 158 ms                                                       | 192 ms: 1.22x slower                                                       |
| 2to3                    | 288 ms                                                       | 351 ms: 1.22x slower                                                       |
| genshi_text             | 26.1 ms                                                      | 32.0 ms: 1.22x slower                                                      |
| chameleon               | 7.67 ms                                                      | 9.41 ms: 1.23x slower                                                      |
| logging_simple          | 7.19 us                                                      | 8.96 us: 1.25x slower                                                      |
| pycparser               | 1.32 sec                                                     | 1.67 sec: 1.26x slower                                                     |
| async_tree_cpu_io_mixed | 749 ms                                                       | 955 ms: 1.27x slower                                                       |
| deepcopy_memo           | 38.8 us                                                      | 50.0 us: 1.29x slower                                                      |
| pprint_pformat          | 1.63 sec                                                     | 2.11 sec: 1.29x slower                                                     |
| html5lib                | 72.9 ms                                                      | 94.4 ms: 1.29x slower                                                      |
| unpack_sequence         | 45.6 ns                                                      | 59.3 ns: 1.30x slower                                                      |
| scimark_sparse_mat_mult | 4.05 ms                                                      | 5.28 ms: 1.31x slower                                                      |
| thrift                  | 925 us                                                       | 1.21 ms: 1.31x slower                                                      |
| tornado_http            | 122 ms                                                       | 159 ms: 1.31x slower                                                       |
| pprint_safe_repr        | 784 ms                                                       | 1.03 sec: 1.31x slower                                                     |
| async_generators        | 316 ms                                                       | 417 ms: 1.32x slower                                                       |
| async_tree_memoization  | 630 ms                                                       | 832 ms: 1.32x slower                                                       |
| unpickle_pure_python    | 241 us                                                       | 320 us: 1.33x slower                                                       |
| hexiom                  | 7.13 ms                                                      | 9.49 ms: 1.33x slower                                                      |
| django_template         | 40.2 ms                                                      | 53.6 ms: 1.33x slower                                                      |
| mako                    | 11.0 ms                                                      | 14.7 ms: 1.34x slower                                                      |
| scimark_fft             | 285 ms                                                       | 383 ms: 1.34x slower                                                       |
| chaos                   | 80.9 ms                                                      | 109 ms: 1.35x slower                                                       |
| async_tree_none         | 519 ms                                                       | 711 ms: 1.37x slower                                                       |
| xml_etree_process       | 56.5 ms                                                      | 77.5 ms: 1.37x slower                                                      |
| async_tree_io           | 1.17 sec                                                     | 1.62 sec: 1.38x slower                                                     |
| sqlglot_transpile       | 1.92 ms                                                      | 2.70 ms: 1.41x slower                                                      |
| crypto_pyaes            | 83.4 ms                                                      | 118 ms: 1.42x slower                                                       |
| pickle_pure_python      | 319 us                                                       | 461 us: 1.44x slower                                                       |
| sqlglot_parse           | 1.53 ms                                                      | 2.25 ms: 1.47x slower                                                      |
| spectral_norm           | 93.3 ms                                                      | 138 ms: 1.48x slower                                                       |
| scimark_lu              | 115 ms                                                       | 170 ms: 1.49x slower                                                       |
| float                   | 74.2 ms                                                      | 111 ms: 1.49x slower                                                       |
| richards                | 48.3 ms                                                      | 72.9 ms: 1.51x slower                                                      |
| nbody                   | 90.7 ms                                                      | 138 ms: 1.52x slower                                                       |
| pyflate                 | 449 ms                                                       | 696 ms: 1.55x slower                                                       |
| raytrace                | 317 ms                                                       | 495 ms: 1.56x slower                                                       |
| bench_mp_pool           | 4.62 ms                                                      | 7.26 ms: 1.57x slower                                                      |
| go                      | 164 ms                                                       | 260 ms: 1.59x slower                                                       |
| scimark_sor             | 111 ms                                                       | 177 ms: 1.59x slower                                                       |
| scimark_monte_carlo     | 68.2 ms                                                      | 110 ms: 1.61x slower                                                       |
| logging_silent          | 101 ns                                                       | 165 ns: 1.64x slower                                                       |
| deltablue               | 4.00 ms                                                      | 7.45 ms: 1.86x slower                                                      |
| Geometric mean          | (ref)                                                        | 1.22x slower                                                               |

Benchmark hidden because not significant (1): mypy2
Ignored benchmarks (4) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.18x
- 95% likely to have a slowdown of 1.17x
- 99% likely to have a slowdown of 1.16x
