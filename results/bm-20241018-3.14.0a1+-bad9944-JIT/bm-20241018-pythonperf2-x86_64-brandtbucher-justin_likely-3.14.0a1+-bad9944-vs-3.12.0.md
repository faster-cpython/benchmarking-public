# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_likely
- machine: linux-x86_64
- commit hash: bad9944
- commit date: 2024-10-18
- overall geometric mean: 1.008x slower
- HPT reliability: 64.85%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 314 ms: 1.10x slower                                                        |
| docutils       | 2.87 sec                                                     | 3.21 sec: 1.12x slower                                                      |
| tornado_http   | 121 ms                                                       | 123 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                        | 1.08x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 377 ms: 1.44x faster                                                        |
| async_tree_none            | 452 ms                                                       | 332 ms: 1.36x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 321 ms: 1.34x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 412 ms: 1.32x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 836 ms: 1.25x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 560 ms: 1.25x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 863 ms: 1.22x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 577 ms: 1.21x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.29x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 83.3 ms: 1.06x faster                                                       |
| pidigits       | 265 ms                                                       | 251 ms: 1.05x faster                                                        |
| float          | 76.6 ms                                                      | 79.3 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.51 ms: 1.02x faster                                                       |
| regex_dna      | 239 ms                                                       | 247 ms: 1.04x slower                                                        |
| regex_compile  | 144 ms                                                       | 152 ms: 1.06x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 26.9 ms: 1.14x slower                                                       |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 82.0 ms: 1.05x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 100.0 ms: 1.03x faster                                                      |
| pickle_dict          | 32.5 us                                                      | 31.7 us: 1.03x faster                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.15 sec: 1.01x faster                                                      |
| pickle               | 10.5 us                                                      | 10.7 us: 1.01x slower                                                       |
| pickle_list          | 4.43 us                                                      | 4.60 us: 1.04x slower                                                       |
| unpickle             | 14.8 us                                                      | 15.4 us: 1.04x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 337 us: 1.06x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 226 us: 1.08x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 11.2 ms: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                                |

