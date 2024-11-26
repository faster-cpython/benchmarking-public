# Results vs. 3.13.0

- fork: faster-cpython
- ref: load_fast_can_be_def
- machine: linux-x86_64
- commit hash: cb9433d
- commit date: 2024-10-04
- overall geometric mean: 1.030x faster
- HPT reliability: 98.81%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 257 ms: 1.04x faster                                                            |
| docutils       | 2.59 sec                                               | 2.64 sec: 1.02x slower                                                          |
| html5lib       | 64.2 ms                                                | 62.2 ms: 1.03x faster                                                           |
| tornado_http   | 92.4 ms                                                | 91.7 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 464 ms                                                 | 386 ms: 1.20x faster                                                            |
| async_tree_memoization    | 442 ms                                                 | 392 ms: 1.13x faster                                                            |
| async_tree_none           | 351 ms                                                 | 312 ms: 1.12x faster                                                            |
| async_tree_none_tg        | 321 ms                                                 | 304 ms: 1.05x faster                                                            |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 562 ms: 1.03x faster                                                            |
| coroutines                | 22.7 ms                                                | 22.4 ms: 1.01x faster                                                           |
| async_generators          | 436 ms                                                 | 433 ms: 1.01x faster                                                            |
| asyncio_websockets        | 552 ms                                                 | 557 ms: 1.01x slower                                                            |
| async_tree_io             | 842 ms                                                 | 874 ms: 1.04x slower                                                            |
| Geometric mean            | (ref)                                                  | 1.04x faster                                                                    |

