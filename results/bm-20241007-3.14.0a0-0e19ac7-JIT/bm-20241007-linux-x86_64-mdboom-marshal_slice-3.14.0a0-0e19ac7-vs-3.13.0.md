# Results vs. 3.13.0

- fork: mdboom
- ref: marshal_slice
- machine: linux-x86_64
- commit hash: 0e19ac7
- commit date: 2024-10-07
- overall geometric mean: 1.01x slower
- HPT reliability: 83.89%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 277 ms: 1.05x slower                                           |
| docutils       | 2.58 sec                                               | 2.93 sec: 1.13x slower                                         |
| tornado_http   | 91.5 ms                                                | 94.5 ms: 1.03x slower                                          |
| Geometric mean | (ref)                                                  | 1.05x slower                                                   |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|---------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 403 ms: 1.15x faster                                           |
| async_tree_memoization    | 442 ms                                                 | 401 ms: 1.10x faster                                           |
| async_tree_none           | 354 ms                                                 | 331 ms: 1.07x faster                                           |
| async_tree_none_tg        | 320 ms                                                 | 310 ms: 1.03x faster                                           |
| asyncio_tcp               | 488 ms                                                 | 485 ms: 1.01x faster                                           |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.81 sec: 1.01x slower                                         |
| async_generators          | 433 ms                                                 | 460 ms: 1.06x slower                                           |
| async_tree_io_tg          | 825 ms                                                 | 915 ms: 1.11x slower                                           |
| async_tree_io             | 843 ms                                                 | 937 ms: 1.11x slower                                           |
| Geometric mean            | (ref)                                                  | 1.00x faster                                                   |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed, asyncio_websockets, coroutines, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 78.5 ms                                                | 72.2 ms: 1.09x faster                                          |
| nbody          | 85.7 ms                                                | 80.7 ms: 1.06x faster                                          |
| pidigits       | 186 ms                                                 | 185 ms: 1.00x faster                                           |
| Geometric mean | (ref)                                                  | 1.05x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_v8       | 25.3 ms                                                | 24.1 ms: 1.05x faster                                          |
| regex_effbot   | 3.88 ms                                                | 3.77 ms: 1.03x faster                                          |
| regex_dna      | 220 ms                                                 | 219 ms: 1.00x faster                                           |
| regex_compile  | 131 ms                                                 | 143 ms: 1.09x slower                                           |
| Geometric mean | (ref)                                                  | 1.00x slower                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 77.2 ms: 1.13x faster                                          |
| xml_etree_process    | 60.4 ms                                                | 54.4 ms: 1.11x faster                                          |
| tomli_loads          | 2.11 sec                                               | 1.91 sec: 1.11x faster                                         |
| xml_etree_parse      | 156 ms                                                 | 144 ms: 1.08x faster                                           |
| json_dumps           | 10.4 ms                                                | 10.0 ms: 1.04x faster                                          |
| xml_etree_iterparse  | 102 ms                                                 | 99.1 ms: 1.03x faster                                          |
| unpickle             | 14.9 us                                                | 14.5 us: 1.03x faster                                          |
| json_loads           | 27.0 us                                                | 26.6 us: 1.01x faster                                          |
| pickle               | 11.6 us                                                | 11.5 us: 1.01x faster                                          |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                           |
| pickle_pure_python   | 300 us                                                 | 307 us: 1.02x slower                                           |
| pickle_dict          | 33.2 us                                                | 34.1 us: 1.03x slower                                          |
| pickle_list          | 5.01 us                                                | 5.20 us: 1.04x slower                                          |
| unpickle_list        | 4.96 us                                                | 5.17 us: 1.04x slower                                          |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.00x faster                                          |
| python_startup_no_site | 6.99 ms                                                | 7.09 ms: 1.02x slower                                          |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.0 ms: 1.11x faster                                          |
| django_template | 34.4 ms                                                | 35.5 ms: 1.03x slower                                          |
| genshi_text     | 22.9 ms                                                | 25.5 ms: 1.11x slower                                          |
| genshi_xml      | 50.3 ms                                                | 58.3 ms: 1.16x slower                                          |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                   |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|---------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 26.9 us: 1.41x faster                                          |
| deepcopy                  | 352 us                                                 | 266 us: 1.33x faster                                           |
| deepcopy_reduce           | 3.17 us                                                | 2.66 us: 1.19x faster                                          |
| scimark_fft               | 369 ms                                                 | 310 ms: 1.19x faster                                           |
| richards_super            | 54.4 ms                                                | 46.9 ms: 1.16x faster                                          |
| async_tree_memoization_tg | 465 ms                                                 | 403 ms: 1.15x faster                                           |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.42 ms: 1.14x faster                                          |
| richards                  | 48.1 ms                                                | 42.6 ms: 1.13x faster                                          |
| xml_etree_generate        | 87.0 ms                                                | 77.2 ms: 1.13x faster                                          |
| spectral_norm             | 115 ms                                                 | 102 ms: 1.12x faster                                           |
| telco                     | 8.45 ms                                                | 7.56 ms: 1.12x faster                                          |
| xml_etree_process         | 60.4 ms                                                | 54.4 ms: 1.11x faster                                          |
| crypto_pyaes              | 73.0 ms                                                | 65.8 ms: 1.11x faster                                          |
| mako                      | 11.1 ms                                                | 10.0 ms: 1.11x faster                                          |
| tomli_loads               | 2.11 sec                                               | 1.91 sec: 1.11x faster                                         |
| async_tree_memoization    | 442 ms                                                 | 401 ms: 1.10x faster                                           |
| float                     | 78.5 ms                                                | 72.2 ms: 1.09x faster                                          |
| bpe_tokeniser             | 4.69 sec                                               | 4.32 sec: 1.09x faster                                         |
| xml_etree_parse           | 156 ms                                                 | 144 ms: 1.08x faster                                           |
| mdp                       | 2.74 sec                                               | 2.54 sec: 1.08x faster                                         |
| go                        | 142 ms                                                 | 132 ms: 1.08x faster                                           |
| pathlib                   | 17.1 ms                                                | 15.9 ms: 1.07x faster                                          |
| async_tree_none           | 354 ms                                                 | 331 ms: 1.07x faster                                           |
| nbody                     | 85.7 ms                                                | 80.7 ms: 1.06x faster                                          |
| regex_v8                  | 25.3 ms                                                | 24.1 ms: 1.05x faster                                          |
| pyflate                   | 460 ms                                                 | 439 ms: 1.05x faster                                           |
| scimark_monte_carlo       | 66.3 ms                                                | 63.3 ms: 1.05x faster                                          |
| pprint_safe_repr          | 744 ms                                                 | 712 ms: 1.04x faster                                           |
| json_dumps                | 10.4 ms                                                | 10.0 ms: 1.04x faster                                          |
| sqlite_synth              | 2.85 us                                                | 2.75 us: 1.04x faster                                          |
| scimark_sor               | 122 ms                                                 | 118 ms: 1.04x faster                                           |
| fannkuch                  | 381 ms                                                 | 369 ms: 1.03x faster                                           |
| async_tree_none_tg        | 320 ms                                                 | 310 ms: 1.03x faster                                           |
| xml_etree_iterparse       | 102 ms                                                 | 99.1 ms: 1.03x faster                                          |
| regex_effbot              | 3.88 ms                                                | 3.77 ms: 1.03x faster                                          |
| scimark_lu                | 115 ms                                                 | 112 ms: 1.03x faster                                           |
| pycparser                 | 1.19 sec                                               | 1.16 sec: 1.03x faster                                         |
| unpickle                  | 14.9 us                                                | 14.5 us: 1.03x faster                                          |
| meteor_contest            | 108 ms                                                 | 105 ms: 1.02x faster                                           |
| thrift                    | 796 us                                                 | 783 us: 1.02x faster                                           |
| json_loads                | 27.0 us                                                | 26.6 us: 1.01x faster                                          |
| logging_silent            | 102 ns                                                 | 101 ns: 1.01x faster                                           |
| pprint_pformat            | 1.51 sec                                               | 1.49 sec: 1.01x faster                                         |
| pickle                    | 11.6 us                                                | 11.5 us: 1.01x faster                                          |
| logging_format            | 6.25 us                                                | 6.20 us: 1.01x faster                                          |
| asyncio_tcp               | 488 ms                                                 | 485 ms: 1.01x faster                                           |
| gc_traversal              | 3.81 ms                                                | 3.78 ms: 1.01x faster                                          |
| pidigits                  | 186 ms                                                 | 185 ms: 1.00x faster                                           |
| regex_dna                 | 220 ms                                                 | 219 ms: 1.00x faster                                           |
| python_startup            | 10.6 ms                                                | 10.6 ms: 1.00x faster                                          |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.81 sec: 1.01x slower                                         |
| python_startup_no_site    | 6.99 ms                                                | 7.09 ms: 1.02x slower                                          |
| unpickle_pure_python      | 213 us                                                 | 217 us: 1.02x slower                                           |
| chaos                     | 58.4 ms                                                | 59.4 ms: 1.02x slower                                          |
| coverage                  | 83.7 ms                                                | 85.3 ms: 1.02x slower                                          |
| pickle_pure_python        | 300 us                                                 | 307 us: 1.02x slower                                           |
| deltablue                 | 3.15 ms                                                | 3.23 ms: 1.03x slower                                          |
| pickle_dict               | 33.2 us                                                | 34.1 us: 1.03x slower                                          |
| django_template           | 34.4 ms                                                | 35.5 ms: 1.03x slower                                          |
| tornado_http              | 91.5 ms                                                | 94.5 ms: 1.03x slower                                          |
| comprehensions            | 16.4 us                                                | 17.0 us: 1.03x slower                                          |
| pickle_list               | 5.01 us                                                | 5.20 us: 1.04x slower                                          |
| unpickle_list             | 4.96 us                                                | 5.17 us: 1.04x slower                                          |
| 2to3                      | 265 ms                                                 | 277 ms: 1.05x slower                                           |
| typing_runtime_protocols  | 159 us                                                 | 167 us: 1.05x slower                                           |
| raytrace                  | 262 ms                                                 | 277 ms: 1.06x slower                                           |
| async_generators          | 433 ms                                                 | 460 ms: 1.06x slower                                           |
| dulwich_log               | 63.0 ms                                                | 67.3 ms: 1.07x slower                                          |
| sqlglot_transpile         | 1.57 ms                                                | 1.69 ms: 1.07x slower                                          |
| sqlglot_parse             | 1.27 ms                                                | 1.36 ms: 1.08x slower                                          |
| nqueens                   | 80.6 ms                                                | 86.7 ms: 1.08x slower                                          |
| sqlglot_normalize         | 107 ms                                                 | 116 ms: 1.08x slower                                           |
| sympy_expand              | 462 ms                                                 | 502 ms: 1.09x slower                                           |
| regex_compile             | 131 ms                                                 | 143 ms: 1.09x slower                                           |
| bench_thread_pool         | 815 us                                                 | 890 us: 1.09x slower                                           |
| sympy_str                 | 274 ms                                                 | 301 ms: 1.10x slower                                           |
| async_tree_io_tg          | 825 ms                                                 | 915 ms: 1.11x slower                                           |
| async_tree_io             | 843 ms                                                 | 937 ms: 1.11x slower                                           |
| genshi_text               | 22.9 ms                                                | 25.5 ms: 1.11x slower                                          |
| create_gc_cycles          | 1.61 ms                                                | 1.80 ms: 1.12x slower                                          |
| sqlglot_optimize          | 53.9 ms                                                | 60.4 ms: 1.12x slower                                          |
| docutils                  | 2.58 sec                                               | 2.93 sec: 1.13x slower                                         |
| hexiom                    | 6.13 ms                                                | 6.97 ms: 1.14x slower                                          |
| genshi_xml                | 50.3 ms                                                | 58.3 ms: 1.16x slower                                          |
| sympy_sum                 | 150 ms                                                 | 175 ms: 1.17x slower                                           |
| sympy_integrate           | 19.9 ms                                                | 23.3 ms: 1.17x slower                                          |
| pylint                    | 313 ms                                                 | 375 ms: 1.20x slower                                           |
| generators                | 28.8 ms                                                | 35.0 ms: 1.22x slower                                          |
| unpack_sequence           | 42.4 ns                                                | 108 ns: 2.54x slower                                           |
| bench_mp_pool             | 24.0 ms                                                | 61.2 ms: 2.55x slower                                          |
| Geometric mean            | (ref)                                                  | 1.01x slower                                                   |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed, logging_simple, json, html5lib, asyncio_websockets, coroutines, async_tree_cpu_io_mixed_tg
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 83.89% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x