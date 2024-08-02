# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: lower_before
- machine: linux-x86_64
- commit hash: 68df0a5
- commit date: 2024-06-17
- overall geometric mean: 1.01x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240617-linux-x86_64-faster%2dcpython-lower_before-3.14.0a0-68df0a5 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 270 ms: 1.01x faster                                                    |
| docutils       | 2.83 sec                                                   | 2.79 sec: 1.01x faster                                                  |
| html5lib       | 67.2 ms                                                    | 68.9 ms: 1.02x slower                                                   |
| tornado_http   | 94.6 ms                                                    | 93.6 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                      | 1.00x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240617-linux-x86_64-faster%2dcpython-lower_before-3.14.0a0-68df0a5 |
|---------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg | 444 ms                                                     | 460 ms: 1.04x slower                                                    |
| async_tree_memoization    | 463 ms                                                     | 489 ms: 1.05x slower                                                    |
| async_tree_io_tg          | 936 ms                                                     | 1.01 sec: 1.08x slower                                                  |
| Geometric mean            | (ref)                                                      | 1.02x slower                                                            |

Benchmark hidden because not significant (5): async_tree_none, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240617-linux-x86_64-faster%2dcpython-lower_before-3.14.0a0-68df0a5 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 78.1 ms: 1.01x faster                                                   |
| pidigits       | 191 ms                                                     | 190 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                      | 1.01x faster                                                            |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240617-linux-x86_64-faster%2dcpython-lower_before-3.14.0a0-68df0a5 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.2 ms: 1.04x faster                                                   |
| regex_compile  | 137 ms                                                     | 134 ms: 1.02x faster                                                    |
| regex_effbot   | 3.67 ms                                                    | 3.79 ms: 1.03x slower                                                   |
| regex_dna      | 221 ms                                                     | 232 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                      | 1.00x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240617-linux-x86_64-faster%2dcpython-lower_before-3.14.0a0-68df0a5 |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                   |
| unpickle             | 15.1 us                                                    | 14.8 us: 1.02x faster                                                   |
| xml_etree_process    | 61.2 ms                                                    | 60.0 ms: 1.02x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                     | 106 ms: 1.01x faster                                                    |
| xml_etree_generate   | 87.4 ms                                                    | 86.3 ms: 1.01x faster                                                   |
| unpickle_pure_python | 218 us                                                     | 216 us: 1.01x faster                                                    |
| pickle_dict          | 34.8 us                                                    | 34.7 us: 1.00x faster                                                   |
| pickle               | 11.5 us                                                    | 11.6 us: 1.01x slower                                                   |
| tomli_loads          | 2.12 sec                                                   | 2.18 sec: 1.03x slower                                                  |
| unpickle_list        | 5.34 us                                                    | 5.50 us: 1.03x slower                                                   |
| Geometric mean       | (ref)                                                      | 1.00x faster                                                            |

Benchmark hidden because not significant (4): xml_etree_parse, pickle_list, pickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240617-linux-x86_64-faster%2dcpython-lower_before-3.14.0a0-68df0a5 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 10.8 ms                                                    | 10.7 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                      | 1.00x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240617-linux-x86_64-faster%2dcpython-lower_before-3.14.0a0-68df0a5 |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 34.8 ms                                                    | 34.4 ms: 1.01x faster                                                   |
| Geometric mean  | (ref)                                                      | 1.00x faster                                                            |

Benchmark hidden because not significant (3): genshi_xml, mako, genshi_text

All benchmarks:
===============

