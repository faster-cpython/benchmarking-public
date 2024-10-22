# Results vs. 3.13.0

- fork: brandtbucher
- ref: confidence
- machine: linux-x86_64
- commit hash: e29039d
- commit date: 2024-09-07
- overall geometric mean: 1.00x faster
- HPT reliability: 83.45%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 275 ms: 1.04x slower                                              |
| docutils       | 2.58 sec                                               | 3.01 sec: 1.16x slower                                            |
| tornado_http   | 91.5 ms                                                | 94.9 ms: 1.04x slower                                             |
| Geometric mean | (ref)                                                  | 1.06x slower                                                      |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|---------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 403 ms: 1.15x faster                                              |
| async_tree_memoization    | 442 ms                                                 | 394 ms: 1.12x faster                                              |
| async_tree_none           | 354 ms                                                 | 326 ms: 1.09x faster                                              |
| async_tree_none_tg        | 320 ms                                                 | 312 ms: 1.03x faster                                              |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 565 ms: 1.02x faster                                              |
| coroutines                | 22.5 ms                                                | 22.3 ms: 1.01x faster                                             |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.01x slower                                            |
| async_generators          | 433 ms                                                 | 456 ms: 1.05x slower                                              |
| async_tree_io_tg          | 825 ms                                                 | 897 ms: 1.09x slower                                              |
| async_tree_io             | 843 ms                                                 | 932 ms: 1.11x slower                                              |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                      |

Benchmark hidden because not significant (3): asyncio_websockets, asyncio_tcp, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.3 ms: 1.12x faster                                             |
| nbody          | 85.7 ms                                                | 79.5 ms: 1.08x faster                                             |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                              |
| Geometric mean | (ref)                                                  | 1.06x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.78 ms: 1.03x faster                                             |
| regex_v8       | 25.3 ms                                                | 24.8 ms: 1.02x faster                                             |
| regex_dna      | 220 ms                                                 | 222 ms: 1.01x slower                                              |
| regex_compile  | 131 ms                                                 | 139 ms: 1.06x slower                                              |
| Geometric mean | (ref)                                                  | 1.01x slower                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 77.3 ms: 1.12x faster                                             |
| xml_etree_process    | 60.4 ms                                                | 54.8 ms: 1.10x faster                                             |
| tomli_loads          | 2.11 sec                                               | 1.92 sec: 1.10x faster                                            |
| xml_etree_parse      | 156 ms                                                 | 145 ms: 1.08x faster                                              |
| xml_etree_iterparse  | 102 ms                                                 | 98.3 ms: 1.04x faster                                             |
| unpickle_pure_python | 213 us                                                 | 211 us: 1.01x faster                                              |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                             |
| pickle_list          | 5.01 us                                                | 5.08 us: 1.02x slower                                             |
| pickle               | 11.6 us                                                | 11.8 us: 1.02x slower                                             |
| unpickle_list        | 4.96 us                                                | 5.18 us: 1.04x slower                                             |
| pickle_dict          | 33.2 us                                                | 34.8 us: 1.05x slower                                             |
| json_loads           | 27.0 us                                                | 28.5 us: 1.06x slower                                             |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                      |

