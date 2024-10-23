# Results vs. 3.13.0

- fork: python
- ref: ded105a62b9d78717f8d
- machine: linux-aarch64
- commit hash: ded105a
- commit date: 2024-10-21
- overall geometric mean: 1.19x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 384 ms: 1.26x slower                                                     |
| docutils       | 2.91 sec                                                 | 3.61 sec: 1.24x slower                                                   |
| html5lib       | 64.3 ms                                                  | 72.5 ms: 1.13x slower                                                    |
| tornado_http   | 131 ms                                                   | 148 ms: 1.13x slower                                                     |
| Geometric mean | (ref)                                                    | 1.19x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|---------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg | 649 ms                                                   | 539 ms: 1.21x faster                                                     |
| async_tree_memoization    | 626 ms                                                   | 597 ms: 1.05x faster                                                     |
| async_tree_none           | 493 ms                                                   | 471 ms: 1.05x faster                                                     |
| async_tree_none_tg        | 467 ms                                                   | 448 ms: 1.04x faster                                                     |
| coroutines                | 28.2 ms                                                  | 29.0 ms: 1.03x slower                                                    |
| async_generators          | 496 ms                                                   | 513 ms: 1.03x slower                                                     |
| async_tree_io             | 1.11 sec                                                 | 1.18 sec: 1.06x slower                                                   |
| async_tree_io_tg          | 1.09 sec                                                 | 1.23 sec: 1.13x slower                                                   |
| Geometric mean            | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, asyncio_websockets, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 97.0 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                    | 1.01x slower                                                             |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.87 ms                                                  | 5.00 ms: 1.03x slower                                                    |
| regex_dna      | 246 ms                                                   | 257 ms: 1.04x slower                                                     |
| regex_compile  | 128 ms                                                   | 175 ms: 1.36x slower                                                     |
| Geometric mean | (ref)                                                    | 1.10x slower                                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse  | 147 ms                                                   | 150 ms: 1.02x slower                                                     |
| tomli_loads          | 2.53 sec                                                 | 2.63 sec: 1.04x slower                                                   |
| unpickle_pure_python | 254 us                                                   | 270 us: 1.06x slower                                                     |
| json_dumps           | 13.4 ms                                                  | 14.3 ms: 1.07x slower                                                    |
| pickle_pure_python   | 359 us                                                   | 390 us: 1.08x slower                                                     |
| Geometric mean       | (ref)                                                    | 1.03x slower                                                             |

