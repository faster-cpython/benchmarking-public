
# Results vs. 3.11.0

- fork: python
- ref: 70be5e42f6e288de32e0
- machine: linux-x86_64
- commit hash: 70be5e4
- commit date: 2022-12-11
- overall geometric mean: 1.03x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221211-pythonperf2-x86_64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 281 ms: 1.02x faster                                                         |
| chameleon      | 7.67 ms                                                      | 7.48 ms: 1.03x faster                                                        |
| docutils       | 2.86 sec                                                     | 2.78 sec: 1.03x faster                                                       |
| html5lib       | 72.9 ms                                                      | 67.6 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221211-pythonperf2-x86_64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 89.3 ms: 1.02x faster                                                        |
| float          | 74.2 ms                                                      | 73.3 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221211-pythonperf2-x86_64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 150 ms: 1.05x faster                                                         |
| regex_effbot   | 3.50 ms                                                      | 3.43 ms: 1.02x faster                                                        |
| regex_v8       | 23.9 ms                                                      | 23.7 ms: 1.01x faster                                                        |
| regex_dna      | 227 ms                                                       | 236 ms: 1.04x slower                                                         |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221211-pythonperf2-x86_64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.3 ms: 1.30x faster                                                        |
| json_loads           | 28.7 us                                                      | 24.0 us: 1.19x faster                                                        |
| xml_etree_parse      | 158 ms                                                       | 141 ms: 1.12x faster                                                         |
| unpickle_pure_python | 241 us                                                       | 216 us: 1.11x faster                                                         |
| unpickle_list        | 4.53 us                                                      | 4.33 us: 1.05x faster                                                        |
| xml_etree_process    | 56.5 ms                                                      | 54.3 ms: 1.04x faster                                                        |
| unpickle             | 13.4 us                                                      | 13.0 us: 1.04x faster                                                        |
| pickle_list          | 3.83 us                                                      | 3.70 us: 1.03x faster                                                        |
| pickle_pure_python   | 319 us                                                       | 311 us: 1.03x faster                                                         |
| xml_etree_generate   | 80.5 ms                                                      | 79.5 ms: 1.01x faster                                                        |
| pickle               | 9.64 us                                                      | 9.71 us: 1.01x slower                                                        |
| xml_etree_iterparse  | 104 ms                                                       | 107 ms: 1.02x slower                                                         |
| pickle_dict          | 30.8 us                                                      | 31.6 us: 1.03x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.06x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221211-pythonperf2-x86_64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 10.8 ms: 1.00x slower                                                        |
| python_startup_no_site | 7.76 ms                                                      | 7.85 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221211-pythonperf2-x86_64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 58.5 ms                                                      | 53.1 ms: 1.10x faster                                                        |
| mako            | 11.0 ms                                                      | 10.2 ms: 1.07x faster                                                        |
| genshi_text     | 26.1 ms                                                      | 24.4 ms: 1.07x faster                                                        |
| django_template | 40.2 ms                                                      | 39.6 ms: 1.02x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.07x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221211-pythonperf2-x86_64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps              | 13.4 ms                                                      | 10.3 ms: 1.30x faster                                                        |
| mypy2                   | 451 ms                                                       | 373 ms: 1.21x faster                                                         |
| json_loads              | 28.7 us                                                      | 24.0 us: 1.19x faster                                                        |
| scimark_lu              | 115 ms                                                       | 101 ms: 1.13x faster                                                         |
| xml_etree_parse         | 158 ms                                                       | 141 ms: 1.12x faster                                                         |
| json                    | 5.65 ms                                                      | 5.04 ms: 1.12x faster                                                        |
| unpickle_pure_python    | 241 us                                                       | 216 us: 1.11x faster                                                         |
| genshi_xml              | 58.5 ms                                                      | 53.1 ms: 1.10x faster                                                        |
| scimark_sparse_mat_mult | 4.05 ms                                                      | 3.74 ms: 1.08x faster                                                        |
| html5lib                | 72.9 ms                                                      | 67.6 ms: 1.08x faster                                                        |
| mako                    | 11.0 ms                                                      | 10.2 ms: 1.07x faster                                                        |
| deepcopy_memo           | 38.8 us                                                      | 36.2 us: 1.07x faster                                                        |
| deltablue               | 4.00 ms                                                      | 3.73 ms: 1.07x faster                                                        |
| deepcopy                | 399 us                                                       | 373 us: 1.07x faster                                                         |
| genshi_text             | 26.1 ms                                                      | 24.4 ms: 1.07x faster                                                        |
| logging_format          | 8.11 us                                                      | 7.59 us: 1.07x faster                                                        |
| asyncio_tcp             | 753 ms                                                       | 709 ms: 1.06x faster                                                         |
| fannkuch                | 429 ms                                                       | 405 ms: 1.06x faster                                                         |
| deepcopy_reduce         | 3.51 us                                                      | 3.33 us: 1.05x faster                                                        |
| bench_thread_pool       | 1.01 ms                                                      | 963 us: 1.05x faster                                                         |
| regex_compile           | 158 ms                                                       | 150 ms: 1.05x faster                                                         |
| scimark_sor             | 111 ms                                                       | 106 ms: 1.05x faster                                                         |
| unpickle_list           | 4.53 us                                                      | 4.33 us: 1.05x faster                                                        |
| nqueens                 | 103 ms                                                       | 98.2 ms: 1.05x faster                                                        |
| chaos                   | 80.9 ms                                                      | 77.2 ms: 1.05x faster                                                        |
| logging_simple          | 7.19 us                                                      | 6.87 us: 1.05x faster                                                        |
| sqlglot_normalize       | 126 ms                                                       | 120 ms: 1.05x faster                                                         |
| telco                   | 6.86 ms                                                      | 6.56 ms: 1.05x faster                                                        |
| xml_etree_process       | 56.5 ms                                                      | 54.3 ms: 1.04x faster                                                        |
| mdp                     | 2.75 sec                                                     | 2.65 sec: 1.04x faster                                                       |
| unpickle                | 13.4 us                                                      | 13.0 us: 1.04x faster                                                        |
| pickle_list             | 3.83 us                                                      | 3.70 us: 1.03x faster                                                        |
| pprint_pformat          | 1.63 sec                                                     | 1.58 sec: 1.03x faster                                                       |
| docutils                | 2.86 sec                                                     | 2.78 sec: 1.03x faster                                                       |
| sqlglot_optimize        | 59.8 ms                                                      | 58.1 ms: 1.03x faster                                                        |
| richards                | 48.3 ms                                                      | 47.0 ms: 1.03x faster                                                        |
| hexiom                  | 7.13 ms                                                      | 6.94 ms: 1.03x faster                                                        |
| pyflate                 | 449 ms                                                       | 437 ms: 1.03x faster                                                         |
| pickle_pure_python      | 319 us                                                       | 311 us: 1.03x faster                                                         |
| chameleon               | 7.67 ms                                                      | 7.48 ms: 1.03x faster                                                        |
| gc_traversal            | 3.85 ms                                                      | 3.75 ms: 1.03x faster                                                        |
| dulwich_log             | 68.4 ms                                                      | 66.7 ms: 1.03x faster                                                        |
| sympy_expand            | 555 ms                                                       | 541 ms: 1.02x faster                                                         |
| 2to3                    | 288 ms                                                       | 281 ms: 1.02x faster                                                         |
| scimark_fft             | 285 ms                                                       | 278 ms: 1.02x faster                                                         |
| regex_effbot            | 3.50 ms                                                      | 3.43 ms: 1.02x faster                                                        |
| thrift                  | 925 us                                                       | 905 us: 1.02x faster                                                         |
| async_tree_memoization  | 630 ms                                                       | 618 ms: 1.02x faster                                                         |
| pycparser               | 1.32 sec                                                     | 1.30 sec: 1.02x faster                                                       |
| django_template         | 40.2 ms                                                      | 39.6 ms: 1.02x faster                                                        |
| sqlglot_transpile       | 1.92 ms                                                      | 1.89 ms: 1.02x faster                                                        |
| pprint_safe_repr        | 784 ms                                                       | 771 ms: 1.02x faster                                                         |
| create_gc_cycles        | 1.61 ms                                                      | 1.58 ms: 1.02x faster                                                        |
| pathlib                 | 19.1 ms                                                      | 18.8 ms: 1.02x faster                                                        |
| nbody                   | 90.7 ms                                                      | 89.3 ms: 1.02x faster                                                        |
| logging_silent          | 101 ns                                                       | 99.3 ns: 1.01x faster                                                        |
| meteor_contest          | 131 ms                                                       | 129 ms: 1.01x faster                                                         |
| xml_etree_generate      | 80.5 ms                                                      | 79.5 ms: 1.01x faster                                                        |
| float                   | 74.2 ms                                                      | 73.3 ms: 1.01x faster                                                        |
| scimark_monte_carlo     | 68.2 ms                                                      | 67.5 ms: 1.01x faster                                                        |
| regex_v8                | 23.9 ms                                                      | 23.7 ms: 1.01x faster                                                        |
| sympy_str               | 337 ms                                                       | 335 ms: 1.01x faster                                                         |
| python_startup          | 10.8 ms                                                      | 10.8 ms: 1.00x slower                                                        |
| coroutines              | 27.6 ms                                                      | 27.7 ms: 1.01x slower                                                        |
| crypto_pyaes            | 83.4 ms                                                      | 84.0 ms: 1.01x slower                                                        |
| pickle                  | 9.64 us                                                      | 9.71 us: 1.01x slower                                                        |
| raytrace                | 317 ms                                                       | 320 ms: 1.01x slower                                                         |
| python_startup_no_site  | 7.76 ms                                                      | 7.85 ms: 1.01x slower                                                        |
| async_tree_cpu_io_mixed | 749 ms                                                       | 760 ms: 1.01x slower                                                         |
| coverage                | 84.8 ms                                                      | 86.1 ms: 1.02x slower                                                        |
| go                      | 164 ms                                                       | 167 ms: 1.02x slower                                                         |
| xml_etree_iterparse     | 104 ms                                                       | 107 ms: 1.02x slower                                                         |
| spectral_norm           | 93.3 ms                                                      | 95.6 ms: 1.02x slower                                                        |
| sympy_sum               | 185 ms                                                       | 189 ms: 1.03x slower                                                         |
| pickle_dict             | 30.8 us                                                      | 31.6 us: 1.03x slower                                                        |
| regex_dna               | 227 ms                                                       | 236 ms: 1.04x slower                                                         |
| async_generators        | 316 ms                                                       | 328 ms: 1.04x slower                                                         |
| sqlite_synth            | 2.50 us                                                      | 2.61 us: 1.04x slower                                                        |
| comprehensions          | 24.6 us                                                      | 26.8 us: 1.09x slower                                                        |
| generators              | 56.0 ms                                                      | 61.2 ms: 1.09x slower                                                        |
| Geometric mean          | (ref)                                                        | 1.03x faster                                                                 |

Benchmark hidden because not significant (8): async_tree_io, sympy_integrate, sqlglot_parse, pidigits, unpack_sequence, bench_mp_pool, async_tree_none, dask
Ignored benchmarks (11) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x
