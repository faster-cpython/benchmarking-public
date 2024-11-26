# Results vs. 3.13.0

- fork: brandtbucher
- ref: underflow_known
- machine: linux-x86_64
- commit hash: 8763a2d
- commit date: 2024-09-07
- overall geometric mean: 1.023x faster
- HPT reliability: 60.72%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 281 ms: 1.05x slower                                                   |
| docutils       | 2.59 sec                                               | 3.01 sec: 1.16x slower                                                 |
| html5lib       | 64.2 ms                                                | 61.9 ms: 1.04x faster                                                  |
| tornado_http   | 92.4 ms                                                | 96.8 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.05x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|---------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg | 464 ms                                                 | 402 ms: 1.15x faster                                                   |
| async_tree_memoization    | 442 ms                                                 | 396 ms: 1.12x faster                                                   |
| async_tree_none           | 351 ms                                                 | 327 ms: 1.07x faster                                                   |
| async_tree_none_tg        | 321 ms                                                 | 310 ms: 1.03x faster                                                   |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 563 ms: 1.02x faster                                                   |
| asyncio_websockets        | 552 ms                                                 | 556 ms: 1.01x slower                                                   |
| async_tree_io_tg          | 857 ms                                                 | 898 ms: 1.05x slower                                                   |
| async_generators          | 436 ms                                                 | 462 ms: 1.06x slower                                                   |
| async_tree_io             | 842 ms                                                 | 936 ms: 1.11x slower                                                   |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 70.1 ms: 1.13x faster                                                  |
| nbody          | 87.0 ms                                                | 80.4 ms: 1.08x faster                                                  |
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.4 ms: 1.07x faster                                                  |
| regex_effbot   | 3.73 ms                                                | 3.62 ms: 1.03x faster                                                  |
| regex_dna      | 218 ms                                                 | 213 ms: 1.03x faster                                                   |
| regex_compile  | 132 ms                                                 | 146 ms: 1.11x slower                                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_generate   | 86.7 ms                                                | 76.9 ms: 1.13x faster                                                  |
| xml_etree_process    | 60.6 ms                                                | 54.4 ms: 1.12x faster                                                  |
| unpickle_pure_python | 216 us                                                 | 198 us: 1.09x faster                                                   |
| tomli_loads          | 2.14 sec                                               | 1.96 sec: 1.09x faster                                                 |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.07x faster                                                   |
| xml_etree_iterparse  | 101 ms                                                 | 98.4 ms: 1.03x faster                                                  |
| json_dumps           | 10.6 ms                                                | 10.4 ms: 1.02x faster                                                  |
| json_loads           | 27.2 us                                                | 28.2 us: 1.04x slower                                                  |
| pickle_pure_python   | 310 us                                                 | 323 us: 1.04x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.7 ms: 1.17x faster                                                  |
| python_startup_no_site | 6.96 ms                                                | 7.17 ms: 1.03x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.72 ms: 1.14x faster                                                  |
| django_template | 35.2 ms                                                | 35.7 ms: 1.02x slower                                                  |
| genshi_text     | 23.5 ms                                                | 23.9 ms: 1.02x slower                                                  |
| genshi_xml      | 50.9 ms                                                | 54.1 ms: 1.06x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                           |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|---------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy_memo             | 39.1 us                                                | 25.2 us: 1.55x faster                                                  |
| create_gc_cycles          | 2.41 ms                                                | 1.75 ms: 1.37x faster                                                  |
| deepcopy                  | 358 us                                                 | 267 us: 1.34x faster                                                   |
| richards_super            | 54.9 ms                                                | 42.3 ms: 1.30x faster                                                  |
| richards                  | 48.7 ms                                                | 37.8 ms: 1.29x faster                                                  |
| gc_traversal              | 4.37 ms                                                | 3.59 ms: 1.22x faster                                                  |
| deepcopy_reduce           | 3.20 us                                                | 2.69 us: 1.19x faster                                                  |
| python_startup            | 12.5 ms                                                | 10.7 ms: 1.17x faster                                                  |
| async_tree_memoization_tg | 464 ms                                                 | 402 ms: 1.15x faster                                                   |
| scimark_fft               | 364 ms                                                 | 316 ms: 1.15x faster                                                   |
| mako                      | 11.1 ms                                                | 9.72 ms: 1.14x faster                                                  |
| spectral_norm             | 115 ms                                                 | 101 ms: 1.14x faster                                                   |
| crypto_pyaes              | 75.3 ms                                                | 66.5 ms: 1.13x faster                                                  |
| float                     | 79.2 ms                                                | 70.1 ms: 1.13x faster                                                  |
| xml_etree_generate        | 86.7 ms                                                | 76.9 ms: 1.13x faster                                                  |
| scimark_sparse_mat_mult   | 5.04 ms                                                | 4.49 ms: 1.12x faster                                                  |
| async_tree_memoization    | 442 ms                                                 | 396 ms: 1.12x faster                                                   |
| xml_etree_process         | 60.6 ms                                                | 54.4 ms: 1.12x faster                                                  |
| pathlib                   | 17.5 ms                                                | 15.7 ms: 1.11x faster                                                  |
| unpickle_pure_python      | 216 us                                                 | 198 us: 1.09x faster                                                   |
| tomli_loads               | 2.14 sec                                               | 1.96 sec: 1.09x faster                                                 |
| fannkuch                  | 404 ms                                                 | 373 ms: 1.08x faster                                                   |
| nbody                     | 87.0 ms                                                | 80.4 ms: 1.08x faster                                                  |
| async_tree_none           | 351 ms                                                 | 327 ms: 1.07x faster                                                   |
| regex_v8                  | 26.2 ms                                                | 24.4 ms: 1.07x faster                                                  |
| telco                     | 8.54 ms                                                | 7.97 ms: 1.07x faster                                                  |
| xml_etree_parse           | 156 ms                                                 | 146 ms: 1.07x faster                                                   |
| mdp                       | 2.72 sec                                               | 2.55 sec: 1.07x faster                                                 |
| bpe_tokeniser             | 4.75 sec                                               | 4.48 sec: 1.06x faster                                                 |
| scimark_sor               | 124 ms                                                 | 117 ms: 1.06x faster                                                   |
| thrift                    | 809 us                                                 | 771 us: 1.05x faster                                                   |
| go                        | 144 ms                                                 | 139 ms: 1.04x faster                                                   |
| html5lib                  | 64.2 ms                                                | 61.9 ms: 1.04x faster                                                  |
| async_tree_none_tg        | 321 ms                                                 | 310 ms: 1.03x faster                                                   |
| pyflate                   | 471 ms                                                 | 455 ms: 1.03x faster                                                   |
| deltablue                 | 3.23 ms                                                | 3.12 ms: 1.03x faster                                                  |
| regex_effbot              | 3.73 ms                                                | 3.62 ms: 1.03x faster                                                  |
| logging_format            | 6.40 us                                                | 6.22 us: 1.03x faster                                                  |
| xml_etree_iterparse       | 101 ms                                                 | 98.4 ms: 1.03x faster                                                  |
| regex_dna                 | 218 ms                                                 | 213 ms: 1.03x faster                                                   |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 563 ms: 1.02x faster                                                   |
| scimark_lu                | 113 ms                                                 | 110 ms: 1.02x faster                                                   |
| json_dumps                | 10.6 ms                                                | 10.4 ms: 1.02x faster                                                  |
| logging_simple            | 5.72 us                                                | 5.67 us: 1.01x faster                                                  |
| logging_silent            | 102 ns                                                 | 101 ns: 1.01x faster                                                   |
| pidigits                  | 186 ms                                                 | 187 ms: 1.01x slower                                                   |
| comprehensions            | 16.5 us                                                | 16.6 us: 1.01x slower                                                  |
| asyncio_websockets        | 552 ms                                                 | 556 ms: 1.01x slower                                                   |
| bench_thread_pool         | 822 us                                                 | 835 us: 1.02x slower                                                   |
| django_template           | 35.2 ms                                                | 35.7 ms: 1.02x slower                                                  |
| coverage                  | 84.0 ms                                                | 85.4 ms: 1.02x slower                                                  |
| genshi_text               | 23.5 ms                                                | 23.9 ms: 1.02x slower                                                  |
| pycparser                 | 1.20 sec                                               | 1.24 sec: 1.03x slower                                                 |
| python_startup_no_site    | 6.96 ms                                                | 7.17 ms: 1.03x slower                                                  |
| pprint_safe_repr          | 728 ms                                                 | 751 ms: 1.03x slower                                                   |
| pprint_pformat            | 1.49 sec                                               | 1.55 sec: 1.03x slower                                                 |
| json_loads                | 27.2 us                                                | 28.2 us: 1.04x slower                                                  |
| pickle_pure_python        | 310 us                                                 | 323 us: 1.04x slower                                                   |
| tornado_http              | 92.4 ms                                                | 96.8 ms: 1.05x slower                                                  |
| async_tree_io_tg          | 857 ms                                                 | 898 ms: 1.05x slower                                                   |
| sqlglot_normalize         | 108 ms                                                 | 113 ms: 1.05x slower                                                   |
| 2to3                      | 267 ms                                                 | 281 ms: 1.05x slower                                                   |
| raytrace                  | 267 ms                                                 | 283 ms: 1.06x slower                                                   |
| async_generators          | 436 ms                                                 | 462 ms: 1.06x slower                                                   |
| chaos                     | 58.1 ms                                                | 61.6 ms: 1.06x slower                                                  |
| genshi_xml                | 50.9 ms                                                | 54.1 ms: 1.06x slower                                                  |
| sqlglot_transpile         | 1.58 ms                                                | 1.70 ms: 1.07x slower                                                  |
| sqlglot_parse             | 1.27 ms                                                | 1.38 ms: 1.08x slower                                                  |
| sqlglot_optimize          | 53.7 ms                                                | 58.7 ms: 1.09x slower                                                  |
| sympy_expand              | 463 ms                                                 | 508 ms: 1.10x slower                                                   |
| nqueens                   | 78.4 ms                                                | 86.2 ms: 1.10x slower                                                  |
| dulwich_log               | 64.3 ms                                                | 70.8 ms: 1.10x slower                                                  |
| regex_compile             | 132 ms                                                 | 146 ms: 1.11x slower                                                   |
| async_tree_io             | 842 ms                                                 | 936 ms: 1.11x slower                                                   |
| sympy_str                 | 275 ms                                                 | 306 ms: 1.11x slower                                                   |
| generators                | 29.0 ms                                                | 33.1 ms: 1.14x slower                                                  |
| scimark_monte_carlo       | 67.4 ms                                                | 77.3 ms: 1.15x slower                                                  |
| sympy_integrate           | 19.9 ms                                                | 23.0 ms: 1.16x slower                                                  |
| docutils                  | 2.59 sec                                               | 3.01 sec: 1.16x slower                                                 |
| sympy_sum                 | 150 ms                                                 | 179 ms: 1.19x slower                                                   |
| pylint                    | 313 ms                                                 | 373 ms: 1.19x slower                                                   |
| hexiom                    | 6.16 ms                                                | 7.72 ms: 1.25x slower                                                  |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed_tg, coroutines, meteor_contest, bench_mp_pool, typing_runtime_protocols, json
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240907-3.14.0a0-8763a2d-JIT/bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.023x faster
# HPT report

- Reliability score: 60.72% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x