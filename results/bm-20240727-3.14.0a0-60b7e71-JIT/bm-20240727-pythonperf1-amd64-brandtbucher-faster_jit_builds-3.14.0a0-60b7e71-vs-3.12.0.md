# Results vs. 3.12.0

- fork: brandtbucher
- ref: faster_jit_builds
- machine: windows-amd64
- commit hash: 60b7e71
- commit date: 2024-07-27
- overall geometric mean: 1.07x faster
- HPT reliability: 95.20%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 238 ms: 1.09x slower                                                          |
| docutils       | 1.66 sec                                                    | 1.83 sec: 1.10x slower                                                        |
| tornado_http   | 89.5 ms                                                     | 94.0 ms: 1.05x slower                                                         |
| Geometric mean | (ref)                                                       | 1.08x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 187 ms: 1.53x faster                                                          |
| async_tree_memoization_tg  | 367 ms                                                      | 242 ms: 1.52x faster                                                          |
| async_tree_io_tg           | 771 ms                                                      | 526 ms: 1.47x faster                                                          |
| async_tree_none            | 291 ms                                                      | 208 ms: 1.40x faster                                                          |
| async_tree_io              | 731 ms                                                      | 536 ms: 1.37x faster                                                          |
| async_tree_memoization     | 339 ms                                                      | 255 ms: 1.33x faster                                                          |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 384 ms: 1.31x faster                                                          |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 383 ms: 1.28x faster                                                          |
| Geometric mean             | (ref)                                                       | 1.40x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 50.9 ms: 1.41x faster                                                         |
| float          | 56.8 ms                                                     | 43.9 ms: 1.29x faster                                                         |
| pidigits       | 152 ms                                                      | 150 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                       | 1.23x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 121 ms: 1.05x faster                                                          |
| regex_effbot   | 1.62 ms                                                     | 1.60 ms: 1.01x faster                                                         |
| regex_compile  | 87.5 ms                                                     | 89.4 ms: 1.02x slower                                                         |
| regex_v8       | 14.2 ms                                                     | 15.5 ms: 1.09x slower                                                         |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.25 sec: 1.10x faster                                                        |
| pickle_pure_python   | 195 us                                                      | 181 us: 1.08x faster                                                          |
| xml_etree_generate   | 55.8 ms                                                     | 52.5 ms: 1.06x faster                                                         |
| xml_etree_iterparse  | 65.2 ms                                                     | 61.8 ms: 1.05x faster                                                         |
| unpickle_pure_python | 133 us                                                      | 130 us: 1.03x faster                                                          |
| xml_etree_process    | 37.7 ms                                                     | 37.2 ms: 1.01x faster                                                         |
| json_dumps           | 5.70 ms                                                     | 5.80 ms: 1.02x slower                                                         |
| json_loads           | 13.9 us                                                     | 14.2 us: 1.02x slower                                                         |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                                  |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.2 ms: 1.12x slower                                                         |
| python_startup         | 19.5 ms                                                     | 22.0 ms: 1.13x slower                                                         |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 4.98 ms: 1.42x faster                                                         |
| django_template | 22.9 ms                                                     | 25.5 ms: 1.11x slower                                                         |
| Geometric mean  | (ref)                                                       | 1.13x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| deepcopy_memo              | 23.7 us                                                     | 15.5 us: 1.53x faster                                                         |
| async_tree_none_tg         | 285 ms                                                      | 187 ms: 1.53x faster                                                          |
| async_tree_memoization_tg  | 367 ms                                                      | 242 ms: 1.52x faster                                                          |
| async_tree_io_tg           | 771 ms                                                      | 526 ms: 1.47x faster                                                          |
| spectral_norm              | 66.9 ms                                                     | 46.1 ms: 1.45x faster                                                         |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.46 sec: 1.43x faster                                                        |
| mako                       | 7.09 ms                                                     | 4.98 ms: 1.42x faster                                                         |
| nbody                      | 71.9 ms                                                     | 50.9 ms: 1.41x faster                                                         |
| async_tree_none            | 291 ms                                                      | 208 ms: 1.40x faster                                                          |
| comprehensions             | 14.1 us                                                     | 10.2 us: 1.38x faster                                                         |
| async_tree_io              | 731 ms                                                      | 536 ms: 1.37x faster                                                          |
| async_tree_memoization     | 339 ms                                                      | 255 ms: 1.33x faster                                                          |
| deepcopy                   | 238 us                                                      | 182 us: 1.31x faster                                                          |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 384 ms: 1.31x faster                                                          |
| float                      | 56.8 ms                                                     | 43.9 ms: 1.29x faster                                                         |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 383 ms: 1.28x faster                                                          |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.01 ms: 1.27x faster                                                         |
| scimark_fft                | 184 ms                                                      | 149 ms: 1.24x faster                                                          |
| crypto_pyaes               | 48.5 ms                                                     | 40.5 ms: 1.20x faster                                                         |
| pyflate                    | 295 ms                                                      | 247 ms: 1.19x faster                                                          |
| scimark_monte_carlo        | 43.7 ms                                                     | 37.4 ms: 1.17x faster                                                         |
| deepcopy_reduce            | 2.09 us                                                     | 1.83 us: 1.15x faster                                                         |
| fannkuch                   | 247 ms                                                      | 219 ms: 1.13x faster                                                          |
| pprint_pformat             | 1.05 sec                                                    | 950 ms: 1.10x faster                                                          |
| pprint_safe_repr           | 513 ms                                                      | 468 ms: 1.10x faster                                                          |
| raytrace                   | 192 ms                                                      | 176 ms: 1.10x faster                                                          |
| tomli_loads                | 1.37 sec                                                    | 1.25 sec: 1.10x faster                                                        |
| logging_silent             | 60.5 ns                                                     | 55.4 ns: 1.09x faster                                                         |
| chaos                      | 43.3 ms                                                     | 39.7 ms: 1.09x faster                                                         |
| logging_simple             | 6.28 us                                                     | 5.80 us: 1.08x faster                                                         |
| pickle_pure_python         | 195 us                                                      | 181 us: 1.08x faster                                                          |
| logging_format             | 6.72 us                                                     | 6.24 us: 1.08x faster                                                         |
| coroutines                 | 14.3 ms                                                     | 13.3 ms: 1.07x faster                                                         |
| nqueens                    | 62.8 ms                                                     | 59.0 ms: 1.06x faster                                                         |
| xml_etree_generate         | 55.8 ms                                                     | 52.5 ms: 1.06x faster                                                         |
| dulwich_log                | 44.3 ms                                                     | 41.8 ms: 1.06x faster                                                         |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.8 ms: 1.05x faster                                                         |
| bench_thread_pool          | 857 us                                                      | 815 us: 1.05x faster                                                          |
| regex_dna                  | 126 ms                                                      | 121 ms: 1.05x faster                                                          |
| generators                 | 22.5 ms                                                     | 21.6 ms: 1.04x faster                                                         |
| meteor_contest             | 74.6 ms                                                     | 71.8 ms: 1.04x faster                                                         |
| unpickle_pure_python       | 133 us                                                      | 130 us: 1.03x faster                                                          |
| json                       | 3.05 ms                                                     | 2.97 ms: 1.02x faster                                                         |
| xml_etree_process          | 37.7 ms                                                     | 37.2 ms: 1.01x faster                                                         |
| regex_effbot               | 1.62 ms                                                     | 1.60 ms: 1.01x faster                                                         |
| pidigits                   | 152 ms                                                      | 150 ms: 1.01x faster                                                          |
| deltablue                  | 2.16 ms                                                     | 2.14 ms: 1.01x faster                                                         |
| pathlib                    | 80.5 ms                                                     | 81.4 ms: 1.01x slower                                                         |
| pycparser                  | 699 ms                                                      | 708 ms: 1.01x slower                                                          |
| sqlglot_transpile          | 1.02 ms                                                     | 1.04 ms: 1.01x slower                                                         |
| json_dumps                 | 5.70 ms                                                     | 5.80 ms: 1.02x slower                                                         |
| regex_compile              | 87.5 ms                                                     | 89.4 ms: 1.02x slower                                                         |
| json_loads                 | 13.9 us                                                     | 14.2 us: 1.02x slower                                                         |
| sqlglot_normalize          | 187 ms                                                      | 192 ms: 1.03x slower                                                          |
| sympy_sum                  | 91.5 ms                                                     | 94.5 ms: 1.03x slower                                                         |
| gc_traversal               | 1.52 ms                                                     | 1.58 ms: 1.04x slower                                                         |
| sympy_str                  | 175 ms                                                      | 182 ms: 1.04x slower                                                          |
| go                         | 91.6 ms                                                     | 95.4 ms: 1.04x slower                                                         |
| richards_super             | 32.1 ms                                                     | 33.5 ms: 1.04x slower                                                         |
| bench_mp_pool              | 69.2 ms                                                     | 72.6 ms: 1.05x slower                                                         |
| tornado_http               | 89.5 ms                                                     | 94.0 ms: 1.05x slower                                                         |
| async_generators           | 239 ms                                                      | 252 ms: 1.05x slower                                                          |
| sqlglot_optimize           | 34.5 ms                                                     | 36.4 ms: 1.05x slower                                                         |
| richards                   | 28.4 ms                                                     | 29.9 ms: 1.05x slower                                                         |
| mdp                        | 1.37 sec                                                    | 1.45 sec: 1.06x slower                                                        |
| telco                      | 4.13 ms                                                     | 4.47 ms: 1.08x slower                                                         |
| asyncio_tcp                | 487 ms                                                      | 531 ms: 1.09x slower                                                          |
| regex_v8                   | 14.2 ms                                                     | 15.5 ms: 1.09x slower                                                         |
| scimark_sor                | 78.8 ms                                                     | 86.1 ms: 1.09x slower                                                         |
| 2to3                       | 218 ms                                                      | 238 ms: 1.09x slower                                                          |
| sympy_integrate            | 13.0 ms                                                     | 14.2 ms: 1.10x slower                                                         |
| docutils                   | 1.66 sec                                                    | 1.83 sec: 1.10x slower                                                        |
| sympy_expand               | 284 ms                                                      | 315 ms: 1.11x slower                                                          |
| django_template            | 22.9 ms                                                     | 25.5 ms: 1.11x slower                                                         |
| python_startup_no_site     | 16.2 ms                                                     | 18.2 ms: 1.12x slower                                                         |
| python_startup             | 19.5 ms                                                     | 22.0 ms: 1.13x slower                                                         |
| hexiom                     | 4.10 ms                                                     | 4.65 ms: 1.13x slower                                                         |
| coverage                   | 40.8 ms                                                     | 47.0 ms: 1.15x slower                                                         |
| create_gc_cycles           | 752 us                                                      | 910 us: 1.21x slower                                                          |
| scimark_lu                 | 58.9 ms                                                     | 72.0 ms: 1.22x slower                                                         |
| typing_runtime_protocols   | 95.1 us                                                     | 118 us: 1.24x slower                                                          |
| Geometric mean             | (ref)                                                       | 1.07x faster                                                                  |

Benchmark hidden because not significant (2): xml_etree_parse, sqlglot_parse
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240727-3.14.0a0-60b7e71-JIT/bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 95.20% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown