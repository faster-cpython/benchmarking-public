
# Results vs. 3.11.0

- fork: python
- ref: 7d4cc5aa854fdea4d01a
- machine: linux-x86_64
- commit hash: 7d4cc5a
- commit date: 2023-04-04
- overall geometric mean: 1.21x slower \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-pythonperf2-x86_64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 350 ms: 1.22x slower                                                       |
| chameleon      | 7.67 ms                                                      | 9.41 ms: 1.23x slower                                                      |
| docutils       | 2.86 sec                                                     | 3.42 sec: 1.20x slower                                                     |
| html5lib       | 72.9 ms                                                      | 93.6 ms: 1.28x slower                                                      |
| tornado_http   | 122 ms                                                       | 150 ms: 1.24x slower                                                       |
| Geometric mean | (ref)                                                        | 1.23x slower                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-pythonperf2-x86_64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 251 ms                                                       | 271 ms: 1.08x slower                                                       |
| float          | 74.2 ms                                                      | 110 ms: 1.49x slower                                                       |
| nbody          | 90.7 ms                                                      | 137 ms: 1.51x slower                                                       |
| Geometric mean | (ref)                                                        | 1.34x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-pythonperf2-x86_64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.50 ms                                                      | 3.25 ms: 1.08x faster                                                      |
| regex_v8       | 23.9 ms                                                      | 27.1 ms: 1.13x slower                                                      |
| regex_dna      | 227 ms                                                       | 259 ms: 1.14x slower                                                       |
| regex_compile  | 158 ms                                                       | 191 ms: 1.21x slower                                                       |
| Geometric mean | (ref)                                                        | 1.10x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-pythonperf2-x86_64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_dict          | 30.8 us                                                      | 31.1 us: 1.01x slower                                                      |
| xml_etree_parse      | 158 ms                                                       | 160 ms: 1.01x slower                                                       |
| unpickle_list        | 4.53 us                                                      | 4.61 us: 1.02x slower                                                      |
| xml_etree_iterparse  | 104 ms                                                       | 109 ms: 1.05x slower                                                       |
| unpickle             | 13.4 us                                                      | 14.1 us: 1.05x slower                                                      |
| pickle               | 9.64 us                                                      | 10.1 us: 1.05x slower                                                      |
| json_loads           | 28.7 us                                                      | 30.2 us: 1.05x slower                                                      |
| pickle_list          | 3.83 us                                                      | 4.04 us: 1.05x slower                                                      |
| json_dumps           | 13.4 ms                                                      | 14.4 ms: 1.08x slower                                                      |
| xml_etree_generate   | 80.5 ms                                                      | 92.8 ms: 1.15x slower                                                      |
| unpickle_pure_python | 241 us                                                       | 313 us: 1.30x slower                                                       |
| xml_etree_process    | 56.5 ms                                                      | 76.5 ms: 1.35x slower                                                      |
| pickle_pure_python   | 319 us                                                       | 454 us: 1.42x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.12x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-pythonperf2-x86_64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 7.76 ms                                                      | 7.35 ms: 1.06x faster                                                      |
| python_startup         | 10.8 ms                                                      | 11.5 ms: 1.07x slower                                                      |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-pythonperf2-x86_64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 58.5 ms                                                      | 63.7 ms: 1.09x slower                                                      |
| genshi_text     | 26.1 ms                                                      | 31.7 ms: 1.21x slower                                                      |
| django_template | 40.2 ms                                                      | 53.2 ms: 1.32x slower                                                      |
| mako            | 11.0 ms                                                      | 14.9 ms: 1.36x slower                                                      |
| Geometric mean  | (ref)                                                        | 1.24x slower                                                               |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-pythonperf2-x86_64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|-------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| coverage                | 84.8 ms                                                      | 63.5 ms: 1.33x faster                                                      |
| regex_effbot            | 3.50 ms                                                      | 3.25 ms: 1.08x faster                                                      |
| python_startup_no_site  | 7.76 ms                                                      | 7.35 ms: 1.06x faster                                                      |
| gc_traversal            | 3.85 ms                                                      | 3.68 ms: 1.05x faster                                                      |
| pickle_dict             | 30.8 us                                                      | 31.1 us: 1.01x slower                                                      |
| xml_etree_parse         | 158 ms                                                       | 160 ms: 1.01x slower                                                       |
| unpickle_list           | 4.53 us                                                      | 4.61 us: 1.02x slower                                                      |
| generators              | 56.0 ms                                                      | 57.8 ms: 1.03x slower                                                      |
| asyncio_tcp             | 753 ms                                                       | 781 ms: 1.04x slower                                                       |
| telco                   | 6.86 ms                                                      | 7.16 ms: 1.04x slower                                                      |
| xml_etree_iterparse     | 104 ms                                                       | 109 ms: 1.05x slower                                                       |
| unpickle                | 13.4 us                                                      | 14.1 us: 1.05x slower                                                      |
| pickle                  | 9.64 us                                                      | 10.1 us: 1.05x slower                                                      |
| json_loads              | 28.7 us                                                      | 30.2 us: 1.05x slower                                                      |
| pickle_list             | 3.83 us                                                      | 4.04 us: 1.05x slower                                                      |
| json                    | 5.65 ms                                                      | 5.97 ms: 1.06x slower                                                      |
| meteor_contest          | 131 ms                                                       | 139 ms: 1.06x slower                                                       |
| python_startup          | 10.8 ms                                                      | 11.5 ms: 1.07x slower                                                      |
| sympy_sum               | 185 ms                                                       | 199 ms: 1.07x slower                                                       |
| json_dumps              | 13.4 ms                                                      | 14.4 ms: 1.08x slower                                                      |
| pidigits                | 251 ms                                                       | 271 ms: 1.08x slower                                                       |
| sympy_str               | 337 ms                                                       | 366 ms: 1.09x slower                                                       |
| genshi_xml              | 58.5 ms                                                      | 63.7 ms: 1.09x slower                                                      |
| bench_thread_pool       | 1.01 ms                                                      | 1.10 ms: 1.09x slower                                                      |
| nqueens                 | 103 ms                                                       | 112 ms: 1.09x slower                                                       |
| coroutines              | 27.6 ms                                                      | 30.2 ms: 1.10x slower                                                      |
| comprehensions          | 24.6 us                                                      | 27.1 us: 1.10x slower                                                      |
| sympy_integrate         | 25.8 ms                                                      | 28.4 ms: 1.10x slower                                                      |
| pathlib                 | 19.1 ms                                                      | 21.0 ms: 1.10x slower                                                      |
| sympy_expand            | 555 ms                                                       | 615 ms: 1.11x slower                                                       |
| pylint                  | 515 ms                                                       | 572 ms: 1.11x slower                                                       |
| fannkuch                | 429 ms                                                       | 477 ms: 1.11x slower                                                       |
| flaskblogging           | 3.88 ms                                                      | 4.33 ms: 1.12x slower                                                      |
| dask                    | 410 ms                                                       | 459 ms: 1.12x slower                                                       |
| create_gc_cycles        | 1.61 ms                                                      | 1.82 ms: 1.13x slower                                                      |
| regex_v8                | 23.9 ms                                                      | 27.1 ms: 1.13x slower                                                      |
| deepcopy_reduce         | 3.51 us                                                      | 3.99 us: 1.13x slower                                                      |
| mdp                     | 2.75 sec                                                     | 3.12 sec: 1.14x slower                                                     |
| regex_dna               | 227 ms                                                       | 259 ms: 1.14x slower                                                       |
| sqlalchemy_imperative   | 20.1 ms                                                      | 23.0 ms: 1.15x slower                                                      |
| sqlglot_normalize       | 126 ms                                                       | 144 ms: 1.15x slower                                                       |
| xml_etree_generate      | 80.5 ms                                                      | 92.8 ms: 1.15x slower                                                      |
| sqlglot_optimize        | 59.8 ms                                                      | 69.1 ms: 1.15x slower                                                      |
| gunicorn                | 973 us                                                       | 1.13 ms: 1.16x slower                                                      |
| deepcopy                | 399 us                                                       | 465 us: 1.16x slower                                                       |
| aiohttp                 | 985 us                                                       | 1.15 ms: 1.17x slower                                                      |
| dulwich_log             | 68.4 ms                                                      | 80.1 ms: 1.17x slower                                                      |
| logging_format          | 8.11 us                                                      | 9.57 us: 1.18x slower                                                      |
| sqlite_synth            | 2.50 us                                                      | 2.97 us: 1.19x slower                                                      |
| docutils                | 2.86 sec                                                     | 3.42 sec: 1.20x slower                                                     |
| genshi_text             | 26.1 ms                                                      | 31.7 ms: 1.21x slower                                                      |
| regex_compile           | 158 ms                                                       | 191 ms: 1.21x slower                                                       |
| 2to3                    | 288 ms                                                       | 350 ms: 1.22x slower                                                       |
| pycparser               | 1.32 sec                                                     | 1.61 sec: 1.22x slower                                                     |
| sqlalchemy_declarative  | 154 ms                                                       | 188 ms: 1.22x slower                                                       |
| chameleon               | 7.67 ms                                                      | 9.41 ms: 1.23x slower                                                      |
| tornado_http            | 122 ms                                                       | 150 ms: 1.24x slower                                                       |
| logging_simple          | 7.19 us                                                      | 8.94 us: 1.24x slower                                                      |
| thrift                  | 925 us                                                       | 1.17 ms: 1.26x slower                                                      |
| scimark_fft             | 285 ms                                                       | 360 ms: 1.26x slower                                                       |
| async_tree_cpu_io_mixed | 749 ms                                                       | 952 ms: 1.27x slower                                                       |
| html5lib                | 72.9 ms                                                      | 93.6 ms: 1.28x slower                                                      |
| scimark_sparse_mat_mult | 4.05 ms                                                      | 5.22 ms: 1.29x slower                                                      |
| chaos                   | 80.9 ms                                                      | 105 ms: 1.30x slower                                                       |
| unpickle_pure_python    | 241 us                                                       | 313 us: 1.30x slower                                                       |
| unpack_sequence         | 45.6 ns                                                      | 59.4 ns: 1.30x slower                                                      |
| async_tree_memoization  | 630 ms                                                       | 827 ms: 1.31x slower                                                       |
| pprint_pformat          | 1.63 sec                                                     | 2.14 sec: 1.32x slower                                                     |
| deepcopy_memo           | 38.8 us                                                      | 51.1 us: 1.32x slower                                                      |
| pprint_safe_repr        | 784 ms                                                       | 1.03 sec: 1.32x slower                                                     |
| hexiom                  | 7.13 ms                                                      | 9.43 ms: 1.32x slower                                                      |
| django_template         | 40.2 ms                                                      | 53.2 ms: 1.32x slower                                                      |
| async_generators        | 316 ms                                                       | 418 ms: 1.32x slower                                                       |
| async_tree_none         | 519 ms                                                       | 695 ms: 1.34x slower                                                       |
| xml_etree_process       | 56.5 ms                                                      | 76.5 ms: 1.35x slower                                                      |
| mako                    | 11.0 ms                                                      | 14.9 ms: 1.36x slower                                                      |
| async_tree_io           | 1.17 sec                                                     | 1.61 sec: 1.37x slower                                                     |
| crypto_pyaes            | 83.4 ms                                                      | 115 ms: 1.37x slower                                                       |
| sqlglot_transpile       | 1.92 ms                                                      | 2.69 ms: 1.40x slower                                                      |
| scimark_lu              | 115 ms                                                       | 161 ms: 1.41x slower                                                       |
| pickle_pure_python      | 319 us                                                       | 454 us: 1.42x slower                                                       |
| spectral_norm           | 93.3 ms                                                      | 137 ms: 1.47x slower                                                       |
| sqlglot_parse           | 1.53 ms                                                      | 2.26 ms: 1.47x slower                                                      |
| bench_mp_pool           | 4.62 ms                                                      | 6.82 ms: 1.48x slower                                                      |
| float                   | 74.2 ms                                                      | 110 ms: 1.49x slower                                                       |
| nbody                   | 90.7 ms                                                      | 137 ms: 1.51x slower                                                       |
| richards                | 48.3 ms                                                      | 74.5 ms: 1.54x slower                                                      |
| pyflate                 | 449 ms                                                       | 693 ms: 1.55x slower                                                       |
| raytrace                | 317 ms                                                       | 491 ms: 1.55x slower                                                       |
| scimark_sor             | 111 ms                                                       | 176 ms: 1.59x slower                                                       |
| go                      | 164 ms                                                       | 264 ms: 1.61x slower                                                       |
| scimark_monte_carlo     | 68.2 ms                                                      | 110 ms: 1.62x slower                                                       |
| logging_silent          | 101 ns                                                       | 166 ns: 1.64x slower                                                       |
| deltablue               | 4.00 ms                                                      | 7.44 ms: 1.86x slower                                                      |
| Geometric mean          | (ref)                                                        | 1.21x slower                                                               |

Benchmark hidden because not significant (1): mypy2
Ignored benchmarks (4) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.17x
- 95% likely to have a slowdown of 1.16x
- 99% likely to have a slowdown of 1.14x