Benchmark hidden because not significant (4): xml_etree_parse, json_loads, xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup | 13.3 ms                                                  | 14.5 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                    | 1.05x slower                                                             |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 13.3 ms                                                  | 13.2 ms: 1.01x faster                                                    |
| genshi_text     | 27.7 ms                                                  | 34.2 ms: 1.23x slower                                                    |
| django_template | 42.3 ms                                                  | 53.5 ms: 1.27x slower                                                    |
| genshi_xml      | 60.2 ms                                                  | 84.1 ms: 1.40x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.21x slower                                                             |

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|---------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy_memo             | 51.0 us                                                  | 38.7 us: 1.32x faster                                                    |
| async_tree_memoization_tg | 649 ms                                                   | 539 ms: 1.21x faster                                                     |
| deepcopy                  | 451 us                                                   | 377 us: 1.20x faster                                                     |
| async_tree_memoization    | 626 ms                                                   | 597 ms: 1.05x faster                                                     |
| async_tree_none           | 493 ms                                                   | 471 ms: 1.05x faster                                                     |
| async_tree_none_tg        | 467 ms                                                   | 448 ms: 1.04x faster                                                     |
| deepcopy_reduce           | 4.07 us                                                  | 3.92 us: 1.04x faster                                                    |
| telco                     | 9.73 ms                                                  | 9.41 ms: 1.03x faster                                                    |
| pathlib                   | 22.4 ms                                                  | 21.8 ms: 1.03x faster                                                    |
| scimark_sor               | 159 ms                                                   | 155 ms: 1.03x faster                                                     |
| logging_silent            | 135 ns                                                   | 133 ns: 1.02x faster                                                     |
| mako                      | 13.3 ms                                                  | 13.2 ms: 1.01x faster                                                    |
| scimark_fft               | 447 ms                                                   | 456 ms: 1.02x slower                                                     |
| bpe_tokeniser             | 5.90 sec                                                 | 6.01 sec: 1.02x slower                                                   |
| xml_etree_iterparse       | 147 ms                                                   | 150 ms: 1.02x slower                                                     |
| regex_effbot              | 4.87 ms                                                  | 5.00 ms: 1.03x slower                                                    |
| coroutines                | 28.2 ms                                                  | 29.0 ms: 1.03x slower                                                    |
| float                     | 94.4 ms                                                  | 97.0 ms: 1.03x slower                                                    |
| thrift                    | 946 us                                                   | 973 us: 1.03x slower                                                     |
| async_generators          | 496 ms                                                   | 513 ms: 1.03x slower                                                     |
| logging_format            | 7.83 us                                                  | 8.13 us: 1.04x slower                                                    |
| tomli_loads               | 2.53 sec                                                 | 2.63 sec: 1.04x slower                                                   |
| mdp                       | 3.36 sec                                                 | 3.51 sec: 1.04x slower                                                   |
| regex_dna                 | 246 ms                                                   | 257 ms: 1.04x slower                                                     |
| unpickle_pure_python      | 254 us                                                   | 270 us: 1.06x slower                                                     |
| async_tree_io             | 1.11 sec                                                 | 1.18 sec: 1.06x slower                                                   |
| scimark_monte_carlo       | 83.8 ms                                                  | 89.6 ms: 1.07x slower                                                    |
| logging_simple            | 7.04 us                                                  | 7.54 us: 1.07x slower                                                    |
| json_dumps                | 13.4 ms                                                  | 14.3 ms: 1.07x slower                                                    |
| bench_thread_pool         | 1.28 ms                                                  | 1.37 ms: 1.07x slower                                                    |
| scimark_lu                | 139 ms                                                   | 150 ms: 1.08x slower                                                     |
| scimark_sparse_mat_mult   | 6.58 ms                                                  | 7.11 ms: 1.08x slower                                                    |
| meteor_contest            | 113 ms                                                   | 123 ms: 1.08x slower                                                     |
| pickle_pure_python        | 359 us                                                   | 390 us: 1.08x slower                                                     |
| crypto_pyaes              | 82.7 ms                                                  | 90.2 ms: 1.09x slower                                                    |
| python_startup            | 13.3 ms                                                  | 14.5 ms: 1.09x slower                                                    |
| pyflate                   | 556 ms                                                   | 623 ms: 1.12x slower                                                     |
| tornado_http              | 131 ms                                                   | 148 ms: 1.13x slower                                                     |
| html5lib                  | 64.3 ms                                                  | 72.5 ms: 1.13x slower                                                    |
| async_tree_io_tg          | 1.09 sec                                                 | 1.23 sec: 1.13x slower                                                   |
| typing_runtime_protocols  | 192 us                                                   | 217 us: 1.13x slower                                                     |
| spectral_norm             | 141 ms                                                   | 160 ms: 1.13x slower                                                     |
| richards_super            | 60.3 ms                                                  | 69.3 ms: 1.15x slower                                                    |
| go                        | 163 ms                                                   | 187 ms: 1.15x slower                                                     |
| fannkuch                  | 452 ms                                                   | 526 ms: 1.16x slower                                                     |
| richards                  | 53.5 ms                                                  | 63.1 ms: 1.18x slower                                                    |
| raytrace                  | 298 ms                                                   | 352 ms: 1.18x slower                                                     |
| deltablue                 | 3.85 ms                                                  | 4.57 ms: 1.19x slower                                                    |
| comprehensions            | 20.4 us                                                  | 24.7 us: 1.21x slower                                                    |
| pycparser                 | 1.26 sec                                                 | 1.54 sec: 1.22x slower                                                   |
| sqlglot_normalize         | 128 ms                                                   | 157 ms: 1.22x slower                                                     |
| genshi_text               | 27.7 ms                                                  | 34.2 ms: 1.23x slower                                                    |
| sqlglot_parse             | 1.38 ms                                                  | 1.71 ms: 1.24x slower                                                    |
| docutils                  | 2.91 sec                                                 | 3.61 sec: 1.24x slower                                                   |
| chaos                     | 68.8 ms                                                  | 85.8 ms: 1.25x slower                                                    |
| nqueens                   | 98.7 ms                                                  | 123 ms: 1.25x slower                                                     |
| 2to3                      | 306 ms                                                   | 384 ms: 1.26x slower                                                     |
| django_template           | 42.3 ms                                                  | 53.5 ms: 1.27x slower                                                    |
| sqlglot_transpile         | 1.73 ms                                                  | 2.21 ms: 1.28x slower                                                    |
| pprint_safe_repr          | 926 ms                                                   | 1.20 sec: 1.30x slower                                                   |
| sympy_expand              | 455 ms                                                   | 596 ms: 1.31x slower                                                     |
| sqlglot_optimize          | 62.4 ms                                                  | 82.4 ms: 1.32x slower                                                    |
| pprint_pformat            | 1.90 sec                                                 | 2.53 sec: 1.33x slower                                                   |
| sympy_str                 | 264 ms                                                   | 357 ms: 1.36x slower                                                     |
| regex_compile             | 128 ms                                                   | 175 ms: 1.36x slower                                                     |
| pylint                    | 343 ms                                                   | 480 ms: 1.40x slower                                                     |
| genshi_xml                | 60.2 ms                                                  | 84.1 ms: 1.40x slower                                                    |
| gc_traversal              | 4.53 ms                                                  | 6.38 ms: 1.41x slower                                                    |
| sympy_integrate           | 21.0 ms                                                  | 29.9 ms: 1.42x slower                                                    |
| hexiom                    | 7.13 ms                                                  | 10.3 ms: 1.44x slower                                                    |
| sympy_sum                 | 143 ms                                                   | 216 ms: 1.50x slower                                                     |
| generators                | 37.8 ms                                                  | 59.0 ms: 1.56x slower                                                    |
| create_gc_cycles          | 2.12 ms                                                  | 3.65 ms: 1.72x slower                                                    |
| bench_mp_pool             | 7.30 ms                                                  | 2.31 sec: 316.66x slower                                                 |
| Geometric mean            | (ref)                                                    | 1.19x slower                                                             |

Benchmark hidden because not significant (13): async_tree_cpu_io_mixed, xml_etree_parse, coverage, nbody, json_loads, xml_etree_generate, python_startup_no_site, asyncio_websockets, pidigits, json, regex_v8, async_tree_cpu_io_mixed_tg, xml_etree_process
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (2) of results/bm-20241021-3.14.0a1+-ded105a-JIT/bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a.json: dulwich_log, sphinx

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 1.20x