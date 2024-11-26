# Results vs. 3.12.0

- fork: faster-cpython
- ref: use_stackrefs
- machine: linux-x86_64
- commit hash: 7e6deef
- commit date: 2024-10-29
- overall geometric mean: 1.478x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.87x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-7e6deef |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 530 ms: 1.93x slower                                                      |
| docutils       | 2.77 sec                                               | 5.45 sec: 1.97x slower                                                    |
| tornado_http   | 103 ms                                                 | 187 ms: 1.82x slower                                                      |
| Geometric mean | (ref)                                                  | 1.91x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-7e6deef |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 781 ms: 1.36x slower                                                      |
| async_tree_none            | 472 ms                                                 | 687 ms: 1.46x slower                                                      |
| async_tree_none_tg         | 450 ms                                                 | 659 ms: 1.47x slower                                                      |
| async_tree_io              | 1.16 sec                                               | 1.75 sec: 1.52x slower                                                    |
| async_tree_memoization     | 578 ms                                                 | 878 ms: 1.52x slower                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 1.85 sec: 1.57x slower                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 1.16 sec: 1.60x slower                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 1.17 sec: 1.61x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.51x slower                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-7e6deef |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 161 ms: 1.90x slower                                                      |
| nbody          | 97.0 ms                                                | 195 ms: 2.01x slower                                                      |
| pidigits       | 187 ms                                                 | 378 ms: 2.02x slower                                                      |
| Geometric mean | (ref)                                                  | 1.98x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-7e6deef |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 264 ms: 1.78x slower                                                      |
| regex_effbot   | 3.61 ms                                                | 7.47 ms: 2.07x slower                                                     |
| regex_dna      | 212 ms                                                 | 439 ms: 2.07x slower                                                      |
| regex_v8       | 23.1 ms                                                | 49.1 ms: 2.12x slower                                                     |
| Geometric mean | (ref)                                                  | 2.01x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-7e6deef |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 4.25 sec: 1.82x slower                                                    |
| json_loads           | 28.5 us                                                | 53.4 us: 1.87x slower                                                     |
| xml_etree_iterparse  | 107 ms                                                 | 206 ms: 1.93x slower                                                      |
| unpickle_pure_python | 230 us                                                 | 445 us: 1.93x slower                                                      |
| pickle_pure_python   | 324 us                                                 | 635 us: 1.96x slower                                                      |
| xml_etree_parse      | 159 ms                                                 | 314 ms: 1.97x slower                                                      |
| xml_etree_generate   | 89.2 ms                                                | 177 ms: 1.98x slower                                                      |
| xml_etree_process    | 61.7 ms                                                | 123 ms: 1.99x slower                                                      |
| json_dumps           | 10.4 ms                                                | 23.2 ms: 2.23x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.96x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-7e6deef |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 15.7 ms: 2.27x slower                                                     |
| python_startup         | 9.55 ms                                                | 31.0 ms: 3.25x slower                                                     |
| Geometric mean         | (ref)                                                  | 2.71x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-7e6deef |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 23.3 ms: 1.96x slower                                                     |
| django_template | 34.6 ms                                                | 72.1 ms: 2.08x slower                                                     |
| Geometric mean  | (ref)                                                  | 2.02x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-7e6deef |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 781 ms: 1.36x slower                                                      |
| deepcopy                   | 371 us                                                 | 533 us: 1.44x slower                                                      |
| deepcopy_memo              | 40.7 us                                                | 58.7 us: 1.44x slower                                                     |
| async_tree_none            | 472 ms                                                 | 687 ms: 1.46x slower                                                      |
| async_tree_none_tg         | 450 ms                                                 | 659 ms: 1.47x slower                                                      |
| async_tree_io              | 1.16 sec                                               | 1.75 sec: 1.52x slower                                                    |
| async_tree_memoization     | 578 ms                                                 | 878 ms: 1.52x slower                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 1.85 sec: 1.57x slower                                                    |
| comprehensions             | 21.8 us                                                | 34.9 us: 1.60x slower                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 1.16 sec: 1.60x slower                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 1.17 sec: 1.61x slower                                                    |
| deepcopy_reduce            | 3.35 us                                                | 5.62 us: 1.68x slower                                                     |
| pathlib                    | 19.3 ms                                                | 32.6 ms: 1.69x slower                                                     |
| raytrace                   | 312 ms                                                 | 542 ms: 1.74x slower                                                      |
| go                         | 139 ms                                                 | 242 ms: 1.74x slower                                                      |
| deltablue                  | 3.72 ms                                                | 6.46 ms: 1.74x slower                                                     |
| regex_compile              | 148 ms                                                 | 264 ms: 1.78x slower                                                      |
| sympy_sum                  | 169 ms                                                 | 303 ms: 1.79x slower                                                      |
| sqlalchemy_declarative     | 147 ms                                                 | 264 ms: 1.80x slower                                                      |
| tornado_http               | 103 ms                                                 | 187 ms: 1.82x slower                                                      |
| tomli_loads                | 2.33 sec                                               | 4.25 sec: 1.82x slower                                                    |
| logging_format             | 7.23 us                                                | 13.2 us: 1.82x slower                                                     |
| crypto_pyaes               | 81.9 ms                                                | 150 ms: 1.83x slower                                                      |
| scimark_monte_carlo        | 75.1 ms                                                | 138 ms: 1.84x slower                                                      |
| logging_silent             | 104 ns                                                 | 193 ns: 1.85x slower                                                      |
| sympy_str                  | 300 ms                                                 | 553 ms: 1.85x slower                                                      |
| logging_simple             | 6.46 us                                                | 11.9 us: 1.85x slower                                                     |
| json                       | 5.26 ms                                                | 9.80 ms: 1.86x slower                                                     |
| json_loads                 | 28.5 us                                                | 53.4 us: 1.87x slower                                                     |
| chaos                      | 67.0 ms                                                | 126 ms: 1.88x slower                                                      |
| generators                 | 31.2 ms                                                | 58.8 ms: 1.88x slower                                                     |
| sympy_integrate            | 21.4 ms                                                | 40.5 ms: 1.89x slower                                                     |
| sqlalchemy_imperative      | 18.7 ms                                                | 35.3 ms: 1.89x slower                                                     |
| dulwich_log                | 68.5 ms                                                | 130 ms: 1.89x slower                                                      |
| float                      | 84.7 ms                                                | 161 ms: 1.90x slower                                                      |
| async_generators           | 463 ms                                                 | 882 ms: 1.91x slower                                                      |
| mdp                        | 2.63 sec                                               | 5.02 sec: 1.91x slower                                                    |
| meteor_contest             | 112 ms                                                 | 216 ms: 1.92x slower                                                      |
| sqlglot_parse              | 1.36 ms                                                | 2.62 ms: 1.92x slower                                                     |
| xml_etree_iterparse        | 107 ms                                                 | 206 ms: 1.93x slower                                                      |
| 2to3                       | 274 ms                                                 | 530 ms: 1.93x slower                                                      |
| pprint_safe_repr           | 776 ms                                                 | 1.50 sec: 1.93x slower                                                    |
| unpickle_pure_python       | 230 us                                                 | 445 us: 1.93x slower                                                      |
| sqlglot_transpile          | 1.68 ms                                                | 3.28 ms: 1.95x slower                                                     |
| scimark_fft                | 382 ms                                                 | 746 ms: 1.95x slower                                                      |
| mako                       | 11.9 ms                                                | 23.3 ms: 1.96x slower                                                     |
| pprint_pformat             | 1.57 sec                                               | 3.07 sec: 1.96x slower                                                    |
| pickle_pure_python         | 324 us                                                 | 635 us: 1.96x slower                                                      |
| scimark_lu                 | 118 ms                                                 | 232 ms: 1.96x slower                                                      |
| xml_etree_parse            | 159 ms                                                 | 314 ms: 1.97x slower                                                      |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 9.96 ms: 1.97x slower                                                     |
| docutils                   | 2.77 sec                                               | 5.45 sec: 1.97x slower                                                    |
| sympy_expand               | 478 ms                                                 | 943 ms: 1.97x slower                                                      |
| xml_etree_generate         | 89.2 ms                                                | 177 ms: 1.98x slower                                                      |
| xml_etree_process          | 61.7 ms                                                | 123 ms: 1.99x slower                                                      |
| sqlglot_normalize          | 110 ms                                                 | 219 ms: 1.99x slower                                                      |
| spectral_norm              | 115 ms                                                 | 230 ms: 2.00x slower                                                      |
| nbody                      | 97.0 ms                                                | 195 ms: 2.01x slower                                                      |
| hexiom                     | 6.41 ms                                                | 12.9 ms: 2.01x slower                                                     |
| asyncio_websockets         | 551 ms                                                 | 1.11 sec: 2.01x slower                                                    |
| richards                   | 45.8 ms                                                | 92.4 ms: 2.02x slower                                                     |
| pidigits                   | 187 ms                                                 | 378 ms: 2.02x slower                                                      |
| sqlglot_optimize           | 54.8 ms                                                | 112 ms: 2.04x slower                                                      |
| pycparser                  | 1.18 sec                                               | 2.41 sec: 2.04x slower                                                    |
| pyflate                    | 482 ms                                                 | 987 ms: 2.05x slower                                                      |
| richards_super             | 51.5 ms                                                | 105 ms: 2.05x slower                                                      |
| fannkuch                   | 417 ms                                                 | 859 ms: 2.06x slower                                                      |
| regex_effbot               | 3.61 ms                                                | 7.47 ms: 2.07x slower                                                     |
| regex_dna                  | 212 ms                                                 | 439 ms: 2.07x slower                                                      |
| nqueens                    | 83.3 ms                                                | 173 ms: 2.08x slower                                                      |
| django_template            | 34.6 ms                                                | 72.1 ms: 2.08x slower                                                     |
| scimark_sor                | 129 ms                                                 | 270 ms: 2.09x slower                                                      |
| typing_runtime_protocols   | 158 us                                                 | 331 us: 2.10x slower                                                      |
| regex_v8                   | 23.1 ms                                                | 49.1 ms: 2.12x slower                                                     |
| coroutines                 | 23.2 ms                                                | 50.5 ms: 2.18x slower                                                     |
| json_dumps                 | 10.4 ms                                                | 23.2 ms: 2.23x slower                                                     |
| python_startup_no_site     | 6.94 ms                                                | 15.7 ms: 2.27x slower                                                     |
| telco                      | 7.10 ms                                                | 16.2 ms: 2.28x slower                                                     |
| coverage                   | 72.7 ms                                                | 167 ms: 2.30x slower                                                      |
| gc_traversal               | 3.79 ms                                                | 8.77 ms: 2.31x slower                                                     |
| python_startup             | 9.55 ms                                                | 31.0 ms: 3.25x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 5.24 ms: 3.55x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 128 ms: 5.32x slower                                                      |
| bench_thread_pool          | 842 us                                                 | 30.3 ms: 35.97x slower                                                    |
| Geometric mean             | (ref)                                                  | 2.00x slower                                                              |
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (10) of results/bm-20241029-3.14.0a1+-7e6deef/bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-7e6deef.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.478x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.90x
- 95% likely to have a slowdown of 1.89x
- 99% likely to have a slowdown of 1.87x

# Memory
- memory change: 1.07x