Benchmark hidden because not significant (2): async_tree_io_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 77.1 ms: 1.03x faster                                                           |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                            |
| nbody          | 87.0 ms                                                | 88.0 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 25.3 ms: 1.04x faster                                                           |
| regex_compile  | 132 ms                                                 | 131 ms: 1.01x faster                                                            |
| regex_effbot   | 3.73 ms                                                | 3.75 ms: 1.01x slower                                                           |
| regex_dna      | 218 ms                                                 | 223 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|---------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps          | 10.6 ms                                                | 10.2 ms: 1.04x faster                                                           |
| xml_etree_process   | 60.6 ms                                                | 59.3 ms: 1.02x faster                                                           |
| tomli_loads         | 2.14 sec                                               | 2.10 sec: 1.02x faster                                                          |
| pickle_pure_python  | 310 us                                                 | 308 us: 1.01x faster                                                            |
| json_loads          | 27.2 us                                                | 27.1 us: 1.01x faster                                                           |
| xml_etree_generate  | 86.7 ms                                                | 86.3 ms: 1.00x faster                                                           |
| xml_etree_iterparse | 101 ms                                                 | 104 ms: 1.03x slower                                                            |
| Geometric mean      | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (2): xml_etree_parse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                           |
| python_startup_no_site | 6.96 ms                                                | 6.99 ms: 1.00x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 23.5 ms                                                | 22.7 ms: 1.04x faster                                                           |
| django_template | 35.2 ms                                                | 34.5 ms: 1.02x faster                                                           |
| genshi_xml      | 50.9 ms                                                | 50.5 ms: 1.01x faster                                                           |
| mako            | 11.1 ms                                                | 11.3 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                                    |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| create_gc_cycles          | 2.41 ms                                                | 1.71 ms: 1.41x faster                                                           |
| deepcopy                  | 358 us                                                 | 262 us: 1.37x faster                                                            |
| deepcopy_memo             | 39.1 us                                                | 30.3 us: 1.29x faster                                                           |
| go                        | 144 ms                                                 | 120 ms: 1.20x faster                                                            |
| async_tree_memoization_tg | 464 ms                                                 | 386 ms: 1.20x faster                                                            |
| python_startup            | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                           |
| gc_traversal              | 4.37 ms                                                | 3.72 ms: 1.18x faster                                                           |
| deepcopy_reduce           | 3.20 us                                                | 2.75 us: 1.16x faster                                                           |
| async_tree_memoization    | 442 ms                                                 | 392 ms: 1.13x faster                                                            |
| async_tree_none           | 351 ms                                                 | 312 ms: 1.12x faster                                                            |
| pathlib                   | 17.5 ms                                                | 15.9 ms: 1.11x faster                                                           |
| mdp                       | 2.72 sec                                               | 2.51 sec: 1.08x faster                                                          |
| telco                     | 8.54 ms                                                | 8.00 ms: 1.07x faster                                                           |
| thrift                    | 809 us                                                 | 763 us: 1.06x faster                                                            |
| async_tree_none_tg        | 321 ms                                                 | 304 ms: 1.05x faster                                                            |
| json                      | 5.36 ms                                                | 5.11 ms: 1.05x faster                                                           |
| crypto_pyaes              | 75.3 ms                                                | 72.3 ms: 1.04x faster                                                           |
| generators                | 29.0 ms                                                | 27.8 ms: 1.04x faster                                                           |
| json_dumps                | 10.6 ms                                                | 10.2 ms: 1.04x faster                                                           |
| pycparser                 | 1.20 sec                                               | 1.16 sec: 1.04x faster                                                          |
| genshi_text               | 23.5 ms                                                | 22.7 ms: 1.04x faster                                                           |
| richards                  | 48.7 ms                                                | 46.9 ms: 1.04x faster                                                           |
| regex_v8                  | 26.2 ms                                                | 25.3 ms: 1.04x faster                                                           |
| 2to3                      | 267 ms                                                 | 257 ms: 1.04x faster                                                            |
| html5lib                  | 64.2 ms                                                | 62.2 ms: 1.03x faster                                                           |
| richards_super            | 54.9 ms                                                | 53.2 ms: 1.03x faster                                                           |
| float                     | 79.2 ms                                                | 77.1 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 562 ms: 1.03x faster                                                            |
| xml_etree_process         | 60.6 ms                                                | 59.3 ms: 1.02x faster                                                           |
| django_template           | 35.2 ms                                                | 34.5 ms: 1.02x faster                                                           |
| tomli_loads               | 2.14 sec                                               | 2.10 sec: 1.02x faster                                                          |
| pprint_safe_repr          | 728 ms                                                 | 716 ms: 1.02x faster                                                            |
| logging_format            | 6.40 us                                                | 6.30 us: 1.01x faster                                                           |
| sympy_str                 | 275 ms                                                 | 271 ms: 1.01x faster                                                            |
| sympy_sum                 | 150 ms                                                 | 148 ms: 1.01x faster                                                            |
| coroutines                | 22.7 ms                                                | 22.4 ms: 1.01x faster                                                           |
| pprint_pformat            | 1.49 sec                                               | 1.48 sec: 1.01x faster                                                          |
| genshi_xml                | 50.9 ms                                                | 50.5 ms: 1.01x faster                                                           |
| typing_runtime_protocols  | 165 us                                                 | 163 us: 1.01x faster                                                            |
| regex_compile             | 132 ms                                                 | 131 ms: 1.01x faster                                                            |
| pickle_pure_python        | 310 us                                                 | 308 us: 1.01x faster                                                            |
| tornado_http              | 92.4 ms                                                | 91.7 ms: 1.01x faster                                                           |
| async_generators          | 436 ms                                                 | 433 ms: 1.01x faster                                                            |
| json_loads                | 27.2 us                                                | 27.1 us: 1.01x faster                                                           |
| logging_simple            | 5.72 us                                                | 5.69 us: 1.01x faster                                                           |
| xml_etree_generate        | 86.7 ms                                                | 86.3 ms: 1.00x faster                                                           |
| spectral_norm             | 115 ms                                                 | 115 ms: 1.00x faster                                                            |
| sqlglot_transpile         | 1.58 ms                                                | 1.58 ms: 1.00x faster                                                           |
| sympy_integrate           | 19.9 ms                                                | 20.0 ms: 1.00x slower                                                           |
| pidigits                  | 186 ms                                                 | 187 ms: 1.00x slower                                                            |
| python_startup_no_site    | 6.96 ms                                                | 6.99 ms: 1.00x slower                                                           |
| regex_effbot              | 3.73 ms                                                | 3.75 ms: 1.01x slower                                                           |
| sqlglot_parse             | 1.27 ms                                                | 1.28 ms: 1.01x slower                                                           |
| scimark_sparse_mat_mult   | 5.04 ms                                                | 5.08 ms: 1.01x slower                                                           |
| comprehensions            | 16.5 us                                                | 16.6 us: 1.01x slower                                                           |
| scimark_lu                | 113 ms                                                 | 114 ms: 1.01x slower                                                            |
| asyncio_websockets        | 552 ms                                                 | 557 ms: 1.01x slower                                                            |
| scimark_fft               | 364 ms                                                 | 368 ms: 1.01x slower                                                            |
| nbody                     | 87.0 ms                                                | 88.0 ms: 1.01x slower                                                           |
| scimark_monte_carlo       | 67.4 ms                                                | 68.3 ms: 1.01x slower                                                           |
| pyflate                   | 471 ms                                                 | 477 ms: 1.01x slower                                                            |
| meteor_contest            | 109 ms                                                 | 111 ms: 1.02x slower                                                            |
| deltablue                 | 3.23 ms                                                | 3.28 ms: 1.02x slower                                                           |
| dulwich_log               | 64.3 ms                                                | 65.5 ms: 1.02x slower                                                           |
| bpe_tokeniser             | 4.75 sec                                               | 4.83 sec: 1.02x slower                                                          |
| coverage                  | 84.0 ms                                                | 85.6 ms: 1.02x slower                                                           |
| docutils                  | 2.59 sec                                               | 2.64 sec: 1.02x slower                                                          |
| regex_dna                 | 218 ms                                                 | 223 ms: 1.02x slower                                                            |
| hexiom                    | 6.16 ms                                                | 6.29 ms: 1.02x slower                                                           |
| logging_silent            | 102 ns                                                 | 104 ns: 1.02x slower                                                            |
| mako                      | 11.1 ms                                                | 11.3 ms: 1.02x slower                                                           |
| scimark_sor               | 124 ms                                                 | 127 ms: 1.03x slower                                                            |
| xml_etree_iterparse       | 101 ms                                                 | 104 ms: 1.03x slower                                                            |
| bench_thread_pool         | 822 us                                                 | 850 us: 1.03x slower                                                            |
| async_tree_io             | 842 ms                                                 | 874 ms: 1.04x slower                                                            |
| nqueens                   | 78.4 ms                                                | 81.5 ms: 1.04x slower                                                           |
| chaos                     | 58.1 ms                                                | 61.7 ms: 1.06x slower                                                           |
| bench_mp_pool             | 24.0 ms                                                | 56.1 ms: 2.34x slower                                                           |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (10): sympy_expand, xml_etree_parse, fannkuch, sqlglot_optimize, unpickle_pure_python, raytrace, sqlglot_normalize, async_tree_io_tg, async_tree_cpu_io_mixed_tg, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241004-3.14.0a0-cb9433d/bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.030x faster
# HPT report

- Reliability score: 98.81% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x