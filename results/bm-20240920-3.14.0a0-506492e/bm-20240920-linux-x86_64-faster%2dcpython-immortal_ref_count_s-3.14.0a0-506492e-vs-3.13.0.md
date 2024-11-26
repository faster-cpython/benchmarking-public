# Results vs. 3.13.0

- fork: faster-cpython
- ref: immortal_ref_count_s
- machine: linux-x86_64
- commit hash: 506492e
- commit date: 2024-09-20
- overall geometric mean: 1.037x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-506492e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 254 ms: 1.05x faster                                                            |
| docutils       | 2.59 sec                                               | 2.65 sec: 1.02x slower                                                          |
| html5lib       | 64.2 ms                                                | 63.4 ms: 1.01x faster                                                           |
| tornado_http   | 92.4 ms                                                | 91.1 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-506492e |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 464 ms                                                 | 388 ms: 1.19x faster                                                            |
| async_tree_memoization    | 442 ms                                                 | 390 ms: 1.13x faster                                                            |
| async_tree_none           | 351 ms                                                 | 312 ms: 1.12x faster                                                            |
| async_tree_none_tg        | 321 ms                                                 | 306 ms: 1.05x faster                                                            |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 557 ms: 1.04x faster                                                            |
| async_generators          | 436 ms                                                 | 433 ms: 1.01x faster                                                            |
| asyncio_websockets        | 552 ms                                                 | 555 ms: 1.01x slower                                                            |
| async_tree_io_tg          | 857 ms                                                 | 875 ms: 1.02x slower                                                            |
| coroutines                | 22.7 ms                                                | 23.3 ms: 1.03x slower                                                           |
| Geometric mean            | (ref)                                                  | 1.04x faster                                                                    |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-506492e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 76.2 ms: 1.04x faster                                                           |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x slower                                                            |
| nbody          | 87.0 ms                                                | 87.7 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-506492e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.8 ms: 1.06x faster                                                           |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                            |
| regex_effbot   | 3.73 ms                                                | 3.66 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                    |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-506492e |
|---------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads         | 2.14 sec                                               | 2.06 sec: 1.04x faster                                                          |
| xml_etree_process   | 60.6 ms                                                | 58.5 ms: 1.04x faster                                                           |
| json_dumps          | 10.6 ms                                                | 10.3 ms: 1.03x faster                                                           |
| xml_etree_generate  | 86.7 ms                                                | 84.4 ms: 1.03x faster                                                           |
| json_loads          | 27.2 us                                                | 26.6 us: 1.02x faster                                                           |
| pickle_pure_python  | 310 us                                                 | 305 us: 1.02x faster                                                            |
| xml_etree_iterparse | 101 ms                                                 | 106 ms: 1.04x slower                                                            |
| Geometric mean      | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (2): unpickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-506492e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                           |
| python_startup_no_site | 6.96 ms                                                | 6.98 ms: 1.00x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-506492e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 23.5 ms                                                | 22.0 ms: 1.07x faster                                                           |
| django_template | 35.2 ms                                                | 34.4 ms: 1.02x faster                                                           |
| genshi_xml      | 50.9 ms                                                | 50.0 ms: 1.02x faster                                                           |
| mako            | 11.1 ms                                                | 11.1 ms: 1.00x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                                    |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-506492e |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| create_gc_cycles          | 2.41 ms                                                | 1.73 ms: 1.39x faster                                                           |
| deepcopy                  | 358 us                                                 | 259 us: 1.38x faster                                                            |
| deepcopy_memo             | 39.1 us                                                | 30.0 us: 1.30x faster                                                           |
| go                        | 144 ms                                                 | 118 ms: 1.22x faster                                                            |
| async_tree_memoization_tg | 464 ms                                                 | 388 ms: 1.19x faster                                                            |
| python_startup            | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                           |
| deepcopy_reduce           | 3.20 us                                                | 2.70 us: 1.18x faster                                                           |
| gc_traversal              | 4.37 ms                                                | 3.79 ms: 1.15x faster                                                           |
| async_tree_memoization    | 442 ms                                                 | 390 ms: 1.13x faster                                                            |
| async_tree_none           | 351 ms                                                 | 312 ms: 1.12x faster                                                            |
| pathlib                   | 17.5 ms                                                | 16.1 ms: 1.09x faster                                                           |
| json                      | 5.36 ms                                                | 4.95 ms: 1.08x faster                                                           |
| mdp                       | 2.72 sec                                               | 2.53 sec: 1.07x faster                                                          |
| genshi_text               | 23.5 ms                                                | 22.0 ms: 1.07x faster                                                           |
| richards                  | 48.7 ms                                                | 46.0 ms: 1.06x faster                                                           |
| regex_v8                  | 26.2 ms                                                | 24.8 ms: 1.06x faster                                                           |
| richards_super            | 54.9 ms                                                | 52.0 ms: 1.05x faster                                                           |
| 2to3                      | 267 ms                                                 | 254 ms: 1.05x faster                                                            |
| async_tree_none_tg        | 321 ms                                                 | 306 ms: 1.05x faster                                                            |
| thrift                    | 809 us                                                 | 773 us: 1.05x faster                                                            |
| tomli_loads               | 2.14 sec                                               | 2.06 sec: 1.04x faster                                                          |
| crypto_pyaes              | 75.3 ms                                                | 72.4 ms: 1.04x faster                                                           |
| float                     | 79.2 ms                                                | 76.2 ms: 1.04x faster                                                           |
| scimark_sparse_mat_mult   | 5.04 ms                                                | 4.85 ms: 1.04x faster                                                           |
| regex_compile             | 132 ms                                                 | 127 ms: 1.04x faster                                                            |
| xml_etree_process         | 60.6 ms                                                | 58.5 ms: 1.04x faster                                                           |
| typing_runtime_protocols  | 165 us                                                 | 159 us: 1.04x faster                                                            |
| bench_thread_pool         | 822 us                                                 | 792 us: 1.04x faster                                                            |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 557 ms: 1.04x faster                                                            |
| generators                | 29.0 ms                                                | 28.0 ms: 1.03x faster                                                           |
| pprint_safe_repr          | 728 ms                                                 | 707 ms: 1.03x faster                                                            |
| json_dumps                | 10.6 ms                                                | 10.3 ms: 1.03x faster                                                           |
| pprint_pformat            | 1.49 sec                                               | 1.45 sec: 1.03x faster                                                          |
| xml_etree_generate        | 86.7 ms                                                | 84.4 ms: 1.03x faster                                                           |
| logging_format            | 6.40 us                                                | 6.23 us: 1.03x faster                                                           |
| meteor_contest            | 109 ms                                                 | 106 ms: 1.03x faster                                                            |
| telco                     | 8.54 ms                                                | 8.32 ms: 1.03x faster                                                           |
| pycparser                 | 1.20 sec                                               | 1.17 sec: 1.02x faster                                                          |
| sympy_str                 | 275 ms                                                 | 269 ms: 1.02x faster                                                            |
| json_loads                | 27.2 us                                                | 26.6 us: 1.02x faster                                                           |
| sympy_integrate           | 19.9 ms                                                | 19.5 ms: 1.02x faster                                                           |
| django_template           | 35.2 ms                                                | 34.4 ms: 1.02x faster                                                           |
| spectral_norm             | 115 ms                                                 | 113 ms: 1.02x faster                                                            |
| sympy_sum                 | 150 ms                                                 | 148 ms: 1.02x faster                                                            |
| regex_effbot              | 3.73 ms                                                | 3.66 ms: 1.02x faster                                                           |
| pickle_pure_python        | 310 us                                                 | 305 us: 1.02x faster                                                            |
| raytrace                  | 267 ms                                                 | 262 ms: 1.02x faster                                                            |
| genshi_xml                | 50.9 ms                                                | 50.0 ms: 1.02x faster                                                           |
| tornado_http              | 92.4 ms                                                | 91.1 ms: 1.02x faster                                                           |
| logging_simple            | 5.72 us                                                | 5.64 us: 1.01x faster                                                           |
| html5lib                  | 64.2 ms                                                | 63.4 ms: 1.01x faster                                                           |
| deltablue                 | 3.23 ms                                                | 3.19 ms: 1.01x faster                                                           |
| sqlglot_normalize         | 108 ms                                                 | 106 ms: 1.01x faster                                                            |
| sqlglot_optimize          | 53.7 ms                                                | 53.2 ms: 1.01x faster                                                           |
| async_generators          | 436 ms                                                 | 433 ms: 1.01x faster                                                            |
| scimark_monte_carlo       | 67.4 ms                                                | 67.1 ms: 1.01x faster                                                           |
| sqlglot_transpile         | 1.58 ms                                                | 1.58 ms: 1.01x faster                                                           |
| pidigits                  | 186 ms                                                 | 186 ms: 1.00x slower                                                            |
| python_startup_no_site    | 6.96 ms                                                | 6.98 ms: 1.00x slower                                                           |
| mako                      | 11.1 ms                                                | 11.1 ms: 1.00x slower                                                           |
| asyncio_websockets        | 552 ms                                                 | 555 ms: 1.01x slower                                                            |
| comprehensions            | 16.5 us                                                | 16.6 us: 1.01x slower                                                           |
| hexiom                    | 6.16 ms                                                | 6.21 ms: 1.01x slower                                                           |
| pyflate                   | 471 ms                                                 | 474 ms: 1.01x slower                                                            |
| scimark_sor               | 124 ms                                                 | 124 ms: 1.01x slower                                                            |
| nbody                     | 87.0 ms                                                | 87.7 ms: 1.01x slower                                                           |
| bpe_tokeniser             | 4.75 sec                                               | 4.79 sec: 1.01x slower                                                          |
| scimark_fft               | 364 ms                                                 | 368 ms: 1.01x slower                                                            |
| dulwich_log               | 64.3 ms                                                | 65.2 ms: 1.01x slower                                                           |
| logging_silent            | 102 ns                                                 | 103 ns: 1.02x slower                                                            |
| scimark_lu                | 113 ms                                                 | 115 ms: 1.02x slower                                                            |
| chaos                     | 58.1 ms                                                | 59.0 ms: 1.02x slower                                                           |
| docutils                  | 2.59 sec                                               | 2.65 sec: 1.02x slower                                                          |
| async_tree_io_tg          | 857 ms                                                 | 875 ms: 1.02x slower                                                            |
| nqueens                   | 78.4 ms                                                | 80.3 ms: 1.02x slower                                                           |
| coroutines                | 22.7 ms                                                | 23.3 ms: 1.03x slower                                                           |
| coverage                  | 84.0 ms                                                | 87.1 ms: 1.04x slower                                                           |
| xml_etree_iterparse       | 101 ms                                                 | 106 ms: 1.04x slower                                                            |
| Geometric mean            | (ref)                                                  | 1.04x faster                                                                    |

Benchmark hidden because not significant (10): fannkuch, sympy_expand, bench_mp_pool, unpickle_pure_python, async_tree_cpu_io_mixed_tg, sqlglot_parse, xml_etree_parse, regex_dna, async_tree_io, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240920-3.14.0a0-506492e/bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-506492e.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.037x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x