Benchmark hidden because not significant (2): pickle_pure_python, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.01x slower                                             |
| python_startup_no_site | 6.99 ms                                                | 7.16 ms: 1.02x slower                                             |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.84 ms: 1.13x faster                                             |
| django_template | 34.4 ms                                                | 35.5 ms: 1.03x slower                                             |
| genshi_text     | 22.9 ms                                                | 24.0 ms: 1.05x slower                                             |
| genshi_xml      | 50.3 ms                                                | 56.7 ms: 1.13x slower                                             |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                      |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|---------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 26.8 us: 1.42x faster                                             |
| deepcopy                  | 352 us                                                 | 269 us: 1.31x faster                                              |
| richards_super            | 54.4 ms                                                | 43.0 ms: 1.27x faster                                             |
| richards                  | 48.1 ms                                                | 38.9 ms: 1.24x faster                                             |
| scimark_fft               | 369 ms                                                 | 311 ms: 1.19x faster                                              |
| deepcopy_reduce           | 3.17 us                                                | 2.67 us: 1.18x faster                                             |
| spectral_norm             | 115 ms                                                 | 98.6 ms: 1.17x faster                                             |
| async_tree_memoization_tg | 465 ms                                                 | 403 ms: 1.15x faster                                              |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.36 ms: 1.15x faster                                             |
| mako                      | 11.1 ms                                                | 9.84 ms: 1.13x faster                                             |
| xml_etree_generate        | 87.0 ms                                                | 77.3 ms: 1.12x faster                                             |
| async_tree_memoization    | 442 ms                                                 | 394 ms: 1.12x faster                                              |
| float                     | 78.5 ms                                                | 70.3 ms: 1.12x faster                                             |
| crypto_pyaes              | 73.0 ms                                                | 66.0 ms: 1.11x faster                                             |
| xml_etree_process         | 60.4 ms                                                | 54.8 ms: 1.10x faster                                             |
| tomli_loads               | 2.11 sec                                               | 1.92 sec: 1.10x faster                                            |
| go                        | 142 ms                                                 | 130 ms: 1.09x faster                                              |
| async_tree_none           | 354 ms                                                 | 326 ms: 1.09x faster                                              |
| telco                     | 8.45 ms                                                | 7.81 ms: 1.08x faster                                             |
| nbody                     | 85.7 ms                                                | 79.5 ms: 1.08x faster                                             |
| xml_etree_parse           | 156 ms                                                 | 145 ms: 1.08x faster                                              |
| scimark_sor               | 122 ms                                                 | 114 ms: 1.07x faster                                              |
| pyflate                   | 460 ms                                                 | 432 ms: 1.06x faster                                              |
| bpe_tokeniser             | 4.69 sec                                               | 4.41 sec: 1.06x faster                                            |
| mdp                       | 2.74 sec                                               | 2.60 sec: 1.05x faster                                            |
| pathlib                   | 17.1 ms                                                | 16.2 ms: 1.05x faster                                             |
| scimark_monte_carlo       | 66.3 ms                                                | 63.1 ms: 1.05x faster                                             |
| scimark_lu                | 115 ms                                                 | 110 ms: 1.05x faster                                              |
| sqlite_synth              | 2.85 us                                                | 2.74 us: 1.04x faster                                             |
| xml_etree_iterparse       | 102 ms                                                 | 98.3 ms: 1.04x faster                                             |
| pprint_safe_repr          | 744 ms                                                 | 718 ms: 1.04x faster                                              |
| regex_effbot              | 3.88 ms                                                | 3.78 ms: 1.03x faster                                             |
| async_tree_none_tg        | 320 ms                                                 | 312 ms: 1.03x faster                                              |
| pprint_pformat            | 1.51 sec                                               | 1.47 sec: 1.02x faster                                            |
| fannkuch                  | 381 ms                                                 | 373 ms: 1.02x faster                                              |
| regex_v8                  | 25.3 ms                                                | 24.8 ms: 1.02x faster                                             |
| thrift                    | 796 us                                                 | 782 us: 1.02x faster                                              |
| gc_traversal              | 3.81 ms                                                | 3.74 ms: 1.02x faster                                             |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 565 ms: 1.02x faster                                              |
| meteor_contest            | 108 ms                                                 | 106 ms: 1.01x faster                                              |
| coroutines                | 22.5 ms                                                | 22.3 ms: 1.01x faster                                             |
| unpickle_pure_python      | 213 us                                                 | 211 us: 1.01x faster                                              |
| json_dumps                | 10.4 ms                                                | 10.3 ms: 1.01x faster                                             |
| logging_format            | 6.25 us                                                | 6.19 us: 1.01x faster                                             |
| pidigits                  | 186 ms                                                 | 186 ms: 1.00x faster                                              |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.01x slower                                            |
| python_startup            | 10.6 ms                                                | 10.6 ms: 1.01x slower                                             |
| pycparser                 | 1.19 sec                                               | 1.20 sec: 1.01x slower                                            |
| regex_dna                 | 220 ms                                                 | 222 ms: 1.01x slower                                              |
| pickle_list               | 5.01 us                                                | 5.08 us: 1.02x slower                                             |
| comprehensions            | 16.4 us                                                | 16.7 us: 1.02x slower                                             |
| pickle                    | 11.6 us                                                | 11.8 us: 1.02x slower                                             |
| json                      | 5.20 ms                                                | 5.32 ms: 1.02x slower                                             |
| deltablue                 | 3.15 ms                                                | 3.22 ms: 1.02x slower                                             |
| python_startup_no_site    | 6.99 ms                                                | 7.16 ms: 1.02x slower                                             |
| coverage                  | 83.7 ms                                                | 85.8 ms: 1.02x slower                                             |
| bench_thread_pool         | 815 us                                                 | 836 us: 1.03x slower                                              |
| typing_runtime_protocols  | 159 us                                                 | 164 us: 1.03x slower                                              |
| django_template           | 34.4 ms                                                | 35.5 ms: 1.03x slower                                             |
| 2to3                      | 265 ms                                                 | 275 ms: 1.04x slower                                              |
| tornado_http              | 91.5 ms                                                | 94.9 ms: 1.04x slower                                             |
| unpickle_list             | 4.96 us                                                | 5.18 us: 1.04x slower                                             |
| sqlglot_normalize         | 107 ms                                                 | 112 ms: 1.05x slower                                              |
| sqlglot_parse             | 1.27 ms                                                | 1.33 ms: 1.05x slower                                             |
| raytrace                  | 262 ms                                                 | 274 ms: 1.05x slower                                              |
| pickle_dict               | 33.2 us                                                | 34.8 us: 1.05x slower                                             |
| genshi_text               | 22.9 ms                                                | 24.0 ms: 1.05x slower                                             |
| async_generators          | 433 ms                                                 | 456 ms: 1.05x slower                                              |
| json_loads                | 27.0 us                                                | 28.5 us: 1.06x slower                                             |
| nqueens                   | 80.6 ms                                                | 85.5 ms: 1.06x slower                                             |
| sqlglot_transpile         | 1.57 ms                                                | 1.67 ms: 1.06x slower                                             |
| regex_compile             | 131 ms                                                 | 139 ms: 1.06x slower                                              |
| sqlglot_optimize          | 53.9 ms                                                | 57.9 ms: 1.07x slower                                             |
| async_tree_io_tg          | 825 ms                                                 | 897 ms: 1.09x slower                                              |
| dulwich_log               | 63.0 ms                                                | 68.6 ms: 1.09x slower                                             |
| sympy_str                 | 274 ms                                                 | 298 ms: 1.09x slower                                              |
| sympy_expand              | 462 ms                                                 | 505 ms: 1.09x slower                                              |
| create_gc_cycles          | 1.61 ms                                                | 1.76 ms: 1.10x slower                                             |
| async_tree_io             | 843 ms                                                 | 932 ms: 1.11x slower                                              |
| hexiom                    | 6.13 ms                                                | 6.83 ms: 1.12x slower                                             |
| genshi_xml                | 50.3 ms                                                | 56.7 ms: 1.13x slower                                             |
| sympy_integrate           | 19.9 ms                                                | 22.7 ms: 1.14x slower                                             |
| generators                | 28.8 ms                                                | 32.9 ms: 1.14x slower                                             |
| sympy_sum                 | 150 ms                                                 | 172 ms: 1.15x slower                                              |
| docutils                  | 2.58 sec                                               | 3.01 sec: 1.16x slower                                            |
| pylint                    | 313 ms                                                 | 371 ms: 1.19x slower                                              |
| unpack_sequence           | 42.4 ns                                                | 107 ns: 2.52x slower                                              |
| Geometric mean            | (ref)                                                  | 1.00x faster                                                      |

Benchmark hidden because not significant (10): logging_silent, html5lib, asyncio_websockets, bench_mp_pool, pickle_pure_python, asyncio_tcp, chaos, logging_simple, async_tree_cpu_io_mixed_tg, unpickle
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 83.45% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.10x