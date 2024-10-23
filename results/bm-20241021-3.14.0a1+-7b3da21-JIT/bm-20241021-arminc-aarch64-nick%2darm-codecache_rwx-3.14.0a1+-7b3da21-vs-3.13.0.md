# Results vs. 3.13.0

- fork: nick-arm
- ref: codecache_rwx
- machine: linux-aarch64
- commit hash: 7b3da21
- commit date: 2024-10-21
- overall geometric mean: 1.18x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 363 ms: 1.19x slower                                                  |
| docutils       | 2.91 sec                                                 | 3.48 sec: 1.20x slower                                                |
| html5lib       | 64.3 ms                                                  | 71.7 ms: 1.12x slower                                                 |
| tornado_http   | 131 ms                                                   | 143 ms: 1.09x slower                                                  |
| Geometric mean | (ref)                                                    | 1.15x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|---------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg | 649 ms                                                   | 539 ms: 1.21x faster                                                  |
| async_tree_none_tg        | 467 ms                                                   | 448 ms: 1.04x faster                                                  |
| async_tree_none           | 493 ms                                                   | 473 ms: 1.04x faster                                                  |
| async_tree_memoization    | 626 ms                                                   | 604 ms: 1.04x faster                                                  |
| coroutines                | 28.2 ms                                                  | 28.7 ms: 1.02x slower                                                 |
| async_generators          | 496 ms                                                   | 506 ms: 1.02x slower                                                  |
| async_tree_io             | 1.11 sec                                                 | 1.20 sec: 1.08x slower                                                |
| async_tree_io_tg          | 1.09 sec                                                 | 1.26 sec: 1.16x slower                                                |
| Geometric mean            | (ref)                                                    | 1.00x faster                                                          |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, asyncio_websockets, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 97.0 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                    | 1.01x slower                                                          |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 31.0 ms: 1.02x faster                                                 |
| regex_dna      | 246 ms                                                   | 252 ms: 1.02x slower                                                  |
| regex_compile  | 128 ms                                                   | 162 ms: 1.26x slower                                                  |
| Geometric mean | (ref)                                                    | 1.06x slower                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.53 sec                                                 | 2.61 sec: 1.03x slower                                                |
| xml_etree_iterparse  | 147 ms                                                   | 153 ms: 1.04x slower                                                  |
| unpickle_pure_python | 254 us                                                   | 267 us: 1.05x slower                                                  |
| json_dumps           | 13.4 ms                                                  | 14.3 ms: 1.07x slower                                                 |
| pickle_pure_python   | 359 us                                                   | 392 us: 1.09x slower                                                  |
| Geometric mean       | (ref)                                                    | 1.03x slower                                                          |

