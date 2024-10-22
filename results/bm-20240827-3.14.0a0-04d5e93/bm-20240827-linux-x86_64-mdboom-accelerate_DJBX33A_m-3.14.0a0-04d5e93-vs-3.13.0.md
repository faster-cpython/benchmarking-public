# Results vs. 3.13.0

- fork: mdboom
- ref: accelerate_DJBX33A_m
- machine: linux-x86_64
- commit hash: 04d5e93
- commit date: 2024-08-27
- overall geometric mean: 1.01x faster
- HPT reliability: 92.17%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240827-linux-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 257 ms: 1.03x faster                                                  |
| docutils       | 2.58 sec                                               | 2.72 sec: 1.05x slower                                                |
| tornado_http   | 91.5 ms                                                | 90.5 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240827-linux-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 400 ms: 1.16x faster                                                  |
| async_tree_memoization    | 442 ms                                                 | 392 ms: 1.13x faster                                                  |
| async_tree_none           | 354 ms                                                 | 322 ms: 1.10x faster                                                  |
| async_tree_none_tg        | 320 ms                                                 | 305 ms: 1.05x faster                                                  |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 561 ms: 1.02x faster                                                  |
| asyncio_tcp               | 488 ms                                                 | 482 ms: 1.01x faster                                                  |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.79 sec: 1.00x faster                                                |
| coroutines                | 22.5 ms                                                | 22.9 ms: 1.02x slower                                                 |
| async_tree_io_tg          | 825 ms                                                 | 894 ms: 1.08x slower                                                  |
| async_tree_io             | 843 ms                                                 | 929 ms: 1.10x slower                                                  |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed_tg, async_generators, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240827-linux-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 77.1 ms: 1.02x faster                                                 |
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240827-linux-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.73 ms: 1.04x faster                                                 |
| regex_compile  | 131 ms                                                 | 131 ms: 1.00x faster                                                  |
| regex_dna      | 220 ms                                                 | 220 ms: 1.00x slower                                                  |
| regex_v8       | 25.3 ms                                                | 26.2 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240827-linux-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 2.02 sec: 1.04x faster                                                |
| xml_etree_process    | 60.4 ms                                                | 58.9 ms: 1.03x faster                                                 |
| xml_etree_generate   | 87.0 ms                                                | 85.0 ms: 1.02x faster                                                 |
| unpickle_pure_python | 213 us                                                 | 212 us: 1.01x faster                                                  |
| pickle_pure_python   | 300 us                                                 | 303 us: 1.01x slower                                                  |
| xml_etree_iterparse  | 102 ms                                                 | 105 ms: 1.03x slower                                                  |
| json_loads           | 27.0 us                                                | 28.3 us: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (2): xml_etree_parse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240827-linux-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                 |
| python_startup_no_site | 6.99 ms                                                | 7.04 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240827-linux-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 34.4 ms                                                | 34.3 ms: 1.00x faster                                                 |
| genshi_text     | 22.9 ms                                                | 23.3 ms: 1.02x slower                                                 |
| mako            | 11.1 ms                                                | 11.3 ms: 1.02x slower                                                 |
| genshi_xml      | 50.3 ms                                                | 51.9 ms: 1.03x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                          |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240827-linux-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                  | 352 us                                                 | 262 us: 1.34x faster                                                  |
| deepcopy_memo             | 38.0 us                                                | 29.3 us: 1.30x faster                                                 |
| deepcopy_reduce           | 3.17 us                                                | 2.69 us: 1.18x faster                                                 |
| async_tree_memoization_tg | 465 ms                                                 | 400 ms: 1.16x faster                                                  |
| async_tree_memoization    | 442 ms                                                 | 392 ms: 1.13x faster                                                  |
| async_tree_none           | 354 ms                                                 | 322 ms: 1.10x faster                                                  |
| mdp                       | 2.74 sec                                               | 2.53 sec: 1.08x faster                                                |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.68 ms: 1.07x faster                                                 |
| pathlib                   | 17.1 ms                                                | 15.9 ms: 1.07x faster                                                 |
| richards_super            | 54.4 ms                                                | 51.9 ms: 1.05x faster                                                 |
| async_tree_none_tg        | 320 ms                                                 | 305 ms: 1.05x faster                                                  |
| logging_silent            | 102 ns                                                 | 97.7 ns: 1.05x faster                                                 |
| tomli_loads               | 2.11 sec                                               | 2.02 sec: 1.04x faster                                                |
| regex_effbot              | 3.88 ms                                                | 3.73 ms: 1.04x faster                                                 |
| logging_simple            | 5.66 us                                                | 5.44 us: 1.04x faster                                                 |
| bench_thread_pool         | 815 us                                                 | 784 us: 1.04x faster                                                  |
| richards                  | 48.1 ms                                                | 46.4 ms: 1.04x faster                                                 |
| spectral_norm             | 115 ms                                                 | 111 ms: 1.04x faster                                                  |
| generators                | 28.8 ms                                                | 27.9 ms: 1.03x faster                                                 |
| 2to3                      | 265 ms                                                 | 257 ms: 1.03x faster                                                  |
| thrift                    | 796 us                                                 | 774 us: 1.03x faster                                                  |
| pprint_safe_repr          | 744 ms                                                 | 724 ms: 1.03x faster                                                  |
| scimark_lu                | 115 ms                                                 | 112 ms: 1.03x faster                                                  |
| xml_etree_process         | 60.4 ms                                                | 58.9 ms: 1.03x faster                                                 |
| xml_etree_generate        | 87.0 ms                                                | 85.0 ms: 1.02x faster                                                 |
| scimark_fft               | 369 ms                                                 | 360 ms: 1.02x faster                                                  |
| logging_format            | 6.25 us                                                | 6.11 us: 1.02x faster                                                 |
| pprint_pformat            | 1.51 sec                                               | 1.48 sec: 1.02x faster                                                |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 561 ms: 1.02x faster                                                  |
| sympy_str                 | 274 ms                                                 | 268 ms: 1.02x faster                                                  |
| float                     | 78.5 ms                                                | 77.1 ms: 1.02x faster                                                 |
| sympy_integrate           | 19.9 ms                                                | 19.6 ms: 1.01x faster                                                 |
| telco                     | 8.45 ms                                                | 8.33 ms: 1.01x faster                                                 |
| asyncio_tcp               | 488 ms                                                 | 482 ms: 1.01x faster                                                  |
| tornado_http              | 91.5 ms                                                | 90.5 ms: 1.01x faster                                                 |
| sympy_sum                 | 150 ms                                                 | 148 ms: 1.01x faster                                                  |
| python_startup            | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                 |
| gc_traversal              | 3.81 ms                                                | 3.77 ms: 1.01x faster                                                 |
| sympy_expand              | 462 ms                                                 | 458 ms: 1.01x faster                                                  |
| sqlglot_optimize          | 53.9 ms                                                | 53.5 ms: 1.01x faster                                                 |
| unpickle_pure_python      | 213 us                                                 | 212 us: 1.01x faster                                                  |
| regex_compile             | 131 ms                                                 | 131 ms: 1.00x faster                                                  |
| django_template           | 34.4 ms                                                | 34.3 ms: 1.00x faster                                                 |
| hexiom                    | 6.13 ms                                                | 6.10 ms: 1.00x faster                                                 |
| sqlglot_normalize         | 107 ms                                                 | 107 ms: 1.00x faster                                                  |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.79 sec: 1.00x faster                                                |
| regex_dna                 | 220 ms                                                 | 220 ms: 1.00x slower                                                  |
| comprehensions            | 16.4 us                                                | 16.5 us: 1.00x slower                                                 |
| pidigits                  | 186 ms                                                 | 187 ms: 1.01x slower                                                  |
| python_startup_no_site    | 6.99 ms                                                | 7.04 ms: 1.01x slower                                                 |
| pickle_pure_python        | 300 us                                                 | 303 us: 1.01x slower                                                  |
| sqlglot_parse             | 1.27 ms                                                | 1.28 ms: 1.01x slower                                                 |
| pycparser                 | 1.19 sec                                               | 1.21 sec: 1.01x slower                                                |
| deltablue                 | 3.15 ms                                                | 3.19 ms: 1.01x slower                                                 |
| coverage                  | 83.7 ms                                                | 84.9 ms: 1.01x slower                                                 |
| pyflate                   | 460 ms                                                 | 466 ms: 1.01x slower                                                  |
| crypto_pyaes              | 73.0 ms                                                | 74.0 ms: 1.01x slower                                                 |
| genshi_text               | 22.9 ms                                                | 23.3 ms: 1.02x slower                                                 |
| coroutines                | 22.5 ms                                                | 22.9 ms: 1.02x slower                                                 |
| mako                      | 11.1 ms                                                | 11.3 ms: 1.02x slower                                                 |
| scimark_monte_carlo       | 66.3 ms                                                | 67.6 ms: 1.02x slower                                                 |
| typing_runtime_protocols  | 159 us                                                 | 163 us: 1.02x slower                                                  |
| scimark_sor               | 122 ms                                                 | 126 ms: 1.03x slower                                                  |
| genshi_xml                | 50.3 ms                                                | 51.9 ms: 1.03x slower                                                 |
| xml_etree_iterparse       | 102 ms                                                 | 105 ms: 1.03x slower                                                  |
| bpe_tokeniser             | 4.69 sec                                               | 4.85 sec: 1.03x slower                                                |
| regex_v8                  | 25.3 ms                                                | 26.2 ms: 1.04x slower                                                 |
| json_loads                | 27.0 us                                                | 28.3 us: 1.05x slower                                                 |
| docutils                  | 2.58 sec                                               | 2.72 sec: 1.05x slower                                                |
| fannkuch                  | 381 ms                                                 | 406 ms: 1.07x slower                                                  |
| create_gc_cycles          | 1.61 ms                                                | 1.73 ms: 1.08x slower                                                 |
| async_tree_io_tg          | 825 ms                                                 | 894 ms: 1.08x slower                                                  |
| async_tree_io             | 843 ms                                                 | 929 ms: 1.10x slower                                                  |
| go                        | 142 ms                                                 | 162 ms: 1.15x slower                                                  |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (15): xml_etree_parse, nbody, meteor_contest, nqueens, raytrace, async_tree_cpu_io_mixed_tg, async_generators, bench_mp_pool, sqlglot_transpile, chaos, json, asyncio_websockets, json_dumps, html5lib, pylint
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 92.17% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x