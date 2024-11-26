# Results vs. 3.13.0

- fork: brandtbucher
- ref: confidence
- machine: linux-x86_64
- commit hash: e29039d
- commit date: 2024-09-07
- overall geometric mean: 1.032x faster
- HPT reliability: 91.24%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 275 ms: 1.03x slower                                              |
| docutils       | 2.59 sec                                               | 3.01 sec: 1.16x slower                                            |
| tornado_http   | 92.4 ms                                                | 94.9 ms: 1.03x slower                                             |
| Geometric mean | (ref)                                                  | 1.05x slower                                                      |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|---------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization_tg | 464 ms                                                 | 403 ms: 1.15x faster                                              |
| async_tree_memoization    | 442 ms                                                 | 394 ms: 1.12x faster                                              |
| async_tree_none           | 351 ms                                                 | 326 ms: 1.08x faster                                              |
| async_tree_none_tg        | 321 ms                                                 | 312 ms: 1.03x faster                                              |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 565 ms: 1.02x faster                                              |
| coroutines                | 22.7 ms                                                | 22.3 ms: 1.02x faster                                             |
| asyncio_websockets        | 552 ms                                                 | 555 ms: 1.01x slower                                              |
| async_generators          | 436 ms                                                 | 456 ms: 1.05x slower                                              |
| async_tree_io_tg          | 857 ms                                                 | 897 ms: 1.05x slower                                              |
| async_tree_io             | 842 ms                                                 | 932 ms: 1.11x slower                                              |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                      |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 79.2 ms                                                | 70.3 ms: 1.13x faster                                             |
| nbody          | 87.0 ms                                                | 79.5 ms: 1.09x faster                                             |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                              |
| Geometric mean | (ref)                                                  | 1.07x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.8 ms: 1.06x faster                                             |
| regex_effbot   | 3.73 ms                                                | 3.78 ms: 1.01x slower                                             |
| regex_dna      | 218 ms                                                 | 222 ms: 1.02x slower                                              |
| regex_compile  | 132 ms                                                 | 139 ms: 1.05x slower                                              |
| Geometric mean | (ref)                                                  | 1.01x slower                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| xml_etree_generate   | 86.7 ms                                                | 77.3 ms: 1.12x faster                                             |
| tomli_loads          | 2.14 sec                                               | 1.92 sec: 1.12x faster                                            |
| xml_etree_process    | 60.6 ms                                                | 54.8 ms: 1.11x faster                                             |
| xml_etree_parse      | 156 ms                                                 | 145 ms: 1.07x faster                                              |
| pickle_pure_python   | 310 us                                                 | 300 us: 1.03x faster                                              |
| xml_etree_iterparse  | 101 ms                                                 | 98.3 ms: 1.03x faster                                             |
| json_dumps           | 10.6 ms                                                | 10.3 ms: 1.03x faster                                             |
| unpickle_pure_python | 216 us                                                 | 211 us: 1.02x faster                                              |
| json_loads           | 27.2 us                                                | 28.5 us: 1.05x slower                                             |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.6 ms: 1.17x faster                                             |
| python_startup_no_site | 6.96 ms                                                | 7.16 ms: 1.03x slower                                             |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.84 ms: 1.13x faster                                             |
| django_template | 35.2 ms                                                | 35.5 ms: 1.01x slower                                             |
| genshi_text     | 23.5 ms                                                | 24.0 ms: 1.02x slower                                             |
| genshi_xml      | 50.9 ms                                                | 56.7 ms: 1.11x slower                                             |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                      |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|---------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| deepcopy_memo             | 39.1 us                                                | 26.8 us: 1.46x faster                                             |
| create_gc_cycles          | 2.41 ms                                                | 1.76 ms: 1.37x faster                                             |
| deepcopy                  | 358 us                                                 | 269 us: 1.33x faster                                              |
| richards_super            | 54.9 ms                                                | 43.0 ms: 1.28x faster                                             |
| richards                  | 48.7 ms                                                | 38.9 ms: 1.25x faster                                             |
| deepcopy_reduce           | 3.20 us                                                | 2.67 us: 1.20x faster                                             |
| python_startup            | 12.5 ms                                                | 10.6 ms: 1.17x faster                                             |
| scimark_fft               | 364 ms                                                 | 311 ms: 1.17x faster                                              |
| spectral_norm             | 115 ms                                                 | 98.6 ms: 1.17x faster                                             |
| gc_traversal              | 4.37 ms                                                | 3.74 ms: 1.17x faster                                             |
| scimark_sparse_mat_mult   | 5.04 ms                                                | 4.36 ms: 1.16x faster                                             |
| async_tree_memoization_tg | 464 ms                                                 | 403 ms: 1.15x faster                                              |
| crypto_pyaes              | 75.3 ms                                                | 66.0 ms: 1.14x faster                                             |
| mako                      | 11.1 ms                                                | 9.84 ms: 1.13x faster                                             |
| float                     | 79.2 ms                                                | 70.3 ms: 1.13x faster                                             |
| xml_etree_generate        | 86.7 ms                                                | 77.3 ms: 1.12x faster                                             |
| async_tree_memoization    | 442 ms                                                 | 394 ms: 1.12x faster                                              |
| tomli_loads               | 2.14 sec                                               | 1.92 sec: 1.12x faster                                            |
| go                        | 144 ms                                                 | 130 ms: 1.11x faster                                              |
| xml_etree_process         | 60.6 ms                                                | 54.8 ms: 1.11x faster                                             |
| nbody                     | 87.0 ms                                                | 79.5 ms: 1.09x faster                                             |
| telco                     | 8.54 ms                                                | 7.81 ms: 1.09x faster                                             |
| pyflate                   | 471 ms                                                 | 432 ms: 1.09x faster                                              |
| fannkuch                  | 404 ms                                                 | 373 ms: 1.09x faster                                              |
| pathlib                   | 17.5 ms                                                | 16.2 ms: 1.08x faster                                             |
| scimark_sor               | 124 ms                                                 | 114 ms: 1.08x faster                                              |
| async_tree_none           | 351 ms                                                 | 326 ms: 1.08x faster                                              |
| bpe_tokeniser             | 4.75 sec                                               | 4.41 sec: 1.08x faster                                            |
| xml_etree_parse           | 156 ms                                                 | 145 ms: 1.07x faster                                              |
| scimark_monte_carlo       | 67.4 ms                                                | 63.1 ms: 1.07x faster                                             |
| regex_v8                  | 26.2 ms                                                | 24.8 ms: 1.06x faster                                             |
| mdp                       | 2.72 sec                                               | 2.60 sec: 1.05x faster                                            |
| thrift                    | 809 us                                                 | 782 us: 1.03x faster                                              |
| pickle_pure_python        | 310 us                                                 | 300 us: 1.03x faster                                              |
| logging_format            | 6.40 us                                                | 6.19 us: 1.03x faster                                             |
| xml_etree_iterparse       | 101 ms                                                 | 98.3 ms: 1.03x faster                                             |
| async_tree_none_tg        | 321 ms                                                 | 312 ms: 1.03x faster                                              |
| scimark_lu                | 113 ms                                                 | 110 ms: 1.03x faster                                              |
| meteor_contest            | 109 ms                                                 | 106 ms: 1.03x faster                                              |
| json_dumps                | 10.6 ms                                                | 10.3 ms: 1.03x faster                                             |
| unpickle_pure_python      | 216 us                                                 | 211 us: 1.02x faster                                              |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 565 ms: 1.02x faster                                              |
| coroutines                | 22.7 ms                                                | 22.3 ms: 1.02x faster                                             |
| pprint_safe_repr          | 728 ms                                                 | 718 ms: 1.01x faster                                              |
| pprint_pformat            | 1.49 sec                                               | 1.47 sec: 1.01x faster                                            |
| logging_simple            | 5.72 us                                                | 5.68 us: 1.01x faster                                             |
| pidigits                  | 186 ms                                                 | 186 ms: 1.00x faster                                              |
| asyncio_websockets        | 552 ms                                                 | 555 ms: 1.01x slower                                              |
| chaos                     | 58.1 ms                                                | 58.6 ms: 1.01x slower                                             |
| django_template           | 35.2 ms                                                | 35.5 ms: 1.01x slower                                             |
| comprehensions            | 16.5 us                                                | 16.7 us: 1.01x slower                                             |
| regex_effbot              | 3.73 ms                                                | 3.78 ms: 1.01x slower                                             |
| regex_dna                 | 218 ms                                                 | 222 ms: 1.02x slower                                              |
| bench_thread_pool         | 822 us                                                 | 836 us: 1.02x slower                                              |
| genshi_text               | 23.5 ms                                                | 24.0 ms: 1.02x slower                                             |
| coverage                  | 84.0 ms                                                | 85.8 ms: 1.02x slower                                             |
| raytrace                  | 267 ms                                                 | 274 ms: 1.03x slower                                              |
| tornado_http              | 92.4 ms                                                | 94.9 ms: 1.03x slower                                             |
| python_startup_no_site    | 6.96 ms                                                | 7.16 ms: 1.03x slower                                             |
| 2to3                      | 267 ms                                                 | 275 ms: 1.03x slower                                              |
| sqlglot_parse             | 1.27 ms                                                | 1.33 ms: 1.04x slower                                             |
| sqlglot_normalize         | 108 ms                                                 | 112 ms: 1.04x slower                                              |
| async_generators          | 436 ms                                                 | 456 ms: 1.05x slower                                              |
| async_tree_io_tg          | 857 ms                                                 | 897 ms: 1.05x slower                                              |
| json_loads                | 27.2 us                                                | 28.5 us: 1.05x slower                                             |
| regex_compile             | 132 ms                                                 | 139 ms: 1.05x slower                                              |
| sqlglot_transpile         | 1.58 ms                                                | 1.67 ms: 1.05x slower                                             |
| dulwich_log               | 64.3 ms                                                | 68.6 ms: 1.07x slower                                             |
| sqlglot_optimize          | 53.7 ms                                                | 57.9 ms: 1.08x slower                                             |
| sympy_str                 | 275 ms                                                 | 298 ms: 1.08x slower                                              |
| sympy_expand              | 463 ms                                                 | 505 ms: 1.09x slower                                              |
| nqueens                   | 78.4 ms                                                | 85.5 ms: 1.09x slower                                             |
| async_tree_io             | 842 ms                                                 | 932 ms: 1.11x slower                                              |
| hexiom                    | 6.16 ms                                                | 6.83 ms: 1.11x slower                                             |
| genshi_xml                | 50.9 ms                                                | 56.7 ms: 1.11x slower                                             |
| generators                | 29.0 ms                                                | 32.9 ms: 1.14x slower                                             |
| sympy_integrate           | 19.9 ms                                                | 22.7 ms: 1.14x slower                                             |
| sympy_sum                 | 150 ms                                                 | 172 ms: 1.14x slower                                              |
| docutils                  | 2.59 sec                                               | 3.01 sec: 1.16x slower                                            |
| pylint                    | 313 ms                                                 | 371 ms: 1.19x slower                                              |
| Geometric mean            | (ref)                                                  | 1.03x faster                                                      |

Benchmark hidden because not significant (8): json, typing_runtime_protocols, deltablue, logging_silent, bench_mp_pool, async_tree_cpu_io_mixed_tg, html5lib, pycparser
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240907-3.14.0a0-e29039d-JIT/bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.032x faster
# HPT report

- Reliability score: 91.24% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x