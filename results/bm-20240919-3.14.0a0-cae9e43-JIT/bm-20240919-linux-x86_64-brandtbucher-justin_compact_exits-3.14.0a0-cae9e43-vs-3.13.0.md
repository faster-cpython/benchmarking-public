# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_compact_exits
- machine: linux-x86_64
- commit hash: cae9e43
- commit date: 2024-09-19
- overall geometric mean: 1.041x faster
- HPT reliability: 98.91%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 277 ms: 1.04x slower                                                        |
| docutils       | 2.59 sec                                               | 2.92 sec: 1.13x slower                                                      |
| tornado_http   | 92.4 ms                                                | 94.0 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                  | 1.06x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg | 464 ms                                                 | 371 ms: 1.25x faster                                                        |
| async_tree_memoization    | 442 ms                                                 | 380 ms: 1.16x faster                                                        |
| async_tree_none           | 351 ms                                                 | 320 ms: 1.09x faster                                                        |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 536 ms: 1.08x faster                                                        |
| async_tree_none_tg        | 321 ms                                                 | 307 ms: 1.04x faster                                                        |
| asyncio_websockets        | 552 ms                                                 | 555 ms: 1.01x slower                                                        |
| coroutines                | 22.7 ms                                                | 23.1 ms: 1.02x slower                                                       |
| async_generators          | 436 ms                                                 | 458 ms: 1.05x slower                                                        |
| async_tree_io             | 842 ms                                                 | 929 ms: 1.10x slower                                                        |
| Geometric mean            | (ref)                                                  | 1.04x faster                                                                |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 70.4 ms: 1.12x faster                                                       |
| nbody          | 87.0 ms                                                | 80.5 ms: 1.08x faster                                                       |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.0 ms: 1.09x faster                                                       |
| regex_effbot   | 3.73 ms                                                | 3.63 ms: 1.03x faster                                                       |
| regex_dna      | 218 ms                                                 | 215 ms: 1.01x faster                                                        |
| regex_compile  | 132 ms                                                 | 137 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 86.7 ms                                                | 76.0 ms: 1.14x faster                                                       |
| xml_etree_process    | 60.6 ms                                                | 53.7 ms: 1.13x faster                                                       |
| tomli_loads          | 2.14 sec                                               | 1.91 sec: 1.12x faster                                                      |
| xml_etree_parse      | 156 ms                                                 | 147 ms: 1.06x faster                                                        |
| xml_etree_iterparse  | 101 ms                                                 | 97.4 ms: 1.04x faster                                                       |
| json_dumps           | 10.6 ms                                                | 10.2 ms: 1.04x faster                                                       |
| pickle_pure_python   | 310 us                                                 | 302 us: 1.03x faster                                                        |
| unpickle_pure_python | 216 us                                                 | 213 us: 1.01x faster                                                        |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                                |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.18x faster                                                       |
| python_startup_no_site | 6.96 ms                                                | 7.07 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.72 ms: 1.14x faster                                                       |
| django_template | 35.2 ms                                                | 36.0 ms: 1.02x slower                                                       |
| genshi_text     | 23.5 ms                                                | 24.4 ms: 1.04x slower                                                       |
| genshi_xml      | 50.9 ms                                                | 56.4 ms: 1.11x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                                |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo             | 39.1 us                                                | 26.7 us: 1.47x faster                                                       |
| deepcopy                  | 358 us                                                 | 254 us: 1.41x faster                                                        |
| create_gc_cycles          | 2.41 ms                                                | 1.74 ms: 1.39x faster                                                       |
| async_tree_memoization_tg | 464 ms                                                 | 371 ms: 1.25x faster                                                        |
| richards_super            | 54.9 ms                                                | 45.7 ms: 1.20x faster                                                       |
| richards                  | 48.7 ms                                                | 40.7 ms: 1.20x faster                                                       |
| scimark_sparse_mat_mult   | 5.04 ms                                                | 4.21 ms: 1.20x faster                                                       |
| deepcopy_reduce           | 3.20 us                                                | 2.67 us: 1.20x faster                                                       |
| scimark_fft               | 364 ms                                                 | 306 ms: 1.19x faster                                                        |
| python_startup            | 12.5 ms                                                | 10.5 ms: 1.18x faster                                                       |
| gc_traversal              | 4.37 ms                                                | 3.72 ms: 1.17x faster                                                       |
| async_tree_memoization    | 442 ms                                                 | 380 ms: 1.16x faster                                                        |
| spectral_norm             | 115 ms                                                 | 100 ms: 1.15x faster                                                        |
| go                        | 144 ms                                                 | 125 ms: 1.15x faster                                                        |
| xml_etree_generate        | 86.7 ms                                                | 76.0 ms: 1.14x faster                                                       |
| crypto_pyaes              | 75.3 ms                                                | 66.0 ms: 1.14x faster                                                       |
| mako                      | 11.1 ms                                                | 9.72 ms: 1.14x faster                                                       |
| xml_etree_process         | 60.6 ms                                                | 53.7 ms: 1.13x faster                                                       |
| float                     | 79.2 ms                                                | 70.4 ms: 1.12x faster                                                       |
| tomli_loads               | 2.14 sec                                               | 1.91 sec: 1.12x faster                                                      |
| pathlib                   | 17.5 ms                                                | 15.7 ms: 1.12x faster                                                       |
| async_tree_none           | 351 ms                                                 | 320 ms: 1.09x faster                                                        |
| regex_v8                  | 26.2 ms                                                | 24.0 ms: 1.09x faster                                                       |
| bpe_tokeniser             | 4.75 sec                                               | 4.38 sec: 1.08x faster                                                      |
| nbody                     | 87.0 ms                                                | 80.5 ms: 1.08x faster                                                       |
| mdp                       | 2.72 sec                                               | 2.52 sec: 1.08x faster                                                      |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 536 ms: 1.08x faster                                                        |
| scimark_monte_carlo       | 67.4 ms                                                | 62.7 ms: 1.08x faster                                                       |
| telco                     | 8.54 ms                                                | 7.95 ms: 1.08x faster                                                       |
| fannkuch                  | 404 ms                                                 | 380 ms: 1.06x faster                                                        |
| xml_etree_parse           | 156 ms                                                 | 147 ms: 1.06x faster                                                        |
| scimark_sor               | 124 ms                                                 | 117 ms: 1.06x faster                                                        |
| json                      | 5.36 ms                                                | 5.09 ms: 1.05x faster                                                       |
| async_tree_none_tg        | 321 ms                                                 | 307 ms: 1.04x faster                                                        |
| logging_format            | 6.40 us                                                | 6.14 us: 1.04x faster                                                       |
| xml_etree_iterparse       | 101 ms                                                 | 97.4 ms: 1.04x faster                                                       |
| json_dumps                | 10.6 ms                                                | 10.2 ms: 1.04x faster                                                       |
| pyflate                   | 471 ms                                                 | 457 ms: 1.03x faster                                                        |
| typing_runtime_protocols  | 165 us                                                 | 160 us: 1.03x faster                                                        |
| deltablue                 | 3.23 ms                                                | 3.14 ms: 1.03x faster                                                       |
| pickle_pure_python        | 310 us                                                 | 302 us: 1.03x faster                                                        |
| thrift                    | 809 us                                                 | 787 us: 1.03x faster                                                        |
| regex_effbot              | 3.73 ms                                                | 3.63 ms: 1.03x faster                                                       |
| logging_simple            | 5.72 us                                                | 5.57 us: 1.03x faster                                                       |
| scimark_lu                | 113 ms                                                 | 110 ms: 1.02x faster                                                        |
| meteor_contest            | 109 ms                                                 | 107 ms: 1.02x faster                                                        |
| regex_dna                 | 218 ms                                                 | 215 ms: 1.01x faster                                                        |
| unpickle_pure_python      | 216 us                                                 | 213 us: 1.01x faster                                                        |
| pprint_safe_repr          | 728 ms                                                 | 722 ms: 1.01x faster                                                        |
| pidigits                  | 186 ms                                                 | 186 ms: 1.00x faster                                                        |
| asyncio_websockets        | 552 ms                                                 | 555 ms: 1.01x slower                                                        |
| comprehensions            | 16.5 us                                                | 16.6 us: 1.01x slower                                                       |
| coverage                  | 84.0 ms                                                | 84.7 ms: 1.01x slower                                                       |
| logging_silent            | 102 ns                                                 | 103 ns: 1.02x slower                                                        |
| python_startup_no_site    | 6.96 ms                                                | 7.07 ms: 1.02x slower                                                       |
| tornado_http              | 92.4 ms                                                | 94.0 ms: 1.02x slower                                                       |
| coroutines                | 22.7 ms                                                | 23.1 ms: 1.02x slower                                                       |
| bench_thread_pool         | 822 us                                                 | 837 us: 1.02x slower                                                        |
| sqlglot_normalize         | 108 ms                                                 | 110 ms: 1.02x slower                                                        |
| django_template           | 35.2 ms                                                | 36.0 ms: 1.02x slower                                                       |
| raytrace                  | 267 ms                                                 | 275 ms: 1.03x slower                                                        |
| sqlglot_parse             | 1.27 ms                                                | 1.32 ms: 1.04x slower                                                       |
| regex_compile             | 132 ms                                                 | 137 ms: 1.04x slower                                                        |
| genshi_text               | 23.5 ms                                                | 24.4 ms: 1.04x slower                                                       |
| 2to3                      | 267 ms                                                 | 277 ms: 1.04x slower                                                        |
| dulwich_log               | 64.3 ms                                                | 67.3 ms: 1.05x slower                                                       |
| async_generators          | 436 ms                                                 | 458 ms: 1.05x slower                                                        |
| sqlglot_optimize          | 53.7 ms                                                | 56.5 ms: 1.05x slower                                                       |
| sqlglot_transpile         | 1.58 ms                                                | 1.70 ms: 1.07x slower                                                       |
| sympy_str                 | 275 ms                                                 | 297 ms: 1.08x slower                                                        |
| sympy_expand              | 463 ms                                                 | 502 ms: 1.08x slower                                                        |
| async_tree_io             | 842 ms                                                 | 929 ms: 1.10x slower                                                        |
| genshi_xml                | 50.9 ms                                                | 56.4 ms: 1.11x slower                                                       |
| nqueens                   | 78.4 ms                                                | 86.8 ms: 1.11x slower                                                       |
| hexiom                    | 6.16 ms                                                | 6.87 ms: 1.11x slower                                                       |
| generators                | 29.0 ms                                                | 32.4 ms: 1.12x slower                                                       |
| docutils                  | 2.59 sec                                               | 2.92 sec: 1.13x slower                                                      |
| sympy_sum                 | 150 ms                                                 | 171 ms: 1.14x slower                                                        |
| sympy_integrate           | 19.9 ms                                                | 22.7 ms: 1.14x slower                                                       |
| pylint                    | 313 ms                                                 | 360 ms: 1.15x slower                                                        |
| Geometric mean            | (ref)                                                  | 1.04x faster                                                                |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed_tg, pprint_pformat, json_loads, bench_mp_pool, chaos, async_tree_io_tg
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, html5lib, k_core, mypy2, pycparser, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240919-3.14.0a0-cae9e43-JIT/bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.041x faster
# HPT report

- Reliability score: 98.91% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x