Benchmark hidden because not significant (4): json_loads, xml_etree_parse, xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup | 13.3 ms                                                  | 14.5 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                    | 1.04x slower                                                          |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|-----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 13.3 ms                                                  | 13.2 ms: 1.01x faster                                                 |
| genshi_text     | 27.7 ms                                                  | 32.6 ms: 1.18x slower                                                 |
| django_template | 42.3 ms                                                  | 50.6 ms: 1.20x slower                                                 |
| genshi_xml      | 60.2 ms                                                  | 78.6 ms: 1.31x slower                                                 |
| Geometric mean  | (ref)                                                    | 1.16x slower                                                          |

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|---------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo             | 51.0 us                                                  | 38.9 us: 1.31x faster                                                 |
| async_tree_memoization_tg | 649 ms                                                   | 539 ms: 1.21x faster                                                  |
| deepcopy                  | 451 us                                                   | 379 us: 1.19x faster                                                  |
| deepcopy_reduce           | 4.07 us                                                  | 3.87 us: 1.05x faster                                                 |
| async_tree_none_tg        | 467 ms                                                   | 448 ms: 1.04x faster                                                  |
| async_tree_none           | 493 ms                                                   | 473 ms: 1.04x faster                                                  |
| scimark_sor               | 159 ms                                                   | 153 ms: 1.04x faster                                                  |
| async_tree_memoization    | 626 ms                                                   | 604 ms: 1.04x faster                                                  |
| pathlib                   | 22.4 ms                                                  | 21.8 ms: 1.03x faster                                                 |
| telco                     | 9.73 ms                                                  | 9.49 ms: 1.03x faster                                                 |
| logging_silent            | 135 ns                                                   | 133 ns: 1.02x faster                                                  |
| regex_v8                  | 31.5 ms                                                  | 31.0 ms: 1.02x faster                                                 |
| mako                      | 13.3 ms                                                  | 13.2 ms: 1.01x faster                                                 |
| thrift                    | 946 us                                                   | 941 us: 1.00x faster                                                  |
| scimark_fft               | 447 ms                                                   | 454 ms: 1.01x slower                                                  |
| coverage                  | 98.5 ms                                                  | 99.9 ms: 1.01x slower                                                 |
| coroutines                | 28.2 ms                                                  | 28.7 ms: 1.02x slower                                                 |
| bpe_tokeniser             | 5.90 sec                                                 | 6.00 sec: 1.02x slower                                                |
| async_generators          | 496 ms                                                   | 506 ms: 1.02x slower                                                  |
| logging_format            | 7.83 us                                                  | 7.99 us: 1.02x slower                                                 |
| regex_dna                 | 246 ms                                                   | 252 ms: 1.02x slower                                                  |
| float                     | 94.4 ms                                                  | 97.0 ms: 1.03x slower                                                 |
| mdp                       | 3.36 sec                                                 | 3.47 sec: 1.03x slower                                                |
| tomli_loads               | 2.53 sec                                                 | 2.61 sec: 1.03x slower                                                |
| xml_etree_iterparse       | 147 ms                                                   | 153 ms: 1.04x slower                                                  |
| unpickle_pure_python      | 254 us                                                   | 267 us: 1.05x slower                                                  |
| logging_simple            | 7.04 us                                                  | 7.38 us: 1.05x slower                                                 |
| richards_super            | 60.3 ms                                                  | 63.9 ms: 1.06x slower                                                 |
| bench_thread_pool         | 1.28 ms                                                  | 1.36 ms: 1.07x slower                                                 |
| scimark_monte_carlo       | 83.8 ms                                                  | 90.0 ms: 1.07x slower                                                 |
| json_dumps                | 13.4 ms                                                  | 14.3 ms: 1.07x slower                                                 |
| async_tree_io             | 1.11 sec                                                 | 1.20 sec: 1.08x slower                                                |
| tornado_http              | 131 ms                                                   | 143 ms: 1.09x slower                                                  |
| go                        | 163 ms                                                   | 177 ms: 1.09x slower                                                  |
| pickle_pure_python        | 359 us                                                   | 392 us: 1.09x slower                                                  |
| meteor_contest            | 113 ms                                                   | 124 ms: 1.09x slower                                                  |
| python_startup            | 13.3 ms                                                  | 14.5 ms: 1.09x slower                                                 |
| scimark_lu                | 139 ms                                                   | 152 ms: 1.09x slower                                                  |
| crypto_pyaes              | 82.7 ms                                                  | 90.5 ms: 1.09x slower                                                 |
| typing_runtime_protocols  | 192 us                                                   | 210 us: 1.10x slower                                                  |
| scimark_sparse_mat_mult   | 6.58 ms                                                  | 7.27 ms: 1.10x slower                                                 |
| richards                  | 53.5 ms                                                  | 59.7 ms: 1.12x slower                                                 |
| html5lib                  | 64.3 ms                                                  | 71.7 ms: 1.12x slower                                                 |
| spectral_norm             | 141 ms                                                   | 159 ms: 1.12x slower                                                  |
| fannkuch                  | 452 ms                                                   | 513 ms: 1.14x slower                                                  |
| pyflate                   | 556 ms                                                   | 636 ms: 1.14x slower                                                  |
| async_tree_io_tg          | 1.09 sec                                                 | 1.26 sec: 1.16x slower                                                |
| deltablue                 | 3.85 ms                                                  | 4.49 ms: 1.16x slower                                                 |
| sqlglot_normalize         | 128 ms                                                   | 150 ms: 1.17x slower                                                  |
| pycparser                 | 1.26 sec                                                 | 1.48 sec: 1.17x slower                                                |
| genshi_text               | 27.7 ms                                                  | 32.6 ms: 1.18x slower                                                 |
| raytrace                  | 298 ms                                                   | 351 ms: 1.18x slower                                                  |
| 2to3                      | 306 ms                                                   | 363 ms: 1.19x slower                                                  |
| docutils                  | 2.91 sec                                                 | 3.48 sec: 1.20x slower                                                |
| django_template           | 42.3 ms                                                  | 50.6 ms: 1.20x slower                                                 |
| comprehensions            | 20.4 us                                                  | 24.6 us: 1.21x slower                                                 |
| sqlglot_parse             | 1.38 ms                                                  | 1.68 ms: 1.22x slower                                                 |
| sqlglot_optimize          | 62.4 ms                                                  | 77.0 ms: 1.23x slower                                                 |
| sympy_expand              | 455 ms                                                   | 563 ms: 1.24x slower                                                  |
| chaos                     | 68.8 ms                                                  | 85.4 ms: 1.24x slower                                                 |
| sqlglot_transpile         | 1.73 ms                                                  | 2.15 ms: 1.24x slower                                                 |
| regex_compile             | 128 ms                                                   | 162 ms: 1.26x slower                                                  |
| nqueens                   | 98.7 ms                                                  | 126 ms: 1.27x slower                                                  |
| pylint                    | 343 ms                                                   | 442 ms: 1.29x slower                                                  |
| sympy_str                 | 264 ms                                                   | 343 ms: 1.30x slower                                                  |
| genshi_xml                | 60.2 ms                                                  | 78.6 ms: 1.31x slower                                                 |
| pprint_safe_repr          | 926 ms                                                   | 1.22 sec: 1.32x slower                                                |
| pprint_pformat            | 1.90 sec                                                 | 2.58 sec: 1.36x slower                                                |
| hexiom                    | 7.13 ms                                                  | 9.81 ms: 1.37x slower                                                 |
| sympy_integrate           | 21.0 ms                                                  | 28.9 ms: 1.38x slower                                                 |
| gc_traversal              | 4.53 ms                                                  | 6.29 ms: 1.39x slower                                                 |
| sympy_sum                 | 143 ms                                                   | 205 ms: 1.43x slower                                                  |
| generators                | 37.8 ms                                                  | 58.8 ms: 1.56x slower                                                 |
| create_gc_cycles          | 2.12 ms                                                  | 3.64 ms: 1.72x slower                                                 |
| bench_mp_pool             | 7.30 ms                                                  | 4.29 sec: 587.71x slower                                              |
| Geometric mean            | (ref)                                                    | 1.18x slower                                                          |

Benchmark hidden because not significant (12): python_startup_no_site, json_loads, nbody, async_tree_cpu_io_mixed, pidigits, xml_etree_parse, asyncio_websockets, json, xml_etree_generate, regex_effbot, async_tree_cpu_io_mixed_tg, xml_etree_process
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (2) of results/bm-20241021-3.14.0a1+-7b3da21-JIT/bm-20241021-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21.json: dulwich_log, sphinx

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.22x