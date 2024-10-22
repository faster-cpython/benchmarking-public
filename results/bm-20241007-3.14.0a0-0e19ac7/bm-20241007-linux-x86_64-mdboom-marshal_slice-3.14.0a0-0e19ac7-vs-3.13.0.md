# Results vs. 3.13.0

- fork: mdboom
- ref: marshal_slice
- machine: linux-x86_64
- commit hash: 0e19ac7
- commit date: 2024-10-07
- overall geometric mean: 1.01x faster
- HPT reliability: 98.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 253 ms: 1.05x faster                                           |
| docutils       | 2.58 sec                                               | 2.62 sec: 1.02x slower                                         |
| html5lib       | 64.5 ms                                                | 61.4 ms: 1.05x faster                                          |
| tornado_http   | 91.5 ms                                                | 90.2 ms: 1.01x faster                                          |
| Geometric mean | (ref)                                                  | 1.02x faster                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|---------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 400 ms: 1.16x faster                                           |
| async_tree_memoization    | 442 ms                                                 | 389 ms: 1.14x faster                                           |
| async_tree_none           | 354 ms                                                 | 320 ms: 1.11x faster                                           |
| async_tree_none_tg        | 320 ms                                                 | 307 ms: 1.04x faster                                           |
| asyncio_tcp               | 488 ms                                                 | 470 ms: 1.04x faster                                           |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 555 ms: 1.03x faster                                           |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.77 sec: 1.01x faster                                         |
| asyncio_websockets        | 555 ms                                                 | 558 ms: 1.00x slower                                           |
| coroutines                | 22.5 ms                                                | 22.8 ms: 1.01x slower                                          |
| async_tree_io             | 843 ms                                                 | 924 ms: 1.10x slower                                           |
| async_tree_io_tg          | 825 ms                                                 | 915 ms: 1.11x slower                                           |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                   |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 78.5 ms                                                | 76.1 ms: 1.03x faster                                          |
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                           |
| nbody          | 85.7 ms                                                | 86.8 ms: 1.01x slower                                          |
| Geometric mean | (ref)                                                  | 1.00x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.70 ms: 1.05x faster                                          |
| regex_compile  | 131 ms                                                 | 127 ms: 1.03x faster                                           |
| regex_v8       | 25.3 ms                                                | 25.2 ms: 1.00x faster                                          |
| regex_dna      | 220 ms                                                 | 220 ms: 1.00x slower                                           |
| Geometric mean | (ref)                                                  | 1.02x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| xml_etree_process    | 60.4 ms                                                | 59.0 ms: 1.02x faster                                          |
| tomli_loads          | 2.11 sec                                               | 2.07 sec: 1.02x faster                                         |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                          |
| xml_etree_generate   | 87.0 ms                                                | 86.1 ms: 1.01x faster                                          |
| pickle               | 11.6 us                                                | 11.5 us: 1.00x faster                                          |
| json_loads           | 27.0 us                                                | 27.1 us: 1.00x slower                                          |
| unpickle_pure_python | 213 us                                                 | 215 us: 1.01x slower                                           |
| unpickle             | 14.9 us                                                | 15.0 us: 1.01x slower                                          |
| pickle_pure_python   | 300 us                                                 | 305 us: 1.02x slower                                           |
| xml_etree_iterparse  | 102 ms                                                 | 104 ms: 1.02x slower                                           |
| pickle_dict          | 33.2 us                                                | 34.9 us: 1.05x slower                                          |
| unpickle_list        | 4.96 us                                                | 5.41 us: 1.09x slower                                          |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                   |

