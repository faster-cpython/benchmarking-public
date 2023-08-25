
# Results vs. 3.11.0

- fork: python
- ref: b6bd7ffcbc1ffaa68e34
- machine: linux-x86_64
- commit hash: b6bd7ff
- commit date: 2022-12-06
- overall geometric mean: 1.03x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-pythonperf2-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 281 ms: 1.02x faster                                                        |
| chameleon      | 7.67 ms                                                      | 7.51 ms: 1.02x faster                                                       |
| docutils       | 2.86 sec                                                     | 2.76 sec: 1.04x faster                                                      |
| html5lib       | 72.9 ms                                                      | 66.2 ms: 1.10x faster                                                       |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-pythonperf2-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 74.2 ms                                                      | 73.2 ms: 1.01x faster                                                       |
| pidigits       | 251 ms                                                       | 250 ms: 1.00x faster                                                        |
| nbody          | 90.7 ms                                                      | 94.3 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-pythonperf2-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.9 ms                                                      | 22.3 ms: 1.07x faster                                                       |
| regex_compile  | 158 ms                                                       | 150 ms: 1.05x faster                                                        |
| regex_effbot   | 3.50 ms                                                      | 3.44 ms: 1.02x faster                                                       |
| regex_dna      | 227 ms                                                       | 233 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-pythonperf2-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.3 ms: 1.30x faster                                                       |
| json_loads           | 28.7 us                                                      | 24.2 us: 1.19x faster                                                       |
| unpickle_pure_python | 241 us                                                       | 212 us: 1.14x faster                                                        |
| xml_etree_parse      | 158 ms                                                       | 141 ms: 1.12x faster                                                        |
| unpickle             | 13.4 us                                                      | 13.1 us: 1.02x faster                                                       |
| xml_etree_generate   | 80.5 ms                                                      | 78.9 ms: 1.02x faster                                                       |
| xml_etree_process    | 56.5 ms                                                      | 55.6 ms: 1.02x faster                                                       |
| unpickle_list        | 4.53 us                                                      | 4.47 us: 1.01x faster                                                       |
| pickle_pure_python   | 319 us                                                       | 316 us: 1.01x faster                                                        |
| pickle_list          | 3.83 us                                                      | 3.90 us: 1.02x slower                                                       |
| pickle               | 9.64 us                                                      | 9.84 us: 1.02x slower                                                       |
| xml_etree_iterparse  | 104 ms                                                       | 108 ms: 1.03x slower                                                        |
| pickle_dict          | 30.8 us                                                      | 31.9 us: 1.04x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-pythonperf2-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 10.8 ms: 1.00x slower                                                       |
| python_startup_no_site | 7.76 ms                                                      | 7.86 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-pythonperf2-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 58.5 ms                                                      | 53.5 ms: 1.09x faster                                                       |
| mako            | 11.0 ms                                                      | 10.4 ms: 1.06x faster                                                       |
| django_template | 40.2 ms                                                      | 39.6 ms: 1.02x faster                                                       |
| genshi_text     | 26.1 ms                                                      | 25.8 ms: 1.01x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.04x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-pythonperf2-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps              | 13.4 ms                                                      | 10.3 ms: 1.30x faster                                                       |
| mypy2                   | 451 ms                                                       | 375 ms: 1.20x faster                                                        |
| json_loads              | 28.7 us                                                      | 24.2 us: 1.19x faster                                                       |
| scimark_lu              | 115 ms                                                       | 100 ms: 1.14x faster                                                        |
| unpickle_pure_python    | 241 us                                                       | 212 us: 1.14x faster                                                        |
| xml_etree_parse         | 158 ms                                                       | 141 ms: 1.12x faster                                                        |
| json                    | 5.65 ms                                                      | 5.11 ms: 1.11x faster                                                       |
| html5lib                | 72.9 ms                                                      | 66.2 ms: 1.10x faster                                                       |
| genshi_xml              | 58.5 ms                                                      | 53.5 ms: 1.09x faster                                                       |
| deltablue               | 4.00 ms                                                      | 3.67 ms: 1.09x faster                                                       |
| scimark_sparse_mat_mult | 4.05 ms                                                      | 3.73 ms: 1.08x faster                                                       |
| fannkuch                | 429 ms                                                       | 398 ms: 1.08x faster                                                        |
| regex_v8                | 23.9 ms                                                      | 22.3 ms: 1.07x faster                                                       |
| deepcopy_memo           | 38.8 us                                                      | 36.2 us: 1.07x faster                                                       |
| mako                    | 11.0 ms                                                      | 10.4 ms: 1.06x faster                                                       |
| hexiom                  | 7.13 ms                                                      | 6.73 ms: 1.06x faster                                                       |
| pycparser               | 1.32 sec                                                     | 1.26 sec: 1.05x faster                                                      |
| regex_compile           | 158 ms                                                       | 150 ms: 1.05x faster                                                        |
| deepcopy                | 399 us                                                       | 380 us: 1.05x faster                                                        |
| logging_format          | 8.11 us                                                      | 7.72 us: 1.05x faster                                                       |
| richards                | 48.3 ms                                                      | 46.1 ms: 1.05x faster                                                       |
| pprint_pformat          | 1.63 sec                                                     | 1.56 sec: 1.04x faster                                                      |
| deepcopy_reduce         | 3.51 us                                                      | 3.37 us: 1.04x faster                                                       |
| sqlglot_normalize       | 126 ms                                                       | 121 ms: 1.04x faster                                                        |
| telco                   | 6.86 ms                                                      | 6.60 ms: 1.04x faster                                                       |
| docutils                | 2.86 sec                                                     | 2.76 sec: 1.04x faster                                                      |
| bench_mp_pool           | 4.62 ms                                                      | 4.46 ms: 1.04x faster                                                       |
| thrift                  | 925 us                                                       | 894 us: 1.04x faster                                                        |
| pprint_safe_repr        | 784 ms                                                       | 758 ms: 1.03x faster                                                        |
| chaos                   | 80.9 ms                                                      | 78.3 ms: 1.03x faster                                                       |
| go                      | 164 ms                                                       | 159 ms: 1.03x faster                                                        |
| sympy_expand            | 555 ms                                                       | 539 ms: 1.03x faster                                                        |
| dulwich_log             | 68.4 ms                                                      | 66.7 ms: 1.03x faster                                                       |
| unpickle                | 13.4 us                                                      | 13.1 us: 1.02x faster                                                       |
| 2to3                    | 288 ms                                                       | 281 ms: 1.02x faster                                                        |
| sqlglot_transpile       | 1.92 ms                                                      | 1.87 ms: 1.02x faster                                                       |
| logging_simple          | 7.19 us                                                      | 7.03 us: 1.02x faster                                                       |
| chameleon               | 7.67 ms                                                      | 7.51 ms: 1.02x faster                                                       |
| sqlglot_optimize        | 59.8 ms                                                      | 58.5 ms: 1.02x faster                                                       |
| xml_etree_generate      | 80.5 ms                                                      | 78.9 ms: 1.02x faster                                                       |
| crypto_pyaes            | 83.4 ms                                                      | 81.8 ms: 1.02x faster                                                       |
| pyflate                 | 449 ms                                                       | 440 ms: 1.02x faster                                                        |
| sympy_str               | 337 ms                                                       | 331 ms: 1.02x faster                                                        |
| regex_effbot            | 3.50 ms                                                      | 3.44 ms: 1.02x faster                                                       |
| django_template         | 40.2 ms                                                      | 39.6 ms: 1.02x faster                                                       |
| scimark_sor             | 111 ms                                                       | 109 ms: 1.02x faster                                                        |
| gc_traversal            | 3.85 ms                                                      | 3.79 ms: 1.02x faster                                                       |
| xml_etree_process       | 56.5 ms                                                      | 55.6 ms: 1.02x faster                                                       |
| unpickle_list           | 4.53 us                                                      | 4.47 us: 1.01x faster                                                       |
| meteor_contest          | 131 ms                                                       | 129 ms: 1.01x faster                                                        |
| float                   | 74.2 ms                                                      | 73.2 ms: 1.01x faster                                                       |
| asyncio_tcp             | 753 ms                                                       | 743 ms: 1.01x faster                                                        |
| genshi_text             | 26.1 ms                                                      | 25.8 ms: 1.01x faster                                                       |
| logging_silent          | 101 ns                                                       | 99.7 ns: 1.01x faster                                                       |
| async_tree_memoization  | 630 ms                                                       | 623 ms: 1.01x faster                                                        |
| sqlglot_parse           | 1.53 ms                                                      | 1.52 ms: 1.01x faster                                                       |
| scimark_fft             | 285 ms                                                       | 282 ms: 1.01x faster                                                        |
| pickle_pure_python      | 319 us                                                       | 316 us: 1.01x faster                                                        |
| sympy_integrate         | 25.8 ms                                                      | 25.6 ms: 1.01x faster                                                       |
| nqueens                 | 103 ms                                                       | 102 ms: 1.01x faster                                                        |
| sympy_sum               | 185 ms                                                       | 183 ms: 1.01x faster                                                        |
| mdp                     | 2.75 sec                                                     | 2.73 sec: 1.01x faster                                                      |
| pidigits                | 251 ms                                                       | 250 ms: 1.00x faster                                                        |
| python_startup          | 10.8 ms                                                      | 10.8 ms: 1.00x slower                                                       |
| python_startup_no_site  | 7.76 ms                                                      | 7.86 ms: 1.01x slower                                                       |
| coroutines              | 27.6 ms                                                      | 28.0 ms: 1.02x slower                                                       |
| pickle_list             | 3.83 us                                                      | 3.90 us: 1.02x slower                                                       |
| pickle                  | 9.64 us                                                      | 9.84 us: 1.02x slower                                                       |
| async_tree_none         | 519 ms                                                       | 531 ms: 1.02x slower                                                        |
| async_tree_cpu_io_mixed | 749 ms                                                       | 767 ms: 1.02x slower                                                        |
| regex_dna               | 227 ms                                                       | 233 ms: 1.03x slower                                                        |
| spectral_norm           | 93.3 ms                                                      | 96.2 ms: 1.03x slower                                                       |
| xml_etree_iterparse     | 104 ms                                                       | 108 ms: 1.03x slower                                                        |
| raytrace                | 317 ms                                                       | 327 ms: 1.03x slower                                                        |
| pickle_dict             | 30.8 us                                                      | 31.9 us: 1.04x slower                                                       |
| nbody                   | 90.7 ms                                                      | 94.3 ms: 1.04x slower                                                       |
| sqlite_synth            | 2.50 us                                                      | 2.60 us: 1.04x slower                                                       |
| async_generators        | 316 ms                                                       | 335 ms: 1.06x slower                                                        |
| scimark_monte_carlo     | 68.2 ms                                                      | 72.7 ms: 1.07x slower                                                       |
| generators              | 56.0 ms                                                      | 60.8 ms: 1.09x slower                                                       |
| comprehensions          | 24.6 us                                                      | 27.3 us: 1.11x slower                                                       |
| Geometric mean          | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (7): bench_thread_pool, create_gc_cycles, unpack_sequence, dask, pathlib, coverage, async_tree_io
Ignored benchmarks (11) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x
