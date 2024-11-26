# Results vs. 3.13.0

- fork: brandtbucher
- ref: underflow_known_dyna
- machine: linux-x86_64
- commit hash: e666b14
- commit date: 2024-09-08
- overall geometric mean: 1.007x faster
- HPT reliability: 65.26%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 288 ms: 1.08x slower                                                        |
| docutils       | 2.59 sec                                               | 3.23 sec: 1.25x slower                                                      |
| html5lib       | 64.2 ms                                                | 67.7 ms: 1.06x slower                                                       |
| tornado_http   | 92.4 ms                                                | 104 ms: 1.12x slower                                                        |
| Geometric mean | (ref)                                                  | 1.12x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg | 464 ms                                                 | 412 ms: 1.13x faster                                                        |
| async_tree_none           | 351 ms                                                 | 326 ms: 1.08x faster                                                        |
| async_tree_memoization    | 442 ms                                                 | 416 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 561 ms: 1.03x faster                                                        |
| asyncio_websockets        | 552 ms                                                 | 554 ms: 1.00x slower                                                        |
| coroutines                | 22.7 ms                                                | 22.8 ms: 1.01x slower                                                       |
| async_generators          | 436 ms                                                 | 452 ms: 1.04x slower                                                        |
| async_tree_io_tg          | 857 ms                                                 | 910 ms: 1.06x slower                                                        |
| async_tree_io             | 842 ms                                                 | 938 ms: 1.11x slower                                                        |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (2): async_tree_none_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 71.4 ms: 1.11x faster                                                       |
| nbody          | 87.0 ms                                                | 80.7 ms: 1.08x faster                                                       |
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.73 ms                                                | 3.59 ms: 1.04x faster                                                       |
| regex_v8       | 26.2 ms                                                | 25.3 ms: 1.03x faster                                                       |
| regex_dna      | 218 ms                                                 | 212 ms: 1.03x faster                                                        |
| regex_compile  | 132 ms                                                 | 154 ms: 1.16x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_process    | 60.6 ms                                                | 53.9 ms: 1.13x faster                                                       |
| xml_etree_generate   | 86.7 ms                                                | 77.2 ms: 1.12x faster                                                       |
| unpickle_pure_python | 216 us                                                 | 201 us: 1.07x faster                                                        |
| xml_etree_parse      | 156 ms                                                 | 145 ms: 1.07x faster                                                        |
| tomli_loads          | 2.14 sec                                               | 2.07 sec: 1.03x faster                                                      |
| xml_etree_iterparse  | 101 ms                                                 | 98.3 ms: 1.03x faster                                                       |
| json_dumps           | 10.6 ms                                                | 10.3 ms: 1.03x faster                                                       |
| pickle_pure_python   | 310 us                                                 | 330 us: 1.06x slower                                                        |
| json_loads           | 27.2 us                                                | 28.9 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.6 ms: 1.17x faster                                                       |
| python_startup_no_site | 6.96 ms                                                | 7.17 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.75 ms: 1.14x faster                                                       |
| genshi_text     | 23.5 ms                                                | 22.8 ms: 1.03x faster                                                       |
| django_template | 35.2 ms                                                | 37.8 ms: 1.07x slower                                                       |
| genshi_xml      | 50.9 ms                                                | 58.7 ms: 1.15x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                                |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo             | 39.1 us                                                | 25.2 us: 1.55x faster                                                       |
| create_gc_cycles          | 2.41 ms                                                | 1.77 ms: 1.36x faster                                                       |
| deepcopy                  | 358 us                                                 | 267 us: 1.34x faster                                                        |
| richards_super            | 54.9 ms                                                | 44.3 ms: 1.24x faster                                                       |
| richards                  | 48.7 ms                                                | 39.4 ms: 1.23x faster                                                       |
| deepcopy_reduce           | 3.20 us                                                | 2.71 us: 1.18x faster                                                       |
| python_startup            | 12.5 ms                                                | 10.6 ms: 1.17x faster                                                       |
| scimark_fft               | 364 ms                                                 | 311 ms: 1.17x faster                                                        |
| gc_traversal              | 4.37 ms                                                | 3.77 ms: 1.16x faster                                                       |
| spectral_norm             | 115 ms                                                 | 100 ms: 1.15x faster                                                        |
| scimark_sparse_mat_mult   | 5.04 ms                                                | 4.41 ms: 1.14x faster                                                       |
| mako                      | 11.1 ms                                                | 9.75 ms: 1.14x faster                                                       |
| crypto_pyaes              | 75.3 ms                                                | 66.5 ms: 1.13x faster                                                       |
| xml_etree_process         | 60.6 ms                                                | 53.9 ms: 1.13x faster                                                       |
| async_tree_memoization_tg | 464 ms                                                 | 412 ms: 1.13x faster                                                        |
| xml_etree_generate        | 86.7 ms                                                | 77.2 ms: 1.12x faster                                                       |
| float                     | 79.2 ms                                                | 71.4 ms: 1.11x faster                                                       |
| pathlib                   | 17.5 ms                                                | 15.9 ms: 1.10x faster                                                       |
| fannkuch                  | 404 ms                                                 | 373 ms: 1.08x faster                                                        |
| nbody                     | 87.0 ms                                                | 80.7 ms: 1.08x faster                                                       |
| async_tree_none           | 351 ms                                                 | 326 ms: 1.08x faster                                                        |
| unpickle_pure_python      | 216 us                                                 | 201 us: 1.07x faster                                                        |
| mdp                       | 2.72 sec                                               | 2.54 sec: 1.07x faster                                                      |
| xml_etree_parse           | 156 ms                                                 | 145 ms: 1.07x faster                                                        |
| telco                     | 8.54 ms                                                | 8.02 ms: 1.07x faster                                                       |
| async_tree_memoization    | 442 ms                                                 | 416 ms: 1.06x faster                                                        |
| go                        | 144 ms                                                 | 135 ms: 1.06x faster                                                        |
| bpe_tokeniser             | 4.75 sec                                               | 4.55 sec: 1.04x faster                                                      |
| regex_effbot              | 3.73 ms                                                | 3.59 ms: 1.04x faster                                                       |
| regex_v8                  | 26.2 ms                                                | 25.3 ms: 1.03x faster                                                       |
| thrift                    | 809 us                                                 | 782 us: 1.03x faster                                                        |
| tomli_loads               | 2.14 sec                                               | 2.07 sec: 1.03x faster                                                      |
| genshi_text               | 23.5 ms                                                | 22.8 ms: 1.03x faster                                                       |
| regex_dna                 | 218 ms                                                 | 212 ms: 1.03x faster                                                        |
| meteor_contest            | 109 ms                                                 | 106 ms: 1.03x faster                                                        |
| xml_etree_iterparse       | 101 ms                                                 | 98.3 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 561 ms: 1.03x faster                                                        |
| pyflate                   | 471 ms                                                 | 458 ms: 1.03x faster                                                        |
| json_dumps                | 10.6 ms                                                | 10.3 ms: 1.03x faster                                                       |
| scimark_sor               | 124 ms                                                 | 121 ms: 1.02x faster                                                        |
| scimark_lu                | 113 ms                                                 | 111 ms: 1.02x faster                                                        |
| chaos                     | 58.1 ms                                                | 57.5 ms: 1.01x faster                                                       |
| asyncio_websockets        | 552 ms                                                 | 554 ms: 1.00x slower                                                        |
| pidigits                  | 186 ms                                                 | 187 ms: 1.01x slower                                                        |
| coroutines                | 22.7 ms                                                | 22.8 ms: 1.01x slower                                                       |
| coverage                  | 84.0 ms                                                | 85.2 ms: 1.01x slower                                                       |
| deltablue                 | 3.23 ms                                                | 3.28 ms: 1.02x slower                                                       |
| bench_thread_pool         | 822 us                                                 | 837 us: 1.02x slower                                                        |
| typing_runtime_protocols  | 165 us                                                 | 168 us: 1.02x slower                                                        |
| pprint_safe_repr          | 728 ms                                                 | 746 ms: 1.02x slower                                                        |
| logging_simple            | 5.72 us                                                | 5.89 us: 1.03x slower                                                       |
| python_startup_no_site    | 6.96 ms                                                | 7.17 ms: 1.03x slower                                                       |
| async_generators          | 436 ms                                                 | 452 ms: 1.04x slower                                                        |
| html5lib                  | 64.2 ms                                                | 67.7 ms: 1.06x slower                                                       |
| scimark_monte_carlo       | 67.4 ms                                                | 71.4 ms: 1.06x slower                                                       |
| pickle_pure_python        | 310 us                                                 | 330 us: 1.06x slower                                                        |
| json_loads                | 27.2 us                                                | 28.9 us: 1.06x slower                                                       |
| async_tree_io_tg          | 857 ms                                                 | 910 ms: 1.06x slower                                                        |
| raytrace                  | 267 ms                                                 | 284 ms: 1.06x slower                                                        |
| nqueens                   | 78.4 ms                                                | 84.0 ms: 1.07x slower                                                       |
| django_template           | 35.2 ms                                                | 37.8 ms: 1.07x slower                                                       |
| logging_silent            | 102 ns                                                 | 109 ns: 1.08x slower                                                        |
| 2to3                      | 267 ms                                                 | 288 ms: 1.08x slower                                                        |
| pycparser                 | 1.20 sec                                               | 1.32 sec: 1.10x slower                                                      |
| sqlglot_transpile         | 1.58 ms                                                | 1.75 ms: 1.10x slower                                                       |
| async_tree_io             | 842 ms                                                 | 938 ms: 1.11x slower                                                        |
| tornado_http              | 92.4 ms                                                | 104 ms: 1.12x slower                                                        |
| sqlglot_normalize         | 108 ms                                                 | 121 ms: 1.13x slower                                                        |
| sqlglot_optimize          | 53.7 ms                                                | 61.6 ms: 1.15x slower                                                       |
| generators                | 29.0 ms                                                | 33.2 ms: 1.15x slower                                                       |
| sympy_expand              | 463 ms                                                 | 533 ms: 1.15x slower                                                        |
| genshi_xml                | 50.9 ms                                                | 58.7 ms: 1.15x slower                                                       |
| regex_compile             | 132 ms                                                 | 154 ms: 1.16x slower                                                        |
| sympy_str                 | 275 ms                                                 | 322 ms: 1.17x slower                                                        |
| dulwich_log               | 64.3 ms                                                | 75.4 ms: 1.17x slower                                                       |
| sqlglot_parse             | 1.27 ms                                                | 1.49 ms: 1.17x slower                                                       |
| hexiom                    | 6.16 ms                                                | 7.42 ms: 1.20x slower                                                       |
| docutils                  | 2.59 sec                                               | 3.23 sec: 1.25x slower                                                      |
| sympy_integrate           | 19.9 ms                                                | 24.9 ms: 1.25x slower                                                       |
| sympy_sum                 | 150 ms                                                 | 190 ms: 1.26x slower                                                        |
| pylint                    | 313 ms                                                 | 412 ms: 1.32x slower                                                        |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (7): async_tree_none_tg, logging_format, bench_mp_pool, json, async_tree_cpu_io_mixed_tg, comprehensions, pprint_pformat
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240908-3.14.0a0-e666b14-JIT/bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.007x faster
# HPT report

- Reliability score: 65.26% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.03x