Benchmark hidden because not significant (2): pickle_list, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                          |
| python_startup_no_site | 6.99 ms                                                | 7.01 ms: 1.00x slower                                          |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| genshi_text     | 22.9 ms                                                | 21.9 ms: 1.05x faster                                          |
| genshi_xml      | 50.3 ms                                                | 49.3 ms: 1.02x faster                                          |
| django_template | 34.4 ms                                                | 34.2 ms: 1.01x faster                                          |
| mako            | 11.1 ms                                                | 11.4 ms: 1.03x slower                                          |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                   |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|---------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| deepcopy                  | 352 us                                                 | 260 us: 1.36x faster                                           |
| deepcopy_memo             | 38.0 us                                                | 29.7 us: 1.28x faster                                          |
| go                        | 142 ms                                                 | 119 ms: 1.19x faster                                           |
| deepcopy_reduce           | 3.17 us                                                | 2.71 us: 1.17x faster                                          |
| async_tree_memoization_tg | 465 ms                                                 | 400 ms: 1.16x faster                                           |
| async_tree_memoization    | 442 ms                                                 | 389 ms: 1.14x faster                                           |
| async_tree_none           | 354 ms                                                 | 320 ms: 1.11x faster                                           |
| mdp                       | 2.74 sec                                               | 2.52 sec: 1.09x faster                                         |
| pathlib                   | 17.1 ms                                                | 15.8 ms: 1.08x faster                                          |
| pprint_safe_repr          | 744 ms                                                 | 703 ms: 1.06x faster                                           |
| telco                     | 8.45 ms                                                | 8.01 ms: 1.06x faster                                          |
| html5lib                  | 64.5 ms                                                | 61.4 ms: 1.05x faster                                          |
| regex_effbot              | 3.88 ms                                                | 3.70 ms: 1.05x faster                                          |
| pprint_pformat            | 1.51 sec                                               | 1.44 sec: 1.05x faster                                         |
| genshi_text               | 22.9 ms                                                | 21.9 ms: 1.05x faster                                          |
| richards                  | 48.1 ms                                                | 46.0 ms: 1.05x faster                                          |
| 2to3                      | 265 ms                                                 | 253 ms: 1.05x faster                                           |
| richards_super            | 54.4 ms                                                | 52.1 ms: 1.04x faster                                          |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.82 ms: 1.04x faster                                          |
| async_tree_none_tg        | 320 ms                                                 | 307 ms: 1.04x faster                                           |
| generators                | 28.8 ms                                                | 27.7 ms: 1.04x faster                                          |
| asyncio_tcp               | 488 ms                                                 | 470 ms: 1.04x faster                                           |
| thrift                    | 796 us                                                 | 767 us: 1.04x faster                                           |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 555 ms: 1.03x faster                                           |
| float                     | 78.5 ms                                                | 76.1 ms: 1.03x faster                                          |
| regex_compile             | 131 ms                                                 | 127 ms: 1.03x faster                                           |
| scimark_lu                | 115 ms                                                 | 112 ms: 1.03x faster                                           |
| sympy_expand              | 462 ms                                                 | 450 ms: 1.02x faster                                           |
| spectral_norm             | 115 ms                                                 | 112 ms: 1.02x faster                                           |
| json                      | 5.20 ms                                                | 5.07 ms: 1.02x faster                                          |
| sympy_str                 | 274 ms                                                 | 267 ms: 1.02x faster                                           |
| xml_etree_process         | 60.4 ms                                                | 59.0 ms: 1.02x faster                                          |
| tomli_loads               | 2.11 sec                                               | 2.07 sec: 1.02x faster                                         |
| genshi_xml                | 50.3 ms                                                | 49.3 ms: 1.02x faster                                          |
| sympy_sum                 | 150 ms                                                 | 146 ms: 1.02x faster                                           |
| logging_simple            | 5.66 us                                                | 5.55 us: 1.02x faster                                          |
| sqlite_synth              | 2.85 us                                                | 2.80 us: 1.02x faster                                          |
| pycparser                 | 1.19 sec                                               | 1.17 sec: 1.02x faster                                         |
| crypto_pyaes              | 73.0 ms                                                | 71.7 ms: 1.02x faster                                          |
| logging_format            | 6.25 us                                                | 6.15 us: 1.02x faster                                          |
| tornado_http              | 91.5 ms                                                | 90.2 ms: 1.01x faster                                          |
| json_dumps                | 10.4 ms                                                | 10.3 ms: 1.01x faster                                          |
| sqlglot_optimize          | 53.9 ms                                                | 53.3 ms: 1.01x faster                                          |
| scimark_fft               | 369 ms                                                 | 364 ms: 1.01x faster                                           |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.77 sec: 1.01x faster                                         |
| xml_etree_generate        | 87.0 ms                                                | 86.1 ms: 1.01x faster                                          |
| meteor_contest            | 108 ms                                                 | 107 ms: 1.01x faster                                           |
| django_template           | 34.4 ms                                                | 34.2 ms: 1.01x faster                                          |
| sqlglot_normalize         | 107 ms                                                 | 107 ms: 1.01x faster                                           |
| sympy_integrate           | 19.9 ms                                                | 19.8 ms: 1.01x faster                                          |
| pickle                    | 11.6 us                                                | 11.5 us: 1.00x faster                                          |
| python_startup            | 10.6 ms                                                | 10.5 ms: 1.00x faster                                          |
| regex_v8                  | 25.3 ms                                                | 25.2 ms: 1.00x faster                                          |
| regex_dna                 | 220 ms                                                 | 220 ms: 1.00x slower                                           |
| python_startup_no_site    | 6.99 ms                                                | 7.01 ms: 1.00x slower                                          |
| json_loads                | 27.0 us                                                | 27.1 us: 1.00x slower                                          |
| asyncio_websockets        | 555 ms                                                 | 558 ms: 1.00x slower                                           |
| sqlglot_transpile         | 1.57 ms                                                | 1.58 ms: 1.00x slower                                          |
| pidigits                  | 186 ms                                                 | 187 ms: 1.01x slower                                           |
| unpickle_pure_python      | 213 us                                                 | 215 us: 1.01x slower                                           |
| comprehensions            | 16.4 us                                                | 16.5 us: 1.01x slower                                          |
| sqlglot_parse             | 1.27 ms                                                | 1.28 ms: 1.01x slower                                          |
| bpe_tokeniser             | 4.69 sec                                               | 4.73 sec: 1.01x slower                                         |
| coverage                  | 83.7 ms                                                | 84.5 ms: 1.01x slower                                          |
| raytrace                  | 262 ms                                                 | 264 ms: 1.01x slower                                           |
| coroutines                | 22.5 ms                                                | 22.8 ms: 1.01x slower                                          |
| unpickle                  | 14.9 us                                                | 15.0 us: 1.01x slower                                          |
| nbody                     | 85.7 ms                                                | 86.8 ms: 1.01x slower                                          |
| scimark_sor               | 122 ms                                                 | 124 ms: 1.01x slower                                           |
| docutils                  | 2.58 sec                                               | 2.62 sec: 1.02x slower                                         |
| pickle_pure_python        | 300 us                                                 | 305 us: 1.02x slower                                           |
| hexiom                    | 6.13 ms                                                | 6.24 ms: 1.02x slower                                          |
| logging_silent            | 102 ns                                                 | 104 ns: 1.02x slower                                           |
| nqueens                   | 80.6 ms                                                | 82.2 ms: 1.02x slower                                          |
| xml_etree_iterparse       | 102 ms                                                 | 104 ms: 1.02x slower                                           |
| chaos                     | 58.4 ms                                                | 59.8 ms: 1.02x slower                                          |
| scimark_monte_carlo       | 66.3 ms                                                | 67.8 ms: 1.02x slower                                          |
| dulwich_log               | 63.0 ms                                                | 64.4 ms: 1.02x slower                                          |
| pyflate                   | 460 ms                                                 | 472 ms: 1.03x slower                                           |
| mako                      | 11.1 ms                                                | 11.4 ms: 1.03x slower                                          |
| deltablue                 | 3.15 ms                                                | 3.26 ms: 1.03x slower                                          |
| gc_traversal              | 3.81 ms                                                | 3.95 ms: 1.04x slower                                          |
| fannkuch                  | 381 ms                                                 | 399 ms: 1.05x slower                                           |
| bench_thread_pool         | 815 us                                                 | 856 us: 1.05x slower                                           |
| pickle_dict               | 33.2 us                                                | 34.9 us: 1.05x slower                                          |
| unpickle_list             | 4.96 us                                                | 5.41 us: 1.09x slower                                          |
| async_tree_io             | 843 ms                                                 | 924 ms: 1.10x slower                                           |
| async_tree_io_tg          | 825 ms                                                 | 915 ms: 1.11x slower                                           |
| create_gc_cycles          | 1.61 ms                                                | 1.79 ms: 1.11x slower                                          |
| unpack_sequence           | 42.4 ns                                                | 48.3 ns: 1.14x slower                                          |
| bench_mp_pool             | 24.0 ms                                                | 55.9 ms: 2.33x slower                                          |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                   |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed_tg, typing_runtime_protocols, pickle_list, async_generators, xml_etree_parse, pylint
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 98.96% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x