Benchmark hidden because not significant (4): xml_etree_parse, json_loads, xml_etree_process, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.98 ms: 1.04x slower                                                       |
| python_startup         | 11.6 ms                                                      | 14.9 ms: 1.28x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.39 ms: 1.07x faster                                                       |
| django_template | 38.2 ms                                                      | 43.9 ms: 1.15x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.04x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 377 ms: 1.44x faster                                                        |
| async_tree_none            | 452 ms                                                       | 332 ms: 1.36x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 321 ms: 1.34x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 412 ms: 1.32x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 836 ms: 1.25x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 560 ms: 1.25x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 29.9 us: 1.23x faster                                                       |
| async_tree_io_tg           | 1.05 sec                                                     | 863 ms: 1.22x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 577 ms: 1.21x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 15.9 ms: 1.19x faster                                                       |
| deepcopy                   | 368 us                                                       | 313 us: 1.18x faster                                                        |
| comprehensions             | 21.9 us                                                      | 18.9 us: 1.16x faster                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 71.5 ms: 1.12x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 3.11 us: 1.09x faster                                                       |
| mako                       | 10.0 ms                                                      | 9.39 ms: 1.07x faster                                                       |
| scimark_sor                | 109 ms                                                       | 103 ms: 1.06x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 21.8 ms: 1.06x faster                                                       |
| nbody                      | 88.0 ms                                                      | 83.3 ms: 1.06x faster                                                       |
| pidigits                   | 265 ms                                                       | 251 ms: 1.05x faster                                                        |
| scimark_lu                 | 98.8 ms                                                      | 93.9 ms: 1.05x faster                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 82.0 ms: 1.05x faster                                                       |
| richards_super             | 51.3 ms                                                      | 48.9 ms: 1.05x faster                                                       |
| logging_format             | 7.48 us                                                      | 7.14 us: 1.05x faster                                                       |
| richards                   | 45.7 ms                                                      | 43.7 ms: 1.05x faster                                                       |
| logging_silent             | 94.4 ns                                                      | 90.8 ns: 1.04x faster                                                       |
| scimark_fft                | 301 ms                                                       | 291 ms: 1.04x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 100.0 ms: 1.03x faster                                                      |
| pickle_dict                | 32.5 us                                                      | 31.7 us: 1.03x faster                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.51 ms: 1.02x faster                                                       |
| dulwich_log                | 65.4 ms                                                      | 64.4 ms: 1.02x faster                                                       |
| asyncio_websockets         | 387 ms                                                       | 381 ms: 1.01x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.63 us: 1.01x faster                                                       |
| sqlite_synth               | 2.77 us                                                      | 2.74 us: 1.01x faster                                                       |
| async_generators           | 390 ms                                                       | 388 ms: 1.01x faster                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.15 sec: 1.01x faster                                                      |
| go                         | 150 ms                                                       | 151 ms: 1.01x slower                                                        |
| tornado_http               | 121 ms                                                       | 123 ms: 1.01x slower                                                        |
| spectral_norm              | 91.6 ms                                                      | 92.8 ms: 1.01x slower                                                       |
| mdp                        | 2.57 sec                                                     | 2.60 sec: 1.01x slower                                                      |
| pickle                     | 10.5 us                                                      | 10.7 us: 1.01x slower                                                       |
| deltablue                  | 3.24 ms                                                      | 3.31 ms: 1.02x slower                                                       |
| generators                 | 37.4 ms                                                      | 38.3 ms: 1.02x slower                                                       |
| meteor_contest             | 128 ms                                                       | 131 ms: 1.02x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.27 sec: 1.03x slower                                                      |
| raytrace                   | 298 ms                                                       | 307 ms: 1.03x slower                                                        |
| float                      | 76.6 ms                                                      | 79.3 ms: 1.03x slower                                                       |
| regex_dna                  | 239 ms                                                       | 247 ms: 1.04x slower                                                        |
| pickle_list                | 4.43 us                                                      | 4.60 us: 1.04x slower                                                       |
| fannkuch                   | 350 ms                                                       | 364 ms: 1.04x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 8.98 ms: 1.04x slower                                                       |
| unpickle                   | 14.8 us                                                      | 15.4 us: 1.04x slower                                                       |
| chaos                      | 64.0 ms                                                      | 67.0 ms: 1.05x slower                                                       |
| regex_compile              | 144 ms                                                       | 152 ms: 1.06x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 337 us: 1.06x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.47 ms: 1.06x slower                                                       |
| pyflate                    | 439 ms                                                       | 467 ms: 1.06x slower                                                        |
| sympy_str                  | 302 ms                                                       | 324 ms: 1.07x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 226 us: 1.08x slower                                                        |
| sympy_sum                  | 162 ms                                                       | 176 ms: 1.09x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 11.2 ms: 1.10x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.52 ms: 1.10x slower                                                       |
| 2to3                       | 285 ms                                                       | 314 ms: 1.10x slower                                                        |
| sympy_expand               | 484 ms                                                       | 534 ms: 1.10x slower                                                        |
| telco                      | 6.96 ms                                                      | 7.73 ms: 1.11x slower                                                       |
| docutils                   | 2.87 sec                                                     | 3.21 sec: 1.12x slower                                                      |
| sqlglot_transpile          | 1.78 ms                                                      | 2.01 ms: 1.13x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 26.9 ms: 1.14x slower                                                       |
| nqueens                    | 89.9 ms                                                      | 103 ms: 1.15x slower                                                        |
| django_template            | 38.2 ms                                                      | 43.9 ms: 1.15x slower                                                       |
| sympy_integrate            | 23.9 ms                                                      | 27.6 ms: 1.15x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 134 ms: 1.16x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 178 us: 1.18x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 7.16 ms: 1.20x slower                                                       |
| sqlglot_optimize           | 57.5 ms                                                      | 70.3 ms: 1.22x slower                                                       |
| coverage                   | 66.7 ms                                                      | 82.9 ms: 1.24x slower                                                       |
| python_startup             | 11.6 ms                                                      | 14.9 ms: 1.28x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 5.21 ms: 1.50x slower                                                       |
| unpack_sequence            | 53.2 ns                                                      | 91.3 ns: 1.72x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.89 ms: 1.82x slower                                                       |
| bench_mp_pool              | 4.76 ms                                                      | 3.16 sec: 663.70x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.09x slower                                                                |

Benchmark hidden because not significant (11): json, pprint_pformat, asyncio_tcp_ssl, xml_etree_parse, json_loads, asyncio_tcp, pprint_safe_repr, bench_thread_pool, xml_etree_process, unpickle_list, scimark_monte_carlo
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (7) of results/bm-20241018-3.14.0a1+-bad9944-JIT/bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.008x slower
# HPT report

- Reliability score: 64.85% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.10x