| Benchmark                 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240617-linux-x86_64-faster%2dcpython-lower_before-3.14.0a0-68df0a5 |
|---------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                  | 367 us                                                     | 270 us: 1.36x faster                                                    |
| deepcopy_memo             | 39.7 us                                                    | 29.9 us: 1.33x faster                                                   |
| deepcopy_reduce           | 3.35 us                                                    | 2.78 us: 1.20x faster                                                   |
| pathlib                   | 17.3 ms                                                    | 16.3 ms: 1.07x faster                                                   |
| scimark_lu                | 122 ms                                                     | 114 ms: 1.06x faster                                                    |
| mdp                       | 2.79 sec                                                   | 2.63 sec: 1.06x faster                                                  |
| crypto_pyaes              | 77.5 ms                                                    | 74.0 ms: 1.05x faster                                                   |
| gc_traversal              | 3.98 ms                                                    | 3.80 ms: 1.05x faster                                                   |
| scimark_fft               | 392 ms                                                     | 377 ms: 1.04x faster                                                    |
| nqueens                   | 81.4 ms                                                    | 78.2 ms: 1.04x faster                                                   |
| scimark_sparse_mat_mult   | 5.27 ms                                                    | 5.07 ms: 1.04x faster                                                   |
| regex_v8                  | 25.1 ms                                                    | 24.2 ms: 1.04x faster                                                   |
| hexiom                    | 6.30 ms                                                    | 6.09 ms: 1.03x faster                                                   |
| create_gc_cycles          | 1.82 ms                                                    | 1.76 ms: 1.03x faster                                                   |
| bench_thread_pool         | 834 us                                                     | 807 us: 1.03x faster                                                    |
| spectral_norm             | 116 ms                                                     | 113 ms: 1.03x faster                                                    |
| dulwich_log               | 67.2 ms                                                    | 65.6 ms: 1.02x faster                                                   |
| regex_compile             | 137 ms                                                     | 134 ms: 1.02x faster                                                    |
| richards_super            | 57.4 ms                                                    | 56.1 ms: 1.02x faster                                                   |
| richards                  | 50.9 ms                                                    | 49.8 ms: 1.02x faster                                                   |
| logging_simple            | 5.74 us                                                    | 5.62 us: 1.02x faster                                                   |
| json_dumps                | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                   |
| unpickle                  | 15.1 us                                                    | 14.8 us: 1.02x faster                                                   |
| xml_etree_process         | 61.2 ms                                                    | 60.0 ms: 1.02x faster                                                   |
| logging_format            | 6.47 us                                                    | 6.35 us: 1.02x faster                                                   |
| thrift                    | 823 us                                                     | 810 us: 1.02x faster                                                    |
| meteor_contest            | 110 ms                                                     | 108 ms: 1.02x faster                                                    |
| chaos                     | 61.3 ms                                                    | 60.4 ms: 1.01x faster                                                   |
| xml_etree_iterparse       | 107 ms                                                     | 106 ms: 1.01x faster                                                    |
| 2to3                      | 274 ms                                                     | 270 ms: 1.01x faster                                                    |
| sympy_integrate           | 20.5 ms                                                    | 20.2 ms: 1.01x faster                                                   |
| xml_etree_generate        | 87.4 ms                                                    | 86.3 ms: 1.01x faster                                                   |
| docutils                  | 2.83 sec                                                   | 2.79 sec: 1.01x faster                                                  |
| unpickle_pure_python      | 218 us                                                     | 216 us: 1.01x faster                                                    |
| tornado_http              | 94.6 ms                                                    | 93.6 ms: 1.01x faster                                                   |
| bpe_tokeniser             | 5.02 sec                                                   | 4.97 sec: 1.01x faster                                                  |
| sqlite_synth              | 2.99 us                                                    | 2.96 us: 1.01x faster                                                   |
| django_template           | 34.8 ms                                                    | 34.4 ms: 1.01x faster                                                   |
| sympy_str                 | 282 ms                                                     | 280 ms: 1.01x faster                                                    |
| sqlglot_transpile         | 1.63 ms                                                    | 1.62 ms: 1.01x faster                                                   |
| float                     | 78.9 ms                                                    | 78.1 ms: 1.01x faster                                                   |
| telco                     | 8.41 ms                                                    | 8.33 ms: 1.01x faster                                                   |
| sympy_sum                 | 156 ms                                                     | 154 ms: 1.01x faster                                                    |
| raytrace                  | 267 ms                                                     | 264 ms: 1.01x faster                                                    |
| sqlglot_optimize          | 55.5 ms                                                    | 55.0 ms: 1.01x faster                                                   |
| pidigits                  | 191 ms                                                     | 190 ms: 1.01x faster                                                    |
| generators                | 29.6 ms                                                    | 29.4 ms: 1.01x faster                                                   |
| pprint_pformat            | 1.56 sec                                                   | 1.55 sec: 1.01x faster                                                  |
| python_startup            | 10.8 ms                                                    | 10.7 ms: 1.01x faster                                                   |
| asyncio_tcp               | 508 ms                                                     | 505 ms: 1.01x faster                                                    |
| pprint_safe_repr          | 758 ms                                                     | 755 ms: 1.00x faster                                                    |
| pickle_dict               | 34.8 us                                                    | 34.7 us: 1.00x faster                                                   |
| asyncio_tcp_ssl           | 1.84 sec                                                   | 1.85 sec: 1.00x slower                                                  |
| comprehensions            | 16.6 us                                                    | 16.7 us: 1.00x slower                                                   |
| json                      | 5.31 ms                                                    | 5.35 ms: 1.01x slower                                                   |
| typing_runtime_protocols  | 165 us                                                     | 166 us: 1.01x slower                                                    |
| pickle                    | 11.5 us                                                    | 11.6 us: 1.01x slower                                                   |
| coverage                  | 93.1 ms                                                    | 94.5 ms: 1.01x slower                                                   |
| pyflate                   | 484 ms                                                     | 492 ms: 1.02x slower                                                    |
| html5lib                  | 67.2 ms                                                    | 68.9 ms: 1.02x slower                                                   |
| tomli_loads               | 2.12 sec                                                   | 2.18 sec: 1.03x slower                                                  |
| unpickle_list             | 5.34 us                                                    | 5.50 us: 1.03x slower                                                   |
| regex_effbot              | 3.67 ms                                                    | 3.79 ms: 1.03x slower                                                   |
| async_tree_memoization_tg | 444 ms                                                     | 460 ms: 1.04x slower                                                    |
| scimark_sor               | 127 ms                                                     | 133 ms: 1.05x slower                                                    |
| regex_dna                 | 221 ms                                                     | 232 ms: 1.05x slower                                                    |
| coroutines                | 23.2 ms                                                    | 24.3 ms: 1.05x slower                                                   |
| async_tree_memoization    | 463 ms                                                     | 489 ms: 1.05x slower                                                    |
| async_tree_io_tg          | 936 ms                                                     | 1.01 sec: 1.08x slower                                                  |
| Geometric mean            | (ref)                                                      | 1.01x faster                                                            |

Benchmark hidden because not significant (28): async_tree_none, async_tree_none_tg, async_tree_cpu_io_mixed_tg, xml_etree_parse, dask, pickle_list, pylint, deltablue, genshi_xml, fannkuch, pickle_pure_python, scimark_monte_carlo, sqlglot_parse, python_startup_no_site, async_generators, nbody, asyncio_websockets, mako, go, pycparser, bench_mp_pool, genshi_text, sympy_expand, json_loads, sqlglot_normalize, logging_silent, async_tree_io, async_tree_cpu_io_mixed
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x